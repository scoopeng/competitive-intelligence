# BUA Framework Scoring - DataGPT

**Competitor**: DataGPT
**Date Scored**: September 27, 2025
**Scored By**: AI Competitive Intelligence System
**Total Score**: 30/100 (30%, Category C - Weak)
**Framework Version**: Business User Autonomy Framework (100-point system)

---

## Dimension 1: Autonomy (4/20)

### Setup (0/8)
**Score**: 0/8
**Evidence**:
- **Requires 2-4 weeks implementation** - Schema configuration mandatory
- "Always begins with pilot" (their own docs)
- Schema must be defined upfront by technical teams
- "Rare to adjust after setup" - locks business users into initial structure
- Steep learning curve documented
- Business users cannot start querying without IT setup
**Source**:
- Phase 2: "2-4 weeks typical implementation (vs Scoop's 30 seconds)"
- Phase 2: "Schema configuration needed upfront"
- BATTLE_CARD: "Setup Time: 2-4 weeks"
**Reasoning**: Complete IT dependency. Schema configuration required before any business user can ask questions. Zero self-service setup.

### Questions (2/6)
**Score**: 2/6
**Evidence**:
- Natural language interface exists
- BUT: "Requires exact phrasing" (Phase 2)
- Single query only - cannot investigate
- Only 15 G2 reviews (tiny validation base)
- Can answer "what happened" not "why it happened"
- No context retention between questions
**Source**:
- Phase 2: "Business User Empowerment: 3/10 - requires exact phrasing"
- Phase 2: "Single query processing (not multi-pass)"
**Reasoning**: Can ask questions but limited to surface-level metrics. No investigation capability.

### Speed (2/6)
**Score**: 2/6
**Evidence**:
- Claims "100x faster" but no actual benchmarks
- "Lightning Cache" is just standard database caching
- Fast at displaying single metrics
- BUT: 2-4 weeks before first query possible
- Schema changes "rare to adjust" - weeks more delay
**Source**:
- Phase 3: "'100x faster' claim without evidence"
- Phase 3: "Standard caching marketed as innovation"
**Reasoning**: Fast query response but weeks to value. Misleading speed claims.

**Total Autonomy**: 4/20

---

## Dimension 2: Flow (2/20)

### Native Integration (0/8)
**Score**: 0/8
**Evidence**:
- **Excel**: NO SUPPORT - "No formula support (0 functions vs Scoop's 150+)"
- **Slack**: NO INTEGRATION FOUND - "No Slack integration found"
- **PowerPoint**: NO INTEGRATION - "No PowerPoint generation"
- **Mobile**: NO MOBILE APP - "No mobile app exists"
- Portal-only access confirmed
- Export only (static CSV dumps)
**Source**:
- Phase 2: "NO EXCEL INTEGRATION FOUND"
- Phase 2: "NO WORKFLOW INTEGRATION"
- Phase 3: "Portal-only access confirmed"
**Reasoning**: Complete failure on workflow integration. Zero native tool support.

### Portal Prison (0/6)
**Score**: 0/6
**Evidence**:
- Must use DataGPT web portal exclusively
- "Portal-only access" (Phase 3)
- No API documentation found publicly
- No embedding capability
- Must log into separate system
- Manual copy/paste for any external use
**Source**:
- Phase 3: "Portal-only access confirmed"
- Phase 3: "No API documentation found publicly"
**Reasoning**: 100% portal-dependent. Cannot work in native tools.

### Interface Simplicity (2/6)
**Score**: 2/6
**Evidence**:
- Natural language interface conceptually simple
- BUT: "Steep learning curve documented" (Phase 2)
- "Not intuitive for beginners" (Phase 2)
- Requires understanding schema configuration
- Only 15 G2 reviews (minimal validation)
- "Requires exact phrasing" limits simplicity
**Source**:
- Phase 2: "Steep learning curve documented"
- Phase 2: "Not intuitive for beginners"
**Reasoning**: Looks simple but documented as steep learning curve. Limited validation base.

