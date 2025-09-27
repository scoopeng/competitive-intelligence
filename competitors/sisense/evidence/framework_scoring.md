# BUA Framework Scoring - Sisense

**Competitor**: Sisense
**Date Scored**: September 27, 2025
**Scored By**: AI Competitive Intelligence System
**Total Score**: 14/50 (Category D - Dashboard Tool)
**Previous Score**: 12/50 (Old BUPAF Framework - minor increase)

---

## Dimension 1: Autonomy (3/10)

### Setup (0/4)
**Score**: 0/4
**Evidence**:
- **14+ week implementation** typical (Phase 2)
- "Requires extensive training if new to BI" (Phase 2)
- **Sisense Academy**: "30-80 hours of training needed" (Phase 2)
- **ElastiCube requires SQL** despite "no code" claims (Phase 2)
- Business users cannot setup independently
- IT must create data models before users can view
**Source**:
- Phase 2: "14+ Week Implementation - Standard timeline"
- Phase 2: "30-80 hours of training needed"
- BATTLE_CARD: "14+ weeks typical"
**Reasoning**: Complete IT dependency. Enterprise implementation required. Zero self-service setup.

### Questions (2/3)
**Score**: 2/3
**Evidence**:
- Has natural language capability (Simply Ask being deprecated)
- New chatbot in beta (Generative AI for cloud only)
- "Template-based NLQ, not true understanding" (Phase 2)
- "Requires training on syntax" (Phase 2)
- Can ask questions but limited understanding
- Simply Ask being deprecated suggests quality issues
**Source**:
- Phase 2: "Simply Ask (DEPRECATED) - Natural language failed, being replaced"
- Phase 2: "New chatbot in beta"
**Reasoning**: NL exists and partially works (better than complete failures). Being replaced suggests issues but functionality exists. 2/3 for working but limited capability.

### Speed (1/3)
**Score**: 1/3
**Evidence**:
- **Default 300-second timeout** (5 minutes) for queries (Phase 3)
- "Large Data Issues: Response sizes over 10KB cause degradation" (Phase 3)
- Fast for small queries, slow for complex
- BUT: 14+ weeks before first query possible
- Not instant insights
**Source**:
- Phase 3: "Default 300 seconds (5 minutes) for web queries"
- Phase 3: "6-8 widgets recommended for optimal performance"
**Reasoning**: Slow queries (5-minute timeouts) and weeks to value. 1/3 for functional but slow.

**Total Autonomy**: 3/10

---

## Dimension 2: Flow (1/10)

### Native Integration (0/4)
**Score**: 0/4
**Evidence**:
- **Excel**: EXPORT ONLY - "Export to Excel (XLSX) with 1.5M cell limit, static export only, no live formulas" (Phase 2)
- NO Excel formula support - "Cannot use ANY Excel formulas with live data" (Phase 2)
- **Slack**: "Slack posting (screenshots)" only (Phase 2)
- **PowerPoint**: NO SUPPORT - "No PowerPoint capability found" (Phase 2)
- **Mobile**: "Mobile was certainly an afterthought" - Users must reinstall weekly (Phase 3)
**Source**:
- Phase 2: "Excel Integration ❌ CRITICAL GAP"
- Phase 2: "Workflow Integration ❌ PORTAL PRISON"
- Phase 3: "Mobile experience criticized"
**Reasoning**: Complete failure on native tool integration. Export-only is not integration.

### Portal Prison (0/3)
**Score**: 0/3
**Evidence**:
- Portal-based architecture
- "No Scheduled Email Reports - Users must log into portal" (Phase 2)
- "Must leave tools to use Sisense" (Phase 2)
- Embedded analytics focus means platform lock-in
- Cannot work in native tools
**Source**:
- Phase 2: "Portal + exports" workflow
- Phase 2: "No Scheduled Email Reports"
**Reasoning**: 100% portal-dependent. Forces workflow migration.

### Interface Simplicity (1/3)
**Score**: 1/3
**Evidence**:
- Drag-drop dashboard creation exists
- BUT: "Not easy to use" per reviews (Phase 2)
- "Steep learning curve" per multiple sources (Phase 2)
- "Requires extensive training if new to BI" (Phase 2)
- "30-80 hours of training needed" (Phase 2)
- ElastiCube "not user-friendly, requires SQL" (Phase 3)
**Source**:
- Phase 2: "Not easy to use" per reviews
- Phase 2: "Steep learning curve"
- Phase 3: Gartner customer complaints
**Reasoning**: Basic drag-drop exists but steep learning curve documented. 1/3 for attempting simplicity but failing.

