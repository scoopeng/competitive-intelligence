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

**Total Score**: 100 points (5 dimensions × 20 points each)

---

## Dimension 1: Autonomy (20 points)

**What It Measures**: Can business users start and operate without IT involvement?

### Detailed Scoring Rubric

#### Component A: Self-Service Setup (0-8 points)
*Can user install/configure themselves without IT project?*

| Points | Capability |
|--------|------------|
| **0** | Requires IT implementation project (weeks/months), multiple teams involved |
| **2** | IT setup required, but faster (1-2 weeks), limited configuration |
| **4** | Some self-service possible but IT needed for key steps (2-3 days) |
| **6** | Mostly self-service, minor IT help for connections (few hours) |
| **8** | Complete self-service setup in minutes, zero IT involvement |

**What to evaluate**:
- Installation process (click vs IT project)
- Data source connections (self-serve vs IT ticket)
- User provisioning (self-signup vs IT approval)
- Time from signup to connected

#### Component B: Question Independence (0-6 points)
*Can user ask ad-hoc questions without analyst queue?*

| Points | Capability |
|--------|------------|
| **0** | All questions require analyst ticket, view-only access |
| **2** | Can ask questions within pre-built dashboards only (drill-downs) |
| **4** | Can ask new questions but limited to pre-defined metrics/dimensions |
| **6** | Complete question freedom, natural language, no constraints |

**What to evaluate**:
- Natural language support (conversational vs SQL/DAX)
- Query flexibility (any question vs pre-defined)
- Response time (instant vs analyst queue)
- No ticket system required

#### Component C: Speed to Value (0-6 points)
*How fast from signup to first meaningful insight?*

| Points | Capability |
|--------|------------|
| **0** | Months (implementation project, semantic model building) |
| **2** | Weeks (setup, training, configuration) |
| **4** | Days (connect data, learn interface) |
| **6** | Minutes (30 seconds to first insight, immediate productivity) |

**What to evaluate**:
- First insight time (measure actual time)
- Training required (none vs days of classes)
- Onboarding complexity (one step vs many)

**Total Autonomy Score**: Sum of A + B + C (max 20 points)

### Business Impact
- **High score (18-20)**: SMB owner or department head can start TODAY
- **Low score (0-8)**: Requires IT project, budgeting, implementation timeline

### Competitive Examples
- **Power BI Copilot**: 6/20 (14-week F64 setup + semantic model required)
- **Snowflake Cortex**: 4/20 (6-month implementation, data engineering required)
- **Scoop**: 18/20 (30-second Slack install, connect data sources, start asking)

---

## Dimension 2: Flow (20 points)

**What It Measures**: Can business users work in their existing tools vs switching to separate BI portal?

### Detailed Scoring Rubric

#### Component A: Native Integration (0-8 points)
*Does it work WHERE users already work?*

| Points | Capability |
|--------|------------|
| **0** | Separate portal only, must login and navigate BI tool |
| **2** | Portal-based with basic embedding (iframes, limited functionality) |
| **4** | One native integration (Slack notifications OR basic Excel export) |
| **6** | Native in one tool with full functionality (Slack OR Excel with analysis) |
| **8** | Native in multiple tools (Slack + Excel/Sheets + Mobile + PowerPoint) |

**What to evaluate**:
- Slack: Notifications only vs full analysis in threads
- Excel/Sheets: Export only vs live plugin with refresh
- Mobile: Responsive web vs native mobile experience
- PowerPoint: Manual copy/paste vs automated generation
- Setup time (weeks of custom dev vs 30 seconds)

#### Component B: No Portal Prison (0-6 points)
*Can users avoid logging into separate BI tool?*

| Points | Capability |
|--------|------------|
| **0** | Portal required for all analysis, separate login, tool navigation |
| **2** | Portal optional for simple tasks, but complex analysis requires portal |
| **4** | Most tasks possible outside portal but some features portal-only |
| **6** | Zero portal requirement, complete analysis in user's workflow tools |

