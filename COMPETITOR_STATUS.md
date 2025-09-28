# Competitive Intelligence Status - September 28, 2025

## Overall Progress: 7 of 11 Competitors With Strategy Docs

### Strategy Complete, Web Comparison Deployed (1)
| Competitor | BUA Score | Strategy Version | Web Comparison | Status |
|------------|-----------|------------------|----------------|--------|
| Power BI Copilot | 32/100 (D) | v2.0 (Sept 28) | 8,450 words | ✅ Deployed |

### Strategy + Web Comparison Generated (3)
| Competitor | BUA Score | Strategy Version | Web Comparison | Status |
|------------|-----------|------------------|----------------|--------|
| Snowflake Cortex | 26/100 (C) | v1.1 (Sept 28) | 8,608 words | ✅ Generated (ready to deploy) |
| Tableau Pulse | 37/100 (C) | v1.1 (Sept 28) | 6,568 words | ✅ Generated (ready to deploy) |
| Zenlytic | 42/100 (C) | v1.1 (Sept 28) | 8,151 words | ✅ Generated (ready to deploy) |

### Strategy + Web Comparison Generated (Additional 3)
| Competitor | BUA Score | Strategy Version | Web Comparison | Status |
|------------|-----------|------------------|----------------|--------|
| ThoughtSpot | 57/100 (B) | v1.1 (Sept 28) | 8,969 words | ✅ Generated (ready to deploy) |
| Domo | 62/100 (B) | v1.1 (Sept 28) | 8,699 words | ✅ Generated (ready to deploy) |
| Qlik | 47/100 (C) | v1.1 (Sept 28) | 8,361 words | ✅ Generated (ready to deploy) |

### Priority Queue (4 remaining)

**Tier 2: Lower Market Presence**
- Sisense: 28/100 (C) - Embedded analytics
- DataGPT: 22/100 (D) - Single-source limitation
- Tellius: 22/100 (D) - Apache Spark crashes
- DataChat: 17/100 (D) - Minimal market presence


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

## Next Actions

1. **Deploy** all 6 web comparisons to production:
   - Snowflake Cortex (8,608 words)
   - Tableau Pulse (6,568 words)
   - Zenlytic (8,151 words)
   - ThoughtSpot (8,969 words) ⭐ NEW
   - Domo (8,699 words) ⭐ NEW
   - Qlik (8,361 words) ⭐ NEW

2. **Consider** Tier 2 strategies + web comparisons (Sisense, DataGPT, Tellius, DataChat) - lower priority

Last Updated: September 28, 2025 (Evening - Tier 1 fully complete with strategies + web comparisons)