**Total Flow**: 1/10

---

## Dimension 3: Understanding (4/10)

### Investigation (1/4)
**Score**: 1/4
**Evidence**:
- **Drill-down in dashboards** only (Phase 2)
- "Click through pre-built hierarchies" (Phase 2)
- "Cannot investigate, only navigate dashboards" (Phase 2)
- No multi-pass investigation
- No root cause analysis capability found
- Single query limitation
**Source**:
- Phase 2: "Investigation & Root Cause ❌ DOESN'T EXIST"
- Phase 2: "Not real investigation"
**Reasoning**: Basic drill-down only, not true investigation. 1/4 for attempting but very limited capability.

### ML (0/3)
**Score**: 0/3
**Evidence**:
- **ARIMA forecasting** from 1970s (Phase 2)
- "Statistical methods from 1970s, not ML" (Phase 2)
- "ARIMA ≠ AI" - Marketing mirage (README)
- No automatic ML capability
- "Requires data science knowledge" (Phase 2)
- Simply Ask deprecated suggests AI failures
**Source**:
- Phase 2: "Machine Learning/AI 🔴 MARKETING MIRAGE"
- Phase 2: "ARIMA from 1970s, not ML"
- BATTLE_CARD: "ARIMA isn't AI - Statistical method from 1970s"
**Reasoning**: Zero real ML. ARIMA is statistics, not machine learning. Marketing deception.