**What to evaluate**:
- Can ask questions without opening BI tool?
- Can create presentations without portal?
- Can share insights without portal access?
- Login friction (separate auth vs SSO vs no login)

#### Component C: Interface Simplicity (0-6 points)
*How easy is it to use?*

| Points | Capability |
|--------|------------|
| **0** | Technical query language required (SQL, DAX, Python) |
| **2** | Guided NL with templates, limited flexibility |
| **4** | Good NL but some tasks require technical knowledge |
| **6** | True conversational NL, zero technical knowledge required |

**What to evaluate**:
- Natural language quality (conversational vs keyword matching)
- Learning curve (minutes vs days/weeks of training)
- Error handling (helps user vs cryptic errors)
- Context retention (conversation vs isolated queries)

**Total Flow Score**: Sum of A + B + C (max 20 points)

### Business Impact
- **High score (18-20)**: User works in familiar environment, no tool switching
- **Low score (0-8)**: Must learn new interface, separate from daily workflow

### Competitive Examples
- **Domo**: 2/20 (portal prison, no native integrations)
- **Power BI Copilot**: 8/20 (separate tool, limited Excel Copilot Pro for $30/user)
- **Scoop**: 18/20 (Slack native, mobile, Google Sheets plugin, PowerPoint integration)

---

## Dimension 3: Understanding (20 points)

**What It Measures**: Can business users get deep insights (root cause WHY) without data analyst?

**Core Concept**: "Understanding" means using deep ML to understand relationships and root causes - it's deeper than just poking at a problem. This includes broader agentic investigation with the ability to plan new rounds of probes (queries or ML).

### Detailed Scoring Rubric

#### Component A: Agentic Investigation Depth (0-8 points)
*Does the system autonomously investigate root causes through multiple rounds of interconnected analysis?*

| Points | Capability |
|--------|------------|
| **0** | Static dashboards only (shows WHAT happened, no investigation) |
| **2** | Single-query answers with basic drill-downs (user cannot investigate further) |
| **4** | User-guided multi-query (user CAN ask follow-ups but must know what to ask next) |
| **6** | Semi-autonomous investigation (system suggests next questions, user must approve each step) |
| **8** | Fully autonomous agentic investigation (automatic multi-round investigation with probe dependencies) |

**For 8 points, system must have**:
- **Automatic multi-round investigation** - 2-8+ interconnected probes without user prompting
- **Investigation planning** - System generates investigation strategy (drill-down, causal, temporal, comparative)
- **Probe dependencies** - Later probes extract values from earlier probe results
  - Example: Probe 1 finds "highest churn in month-to-month contracts"
  - Probe 2 automatically analyzes month-to-month segment deeper using value from Probe 1
  - Probe 3 compares to other contract types using findings from Probes 1 & 2
- **Multiple probe types** - Can plan mix of DATASET queries, ML_RELATIONSHIP, ML_GROUP, ML_PERIOD
- **Hypothesis testing** - Tests theories automatically without user guidance
- **Statistical validation** - Confidence intervals, significance testing
- **Synthesis** - Combines findings from all probes into coherent narrative

**Key distinction**: Does the AI autonomously investigate (planning ahead, probe dependencies), or does it just let users click around?

**What to evaluate**:
- Does system plan investigation strategy before executing?
- Can later queries use extracted values from earlier query results? (probe dependencies)
- Does system decide which probe type (query vs ML) based on investigation needs?
- Does system run multiple rounds if first round doesn't fully answer?
- Or does user drive every step manually?

#### Component B: Deep ML Understanding (0-6 points)
*Can the system discover patterns using ML and explain WHY patterns exist (not just predict)?*

| Points | Capability |
|--------|------------|
| **0** | No ML capabilities, manual analysis only |
| **2** | Basic statistics (correlations, trends) marketed as "AI" |
| **4** | Real ML but black-box predictions (cannot explain WHY) |
| **6** | Explainable ML with deep understanding (shows decision paths, business rules, segment definitions) |

**For 6 points, system must have**:
- **Real ML models with explainability**:
  - Decision Trees (showing decision paths, e.g., J48 with 800+ nodes)
  - Rule Mining (business logic extraction, e.g., JRip rules)
  - Clustering (segment definitions, e.g., EM clustering)
