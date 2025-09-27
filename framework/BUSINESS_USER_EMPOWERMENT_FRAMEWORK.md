# Business User Autonomy Framework

**Version**: 2.0
**Date**: September 27, 2025
**Status**: Active Framework
**Subtitle**: Measuring Independent Analytics Capability for Non-Technical Business Users

---

## A New Category in Analytics

### Gartner's Four Primary Use Cases

Gartner's Critical Capabilities for Analytics and Business Intelligence Platforms evaluate vendors across four primary use cases:

1. **Centralized BI Provisioning** - IT/BI team builds and maintains all reports, dashboards, and data models
2. **Decentralized Analytics** - Business units/domain experts have self-service tools (but require data skills)
3. **Governed Data Discovery** - Balance between end-user empowerment and centralized governance
4. **OEM/Embedded BI** - Analytics embedded within other applications

**These categories focus on different organizational models for delivering analytics through IT departments, data teams, or business analysts.**

### The Missing Fifth Category: Business User Autonomy

**What Gartner's categories assume:**
- Users have data skills (SQL, DAX, data modeling) OR
- IT sets up semantic models/data infrastructure OR
- Business analysts act as intermediaries OR
- Weeks/months of implementation time

**What they don't measure:**
- Can a **non-technical business user** (marketing manager, sales VP, finance director) operate **completely independently**?
- Zero IT setup, zero analyst involvement, zero data engineering support
- Natural language only, no SQL/DAX/Python
- Minutes to productivity, not weeks

**Business User Autonomy is a fundamentally different architecture** - not "better" or "worse" than traditional BI, but optimized for different users and different needs.

### Architectural Comparison

