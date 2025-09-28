# Competitive Strategy: Tellius

**Last Updated**: September 28, 2025
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

**#1: Apache Spark Architecture Crashes** (Severity: Critical | Defensibility: Architectural)
- **Evidence**: "Tool hangs sometimes" (G2 reviews), Apache Spark memory crashes, GC overhead, "notoriously difficult to tune"
- **Why It Matters**: Core platform reliability - if the foundation crashes, nothing else matters for business decisions
- **Our Advantage**: Stable, proven architecture that doesn't require Spark expertise or crash management
- **Defensibility**: Architectural - they built entire platform on Spark, cannot easily change without complete rebuild
- **Emphasis Level**: 25% of web comparison

**#2: Complete Excel Elimination (Zero Native Integration)** (Severity: Critical | Defensibility: Strategic)
- **Evidence**: BUA Flow 0/20, "Tellius wants to REPLACE Excel, not enhance it", zero Excel formula engine
- **Why It Matters**: Forces complete workflow abandonment vs enhancement - destroys user productivity instead of amplifying it
- **Our Advantage**: 150+ Excel functions, enhances existing skills rather than replacing them
- **Defensibility**: Strategic - they chose replacement strategy, could build Excel support but philosophically opposed
- **Emphasis Level**: 25% of web comparison

**#3: Natural Language Adoption Failure (Tellius's Own Admission)** (Severity: High | Defensibility: Temporal)
- **Evidence**: "Natural Language Search has not been adopted for analytics" (Tellius documentation), "ambiguous language, mismatched definitions, unreliable multi-step logic"
- **Why It Matters**: Their main value proposition doesn't work - admitted by the vendor themselves
- **Our Advantage**: Conversational interface that actually works with Excel-like reliability
- **Defensibility**: Temporal - they could improve NL but have admitted failure after years of trying
- **Emphasis Level**: 20% of web comparison

---

## 2. KEY SCENARIOS (Stories that expose weaknesses)

**Instructions**: Choose 2-4 real-world scenarios that make the competitor's weaknesses obvious. Good scenarios are specific, relatable, and measurable (time/cost differences).