- **Pattern discovery** - Finds hidden segments, drivers, relationships users wouldn't find
- **Causal understanding** - Shows WHAT drives WHAT (not just correlation)
- **Business rules extraction** - "If X and Y, then Z with 85% confidence"
- **Accessible to business users** - Automatic execution, no data scientist required
- **Multiple ML types available**:
  - ML_RELATIONSHIP - What predicts/influences outcome
  - ML_CLUSTER - Natural groupings in data
  - ML_PERIOD - What changed between time periods (using ML)
  - ML_GROUP - How groups differ (using ML to explain differences)

**Key distinction**: Must explain WHY (decision paths, rules, segment definitions), not just make predictions.

**What to evaluate**:
- Can it show decision trees or rules (not just "prediction: 85% likely to churn")?
- Can business users understand WHY without data scientist?
- Uses real ML algorithms (decision trees, clustering) vs just regression/correlation?
- Can extract business-understandable rules from patterns?

#### Component C: Business-Language Explanation (0-6 points)
*Can users understand complex findings and explain them to executives?*

| Points | Capability |
|--------|------------|
| **0** | Raw technical output (SQL results, data dumps, statistical notation) |
| **2** | Basic summaries with technical jargon (p-values, R-squared, standard deviations) |
| **4** | Good explanations, some technical knowledge helpful (mostly business language) |
| **6** | Complete business-language translation (zero jargon, executive-ready narratives) |

**For 6 points, explanations must have**:
- **Zero technical jargon** - Pure business language, no statistical terms
- **Narratives with context** - Tells a story, not just numbers
- **Actionable recommendations** - Suggests what to do, with reasoning
- **Confidence explained** - "We know this because..." (not just "we found this")
- **Executive-ready** - User can present findings to C-level without help
- **Synthesizes across findings** - Combines multiple probe results into coherent story
- **Example transformation**:
  - Technical: "J48 tree node: if tenure < 12 AND contract = month-to-month then churn"
  - Business: "New customers on flexible contracts are at highest risk - they haven't invested enough time to commit long-term"

**Key distinction**: Boss test - Can user explain to their boss without any technical help?

**What to evaluate**:
- Does it use business language or statistical jargon?
- Does it explain WHY this matters, not just WHAT was found?
- Does it suggest what to DO about findings?
- Can a marketing manager present this to the CEO?

**Total Understanding Score**: Sum of A + B + C (max 20 points)

### The Agentic Investigation Test

**Question**: "Why did sales drop 15% in Q3?"

**Low Score (2-4 points)**:
- Tool returns: "Sales were $850K in Q3 vs $1M in Q2"
- User must then ask: "Which regions dropped?"
- User must then ask: "Why did West region drop?"
- User must then ask: "Which products in West region?"
- **Tool never drives the investigation**

**Medium Score (6 points)**:
- Tool suggests: "Would you like to see by region?"
- User clicks "Yes"
- Tool suggests: "West region dropped most. Drill into West?"
- User clicks "Yes"
- **Tool suggests but user must approve each step**

**High Score (8 points)**:
- Tool automatically executes investigation plan:
  - **Probe 1**: Identify regions with largest drops → finds "West: -40%"
  - **Probe 2**: Analyze West region (value extracted from Probe 1) by product
  - **Probe 3**: Compare West to other regions using ML_GROUP
  - **Probe 4**: Analyze timing - when did drop start in West?
  - **Probe 5**: ML_RELATIONSHIP - what factors predict drops in West?
  - **Synthesis**: "West region sales dropped 40% starting July 15th when your top sales rep left. The drop was concentrated in enterprise accounts (>$50K). ML analysis shows 'days since last contact' is now 3x higher in West than other regions. Recommend immediate territory reassignment."
- **System planned and executed entire investigation autonomously**

### Business Impact
- **High score (18-20)**: User finds root causes themselves, no analyst ticket required
- **Low score (0-8)**: User sees problem but needs analyst to investigate why

