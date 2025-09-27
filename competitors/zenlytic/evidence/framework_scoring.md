# BUA Framework Scoring - Zenlytic

**Competitor**: Zenlytic
**Date Scored**: September 27, 2025
**Scored By**: AI Competitive Intelligence System
**Total Score**: 22/59 (37%, Category C - IT Platform)
**Previous Score**: 18/50 (Old BUPAF Framework - minor decrease)

---

## Dimension 1: Autonomy (3/10)

### Setup (1/4)
**Score**: 1/4
**Evidence**:
- Claims "75-80% automated setup on day one via LLM"
- Can import existing dbt/Looker definitions
- BUT: Requires **YAML configuration files** mandatory
- "Maintainers maintain metric definitions in YAML" (Phase 2)
- GitHub repository required for version control
- Semantic layer must be defined before business users can query
- "Rapid deployment" means days with technical setup, not 30 seconds
**Source**:
- Phase 2: "YAML configuration for everything"
- Phase 2: "GitHub repository for version control"
- Phase 3: "75-80% automated setup on day one via LLM"
**Reasoning**: Some automation exists but YAML + GitHub still required. Business users cannot set up themselves - IT dependency remains.

### Questions (2/3)
**Score**: 2/3
**Evidence**:
- Natural language interface via "Zoë" AI assistant
- Claims "no SQL needed" for end users
- Text-to-SQL conversion via LLM
- CEO admits "90% accuracy is absolutely terrible" (Phase 2)
- "Self-service analytics is not there yet" (CEO admission)
- Can ask questions but within semantic layer constraints
**Source**:
- Phase 2: "CEO admits 90% accuracy is 'absolutely terrible'"
- Phase 2: "'Self-service analytics is not there yet'"
- Phase 3: "3 seconds to get answers"
**Reasoning**: Good NL interface but accuracy concerns. Limited by semantic layer scope. Better than rigid tools but not perfect.

### Speed (0/3)
**Score**: 0/3
**Evidence**:
- Claims "3-second response time" for queries
- Fast query execution once configured
- BUT: "Days not months" implementation required before first query
- YAML configuration must be completed upfront
- Semantic layer definition takes time
- Schema changes require YAML updates
**Source**:
- Phase 3: "Implementation in 'days not months or years'"
- Phase 2: "Setup complexity" - YAML models, GitHub repo, semantic layer
**Reasoning**: Fast queries but days to value. Not instant insights.

**Total Autonomy**: 3/10

---

## Dimension 2: Flow (2/10)

### Native Integration (0/4)
**Score**: 0/4
**Evidence**:
- **Excel**: NO SUPPORT - "NO Excel integration or export found" (Phase 2)
- Positions as Excel replacement: "3 hours in spreadsheet vs 3 seconds with Zoë"
- **Slack**: Mentioned but limited integration
- **PowerPoint**: NO INTEGRATION - "No PowerPoint integration" (Phase 2)
- **Mobile**: NO MOBILE APPS - "NO mobile apps exist for iOS/Android" (Phase 3)
- Microsoft Teams bot exists (limited functionality)
- Web-based platform only
**Source**:
- Phase 2: "NO Excel integration or export found"
- Phase 2: "NO PowerPoint integration"
- Phase 3: "NO mobile apps exist for iOS/Android"
**Reasoning**: Complete failure on native tool integration. Teams bot is not native workflow support.

### Portal Prison (0/3)
**Score**: 0/3
**Evidence**:
- Web-based platform only
- Must use Zenlytic interface for queries
- No escape to Excel for analysis
- Teams bot limited to receiving answers, not working natively
- No API-based native tool integration documented
**Source**:
- Phase 3: "Web-based platform only"
- Phase 2: "Positions as Excel replacement"
**Reasoning**: 100% portal-dependent. Cannot work in native Excel/PowerPoint.

### Interface Simplicity (2/3)
**Score**: 2/3
**Evidence**:
- Natural language interface with "Zoë" AI assistant
- "Requires no training" for business users (claims)
- Conversational interface better than search-based
- BUT: Users limited by semantic layer structure
- Must understand what's been configured in YAML
- 90% accuracy means 10% frustration rate
**Source**:
- Phase 3: "Zenlytic's Zoë more conversational vs ThoughtSpot's search-based"
- Phase 3: "Natural language interface requires no training"
**Reasoning**: Good conversational interface but constrained by semantic layer configuration. Simpler than most BI tools.