### Explanation (3/3)
**Score**: 3/3
**Evidence**:
- Dashboard visualizations show data clearly
- Tables and charts display results
- Can explain what the data shows
- Adequate at showing WHAT (not WHY, but that's Investigation)
- Standard BI visualization explanations
**Source**: Product documentation on dashboard capabilities
**Reasoning**: Good at explaining what dashboards show. Standard BI explanation capability.

**Total Understanding**: 4/10

---

## Dimension 4: Presentation (2/10)

### Visuals (2/3)
**Score**: 2/3
**Evidence**:
- Dashboard creation with visualizations
- "6-8 widgets per dashboard for performance" (Phase 3)
- Multiple chart types available
- Embedded analytics focus = visualization strength
- Better than basic but not exceptional
**Source**: Phase 3 performance documentation
**Reasoning**: Good visualization capabilities for embedded analytics platform. 2/3 for solid dashboards.

### Brand (0/4)
**Score**: 0/4
**Evidence**:
- No brand customization found
- No logo insertion
- No AI-powered brand intelligence
- Standard Sisense output
- White-label for ISVs ≠ brand intelligence
**Source**: No brand automation capabilities found
**Reasoning**: Zero brand automation for end users. White-label is for ISV embedding, not business user branding.

### Speed (0/3)
**Score**: 0/3
**Evidence**:
- **PowerPoint**: NO SUPPORT - "None found" (Phase 2)
- **Export**: Manual only - "Export to Excel static" (Phase 2)
- "No PowerPoint generation" (Phase 2)
- "Wide Tables Cut Off - PDF exports truncate" (Phase 2)
- Manual screenshot workflow required
**Source**:
- Phase 2: "PowerPoint Integration ❌"
- Phase 2: Critical limitations list
**Reasoning**: Completely manual presentation creation. No automation.

**Total Presentation**: 2/10

---

## Dimension 5: Data (4/10)

### Connections (2/2)
**Score**: 2/2
**Evidence**:
- Multiple database connectors
- ElastiCube for data integration
- Can connect to various sources
- Good connectivity architecture
**Source**: Product documentation on connectors
**Reasoning**: Good data connectivity. Adequate connectors.

### Schema Evolution (0/4)
**Score**: 0/4
**Evidence**:
- No automatic schema evolution
- ElastiCube must be reconfigured manually
- Requires SQL expertise to update (Phase 2)
- Schema changes require IT involvement
- "Requires SQL for ElastiCube" (Phase 2)
**Source**:
- Phase 2: "ElastiCube requires SQL despite 'no code' claims"
- No automatic adaptation capability found
**Reasoning**: Universal BI platform failure. Manual schema updates required with SQL expertise.

### Prep (2/2)
**Score**: 2/2
**Evidence**:
- ElastiCube provides data preparation
- SQL-based transformations
- Good data modeling capabilities
- Adequate prep for technical users
**Source**: Phase 2 documentation on ElastiCube
**Reasoning**: Good data prep capabilities through ElastiCube. Adequate for technical users.

### Writeback (0/2)
**Score**: 0/2
**Evidence**:
- NO writeback capability documented
- Read-only analytics platform
- Dashboard and reporting focus only
- Cannot write back to operational systems
**Source**: No writeback evidence found in comprehensive research
**Reasoning**: No writeback capability. Read-only tool.

**Total Data**: 4/10

---

## Score Summary

| Dimension | Score | Key Weakness |
|-----------|-------|---------------|
| Autonomy | 3/10 | 14+ weeks implementation, 30-80 hours training, ElastiCube requires SQL |
| Flow | 1/10 | Excel export-only (no formulas), no PowerPoint, portal prison, mobile "afterthought" |
| Understanding | 4/10 | Dashboard drill-down only (1/4 investigation), **ARIMA not ML** (0/3), good explanations (3/3) |
| Presentation | 2/10 | Good dashboards (2/3), no automation, no brand intelligence |
| Data | 4/10 | Good connectivity (2/2), **no schema evolution** (0/4), good prep (2/2) |
| **TOTAL** | **14/50** | **Category D - Dashboard Tool** |

---

## Category: D - Dashboard Tool (0-14 points)

**Definition**: Basic tools with severe business user empowerment limitations. Require significant IT support. Technical focus over business user needs.

**Sisense Reality**:
- Embedded analytics platform for ISVs, not business users
- ARIMA from 1970s marketed as "AI"
- Simply Ask deprecated (AI failed)
- 400% renewal price increases documented
- 14+ week implementations
- $200K+ total cost
- 0.01% market share (tiny)
- 13% workforce cuts in 2024

---

## Key Differentiators vs Scoop (45/50)

### 1. **Autonomy Dimension** Gap
- **Scoop**: 9/10 (30-second setup, 100% success rate)
- **Sisense**: 3/10 (14+ weeks, 30-80 hours training, SQL required)
- **Impact**: Instant insights vs months-long IT project.

### 2. **Understanding Dimension** Gap
- **Scoop**: 9/10 (multi-pass investigation, explainable ML, root cause)
- **Sisense**: 4/10 (drill-down only 1/4, ARIMA not ML 0/3, good explanations 3/3)
- **Impact**: Root cause discovery vs dashboard navigation. Real ML vs 1970s statistics.

### 3. **Flow Dimension** Gap
- **Scoop**: 9/10 (Excel formulas, native PowerPoint, Slack)
- **Sisense**: 1/10 (Excel export-only, no PowerPoint, portal prison)
- **Impact**: Native workflow enhancement vs forced platform migration.

### 4. **Data Dimension** Gap
- **Scoop**: 9/10 (automatic schema evolution, writeback)
- **Sisense**: 4/10 (good connectivity, no schema evolution, no writeback)
- **Impact**: Automatic adaptation vs manual SQL updates.

### 5. **Presentation Dimension** Gap
- **Scoop**: 9/10 (auto PowerPoint, brand intelligence)
- **Sisense**: 2/10 (good dashboards, no automation, no brand)
- **Impact**: 30-second board decks vs manual screenshot workflow.

---

## Scoring Rationale: Why 14/50

**Low Score Because**:
- **Zero Excel formulas** - automatic 0/4 on Native Integration (export-only)
- **100% portal prison** - automatic 0/3
- **ARIMA not ML** - automatic 0/3 on ML (1970s statistics marketed as AI)
- **No investigation** - penalized to 1/4 (drill-down only, not real investigation)
- **No schema evolution** - automatic 0/4
- **No writeback** - automatic 0/2
- **No presentation automation** - automatic 0/3 on Speed, 0/4 on Brand
- **14+ weeks implementation** - automatic 0/4 on Setup

**Scores Points For**:
- NL capability exists (2/3 questions - being replaced but works)
- Queries work (1/3 speed - slow but functional)
- Basic interface (1/3 - steep learning curve but drag-drop exists)
- Basic drill-down (1/4 - limited investigation)
- Good explanations (3/3 - standard BI capability)
- Good dashboards (2/3 - embedded analytics strength)
- Good connectivity (2/2)
- Good data prep (2/2)

**Total**: 3+1+4+2+4 = 14/50

**Why 2 Points Higher Than Old Framework (14/50 vs 12/50)**:
- New framework recognizes NL capability exists (2/3 vs previous 1/3)
- Dashboard visualization strength properly credited (2/3 vs previous 1/3)
- But still penalizes ARIMA as fake AI (0/3) and lack of real investigation (1/4)
- Embedded analytics strength acknowledged while still failing on business user empowerment

---

## Key Evidence

**ARIMA Not AI (Marketing Mirage)**:
- "ARIMA forecasting, regression analysis" (Phase 2)
- "Statistical methods from 1970s, not ML" (Phase 2)
- ARIMA invented in 1970s - time series statistics, not machine learning
- Simply Ask deprecated - actual AI attempt failed
- "ARIMA ≠ AI" documented as marketing mirage

**400% Renewal Price Increases**:
- "400% price increase at renewal time" (customer reports)
- "Sisense quadrupled the price when initial contract ended"
- €50,000 forced migration cost (Windows to Linux)
- Hidden fees: "20-30% extra" for AI features
- $109,000 to $137,000 annually typical

**Implementation Complexity**:
- **14+ week implementations** typical
- **30-80 hours of training** required (Sisense Academy)
- "Requires extensive training if new to BI"
- "Steep learning curve" per multiple sources
- ElastiCube "not user-friendly, requires SQL"

**Excel Integration Failure**:
- Export only - "static export only, no live formulas"
- "Cannot use ANY Excel formulas with live data"
- 1.5M cell limit on exports
- No =SISENSE() formula capability
- Forces workflow abandonment

**Performance Issues**:
- **300-second timeout** (5 minutes) for queries
- "Large Data Issues: Response sizes over 10KB cause degradation"
- "M2M Problems: extreme slowness and exponential RAM growth"
- "Abnormal memory consumption" errors common
- 33 outages since September 2022

**Market Reality**:
- **0.01% market share** in reporting
- Only 912 companies using it
- **13% workforce cuts** January 2024 (second round in 6 months)
- Tiny player in crowded market
- Pivoting to API-first suggests struggling

**Embedded Analytics Focus**:
- Built for ISVs embedding in software products
- Not for direct business user self-service
- Compose SDK = developer focus
- White-label capabilities for software vendors
- Wrong market for enterprise business users

---

## Validation Notes

**Score is defensible because**:
- **ARIMA from 1970s**: Verifiable fact - not machine learning
- **Simply Ask deprecated**: Their own documentation
- **400% renewal increases**: Multiple customer reports with URLs
- BUA measures business user independence - Sisense fails on embedded analytics focus

**This is "Dashboard Tool"** not self-service analytics:
- Requires 14+ weeks IT implementation
- 30-80 hours training mandatory
- ElastiCube requires SQL expertise
- Export-only Excel (not integration)
- Portal-based architecture
- Built for ISV embedding, not business empowerment

**Why 14/50 Specifically?**:
- Higher than Tellius (11/50): Better NL (2 vs 1), better dashboards (2 vs 1)
- Higher than DataGPT (12/50): Better NL (2 vs 1), better questions capability
- Higher than Snowflake Cortex (13/50): Better NL (2 vs 1), better dashboards (2 vs 1)
- Equal to Power BI (14/50): Similar category - legacy BI with limited empowerment
- Lower than Zenlytic (15/50): YAML config vs ARIMA fake AI - similar failures
- Lower than ThoughtSpot (20/50): No real ML, worse investigation
- Lower than Domo (25/50): Worse on all dimensions, fake AI vs real AutoML

**Why Category D (Dashboard Tool)?**:
- Requires IT for setup and maintenance
- No real ML (ARIMA is statistics)
- Export-only Excel (not integration)
- Portal prison architecture
- Embedded analytics focus ≠ business user empowerment
- Better than worst tools but still IT-dependent

---

**Last Updated**: September 27, 2025
**Framework Version**: Business User Autonomy
**Confidence**: Very High (based on comprehensive Phase 2/3 research and documented ARIMA marketing deception)