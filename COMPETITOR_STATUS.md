# Competitive Intelligence Status - September 28, 2025

## Overall Progress: 7 of 11 Competitors With Strategy Docs

### Strategy + Web Comparison Deployed (7) ✅ ALL TIER 1 COMPLETE
| Competitor | BUA Score | Strategy Version | Web Comparison | Status |
|------------|-----------|------------------|----------------|--------|
| Power BI Copilot | 32/100 (D) | v2.0 (Sept 28) | 8,450 words | ✅ Deployed |
| Snowflake Cortex | 26/100 (C) | v1.1 (Sept 28) | 8,608 words | ✅ Deployed |
| Tableau Pulse | 37/100 (C) | v1.1 (Sept 28) | 6,568 words | ✅ Deployed |
| Zenlytic | 42/100 (C) | v1.1 (Sept 28) | 8,151 words | ✅ Deployed |
| ThoughtSpot | 57/100 (B) | v1.1 (Sept 28) | 8,969 words | ✅ Deployed |
| Domo | 62/100 (B) | v1.1 (Sept 28) | 8,699 words | ✅ Deployed |
| Qlik | 47/100 (C) | v1.1 (Sept 28) | 8,361 words | ✅ Deployed |

### Strategy + Web Comparison Generated (4 Additional) ✅ TIER 2 COMPLETE
| Competitor | BUA Score | Strategy Version | Web Comparison | Status |
|------------|-----------|------------------|----------------|--------|
| Sisense | 28/100 (C) | v1.1 (Sept 28) | 7,254 words | ✅ Generated (ready to deploy) |
| DataGPT | 22/100 (D) | v1.1 (Sept 28) | 6,116 words | ✅ Generated (ready to deploy) |
| Tellius | 22/100 (D) | v1.1 (Sept 28) | 6,121 words | ✅ Generated (ready to deploy) |
| DataChat | 17/100 (F) | v1.1 (Sept 28) | 3,241 words | ✅ Generated (ready to deploy) |


## Key Patterns Identified

### Pattern 1: YAML/Semantic Layer Dependency
- **Competitors**: Snowflake Cortex, Zenlytic, (likely ThoughtSpot, Tableau, Domo)
- **Weakness**: IT must maintain definitions before business users can query
- **Defensibility**: Architectural

### Pattern 2: Portal Prison (0/6 on Portal Prison BUA score)
- **Competitors**: All 3 completed today
- **Weakness**: Must use vendor portal, no native Excel/Slack/PowerPoint
- **Defensibility**: Architectural (dashboard-first design)

### Pattern 3: Text-to-SQL Architecture
- **Competitors**: Snowflake, Zenlytic
- **Weakness**: One SQL query per question, no multi-pass investigation
- **Defensibility**: Architectural

### Pattern 4: Schema Brittleness
- **Competitors**: Tableau Pulse (400 errors), semantic layer tools
- **Weakness**: Breaks when data schemas change
- **Defensibility**: Architectural

## Templates Status

### Competitive Strategy Template
- **Version**: 1.1
- **Location**: `/competitors/SHARED/COMPETITIVE_STRATEGY_TEMPLATE.md`
- **Features**: Defensibility framework, emphasis adjustment philosophy, product type classification

### Web Comparison Template
- **Version**: 2.1
- **Location**: `/templates/WEB_COMPARISON_TEMPLATE.md`
- **Features**: Question Hierarchy, Semantic Model Boundary (optional), At-a-Glance question rows, complex query FAQ

## Competitive Insights from Tier 1 Strategies (Sept 28)

### ThoughtSpot (57/100, Category B)
**Top 3 Weaknesses**:
1. Search-Based Architecture Limitations (30%) - Architectural | Single-query responses, not multi-pass investigation
2. Expensive IT Dependency (25%) - Strategic + Architectural | $140K-$500K annually, 96 CPUs/600GB RAM for 2-3TB
3. Portal Prison + Zero Native Tools (20%) - Architectural | Zero Excel formulas, no PowerPoint generation

**Key Insight**: Ex-Google search heritage = search platform, not investigation platform. Semantic layer (even "Agentic") still requires IT.

