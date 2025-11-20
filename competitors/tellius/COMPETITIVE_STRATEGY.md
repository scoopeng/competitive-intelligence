# Competitive Strategy: Tellius

**Last Updated**: November 18, 2025
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

**#1: Architectural Instability: Apache Spark Fragility vs. Cloud-Native Reliability** (Severity: Critical | Defensibility: Architectural)
- **Evidence**: "Tool hangs sometimes" (G2 reviews), Apache Spark memory crashes, GC overhead, "notoriously difficult to tune"
- **Why It Matters**: Core platform reliability is non-negotiable. If the foundation crashes during complex analysis, **Domain Intelligence** is impossible. Tellius's reliance on fragile Apache Spark clusters creates operational risk.
- **Our Advantage**: Scoop is built on a stable, cloud-native architecture designed for **Autonomous Investigation**. We eliminate Spark management, crashes, and tuning, delivering reliable, deterministic results.
- **Defensibility**: Architectural - they built entire platform on Spark, cannot easily change without complete rebuild
- **Emphasis Level**: 25% of web comparison

**#2: Workflow Destruction: Excel Replacement vs. True Workflow Integration** (Severity: Critical | Defensibility: Strategic)
- **Evidence**: BUA Flow 0/20, "Tellius wants to REPLACE Excel, not enhance it", zero Excel formula engine
- **Why It Matters**: Forcing users to abandon Excel destroys existing workflows and expertise. It is **Workflow Destruction**, not empowerment. Business users want to operationalize their expertise in the tools they know.
- **Our Advantage**: Scoop offers **True Workflow Integration** with a native **Spreadsheet Calculation Engine** (150+ formulas). We enhance existing skills, operationalizing expertise directly in Excel and Slack.
- **Defensibility**: Strategic - they chose replacement strategy, could build Excel support but philosophically opposed
- **Emphasis Level**: 25% of web comparison

**#3: Credibility Gap: Aspirational AI vs. Deterministic Domain Intelligence** (Severity: High | Defensibility: Temporal)
- **Evidence**: "Natural Language Search has not been adopted for analytics" (Tellius documentation), "ambiguous language, mismatched definitions, unreliable multi-step logic"
- **Why It Matters**: Tellius admits their core "Natural Language" value proposition has failed adoption. This creates a massive **Credibility Gap**. Their AI is aspirational and unreliable.
- **Our Advantage**: Scoop provides **Deterministic Domain Intelligence**. Our **Investigation Coordinator** and **Encoded Expertise** ensure reliable, verifiable, multi-step reasoning that users trust and adopt.
- **Defensibility**: Temporal - they could improve NL but have admitted failure after years of trying
- **Emphasis Level**: 20% of web comparison

---

## 2. KEY SCENARIOS (Stories that expose weaknesses)

**Instructions**: Choose 2-4 real-world scenarios that make the competitor's weaknesses obvious. Good scenarios are specific, relatable, and measurable (time/cost differences).