**Scenario 1: Emergency Data Analysis During Spark Crash**
- **When to Use**: Exposes reliability weakness (#1)
- **Story**: Financial analyst needs quarterly variance analysis for board meeting in 2 hours. Tellius Spark cluster crashes with memory overflow during complex calculation. IT estimates 4-6 hours to restart and tune parameters.
- **Expected Impact**: Demonstrates that unstable architecture creates business risk during critical moments

**Scenario 2: Excel Power User Forced Platform Migration**
- **When to Use**: Exposes Excel replacement strategy (#2)
- **Story**: CFO team with advanced Excel skills (pivot tables, VLOOKUP, complex formulas) told they must abandon Excel completely and learn Tellius interface for "citizen data scientist" training.
- **Expected Impact**: Shows workflow destruction vs enhancement - forces regression of existing skills

**Scenario 3: Natural Language Promise vs Reality**
- **When to Use**: Exposes NL failure (#3)
- **Story**: Sales team demo'd natural language analytics, but after 6-month implementation discover Tellius admits NL "has not been adopted" and most users "still rely on canned reports or dashboards."
- **Expected Impact**: Vendor admits their main selling point failed - credibility destroyer

**Scenario 4: Hidden Cost Explosion**
- **When to Use**: Exposes true TCO vs advertised pricing
- **Story**: $495/month advertised cost becomes $125,000+ Year 1 with Spark expertise, implementation, training, and professional services requirements.
- **Expected Impact**: 33x cost increase from advertised price - demonstrates deceptive pricing

---

## 3. TALKING POINTS (Emphasis hierarchy)

**Instructions**: Order these by importance. Top 3 should directly address primary weaknesses from Section 1.

**Lead With** (Most important - use these in first 1000 words):
1. **Apache Spark reliability crisis** - *Because their foundation crashes during analysis ("tool hangs sometimes")*
2. **Zero Excel support destroys workflows** - *Because they force complete abandonment of existing skills vs enhancement*
3. **Natural language failure (vendor admitted)** - *Because Tellius documented that NL "has not been adopted"*

**Always Mention** (Standard Scoop advantages):
4. **30 seconds vs 6-month implementations** - *90-day vs instant value*
5. **$3,588 vs $125,000+ true cost** - *33x price difference*
6. **Investigation engine vs single queries** - *Multi-pass analysis vs basic reporting*

**De-Emphasize** (Don't lead with these, minor mentions only):
- **Visualization capabilities** - Tellius has adequate charts, not a key differentiator
- **Data connectivity** - They score 4/4 on multi-source, this is table stakes

---

## 4. CONTENT DISTRIBUTION (Word allocation for 7,500-word comparison)

**Instructions**: Allocate percentages based on competitor weaknesses and defensibility. Emphasize architectural limitations (hard for competitor to fix), de-emphasize temporal limitations (may improve).

**Emphasis Adjustment Philosophy**:
- ⬆️ INCREASE emphasis on architectural limitations (competitor cannot easily fix)
- ⬇️ DECREASE emphasis on temporal limitations (may improve with better models/updates)
- ⬆️ INCREASE where competitor gap is widest (BUA dimension <5/20)
- ⬆️ INCREASE where differentiation is clearest and most measurable
- ⬇️ DECREASE where competitor is adequate or gap is narrow

**Recommended Mix**:
- **Section 1 (Executive Summary)**: 15% (~1,125 words)
- **Section 2 (Capabilities)**: 55% (~4,125 words)
  - Apache Spark Reliability Issues: 15%
  - Excel/Spreadsheet Engine: 15%
  - Natural Language Failure: 10%
  - Setup/Implementation: 10%
  - Schema Evolution: 5%
- **Section 3 (Cost/TCO)**: 15% (~1,125 words)
- **Section 4 (Use Cases)**: 10% (~750 words)
- **Section 5-7 (FAQ/Evidence/Next Steps)**: 5% (~375 words)

**Rationale**:
Heavy emphasis on capabilities because that's where all three primary weaknesses live. Apache Spark crashes and Excel elimination are architectural issues Tellius cannot easily fix. Natural language failure is documented by Tellius themselves. Cost section important because true cost is 33x advertised price.

**Comparison to Default**:
- ⬆️ Increased: Capabilities section (normally 40%, now 55%) - Because all three architectural weaknesses are capability-based
- ⬇️ Decreased: Use Cases section (normally 15%, now 10%) - Because focus should be on fundamental platform failures

---

## 5. PROOF POINTS (Evidence to cite)

**Instructions**: Pull specific evidence that supports your positioning. Link to framework_scoring.md and research files.

**From Framework Scoring** (`evidence/framework_scoring.md`):
- **BUA Total**: 22/100 (Category D - Poor)
- **Lowest Dimension**: Flow 0/20 (complete failure on native integration)
- **Critical Sub-Scores**:
  - Native Integration: 0/8 (forces Excel replacement)
  - Portal Prison: 0/6 (100% platform dependency)
  - Setup: 0/8 (6-week to 6-month implementations)
  - Schema Evolution: 0/8 (universal BI platform failure)

**From Research** (`BATTLE_CARD.md` and battle card sources):
- "The tool hangs sometimes" - G2 customer review
- "Natural Language Search has not been adopted for analytics" - Tellius's own documentation
- "90% employee turnover" with "lightyears behind competitors" - Glassdoor employee reviews
- "31 customers globally" after 8 years - extreme market failure

**From Public Documentation**:
- "eliminate manual Excel work that traditionally involves tedious copy-pasting and VLOOKUP formulas" - Official positioning against Excel
- "$495/month (Premium)" vs $125,000+ Year 1 reality - pricing documentation vs customer reports
- "6-week to 6-month implementations" - implementation documentation

---

## 6. WIN CONDITIONS (What makes us win)

**Instructions**: Be specific about when Scoop wins vs loses. Honesty here prevents wasted sales cycles.

**We Win When**:
1. **Business users need reliable analytics** - *Because Spark crashes make Tellius unreliable*
2. **Excel skills are organizational strength** - *Because Tellius forces abandonment of existing capabilities*
3. **Fast time-to-value required** - *Because 30 seconds vs 6 months is 1000x faster*
4. **Budget constraints exist** - *Because $3,588 vs $125,000+ is 33x savings*
5. **Natural language actually needs to work** - *Because Tellius admits their NL "has not been adopted"*
6. **Company stability matters** - *Because 90% turnover indicates vendor risk*

**We Lose When** (Be honest):
- Customer specifically needs Tellius's investigation capabilities and can tolerate crashes/complexity (rare edge case)
- Budget unlimited and complexity acceptable for specialized use case

**Neutral** (Could go either way):
- Advanced ML scenarios where both have capabilities (though Scoop's explainable ML usually wins)

---

## 7. COMPETITIVE POSITIONING

**Instructions**: Craft the core positioning message. Start with product type classification to set the frame, then build specific positioning.

**Product Type Classification**:
- **What They Really Are**: Enterprise analytics platform with Apache Spark foundation requiring "citizen data scientist" training
- **What We Really Are**: AI data analyst you chat with
- **Their Primary Audience**: Technical analysts willing to abandon Excel and manage Spark complexity
- **Our Primary Audience**: Business users with Excel skills who need reliable answers
- **Key Architectural Difference**: Tellius built on unstable Spark requiring expertise; Scoop built on stable platform for business users

**One-Sentence Position**:
"Tellius is an enterprise analytics platform for technical users who can manage Apache Spark crashes, Scoop is an AI data analyst for business users who need reliable answers in 30 seconds."

**Elevator Pitch** (30 seconds, ~60 words):
Tellius requires 6-month implementations, "citizen data scientist" training, and forces complete Excel abandonment—plus their own documentation admits natural language "has not been adopted." Meanwhile customers report "tool hangs sometimes" due to Apache Spark crashes. Scoop is an AI data analyst you chat with—30-second setup, works with your Excel skills, always reliable.

**Key Contrast**:
| Dimension | Tellius | Scoop |
|-----------|---------|-------|
| **Product Type** | Enterprise analytics platform | AI data analyst you chat with |
| **Built For** | "Citizen data scientists" | Business users with Excel skills |
| **Primary Interface** | Complex platform requiring training | Natural conversation (Slack + Excel) |
| **Deliverable** | Dashboard portal (if Spark doesn't crash) | Branded presentations with insights |
| **Setup Time** | 6 weeks to 6 months | 30 seconds |

---

## 8. AVOID OVER-CLAIMING (Credibility guardrails)

**Instructions**: List things we should NOT say because they're inaccurate or unprovable. Prevents credibility damage.

**Don't Say** (Risks credibility):
- "Tellius never works" - *Because they do have some successful customers despite low adoption*
- "Apache Spark always crashes" - *Because saying "always" is unprovable, better to quote customer "hangs sometimes"*
- "All 31 customers are unhappy" - *Because we don't have evidence on all customers*

**Instead Say** (Evidence-based alternatives):
- "Customers report 'tool hangs sometimes' due to Spark issues" - *Supported by G2 reviews*
- "90% employee turnover with staff saying 'lightyears behind competitors'" - *Supported by Glassdoor*
- "Only 31 customers globally after 8 years indicates adoption challenges" - *Supported by research*

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
- September 28, 2025: Initial strategy created based on BUA 22/100 score and battle card analysis

---

**Template Version**: 1.1
**Created**: September 27, 2025
**Last Updated**: September 28, 2025