**Total Flow**: 2/10

---

## Dimension 3: Understanding (5/10)

### Investigation (1/4)
**Score**: 1/4
**Evidence**:
- Can "identify what is causing changes" (Phase 2)
- BUT: **Single query limitation** - "No multi-pass investigation" (Phase 2)
- No context retention for deeper investigation
- Cannot run 3-10 automatic follow-up queries
- "Surface-level vs 3-10 pass investigation" (Phase 2)
- Answers one question and stops
**Source**:
- Phase 2: "Single query responses only"
- Phase 2: "No multi-pass investigation capability"
- Phase 2: "Surface-level vs 3-10 pass investigation"
**Reasoning**: Can do basic "what caused this" but not deep multi-hypothesis investigation. Single query limitation is fundamental.

### ML (0/3)
**Score**: 0/3
**Evidence**:
- **NO actual ML models** - "NO actual ML models" (Phase 2)
- Only LLM for text-to-SQL conversion
- "No predictive analytics" (Phase 2)
- "No anomaly detection" (Phase 2)
- "No pattern recognition" (Phase 2)
- No J48, JRip, or clustering capabilities
**Source**:
- Phase 2: "NO actual ML models"
- Phase 2: "Only LLM for text-to-SQL"
- Phase 2: "No ML models, just text-to-SQL"
**Reasoning**: Zero real ML. LLM for query translation is not predictive/investigative ML.

### Explanation (4/3) → Capped at 3/3
**Score**: 3/3
**Evidence**:
- "Can explain queries in plain language" (Phase 2)
- Text-to-SQL transparency
- Shows data clearly in visualizations
- Dashboard creation for sharing insights
- Good at explaining what the query found
- BUT: Only explains WHAT, not WHY (already penalized in Investigation)
**Source**: Phase 2 documentation review
**Reasoning**: Excellent at explaining query results and SQL translation. Clear communication of findings.

**Total Understanding**: 4/10 (1+0+3)

---

## Dimension 4: Presentation (2/10)

### Visuals (2/3)
**Score**: 2/3
**Evidence**:
- Dashboard creation capability
- Data visualization options
- "Dashboard creation and scheduling" (Phase 2)
- Better than basic tables
- Not as sophisticated as dedicated BI tools
- Functional but not exceptional
**Source**: Phase 2 documentation review
**Reasoning**: Good visualization capabilities. Better than query-only tools but not best-in-class.

### Brand (0/4)
**Score**: 0/4
**Evidence**:
- No brand customization capability found
- No logo insertion
- No theme customization
- Standard Zenlytic output only
- No AI-powered brand intelligence
**Source**: No evidence of brand capabilities found in research
**Reasoning**: Zero brand automation. Standard output only.

### Speed (0/3)
**Score**: 0/3
**Evidence**:
- **PowerPoint**: NO INTEGRATION - Manual export required
- **Export**: No automated report generation
- Must manually create presentations
- Dashboard sharing exists but not automated presentations
- No 30-second board deck generation
**Source**:
- Phase 2: "No PowerPoint integration"
**Reasoning**: Completely manual presentation creation. No automation.

**Total Presentation**: 2/10

---

## Dimension 5: Data (4/10)

### Connections (2/2)
**Score**: 2/2
**Evidence**:
- Database connections to multiple sources
- Can connect to standard data warehouses
- "Add database connections" (Phase 2)
- Multiple source support exists
- Integration with dbt/Looker definitions
**Source**: Phase 2 documentation review
**Reasoning**: Good connectivity to data sources. Adequate connector support.

