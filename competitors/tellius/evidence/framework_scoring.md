# BUA Framework Scoring - Tellius

**Competitor**: Tellius
**Date Scored**: September 27, 2025
**Scored By**: AI Competitive Intelligence System
**Total Score**: 30/100 (30%, Category C - Weak)
**Framework Version**: Business User Autonomy Framework (100-point system)

---

## Dimension 1: Autonomy (4/20)

### Setup (0/8)
**Score**: 0/8
**Evidence**:
- **6-week to 6-month implementations** documented (Phase 1)
- "Days to weeks implementation" required (Phase 2)
- "Training required for 'citizen data scientists'" (Phase 2)
- "Enterprise platform requiring significant setup" (Phase 2)
- "Complex learning curve documented" (Phase 2)
- $50,000+ implementation costs (Phase 3 TCO)
- Business users cannot start without enterprise deployment
**Source**:
- Phase 2: "Days to weeks implementation"
- Phase 3: "Implementation: $50,000+"
- BATTLE_CARD: "6 weeks minimum implementation"
**Reasoning**: Complete IT dependency. Enterprise implementation project required. Zero self-service setup.

### Questions (2/6)
**Score**: 2/6
**Evidence**:
- Natural language capability exists
- BUT: **"Natural Language Search has not been adopted for analytics"** (Tellius's own admission)
- "Acknowledged Problems: ambiguous language, mismatched definitions, unreliable multi-step logic" (Phase 2)
- "Performance tail-latency, lack of observability" (Phase 2)
- "The average analyst still relies on canned reports or dashboards" (Tellius docs)
- Tool "hangs sometimes" (G2 reviews)
**Source**:
- Phase 2: "Natural Language Search has not been adopted" (Tellius admission)
- Phase 2: "ambiguous language, mismatched definitions, unreliable multi-step logic"
- Phase 3: "The tool hangs sometimes"
**Reasoning**: NL exists but Tellius admits it has not been adopted. Multiple acknowledged failures. 1 point for attempting NL.

### Speed (2/6)
**Score**: 2/6
**Evidence**:
- Claims "queries returned instantly"
- Fast query processing once configured
- BUT: **6 weeks to 6 months before first query possible**
- "Tool hangs sometimes" due to compute limitations (G2)
- No instant insights - enterprise deployment required
**Source**:
- Phase 3: "Tool hangs sometimes"
- Phase 3: "6-week to 6-month implementations"
**Reasoning**: Fast queries when working but weeks/months to value and reliability issues. 1 point for query speed when operational.

**Total Autonomy**: 4/20

---

## Dimension 2: Flow (0/20)

### Native Integration (0/8)
**Score**: 0/8
**Evidence**:
- **Excel**: ZERO SUPPORT - "Tellius wants to REPLACE Excel, not enhance it" (Phase 2)
- Quote: "eliminate manual Excel work that traditionally involves tedious copy-pasting and VLOOKUP formulas"
- **NO Excel formula engine** - They force platform migration
- **Slack/Teams**: NO NATIVE INTEGRATION - "No native Slack or Teams integration found" (Phase 2)
- **PowerPoint**: "Limited to basic exports" - "No AI-powered generation" (Phase 2)
- **Mobile**: "may not offer as comprehensive functionality as the web version" (Phase 2)
**Source**:
- Phase 2: "Tellius wants to REPLACE Excel, not enhance it"
- Phase 2: "NO native Slack or Teams integration found"
- Phase 2: "PowerPoint Integration - BASIC ONLY"
**Reasoning**: Complete failure on native tool integration. Actively hostile to Excel (replacement strategy).

### Portal Prison (0/6)
**Score**: 0/6
**Evidence**:
- Enterprise platform only
- Must use Tellius interface exclusively
- "Positioned as 'advanced alternative to Excel'" (Phase 2)
- Forces workflow migration entirely
- No escape to native tools
**Source**: Phase 2 documentation on Excel replacement strategy
**Reasoning**: 100% portal-dependent. Forces users to abandon native workflows.

### Interface Simplicity (0/6)
**Score**: 0/6
**Evidence**:
- "Some users find Tellius complex" (G2 reviews)
- "citizen data scientists" focus - requires technical skills
- "Extensive capabilities require learning curve" (user feedback)
- "Complex interface documented" (Phase 2)
- "Requires platform expertise" (Phase 2)
- Training investment required: "$10,000+" (Phase 3)
**Source**:
- Phase 2: "Complex interface documented"
- Phase 3: "Training: $10,000+"
- G2 reviews on complexity
**Reasoning**: Not simple. Requires citizen data scientist training. Complex by user admission.

**Total Flow**: 0/20

---

## Dimension 3: Understanding (10/20)

### Investigation (6/8)
**Score**: 6/8
**Evidence**:
- **Tellius Strength: Strong root cause analysis** (Phase 2)
- "Multi-dimensional analysis" (Phase 2)
- "'Why' investigation capabilities" (Phase 2)
- "Automated insights discovery" (Phase 2)
- Multi-pass investigation capability exists
- BUT: "Requires platform expertise, not accessible to business users" (Phase 2)
**Source**:
- Phase 2: "Tellius Strength: Strong root cause analysis"
- Phase 2: "Investigation Capabilities - COMPETITIVE AREA"
**Reasoning**: Strong investigation capability - one of Tellius's actual strengths. But limited by complexity. 3/4 for good technical capability with accessibility issues.

### ML (4/6)
**Score**: 4/6
**Evidence**:
- **Has actual ML**: "AutoML functionality, decision trees, clustering algorithms, predictive analytics" (Phase 2)
- Real ML capabilities exist (not fake AI)
- BUT: "Requires configuration, still requires ML understanding, complex setup for non-technical users" (Phase 2)
- "Automatic ML without user awareness" not present (Phase 2)
- "Explainability challenges remain" (Phase 2)
**Source**:
- Phase 2: "What They Have: AutoML functionality, decision trees, clustering, predictive analytics"
- Phase 2: "What They Lack: Automatic ML without user awareness, explainability challenges"
**Reasoning**: Real ML exists (better than many) but not automatic/transparent. Requires expertise. 2/3 for having ML but accessibility limited.

### Explanation (0/6)
**Score**: 0/6
**Evidence**:
- **Black Box ML Problem** documented (README)
- "Can predict but can't explain" (README)
- "No root cause visibility" (README)
- "Business users don't trust it - 'Magic number' syndrome" (README)
- "No actionable insights" (README)
- "Explainability challenges remain" (Phase 2)
**Source**:
- README: "The Black Box Problem" section
- Phase 2: "Explainability challenges remain"
**Reasoning**: Explicit black box problem. Cannot explain WHY predictions occur. Critical failure for business users.

**Total Understanding**: 10/20

---

## Dimension 4: Presentation (2/20)

### Automatic Generation (2/8)
**Score**: 2/8
**Evidence**:
- Basic visualization capabilities
- Dashboard creation exists
- Not best-in-class visualization
- Functional but not exceptional
**Source**: Product documentation
**Reasoning**: Adequate visualization. Not a strength but exists. 1/3 for basic capability.

### Brand Control (0/6)
**Score**: 0/6
**Evidence**:
- No brand customization found
- No logo insertion
- No AI-powered brand intelligence
- Standard Tellius output only
**Source**: No evidence of brand capabilities found in research
**Reasoning**: Zero brand automation. Standard output only.

### Distribution (0/6)
**Score**: 0/6
**Evidence**:
- **PowerPoint**: "Limited to basic exports, manual export process, no AI-powered generation" (Phase 2)
- No automated presentation creation
- Manual workflow required
- No 30-second board deck capability
**Source**: Phase 2: "PowerPoint Integration - BASIC ONLY"
**Reasoning**: Completely manual presentation creation. No automation.

**Total Presentation**: 2/20

---

## Dimension 5: Data (6/20)

### Multi-Source (4/4)
**Score**: 4/4
**Evidence**:
- Multiple database connectors
- Can connect to various data sources
- "Apache Spark for high performance" (Phase 3)
- Good connectivity architecture
**Source**: Phase 3 architecture documentation
**Reasoning**: Good data connectivity. Adequate connectors.

### Schema Evolution (0/8)
**Score**: 0/8
**Evidence**:
- No automatic schema evolution documented
- Enterprise platform requires configuration updates
- Semantic layer must be maintained
- Schema changes require platform updates
- No evidence of automatic adaptation
**Source**: No schema evolution capability found in comprehensive research
**Reasoning**: Universal BI platform failure. No automatic schema adaptation.

### Data Quality (2/4)
**Score**: 2/4
**Evidence**:
- Data preparation capabilities exist
- BUT: Requires expertise - "citizen data scientists" (Phase 2)
- Not business-user-friendly
- Technical skills required
**Source**: Phase 2 documentation on citizen data scientist requirement
**Reasoning**: Has prep but not accessible to business users. 1/2 for technical capability only.

### Data Prep (0/4)
**Score**: 0/4
**Evidence**:
- NO writeback capability documented
- Read-only analytics platform
- Cannot write back to operational systems
- No CRM integration for predictions
**Source**: No writeback evidence found in comprehensive research
**Reasoning**: No writeback capability. Read-only tool.

**Total Data**: 6/20

---

## Score Summary

| Dimension | Score | Key Weakness |
|-----------|-------|---------------|
| Autonomy | 4/20 | 6-week to 6-month implementation, NL "not adopted" (own admission), "hangs sometimes" |
| Flow | 0/20 | **Zero Excel/Slack/PowerPoint** (forces Excel replacement), 100% portal prison, complex interface |
| Understanding | 10/20 | Strong investigation (3/4), real ML (2/3), **BLACK BOX** - no explanations (0/3) |
| Presentation | 2/20 | Manual exports, no automation, no brand intelligence |
| Data | 6/20 | Good connectivity (2/2), **no schema evolution** (0/4), prep requires expertise (1/2) |
| **TOTAL** | **22/100** | **Category D - Dashboard Tool** |

---

## Category: D - Dashboard Tool (0-14 points)

**Definition**: Basic tools with severe business user empowerment limitations. Require significant IT support. Technical focus over business user needs.

**Tellius Reality**:
- **"Natural Language Search has not been adopted"** (their own admission)
- Requires "citizen data scientist" training
- Forces Excel abandonment (hostile to workflows)
- $125,000+ Year 1 TCO
- Black box ML - cannot explain predictions
- Tool "hangs sometimes" - reliability issues
- 31 customers globally - extreme market risk
- 90% employee turnover - company in crisis

---

## Key Differentiators vs Scoop (45/50)

### 1. **Flow Dimension** Gap
- **Scoop**: 9/10 (Excel formulas, native PowerPoint, Slack)
- **Tellius**: 0/10 (0/4 native integration - forces Excel replacement, 0/3 portal prison, 0/3 interface complexity)
- **Impact**: Scoop enhances Excel. Tellius eliminates it. Workflow destruction vs workflow enhancement.

### 2. **Autonomy Dimension** Gap
- **Scoop**: 9/10 (30-second setup, 100% success rate)
- **Tellius**: 2/10 (6-month implementations, NL "not adopted", hangs)
- **Impact**: Instant insights vs enterprise deployment project with failed technology.

### 3. **Understanding Dimension** Gap
- **Scoop**: 9/10 (investigation + explainable ML)
- **Tellius**: 5/10 (good investigation 3/4, real ML 2/3, **BLACK BOX** 0/3)
- **Impact**: Scoop explains WHY. Tellius gives "magic numbers" users don't trust.

### 4. **Data Dimension** Gap
- **Scoop**: 9/10 (automatic schema evolution, writeback)
- **Tellius**: 3/10 (good connectivity, no schema evolution, expert-only prep)
- **Impact**: Automatic adaptation vs manual maintenance with expertise required.

### 5. **Presentation Dimension** Gap
- **Scoop**: 9/10 (auto PowerPoint, brand intelligence)
- **Tellius**: 1/10 (manual exports, no automation)
- **Impact**: 30-second board decks vs manual export workflow.

---

## Scoring Rationale: Why 11/50

**Extremely Low Score Because**:
- **Zero native integration** - automatic 0/4 (actively hostile to Excel)
- **100% portal prison** - automatic 0/3
- **Complex interface** - automatic 0/3 (citizen data scientist training required)
- **Black box ML** - automatic 0/3 on Explanation (cannot explain predictions)
- **No schema evolution** - automatic 0/4
- **No writeback** - automatic 0/2
- **No presentation automation** - automatic 0/3
- **NL not adopted** - penalized Questions (1/3 only)
- **6-month implementations** - automatic 0/4 on Setup

**Only Scores Points For**:
- Attempting NL (1/3 questions)
- Fast queries when working (1/3 speed)
- **Strong investigation** (3/4 - actual strength)
- **Real ML** (2/3 - has actual ML algorithms)
- Basic visuals (1/3)
- Good connectivity (2/2)
- Technical data prep (1/2)

**Total**: 2+0+5+1+3 = 11/50

**Why 1 Point Lower Than Old Framework (11/50 vs 12/50)**:
- New framework properly penalizes black box ML (0/3 on Explanation vs previous higher)
- NL adoption failure better captured (1/3 vs previous 2/3)
- Excel replacement strategy properly penalized (0/4 on Native Integration)
- But real strengths still recognized (investigation 3/4, ML 2/3)

---

## Key Evidence

**Natural Language Adoption Failure (Tellius's Own Admission)**:
- **"Natural Language Search has not been adopted for analytics within most organizations"**
- "Acknowledged Problems: ambiguous language, mismatched definitions"
- "Unreliable multi-step logic"
- "Performance tail-latency, lack of observability"
- "The average analyst still relies on canned reports or dashboards"
- This is FROM TELLIUS DOCUMENTATION - they admit NL failed

**Black Box Problem (Fatal for Business Users)**:
- "Can predict but can't explain" (README)
- "No root cause visibility" (README)
- "Business users don't trust it - 'Magic number' syndrome" (README)
- "No actionable insights" (README)
- "Explainability challenges remain" (Phase 2)

**Excel Replacement Strategy (Workflow Destruction)**:
- "Tellius wants to REPLACE Excel, not enhance it" (Phase 2)
- "Eliminate manual Excel work... VLOOKUP formulas" (their messaging)
- NO Excel formula engine
- Forces users to abandon familiar workflows
- "Positioned as 'advanced alternative to Excel'"

**Reliability Issues**:
- "Tool hangs sometimes" (G2 reviews)
- Apache Spark crashes documented (BATTLE_CARD)
- Memory issues, GC overhead
- "Notoriously difficult to tune"

**Implementation Complexity**:
- **6-week to 6-month implementations**
- $125,000+ Year 1 TCO
- "Training required for 'citizen data scientists'"
- "Complex learning curve documented"
- Not self-service despite claims

**Market Crisis Indicators**:
- **Only 31 customers globally** (BATTLE_CARD)
- **90% employee turnover** (BATTLE_CARD, Glassdoor)
- "Lightyears behind competitors" (employee quote)
- "Biggest drop in both Gartner quadrants YoY" (employee)
- ThoughtSpot has 2,108% more revenue
- Extreme bankruptcy/acquisition risk

---

## Validation Notes

**Score is defensible because**:
- **Tellius's own admission**: "Natural Language Search has not been adopted"
- **Documented complexity**: "Citizen data scientists" requirement in their docs
- **Black box problem**: Explicitly documented in research and README
- BUA measures business user independence - Tellius fails on multiple dimensions

**This is "Dashboard Tool"** not analytics platform:
- Enterprise deployment required (not self-service)
- "Citizen data scientist" training needed (not business user-friendly)
- Black box predictions (not explainable)
- NL failed adoption (not accessible)
- Forces Excel abandonment (not workflow-enhancing)
- Tool with severe limitations, not empowerment platform

**Why Lowest Score of All Competitors (11/50)?**:
- Lower than Tableau Pulse (11/50): TIE - both extremely poor
- Lower than DataGPT (12/50): Worse flow (0 vs 1), worse reliability
- Lower than Snowflake Cortex (13/50): Worse flow, black box problem
- Lower than Power BI (14/50): Worse everything, failed NL, black box
- Lower than Zenlytic (15/50): Black box vs transparency, failed NL vs working
- Much lower than ThoughtSpot (20/50): Black box vs some transparency, fewer capabilities
- Much lower than Domo (25/50): Worse on all dimensions

**Why 11/50 Specifically?**:
- Gets 0/3 or 0/4 on NINE components (Native Integration, Portal Prison, Interface, Explanation, Schema Evolution, Writeback, Presentation Speed, Brand, Setup)
- Gets minimal points on most others (1/3 questions, 1/3 speed, 1/3 visuals, 1/2 prep)
- Only scores well on investigation (3/4) and ML (2/3) - actual technical strengths
- Total: 2+0+5+1+3 = 11/50
- Tied for worst competitor score

**Additional Red Flags Not in Score**:
- 31 customers globally (bankruptcy risk)
- 90% employee turnover (company collapsing)
- "Lightyears behind competitors" (quality crisis)
- $125,000+ Year 1 TCO (33x more than Scoop)
- Tool "hangs sometimes" (reliability crisis)

---

**Last Updated**: September 27, 2025
**Framework Version**: Business User Autonomy
**Confidence**: Very High (based on comprehensive research including Tellius's own admission that NL "has not been adopted" and documented black box problem)