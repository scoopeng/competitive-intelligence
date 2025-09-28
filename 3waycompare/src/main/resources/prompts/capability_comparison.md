Generate a capability comparison section for {capabilityType} comparing {competitorA}, {competitorB}, and Scoop.

Capability Context:
{capabilityContext}

Competitor Evidence:
- {competitorA}: {aCapabilityEvidence}
- {competitorB}: {bCapabilityEvidence}
- Scoop: {scoopCapabilityEvidence}

OUTPUT CONTRACT:

Return a JSON object with this structure:
```json
{
  "markdown": {
    "sectionTitle": "[Capability Name]",
    "openingNarrative": "[100-150 words setting business context]",
    "capabilityTable": [
      {
        "feature": "[Feature/Capability]",
        "competitorA": "[Status/Implementation]",
        "competitorB": "[Status/Implementation]",
        "scoop": "[Status/Implementation]",
        "businessImpact": "[Why this matters]"
      }
    ],
    "deepDiveAnalysis": "[200-250 words detailed comparison]",
    "exampleScenario": "[150-200 words showing real-world usage]",
    "bottomLine": "[60-80 words summary]",
    "evidenceCitations": ["[Evidence: source]"]
  }
}
```

CAPABILITY TYPES AND FOCUS:

**INVESTIGATION & ROOT CAUSE ANALYSIS:**
- Multi-pass vs single query architecture
- Automatic hypothesis testing
- Pattern discovery and correlation
- Example: "Why did revenue drop in Q3?"
- Key metric: Number of queries to reach root cause

**EXCEL & SPREADSHEET INTEGRATION:**
- Native add-in vs export/import
- Live connection vs static data
- Formula integration capabilities
- Example: Monthly reporting workflow
- Key metric: Clicks from Excel to insight

**MACHINE LEARNING & AI:**
- Automatic vs manual ML deployment
- Types of analysis available
- Configuration requirements
- Example: Anomaly detection in sales data
- Key metric: Time from data to prediction

**NATURAL LANGUAGE QUALITY:**
- Understanding of business terminology
- Query complexity handling
- Need for technical syntax
- Example: "Show me customers at risk of churning"
- Key metric: Success rate on first query

**WORKFLOW INTEGRATION:**
- Native integrations (Excel, Slack, etc.)
- API availability
- Collaboration features
- Example: Team investigation in Slack
- Key metric: Context switches required

**DATA CONNECTIVITY:**
- Direct connection vs ETL
- Supported data sources
- Setup complexity
- Example: Connecting to Snowflake
- Key metric: Time to first query

**GOVERNANCE & SECURITY:**
- Row-level security
- Audit trails
- Data lineage
- Example: HIPAA compliance scenario
- Key metric: Configuration complexity

**COST & TCO:**
- License model
- Implementation costs
- Training requirements
- Maintenance needs
- Hidden costs (consultants, IT support)
- Example: 200-user deployment
- Key metric: Total 3-year cost

REQUIREMENTS:

1. **Opening Narrative**:
   - Start with relatable business scenario
   - Explain why this capability matters
   - Set up the comparison framework
   - Use conversational tone

2. **Capability Table**:
   - 5-8 specific features/aspects
   - Clear yes/no/partial status
   - Business impact for each row
   - Highlight architectural differences

3. **Deep Dive Analysis**:
   - Go beyond feature lists to explain WHY
   - Focus on architectural limitations
   - Include quantitative comparisons
   - Weave in evidence naturally

4. **Example Scenario**:
   - Walk through specific use case
   - Show how each platform handles it
   - Highlight friction points
   - Quantify time/effort differences

5. **Bottom Line**:
   - Crisp summary of key advantage
   - Acknowledge fair competitor strengths
   - End with business impact statement

TONE AND STYLE:
- Conversational but authoritative
- Concrete over abstract
- Examples over generalizations
- Evidence over assertions
- Business impact over features

AVOID:
- Feature arms race comparisons
- Unfair characterizations
- Technical jargon without translation
- Claims without evidence
- Hyperbole or marketing speak

EXAMPLE OUTPUT SNIPPET:

"openingNarrative": "When a CEO asks 'Why did Northeast region sales drop 15% last quarter?', the path to an answer reveals everything about a platform's true capability. This isn't about dashboards showing the drop—it's about investigation tools that uncover the why. Let's examine how each platform handles this critical business need."

"exampleScenario": "A sales manager notices an unusual pattern in quarterly results. With Scoop, she types 'Why did enterprise deals drop in Q3?' Scoop automatically investigates: checking seasonality, comparing segments, analyzing win rates, and identifying that competitor pricing changed in July. Total time: 3 minutes. Power BI Copilot would require manually building 4-5 separate queries. Snowflake Cortex would need SQL for each investigation step."

{additionalGuidance}