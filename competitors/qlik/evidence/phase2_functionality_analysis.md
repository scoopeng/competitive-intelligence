# Phase 2: Functionality Deep Dive Research Library

**Research Date**: September 26, 2025
**Researcher**: Claude
**Time Spent**: 40 minutes

## Phase 2A: Documentation & Core Functionality

### Core Capabilities Overview
**URL**: https://help.qlik.com
**Summary**: Qlik positions itself as an enterprise analytics platform with multi-cloud architecture and self-service capabilities.
**Key Capabilities Found**:
- Associative Engine technology (unique data exploration model)
- Dashboard and analytics visualization
- GeoAnalytics for spatial data
- Qlik Predict (mentioned but limited details)
- "Augmented analytics" (vague marketing term)
- Centralized management and governance

### Demo Walkthrough Research
**URL**: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Tutorials/
**Summary**: Official tutorials show basic BI functionality with steep learning curve.
**Key Evidence**:
- "Beginning with the Basics" tutorial needed for simple tasks
- Interactive dashboards for "in-depth examination"
- R/Python integration for "complex analyses" (requires coding)
- Storytelling feature for data narratives
- AutoML requires technical expertise despite "automated" claims

### Feature List Documentation
**URL**: https://qlik.dev and various help pages
**Summary**: Complex platform with multiple products requiring significant integration.
**Key Features**:
- Qlik Sense, Qlik Replicate, Talend Data Fabric, Stitch Data (confusing product portfolio)
- Data Flow with "intuitive drag-drop" (still requires understanding of data structures)
- APIs with TypeScript support (developer-focused, not business users)
- Visual low-code automation (but requires technical understanding)
- 500 unique report maximum, 4-hour execution time limits

### Use Cases and Applications
**URL**: Various customer stories
**Summary**: Focus on large enterprises with dedicated data teams.
**Notable Examples**:
- Honda: 7,000 users (but what percentage actively use it?)
- Samsung: "Real-time alerting" (basic feature marketed as advanced)
- Lenovo: "Transforms data" (vague claim)
- Fraud detection, forecasting (standard BI features)

### Workflow End-to-End Process
**URL**: https://www.qlik.com/us/products/qlik-automate
**Summary**: Complex multi-step process requiring technical setup.
**Key Evidence**:
- Qlik Compose requires understanding of data warehouses and ETL
- Workflow Designer needs technical knowledge of data flows
- "No-code" still requires understanding connectors and logic
- Task chaining requires automation expertise
- "What used to take days" but initial setup takes weeks/months

## Phase 2B: Business User Empowerment Assessment (vs Scoop)

### Excel Integration
**Capability**: Export to Excel
**What It Does**: Exports static data to Excel files
**How It Works**: Data export only, no formula conversion
**Business User Empowerment**: 2/10 - Loses all interactivity
**vs Scoop Equivalent**: Scoop has 150+ native Excel functions that work on live data
**Gaps/Limitations**:
- Cannot export Qlik formulas as Excel formulas
- No live connection to Excel
- Requires third-party extensions for Excel-like features
- Formatting and conditional logic lost in export
**Evidence**: Community forums confirm "QlikView formulas cannot be directly exported as Excel formulas"

### Natural Language Processing
**Capability**: Insight Advisor Chat
**What It Does**: Accepts natural language queries
**How It Works**: NLP engine interprets user intent
**Business User Empowerment**: 4/10 - Requires exact field names
**vs Scoop Equivalent**: Scoop's multi-pass investigation with context retention
**Gaps/Limitations**:
- Cannot handle typos (one typo = query fails)
- Requires Business Logic customization
- Limited to single queries, no investigation depth
- Needs exact field names and syntax
**Evidence**: "Insight Advisor supports natural language searches" but requires precise syntax

### Machine Learning/AI
**Capability**: Qlik Predict and AutoML
**What It Does**: No-code ML platform for predictive models
**How It Works**: AutoML tools for model creation
**Business User Empowerment**: 3/10 - Still requires data science understanding
**vs Scoop Equivalent**: Scoop's automatic ML (J48, JRip, EM) runs without user awareness
**Gaps/Limitations**:
- "No-code" but requires understanding of ML concepts
- Models need manual training and deployment
- Not automatic - user must initiate and configure
- Requires data preparation and feature engineering
**Evidence**: "Empower analysts - not just data scientists" but still requires technical knowledge

### Self-Service Analytics
**Capability**: Self-service BI platform
**What It Does**: Allows users to create dashboards and reports
**How It Works**: Drag-drop interface with associative model
**Business User Empowerment**: 3/10 - Requires significant training
**vs Scoop Equivalent**: Scoop's 30-second setup with no training
**Gaps/Limitations**:
- "Self-service" requires weeks of training
- Need to understand data models and relationships
- Must know field names and structures
- IT still needed for data connections
**Evidence**: "Business users no longer have to submit request to IT" but Phase 1 evidence shows "depend on developers"

### PowerPoint/Slack Integration
**Capability**: Qlik Application Automation with connectors
**What It Does**: Send charts and alerts to Slack
**How It Works**: Automation workflows with visual interface
**Business User Empowerment**: 4/10 - Requires workflow setup knowledge
**vs Scoop Equivalent**: Scoop native in Slack, PowerPoint generation in 30 seconds
**Gaps/Limitations**:
- No direct PowerPoint generation found
- Slack integration requires automation setup
- Cannot generate presentations, only send images
- Multiple steps and configuration needed
**Evidence**: "Send chart image to Slack" but no presentation generation capability

