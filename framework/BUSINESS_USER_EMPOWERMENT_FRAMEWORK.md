# Business User Empowerment Framework (5 Dimensions)

**Version**: 2.0
**Date**: September 27, 2025
**Status**: Active Framework

---

## Executive Summary

The Business User Empowerment Framework measures how completely a business user can self-serve analytics **without dependencies on IT, data teams, analysts, or designers**.

**Core Question**: Can a non-technical business user independently:
1. Start using the tool themselves?
2. Work in their existing tools?
3. Get deep insights explained clearly?
4. Create professional presentations?
5. Handle all data operations?

---

## The 5 Dimensions

### Pattern: Removing Dependencies
Each dimension measures a specific dependency removal:

| Dimension | Removes Dependency On | Empowerment Question |
|-----------|----------------------|----------------------|
| 1. **Autonomy** | IT department | Can user start and operate themselves? |
| 2. **Flow** | Separate BI portal | Can user work in their existing tools? |
| 3. **Understanding** | Data analyst | Can user get deep insights themselves? |
| 4. **Presentation** | Designer | Can user create professional outputs? |
| 5. **Data** | Data engineer | Can user handle data operations? |

**Total Score**: 50 points (5 dimensions × 10 points each)

---

## Dimension 1: Autonomy (10 points)

**What It Measures**: Can business users start and operate without IT involvement?

### Key Components
- **Self-service setup**: Can user install/configure themselves? (no IT project required)
- **Question independence**: Can user ask ad-hoc questions? (no analyst queue)
- **Speed to value**: How fast from signup to first insight?

### Scoring Rubric (0-10)

| Score | Capability |
|-------|------------|
| **0-2** | Requires IT implementation project (weeks/months) |
| **3-4** | IT setup required but user can ask questions after (days/weeks) |
| **5-6** | Self-service setup but requires training/configuration (hours/days) |
| **7-8** | Quick self-service setup, minimal training needed (30-60 min) |
| **9-10** | Instant self-service (under 5 minutes), natural language, no training |

### Business Impact
- **High score (9-10)**: SMB owner or department head can start TODAY
- **Low score (0-4)**: Requires IT project, budgeting, implementation timeline

### Competitive Examples
- **Power BI Copilot**: 3/10 (14-week F64 setup + semantic model required)
- **Snowflake Cortex**: 2/10 (6-month implementation, data engineering required)
- **Scoop**: 9/10 (30-second Slack install, connect data sources, start asking)

---

## Dimension 2: Flow (10 points)

**What It Measures**: Can business users work in their existing tools vs switching to separate BI portal?

### Key Components
- **Native integration**: Works in Slack, mobile, where user already works?
- **No portal prison**: Can avoid logging into separate BI tool?
- **Interface simplicity**: Natural language vs learning query syntax?

### Scoring Rubric (0-10)

| Score | Capability |
|-------|------------|
| **0-2** | Separate portal only, must login and navigate tool |
| **3-4** | Portal-based but has basic export/embed capabilities |
| **5-6** | Some integrations (Slack notifications) but analysis requires portal |
| **7-8** | Native in one key tool (Slack or Excel) with full functionality |
| **9-10** | Native in multiple tools (Slack + Excel + Mobile), natural language everywhere |

### Business Impact
- **High score (9-10)**: User works in familiar environment, no tool switching
- **Low score (0-4)**: Must learn new interface, separate from daily workflow

### Competitive Examples
- **Domo**: 1/10 (portal prison, no native integrations)
- **Power BI Copilot**: 4/10 (separate tool, limited Excel Copilot Pro for $30/user)
- **Scoop**: 9/10 (Slack native, mobile, Google Sheets plugin, PowerPoint integration)

---

## Dimension 3: Understanding (10 points)

**What It Measures**: Can business users get deep insights (root cause WHY) without data analyst?

### Key Components
- **Investigation depth**: Multi-pass reasoning vs single query
- **Root cause analysis**: Finds WHY not just WHAT
- **ML insights**: Provides pattern discovery (J48, clustering, etc.)
- **Explainability**: ML/statistical results explained in business language

### Scoring Rubric (0-10)

| Score | Capability |
|-------|------------|
| **0-2** | Static dashboards only (shows WHAT happened) |
| **3-4** | Single-query answers, no follow-up investigation |
| **5-6** | User can drill down manually but must know what to ask |
| **7-8** | Multi-pass investigation OR explainable ML (but not both) |
| **9-10** | Automatic multi-pass investigation + ML insights + business-language explanation |