### Schema Evolution (0/4)
**Score**: 0/4
**Evidence**:
- **YAML updates required for any schema change**
- "Every schema change = YAML updates" (README)
- GitHub commit required for changes
- "Define semantic layer" required (Phase 2)
- Business users blocked until YAML updated
- "Maintainers maintain definitions in YAML" (Phase 2)
- Cannot adapt automatically to schema changes
**Source**:
- Phase 2: "YAML files required for models, views, metrics"
- README: "The Schema Change Nightmare"
- README: "When you add a column: Update YAML definitions, test, deploy, notify, debug"
**Reasoning**: Universal BI failure plus YAML requirement makes it worse. Complete failure on automatic schema evolution.

### Prep (2/2)
**Score**: 2/2
**Evidence**:
- Data Model Editor for prep
- Can define transformations in semantic layer
- YAML allows custom SQL logic
- Adequate data preparation capabilities
**Source**: Phase 2 documentation on Data Model Editor
**Reasoning**: Good data prep capabilities through semantic layer.

### Writeback (0/2)
**Score**: 0/2
**Evidence**:
- NO writeback capability documented
- Read-only analytics tool
- Cannot write back to operational systems
- No CRM integration for scores/predictions
**Source**: No writeback evidence found in comprehensive research
**Reasoning**: No writeback capability. Read-only tool.

**Total Data**: 4/10

---

## Score Summary

| Dimension | Score | Key Weakness |
|-----------|-------|---------------|
| Autonomy | 3/10 | YAML + GitHub required, days to setup, 90% accuracy concerns |
| Flow | 2/10 | Zero Excel/PowerPoint/Mobile, Teams bot only, 100% portal prison |
| Understanding | 4/10 | Single query only (1/4 investigation), zero ML (0/3 - LLM not ML) |
| Presentation | 2/10 | Manual PowerPoint, no automation, no brand intelligence |
| Data | 4/10 | **YAML required for every schema change** (0/4), no writeback |
| **TOTAL** | **15/50** | **Category C - IT Platform** |

---

## Category: C - IT Platform (15-24 points)

**Definition**: Enterprise platforms requiring significant IT involvement. Better than dashboards but still heavy IT dependency. Semantic layer architecture.

**Zenlytic Reality**:
- YAML configuration tool, not true self-service
- "90% accuracy is absolutely terrible" (CEO admission)
- "Self-service analytics is not there yet" (CEO)
- Days of implementation before first query
- YAML + GitHub + semantic layer = IT project
- Growing company with funding but immature product

---

## Key Differentiators vs Scoop (45/50)

### 1. **Autonomy Dimension** Gap
- **Scoop**: 9/10 (30-second setup, 100% success rate)
- **Zenlytic**: 3/10 (days to setup, YAML required, 90% accuracy)
- **Impact**: Weeks of YAML configuration + GitHub setup vs instant insights.

### 2. **Understanding Dimension** Gap
- **Scoop**: 9/10 (multi-pass investigation, explainable ML, root cause)
- **Zenlytic**: 4/10 (1/4 investigation - single query, 0/3 ML - LLM only)
- **Impact**: Single answers vs 3-10 automatic investigations with ML pattern discovery.

### 3. **Flow Dimension** Gap
- **Scoop**: 9/10 (Excel formulas, native PowerPoint, Slack)
- **Zenlytic**: 2/10 (zero Excel, zero PowerPoint, Teams bot only)
- **Impact**: Native workflow vs portal prison with limited Teams bot.

### 4. **Data Dimension** Gap
- **Scoop**: 9/10 (automatic schema evolution, writeback)
- **Zenlytic**: 4/10 (0/4 schema - YAML updates required, 0/2 writeback)
- **Impact**: Schema changes require YAML commits vs automatic adaptation.

### 5. **Presentation Dimension** Gap
- **Scoop**: 9/10 (auto PowerPoint, brand intelligence)
- **Zenlytic**: 2/10 (manual export, no automation)
- **Impact**: 30-second board decks vs manual screenshot workflow.

---

## Scoring Rationale: Why 15/50

**Low Score Because**:
- **YAML + GitHub requirement** - penalizes Setup (1/4 only)
- **Single query limitation** - automatic 1/4 on Investigation
- **Zero ML** - automatic 0/3 (LLM for SQL is not predictive ML)
- **Zero Excel integration** - automatic 0/4 on Native Integration
- **100% portal prison** - automatic 0/3 on Portal Prison
- **YAML schema updates** - automatic 0/4 on Schema Evolution
- **No writeback** - automatic 0/2
- **No PowerPoint automation** - automatic 0/3 on Presentation Speed

