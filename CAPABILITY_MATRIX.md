# Platform Capability Matrix

**Last Updated**: September 30, 2025
**Purpose**: Objective feature comparison across 12 AI analytics platforms
**Scoring**: ✓✓✓ (Full capability) | ✓✓ (Partial) | ✓ (Basic) | ✗ (None) | ⚬⚬⚬ (Announced/Roadmap)

---

## Navigation

- [Setup & Accessibility](#setup--accessibility)
- [Agentic Investigation](#agentic-investigation)
- [Machine Learning](#machine-learning)
- [Data Transformation](#data-transformation)
- [Output & Distribution](#output--distribution)
- [Platform Infrastructure](#platform-infrastructure)
- [Evidence Sources](#evidence-sources)

---

## Setup & Accessibility

Measures how quickly business users can start getting value without IT support.

| Platform | Setup Time | No Data Modeling | No Training Required | No IT for Setup |
|----------|-----------|------------------|---------------------|-----------------|
| **Scoop Analytics** | **Minutes** | ✓✓✓ | ✓✓✓ | ✓✓✓ |
| Domo | Hours-Days | ✗ | ✓ | ✗ |
| ThoughtSpot | Days-Weeks | ✗ | ✓ | ✗ |
| Qlik | Hours-Months | ✗ | ✗ | ✗ |
| Zenlytic | Weeks | ✗ | ✓✓ | ✗ |
| Tableau Pulse | Days-Weeks | ✗ | ✓ | ✗ |
| Power BI Copilot | Hours-Days | ✗ | ✓ | ✗ |
| Sisense | Weeks | ✗ | ✗ | ✗ |
| Snowflake Cortex | Weeks | ✗ | ✓ | ✗ |
| DataGPT | Days | ✗ | ✓✓ | ✗ |
| Tellius | Days-Weeks | ✗ | ✓ | ✗ |
| DataChat | Days | ✗ | ✓✓ | ✗ |

**Evidence**:
- **Scoop**: Upload CSV, start analyzing in <5 minutes. No semantic layer, no modeling, no training.
- **No Data Modeling**: Competitors require semantic layers (Cortex YAML), metric definitions (Pulse), or data models (Qlik).
- **No Training**: Qlik has 58% certification failure rate. Power BI requires understanding of data models.

---

## Agentic Investigation

Measures the platform's ability to autonomously investigate "why" questions through multi-step reasoning.

| Platform | Natural Language Query | Multi-Turn Chat | Interactive Exploration | Multi-Pass Investigation | Context Retention | Hypothesis Testing |
|----------|----------------------|-----------------|------------------------|-------------------------|-------------------|-------------------|
| **Scoop Analytics** | ✓✓✓ | ✓✓✓ | ✓✓✓ | **✓✓✓** | **✓✓✓** | **✓✓✓** |
| Domo | ✓✓ | ✓✓ | ✓ | ✗ | ✗ | ✗ |
| ThoughtSpot | ✓✓ | ✓✓ | ✓ | ✗ | ✗ | ✗ |
| Qlik | ✓ | ✓✓ | **✓✓✓** | ✗ | ✗ | ✗ |
| Zenlytic | ✓✓ | ✓✓ | ✓ | ✗ | ✗ | ✗ |
| Tableau Pulse | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ |
| Power BI Copilot | ✓✓ | ✗ | ✓ | ✗ | ✗ | ✗ |
| Sisense | ✓✓ | ✓✓ | ✓ | ✗ | ✗ | ✗ |
| Snowflake Cortex | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| DataGPT | ✓✓ | ✓✓ | ✓ | ✗ | ✗ | ✗ |
| Tellius | ✓✓ | ✓✓ | ✓ | ✗ | ✗ | ✗ |
| DataChat | ✓✓ | ✓✓ | ✓ | ✗ | ✗ | ✗ |

**Capability Definitions**:

- **Natural Language Query**: Can ask questions in plain English
  - ✓✓✓: Handles typos, context, complex questions (Scoop)
  - ✓✓: Good NL but requires exact syntax (most platforms)
  - ✓: Basic NL with limitations (Qlik "one typo = failure", Cortex 35% success rate)

- **Multi-Turn Chat**: Can handle follow-up questions
  - ✓✓✓: Full conversational context (Scoop)
  - ✓✓: Follow-ups within session (most AI platforms)
  - ✓: Limited follow-up capability
  - ✗: "One question at a time" (Power BI Copilot per Microsoft docs)

- **Interactive Exploration**: User can manually explore data relationships
  - ✓✓✓: Associative model - click through data relationships (Qlik unique strength)
  - ✓✓✓: Full exploration with AI guidance (Scoop)
  - ✓: Basic drill-down/filtering
  - ✗: Static dashboards only

- **Multi-Pass Investigation**: AI autonomously runs 3-10 queries to find root causes
  - **✓✓✓: Automatic investigation planning with probe dependencies (SCOOP ONLY)**
  - ✗: No autonomous multi-pass investigation (all competitors - even Qlik's exploration is user-driven clicks, not AI planning)

- **Context Retention**: System remembers insights across queries within investigation
  - **✓✓✓: Full investigation memory with probe extraction rules (SCOOP ONLY)**
  - ✗: Stateless - each query is independent

- **Hypothesis Testing**: AI automatically tests theories and builds evidence
  - **✓✓✓: Automatic hypothesis generation and testing (SCOOP ONLY)**
  - ✗: User must manually test hypotheses

**Evidence**:
- **Scoop Multi-Pass**: Powered by **Investigation Coordinator** (15-module state machine). Executes deterministic "Display-Diagnose-Decide" workflow. Framework score: 8/8 Investigation (ONLY platform with full score)
- **Qlik Interactive Exploration**: Associative model ✓✓✓ for user-guided clicks, but Multi-Pass Investigation = ✗ because "User must manually explore" (framework_scoring.md: 4/8 Investigation from manual exploration, NOT autonomous investigation)
- **Power BI Copilot**: Microsoft docs: "One question at a time", "Can't currently answer questions that require generating new insights" (framework_scoring.md: 2/8 Investigation)
- **Snowflake Cortex**: Error "Actual statement count 3 did not match desired statement count 1" - cannot multi-step (framework_scoring.md: 2/8 Investigation)
- **All Others**: Single query architecture, no investigation planning (framework_scoring.md: ALL score 2/8 Investigation - none have multi-pass)

---

## Machine Learning

Measures explainable ML capabilities accessible to business users without data science expertise.

| Platform | Explainable ML Models | Automatic Data Prep | AI Explanation Layer | ML Discovery | ML Types Available |
|----------|---------------------|---------------------|---------------------|--------------|-------------------|
| **Scoop Analytics** | **✓✓✓** | **✓✓✓** | **✓✓✓** | **✓✓✓** | ✓✓✓ |
| Domo | ✓✓ | ✗ | ✓✓ | ✗ | ✓✓ |
| ThoughtSpot | ✓✓ | ✗ | ✓✓ | ✗ | ✓✓ |
| Qlik | ✗ | ✗ | ✗ | ✗ | ✓ |
| Zenlytic | ✓✓ | ✗ | ✗ | ✗ | ✓✓ |
| Tableau Pulse | ✓✓ | ✗ | ✓✓ | ✗ | ✓✓ |
| Power BI Copilot | ✗ | ✗ | ✗ | ✗ | ✗ |
| Sisense | ✗ | ✗ | ✗ | ✗ | ✓ |
| Snowflake Cortex | ✗ | ✗ | ✗ | ✗ | ✗ |
| DataGPT | ✗ | ✗ | ✗ | ✗ | ✗ |
| Tellius | ✓✓ | ✗ | ✗ | ✗ | ✓✓ |
| DataChat | ✗ | ✗ | ✗ | ✗ | ✗ |

**Capability Definitions**:

- **Explainable ML Models**: Decision trees, rule mining, or interpretable models (not black boxes)
  - **✓✓✓: J48 decision trees, JRip rules, EM clustering - fully explainable (SCOOP ONLY)**
  - ✓✓: Some explainable models but not accessible to business users (Domo, ThoughtSpot, Tableau, Zenlytic, Tellius)
  - ✓: Basic ML tools requiring data science expertise (Qlik AutoML, Sisense)
  - ✗: No explainable ML or only statistical functions

- **Automatic Data Prep**: AI handles cleaning, binning, feature engineering for ML
  - **✓✓✓: Fully automatic - user asks question, AI preps data (SCOOP ONLY)**
  - ✗: User must prepare data before ML can run

- **AI Explanation Layer**: Translates ML model output into business language
  - **✓✓✓: Analyzes J48/JRip output, converts to business insights with recommendations (SCOOP ONLY)**
  - ✓✓: Provides some business context for ML results (Domo, ThoughtSpot, Tableau)
  - ✗: Raw model output or no ML

- **ML Discovery**: ML runs automatically when user asks "why" questions
  - **✓✓✓: Classification system auto-triggers ML_RELATIONSHIP, ML_CLUSTER, ML_PERIOD, ML_GROUP (SCOOP ONLY)**
  - ✗: User must explicitly request ML analysis

- **ML Types Available**: Clustering, prediction, classification, etc.
  - ✓✓✓: Full suite - relationship analysis, clustering, period comparison, group comparison
  - ✓✓: Multiple ML types but limited accessibility
  - ✓: Basic ML tools
  - ✗: No ML or only statistics

**Evidence**:
- **Scoop**: **Encoded Expertise Engine**. Schema v2.8 captures domain logic (e.g., `definitions.json`) which Layer 2 (J48/JRip) uses to explain anomalies.
- **Scoop**: framework_scoring.md - 6/6 Deep ML Understanding (only platform with full score)
- **Domo/ThoughtSpot/Tableau/Zenlytic/Tellius**: framework_scoring.md - 4/6 ML scores (have ML but not fully accessible)
- **Qlik**: "No-code but requires understanding of ML concepts", "Still requires data science understanding" (framework_scoring.md: 0/6)
- **Power BI/Snowflake/DataGPT/DataChat**: framework_scoring.md - 0/6 ML scores (no ML capabilities)
- **Snowflake Cortex**: "Has CORR(), STDDEV() - correlation not causation. No J48, JRip, or clustering" (framework_scoring.md)

---

## Data Transformation

Measures ability to transform and prepare data for analysis using business-user-friendly methods.

| Platform | Spreadsheet Calculation Engine | Excel Formula Support | Data Prep Interface | Calculated Fields |
|----------|-------------------------------|---------------------|--------------------| -----------------|
| **Scoop Analytics** | **✓✓✓** | **✓✓✓** | ✓✓✓ | ✓✓✓ |
| Domo | ✗ | ✗ | ✓✓ | ✓✓ |
| ThoughtSpot | ✗ | ✗ | ✓ | ✓✓ |
| Qlik | ✗ | ✗ | ✓ | ✓✓ |
| Zenlytic | ✗ | ✗ | ✓ | ✓ |
| Tableau Pulse | ✗ | ✗ | ✓✓ | ✓✓ |
| Power BI Copilot | ✗ | ✗ | ✓✓ | ✓✓ |
| Sisense | ✗ | ✗ | ✓ | ✓✓ |
| Snowflake Cortex | ✗ | ✗ | ✓ | ✓ |
| DataGPT | ✗ | ✗ | ✓ | ✓ |
| Tellius | ✗ | ✗ | ✓ | ✓✓ |
| DataChat | ✗ | ✗ | ✓✓ | ✓✓ |

**Capability Definitions**:

- **Spreadsheet Calculation Engine**: Runtime execution of spreadsheet formulas on query results
  - **✓✓✓: 150+ Excel functions executed in-memory on data (SCOOP ONLY - UNIQUE)**
  - ✗: No runtime spreadsheet engine (all competitors)

- **Excel Formula Support**: Can use familiar Excel formulas for transformations
  - **✓✓✓: VLOOKUP, SUMIFS, nested IFs, FILTER, UNIQUE, etc. - full Excel syntax (SCOOP ONLY)**
  - ✗: Cannot use Excel formulas (must learn platform-specific syntax)

- **Data Prep Interface**: How users prepare and transform data
  - ✓✓✓: Natural language + spreadsheet functions (Scoop)
  - ✓✓: Visual data prep tools (Domo, Tableau, Power BI, DataChat)
  - ✓: Basic transformations or SQL required

- **Calculated Fields**: Can create derived metrics and dimensions
  - ✓✓✓: Excel formula syntax, natural language (Scoop)
  - ✓✓: Platform-specific formula language (most platforms)
  - ✓: Limited calculated field support

**Evidence**:
- **Scoop**: SCOOP_CAPABILITIES.md "Complete in-memory spreadsheet calculation engine with 150+ Excel functions"
- **Scoop**: "ScoopExpression Grammar - VLOOKUP, SUMIFS, nested IFs, FILTER, UNIQUE, etc."
- **Qlik**: "Cannot export Qlik formulas as Excel formulas", "Exports static data to Excel files, no formula conversion" (framework_scoring.md)
- **All Others**: No spreadsheet calculation engine documented - must use platform-specific formula languages

---

## Output & Distribution

Measures how easily users can create and distribute insights.

| Platform | Visualization Quality | PowerPoint Generation | Excel Export | Slack/Teams | Mobile | Presentation Builder | Brand Control |
|----------|---------------------|---------------------|--------------|-------------|--------|---------------------|---------------|
| **Scoop Analytics** | ✓✓✓ | ✓✓✓ | ✓✓✓ | ✓✓✓ | ✓✓✓ | ✓✓✓ | ✓✓✓ |
| Domo | ✓✓✓ | ✗ | ✓✓ | ✓ | ✓✓ | ✗ | ✗ |
| ThoughtSpot | ✓✓✓ | ✗ | ✓✓ | ✓ | ✓✓ | ✗ | ✗ |
| Qlik | ✓✓✓ | ✗ | ✓ | ✓ | ✓ | ✗ | ✗ |
| Zenlytic | ✓✓ | ✗ | ✓✓ | ✓ | ✓✓ | ✗ | ✗ |
| Tableau Pulse | ✓✓✓ | ✗ | ✓✓ | ✓✓ | ✓✓ | ✗ | ✗ |
| Power BI Copilot | ✓✓✓ | ✗ | ✓✓ | ✓ | ✓✓ | ✗ | ✗ |
| Sisense | ✓✓✓ | ✗ | ✓✓ | ✓ | ✓✓ | ✗ | ✗ |
| Snowflake Cortex | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ |
| DataGPT | ✓✓ | ✗ | ✓✓ | ✗ | ✓✓ | ✗ | ✗ |
| Tellius | ✓✓✓ | ✗ | ✓✓ | ✓ | ✓✓ | ✗ | ✗ |
| DataChat | ✓✓ | ✗ | ✓✓ | ✗ | ✓✓ | ✗ | ✗ |

**Capability Definitions**:

- **PowerPoint Generation**: Can create presentation decks automatically
  - **✓✓✓: AI generates full presentation with branded slides (SCOOP ONLY)**
  - ✗: No PowerPoint generation (all competitors - must manually screenshot)

- **Excel Export**: Can export data and analysis to Excel
  - ✓✓✓: Live formulas and calculations (Scoop)
  - ✓✓: Static data export with formatting
  - ✓: Basic CSV/Excel export

- **Slack/Teams Integration**: Can work natively in chat platforms
  - ✓✓✓: Full bidirectional Slack chat - upload files, ask questions, get full analysis (Scoop only)
  - ✓✓: Native integration with alerts/digests (Tableau Pulse)
  - ✓: One-way notifications or chart sharing (ThoughtSpot, Domo, Qlik, most others)
  - ✗: No Slack integration (Snowflake Cortex, DataGPT, DataChat) or Teams-only (Power BI)

- **Brand Control**: AI understands and applies company branding
  - **✓✓✓: Automatic logo detection and brand application (SCOOP ONLY)**
  - ✗: No brand intelligence (all competitors)

**Evidence**:
- **Scoop PowerPoint**: SCOOP_CAPABILITIES.md "Visual Intelligence System - AI-powered presentation generation with brand detection"
- **Scoop Brand Control**: "AI detects company branding from uploaded materials and applies automatically"
- **Scoop Slack**: LLM Prompts.txt "Slack Chat" - full bidirectional analysis with file upload
- **Qlik PowerPoint**: "No direct PowerPoint generation found" (framework_scoring.md)
- **Qlik Slack**: "Send chart image to Slack only - requires automation setup" (framework_scoring.md)
- **ThoughtSpot Slack**: "One-way push only (not bidirectional)" (framework_scoring.md)
- **Tableau Pulse Slack**: "Native integration with digests and alerts" but read-only (framework_scoring.md)
- **Power BI Slack**: "Not supported (Teams only)" (framework_scoring.md)
- **Snowflake Cortex**: "No Excel, PowerPoint, or mobile support", Slack requires custom development (framework_scoring.md: 0/8 Native Integration)
- **DataGPT/DataChat Slack**: "No Slack integration found" (framework_scoring.md)
- **All Others PowerPoint**: framework_scoring.md scores show 0/6 for Distribution (no PowerPoint automation)

---

## Platform Infrastructure

Measures data connectivity, schema flexibility, and performance.

| Platform | Multi-Source Connectivity | Schema Evolution Handling | Performance | Cloud/On-Premise |
|----------|--------------------------|--------------------------|-------------|------------------|
| **Scoop Analytics** | ✓✓✓ | ✓✓✓ | ✓✓✓ | ✓✓✓ |
| Domo | ✓✓✓ | ✓✓ | ✓✓✓ | ✓✓✓ |
| ThoughtSpot | ✓✓✓ | ✓✓ | ✓✓✓ | ✓✓✓ |
| Qlik | ✓✓✓ | ✗ | ✓ | ✓✓✓ |
| Zenlytic | ✓✓ | ✗ | ✓✓ | ✓✓✓ |
| Tableau Pulse | ✓✓✓ | ✗ | ✓✓✓ | ✓✓✓ |
| Power BI Copilot | ✓✓✓ | ✓ | ✓✓✓ | ✓✓✓ |
| Sisense | ✓✓✓ | ✓ | ✓✓✓ | ✓✓✓ |
| Snowflake Cortex | ✓✓✓ | ✗ | ✓✓✓ | ✓✓✓ |
| DataGPT | ✓✓ | ✓✓ | ✓✓ | ✓✓✓ |
| Tellius | ✓✓✓ | ✓ | ✓✓✓ | ✓✓✓ |
| DataChat | ✓✓ | ✓✓ | ✓✓ | ✓✓✓ |

**Capability Definitions**:

- **Schema Evolution Handling**: System adapts when database schema changes
  - ✓✓✓: Automatic adaptation, no maintenance (Scoop - no semantic layer to break)
  - ✓✓: Guided updates with user decisions
  - ✓: Requires manual updates
  - ✗: Semantic layer breaks on schema changes (Cortex, Zenlytic, Tableau Pulse, Qlik)

- **Performance**: Query speed and system responsiveness
  - ✓✓✓: Instant to seconds for most queries
  - ✓✓: Generally fast with occasional slowness
  - ✓: Frequent performance issues
  - Example: Qlik scores ✓ due to "hour-long dashboard loads" documented

**Evidence**:
- **Schema Evolution - Competitors**: Tableau Pulse "400 errors when schema changed" (framework_scoring.md: 0/8 Schema Evolution)
- **Schema Evolution - Cortex**: "YAML semantic model breaks on column renames" (framework_scoring.md: 0/8)
- **Qlik Performance**: "Sheets and dashboards taking up to an hour to load", "55-second API timeout" (framework_scoring.md)

---

## Summary: The Domain Intelligence Advantage

**The Category Shift: Domain Intelligence Platform**
Traditional vendors are either **Platforms** (Snowflake/PowerBI - generic, unopinionated) or **Applications** (Point solutions - rigid, narrow). Scoop is the first **Domain Intelligence Platform**—an analytical application platform that encodes expert logic into a flexible schema.

**Scoop-Only Capabilities (Architectural Moats)**:

1.  **Domain Intelligence Engine** (8/8 Investigation score)
    *   **Architecture**: 15-module recursive state machine (Investigation Coordinator)
    *   **Mechanism**: Deterministic "Display-Diagnose-Decide" workflow
    *   **Result**: Autonomous 3-10 query investigation with context retention

2.  **Encoded Expertise Schema** (6/6 ML score)
    *   **Architecture**: Schema v2.8 (Hierarchical JSON)
    *   **Mechanism**: Virtual Metric Layer (`definitions.json`) that adapts to schema changes
    *   **Result**: Business logic survives data changes (Schema Evolution)

3.  **Spreadsheet Calculation Engine** (150+ Excel functions)
    *   **Architecture**: In-memory formula execution on live query results
    *   **Mechanism**: Native support for VLOOKUP, SUMIFS, FILTER
    *   **Result**: Zero retraining for business users

4.  **3-Layer AI Data Scientist**
    *   **Layer 1**: Automatic Data Prep (Cleaning/Binning)
    *   **Layer 2**: Real ML Execution (J48 Trees, JRip Rules, EM Clustering)
    *   **Layer 3**: Business Translation (Narrative Generation)

5.  **Visual Intelligence System**
    *   **Mechanism**: Brand detection & semantic color mapping
    *   **Output**: Executive-ready PowerPoint in 30 seconds

**Competitor Unique Strengths**:

- **Qlik**: Associative data model for interactive exploration (4/8 Investigation via manual clicks)
- **Snowflake Cortex**: Deep Snowflake ecosystem integration
- **Power BI**: Microsoft ecosystem integration
- **Tableau**: Best-in-class visualization library
- **ThoughtSpot**: Enterprise search-first interface

---

## Evidence Sources

### Framework Scoring Files
All BUA scores sourced from `competitors/*/evidence/framework_scoring.md`:
- Understanding dimension rescored September 30, 2025
- Investigation, ML, and Explanation component scores
- Evidence quotes from product documentation and testing

### Scoop Capabilities
Primary source: `SCOOP_CAPABILITIES.md` and `framework/DOMAIN_INTELLIGENCE_FRAMEWORK.md`
- Spreadsheet engine: Lines 20-71 (150+ Excel functions)
- AI Data Scientist engine: Lines 74-153 (3-layer architecture)
- Investigation Coordinator: `scoop/development/domain-intelligence/investigation-coordinator/`
- Schema v2.8: `scoop/development/domain-intelligence/SCHEMA.md`

### Competitor Documentation
- Official vendor documentation
- Product testing results (Snowflake Cortex test suite)
- Customer reviews and feedback
- Vendor-published limitations (Power BI "one question at a time")

### Last Verification Date
- Matrix structure: November 18, 2025 (Domain Intelligence Update)
- Competitor scores: September 30, 2025 (Understanding dimension rescoring)
- Evidence links: November 18, 2025

---

## Version History

**v2.1** - November 18, 2025
- **Strategic Pivot**: Updated definitions to reflect "Domain Intelligence Platform" positioning.
- **Technical Specificity**: Added references to Investigation Coordinator and Schema v2.8.
- **Category Definition**: Defined "Analytical Application Platform" layer.

**v2.0** - September 30, 2025
- Complete restructure based on Understanding dimension rescoring
- Added Agentic Investigation columns (Multi-Pass, Context Retention, Hypothesis Testing)
- Split ML into 5 specific capabilities (Explainable, Auto Prep, AI Explanation, Discovery, Types)
- Added Spreadsheet Engine as distinct capability
- Added Business User Autonomy columns (No Data Modeling, No Training, No IT Setup)
- Increased from ~17 to 26 capability columns
- Evidence-based scoring with framework_scoring.md alignment

**v1.0** - Pre-September 2025
- Original capability matrix with generic Investigation and ML columns

---

## Implementation Notes

**For Web Display**:
- Consider grouping columns visually (Setup | Investigation | ML | Output | Infrastructure)
- Use color coding: Green (✓✓✓), Medium Green (✓✓), Yellow (✓), Red (✗), Gray (⚬⚬⚬)
- Add hover tooltips with capability definitions
- Highlight Scoop-only capabilities (5 unique competitive advantages)
- Consider 45° angled headers instead of 90° vertical for readability

**For Updates**:
- Verify against `framework_scoring.md` files (authoritative source)
- Document evidence sources for any score changes
- Update "Last Updated" date at top
- Cross-reference with BUA framework scores to ensure alignment

**For Sales Use**:
- Focus on Scoop-Only Capabilities section
- Use "18-point gap" in Investigation (8/8 vs 2/8) as proof point
- Use "6/6 only platform" for ML as differentiator
- Emphasize architectural differences (not just feature count)