**Total Flow**: 2/20

---

## Dimension 3: Understanding (6/20)

### Investigation (0/8)
**Score**: 0/8
**Evidence**:
- **Complete failure on "why" questions**: Can only show WHAT, not WHY
- Single query limitation - no multi-pass investigation
- "No context retention between questions" (Phase 2)
- "Cannot determine 'why' things happened" (Phase 2)
- No hypothesis testing capability
- No root cause analysis
**Source**:
- Phase 2: "NO INVESTIGATION CAPABILITY"
- Phase 2: "Answers 'what happened' not 'why'"
- Phase 2: "Single query only"
**Reasoning**: Cannot investigate WHY. Fundamental architectural limitation - single metrics only.

### ML (0/6)
**Score**: 0/6
**Evidence**:
- **NO AUTOMATIC ML** - "No J48, JRip, or EM clustering equivalents"
- "Basic statistics marketed as 'AI'" (Phase 2)
- No pattern discovery capability
- No automatic segmentation
- Claims "AI-powered" but reality is "Statistics only"
- No feature importance, no predictions, no clustering
**Source**:
- Phase 2: "NO AUTOMATIC ML"
- Phase 2: "Zero ML capabilities vs automatic ML"
- Phase 2: "Marketing vs Reality: Claims 'AI-powered analysis', Reality: Basic statistics only"
**Reasoning**: Zero real ML. Marketing basic statistics as AI.

### Explanation (6/6)
**Score**: 6/6
**Evidence**:
- Returns clear metric displays
- Shows data in tables/charts
- Numbers are explained clearly
- Claims "zero hallucination analytics"
- BUT: Only explains WHAT, not WHY (already penalized above)
- Simple visualization of results
**Source**: Product documentation on output formats
**Reasoning**: Good at explaining what it shows, but shallow depth (single metrics). Clarity on surface-level answers.

**Total Understanding**: 6/20

---

## Dimension 4: Presentation (2/20)

### Automatic Generation (2/8)
**Score**: 2/8
**Evidence**:
- "Databoard" visualization capability exists
- Basic charts and metrics display
- Limited to simple visualizations
- No intelligent visualization selection
- Functional but not impressive
**Source**: Product documentation on Databoard
**Reasoning**: Basic visualization capabilities. Adequate for metrics display.

### Brand Control (0/6)
**Score**: 0/6
**Evidence**:
- No brand customization capability
- No logo insertion
- No theme customization
- Standard DataGPT output only
- No AI-powered brand intelligence
**Source**: No evidence of brand capabilities found
**Reasoning**: Zero brand automation. Standard output only.

### Distribution (0/6)
**Score**: 0/6
**Evidence**:
- **PowerPoint**: Manual workflow - no generation capability
- **Export**: Manual CSV download
- Must copy/paste into presentations
- No automated report generation
- "Manual screenshot workflow" documented
**Source**:
- Phase 2: "No PowerPoint generation"
- BATTLE_CARD: "No PowerPoint integration - copy/paste screenshots"
**Reasoning**: Completely manual presentation creation. No automation.

**Total Presentation**: 2/20

---

## Dimension 5: Data (8/20)

### Multi-Source (2/4)
**Score**: 2/4
**Evidence**:
- Can connect to databases
- BUT: **SINGLE SOURCE ONLY** - Fatal limitation
- "Cannot join multiple data sources" (Phase 2)
- Real business questions need multiple sources
- Architecture limitation not connector availability
**Source**:
- Phase 2: "Single Source Only: Cannot join multiple data sources"
- BATTLE_CARD: "Data Sources: Single source only"
**Reasoning**: Has connectors but single-source architecture makes them inadequate. Major limitation.