### Business Impact
- **High score (9-10)**: User finds root causes themselves, no analyst ticket required
- **Low score (0-4)**: User sees problem but needs analyst to investigate why

### Technical Depth (What Powers Score 9-10)
- **Multi-pass investigation**: 3-10 queries with context retention
- **Three-Layer AI Data Scientist**:
  - Layer 1: Automatic data prep (cleaning, binning, feature engineering)
  - Layer 2: Real ML execution (J48 decision trees 800+ nodes, EM clustering, JRip rules)
  - Layer 3: AI explanation engine (translates model output to business language)

### Competitive Examples
- **Power BI Copilot**: 2/10 (single query only, no investigation, nondeterministic)
- **ThoughtSpot**: 4/10 (single query, no ML, user must know what to drill into)
- **Scoop**: 9/10 (multi-pass investigation + Three-Layer AI + business explanations)

---

## Dimension 4: Presentation (10 points)

**What It Measures**: Can business users create professional, branded visual outputs without designer?

### Key Components
- **Visual quality**: Pixel-perfect, professional aesthetics
- **Brand compliance**: Automatic brand detection and application
- **Speed**: Time to create board-ready presentation
- **Output formats**: PowerPoint, Google Slides, live decks

### Scoring Rubric (0-10)

| Score | Capability |
|-------|------------|
| **0-2** | Screenshot exports only, manual formatting required |
| **3-4** | Basic chart exports, no branding, requires manual PowerPoint work (3-4 hours) |
| **5-6** | Template-based exports but user must apply branding/formatting (1-2 hours) |
| **7-8** | Good visual output but limited branding automation (30-60 min) |
| **9-10** | AI-powered branded deck generation (under 1 minute), board-ready |

### Business Impact
- **High score (9-10)**: User creates executive presentations themselves, no designer
- **Low score (0-4)**: User must export ugly charts, spend hours formatting, or request design help

### Technical Depth (What Powers Score 9-10)
- **Visual Intelligence System**:
  - Automatic brand detection (extract colors from existing templates)
  - AI color theory (semantic color mapping, accessibility compliance)
  - Canvas-based presentation system (1600x900 pixel-perfect)
  - Live data overlay (presentations update automatically)
  - Google Slides bi-directional sync

### Competitive Examples
- **Power BI**: 3/10 (basic chart exports, manual PowerPoint workflow)
- **Tableau**: 4/10 (better visuals but still manual presentation creation)
- **Scoop**: 9/10 (30-second branded deck generation with automatic brand detection)

---

## Dimension 5: Data (10 points)

**What It Measures**: Can business users handle all data operations without data engineer?

### Key Components
- **Data connections**: Can user connect to data sources themselves?
- **Schema evolution**: What happens when data structure changes?
- **Data preparation**: Can user transform/clean data without SQL/Python?
- **Operationalization**: Can user write insights back to operational systems?
- **Maintenance**: Does system break when data changes?

### Scoring Rubric (0-10)

| Score | Capability |
|-------|------------|
| **0-2** | Requires data engineer for setup, prep, and all changes (weeks per change) |
| **3-4** | Data engineer sets up, user can query but breaks on schema changes (days to fix) |
| **5-6** | Some self-service data prep but limited, requires IT for schema updates (1-2 days) |
| **7-8** | Good data prep tools, faster schema adaptation but still requires some IT (hours) |
| **9-10** | Complete self-service: connections, prep, schema evolution automatic (minutes), writeback |

### Business Impact
- **High score (9-10)**: New CRM field available immediately, user can prep data themselves
- **Low score (0-4)**: Every data change = IT ticket, days/weeks waiting

### Technical Depth (What Powers Score 9-10)
- **Spreadsheet Calculation Engine**: 150+ Excel functions for data prep (VLOOKUP, SUMIFS, etc.)
- **Schema Evolution**: Automatic detection and adaptation to data structure changes
- **Direct connections**: Connect to any data source without data warehouse
- **Writeback capabilities**: Update CRM/operational systems with ML scores
- **Smart Scanner**: Handles messy, unstructured data automatically

### Competitive Examples
- **Power BI Copilot**: 3/10 (semantic model breaks on changes, 14-day rebuild, requires data engineer)
- **Tableau**: 4/10 (better than Power BI but still requires data modeling, breaks on changes)
- **Scoop**: 7/10 (schema evolution, spreadsheet engine, but writeback expanding)

