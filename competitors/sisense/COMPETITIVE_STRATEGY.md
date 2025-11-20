# Competitive Strategy: Sisense

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

**#1: Architectural Mismatch: Embedded Focus vs. Domain Intelligence** (Severity: Critical | Defensibility: Architectural)
- **Evidence**: BUA Score 28/100 (Category C), Built for ISV embedding not self-service, 14+ weeks implementation, 30-80 hours training required, ElastiCube requires SQL despite "no code" claims
- **Why It Matters**: Sisense is architected for software vendors embedding analytics in their products, not for business users needing **Domain Intelligence**. This architectural focus creates barriers to self-service investigation and operationalizing expertise within an enterprise.
- **Our Advantage**: Scoop is a **Domain Intelligence Platform** architected for business user autonomy and **Autonomous Investigation**. We offer natural language investigation, leverage **Encoded Expertise** (Schema v2.8), and deploy in minutes, not months.
- **Defensibility**: Architectural - changing from an embedded analytics platform to a **Domain Intelligence** platform would require a complete product rewrite and abandoning their core ISV customer base.
- **Emphasis Level**: 35% of web comparison

**#2: Intelligence Ceiling: Legacy Statistics vs. Encoded Expertise** (Severity: Critical | Defensibility: Architectural)
- **Evidence**: Uses ARIMA from 1970s and markets as "AI", Simply Ask deprecated (actual AI attempt failed), no real ML capability (0/6 BUA ML score)
- **Why It Matters**: Sisense relies on legacy statistical methods (ARIMA) and markets them as AI, creating an **Intelligence Ceiling**. It cannot encode complex business rules or perform AI-driven pattern discovery. Companies expecting modern machine learning get 50-year-old math.
- **Our Advantage**: Scoop leverages **Encoded Expertise** and real ML (J48, JRip, EM clustering) to explain anomalies based on your specific business logic. We operationalize expertise, we don't just project trends.
- **Defensibility**: Architectural - The reliance on legacy statistics and the failure of "Simply Ask" suggests a fundamental inability to pivot to modern **Encoded Expertise** and AI.
- **Emphasis Level**: 25% of web comparison

**#3: Workflow Disruption: Portal Prison vs. True Workflow Integration** (Severity: High | Defensibility: Architectural)
- **Evidence**: Excel export-only with 1.5M cell limit, no formulas with live data, no PowerPoint support, no scheduled emails (0/8 Native Integration, 0/6 Portal Prison BUA scores)
- **Why It Matters**: Sisense forces business users into a "Portal Prison," breaking workflows. Users need to work in Excel with live data and generate presentations automatically. The lack of integration causes **Workflow Disruption** and tool abandonment.
- **Our Advantage**: Scoop offers **True Workflow Integration**. Native in Slack, Excel (150+ formulas with live data via **Spreadsheet Calculation Engine**), and **Automated Presentation Generation**.
- **Defensibility**: Architectural - embedded analytics platforms prioritize embedding in third-party apps over native office tool integration by design.
- **Emphasis Level**: 20% of web comparison

---

## 2. KEY SCENARIOS (Stories that expose weaknesses)

**Instructions**: Choose 2-4 real-world scenarios that make the competitor's weaknesses obvious. Good scenarios are specific, relatable, and measurable (time/cost differences).

**Scenario 1: Intelligence Ceiling: Legacy Statistics vs. Autonomous Investigation**
- **When to Use**: Exposes ARIMA "fake AI" and the lack of true investigation capabilities.
- **Story**: "A CMO asks: 'Why are our customer acquisition costs rising?' Sisense, relying on legacy ARIMA statistics, shows charts and trend lines but hits an **Intelligence Ceiling**. It cannot investigate root causes or discover hidden segments. Scoop's **Investigation Coordinator** autonomously tests hypotheses (e.g., ad spend shift, channel saturation) leveraging **Encoded Expertise**, identifying the specific driver and recommending action."
- **Expected Impact**: Shows how legacy statistics fail to deliver the actionable intelligence that executives demand, contrasting with Scoop's **Autonomous Investigation**.

