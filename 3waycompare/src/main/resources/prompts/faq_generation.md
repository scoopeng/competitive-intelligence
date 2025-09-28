Generate FAQ answers for the three-way comparison between {competitorA}, {competitorB}, and Scoop.

Context:
- {competitorA}: BUA {aScore}/100, {aStrengths}, {aWeaknesses}
- {competitorB}: BUA {bScore}/100, {bStrengths}, {bWeaknesses}
- Scoop: BUA 82/100, AI analyst approach, multi-pass investigation

Questions to Answer:
{faqQuestions}

OUTPUT CONTRACT:

Return a JSON object with this structure:
```json
{
  "markdown": {
    "faqs": [
      {
        "question": "[Exact question text]",
        "answer": "[EXACTLY 40-60 words]",
        "answerType": "[paragraph|list|comparison]",
        "evidence": "[Evidence: source]"
      }
    ]
  }
}
```

CRITICAL REQUIREMENTS:

1. **Word Count**: EVERY answer must be EXACTLY 40-60 words. Count every word including articles (a, an, the).

2. **Answer Types**:
   - **paragraph**: Direct answer in prose form
   - **list**: Bulleted key points (still must be 40-60 words total)
   - **comparison**: Side-by-side contrast (still must be 40-60 words total)

3. **Answer Structure**:
   - Start with direct answer (Yes/No if applicable)
   - Include quantitative comparison where possible
   - End with evidence-based claim
   - Natural, conversational language

4. **Evidence Requirements**:
   - Every answer must include evidence citation
   - Format: [Evidence: specific source]
   - Use actual scores, quotes, or documentation references

STANDARD FAQ TEMPLATES:

**"What is Scoop?"** (MUST be first FAQ):
"Scoop is an AI data analyst you chat with, not another dashboard. Ask questions in plain English, get answers with charts. Works natively in Excel and Slack. Unlike {competitorA} and {competitorB} which require IT setup, Scoop connects directly to your data in 30 seconds. [Evidence: Scoop product documentation]"

**"Can X handle complex queries?"**:
"Scoop handles complex multi-table queries automatically through its AI engine. {competitorA} [capability], while {competitorB} [capability]. Scoop's multi-pass investigation chains 3-10 queries automatically, finding root causes that dashboard tools miss. Business users need zero SQL knowledge. [Evidence: BUA framework scoring]"

**"How much training is required?"**:
"Scoop requires zero training—if you can use ChatGPT, you can use Scoop. {competitorA} requires [X] training, {competitorB} needs [Y]. Scoop's natural language interface means business users start getting value immediately. No semantic layer setup or SQL knowledge needed. [Evidence: comparative analysis]"

**"What does X really cost?"**:
"{competitorA} true cost includes [list categories]. {competitorB} requires [list categories]. Total cost often reaches [X]x the license fee. Scoop eliminates implementation, training, maintenance, and consultant costs—just a simple subscription. This typically reduces TCO by 90%. [Evidence: TCO analysis]"

**Investigation Questions**:
- Focus on multi-pass capability (3-10 queries)
- Emphasize automatic hypothesis testing
- Contrast with single-query limitations

**Technical Questions**:
- Translate to business impact
- Avoid jargon in answers
- Focus on what users can DO

**Cost Questions**:
- Include ALL cost categories (not just licenses)
- Emphasize eliminated categories with Scoop
- Use "fraction of traditional BI TCO" not specific amounts

QUESTION-SPECIFIC GUIDANCE:

{questionGuidance}

WORD COUNTING RULES:
- Count all words including: a, an, the, is, are, etc.
- Hyphenated words count as one (e.g., "multi-pass" = 1 word)
- Numbers count as words (e.g., "3-10" = 1 word)
- Acronyms count as one word (e.g., "TCO" = 1 word)

QUALITY CHECKS:
- Is it exactly 40-60 words? (Critical for AEO)
- Does it answer the question directly?
- Is there quantitative evidence?
- Is the language natural and conversational?
- Is the evidence citation included?

EXAMPLES OF GOOD ANSWERS:

"Can Scoop handle real-time data?"
"Yes, Scoop connects directly to live databases and cloud warehouses for real-time analysis. Power BI requires scheduled refreshes and Tableau uses extracts by default. Scoop queries fresh data with every question, ensuring decisions are based on current information, not yesterday's dashboard cache. [Evidence: Direct connection architecture]" (54 words ✓)

"Which is easiest to learn?"
"Scoop requires zero training—just type questions like you'd ask a colleague. Power BI Copilot needs DAX knowledge for complex queries, Snowflake Cortex requires SQL. With Scoop, if you can write an email, you can analyze data. Business users become productive in minutes, not weeks. [Evidence: User studies]" (50 words ✓)