### Technical Depth (What Powers High Scores)

**For Investigation (8/8)**:
- Multi-round probe planning with dependencies
- Investigation strategies: drill-down, causal, temporal, comparative, pattern discovery
- Mix of probe types: DATASET, ML_RELATIONSHIP, ML_GROUP, ML_PERIOD, ML_CLUSTER
- Automatic hypothesis testing and synthesis
- Statistical validation across probes

**For ML Understanding (6/6)**:
- J48 Decision Trees (800+ node trees showing decision paths)
- EM Clustering (automatic segmentation with definitions)
- JRip Rule Mining (business rules extraction)
- Three-Layer AI: data prep → ML execution → business translation
- Multiple ML analysis types available

**For Business Explanation (6/6)**:
- Narrative generation from complex ML results
- Context and causal reasoning
- Actionable recommendations with confidence
- Executive-level synthesis

### Competitive Examples
- **Scoop**: 18/20 (Investigation: 8/8, ML: 6/6, Explanation: 4/6)
  - Full agentic investigation with probe dependencies
  - Explainable ML (J48, EM, JRip)
  - Business narratives (improving actionability)
- **Power BI Copilot**: 7/20 (Investigation: 2/8, ML: 0/6, Explanation: 5/6)
  - Single query only ("one question at a time" - Microsoft docs)
  - No ML capabilities
  - Basic summaries, nondeterministic
