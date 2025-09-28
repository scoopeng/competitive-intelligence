Generate a detailed BUA dimension analysis for {dimension} comparing {competitorA}, {competitorB}, and Scoop.

Dimension Scores:
- {competitorA}: {aDimensionScore}/20 ({aDimensionBreakdown})
- {competitorB}: {bDimensionScore}/20 ({bDimensionBreakdown})  
- Scoop: {scoopDimensionScore}/20 ({scoopDimensionBreakdown})

Component Evidence:
{componentEvidence}

OUTPUT CONTRACT:

Return a JSON object with this structure:
```json
{
  "markdown": {
    "dimensionNarrative": "[150-200 words explaining why this dimension matters. Short sentences. Active voice. Flesch 80+]",
    "componentTable": [
      {
        "component": "[Component Name]",
        "weight": "[X points]",
        "competitorA": "[Score/8 + brief explanation]",
        "competitorB": "[Score/8 + brief explanation]",
        "scoop": "[Score/8 + brief explanation]",
        "winner": "[Platform name or 'Tie']"
      }
    ],
    "keyDifferentiator": "[80-100 words on the biggest architectural difference]",
    "businessImpact": "[60-80 words on real-world impact]",
    "extractableSummary": "[40-60 words. Complete answer to 'How do these platforms compare on {dimension}?' Must be standalone, no pronouns requiring context.]",
    "evidenceCitations": ["[Evidence: source1]", "[Evidence: source2]"]
  }
}
```

DIMENSION-SPECIFIC FOCUS:

{dimensionGuidance}

REQUIREMENTS:

1. **Dimension Narrative**:
   - Open with a business scenario that illustrates the dimension
   - Explain why this dimension matters for business users
   - Use concrete examples (e.g., "When a CEO asks 'Why did revenue drop?'...")
   - Natural, conversational tone (Flesch 80+)

2. **Component Table**:
   - Break down all components that comprise this dimension
   - Scores should sum to dimension total
   - Brief explanations focus on capability, not features
   - Clear winner identification based on evidence

3. **Key Differentiator**:
   - Identify the single biggest architectural difference
   - Explain WHY the scores differ (not just that they do)
   - Focus on fundamental limitations vs missing features

4. **Business Impact**:
   - Translate technical differences into business outcomes
   - Use time/cost/quality metrics where possible
   - Include specific role impacts (analyst, business user, IT)

5. **Extractable Summary** (CRITICAL for AEO):
   - EXACTLY 40-60 words
   - Complete, standalone answer to "How do these platforms compare on {dimension}?"
   - Include all three platform names explicitly
   - No pronouns that require context (they, it, these)
   - Must make sense if shown alone in search results
   - Include specific scores or metrics

6. **Evidence Citations**:
   - Include 2-4 specific evidence citations
   - Format: [Evidence: source, date if available]

DIMENSION GUIDANCE BY TYPE:

AUTONOMY:
- Focus on IT dependency and self-service capability
- Emphasize investigation depth and multi-pass capability
- Highlight setup/configuration requirements
- Key question: "Can a business user do this alone?"

FLOW:
- Focus on workflow integration and context switching
- Emphasize native vs export/import cycles
- Highlight "portal prison" effect
- Key question: "Where does the user have to go?"

UNDERSTANDING:
- Focus on business terminology vs technical jargon
- Emphasize semantic layer requirements
- Highlight natural language quality
- Key question: "Can a non-technical user understand?"

PRESENTATION:
- Focus on output format and context awareness
- Emphasize automatic vs manual formatting
- Highlight shareability and integration
- Key question: "Is the output business-ready?"

DATA:
- Focus on connection simplicity and maintenance
- Emphasize direct access vs preparation requirements
- Highlight refresh and governance capabilities
- Key question: "How much IT setup is required?"

AVOID:
- Feature comparisons without user impact
- Technical specifications without business context
- Unfair characterizations of competitor limitations
- Claims without evidence citations