# Competitive Strategy: [Competitor Name]

**Last Updated**: [Date]
**Maintained By**: Human (strategic positioning decisions)
**Used By**: web_comparison generation, battle card generation, sales enablement

**Purpose**: This file captures human strategic decisions about how to position against this specific competitor. Machine-generated content (web comparisons, battle cards) reads this file to understand what to emphasize.

---

## 1. PRIMARY WEAKNESSES (Rank Top 3)

**Instructions**: Identify the 3 most exploitable weaknesses. Use BUA framework scores as evidence. Assign severity, defensibility, and emphasis level.

**Defensibility Guide**:
- **Architectural**: Fundamental to competitor's design, hard/impossible to fix (emphasize heavily)
- **Temporal**: May improve with better models/updates (acknowledge but don't over-emphasize)
- **Strategic**: Competitor could fix but chooses not to (moderate emphasis)

**#1: [Weakness Name]** (Severity: Critical | High | Medium | Defensibility: Architectural | Temporal | Strategic)
- **Evidence**: [BUA dimension score, specific finding, or quote from research]
- **Why It Matters**: [Business impact - why buyers care]
- **Our Advantage**: [Specific Scoop capability that addresses this]
- **Defensibility**: [Is this architectural or may competitor improve? How quickly? Why emphasize/de-emphasize?]
- **Emphasis Level**: [XX]% of web comparison

**#2: [Weakness Name]** (Severity: Critical | High | Medium | Defensibility: Architectural | Temporal | Strategic)
- **Evidence**:
- **Why It Matters**:
- **Our Advantage**:
- **Defensibility**:
- **Emphasis Level**: [XX]%

**#3: [Weakness Name]** (Severity: Critical | High | Medium | Defensibility: Architectural | Temporal | Strategic)
- **Evidence**:
- **Why It Matters**:
- **Our Advantage**:
- **Defensibility**:
- **Emphasis Level**: [XX]%

---

## 2. KEY SCENARIOS (Stories that expose weaknesses)

**Instructions**: Choose 2-4 real-world scenarios that make the competitor's weaknesses obvious. Good scenarios are specific, relatable, and measurable (time/cost differences).

**Scenario 1: [Scenario Name]**
- **When to Use**: [Which competitor weakness this exposes]
- **Story**: [1-2 sentence description of the scenario]
- **Expected Impact**: [Why this resonates with buyers]

**Scenario 2: [Scenario Name]**
- **When to Use**:
- **Story**:
- **Expected Impact**:

**Scenario 3: [Optional]**
- **When to Use**:
- **Story**:
- **Expected Impact**:

---

## 3. TALKING POINTS (Emphasis hierarchy)

**Instructions**: Order these by importance. Top 3 should directly address primary weaknesses from Section 1.

**Lead With** (Most important - use these in first 1000 words):
1. [Point] - *Because [competitor weakness]*
2. [Point] - *Because [competitor weakness]*
3. [Point] - *Because [competitor weakness]*

**Always Mention** (Standard Scoop advantages):
4. [Point]
5. [Point]
6. [Point]

**De-Emphasize** (Don't lead with these, minor mentions only):
- [Point where gap is small or irrelevant]
- [Point where competitor is adequate]

---

## 4. CONTENT DISTRIBUTION (Word allocation for 7,500-word comparison)

**Instructions**: Allocate percentages based on competitor weaknesses and defensibility. Emphasize architectural limitations (hard for competitor to fix), de-emphasize temporal limitations (may improve).

**Emphasis Adjustment Philosophy**:
- ⬆️ INCREASE emphasis on architectural limitations (competitor cannot easily fix)
- ⬇️ DECREASE emphasis on temporal limitations (may improve with better models/updates)
- ⬆️ INCREASE where competitor gap is widest (BUA dimension <5/20)
- ⬆️ INCREASE where differentiation is clearest and most measurable
- ⬇️ DECREASE where competitor is adequate or gap is narrow
- **⬆️ COST/TCO SECTION**: Always emphasize cost category elimination (implementation, training, maintenance) over license price comparison

**Recommended Mix**:
- **Section 1 (Executive Summary)**: [XX]% (~XXX words)
- **Section 2 (Capabilities)**: [XX]% (~XXX words)
  - UI/Workflow: [XX]%
  - Excel/Spreadsheet: [XX]%
  - ML/Investigation: [XX]%
  - Setup/Implementation: [XX]%
  - Schema Evolution: [XX]%
- **Section 3 (Cost/TCO)**: [XX]% (~XXX words)
  - Focus: Cost category elimination (5 of 6 categories = $0), NOT license price comparison
  - Emphasize: Architectural reasons for $0 implementation, $0 training, $0 maintenance
  - Avoid: Specific Scoop dollar amounts (pricing may evolve)
- **Section 4 (Use Cases)**: [XX]% (~XXX words)
- **Section 5-7 (FAQ/Evidence/Next Steps)**: [XX]% (~XXX words)

**Rationale**:
[Explain distribution based on defensibility, not just severity. Which weaknesses are architectural vs temporal? Why emphasize certain areas over others?]

**Comparison to Default**:
- ⬆️ Increased: [Section name] (normally XX%, now XX%) - Because [architectural limitation / widest gap / defensibility reason]
- ⬇️ Decreased: [Section name] (normally XX%, now XX%) - Because [may improve / narrow gap / temporal limitation]

---

## 5. PROOF POINTS (Evidence to cite)

**Instructions**: Pull specific evidence that supports your positioning. Link to framework_scoring.md and research files.

**From Framework Scoring** (`evidence/framework_scoring.md`):
- **BUA Total**: [X/100] ([Category])
- **Lowest Dimension**: [Dimension Name] ([Score]/20)
- **Critical Sub-Scores**:
  - [Sub-component]: [Score]/[Max] (e.g., Native Integration: 0/8)
  - [Sub-component]: [Score]/[Max]

**From Research** (`evidence/research_library.md` or other sources):
- "[Specific quote or finding]" - [Source/URL]
- "[Customer pain point or limitation]" - [Source/URL]
- "[Performance data or benchmark]" - [Source/URL]

**From Public Documentation**:
- "[Vendor's own admission or limitation]" - [Official doc URL]
- "[Pricing or requirement]" - [Official doc URL]

---

## 6. WIN CONDITIONS (What makes us win)

**Instructions**: Be specific about when Scoop wins vs loses. Honesty here prevents wasted sales cycles.

**We Win When**:
1. [Condition] - *Because [competitor limitation]*
2. [Condition] - *Because [competitor limitation]*
3. [Condition] - *Because [competitor limitation]*
4. [Condition] - *Because [competitor limitation]*

**We Lose When** (Be honest):
- [Condition where competitor is actually better fit]
- [Scenario where competitor's approach makes sense]

**Neutral** (Could go either way):
- [Condition where both solutions work]

---

## 7. COMPETITIVE POSITIONING

**Instructions**: Craft the core positioning message. Start with product type classification to set the frame, then build specific positioning.

**Product Type Classification**:
- **What They Really Are**: [Text-to-query interface | SQL generation tool | BI tool with AI | Dashboard platform | etc.]
- **What We Really Are**: [AI data analyst | Business analytics platform]
- **Their Primary Audience**: [Data engineers | Analysts | Dashboard creators | Technical users]
- **Our Primary Audience**: Business users with Excel skills
- **Key Architectural Difference**: [Their fundamental approach vs our approach]

**One-Sentence Position**:
"[Competitor] is a {PRODUCT_TYPE} for {AUDIENCE}, Scoop is a {PRODUCT_TYPE} for {AUDIENCE}"

**Example Patterns**:
- "[Competitor] is a text-to-query interface for IT-built semantic models, Scoop is an AI data analyst for any data"
- "[Competitor] is a SQL generation tool for data engineers, Scoop is a business analytics platform for Excel users"
- "[Competitor] is a BI tool with AI features, Scoop is an AI-first analytics platform"

**Elevator Pitch** (30 seconds, ~60 words):
[2-3 sentences capturing the core differentiation. Should mention their product type, primary weakness, and our product type with primary strength.]

**Key Contrast**:
| Dimension | [Competitor] | Scoop |
|-----------|-------------|-------|
| **Product Type** | [Their type] | AI data analyst / Business analytics platform |
| **Built For** | [Their user] | Business users with Excel skills |
| **Primary Interface** | [Their interface] | Slack + Excel + PowerPoint |
| **Deliverable** | [What they give you] | Branded presentations with insights |
| **Setup Time** | [Their time] | 30 seconds |

---

## 8. AVOID OVER-CLAIMING (Credibility guardrails)

**Instructions**: List things we should NOT say because they're inaccurate or unprovable. Prevents credibility damage.

**Don't Say** (Risks credibility):
- "[Exaggeration]" - *Because [why this is inaccurate]*
- "[Over-claim]" - *Because [why we can't prove this]*
- "[Unfair characterization]" - *Because [why this is misleading]*
- **"Scoop costs $X for Y users"** - *Because pricing is evolving and specific claims will become outdated*

**Instead Say** (Evidence-based alternatives):
- "[Accurate statement]" - *Supported by [evidence]*
- **"Scoop eliminates implementation cost ($0), training cost ($0), and maintenance cost ($0)—typical customers see 10x lower TCO"** - *Defensible regardless of license price changes, based on architectural differences*
- "[Provable claim]" - *Supported by [evidence]*
- "[Fair characterization]" - *Supported by [evidence]*

---

## 9. CUSTOM CONTENT BLOCKS (Competitor-specific examples)

**Instructions**: Write 2-3 specific examples or comparisons that are unique to this competitor. These should be copy-paste ready for web comparison.

### Example 1: [Title]

**Setup**: [1 sentence describing the scenario]

**[Competitor] Experience**:
```
[Step-by-step walkthrough showing their painful process]
Step 1: [Action]
Step 2: [Action]
...
TIME: [How long it takes]
RESULT: [What you end up with]
```

**Scoop Experience**:
```
[Step-by-step walkthrough showing our streamlined process]
Step 1: [Action]
Step 2: [Action]
...
TIME: [How long it takes]
RESULT: [What you end up with]
```

**Business Impact**: [Why this matters]

---

### Example 2: [Title]

[Same structure as Example 1]

---

### Example 3: [Optional - Title]

[Same structure as Example 1]

---

## 10. SALES GUIDANCE (How to use this in conversations)

**Instructions**: Practical guidance for sales conversations. What questions to ask, how to position.

**Discovery Questions to Ask**:
1. [Question that exposes competitor weakness]
2. [Question that qualifies for Scoop strengths]
3. [Question about their current pain]

**If They Say**: "[Common objection]"
**We Respond**: "[Counter with evidence from this strategy]"

**If They Say**: "[Another objection]"
**We Respond**: "[Counter with evidence]"

**Demo Focus Areas** (for this competitor):
1. [Scoop capability to show] - Contrasts with [their weakness]
2. [Scoop capability to show] - Contrasts with [their weakness]
3. [Scoop capability to show] - Contrasts with [their weakness]

---

## USAGE INSTRUCTIONS

### For Web Comparison Generation:
1. Read this COMPETITIVE_STRATEGY.md file first
2. Read `evidence/framework_scoring.md` for BUA scores and detailed evidence
3. Apply content distribution from **Section 4** to allocate word count
4. Lead with scenarios from **Section 2** in executive summary
5. Emphasize talking points from **Section 3** throughout
6. Use proof points from **Section 5** as evidence citations
7. Include custom content blocks from **Section 9** verbatim
8. Respect "Avoid" guidance from **Section 8** (never say these things)
9. Structure win conditions from **Section 6** into use cases section

### For Battle Card Generation:
1. Use one-sentence position from **Section 7** as header
2. Lead with primary weakness (#1) from **Section 1**
3. Include top 3 talking points from **Section 3**
4. Highlight win conditions from **Section 6**
5. Use proof points from **Section 5** for quick evidence

### For Sales Enablement:
1. Memorize elevator pitch from **Section 7**
2. Use discovery questions from **Section 10**
3. Know win/lose conditions from **Section 6**
4. Reference custom examples from **Section 9** in conversations

---

## MAINTENANCE SCHEDULE

**Quarterly Review** (Every 3 months):
- [ ] Check if competitor has launched new features
- [ ] Review if BUA scores have changed (re-run framework scoring)
- [ ] Update proof points if research has new findings
- [ ] Verify pricing information is current
- [ ] Check if win/lose conditions have shifted

**Triggered Updates** (Update immediately when):
- Competitor announces major product changes
- Win/loss analysis reveals new patterns
- Sales team reports different objections than expected
- BUA dimension scores change by >3 points

**Version History**:
- [Date]: [What changed and why]
- [Date]: [What changed and why]

---

**Template Version**: 1.1
**Created**: September 27, 2025
**Last Updated**: September 28, 2025

**Changelog**:
- **v1.1 (Sept 28, 2025)**: Added defensibility field to weaknesses (Section 1), emphasis adjustment philosophy to content distribution (Section 4), and product type classification to positioning (Section 7). Based on learnings from Power BI Copilot strategy development.