### Root Cause Analysis
**Capability**: Associative data model exploration
**What It Does**: Allows free exploration of data relationships
**How It Works**: Click through associations in data
**Business User Empowerment**: 5/10 - Better than most but still manual
**vs Scoop Equivalent**: Scoop's multi-hypothesis testing with 3-10 queries
**Gaps/Limitations**:
- User must manually explore relationships
- No automatic investigation or hypothesis testing
- Single-query responses, no multi-pass reasoning
- Requires understanding of data relationships
**Evidence**: "Explore data in unrestricted manner" but user drives investigation manually

## Phase 2C: Gap Analysis & Limitations

### Technical Limitations Found
**Search**: "qlik limitations" cannot do missing features
**Key Limitations**:
- No support for LOB data types in replication
- Virtual columns not supported
- OAuth not supported for Snowflake
- Direct Discovery has no new development planned
- Failed automations only notify once every 6 hours
- Cannot process curly brackets in formulas
- Maximum 500 unique reports per task
- 4-hour maximum execution time for reports

### Scoop vs Qlik Direct Comparison
**Search**: "qlik vs Scoop" comparison
**Key Findings**:
- Qlik requires "significant training" and "dedicated data teams"
- Scoop: "No SQL. No formulas. No training."
- Qlik: "Can't just sign in and build dashboard"
- Scoop: "Connect and go" with 100+ integrations
- Qlik: Enterprise-grade but complex
- Scoop: AI-first with multi-step reasoning

### IT Requirements
**Search**: "qlik requires IT" technical expertise needed
**Evidence of IT Dependency**:
- "Proficiency in QlikView scripting language, set analysis" required
- Need SQL and data modeling expertise
- "Interact with IT professionals to ensure seamless integration"
- Port 443 must be opened by IT
- User permissions and entitlements managed by IT
- "Qlik Developer must possess strong analytical and critical thinking"

### Training and Certification
**Search**: "qlik training certification" learning curve
**Training Requirements**:
- 2-hour exams with 50-60 questions
- Must achieve 58% to pass
- Need "complete knowledge of ETL process"
- "Proficient in SQL and relational databases" required
- Multiple certification levels (fundamental to expert)
- "Significant preparation needed" for advanced certs

### Implementation Timeline
**Search**: "qlik setup time" implementation duration
**Timeline Reality**:
- "Few hours to few months" depending on complexity
- Simple setup: 5 days minimum
- Complex implementations: Several months
- Optimization alone can take weeks
- "Development and maintenance time" ongoing costs
- Compare to Scoop's "30-second setup"

## Competitive Capability Matrix

| Capability | Qlik | Scoop | Winner | Why |
|------------|------|-------|--------|-----|
| Excel Support | ❌ Static export only | ✅ 150+ live functions | Scoop | Native Excel execution vs static export |
| ML/AI Analysis | ⚠️ AutoML requires expertise | ✅ Automatic ML | Scoop | Runs without user awareness |
| Investigation Depth | ❌ Single queries | ✅ Multi-pass reasoning | Scoop | 3-10 queries with context |
| Workflow Integration | ⚠️ Complex automation setup | ✅ 30-second native | Scoop | Native vs complex configuration |
| Business User Ready | ❌ Weeks of training | ✅ No training needed | Scoop | Immediate vs extensive learning |
| Natural Language | ❌ Can't handle typos | ✅ True NLP | Scoop | Flexible vs rigid syntax |
| PowerPoint Generation | ❌ Not found | ✅ 30-second decks | Scoop | Complete presentations vs none |
| Root Cause Analysis | ⚠️ Manual exploration | ✅ Automatic investigation | Scoop | AI-driven vs user-driven |
| Setup Time | ❌ Days to months | ✅ 30 seconds | Scoop | Immediate vs lengthy implementation |
| Cost Transparency | ❌ "Hard to know what you'll pay" | ✅ Clear pricing | Scoop | Transparent vs opaque |

## Fatal Functionality Gaps

### 1. No Excel Formula Engine
- Qlik cannot execute Excel formulas
- Exports are static, losing all interactivity
- Third-party extensions required for Excel-like features
- **Impact**: Business users lose their primary tool

### 2. Typo Intolerance in NLP
- One typo breaks entire query
- Requires exact field names
- Cannot handle variations or synonyms
- **Impact**: Not actually natural language

### 3. No Automatic ML Discovery
- User must initiate ML processes
- Requires understanding of ML concepts
- Manual model training and deployment
- **Impact**: Not accessible to business users

### 4. No Multi-Pass Investigation
- Single query responses only
- No context retention between queries
- Cannot test multiple hypotheses
- **Impact**: Can't answer "why" questions

### 5. No Native Workflow Integration
- Complex setup for Slack integration
- No PowerPoint generation capability
- Requires automation expertise
- **Impact**: Disrupts existing workflows

## Summary of Phase 2 Findings

**Core Weakness**: Qlik is a traditional BI platform trying to bolt on modern AI features, but the foundation wasn't built for business user empowerment.

**Technical Debt**: Legacy architecture shows through in limitations like Direct Discovery having "no new development" and inability to handle modern requirements like OAuth for Snowflake.

**Business User Reality**: Despite "self-service" marketing, Phase 1 evidence of "depend on developers" is confirmed by technical requirements found in Phase 2.

**Training Burden**: Certification requirements confirm weeks to months of learning curve, contradicting self-service claims.

**Integration Complexity**: Every integration requires technical setup, configuration, and ongoing maintenance - nothing is truly "30-second" or "no-code" despite marketing claims.