### Domo (62/100, Category B)
**Top 3 Weaknesses**:
1. Portal Prison + Dashboard-First Architecture (30%) - Architectural | DomoGPT requires AI Readiness metadata, Excel formulas disabled
2. AI Hype vs AI Reality (Bolt-On LLM) (25%) - Architectural + Temporal | 2010s dashboard platform + 2024 LLM layer
3. Consumption Pricing + Cost Explosion (20%) - Strategic | 1120% renewal increases, $95-134K annually

**Key Insight**: Dashboard-first DNA from 2010s. DomoGPT is bolt-on LLM, not investigation platform. Consumption pricing creates renewal shock.

### Qlik (47/100, Category C)
**Top 3 Weaknesses**:
1. Legacy Architecture + Cloud Migration Struggles (30%) - Architectural + Temporal | Desktop-era in-memory engine, hour-long loads, 500-user crashes
2. Business User Empowerment Failure (25%) - Architectural + Strategic | 58% certification fail rate, "depend on developers"
3. Associative Engine Not Built for AI (20%) - Architectural | 1990s manual exploration, not 2024 AI investigation

**Key Insight**: QlikView desktop origins (single-user analyst tool). In-memory architecture doesn't scale cloud-native. Associative engine predates LLM by 20+ years.

## Quality Assurance: All 7 Deployments Verified ✅

**All deployments inspected and approved (Grade A, 9/10 average)**:
- ThoughtSpot: Search vs investigation paradigm clear, $500K crash story prominent
- Domo: DomoGPT fairly handled, 1120% renewal increase featured
- Qlik: Legacy framing balanced with historical credit, 58% cert fail emphasized
- Snowflake, Tableau, Zenlytic: Multi-turn vs multi-pass distinction excellent

**Quality markers across all 7**:
- Strategic emphasis followed (30%/25%/20%)
- Evidence-based positioning (customer quotes, specific data)
- Professional credible tone (acknowledges competitor strengths)
- Investigation-first positioning clear
- Zero critical issues found

## Tier 2 Complete: Key Insights

### Sisense (28/100, Category C)
**Top 3 Weaknesses**:
1. Embedded Analytics Focus (35%) - Architectural | ISV platform, not business user self-service
2. ARIMA Marketing Mirage (25%) - Architectural | Fake AI, just curve fitting
3. Excel Export-Only (20%) - Architectural | Portal prison, no formulas

**Key Insight**: Built for software vendors to embed, not for business user empowerment. ARIMA fake AI is most defensible attack.

### DataGPT (22/100, Category D)
**Top 3 Weaknesses**:
1. Single-Source Architecture (25%) - Architectural | Cannot join multiple data sources
2. Investigation Failure (25%) - Architectural | Single-query limitation
3. Schema Rigidity (20%) - Architectural | "Rare to adjust after setup"

**Key Insight**: Fast metrics display for single source, but cannot investigate across datasets or handle schema changes.

### Tellius (22/100, Category D)
**Top 3 Weaknesses**:
1. Apache Spark Architecture Crashes (25%) - Architectural | Technical instability
2. Complete Excel Elimination (25%) - Strategic | Forces workflow destruction
3. Natural Language Adoption Failure (20%) - Temporal | Vendor admitted

**Key Insight**: Apache Spark reliability crisis is architectural flaw. Excel replacement strategy failed.

### DataChat (17/100, Category F - LOWEST)
**Top 3 Weaknesses**:
1. Zero Excel Integration (35%) - Architectural | No formulas, no support
2. No API Access (25%) - Architectural | Portal prison, cannot integrate
3. Single Query Limitation (20%) - Architectural | Text-to-SQL translator only

**Key Insight**: Lowest BUA score. Minimal functionality, zero market validation after 7 years.

## Next Actions

1. ✅ **ALL 11 COMPETITORS COMPLETE**: 100% strategy + web comparison coverage
   - Tier 1 deployed (7): Power BI, Snowflake, Tableau, Zenlytic, ThoughtSpot, Domo, Qlik
   - Tier 2 ready (4): Sisense, DataGPT, Tellius, DataChat

2. **Deploy Tier 2** to production (4 remaining web comparisons)

3. **Repository Status**: Complete competitive intelligence suite

Last Updated: September 28, 2025 (Late Evening - ALL 11 COMPETITORS COMPLETE)
