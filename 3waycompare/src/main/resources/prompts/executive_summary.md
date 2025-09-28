Generate the Executive Summary section for a three-way comparison between {competitorA}, {competitorB}, and Scoop Analytics.

Competitor Context:
- {competitorA}: BUA Score {aScore}/100 ({aCategory})
  Primary Weaknesses: {aWeaknesses}
  Key Evidence: {aEvidence}

- {competitorB}: BUA Score {bScore}/100 ({bCategory})  
  Primary Weaknesses: {bWeaknesses}
  Key Evidence: {bEvidence}

- Scoop: BUA Score 82/100 (A Strong)
  Key Strengths: Multi-pass investigation, Excel-native, zero setup

OUTPUT CONTRACT – READ CAREFULLY:

Return a JSON object with the following structure:
```json
{
  "markdown": {
    "tldrVerdict": "[THREE sentences totaling 50-58 words. First sentence: scores + differentiator (15-20 words). Second: weakness exploitation (15-20 words). Third: recommendation (15-18 words)]",
    "whatIsScoop": "[50-58 words, MUST start 'Scoop is an AI data analyst you chat with'. Use short, clear sentences. Active voice only.]",
    "chooseScoopIf": "[3-4 bullet points, each 15-25 words]",
    "considerAIf": "[2-3 bullet points for {competitorA}, each 15-25 words]",
    "considerBIf": "[2-3 bullet points for {competitorB}, each 15-25 words]",
    "bottomLine": "[100-150 words synthesis with evidence citations. Short sentences (15-20 words max). High readability.]"
  }
}
```

REQUIREMENTS:

1. **TL;DR Verdict** (CRITICAL - 50-58 words total):
   - Structure as THREE sentences for proper word count:
     * Sentence 1 (15-20 words): State BUA scores and core differentiator
     * Sentence 2 (15-20 words): Explain specific weakness exploitation
     * Sentence 3 (15-18 words): Bottom-line recommendation
   - Must include all three BUA scores
   - Position Scoop's investigation capability as key differentiator
   - Natural comparison flow (not just listing scores)

2. **What is Scoop**:
   - MUST start with "Scoop is an AI data analyst you chat with"
   - Include "not a dashboard" positioning
   - Mention Excel/Slack native integration

3. **Choose Scoop If**:
   - Focus on business user autonomy benefits
   - Include specific use cases (investigation, Excel users, non-technical teams)
   - Avoid technical jargon

4. **Consider Competitors If**:
   - Be fair and balanced
   - Acknowledge legitimate use cases
   - Focus on organizational fit (e.g., "existing {vendor} ecosystem")

5. **Bottom Line**:
   - Weave in evidence citations naturally [Evidence: source]
   - Emphasize investigation vs dashboard paradigm shift  
   - Include TCO advantage (eliminate 5 of 6 cost categories)
   - End with forward-looking statement about business empowerment

EXAMPLE OUTPUT STYLE (with proper 3-sentence structure):

"tldrVerdict": "Scoop (82/100 BUA) delivers true business autonomy through multi-pass investigation, while {competitorA} ({aScore}/100) and {competitorB} ({bScore}/100) remain dashboard-bound. Neither competitor supports the iterative questioning that real investigation requires, forcing users back to IT repeatedly. Choose Scoop for immediate independence, competitors only if locked into existing ecosystems."

"whatIsScoop": "Scoop is an AI data analyst you chat with, not another dashboard tool. Ask questions in plain English, get answers with charts. Works natively in Excel and Slack where business users already work. No SQL, no training, no semantic layer maintenance required."

AVOID:
- Marketing hyperbole ("revolutionary", "game-changing")
- Unsubstantiated claims without evidence
- Technical details that business users don't care about
- Specific pricing (say "fraction of TCO" not dollar amounts)