| Dimension | Traditional BI (Gartner's Categories) | Business User Autonomy (5th Category) |
|-----------|---------------------------------------|--------------------------------------|
| **Primary User** | Data analysts, business analysts, BI developers | Non-technical business users |
| **Skills Required** | SQL, DAX, data modeling, or technical training | Natural language, Excel skills only |
| **IT Involvement** | IT sets up infrastructure, semantic models, governance | Zero - user connects data and operates alone |
| **Setup Time** | Weeks/months (implementation projects) | Minutes (30-second installation) |
| **Semantic Models** | Required, IT-maintained, breaks on data changes | Not required, automatic schema evolution |
| **Investigation Depth** | User asks question, analyst investigates why | User investigates themselves (multi-pass AI) |
| **Output Creation** | User exports data, designer creates presentations | User creates board-ready presentations instantly |
| **Governance Model** | Centralized control, IT-managed access | Self-service with optional governance |
| **Target Org** | Enterprises with BI teams and data infrastructure | Organizations where business speed > centralized control |

### This Framework's Purpose

**This framework measures Business User Autonomy** - the fifth category that Gartner's existing use cases don't capture.

Traditional BI platforms (Power BI, Tableau, Qlik, Looker) will score LOW on this framework **by design** - they optimize for governance, scalability, and enterprise IT control, not business user independence. That's a valid architectural choice with different trade-offs.

Platforms designed for Business User Autonomy will score HIGH - they optimize for independence, speed, and self-sufficiency, with different governance and scalability trade-offs.

**This is not about "better" or "worse" - it's about measuring a different category.**

### What This Framework Does NOT Measure

This framework intentionally does not evaluate capabilities that traditional BI platforms excel at:

**Enterprise Governance & Control:**
- Centralized data governance frameworks
- Role-based access control at scale (1000+ users)
- Audit trails and compliance reporting
- IT oversight and approval workflows
- Certified datasets and metrics definitions

**Enterprise IT Features:**
- Multi-tenant architecture at massive scale
- Enterprise authentication (SAML, AD integration)
- Data lineage and impact analysis
- Master data management integration
- IT service management integration

**Traditional BI Strengths:**
- Complex, governed semantic models
- Pixel-perfect operational reporting
- Scheduled report distribution at enterprise scale
- Deep integration with on-premise data warehouses
- Professional services for enterprise implementations

**Why these aren't measured**: These capabilities require IT departments and centralized control - the opposite of business user autonomy. Organizations that prioritize these features should choose traditional BI platforms.

**When Traditional BI Makes Sense:**
- Enterprise with dedicated BI/data team
- Governance and compliance are primary concerns
- Standardized metrics definitions required
- Centralized control valued over speed
- IT wants oversight of all analytics

**When Business User Autonomy Makes Sense:**
- No BI team or BI team is overloaded
- Business users need ad-hoc investigation
- Speed to insight matters more than governance
- Questions change faster than IT can respond
- Business user independence valued over centralized control

---

## Framework Core Question

Can a non-technical business user independently:
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

### Detailed Scoring Rubric

#### Component A: Self-Service Setup (0-4 points)
*Can user install/configure themselves without IT project?*

| Points | Capability |
|--------|------------|
| **0** | Requires IT implementation project (weeks/months), multiple teams involved |
| **1** | IT setup required, but faster (1-2 weeks), limited configuration |
| **2** | Some self-service possible but IT needed for key steps (2-3 days) |
| **3** | Mostly self-service, minor IT help for connections (few hours) |
| **4** | Complete self-service setup in minutes, zero IT involvement |

**What to evaluate**:
- Installation process (click vs IT project)
- Data source connections (self-serve vs IT ticket)
- User provisioning (self-signup vs IT approval)
- Time from signup to connected

#### Component B: Question Independence (0-3 points)
*Can user ask ad-hoc questions without analyst queue?*

| Points | Capability |
|--------|------------|
| **0** | All questions require analyst ticket, view-only access |
| **1** | Can ask questions within pre-built dashboards only (drill-downs) |
| **2** | Can ask new questions but limited to pre-defined metrics/dimensions |
| **3** | Complete question freedom, natural language, no constraints |

**What to evaluate**:
- Natural language support (conversational vs SQL/DAX)
- Query flexibility (any question vs pre-defined)
- Response time (instant vs analyst queue)
- No ticket system required

#### Component C: Speed to Value (0-3 points)
*How fast from signup to first meaningful insight?*

| Points | Capability |
|--------|------------|
| **0** | Months (implementation project, semantic model building) |
| **1** | Weeks (setup, training, configuration) |
| **2** | Days (connect data, learn interface) |
| **3** | Minutes (30 seconds to first insight, immediate productivity) |

**What to evaluate**:
- First insight time (measure actual time)
- Training required (none vs days of classes)
- Onboarding complexity (one step vs many)

**Total Autonomy Score**: Sum of A + B + C (max 10 points)

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

### Detailed Scoring Rubric

#### Component A: Native Integration (0-4 points)
*Does it work WHERE users already work?*

| Points | Capability |
|--------|------------|
| **0** | Separate portal only, must login and navigate BI tool |
| **1** | Portal-based with basic embedding (iframes, limited functionality) |
| **2** | One native integration (Slack notifications OR basic Excel export) |
| **3** | Native in one tool with full functionality (Slack OR Excel with analysis) |
| **4** | Native in multiple tools (Slack + Excel/Sheets + Mobile + PowerPoint) |

**What to evaluate**:
- Slack: Notifications only vs full analysis in threads
- Excel/Sheets: Export only vs live plugin with refresh
- Mobile: Responsive web vs native mobile experience
- PowerPoint: Manual copy/paste vs automated generation
- Setup time (weeks of custom dev vs 30 seconds)

#### Component B: No Portal Prison (0-3 points)
*Can users avoid logging into separate BI tool?*

| Points | Capability |
|--------|------------|
| **0** | Portal required for all analysis, separate login, tool navigation |
| **1** | Portal optional for simple tasks, but complex analysis requires portal |
| **2** | Most tasks possible outside portal but some features portal-only |
| **3** | Zero portal requirement, complete analysis in user's workflow tools |

**What to evaluate**:
- Can ask questions without opening BI tool?
- Can create presentations without portal?
- Can share insights without portal access?
- Login friction (separate auth vs SSO vs no login)

#### Component C: Interface Simplicity (0-3 points)
*How easy is it to use?*

| Points | Capability |
|--------|------------|
| **0** | Technical query language required (SQL, DAX, Python) |
| **1** | Guided NL with templates, limited flexibility |
| **2** | Good NL but some tasks require technical knowledge |
| **3** | True conversational NL, zero technical knowledge required |

**What to evaluate**:
- Natural language quality (conversational vs keyword matching)
- Learning curve (minutes vs days/weeks of training)
- Error handling (helps user vs cryptic errors)
- Context retention (conversation vs isolated queries)

**Total Flow Score**: Sum of A + B + C (max 10 points)

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

### Detailed Scoring Rubric

#### Component A: Investigation Depth (0-4 points)
*How deep can users go to find WHY?*

| Points | Capability |
|--------|------------|
| **0** | Static dashboards only (shows WHAT happened, no investigation) |
| **1** | Single-query answers with basic drill-downs |
| **2** | User can ask follow-up questions but must know what to ask next |
| **3** | Multi-pass investigation but user must guide it (3-5 queries) |
| **4** | Automatic multi-pass investigation (3-10 queries), finds root cause autonomously |

**What to evaluate**:
- Query depth (one shot vs multi-pass)
- Context retention (remembers conversation vs starts over)
- Hypothesis testing (tests theories automatically vs user must ask)
- Root cause discovery (finds WHY vs just shows WHAT)
- Investigation examples: "Sales dropped 15% in Q3" → automatic investigation of segments, timing, causes

#### Component B: ML Pattern Discovery (0-3 points)
*Can users discover patterns they wouldn't find themselves?*

| Points | Capability |
|--------|------------|
| **0** | No ML capabilities, manual analysis only |
| **1** | Basic statistics (correlations, trends) marketed as "AI" |
| **2** | Real ML but black-box predictions (can't explain why) |
| **3** | Explainable ML with pattern discovery (J48 trees, EM clustering, rule mining) |

**What to evaluate**:
- ML sophistication (none vs real models: decision trees, clustering, rule mining)
- Pattern discovery (finds hidden segments, drivers, relationships)
- Accessibility (automatic vs requires data scientist)
- Examples: Customer segmentation, churn drivers, product affinity

#### Component C: Business-Language Explanation (0-3 points)
*Can users understand and explain insights to others?*

| Points | Capability |
|--------|------------|
| **0** | Raw data dumps, technical output, no explanation |
| **1** | Basic summaries but still technical (statistical jargon) |
| **2** | Good explanations but some technical knowledge helpful |
| **3** | Complete business-language translation, narratives with context, actionable recommendations |

**What to evaluate**:
- Explanation quality (technical vs business language)
- Narrative generation (just numbers vs story with context)
- Actionability (insights only vs recommendations with reasoning)
- Confidence/validation (explains how we know, not just what)
- User can explain to their boss without help

**Total Understanding Score**: Sum of A + B + C (max 10 points)

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

### Detailed Scoring Rubric

#### Component A: Visual Quality & Aesthetics (0-3 points)
*How professional do outputs look?*

| Points | Capability |
|--------|------------|
| **0** | Screenshot exports, unprofessional appearance |
| **1** | Basic charts with standard templates, generic look |
| **2** | Good visuals with customization options, professional but requires effort |
| **3** | Pixel-perfect output (1600x900), Gartner-quality professional aesthetics automatically |

**What to evaluate**:
- Chart quality (basic vs sophisticated)
- Layout/composition (auto vs manual)
- Color theory application (random vs semantic color mapping)
- Professional standards (acceptable vs boardroom-ready)

#### Component B: Brand Compliance & Automation (0-4 points)
*How well does it handle branding?*

| Points | Capability |
|--------|------------|
| **0** | No branding, generic output only |
| **1** | Manual brand color/logo application required |
| **2** | Template-based branding (user uploads, system applies) |
| **3** | Automatic brand detection from uploaded files (extracts colors) |
| **4** | AI-powered brand detection + semantic color application + live data overlay on branded templates |

**What to evaluate**:
- Brand detection (manual vs automatic from PowerPoint)
- Color consistency (user manages vs auto-applied throughout)
- Logo/template handling (separate upload vs integrated)
- Corporate compliance (hit-or-miss vs guaranteed)

#### Component C: Speed & Formats (0-3 points)
*How fast can users create shareable outputs?*

| Points | Capability |
|--------|------------|
| **0** | Manual work required (3-4 hours per deck) |
| **1** | Faster but still significant effort (1-2 hours) |
| **2** | Quick generation with some manual touchup (15-30 min) |
| **3** | Instant generation (under 60 seconds), multiple formats (PPT, Slides, PDF, live decks) |

**What to evaluate**:
- Time to board-ready deck (hours vs seconds)
- Output formats (one vs multiple: PowerPoint, Google Slides, PDF, live decks)
- Bi-directional flow (can import PPT, add data, re-export)
- Live updates (static vs live data refresh in presentations)

**Total Presentation Score**: Sum of A + B + C (max 10 points)

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

### Detailed Scoring Rubric

#### Component A: Data Connections (0-2 points)
*Can users connect to data sources themselves?*

| Points | Capability |
|--------|------------|
| **0** | Data engineer required for all connections, data warehouse setup needed |
| **1** | Some self-service connections but IT needed for enterprise sources |
| **2** | Complete self-service, connect to any source (databases, SaaS, files, APIs) |

**What to evaluate**:
- Connection setup (IT ticket vs self-serve)
- Source variety (limited vs comprehensive)
- Authentication handling (IT required vs user manages)
- Time to connect (days vs minutes)

#### Component B: Schema Evolution & Maintenance (0-4 points)
*What happens when data structure changes?*

| Points | Capability |
|--------|------------|
| **0** | System breaks completely, requires data engineer rebuild (weeks) |
| **1** | Breaks but faster recovery with IT help (days) |
| **2** | Some fields adapt but others break, IT needed (1-2 days) |
| **3** | Most changes handled automatically, rare IT involvement (hours) |
| **4** | Complete automatic adaptation, zero downtime, instant availability (minutes) |

**What to evaluate**:
- New column handling (breaks vs auto-detects)
- Renamed column handling (breaks vs auto-migrates)
- Type change handling (breaks vs adapts)
- Historical data preservation (lost vs maintained)
- Semantic model requirement (YAML files vs zero maintenance)
- Time to availability (weeks vs minutes)

#### Component C: Data Preparation & Transformation (0-2 points)
*Can users prep/clean data without SQL/Python?*

| Points | Capability |
|--------|------------|
| **0** | No data prep, must have clean data, or requires data engineer/SQL |
| **1** | Basic prep capabilities with GUI, limited functionality |
| **2** | In-memory spreadsheet engine (150+ Excel functions), sophisticated transformation |

**What to evaluate**:
- Prep method (SQL vs GUI vs spreadsheet functions)
- Function library (limited vs 150+ Excel functions: VLOOKUP, SUMIFS, etc.)
- Skills required (SQL/Python vs Excel familiarity)
- Combination/joins (manual vs spreadsheet-based)
- Messy data handling (requires clean data vs handles automatically)

#### Component D: Operationalization & Writeback (0-2 points)
*Can users push insights back to operational systems?*

| Points | Capability |
|--------|------------|
| **0** | View/export only, no writeback capability |
| **1** | Manual export to CSV, user must upload to other systems |
| **2** | Direct writeback to CRM/operational systems (Salesforce, HubSpot, etc.) |

**What to evaluate**:
- CRM writeback (can push ML scores/segments to Salesforce)
- API integrations for operationalization
- Automation of insights → action loop
- No manual copy/paste required

**Total Data Score**: Sum of A + B + C + D (max 10 points)

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

**Autonomy: 3/10**
- Setup (0/4): 14-week F64 implementation, semantic model required
- Question Independence (2/3): NL queries but limited semantic model
- Speed to Value (1/3): Weeks to first insight

**Flow: 4/10**
- Native Integration (1/4): Excel Copilot Pro separate $30/user subscription
- No Portal Prison (1/3): Requires Power BI tool for most tasks
- Interface Simplicity (2/3): Good NL but within semantic model constraints

**Understanding: 2/10**
- Investigation Depth (1/4): Single query only ("one question at a time" - Microsoft docs)
- ML Pattern Discovery (0/3): No ML capabilities
- Business Explanation (1/3): Basic summaries, nondeterministic outputs

**Presentation: 3/10**
- Visual Quality (1/3): Standard BI charts
- Brand Automation (1/4): Manual branding work required
- Speed & Formats (1/3): Manual PowerPoint workflow (hours)

**Data: 3/10**
- Connections (1/2): IT required for enterprise connections
- Schema Evolution (0/4): Semantic model breaks on changes, 14-day rebuild
- Data Prep (1/2): Requires DAX/Power Query (technical skills)
- Writeback (1/2): Export only, manual process to operationalize

### Scoop: 42/50 (Category A - True Self-Service)

**Autonomy: 9/10**
- Setup (4/4): 30-second Slack install, zero IT
- Question Independence (3/3): Full NL, any question
- Speed to Value (2/3): Minutes to first insight (improving to seconds)

**Flow: 9/10**
- Native Integration (4/4): Slack + Excel/Sheets + Mobile + PowerPoint
- No Portal Prison (3/3): Zero portal requirement
- Interface Simplicity (2/3): Conversational NL (improving context)

**Understanding: 9/10**
- Investigation Depth (4/4): Automatic multi-pass (3-10 queries), root cause
- ML Pattern Discovery (3/3): J48 (800+ nodes), EM clustering, explainable
- Business Explanation (2/3): Good narratives (improving actionability)

**Presentation: 8/10**
- Visual Quality (3/3): Pixel-perfect, Gartner-quality aesthetics
- Brand Automation (3/4): Auto brand detection (expanding live overlay)
- Speed & Formats (2/3): 30-second generation (expanding formats)

**Data: 7/10**
- Connections (2/2): Self-service, any source
- Schema Evolution (3/4): Automatic adaptation (continuous improvement)
- Data Prep (2/2): 150+ Excel functions, spreadsheet engine
- Writeback (0/2): Coming soon (Salesforce, HubSpot integration)

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

### Comparison to Old BUA

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

### In BUA Comparison Pages
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
- **Version 1.0**: Original BUA (Browse, Understand, Predict, Act, Fix) - 2024
  - Archived: `framework/archive/BUA_V1_ORIGINAL.md`
- **Version 2.0 (January 2025)**: Five dimensions (Independence, Analytical Depth, Workflow Integration, Business Communication, Visual Intelligence)
  - Archived: `framework/archive/BUSINESS_USER_POWER_FRAMEWORK_JAN2025.md`
- **Version 2.0 (September 2025)**: Business User Autonomy Framework - Five dimensions (Autonomy, Flow, Understanding, Presentation, Data)
  - Current active version
  - Added Gartner 5th category positioning
  - Detailed sub-component rubrics
  - Clear "What We Don't Measure" section

---

## Next Steps for Implementation

1. **Update BUA_COMPARISON_TEMPLATE.md** with new framework
2. **Re-score all competitors** using new rubrics
3. **Update existing battle cards** with new scores
4. **Generate new BUA comparison pages** for priority competitors:
   - Power BI Copilot
   - Tableau Pulse
   - ThoughtSpot
   - Domo
5. **Document scoring rationale** for each competitor in their evidence folders

---

**Framework Owner**: Competitive Intelligence Team
**Review Cadence**: Quarterly
**Last Updated**: September 27, 2025