**Scenario 2: Workflow Disruption: Static Export vs. Spreadsheet Calculation Engine**
- **When to Use**: Exposes portal prison and Excel export limitations.
- **Story**: "A finance analyst manages a complex FP&A model in Excel. Sisense offers only a static export (no formulas), forcing the analyst to manually rebuild VLOOKUPs and SUMIFS, breaking the workflow. This is **Workflow Disruption**. Scoop's **Spreadsheet Calculation Engine** allows the analyst to use live data with 150+ native Excel functions directly in their model. No manual rebuilding, no broken links—**True Workflow Integration**."
- **Expected Impact**: Demonstrates the productivity loss from static exports and the value of operationalizing expertise in native tools.

**Scenario 3: Architectural Mismatch: Rigid Implementation vs. Agile Domain Intelligence**
- **When to Use**: Exposes implementation complexity and SQL requirements.
- **Story**: "A company launches a new product line and needs immediate analysis. Sisense requires IT to rebuild the ElastiCube with SQL, a 14+ week process that lags behind business needs. This is an **Architectural Mismatch** for agile intelligence. Scoop's **Schema Evolution** automatically adapts to the new data, allowing business users to ask questions immediately. Zero downtime, zero IT bottleneck."
- **Expected Impact**: Shows the high cost of IT dependency when agility is critical.

**Scenario 4: TCO Trap: Embedded Platform Costs for Business Needs**
- **When to Use**: Exposes total cost and implementation burden.
- **Story**: "A 50-person company needing internal analytics discovers Sisense requires a $200K+ implementation and dedicated IT resources. They are buying an embedded platform for software vendors, not a business tool. Scoop offers a flat, predictable cost and deploys in minutes. We eliminate the labor categories Sisense mandates."
- **Expected Impact**: Highlights the market mismatch and **TCO Trap** of using an embedded platform for internal business intelligence.

---

## 3. TALKING POINTS (Emphasis hierarchy)

**Instructions**: Order these by importance. Top 3 should directly address primary weaknesses from Section 1.

**Lead With** (Most important - use these in first 1000 words):
1.  **"Embedded Platform vs. Domain Intelligence (Architectural Mismatch)"** - *Sisense is built for ISVs; Scoop is built for business user autonomy and Encoded Expertise.*
2.  **"Legacy Statistics vs. Autonomous Investigation (Intelligence Ceiling)"** - *ARIMA is 1970s math; Scoop's **Investigation Coordinator** is modern AI investigation.*
3.  **"Portal Prison vs. True Workflow Integration"** - *Static exports break workflows; Scoop's **Spreadsheet Calculation Engine** enables live analysis in Excel.*

**Always Mention** (Standard Scoop advantages):
4.  **Investigation Coordinator** (Multi-step autonomous reasoning vs. dashboard navigation).
5.  **Spreadsheet Calculation Engine** (150+ native Excel formulas vs. static export).
6.  **Schema v2.8 with Encoded Expertise** (Operationalizing business rules vs. IT-defined ElastiCubes).
7.  **30-Second Setup** (vs. 14+ weeks implementation and training).
8.  **Eliminated Labor Categories** (No IT maintenance vs. SQL-required ElastiCube management).