### Schema Evolution (0/8)
**Score**: 0/8
**Evidence**:
- **FATAL FLAW**: "Rare to adjust after setup" (their own documentation)
- Schema locked after configuration
- "New columns = major project" (README)
- "Business changes = system breaks" (README)
- Cannot adapt to business evolution
- Requires complete reconfiguration for schema changes
**Source**:
- Phase 2: "Schema Rigidity: 'Rare to adjust after setup' (their docs)"
- BATTLE_CARD: "Schema rigid after setup"
- README: "The Rigidity Trap (Fatal Flaw)"
**Reasoning**: Universal BI failure plus explicit admission it's "rare to adjust." Complete failure on schema evolution.

### Data Quality (4/4)
**Score**: 4/4
**Evidence**:
- SQL-like transformations available
- Can configure metrics during setup
- Data transformation capabilities exist
- Schema definition includes prep logic
**Source**: Product architecture documentation
**Reasoning**: Adequate data preparation capabilities during configuration phase.

### Data Prep (2/4)
**Score**: 2/4
**Evidence**:
- Can write back to connected data source
- Technical writeback capability exists
- Not operationalized for business users
- Requires configuration
**Source**: Architecture documentation
**Reasoning**: Technical writeback possible. Adequate for data platform use cases.

**Total Data**: 8/20

---

## Score Summary

| Dimension | Score | Key Weakness |
|-----------|-------|-----------------|
| Autonomy | 4/20 | 2-4 weeks setup, schema locked "rare to adjust", steep learning curve |
| Flow | 2/20 | Zero Excel/Slack/PowerPoint/Mobile, 100% portal prison |
| Understanding | 6/20 | **Cannot answer "why"** (0/4 investigation), zero ML (statistics only) |
| Presentation | 2/20 | Manual screenshots, no automation, no brand intelligence |
| Data | 8/20 | **Single source only** (fatal), schema "rare to adjust" after setup |
| **TOTAL** | **22/100** | **Category D - Dashboard Tool** |

---

## Category: D - Dashboard Tool (0-14 points)

**Definition**: Basic tools with severe business user empowerment limitations. Require significant IT support. Technical focus over business user needs.

**DataGPT Reality**:
- Metrics display tool, not investigation platform
- Schema locked after setup ("rare to adjust")
- Single data source only - cannot join data
- $150K+ first year TCO vs $3,588 for Scoop (42x more)
- Cannot investigate WHY (fundamental limitation)
- Tiny market presence (15 G2 reviews, no major customers)

---

## Key Differentiators vs Scoop (45/50)

### 1. **Understanding Dimension** Gap
- **Scoop**: 9/10 (multi-pass investigation, explainable ML, root cause discovery)
- **DataGPT**: 3/10 (0/4 on investigation - "why" questions impossible, 0/3 on ML - statistics only)
- **Impact**: "Why did churn increase?" - Scoop investigates root causes, DataGPT shows "Churn up 23%" and stops.

### 2. **Data Dimension** Gap
- **Scoop**: 9/10 (automatic schema evolution, multi-source joins)
- **DataGPT**: 5/10 (1/2 on connections due to single-source limit, 0/4 on schema - "rare to adjust")
- **Impact**: Business changes require schema rebuilds. Single source makes real analysis impossible.

### 3. **Autonomy Dimension** Gap
- **Scoop**: 9/10 (30-second setup, 100% question success)
- **DataGPT**: 2/10 (2-4 weeks setup, steep learning curve, schema locked)
- **Impact**: Weeks of IT work + locked schema vs instant insights with flexibility.

### 4. **Flow Dimension** Gap
- **Scoop**: 9/10 (Excel formulas, native PowerPoint, Slack)
- **DataGPT**: 1/10 (zero Excel, zero PowerPoint, zero Slack, 100% portal prison)
- **Impact**: Native workflow vs portal switching and manual exports.

### 5. **Presentation Dimension** Gap
- **Scoop**: 9/10 (auto PowerPoint, brand intelligence)
- **DataGPT**: 1/10 (manual screenshots, no automation)
- **Impact**: Automated presentations vs manual copy/paste workflow.

---

## Scoring Rationale: Why 12/50