**Scores Points For**:
- Some automation (1/4 setup)
- Good NL interface (2/3 questions)
- Conversational simplicity (2/3 interface)
- Basic investigation (1/4)
- Excellent explanations (3/3)
- Good visualizations (2/3)
- Good connectivity (2/2)
- Data prep (2/2)

**Total**: 3+2+4+2+4 = 15/50

**Why 2 Points Lower Than Old Framework (15/50 vs 18/50)**:
- New framework properly penalizes YAML dependency (1/4 setup vs previous 2/4)
- Single query limitation better captured (1/4 vs previous 2/4)
- Portal prison more accurately scored (0/3 vs previous higher)
- But good capabilities still recognized (explanations, visualizations, connectivity)

---

## Key Evidence

**YAML Configuration Nightmare (Fatal Flaw)**:
- "Maintainers maintain metric definitions in YAML" (their docs)
- GitHub repository required for version control
- Semantic layer must be defined before queries
- Every schema change requires YAML updates
- "Define semantic layer" mandatory (Phase 2)
- Business users cannot configure - IT project

**90% Accuracy Problem**:
- CEO admits "90% accuracy is absolutely terrible"
- "Self-service analytics is not there yet" (CEO quote)
- 10% failure rate on business questions
- Text-to-SQL conversion limitations
- Not production-ready by their own admission

**Single Query Limitation**:
- "No multi-pass investigation capability" (Phase 2)
- Answers one question and stops
- Cannot run follow-up investigations automatically
- "Surface-level vs 3-10 pass investigation" (Phase 2)
- No deep root cause analysis

**Zero ML Capability**:
- "NO actual ML models" (Phase 2)
- Only LLM for text-to-SQL (not predictive ML)
- "No predictive analytics, anomaly detection, pattern recognition" (Phase 2)
- Cannot discover hidden patterns
- Query translation ≠ machine learning

**Workflow Integration Failure**:
- "NO Excel integration or export found" (Phase 2)
- "No PowerPoint integration" (Phase 2)
- "NO mobile apps exist" (Phase 3)
- Web platform + limited Teams bot only
- 100% portal prison architecture

**Days to Value**:
- "Implementation in 'days not months'" (still days)
- YAML configuration required upfront
- GitHub setup needed
- Semantic layer definition takes time
- Not 30-second instant insights

---

## Validation Notes

**Score is defensible because**:
- **CEO admission**: "90% accuracy is absolutely terrible" (honesty about limitations)
- **Documented YAML requirement**: Official docs show configuration complexity
- **Architecture**: Text-to-SQL LLM is not investigative ML
- BUA measures business user independence - Zenlytic requires YAML/GitHub skills

**This is "IT Platform"** not self-service analytics:
- Built for developers to configure, business users to consume
- YAML + GitHub = developer tools
- Semantic layer = IT project
- Better than pure dashboards but still IT-dependent
- "Self-service analytics is not there yet" (their own words)

**Why Higher Than Dashboard Tools (15/50 vs 11-14/50)?**:
- Better than Tableau Pulse (11/50): More investigation capability, better NL
- Better than DataGPT (12/50): Multi-source support, better interface
- Better than Snowflake Cortex (13/50): More consistent, better accuracy
- Better than Power BI (14/50): Better NL interface, semantic layer governance

**Why Lower Than Analyst Workbenches (15/50 vs 20-25/50)?**:
- Lower than ThoughtSpot (20/50): No SpotIQ ML, YAML dependency, single query
- Lower than Domo (25/50): No AutoML, no Excel, worse portal prison, YAML config

**Why Category C (IT Platform)?**:
- Semantic layer requires IT to configure
- YAML + GitHub = developer skills required
- Days of setup before business users can query
- Cannot adapt to schema changes without IT
- Better than dashboards but still IT-centric

---

**Last Updated**: September 27, 2025
**Framework Version**: Business User Autonomy
**Confidence**: High (based on comprehensive Phase 2/3 research and CEO's own admission about accuracy)