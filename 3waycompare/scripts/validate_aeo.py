#!/usr/bin/env python3
"""
AEO/SEO Validation Script for 3waycompare Output
Validates that generated comparisons meet AEO requirements
"""

import re
import sys
from pathlib import Path


def count_words(text):
    """Count words in a text string"""
    return len(text.split())


def validate_tldr(content):
    """Validate TL;DR section meets requirements"""
    tldr_match = re.search(r'### TL;DR Verdict\n\n(.+?)\n\n', content, re.DOTALL)
    if not tldr_match:
        return False, "TL;DR section not found"

    tldr_text = tldr_match.group(1).strip()
    word_count = count_words(tldr_text)

    if 50 <= word_count <= 58:
        return True, f"✅ TL;DR: {word_count} words (target: 50-58)"
    else:
        return False, f"❌ TL;DR: {word_count} words (target: 50-58)"


def validate_faq_answers(content):
    """Validate FAQ answers are 40-60 words"""
    faq_section = re.search(r'## Frequently Asked Questions(.+?)(?=## |$)', content, re.DOTALL)
    if not faq_section:
        return False, "FAQ section not found"

    # Find all FAQ answers (text between questions)
    questions = re.findall(r'### (.+?)\n\n(.+?)(?=\n\n###|\Z)', faq_section.group(1), re.DOTALL)

    valid_count = 0
    total_count = len(questions)
    issues = []

    for question, answer in questions:
        # Remove evidence citations for word count
        clean_answer = re.sub(r'\[Evidence:.*?\]', '', answer).strip()
        word_count = count_words(clean_answer)

        if 40 <= word_count <= 60:
            valid_count += 1
        else:
            issues.append(f"  - '{question[:50]}...': {word_count} words")

    if valid_count == total_count:
        return True, f"✅ FAQ: All {total_count} answers are 40-60 words"
    else:
        return False, f"❌ FAQ: {valid_count}/{total_count} answers are 40-60 words\n" + "\n".join(issues[:5])


def validate_readability(content):
    """Check for readability indicators"""
    # Count average sentence length
    sentences = re.split(r'[.!?]+', content)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]

    if not sentences:
        return False, "No sentences found"

    total_words = sum(count_words(s) for s in sentences[:100])  # Sample first 100 sentences
    avg_sentence_length = total_words / min(len(sentences), 100)

    if avg_sentence_length <= 20:
        return True, f"✅ Readability: Avg sentence length {avg_sentence_length:.1f} words (target: <20)"
    else:
        return False, f"⚠️ Readability: Avg sentence length {avg_sentence_length:.1f} words (target: <20)"


def validate_extractable_summaries(content):
    """Check for extractable summary blocks"""
    summaries = re.findall(r'\*\*(?:Quick Summary|Extractable Summary)\*\*.*?:(.+?)(?=\n\n|\Z)', content, re.DOTALL)

    valid_count = 0
    for summary in summaries:
        word_count = count_words(summary.strip())
        if 40 <= word_count <= 60:
            valid_count += 1

    if len(summaries) == 0:
        return False, "❌ No extractable summaries found"
    elif valid_count == len(summaries):
        return True, f"✅ Extractable summaries: All {len(summaries)} are 40-60 words"
    else:
        return False, f"⚠️ Extractable summaries: {valid_count}/{len(summaries)} are 40-60 words"


def validate_questions(content):
    """Check if real user questions are used"""
    generic_indicators = ["What is", "How does", "Can I", "Does it"]
    real_indicators = ["investigate anomalies", "root cause", "Excel", "hidden fees", "consultants", "TCO"]

    faq_section = re.search(r'## Frequently Asked Questions(.+?)(?=## |$)', content, re.DOTALL)
    if not faq_section:
        return False, "FAQ section not found"

    questions = re.findall(r'### (.+?)\n', faq_section.group(1))

    real_count = sum(1 for q in questions if any(ind in q for ind in real_indicators))

    if real_count >= 8:
        return True, f"✅ Questions: {real_count}/{len(questions)} are real user queries"
    else:
        return False, f"⚠️ Questions: Only {real_count}/{len(questions)} are real user queries"


def validate_file(filepath):
    """Validate a single comparison file"""
    print(f"\n{'='*60}")
    print(f"Validating: {filepath.name}")
    print('='*60)

    try:
        content = filepath.read_text()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False

    results = []
    all_valid = True

    # Run all validations
    validations = [
        ("TL;DR Word Count", validate_tldr),
        ("FAQ Word Counts", validate_faq_answers),
        ("Readability", validate_readability),
        ("Extractable Summaries", validate_extractable_summaries),
        ("Question Quality", validate_questions)
    ]

    for name, validator in validations:
        try:
            is_valid, message = validator(content)
            results.append(message)
            if not is_valid:
                all_valid = False
        except Exception as e:
            results.append(f"❌ {name}: Error - {e}")
            all_valid = False

    # Print results
    for result in results:
        print(result)

    # Overall score
    print("\n" + "="*60)
    if all_valid:
        print("✅ PASSED: All AEO requirements met")
    else:
        print("❌ FAILED: Some AEO requirements not met")

    return all_valid


def main():
    """Main validation function"""
    if len(sys.argv) > 1:
        # Validate specific file
        filepath = Path(sys.argv[1])
        if not filepath.exists():
            print(f"Error: File {filepath} not found")
            sys.exit(1)

        valid = validate_file(filepath)
        sys.exit(0 if valid else 1)
    else:
        # Validate all files in output directory
        output_dir = Path("output")
        if not output_dir.exists():
            print("Error: output directory not found")
            sys.exit(1)

        files = list(output_dir.glob("*-vs-*-ai.md"))
        if not files:
            print("No comparison files found in output directory")
            sys.exit(1)

        all_valid = True
        for filepath in files:
            if not validate_file(filepath):
                all_valid = False

        print("\n" + "="*60)
        print(f"Validated {len(files)} files")
        if all_valid:
            print("✅ ALL FILES PASSED")
        else:
            print("❌ SOME FILES FAILED")

        sys.exit(0 if all_valid else 1)


if __name__ == "__main__":
    main()