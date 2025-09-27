# BUA Framework Scoring - Snowflake Cortex

**Competitor**: Snowflake Cortex
**Date Scored**: September 27, 2025
**Scored By**: AI Competitive Intelligence System
**Total Score**: 17/59 (29%, Category C - IT Platform)
**Previous Score**: 13/50 (Old BUPAF Framework - no change)

---

## Dimension 1: Autonomy (2/10)

### Setup (0/4)
**Score**: 0/4
**Evidence**:
- **Requires semantic model creation** - Weeks of IT work to define YAML files
- Business users cannot query until IT defines data relationships
- "Requires IT to create semantic model before any business user can query" (BATTLE_CARD)
- Not even basic questions possible without semantic layer
- 3-6 months typical implementation timeline
**Source**:
- Phase 2 functionality analysis: "Requires IT to define semantic layer before business users can query"
- Multiple sources on semantic model dependency
**Reasoning**: Complete IT dependency. Business users blocked until semantic model built. Zero self-service.

### Questions (1/3)
**Score**: 1/3
**Evidence**:
- Text-to-SQL natural language capability exists
- BUT: Limited to semantic model scope (IT defines what's query-able)
- **35% business question success rate** (10/28 test queries)
- Cannot ask "why" questions - complete failure
- Single query limitation (stateless)
**Source**:
- Phase 2: "35% business correctness rate (10/28 matched expectations)"
- BATTLE_CARD: "35% business success rate"
**Reasoning**: Can ask questions but 65% fail. Semantic model constraints limit flexibility severely.

### Speed (1/3)
**Score**: 1/3
**Evidence**:
- Weeks of semantic model setup before first query
- SQL generation is fast once semantic model exists
- BUT: Cannot get insights without IT building semantic layer first
- 3-6 month implementation timeline typical
**Source**: Multiple implementation timeline sources
**Reasoning**: Fast query generation but weeks/months to value. Not instant insights.

**Total Autonomy**: 2/10

---

## Dimension 2: Flow (1/10)

### Native Integration (0/4)
**Score**: 0/4
**Evidence**:
- **Excel**: ZERO support - "No Excel integration in official documentation"
- **Slack**: Available through Cortex Agents API but requires development
- **PowerPoint**: NO native integration - manual screenshot workflow
- **Mobile**: API only - no native tablet/smartphone interfaces
- API-only access means developers required
**Source**:
- Phase 2: "Excel Integration - CONFIRMED ZERO SUPPORT"
- Phase 2: "PowerPoint Integration - NO NATIVE POWERPOINT INTEGRATION"
- BATTLE_CARD: "Zero mobile support - API-only"
**Reasoning**: Complete failure on workflow integration. API-only is not native.

### Portal Prison (0/3)
**Score**: 0/3
**Evidence**:
- Must use Snowflake console for all queries
- No escape to native tools
- API-only mobile means developers required
- Cannot work in Excel/PowerPoint/Slack without custom development
**Source**: Product architecture documentation
**Reasoning**: 100% portal-dependent or requires custom development. No native tool integration.

### Interface Simplicity (1/3)
**Score**: 1/3
**Evidence**:
- Natural language interface is conceptually simple
- BUT: Requires understanding of semantic model limitations
- **65% of business questions fail** - not actually simple
- SQL generation errors require technical troubleshooting
- "Actual statement count 3 did not match desired statement count 1" - technical errors exposed
**Source**: Phase 2 testing results and error documentation
**Reasoning**: NL interface looks simple but fails frequently. Technical errors exposed to users.

**Total Flow**: 1/10

---

## Dimension 3: Understanding (4/10)

### Investigation (0/4)
**Score**: 0/4
**Evidence**:
- **Complete failure on "why" questions**: "Why are customers churning?" failed with error
- Single query limitation - cannot multi-step investigate
- Stateless - no context retention between queries
- "Cannot execute multi-step churn analysis" (Phase 2 testing)
- Error: "Actual statement count 3 did not match the desired statement count 1"
**Source**:
- Phase 2: Test evidence showing complete churn analysis failure
- BATTLE_CARD: "Zero investigation capability"
**Reasoning**: Cannot investigate WHY. Single queries only. Fundamental architectural limitation.

### ML (1/3)
**Score**: 1/3
**Evidence**:
- **No automatic ML** - basic statistical functions only
- Has CORR(), STDDEV(), PERCENTILE_CONT() - correlation not causation
- No J48, JRip, or clustering algorithms
- "Why are customers churning?" query failed completely (no ML)
- Can calculate statistics but cannot discover patterns
**Source**: Phase 2 ML capabilities analysis
**Reasoning**: Has basic statistics but not real ML. No pattern discovery, no predictive models.

### Explanation (3/3)
**Score**: 3/3
**Evidence**:
- Returns SQL query used (transparency)
- Shows data tables clearly
- Numbers and aggregations are explained
- BUT: Only explains WHAT, not WHY
- 25% of queries strip critical context (values without labels)
**Source**: Phase 2 technical analysis on context stripping
**Reasoning**: Good at explaining what it did (SQL transparency), but shallow on business insights.

**Total Understanding**: 4/10

---

## Dimension 4: Presentation (1/10)

### Visuals (1/3)
**Score**: 1/3
**Evidence**:
- Basic table and chart responses
- Can return visualization data
- Limited chart types compared to BI tools
- No intelligent visualization selection
- Tables are functional but not polished
**Source**: Product documentation on output formats
**Reasoning**: Basic visualization capabilities. Functional but not impressive.

### Brand (0/4)
**Score**: 0/4
**Evidence**:
- No brand customization
- No logo detection or insertion
- Standard Snowflake output only
- Cannot customize colors or themes
- No AI-powered brand intelligence
**Source**: No evidence of brand capabilities found
**Reasoning**: Zero brand automation. Standard output only.

### Speed (0/3)
**Score**: 0/3
**Evidence**:
- **PowerPoint**: Manual screenshot workflow - "30 minutes vs 30 seconds" (BATTLE_CARD)
- **Export**: Manual CSV download and Excel import
- No automated presentation generation
- "Screenshot workflow" documented
**Source**:
- Phase 2: "Manual screenshot and copy-paste workflow"
- BATTLE_CARD presentation comparison
**Reasoning**: Completely manual presentation creation. No automation whatsoever.

**Total Presentation**: 1/10

---

## Dimension 5: Data (5/10)

### Connections (2/2)
**Score**: 2/2
**Evidence**:
- Native Snowflake data warehouse connectivity (obviously)
- Can query any table in Snowflake
- Strong integration with Snowflake ecosystem
- External data through Snowflake stages
**Source**: Snowflake architecture
**Reasoning**: Excellent connectivity within Snowflake ecosystem. Native by design.

### Schema Evolution (0/4)
**Score**: 0/4
**Evidence**:
- **Semantic model breaks on schema changes**
- YAML files must be manually updated when columns added/removed
- Business users blocked until IT updates semantic model
- No automatic adaptation
- Requires IT maintenance on every schema change
**Source**: Semantic model architecture documentation
**Reasoning**: Universal BI platform failure. Semantic model rigidity means complete failure on schema changes.

### Prep (2/2)
**Score**: 2/2
**Evidence**:
- SQL-based transformations available
- Snowflake's full SQL dialect for prep
- Can create views, CTEs, etc.
- Strong data transformation capabilities
**Source**: Snowflake SQL documentation
**Reasoning**: Full SQL power for data prep. Adequate for technical users.

### Writeback (1/2)
**Score**: 1/2
**Evidence**:
- Can write back to Snowflake tables via SQL
- Not operationalized for CRM/ML score delivery
- Requires custom development for business writeback
- No native CRM integration
**Source**: Snowflake SQL INSERT/UPDATE capabilities
**Reasoning**: Technical writeback possible but not business-user-friendly. Requires development.

**Total Data**: 5/10

---

## Score Summary

| Dimension | Score | Key Weakness |
|-----------|-------|--------------|
| Autonomy | 2/10 | Requires weeks of IT semantic model setup, 35% question success rate |
| Flow | 1/10 | Zero Excel/PowerPoint/Mobile, API-only, portal-dependent |
| Understanding | 4/10 | **Cannot answer "why" questions** (complete investigation failure) |
| Presentation | 1/10 | Manual screenshot workflow, no automation, no brand intelligence |
| Data | 5/10 | Strong Snowflake connectivity but **semantic model breaks on schema changes** |
| **TOTAL** | **13/50** | **Category D - Dashboard Tool** |

---

## Category: D - Dashboard Tool (0-14 points)

**Definition**: Basic tools with severe business user empowerment limitations. Require significant IT support. Technical focus over business user needs.

**Snowflake Cortex Reality**:
- SQL generation tool, not business analytics platform
- **35% business question success rate** (65% failure rate)
- Requires semantic model maintenance (IT dependency)
- $86K-$171K first year TCO
- Cannot investigate WHY (fundamental limitation)

---

## Key Differentiators vs Scoop (45/50)

### 1. **Understanding Dimension** Gap
- **Scoop**: 9/10 (multi-pass investigation, explainable ML, root cause discovery)
- **Snowflake Cortex**: 4/10 (0/4 on investigation - "why" questions fail completely)
- **Impact**: "Why are customers churning?" - Scoop finds root causes, Cortex returns error.

### 2. **Autonomy Dimension** Gap
- **Scoop**: 9/10 (30-second setup, 100% question success)
- **Snowflake Cortex**: 2/10 (weeks of semantic model setup, 35% success rate)
- **Impact**: Weeks of IT work + 65% failure rate vs instant insights.

### 3. **Flow Dimension** Gap
- **Scoop**: 9/10 (Excel formulas, native PowerPoint, Slack)
- **Snowflake Cortex**: 1/10 (zero Excel, zero PowerPoint, API-only)
- **Impact**: Native workflow vs API development required for everything.

### 4. **Data Dimension** Gap
- **Scoop**: 9/10 (automatic schema evolution)
- **Snowflake Cortex**: 5/10 (0/4 on schema - semantic model breaks)
- **Impact**: Schema changes require semantic model rebuilds. Scoop adapts instantly.

### 5. **Presentation Dimension** Gap
- **Scoop**: 9/10 (auto PowerPoint, brand intelligence)
- **Snowflake Cortex**: 1/10 (manual screenshots, 30 minutes per deck)
- **Impact**: Automated presentations vs screenshot hell.

---

## Scoring Rationale: Why 13/50

**Extremely Low Score Because**:
- **Zero investigation capability** - automatic 0/4 (cannot answer "why")
- **Zero workflow integration** - automatic 0/4 on Native Integration
- **Semantic model dependency** - penalizes Autonomy (0/4 setup)
- **65% question failure rate** - penalizes Questions (1/3 only)
- **No schema evolution** - automatic 0/4 (universal failure)

**Only Scores Points For**:
- Good Snowflake connectivity (2/2)
- SQL transparency in explanations (3/3)
- SQL-based data prep (2/2)
- Basic SQL writeback (1/2)

**Why Same Score as Old Framework (13/50)**:
- New framework better captures investigation failure (0/4 explicit)
- Properly penalizes semantic model dependency
- More accurate on workflow integration failure
- But limited strengths still recognized (connectivity, SQL)

---

## Key Evidence

**Business Question Failure**:
- **35% success rate** - Only 10/28 test queries delivered usable insights
- **"Why are customers churning?" FAILED** - Cannot execute multi-statement analysis
- Error: "Actual statement count 3 did not match the desired statement count 1"

**Cost Reality**:
- **$86K-$171K first year TCO** (implementation + compute + maintenance)
- 24x more expensive than Scoop ($3,588)
- Hidden warehouse compute costs
- Semantic model maintenance overhead (2 FTE estimated)

**IT Dependency**:
- **Weeks of semantic model setup** before business users can query
- YAML files must define every relationship
- Cannot query without semantic layer
- Business users blocked on IT for every schema change

**Investigation Failure**:
- Cannot answer "why" questions (test evidence)
- Single query limitation (stateless)
- No multi-hypothesis testing
- No root cause discovery

---

## Validation Notes

**Score is defensible because**:
- **Test evidence**: Actual queries run showing 35% success rate
- **Documented limitations**: Semantic model dependency in official docs
- **Architecture**: Single-query design cannot support investigation
- BUA measures business user independence - Cortex fails completely

**This is "SQL Generation Tool"** not business analytics:
- Generates technically correct SQL
- But doesn't deliver business insights
- Requires IT to define semantic model
- Cannot investigate root causes
- Tools-for-tools-teams, not business users

**Why Lower Than All Others Except Tableau/DataChat?**
- Worse than Power BI (14/50): Less visualization, more IT-dependent
- Worse than ThoughtSpot (20/50): Lower success rate, less investigation
- Worse than Domo (25/50): No visuals, no dashboard layer
- Similar to Tableau Pulse (11/50): Both dashboard-narration tools with failures

---

**Last Updated**: September 27, 2025
**Framework Version**: Business User Autonomy
**Confidence**: Very High (based on comprehensive research + actual testing with 28 queries)