**Extremely Low Score Because**:
- **Zero investigation capability** - automatic 0/4 (cannot answer "why")
- **Zero ML** - automatic 0/3 (statistics marketed as AI)
- **Single source architecture** - penalized Connections (1/2 only)
- **Schema rigidity** - automatic 0/4 on Schema Evolution ("rare to adjust")
- **Zero workflow integration** - automatic 0/4 on Native Integration
- **100% portal prison** - automatic 0/3 on Portal Prison

**Only Scores Points For**:
- Basic metric queries exist (1/3)
- Fast single queries (1/3)
- Clear explanations of what it shows (3/3)
- Basic visualizations (1/3)
- Simple interface concept (1/3)
- Data prep during configuration (2/2)
- Technical writeback (2/2)
- Single-source connectivity (1/2)

**Why 1 Point Lower Than Old Framework (12/50 vs 13/50)**:
- New framework properly penalizes single-source limitation (1/2 on Connections instead of 2/2)
- Schema rigidity better captured in new framework
- Investigation failure more explicitly scored
- But basic capabilities still recognized (prep, writeback, explanations)

---

## Key Evidence

**Schema Rigidity (Fatal Flaw)**:
- **"Rare to adjust after setup"** - Their own documentation admission
- Schema locked after configuration
- New columns require major reconfiguration
- Business changes break the system
- No automatic schema evolution

**Single Source Limitation**:
- Cannot join multiple data sources
- Architecture limitation, not connector issue
- Real business questions impossible
- "How do support tickets affect churn?" - Cannot answer (2 sources needed)
- "What's campaign ROI?" - Cannot answer (3+ sources needed)

**Investigation Failure**:
- Can only show WHAT happened (metrics)
- Cannot determine WHY it happened
- No multi-pass reasoning
- No hypothesis testing
- Single query limitation
- No root cause analysis capability

**Tiny Market Presence**:
- Only 15 G2 reviews (vs hundreds for competitors)
- No named major customers
- Absent from analyst reports (Gartner/Forrester)
- Years in market with minimal adoption
- Classic "Marketing Mirage" pattern

**Cost Reality**:
- $21,000/year minimum (10 users)
- $150,000+ estimated year one TCO
- Hidden implementation costs
- No verified ROI case studies
- 42x more expensive than Scoop ($3,588)

---

## Validation Notes

**Score is defensible because**:
- **Documented limitations**: "Rare to adjust" in official docs
- **Architecture**: Single-source design proven
- **Market evidence**: 15 reviews, no major customers
- BUA measures business user independence - DataGPT fails on schema flexibility and investigation

**This is "Metrics Display Tool"** not business analytics:
- Shows single metrics fast
- But cannot investigate causes
- Schema locked after setup
- Single source only
- Portal prison architecture
- Tools-for-looking, not investigating

**Why Lower Than Most Competitors?**:
- Lower than Domo (25/50): No AutoML, single source, worse schema rigidity
- Lower than ThoughtSpot (20/50): No SpotIQ equivalent, single source, schema locked
- Lower than Power BI (14/50): Less visualization, no Excel, single source, schema rigid
- Similar to Snowflake Cortex (13/50): Both dashboard tools with investigation failures
- Similar to Tableau Pulse (11/50): Both metrics display with rigid limitations

**Why 12/50 Specifically?**:
- Gets 0/4 on three critical components (Investigation, ML, Schema Evolution)
- Gets 0/4 on Native Integration and 0/3 on Portal Prison
- Gets 0/4 on Brand and 0/3 on Presentation Speed
- Only scores on basic capabilities: queries (1), speed (1), explanations (3), visuals (1), interface (1), prep (2), writeback (2), connections (1)
- Total: 2+1+3+1+5 = 12/50

---

**Last Updated**: September 27, 2025
**Framework Version**: Business User Autonomy
**Confidence**: Very High (based on comprehensive research including Phase 2/3 analysis and schema rigidity documentation)