**De-Emphasize** (Don't lead with these, minor mentions only):
- **Mobile experience** (Both have adequate mobile capabilities, though Sisense is dashboard-focused).
- **Dashboard quality** (Sisense has strong embedded dashboards; focus on the lack of investigation).
- **Data connectivity** (Sisense has connectors; focus on the setup burden).

---

## 4. CONTENT DISTRIBUTION (Word allocation for 7,500-word comparison)

**Instructions**: Allocate percentages based on competitor weaknesses and defensibility. Emphasize architectural limitations (competitor cannot easily fix), de-emphasize temporal limitations (may improve).

**Emphasis Adjustment Philosophy**:
- ⬆️ INCREASE on **Architectural Mismatch** (Embedded vs. Business User focus).
- ⬆️ INCREASE on **Intelligence Ceiling** (Legacy Statistics vs. AI Investigation).
- ⬆️ INCREASE on **Workflow Disruption** (Portal Prison vs. True Integration).

**Recommended Mix**:
- **Section 1 (Executive Summary)**: 15% (~1,125 words)
- **Section 2 (Capabilities)**: 55% (~4,125 words)
  - **Architectural Mismatch & Embedded Focus**: 20% (Highlighting ISV design vs. Business User autonomy).
  - **Intelligence Ceiling & Legacy AI**: 15% (Contrasting ARIMA/deprecated features with **Investigation Coordinator**).
  - **Workflow Disruption & Integration**: 12% (Static export vs. **Spreadsheet Calculation Engine**).
  - **Setup & Implementation**: 8% (14+ weeks vs. 30 seconds).
  - **Schema Evolution**: 5% (Standard BI limitation).
- **Section 3 (Cost/TCO)**: 12% (~900 words) - Focusing on **TCO Trap** and high implementation costs.
- **Section 4 (Use Cases)**: 10% (~750 words)
- **Section 5-7 (FAQ/Evidence/Next Steps)**: 8% (~600 words)

**Rationale**:
The most critical differentiators are the fundamental **Architectural Mismatch** (Sisense isn't built for business users) and the **Intelligence Ceiling** (fake AI). These are defensible, architectural weaknesses. Workflow disruption is a key practical pain point.

---

## 5. PROOF POINTS (Evidence to cite)

**Instructions**: Pull specific evidence that supports your positioning. Link to framework_scoring.md and research files.

**From Framework Scoring** (`evidence/framework_scoring.md`):
- **BUA Total**: 28/100 (Category C - Weak)
- **Lowest Dimension**: Flow (4/20) - Evidence of **Workflow Disruption**.
- **Critical Sub-Scores**:
  - **Setup**: 0/8 (14+ weeks implementation, 30-80 hours training - Evidence of **Architectural Mismatch**).
  - **Native Integration**: 0/8 (Excel export-only, no formulas - Evidence of **Workflow Disruption**).
  - **Portal Prison**: 0/6 (Must log into portal - Further **Workflow Disruption**).
  - **ML**: 0/6 (ARIMA not ML, Simply Ask deprecated - Evidence of **Intelligence Ceiling**).

**From Research** (`evidence/research_library.md` or other sources):
- "14+ week implementation typical" - Supports **Architectural Mismatch**.
- "30-80 hours of training needed" - Supports **Architectural Mismatch** and lack of business empowerment.
- "ARIMA forecasting, regression analysis" - Supports **Intelligence Ceiling** (legacy statistics).
- "Simply Ask (DEPRECATED)" - Proves failure of AI attempts, reinforcing **Intelligence Ceiling**.
- "400% price increase at renewal time" - Evidence of **TCO Trap**.

**From Public Documentation**:
- ElastiCube requires SQL despite "no code" claims - Supports **Architectural Mismatch** for business users.
- Export to Excel static only, no live formulas - Supports **Workflow Disruption**.
- No PowerPoint capability found - Supports **Workflow Disruption**.

---

## 6. WIN CONDITIONS (What makes us win)

**Instructions**: Be specific about when Scoop wins vs loses. Honesty here prevents wasted sales cycles.

**We Win When**:
1.  **Business User Autonomy is Critical**: When the goal is self-service without IT gatekeeping, avoiding Sisense's **Architectural Mismatch** (14+ weeks implementation).
2.  **True Workflow Integration is Required**: When users need to work natively in Excel with formulas (leveraging our **Spreadsheet Calculation Engine**) rather than dealing with Sisense's static exports and **Workflow Disruption**.
3.  **Real AI Investigation is Demanded**: When the customer needs **Autonomous Investigation** and root cause analysis, not 1970s ARIMA statistics (**Intelligence Ceiling**).
4.  **Agility and Time-to-Value Matter**: When 30-second setup beats 14+ weeks, and predictable costs beat the **TCO Trap** of implementation fees and renewal hikes.
5.  **Native Tool Access is Key**: When users want to stay in Slack and PowerPoint, avoiding the "Portal Prison."

**We Lose When** (Be honest):
- Need analytics embedded in software product for end customers (ISV use case where Sisense excels).
- Already invested heavily in Sisense and switching cost exceeds benefit.
- Regulatory requirement for specific BI platform governance features that Sisense provides for on-prem/cloud hybrid deployments.

**Neutral** (Could go either way):
- Pure dashboard creation needs (both tools can create dashboards, but Scoop offers **Domain Intelligence** on top).

---

## 7. COMPETITIVE POSITIONING

**Instructions**: Craft the core positioning message. Start with product type classification to set the frame, then build specific positioning.

**Product Type Classification**:
- **What They Really Are**: Embedded Analytics Platform for ISVs (Legacy Architecture)
- **What We Really Are**: **Cloud-Native Domain Intelligence Platform** (for Business User Autonomy)
- **Their Primary Audience**: Software vendors and IT teams building embedded analytics
- **Our Primary Audience**: Business users needing immediate insights and **True Workflow Integration**
- **Key Architectural Difference**: 14+ weeks implementation (IT-driven) vs. 30-second setup (**Encoded Expertise**).

**One-Sentence Position**:
"Sisense is an embedded analytics platform for software vendors that relies on legacy statistics and IT-heavy implementation; Scoop is a **Domain Intelligence Platform** that operationalizes **Encoded Expertise** for autonomous investigation and instant business user value."

**Elevator Pitch** (30 seconds, ~60 words):
"Sisense markets 1970s ARIMA statistics as 'AI' while requiring 14+ weeks of IT implementation. It is architecturally built for software vendors to embed dashboards, not for business empowerment. Scoop provides a **Domain Intelligence Platform** with **Autonomous Investigation**, **True Workflow Integration** (native Excel/Slack), and 30-second setup. We deliver real AI and operationalized expertise, not just statistical trends."

**Key Contrast**:
| Dimension | Sisense | Scoop |
|-----------|---------|-------|
| **Product Type** | Embedded Analytics for ISVs | **Domain Intelligence Platform** |
| **Core Mechanism** | Legacy Statistics (ARIMA) | **Investigation Coordinator (AI)** |
| **Workflow** | Portal Prison / Static Export | **True Workflow Integration** |
| **Investigation** | Manual / Statistical Trending | **Autonomous Root Cause Analysis** |
| **Setup Time** | 14+ Weeks (IT Heavy) | **30 Seconds (Zero Config)** |
| **Costs** | High Implementation + Renewal Hikes | **Flat / Predictable (Eliminated Labor)** |

---

## 8. AVOID OVER-CLAIMING (Credibility guardrails)

**Instructions**: List things we should NOT say because they're inaccurate or unprovable. Prevents credibility damage.

**Don't Say** (Risks credibility):
- "Sisense has no AI capabilities" - *They use ARIMA and attempted Simply Ask; focus on the **Intelligence Ceiling**.*
- "Sisense dashboards are bad" - *Their embedded dashboard quality is strong for ISVs; focus on the **Architectural Mismatch** for business users.*
- "Sisense can't connect to data sources" - *They have adequate connectors; focus on the setup burden and IT dependency.*
- "Sisense has no legitimate use cases" - *ISV embedding is a valid use case; highlight it's not **Domain Intelligence** for business users.*

**Instead Say** (Evidence-based alternatives):
- "Sisense relies on 1970s ARIMA statistics and failed 'Simply Ask' attempts, creating an **Intelligence Ceiling**." - *Supported by technical documentation.*
- "Sisense's dashboard focus leads to **Workflow Disruption** for business users who need native Excel and Slack integration." - *Supported by lack of formula support.*
- "Sisense requires significant SQL expertise and IT implementation (14+ weeks), representing an **Architectural Mismatch** for agile business needs." - *Supported by ElastiCube documentation.*
- "Sisense is optimized for ISV embedding, while Scoop is built for **Autonomous Investigation** and operationalizing enterprise expertise." - *Supported by architecture and customer profile.*

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

- [ ] Check if Sisense has addressed the **Intelligence Ceiling** (e.g., new AI features beyond ARIMA).

- [ ] Verify if **Workflow Disruption** has been mitigated (e.g., native Excel/PowerPoint integration).

- [ ] Review if BUA scores have changed (re-run framework scoring).

- [ ] Update proof points regarding **Architectural Mismatch** (e.g., implementation times).

- [ ] Check if win/lose conditions have shifted.



**Triggered Updates** (Update immediately when):

- Competitor announces major product changes (e.g., new AI engine).

- Win/loss analysis reveals new patterns.

- Sales team reports different objections than expected.

- BUA dimension scores change by >3 points.



**Version History**:

- 2025-11-18: Strategic update to align with "Domain Intelligence Platform" positioning. Reframed weaknesses as architectural flaws (Architectural Mismatch, Intelligence Ceiling, Workflow Disruption). Integrated references to Encoded Expertise, Investigation Coordinator, Spreadsheet Calculation Engine, Automated Presentation Generation. Updated sales guidance and demo focus areas.

- September 28, 2025: Initial strategy based on BUA 28/100 scoring and comprehensive Phase 2/3 research



---



**Template Version**: 1.1

**Created**: September 28, 2025

**Last Updated**: September 28, 2025