---

## Category Classification

**Total Score** (sum of 5 dimensions, max 50 points):

| Score Range | Category | Description |
|-------------|----------|-------------|
| **40-50** | **A - True Self-Service** | Business users fully empowered across all dimensions |
| **25-39** | **B - Analyst Workbench** | Good for analysts, limited for business users |
| **15-24** | **C - IT Platform** | Requires IT/analyst involvement for most tasks |
| **0-14** | **D - Dashboard Tool** | Static views, minimal self-service capability |

---

## Competitor Scoring Examples

### Power BI Copilot: 15/50 (Category C - IT Platform)
- **Autonomy**: 3/10 (14-week F64 setup + semantic model)
- **Flow**: 4/10 (separate tool, limited Excel Copilot Pro)
- **Understanding**: 2/10 (single query, nondeterministic, no ML)
- **Presentation**: 3/10 (basic charts, no branded deck generation)
- **Data**: 3/10 (semantic model breaks, requires data engineer)

### Scoop: 42/50 (Category A - True Self-Service)
- **Autonomy**: 9/10 (30-second Slack install, immediate value)
- **Flow**: 9/10 (Slack native, Excel integration, mobile, PowerPoint)
- **Understanding**: 9/10 (multi-pass investigation + Three-Layer AI)
- **Presentation**: 8/10 (30-second branded decks, expanding)
- **Data**: 7/10 (schema evolution, spreadsheet engine, expanding writeback)

---

## Why This Framework?

### Alignment with Scoop's 5 Moats

| Moat | Framework Dimension(s) | How It Maps |
|------|----------------------|-------------|
| **Spreadsheet Engine Moat** | Data | 150+ Excel functions for data prep |
| **AI Data Scientist Moat** | Understanding | Three-Layer AI (prep + ML + explanation) |
| **Investigation Moat** | Understanding | Multi-pass reasoning with context |
| **Integration Moat** | Autonomy + Flow | 30-second setup + Slack/Excel native |
| **Visual Intelligence Moat** | Presentation | AI-powered branded deck generation |

**All 5 moats are represented** in the framework.

### Comparison to Old BUPAF

**Old Framework** (Browse, Understand, Predict, Act, Fix):
- ❌ Missing workflow integration entirely
- ❌ Missing visual intelligence entirely
- ❌ Browse/Understand/Predict overlapped significantly
- ❌ Act was too broad (covered too many things)
- ✅ Predict made ML explicit
- ✅ Fix captured maintenance well

**New Framework** (Autonomy, Flow, Understanding, Presentation, Data):
- ✅ All 5 dimensions are distinct
- ✅ Clear pattern: removes dependency on IT/portal/analyst/designer/engineer
- ✅ Covers all 5 moats explicitly
- ✅ Each dimension measures "can business user do X themselves?"
- ✅ Better measures business user empowerment holistically

---

## Usage in Competitive Content

### In BUPAF Comparison Pages
1. Lead with framework explanation (Section 1)
2. Show competitor's score breakdown (table)
3. Deep dive on 2-3 dimensions where competitor fails worst (Section 2)
4. Show how Scoop scores high across all 5 (Section 3)

### In Battle Cards
- Quote overall score: "Power BI Copilot: 15/50 (Category C - IT Platform)"
- Emphasize worst dimensions: "Scores 2/10 on Understanding - can't investigate WHY"

### In Web Comparisons
- Use framework as organizing principle for capability sections
- Map features to dimensions explicitly

---

## Framework Maintenance

### When to Update Scores
- Quarterly competitor capability reviews
- When major product launches occur
- When new evidence emerges (Gartner reports, customer complaints)

### Version History
- **Version 1.0**: Original BUPAF (Browse, Understand, Predict, Act, Fix) - January 2024
- **Version 2.0**: New framework (Autonomy, Flow, Understanding, Presentation, Data) - September 27, 2025

---

## Next Steps for Implementation

1. **Update BUPAF_COMPARISON_TEMPLATE.md** with new framework
2. **Re-score all competitors** using new rubrics
3. **Update existing battle cards** with new scores
4. **Generate new BUPAF comparison pages** for priority competitors:
   - Power BI Copilot
   - Tableau Pulse
   - ThoughtSpot
   - Domo
5. **Document scoring rationale** for each competitor in their evidence folders

---

**Framework Owner**: Competitive Intelligence Team
**Review Cadence**: Quarterly
**Last Updated**: September 27, 2025