- **ThoughtSpot**: 8/20 (Investigation: 2/8, ML: 4/6, Explanation: 2/6)
  - Single query responses, user-driven
  - SpotIQ has real ML but black-box (can't explain WHY)
  - Shows correlations but not causal understanding
- **Qlik**: 6/20 (Investigation: 4/8, ML: 0/6, Explanation: 2/6)
  - Associative model = user manually clicks relationships
  - Qlik Predict exists but requires data scientist
  - No autonomous investigation or probe dependencies

---

## Dimension 4: Presentation (20 points)

**What It Measures**: Can business users create professional, branded visual outputs without designer?

### Detailed Scoring Rubric

#### Component A: Visual Quality & Aesthetics (0-6 points)
*How professional do outputs look?*

| Points | Capability |
|--------|------------|
| **0** | Screenshot exports, unprofessional appearance |
| **2** | Basic charts with standard templates, generic look |
| **4** | Good visuals with customization options, professional but requires effort |
| **6** | Pixel-perfect output (1600x900), Gartner-quality professional aesthetics automatically |

**What to evaluate**:
- Chart quality (basic vs sophisticated)
- Layout/composition (auto vs manual)
- Color theory application (random vs semantic color mapping)
- Professional standards (acceptable vs boardroom-ready)

#### Component B: Brand Compliance & Automation (0-8 points)
*How well does it handle branding?*

| Points | Capability |
|--------|------------|
| **0** | No branding, generic output only |
| **2** | Manual brand color/logo application required |
| **4** | Template-based branding (user uploads, system applies) |
| **6** | Automatic brand detection from uploaded files (extracts colors) |
| **8** | AI-powered brand detection + semantic color application + live data overlay on branded templates |

**What to evaluate**:
- Brand detection (manual vs automatic from PowerPoint)
- Color consistency (user manages vs auto-applied throughout)
- Logo/template handling (separate upload vs integrated)
- Corporate compliance (hit-or-miss vs guaranteed)

#### Component C: Speed & Formats (0-6 points)
*How fast can users create shareable outputs?*

| Points | Capability |
|--------|------------|
| **0** | Manual work required (3-4 hours per deck) |
| **2** | Faster but still significant effort (1-2 hours) |
| **4** | Quick generation with some manual touchup (15-30 min) |
| **6** | Instant generation (under 60 seconds), multiple formats (PPT, Slides, PDF, live decks) |

**What to evaluate**:
- Time to board-ready deck (hours vs seconds)
- Output formats (one vs multiple: PowerPoint, Google Slides, PDF, live decks)
- Bi-directional flow (can import PPT, add data, re-export)
- Live updates (static vs live data refresh in presentations)

**Total Presentation Score**: Sum of A + B + C (max 20 points)

### Business Impact
- **High score (18-20)**: User creates executive presentations themselves, no designer
- **Low score (0-8)**: User must export ugly charts, spend hours formatting, or request design help

### Technical Depth (What Powers Score 9-10)
- **Visual Intelligence System**:
  - Automatic brand detection (extract colors from existing templates)
  - AI color theory (semantic color mapping, accessibility compliance)
  - Canvas-based presentation system (1600x900 pixel-perfect)
  - Live data overlay (presentations update automatically)
  - Google Slides bi-directional sync

### Competitive Examples
- **Power BI**: 6/20 (basic chart exports, manual PowerPoint workflow)
- **Tableau**: 8/20 (better visuals but still manual presentation creation)
- **Scoop**: 18/20 (30-second branded deck generation with automatic brand detection)

---

## Dimension 5: Data (20 points)

**What It Measures**: Can business users handle all data operations without data engineer?

### Detailed Scoring Rubric

#### Component A: Data Connections (0-4 points)
*Can users connect to data sources themselves?*

| Points | Capability |
|--------|------------|
| **0** | Data engineer required for all connections, data warehouse setup needed |
| **2** | Some self-service connections but IT needed for enterprise sources |
| **4** | Complete self-service, connect to any source (databases, SaaS, files, APIs) |

**What to evaluate**:
- Connection setup (IT ticket vs self-serve)
- Source variety (limited vs comprehensive)
- Authentication handling (IT required vs user manages)
- Time to connect (days vs minutes)

#### Component B: Schema Evolution & Maintenance (0-8 points)
*What happens when data structure changes?*

| Points | Capability |
|--------|------------|
| **0** | System breaks completely, requires data engineer rebuild (weeks) |
| **2** | Breaks but faster recovery with IT help (days) |
| **4** | Some fields adapt but others break, IT needed (1-2 days) |
| **6** | Most changes handled automatically, rare IT involvement (hours) |
| **8** | Complete automatic adaptation, zero downtime, instant availability (minutes) |

**What to evaluate**:
- New column handling (breaks vs auto-detects)
- Renamed column handling (breaks vs auto-migrates)
- Type change handling (breaks vs adapts)
- Historical data preservation (lost vs maintained)
- Semantic model requirement (YAML files vs zero maintenance)
- Time to availability (weeks vs minutes)

#### Component C: Data Preparation & Transformation (0-4 points)
*Can users prep/clean data without SQL/Python?*

| Points | Capability |
|--------|------------|
| **0** | No data prep, must have clean data, or requires data engineer/SQL |
| **2** | Basic prep capabilities with GUI, limited functionality |
| **4** | In-memory spreadsheet engine (150+ Excel functions), sophisticated transformation |

**What to evaluate**:
- Prep method (SQL vs GUI vs spreadsheet functions)
- Function library (limited vs 150+ Excel functions: VLOOKUP, SUMIFS, etc.)
- Skills required (SQL/Python vs Excel familiarity)
- Combination/joins (manual vs spreadsheet-based)
- Messy data handling (requires clean data vs handles automatically)

#### Component D: Operationalization & Writeback (0-4 points)
*Can users push insights back to operational systems?*

| Points | Capability |
|--------|------------|
| **0** | View/export only, no writeback capability |
| **2** | Manual export to CSV, user must upload to other systems |
| **4** | Direct writeback to CRM/operational systems (Salesforce, HubSpot, etc.) |

**What to evaluate**:
- CRM writeback (can push ML scores/segments to Salesforce)
- API integrations for operationalization
- Automation of insights → action loop
- No manual copy/paste required

**Total Data Score**: Sum of A + B + C + D (max 20 points)

### Business Impact
- **High score (18-20)**: New CRM field available immediately, user can prep data themselves
- **Low score (0-8)**: Every data change = IT ticket, days/weeks waiting

### Technical Depth (What Powers Score 9-10)
- **Spreadsheet Calculation Engine**: 150+ Excel functions for data prep (VLOOKUP, SUMIFS, etc.)
- **Schema Evolution**: Automatic detection and adaptation to data structure changes
- **Direct connections**: Connect to any data source without data warehouse
- **Writeback capabilities**: Update CRM/operational systems with ML scores
- **Smart Scanner**: Handles messy, unstructured data automatically

### Competitive Examples
- **Power BI Copilot**: 6/20 (semantic model breaks on changes, 14-day rebuild, requires data engineer)
- **Tableau**: 8/20 (better than Power BI but still requires data modeling, breaks on changes)
- **Scoop**: 14/20 (schema evolution, spreadsheet engine, but writeback expanding)

---

## Category Classification

**Total Score** (sum of 5 dimensions, max 100 points):

| Score Range | Category | Description |
|-------------|----------|-------------|
| **85-100** | **A+ Elite** | Exceptional business user autonomy across all dimensions |
| **70-84** | **A Strong** | Strong business user empowerment with minor gaps |
| **55-69** | **B Good** | Good for analysts, some business user capability |
| **40-54** | **C Moderate** | Moderate capability, requires IT/analyst involvement |
| **25-39** | **D Weak** | Weak self-service, mostly IT-dependent platform |
| **0-24** | **F Poor** | Poor autonomy, static views, minimal capability |

---

## Competitor Scoring Examples

### Power BI Copilot: 32/100 (Category D - Weak)

**Autonomy: 6/20**
- Setup (0/8): 14-week F64 implementation, semantic model required
- Question Independence (4/6): NL queries but limited semantic model
- Speed to Value (2/6): Weeks to first insight

**Flow: 8/20**
- Native Integration (2/8): Excel Copilot Pro separate $30/user subscription
- No Portal Prison (2/6): Requires Power BI tool for most tasks
- Interface Simplicity (4/6): Good NL but within semantic model constraints

**Understanding: 4/20**
- Investigation Depth (2/8): Single query only ("one question at a time" - Microsoft docs)
- ML Pattern Discovery (0/6): No ML capabilities
- Business Explanation (2/6): Basic summaries, nondeterministic outputs

**Presentation: 6/20**
- Visual Quality (2/6): Standard BI charts
- Brand Automation (2/8): Manual branding work required
- Speed & Formats (2/6): Manual PowerPoint workflow (hours)

**Data: 8/20**
- Connections (2/4): IT required for enterprise connections
- Schema Evolution (0/8): Semantic model breaks on changes, 14-day rebuild
- Data Prep (2/4): Requires DAX/Power Query (technical skills)
- Writeback (4/4): Export only, manual process to operationalize

### Scoop: 82/100 (Category A - Strong)

**Autonomy: 18/20**
- Setup (8/8): 30-second Slack install, zero IT
- Question Independence (6/6): Full NL, any question
- Speed to Value (4/6): Minutes to first insight (improving to seconds)

**Flow: 18/20**
- Native Integration (8/8): Slack + Excel/Sheets + Mobile + PowerPoint
- No Portal Prison (6/6): Zero portal requirement
- Interface Simplicity (4/6): Conversational NL (improving context)

**Understanding: 18/20**
- Investigation Depth (8/8): Automatic multi-pass (3-10 queries), root cause
- ML Pattern Discovery (6/6): J48 (800+ nodes), EM clustering, explainable
- Business Explanation (4/6): Good narratives (improving actionability)

**Presentation: 16/20**
- Visual Quality (6/6): Pixel-perfect, Gartner-quality aesthetics
- Brand Automation (6/8): Auto brand detection (expanding live overlay)
- Speed & Formats (4/6): 30-second generation (expanding formats)

**Data: 12/20**
- Connections (4/4): Self-service, any source
- Schema Evolution (6/8): Automatic adaptation (continuous improvement)
- Data Prep (4/4): 150+ Excel functions, spreadsheet engine
- Writeback (0/4): Coming soon (Salesforce, HubSpot integration)

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
- Quote overall score: "Power BI Copilot: 32/100 (Category D - Weak)"
- Emphasize worst dimensions: "Scores 4/20 on Understanding - can't investigate WHY"

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