**Scenario 1: Reliability Crisis: Spark Crash vs. Autonomous Investigation**
- **When to Use**: Exposes architectural instability (#1).
- **Story**: "A financial analyst attempts a quarterly variance analysis. Tellius's Apache Spark engine runs out of memory and crashes ('GC overhead limit exceeded'). IT tuning takes 4-6 hours. The board meeting deadline is missed. Scoop's **Investigation Coordinator** executes the same analysis autonomously, testing multiple hypotheses and delivering a complete, deterministic report in 30 seconds without architectural drama."
- **Expected Impact**: Demonstrates that unstable architecture creates business risk, while Scoop delivers reliable **Domain Intelligence**.

**Scenario 2: Workflow Destruction: Excel Replacement vs. Spreadsheet Calculation Engine**
- **When to Use**: Exposes Excel replacement strategy (#2).
- **Story**: "A CFO team with advanced Excel skills is told to abandon their workflows for Tellius. They lose their VLOOKUPs and pivot tables, forced into a new platform learning curve. This is **Workflow Destruction**. Scoop's **Spreadsheet Calculation Engine** enables them to use 150+ live Excel functions directly on the data. We enhance their expertise; we don't replace their tools."
- **Expected Impact**: Shows workflow destruction vs enhancement - validates Scoop's approach to **True Workflow Integration**.

**Scenario 3: Credibility Gap: Failed NL Promise vs. Encoded Expertise**
- **When to Use**: Exposes NL failure (#3).
- **Story**: "A sales team buys Tellius for its 'Natural Language' promise. After 6 months, they discover Tellius's own documentation admits 'Natural Language Search has not been adopted' due to ambiguity and unreliability. Scoop's **Encoded Expertise (Schema v2.8)** ensures that business terms are understood correctly, delivering trusted, verifiable answers every time. No ambiguity, no adoption failure."
- **Expected Impact**: Vendor admits their main selling point failed - credibility destroyer.

**Scenario 4: TCO Trap: Hidden Costs of Complexity**
- **When to Use**: Exposes true TCO vs advertised pricing.
- **Story**: "Tellius advertises $495/month. But the reality of managing Spark clusters, implementation services, and 'citizen data scientist' training bloats Year 1 costs to $125,000+. Scoop's **Eliminated Labor Categories** (no training, no maintenance) keep the price flat and predictable at ~$3,588/year. We sell intelligence, not infrastructure projects."
- **Expected Impact**: 33x cost increase from advertised price - demonstrates deceptive pricing.

---

## 3. TALKING POINTS (Emphasis hierarchy)

**Instructions**: Order these by importance. Top 3 should directly address primary weaknesses from Section 1.

**Lead With** (Most important - use these in first 1000 words):
1.  **"Cloud-Native Reliability vs. Apache Spark Fragility (Architectural Instability)"** - *Tellius crashes; Scoop scales. The foundation matters.*
2.  **"True Workflow Integration vs. Workflow Destruction"** - *We enhance your Excel skills; they force you to abandon them for a proprietary tool.*
3.  **"Deterministic Domain Intelligence vs. Aspirational AI (Credibility Gap)"** - *We deliver trusted answers; they admit their NL "has not been adopted."*

**Always Mention** (Standard Scoop advantages):
4.  **Investigation Coordinator** (Autonomous multi-step reasoning vs. manual "citizen data scientist" work).
5.  **Spreadsheet Calculation Engine** (150+ native Excel formulas vs. zero support).
6.  **30-Second Setup** (vs. 6-month implementation projects).
7.  **Eliminated Labor Categories** (No IT maintenance, no training vs. Spark cluster management).
8.  **$3,588 vs. $125,000+ TCO** (Value vs. hidden costs).

**De-Emphasize** (Don't lead with these, minor mentions only):
- **Visualization capabilities** - Tellius has adequate charts, not a key differentiator.
- **Data connectivity** - They score 4/4 on multi-source; this is table stakes.

---

## 4. CONTENT DISTRIBUTION (Word allocation for 7,500-word comparison)

**Instructions**: Allocate percentages based on competitor weaknesses and defensibility. Emphasize architectural limitations (hard for competitor to fix), de-emphasize temporal limitations (may improve).

**Emphasis Adjustment Philosophy**:
- ⬆️ INCREASE on **Architectural Instability** (Spark crashes).
- ⬆️ INCREASE on **Workflow Destruction** (Excel replacement).
- ⬆️ INCREASE on **Credibility Gap** (Failed NL adoption).

**Recommended Mix**:
- **Section 1 (Executive Summary)**: 15% (~1,125 words)
- **Section 2 (Capabilities)**: 55% (~4,125 words)
  - **Architectural Instability (Spark Crashes)**: 20% (Fundamental reliability failure).
  - **Workflow Destruction (Excel Elimination)**: 15% (Strategic barrier to adoption).
  - **Credibility Gap (NL Failure)**: 10% (Validates lack of intelligence).
  - **Investigation vs. "Citizen Data Scientist"**: 5% (Contrast autonomous vs. manual).
  - **Setup & Implementation**: 5% (Speed to value).
- **Section 3 (Cost/TCO)**: 15% (~1,125 words)
- **Section 4 (Use Cases)**: 10% (~750 words)
- **Section 5-7 (FAQ/Evidence/Next Steps)**: 5% (~375 words)

**Rationale**:
Heavy emphasis on capabilities because that's where all three primary weaknesses live. Apache Spark crashes and Excel elimination are architectural issues Tellius cannot easily fix. Natural language failure is documented by Tellius themselves. Cost section important because true cost is 33x advertised price.

---

## 5. PROOF POINTS (Evidence to cite)

**Instructions**: Pull specific evidence that supports your positioning. Link to framework_scoring.md and research files.

**From Framework Scoring** (`evidence/framework_scoring.md`):
- **BUA Total**: 22/100 (Category D - Poor)
- **Lowest Dimension**: Flow 0/20 (Evidence of **Workflow Destruction**).
- **Critical Sub-Scores**:
  - **Native Integration**: 0/8 (Forces Excel replacement - **Workflow Destruction**).
  - **Portal Prison**: 0/6 (100% platform dependency).
  - **Setup**: 0/8 (6-week to 6-month implementations - **TCO Trap**).
  - **Schema Evolution**: 0/8 (Universal BI platform failure).

**From Research** (`BATTLE_CARD.md` and battle card sources):
- "The tool hangs sometimes" - G2 customer review (Evidence of **Architectural Instability**).
- "Natural Language Search has not been adopted for analytics" - Tellius's own documentation (Evidence of **Credibility Gap**).
- "90% employee turnover" with "lightyears behind competitors" - Glassdoor employee reviews.
- "31 customers globally" after 8 years - Extreme market failure.

**From Public Documentation**:
- "eliminate manual Excel work that traditionally involves tedious copy-pasting and VLOOKUP formulas" - Official positioning confirming **Workflow Destruction**.
- "$495/month (Premium)" vs $125,000+ Year 1 reality - Evidence of **TCO Trap**.
- "6-week to 6-month implementations" - Implementation documentation.

---

## 6. WIN CONDITIONS (What makes us win)

**Instructions**: Be specific about when Scoop wins vs loses. Honesty here prevents wasted sales cycles.

**We Win When**:
1.  **Cloud-Native Reliability is Non-Negotiable**: When business continuity is critical and Apache Spark crashes are unacceptable (**Architectural Instability**).
2.  **Excel Expertise Must Be Leveraged**: When the organization values its existing Excel skills and rejects forced platform migration (**Workflow Destruction**).
3.  **Deterministic Intelligence is Required**: When the customer needs trusted, verifiable answers, not aspirational AI with low adoption rates (**Credibility Gap**).
4.  **Fast Time-to-Value is Essential**: When 30-second setup beats 6-month "citizen data scientist" projects.
5.  **Cost Predictability Matters**: When a flat $3,588/year beats hidden six-figure implementation costs.
6.  **Vendor Stability is a Concern**: When 90% turnover and low market adoption signal risk.

**We Lose When** (Be honest):
- Customer specifically needs Tellius's niche investigation capabilities and has the IT resources to manage Spark complexity (rare edge case).
- Budget is unlimited, and "citizen data scientist" training is a strategic organizational goal.

**Neutral** (Could go either way):
- Advanced ML scenarios where both have capabilities (though Scoop's explainable ML usually wins on usability).

---

## 7. COMPETITIVE POSITIONING

**Instructions**: Craft the core positioning message. Start with product type classification to set the frame, then build specific positioning.

**Product Type Classification**:
- **What They Really Are**: Fragile Enterprise Analytics Platform (Apache Spark) requiring "citizen data scientist" training.
- **What We Really Are**: **Cloud-Native Domain Intelligence Platform** (for **Autonomous Investigation**).
- **Their Primary Audience**: Technical analysts willing to abandon Excel and manage Spark instability.
- **Our Primary Audience**: Business users with Excel skills who need reliable, deterministic answers.
- **Key Architectural Difference**: Unstable Apache Spark foundation (crashes) vs. **Cloud-Native Investigation Coordinator** (reliable state machine).

**One-Sentence Position**:
"Tellius is a fragile enterprise analytics platform built on unstable Apache Spark architecture that forces **Workflow Destruction** by eliminating Excel; Scoop is a **Domain Intelligence Platform** that enhances existing workflows with **Autonomous Investigation** and **Cloud-Native Reliability**."

**Elevator Pitch** (30 seconds, ~60 words):
"Tellius requires 6-month implementations, 'citizen data scientist' training, and forces complete Excel abandonment. Their own documentation admits natural language 'has not been adopted,' and customers report 'tool hangs sometimes' due to Apache Spark crashes. Scoop is a **Domain Intelligence Platform**. We provide **True Workflow Integration** (enhancing Excel), execute **Autonomous Investigation** via our **Investigation Coordinator**, and deliver deterministic reliability with 30-second setup."

**Key Contrast**:
| Dimension | Tellius | Scoop |
|-----------|---------|-------|
| **Product Type** | Enterprise Analytics (Spark) | **Domain Intelligence Platform** |
| **Reliability** | "Tool hangs sometimes" (Crashes) | **Cloud-Native Reliability** |
| **Workflow** | **Workflow Destruction** (No Excel) | **True Workflow Integration** |
| **Intelligence** | Aspirational NL (Failed Adoption) | **Deterministic Domain Intelligence** |
| **Setup Time** | 6 weeks - 6 months | **30 Seconds** |
| **TCO** | Hidden Costs ($125K+) | **Flat / Predictable** |

---

## 8. AVOID OVER-CLAIMING (Credibility guardrails)

**Instructions**: List things we should NOT say because they're inaccurate or unprovable. Prevents credibility damage.

**Don't Say** (Risks credibility):
- "Tellius never works" - *They have some successful customers; focus on the high turnover and adoption challenges.*
- "Apache Spark always crashes" - *It hangs "sometimes" (per reviews); focus on the inherent **Architectural Instability**.*
- "All 31 customers are unhappy" - *Focus on the limited market adoption as evidence of product-market fit issues.*

**Instead Say** (Evidence-based alternatives):
- "Customers report 'tool hangs sometimes' due to Spark memory issues, creating **Architectural Instability**." - *Supported by G2 reviews.*
- "Tellius's own documentation admits 'Natural Language Search has not been adopted,' indicating a **Credibility Gap**." - *Direct quote from vendor.*
- "Forcing Excel users to abandon their tools for a proprietary platform is **Workflow Destruction**." - *Strategic framing of their replacement philosophy.*
- "90% employee turnover and 'lightyears behind' reviews suggest significant vendor instability." - *Supported by Glassdoor data.*

---

## 9. CUSTOM CONTENT BLOCKS (Competitor-specific examples)

**Instructions**: Write 2-3 specific examples or comparisons that are unique to this competitor. These should be copy-paste ready for web comparison.

### Example 1: The Spark Crash During Board Meeting

**Setup**: CFO needs quarterly analysis for board presentation in 2 hours

**Tellius Experience**:
```
Step 1: Log into Tellius platform
Step 2: Start complex financial variance calculation
Step 3: Apache Spark runs out of memory, crashes with GC overhead
Step 4: IT team called to restart cluster and tune parameters
Step 5: 4-6 hours later, cluster restarted but data may be incomplete
Step 6: "Tool hangs sometimes" - miss board meeting deadline
TIME: 4-6 hours (if successful)
RESULT: Possible missed deadline, unreliable system
```

**Scoop Experience**:
```
Step 1: Ask Scoop in Slack: "Generate variance analysis for board meeting"
Step 2: Scoop investigates data and creates PowerPoint with insights
Step 3: Review and share presentation
TIME: 30 seconds
RESULT: Professional presentation ready for board meeting
```

**Business Impact**: Tellius's Apache Spark foundation creates business risk during critical moments when reliable analytics matter most.

---

### Example 2: Excel Expert Forced Migration

**Setup**: Finance team with advanced Excel skills needs to continue their complex FP&A work

**Tellius Experience**:
```
Step 1: Told to abandon all Excel workflows and formulas
Step 2: Enroll in "citizen data scientist" training program
Step 3: Learn new platform interface and abandon VLOOKUP, pivot tables
Step 4: Rebuild all financial models in Tellius proprietary system
Step 5: Hope Apache Spark doesn't crash during month-end close
TIME: 6-month learning curve + ongoing crash risk
RESULT: Skilled team regresses to beginners, loses productivity
```

**Scoop Experience**:
```
Step 1: Continue using Excel skills you already have
Step 2: Use Scoop's 150+ Excel functions for calculations
Step 3: Ask Scoop for complex analysis in natural language
Step 4: Get results using familiar VLOOKUP, SUMIFS logic
TIME: Immediate productivity using existing skills
RESULT: Enhanced capabilities building on existing expertise
```

**Business Impact**: Tellius destroys existing organizational capabilities; Scoop amplifies them with AI power.

---

### Example 3: Natural Language Promise vs Documented Reality

**Setup**: Sales team sold on natural language analytics promise

**Tellius Experience**:
```
Step 1: Demo shows natural language interface
Step 2: Sign contract based on NL analytics promise
Step 3: 6-month implementation with professional services
Step 4: Discover Tellius's own documentation: "Natural Language Search has not been adopted"
Step 5: Acknowledge "ambiguous language, mismatched definitions, unreliable multi-step logic"
Step 6: Users fall back to "canned reports or dashboards"
TIME: 6 months to discover vendor's main feature failed
RESULT: $125,000+ investment in technology vendor admits doesn't work
```

**Scoop Experience**:
```
Step 1: Ask questions in natural language: "Why did churn increase?"
Step 2: Get multi-pass investigation with root cause analysis
Step 3: Receive confident, deterministic results with business recommendations
TIME: 30 seconds from question to actionable insight
RESULT: Natural language that actually works reliably
```

**Business Impact**: Tellius admits their core value proposition failed; Scoop delivers working conversational analytics.

---

## 10. SALES GUIDANCE (How to use this in conversations)

**Instructions**: Practical guidance for sales conversations. What questions to ask, how to position.

**Discovery Questions to Ask**:
1. "How will you handle Apache Spark memory crashes during critical business periods?"
2. "Are you willing to force your Excel experts to abandon their skills and start over?"
3. "What's your backup plan if Tellius's natural language 'hangs sometimes' like customers report?"

**If They Say**: "Tellius has enterprise features"
**We Respond**: "With 90% employee turnover and staff saying it's 'lightyears behind competitors,' how confident are you in their enterprise support quality?"

**If They Say**: "The price seems reasonable at $495/month"
**We Respond**: "That's the advertised price. Customers report $125,000+ Year 1 with Spark expertise, implementation, and training. That's 33x more than advertised."

**Demo Focus Areas** (for this competitor):
1. **Reliability**: Show Scoop's deterministic results vs "tool hangs sometimes"
2. **Excel Integration**: Demonstrate 150+ functions vs forced Excel abandonment
3. **30-second setup**: Contrast with 6-month implementations

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

- [ ] Check if Tellius has improved Apache Spark stability (**Architectural Instability**).

- [ ] Verify if native Excel integration has been added (mitigating **Workflow Destruction**).

- [ ] Review Tellius documentation for updates on Natural Language adoption (**Credibility Gap**).

- [ ] Update pricing intel (TCO trends).

- [ ] Check employee turnover and customer count metrics.



**Triggered Updates** (Update immediately when):

- Competitor announces a move away from Apache Spark architecture.

- Significant new Excel or native workflow integrations are launched.

- Major new customer wins or losses are publicized.

- BUA dimension scores change by >3 points.



**Version History**:

- 2025-11-18: Strategic update to align with "Domain Intelligence Platform" positioning. Reframed weaknesses as architectural flaws (Architectural Instability, Workflow Destruction, Credibility Gap). Integrated references to Investigation Coordinator, Spreadsheet Calculation Engine, Cloud-Native Reliability. Updated sales guidance and demo focus areas.

- September 28, 2025: Initial strategy created based on BUA 22/100 score and battle card analysis



---



**Template Version**: 1.1

**Created**: September 27, 2025

**Last Updated**: September 28, 2025
