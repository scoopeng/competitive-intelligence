# Competitive Strategy: Sisense

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

**#1: Embedded Analytics Focus (Not Business Empowerment)** (Severity: Critical | Defensibility: Architectural)
- **Evidence**: BUA Score 28/100 (Category C), Built for ISV embedding not self-service, 14+ weeks implementation, 30-80 hours training required, ElastiCube requires SQL despite "no code" claims
- **Why It Matters**: Sisense is architected for software vendors embedding analytics in their products, not for business users doing self-service analysis. This is a fundamental market mismatch for enterprise buyers
- **Our Advantage**: Scoop is architected specifically for business user autonomy - natural language chat, Excel skills leverage, 30-second setup
- **Defensibility**: Architectural - changing from embedded analytics platform to business empowerment would require complete product rewrite and abandoning their core ISV customer base
- **Emphasis Level**: 35% of web comparison

**#2: ARIMA Marketing Mirage (Fake AI)** (Severity: Critical | Defensibility: Architectural)
- **Evidence**: Uses ARIMA from 1970s and markets as "AI", Simply Ask deprecated (actual AI attempt failed), no real ML capability (0/6 BUA ML score)
- **Why It Matters**: Companies implementing "AI" analytics expect modern machine learning, not 50-year-old statistics rebranded as AI. This is deceptive marketing that leads to buyer disappointment
- **Our Advantage**: Scoop uses real ML (J48, JRip, EM clustering) with explainable outputs - actual AI data science
- **Defensibility**: Architectural - ARIMA limitation suggests they lack ML engineering capabilities. Simply Ask deprecation shows failed AI attempts
- **Emphasis Level**: 25% of web comparison

**#3: Excel Export-Only (Portal Prison)** (Severity: High | Defensibility: Architectural)
- **Evidence**: Excel export-only with 1.5M cell limit, no formulas with live data, no PowerPoint support, no scheduled emails (0/8 Native Integration, 0/6 Portal Prison BUA scores)
- **Why It Matters**: Business users need to work in Excel with live data, not static exports. Portal prison forces workflow abandonment and reduces adoption
- **Our Advantage**: Scoop native Excel formulas (150+ functions), PowerPoint generation, Slack integration - works in existing tools
- **Defensibility**: Architectural - embedded analytics platforms prioritize embedding over native tool integration by design
- **Emphasis Level**: 20% of web comparison

---

## 2. KEY SCENARIOS (Stories that expose weaknesses)

**Instructions**: Choose 2-4 real-world scenarios that make the competitor's weaknesses obvious. Good scenarios are specific, relatable, and measurable (time/cost differences).

**Scenario 1: Marketing Executive Needs Quick Customer Segmentation Analysis**
- **When to Use**: Exposes ARIMA fake AI and investigation limitations
- **Story**: CMO asks: "Why are our customer acquisition costs rising?" Sisense shows charts but can't investigate root cause or discover hidden customer segments. ARIMA can't do real customer clustering or pattern discovery
- **Expected Impact**: Shows how fake AI fails when executives need real insights beyond dashboards

**Scenario 2: Finance Analyst Updating Budget Models in Excel**
- **When to Use**: Exposes portal prison and Excel export limitations
- **Story**: Finance analyst has complex FP&A model in Excel with VLOOKUP, SUMIFS, variance analysis. Sisense exports static data (no formulas), analyst must copy/paste and rebuild all calculations manually, loses live data connection
- **Expected Impact**: Demonstrates workflow abandonment cost and productivity loss from static exports

**Scenario 3: Rapid Business Change Requiring Data Adaptation**
- **When to Use**: Exposes implementation complexity and SQL requirements
- **Story**: Company launches new product line, needs immediate analysis. Sisense requires IT to rebuild ElastiCube with SQL, 14+ weeks for changes, business moves faster than analytics can adapt
- **Expected Impact**: Shows cost of IT dependency when business needs agility

**Scenario 4: SMB Team Needing Cost-Effective Analytics**
- **When to Use**: Exposes total cost and implementation burden
- **Story**: 50-person company wants analytics, discovers Sisense requires $200K+ implementation, 14+ weeks timeline, dedicated IT resources they don't have. Perfect for embedding analytics but wrong tool for business empowerment
- **Expected Impact**: Highlights market mismatch between embedded analytics and self-service needs

---

## 3. TALKING POINTS (Emphasis hierarchy)

**Instructions**: Order these by importance. Top 3 should directly address primary weaknesses from Section 1.

**Lead With** (Most important - use these in first 1000 words):
1. Sisense built for ISV embedding, not business empowerment - *Because 14+ weeks implementation and SQL requirements prove it's an IT platform*
2. ARIMA from 1970s is statistics, not AI - Simply Ask deprecated proves real AI failed - *Because fake AI is deceptive marketing*
3. Excel export-only breaks business workflows - no formulas, no live data - *Because portal prison forces tool abandonment*

**Always Mention** (Standard Scoop advantages):
4. 30-second setup vs 14+ weeks implementation timeline
5. Natural language investigation vs dashboard navigation only
6. Real ML (J48, EM clustering) with business explanations vs statistical methods
7. 400% renewal price increases vs flat pricing

**De-Emphasize** (Don't lead with these, minor mentions only):
- Mobile experience (both tools adequate for mobile)
- Dashboard quality (Sisense actually has decent embedded dashboards)
- Data connectivity (Sisense has adequate connectors)

---

## 4. CONTENT DISTRIBUTION (Word allocation for 7,500-word comparison)

**Instructions**: Allocate percentages based on competitor weaknesses and defensibility. Emphasize architectural limitations (competitor cannot easily fix), de-emphasize temporal limitations (may improve).

**Emphasis Adjustment Philosophy**:
- ⬆️ INCREASE emphasis on architectural limitations (competitor cannot easily fix)
- ⬇️ DECREASE emphasis on temporal limitations (may improve with better models/updates)
- ⬆️ INCREASE where competitor gap is widest (BUA dimension <5/20)
- ⬆️ INCREASE where differentiation is clearest and most measurable
- ⬇️ DECREASE where competitor is adequate or gap is narrow

**Recommended Mix**:
- **Section 1 (Executive Summary)**: 15% (~1,125 words)
- **Section 2 (Capabilities)**: 55% (~4,125 words)
  - Investigation & Analysis: 15% (investigation gap, ARIMA vs real ML)
  - Spreadsheet Engine: 12% (Excel export vs formula support)
  - ML & Pattern Discovery: 15% (ARIMA fake AI vs real ML - biggest differentiation)
  - Setup & Implementation: 8% (14+ weeks vs 30 seconds)
  - Schema Evolution: 5% (standard BI limitation)
- **Section 3 (Cost/TCO)**: 12% (~900 words)
- **Section 4 (Use Cases)**: 10% (~750 words)
- **Section 5-7 (FAQ/Evidence/Next Steps)**: 8% (~600 words)

**Rationale**:
ML section gets highest allocation because ARIMA fake AI is most defensible attack - they can't easily fix fundamental lack of ML capabilities. Excel limitations and embedded analytics focus are also architectural. De-emphasize schema evolution since it's universal BI limitation.

**Comparison to Default**:
- ⬆️ Increased: ML section (normally 8%, now 15%) - Because ARIMA fake AI is most defensible architectural limitation
- ⬆️ Increased: Investigation section (normally 8%, now 15%) - Because investigation gap exposes embedded analytics focus
- ⬇️ Decreased: Schema Evolution (normally 8%, now 5%) - Because Sisense isn't worse than other BI tools here

---

## 5. PROOF POINTS (Evidence to cite)

**Instructions**: Pull specific evidence that supports your positioning. Link to framework_scoring.md and research files.

**From Framework Scoring** (`evidence/framework_scoring.md`):
- **BUA Total**: 28/100 (Category C - Weak)
- **Lowest Dimension**: Flow (4/20) - Portal prison and export-only limitations
- **Critical Sub-Scores**:
  - Setup: 0/8 (14+ weeks implementation, 30-80 hours training, SQL required)
  - Native Integration: 0/8 (Excel export-only, no formulas, no PowerPoint)
  - Portal Prison: 0/6 (Must log into portal, no scheduled emails)
  - ML: 0/6 (ARIMA not ML, Simply Ask deprecated)

**From Research** (`evidence/research_library.md` or other sources):
- "14+ week implementation typical" - Phase 2 research
- "30-80 hours of training needed" - Sisense Academy documentation
- "ARIMA forecasting, regression analysis" - Phase 2, statistical methods from 1970s
- "Simply Ask (DEPRECATED) - Natural language failed, being replaced" - Phase 2
- "400% price increase at renewal time" - Customer reports with URLs

**From Public Documentation**:
- ElastiCube requires SQL despite "no code" claims - Phase 2 research
- Export to Excel static only, no live formulas - Phase 2 limitations analysis
- No PowerPoint capability found - Phase 2 comprehensive review

---

## 6. WIN CONDITIONS (What makes us win)

**Instructions**: Be specific about when Scoop wins vs loses. Honesty here prevents wasted sales cycles.

**We Win When**:
1. Business users need self-service analytics without IT gatekeeping - *Because Sisense requires 14+ weeks IT implementation*
2. Team has Excel skills and wants to leverage them - *Because Sisense export-only breaks Excel workflows*
3. Need real AI investigation, not just dashboards - *Because ARIMA isn't AI and can't investigate "why" questions*
4. Budget constraints or need quick ROI - *Because Sisense costs 56x more with $200K+ implementation*
5. Want to work in existing tools (Excel, Slack, PowerPoint) - *Because Sisense is portal-based platform*

**We Lose When** (Be honest):
- Need analytics embedded in software product for end customers (ISV use case where Sisense excels)
- Already invested heavily in Sisense and switching cost exceeds benefit
- Regulatory requirement for specific BI platform governance features

**Neutral** (Could go either way):
- Pure dashboard creation needs (both tools can create dashboards, question is self-service vs IT-built)

---

## 7. COMPETITIVE POSITIONING

**Instructions**: Craft the core positioning message. Start with product type classification to set the frame, then build specific positioning.

**Product Type Classification**:
- **What They Really Are**: Embedded analytics platform for ISV software vendors
- **What We Really Are**: AI data analyst for business users
- **Their Primary Audience**: Software vendors building embedded analytics, IT teams implementing BI
- **Our Primary Audience**: Business users with Excel skills needing self-service analytics
- **Key Architectural Difference**: Sisense optimizes for white-label embedding in software products, Scoop optimizes for business user autonomy

**One-Sentence Position**:
"Sisense is an embedded analytics platform for software vendors, Scoop is an AI data analyst for business users"

**Elevator Pitch** (30 seconds, ~60 words):
Sisense markets 1970s ARIMA statistics as "AI" while requiring 14+ weeks of IT implementation for what they call "no code" analytics. They're built for software vendors embedding analytics, not business empowerment. Scoop provides real AI investigation with 30-second setup - actual machine learning for actual business users.

**Key Contrast**:
| Dimension | Sisense | Scoop |
|-----------|---------|-------|
| **Product Type** | Embedded analytics platform for ISVs | AI data analyst / Business analytics platform |
| **Built For** | Software vendors, IT implementations | Business users with Excel skills |
| **Primary Interface** | Portal with embedded dashboards | Slack + Excel + PowerPoint |
| **Deliverable** | White-label BI for software products | Branded presentations with insights |
| **Setup Time** | 14+ weeks with IT implementation | 30 seconds |

---

## 8. AVOID OVER-CLAIMING (Credibility guardrails)

**Instructions**: List things we should NOT say because they're inaccurate or unprovable. Prevents credibility damage.

**Don't Say** (Risks credibility):
- "Sisense has no AI capabilities" - *Because they do have ARIMA and attempted Simply Ask*
- "Sisense dashboards are bad" - *Because their embedded dashboard quality is actually decent*
- "Sisense can't connect to data sources" - *Because they have adequate connector library*
- "Sisense has no legitimate use cases" - *Because ISV embedding is a valid use case*

**Instead Say** (Evidence-based alternatives):
- "Sisense uses ARIMA from 1970s, not modern ML - Simply Ask deprecated" - *Supported by technical documentation*
- "Sisense dashboards require 14+ weeks IT implementation" - *Supported by customer reports*
- "Sisense requires SQL expertise despite 'no code' claims" - *Supported by ElastiCube documentation*
- "Sisense built for ISV embedding, not business user empowerment" - *Supported by architecture and customer profile*

---

## 9. CUSTOM CONTENT BLOCKS (Competitor-specific examples)

**Instructions**: Write 2-3 specific examples or comparisons that are unique to this competitor. These should be copy-paste ready for web comparison.

### Example 1: The "AI" Investigation Reality Check

**Setup**: Marketing director asks "Why did our customer acquisition cost increase 40% this quarter?"

**Sisense Experience**:
```
Step 1: Log into Sisense portal
Step 2: Navigate to pre-built customer acquisition dashboard
Step 3: View charts showing CAC increased from $120 to $168
Step 4: Try Simply Ask: "Why did CAC increase?" → Feature deprecated, redirect to new beta
Step 5: Try ARIMA forecasting → Shows statistical trend projection, not cause analysis
Step 6: Request IT to build custom analysis (2-4 weeks estimated)
TIME: 2-4 weeks for any "why" investigation
RESULT: Charts showing what happened, no investigation of why
```

**Scoop Experience**:
```
Step 1: Ask in Slack: "Why did our customer acquisition cost increase 40% this quarter?"
Step 2: Scoop investigates with ML - tests 7 hypotheses, runs 9 queries automatically
Step 3: Receive analysis: "Primary cause: iOS 14.5 privacy changes reduced Facebook attribution 67%, shifted budget to more expensive channels. Secondary: Enterprise deals requiring longer sales cycles increased. Recommendation: Increase content marketing budget by $40K to compensate."
TIME: 30 seconds
RESULT: Root cause analysis with specific recommendations and confidence scoring
```

**Business Impact**: Real investigation capability vs statistical trending that marketing calls "AI"

---

### Example 2: Excel Workflow Integration Test

**Setup**: Finance analyst needs to integrate live sales data into quarterly budget variance model

**Sisense Experience**:
```
Step 1: Export sales data from Sisense (static CSV, 1.5M cell limit)
Step 2: Open Excel budget model with complex VLOOKUP, SUMIFS formulas
Step 3: Copy/paste static data, breaking all formula references
Step 4: Manually rebuild all calculations for new data structure
Step 5: No live connection - must repeat entire process when data updates
Step 6: Create manual process to export weekly, rebuild formulas each time
TIME: 2-3 hours initial setup, 30-45 minutes weekly maintenance
RESULT: Static analysis, broken each time data changes
```

**Scoop Experience**:
```
Step 1: In Excel budget model, add formula: =SCOOP("Q4 sales by region and rep")
Step 2: All VLOOKUP, SUMIFS, variance calculations work immediately with live data
Step 3: Formula refreshes automatically when underlying data changes
TIME: 30 seconds setup, automatic updates
RESULT: Live Excel integration with all existing formulas working
```

**Business Impact**: Native Excel workflow vs forced manual export/import process

---

### Example 3: Implementation Reality for 200-Person Company

**Setup**: Growing company needs analytics platform for all departments

**Sisense Experience**:
```
Step 1: Sales process + demo (4-6 weeks)
Step 2: Contract negotiation for custom pricing (2-3 weeks)
Step 3: Plan ElastiCube architecture (2 weeks)
Step 4: Build data models with SQL expertise (4-6 weeks)
Step 5: Configure dashboards and security (2-3 weeks)
Step 6: Train users on Sisense Academy curriculum (30-80 hours per user)
Step 7: Deploy and troubleshoot (1-2 weeks)
TOTAL TIME: 14+ weeks
TOTAL COST: $200K+ (licenses + implementation + training)
RESULT: IT-managed BI platform requiring ongoing maintenance
```

**Scoop Experience**:
```
Step 1: Sign up and connect data source (30 seconds)
Step 2: Ask first business question, get answer (30 seconds)
Step 3: Share with team via Slack integration (immediate)
TOTAL TIME: 30 seconds
TOTAL COST: $3,588/year
RESULT: Self-service AI analytics with zero IT burden
```

**Business Impact**: 56x cost difference, 840x time difference for same outcome

---

## 10. SALES GUIDANCE (How to use this in conversations)

**Instructions**: Practical guidance for sales conversations. What questions to ask, how to position.

**Discovery Questions to Ask**:
1. "What happened when you tried to get insights beyond basic dashboards?" (Exposes ARIMA limitation)
2. "How long did your Sisense implementation take and what role did IT play?" (Exposes implementation complexity)
3. "Do your analysts work primarily in Excel or in the Sisense portal?" (Exposes workflow integration gap)
4. "What was your experience with Simply Ask or their AI features?" (Exposes deprecated features)

**If They Say**: "Sisense has AI capabilities"
**We Respond**: "They use ARIMA from 1970s and call it AI. They actually deprecated Simply Ask because it didn't work. ARIMA is statistics, not machine learning - here's the difference and why it matters for business decisions."

**If They Say**: "Sisense is a mature, established platform"
**We Respond**: "Mature often means legacy. They're designed for ISVs embedding analytics in software products, not business user empowerment. That's why they require 14+ weeks implementation and SQL expertise - different market entirely."

**If They Say**: "We need embedded analytics capabilities"
**We Respond**: "Then you're building software products for end customers, not empowering internal business users. Sisense is great for ISVs, but if you need business analytics, you want user empowerment, not white-label embedding."

**Demo Focus Areas** (for this competitor):
1. Real ML investigation - Contrasts with ARIMA statistical trending
2. Native Excel formula support - Contrasts with export-only static data
3. 30-second setup process - Contrasts with 14+ week IT implementations

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
- September 28, 2025: Initial strategy based on BUA 28/100 scoring and comprehensive Phase 2/3 research

---

**Template Version**: 1.1
**Created**: September 28, 2025
**Last Updated**: September 28, 2025