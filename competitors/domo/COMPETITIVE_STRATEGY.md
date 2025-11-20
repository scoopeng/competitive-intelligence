# Competitive Strategy: Domo

**Last Updated**: November 18, 2025
**Maintained By**: Human (strategic positioning decisions)
**Used By**: web_comparison generation, battle card generation, sales enablement

---

## 1. PRIMARY WEAKNESSES (Rank Top 3)

**#1: Workflow Disruption: Dashboard-First Architecture vs. True Workflow Integration** (Severity: Critical | Defensibility: Architectural)
- **Evidence**: BUA Portal Prison 0/6, Native Integration 4/8. AI Chat (DomoGPT) CAN query datasets but quality depends on AI Readiness metadata configuration. Excel formulas DISABLED for security ("Domo disables any formulas in Excel files before export"). NO native Slack integration (requires Workato/n8n). PowerPoint add-in requires manual one-visual-at-a-time insertion. "Portal prison" per BATTLE_CARD.
- **Why It Matters**: Domo's 2010s dashboard-first architecture forces users into a dedicated portal, creating **Workflow Disruption**. Business users cannot operationalize expertise or perform complex data transformations using familiar tools like Excel (where formulas are disabled). This fragmented experience hinders agility and widespread adoption of intelligence across the organization.
- **Our Advantage**: Scoop offers **True Workflow Integration**. Native in Slack for bidirectional analysis, a full **Spreadsheet Calculation Engine** with 150+ live Excel formulas, and **Automated Presentation Generation** for executive-ready PowerPoint decks. We meet users where they already work, seamlessly integrating intelligence into their daily operational rhythm.
- **Defensibility**: Architectural. Domo's legacy architecture and security policies fundamentally limit its ability to provide native, integrated workflow capabilities comparable to a modern **Domain Intelligence Platform**.
- **Emphasis Level**: 30% of web comparison

**#2: Investigation Gap: Bolt-On LLM vs. Autonomous Investigation** (Severity: High | Defensibility: Architectural + Temporal)
- **Evidence**: BUA Investigation 8/8 (misleading high score for AutoML, but lacks autonomous multi-pass). DomoGPT (bolt-on LLM) does NL-to-SQL but cannot perform multi-pass investigation (3-10 automated queries). No hypothesis testing, no automated root cause analysis. "Can't investigate WHY metrics changed across business" per BATTLE_CARD. "Mr. Roboto is statistics from 2017" - pre-LLM era.
- **Why It Matters**: Domo's AI capabilities are an LLM layer bolted onto a dashboard platform, creating a significant **Investigation Gap**. It can translate natural language into SQL but lacks the architectural components (like a state machine) for multi-step, context-aware, autonomous investigation. This means it can show *what* happened but cannot reliably determine *why* or propose actionable solutions, limiting its ability to operationalize true intelligence.
- **Our Advantage**: Scoop is built from the ground up for **Autonomous Investigation**. Our **Investigation Coordinator** (15-module state machine) executes multi-step "Display-Diagnose-Decide" workflows, tests hypotheses leveraging **Encoded Expertise (Schema v2.8)**, and provides ML-validated root cause analysis. We deliver proactive, actionable intelligence, closing the **Investigation Gap**.
- **Defensibility**: Architectural. A bolt-on LLM cannot fundamentally transform a dashboard platform into an **Autonomous Investigation** engine without a complete re-architecture.
- **Emphasis Level**: 25% of web comparison

**#3: TCO Trap: Unpredictable Consumption vs. Eliminated Labor** (Severity: Critical | Defensibility: Strategic)
- **Evidence**: BUA score notes "$95,800 for 100 users" (not advertised $10K), "$134K average annual cost." "1% of company revenue" (actual customer quote). "1120% renewal increase" documented case. Consumption model drives unpredictable costs. "Pricing chaos: Expensive and hard to understand pricing" (Capterra).
- **Why It Matters**: Domo's consumption pricing model creates a **TCO Trap**, leading to unpredictable costs and renewal shock. This opaque pricing contrasts sharply with the need for cost efficiency in modern intelligence platforms. It burdens organizations with monitoring usage rather than focusing on value, undermining agile budget planning.
- **Our Advantage**: Scoop offers a predictable, flat annual fee ($3,588 typical base). Our cost advantage stems from **Eliminated Labor Categories**: zero implementation, zero training, zero semantic model maintenance (due to **Schema Evolution**). We provide transparent pricing and exceptional value by eliminating the hidden costs associated with traditional BI and bolt-on AI solutions.
- **Defensibility**: Strategic. Domo's business model relies on a consumption-based revenue growth strategy. Scoop's strategy is to deliver maximum intelligence at minimum TCO through architectural efficiency.
- **Emphasis Level**: 20% of web comparison

---

## 2. KEY SCENARIOS

**Scenario 1: Intelligence Ceiling: AI Readiness Metadata vs. Encoded Expertise**
- **When to Use**: AI Chat discussions, self-service claims, and operationalizing expertise.
- **Story**: "Domo's AI Chat (DomoGPT) can query datasets, but its quality is contingent on 'AI Readiness' metadata configuration by IT. This means business users are still dependent on developers to prepare and define business context, creating an **Intelligence Ceiling**. Scoop: Our **Schema v2.8** and **Encoded Expertise** eliminate this dependency. Business users ask questions on raw data, and our system automatically operationalizes existing business rules, providing immediate, context-rich intelligence without IT intervention."
- **Expected Impact**: Clarifies that DomoGPT doesn't eliminate IT dependency; it just adds a natural language interface to a pre-configured portal, limiting its ability to leverage **Domain Intelligence** autonomously.

**Scenario 2: TCO Trap: The 1120% Renewal Shock**
- **When to Use**: Renewal discussions, cost concerns, and TCO comparisons.
- **Story**: "One customer documented an '1120% renewal increase'—a drastic shift from predictable to chaotic pricing. Another stated Domo costs '1% of company revenue.' This consumption-based model creates a **TCO Trap** of unpredictable costs. Scoop: Offers a flat, predictable annual fee ($3,588 typical base). Our cost advantage is rooted in **Eliminated Labor Categories**: zero implementation, zero training, and zero semantic model maintenance due to **Schema Evolution**. We provide transparent pricing and deliver exceptional value by architecturally removing hidden costs, not by playing pricing games."
- **Expected Impact**: Dramatically highlights the financial risk and unpredictability of Domo's pricing model against Scoop's architectural efficiency and transparent cost structure.

**Scenario 3: Workflow Disruption: Excel Formulas Disabled vs. Spreadsheet Calculation Engine**
- **When to Use**: When prospects have Excel-heavy workflows and need advanced data transformation.
- **Story**: "Domo officially disables Excel formulas 'for security' prior to export. This means a business analyst needing a VLOOKUP to match customer segments must download a CSV, manually rebuild formulas, and lose the live connection. This creates significant **Workflow Disruption**. Scoop: Our **Spreadsheet Calculation Engine** natively supports 150+ live Excel functions (including VLOOKUP, SUMIFS, FILTER) directly on your data. Users work in their native Excel environment, operationalizing complex data transformations in real-time without losing context or requiring manual data manipulation."
- **Expected Impact**: Excel power users immediately understand the profound workflow gap, validating Scoop's commitment to **True Workflow Integration** and operationalizing expertise where users already work.

---

## 3. TALKING POINTS

**Lead With** (Most important - first 1000 words):
1.  **"True Workflow Integration vs. Workflow Disruption"** - *We seamlessly operationalize intelligence in Slack and Excel; they force users into a portal and disable critical Excel functionality.*
2.  **"Autonomous Investigation vs. Bolt-On LLM (Investigation Gap)"** - *Our **Investigation Coordinator** autonomously solves problems; their DomoGPT is a single-query NL-to-SQL translator.*
3.  **"Eliminated Labor Categories vs. TCO Trap (Unpredictable Costs)"** - *We remove entire cost centers through architectural efficiency; their consumption model leads to massive renewal shock.*

**Always Mention** (Core Architectural Advantages):
4.  **Spreadsheet Calculation Engine** (150+ live Excel formulas native to Scoop, eliminating Domo's formula disability).
5.  **Investigation Coordinator** (The 15-module state machine for multi-step, autonomous root cause analysis).
6.  **Schema v2.8 with Encoded Expertise** (Operationalizing your business rules, not relying on 'AI Readiness' metadata).
7.  **Automated Presentation Generation** (Delivering executive-ready insights automatically, not one visual at a time).
8.  **Flat, Predictable Pricing** (Escaping the consumption pricing chaos).

**De-Emphasize** (Acknowledge but don't lead):
- **Domo's Dresner Leader position** (Frame as traditional dashboard BI, not modern **Domain Intelligence**).
- **1000+ connectors** (Acknowledge the breadth, but highlight the configuration and maintenance burden).
- **DomoGPT capabilities** (Acknowledge the LLM integration, but emphasize its fundamental **Investigation Gap**).

---

## 4. CONTENT DISTRIBUTION

**Emphasis Adjustment Philosophy**:
- ⬆️ INCREASE on **Workflow Disruption** (dashboard-first, Excel formulas disabled, portal dependency)
- ⬆️ INCREASE on **Investigation Gap** (bolt-on LLM vs. autonomous investigation)
- ⬆️ INCREASE on **TCO Trap** (unpredictable consumption pricing, eliminated labor categories)
- ⬇️ DECREASE on less critical aspects or areas where Domo has limited functionality.

**Recommended Mix**:
- **Section 1 (Executive Summary)**: 10%
- **Section 2 (Capabilities)**: 60%
    - **Workflow Disruption & True Workflow Integration**: 30% (Highlighting portal-first design, lack of native Excel/Slack, vs. Scoop's seamless integration)
    - **Investigation Gap & Autonomous Investigation**: 25% (Emphasizing bolt-on LLM limits vs. Scoop's dedicated Investigation Coordinator)
    - **TCO Trap & Eliminated Labor Categories**: 20% (Focusing on consumption pricing unpredictability vs. Scoop's architectural efficiency)
    - **Intelligence Ceiling & Encoded Expertise**: 15% (Addressing AI Readiness metadata dependency vs. Scoop's Schema v2.8)
    - **Setup & Maintenance Burden**: 10% (Connecting data cards/datasets complexity to IT overhead)
- **Section 3 (Use Cases)**: 15% (Demonstrating scenarios where Domo struggles and Scoop excels)
- **Section 4 (FAQ/Evidence/Next Steps)**: 10%
- **Section 5 (Market & Financials)**: 5% (Briefly touching on market share and financial indicators where relevant)

**Rationale**:
Domo's core challenges revolve around **Workflow Disruption** (due to its dashboard-first legacy), a significant **Investigation Gap** (from its bolt-on LLM strategy), and a problematic **TCO Trap** (from consumption pricing). These are fundamental limitations in the context of a **Domain Intelligence Platform**. The content distribution must reflect these deep architectural and strategic distinctions to establish Scoop's unique value proposition.

---

## 5. PROOF POINTS

**From Framework Scoring** (`evidence/framework_scoring.md`):
- **BUA Total**: 62/100 (Category B - Good for dashboards, but limited for deep investigation)
- **Critical Sub-Scores**:
  - **Portal Prison**: 0/6 (Evidence of **Workflow Disruption**)
  - **Native Integration**: 4/8 (Highlights **Workflow Disruption** due to disabled Excel formulas, manual PowerPoint)
  - **Investigation**: 8/8 (Misleading - high score for AutoML, but explicitly lacks autonomous multi-pass investigation, indicating an **Investigation Gap**)
  - **Setup (AI Readiness Metadata)**: Directly contributes to **Intelligence Ceiling** and IT dependency.

**From Research**:
- "1120% renewal increase" - Direct evidence of **TCO Trap**.
- "1% of company revenue" - Further evidence of **TCO Trap**.
- "$95,800 for 100 users" (vs $10K advertised) - Illustrates opaque pricing of **TCO Trap**.
- "Domo disables any formulas in Excel files before export" - Critical evidence of **Workflow Disruption**.
- "Business users find it complicated" & "49 users mentioned high learning curve" (G2) - Supports **Intelligence Ceiling** and adoption challenges.
- "28 users find it expensive" (G2) - Reinforces **TCO Trap**.
- "Can't investigate WHY metrics changed across business" (BATTLE_CARD) - Explicitly states **Investigation Gap**.
- "Mr. Roboto is statistics from 2017" - Highlights the bolt-on nature of AI and the **Investigation Gap**.

---

## 6. WIN CONDITIONS

**We Win When**:
1.  **True Workflow Integration is Required**: When business users need to operationalize intelligence directly in Slack and Excel (with full formula support), avoiding Domo's **Workflow Disruption** and portal dependency.
2.  **Autonomous Root Cause Investigation is Critical**: When the customer needs AI-driven, multi-step reasoning to find "why" and actionable solutions, beyond DomoGPT's single-query NL-to-SQL translation and its inherent **Investigation Gap**.
3.  **Predictable TCO and Eliminated Labor Categories are a Priority**: When the customer wants to escape unpredictable consumption pricing and seeks to eliminate costly IT dependencies for implementation and semantic model maintenance (addressing Domo's **TCO Trap**).
4.  **Operationalizing Encoded Expertise is Key**: When the goal is to leverage pre-defined business rules without constant IT configuration of 'AI Readiness' metadata.
5.  **Small/Mid-Market Agility**: When organizations need enterprise-grade intelligence without the enterprise-level pricing complexity or scale requirements, as Domo often targets larger enterprises.

**We Lose When**:
- A large enterprise is already deeply invested in Domo's dashboard ecosystem and its cards/datasets model, with a team dedicated to its maintenance.
- The primary use case is simple dashboard consumption and reporting, where the depth of autonomous investigation is not a high priority.
- The organization is comfortable with unpredictable consumption pricing and finds value in Domo's extensive connector library, despite the configuration burden.

**Neutral** (Could go either way):
- A large organization uses Domo for specific dashboarding needs but is open to a complementary **Domain Intelligence Platform** for deeper, autonomous investigation and streamlined business user workflows.

---

## 7. COMPETITIVE POSITIONING

**Product Type Classification**:
- **What They Really Are**: Dashboard-First BI Platform with Bolt-On LLM (Passive BI, creating **Workflow Disruption**)
- **What We Really Are**: **Cloud-Native Domain Intelligence Platform** (for **Autonomous Investigation** and operationalizing **Encoded Expertise**)
- **Their Primary Audience**: IT teams building dashboards for enterprise consumption
- **Our Primary Audience**: Business users requiring immediate, context-aware insights and operationalized expertise
- **Key Architectural Difference**: Dashboard-first, consumption-priced, LLM bolt-on vs. **Investigation-Coordinator** driven, flat-priced, **Encoded Expertise** platform.

**One-Sentence Position**:
"Domo is a dashboard-first BI platform with a bolt-on LLM that creates **Workflow Disruption**, suffers from an **Investigation Gap**, and presents a **TCO Trap** due to unpredictable consumption pricing; Scoop is a **Cloud-Native Domain Intelligence Platform** that provides **True Workflow Integration**, executes **Autonomous Investigation** via its **Investigation Coordinator**, and offers predictable costs through **Eliminated Labor Categories**."

**Elevator Pitch** (30 seconds):
"Domo, a dashboard-first platform, creates **Workflow Disruption** by forcing users into a portal and disabling critical Excel formulas. Its DomoGPT is a bolt-on LLM, creating an **Investigation Gap** by limiting it to single-query NL-to-SQL. Furthermore, its consumption pricing leads to a **TCO Trap** with unpredictable costs and renewal shock (e.g., 1120% increases). Scoop is fundamentally different: a **Cloud-Native Domain Intelligence Platform**. We provide **True Workflow Integration** (native Slack, full Excel formulas), execute **Autonomous Investigation** via our **Investigation Coordinator** and **Encoded Expertise**, and offer predictable costs through **Eliminated Labor Categories**. We don't just show data; we operationalize intelligence and solve business problems."

**Key Contrast**:
| Dimension | Domo | Scoop |
|-----------|------|-------|
| **Product Type** | Dashboard Platform + Bolt-On LLM | **Domain Intelligence Platform** |
| **Core Mechanism** | Dashboard-First / NL-to-SQL | **Investigation Coordinator (State Machine)** |
| **Workflow** | Portal-Centric / Disabled Excel Formulas | **True Workflow Integration (Native Slack/Excel)** |
| **Investigation** | Single-Query / Limited Context | **Autonomous / Multi-Step / Encoded Expertise** |
| **Pricing Model** | Consumption-Based (**TCO Trap**) | **Flat / Predictable (Eliminated Labor)** |
| **Schema Evolution** | Manual / IT-Dependent | **Automatic (Schema v2.8)** |
| **Presentation** | Manual / One-by-One Insertion | **Automated Generation (Visual Intelligence System)** |

---

## 8. AVOID OVER-CLAIMING

**Don't Say** (Risks credibility):
- "Domo has no AI" - *DomoGPT (LLM integration) exists; focus on its architectural limits.*
- "AI Chat requires dashboards" - *It can query datasets; focus on the dependency on 'AI Readiness' metadata.*
- "No connectors" - *They have 1000+ connectors; focus on the configuration and maintenance burden.*

**Instead Say** (Evidence-based alternatives):
- "Domo's DomoGPT is an LLM bolted onto a dashboard platform, creating an **Investigation Gap** by limiting it to single-query NL-to-SQL translation." - *Accurate and highlights architectural flaw.*
- "DomoGPT's quality is contingent on IT-configured 'AI Readiness' metadata, creating an **Intelligence Ceiling** for business users and perpetuating IT dependency." - *Fair and emphasizes user friction.*
- "Domo's extensive connector library requires significant configuration and ongoing maintenance, contributing to the **TCO Trap**." - *True and links breadth to cost.*
- "DoDom's policy of disabling Excel formulas for security creates **Workflow Disruption** for business users who rely on native spreadsheet capabilities." - *Evidence-based critique of a specific functional limitation.*

---

## 9. DOMO-SPECIFIC INSIGHTS

### The Cards/Datasets Model: An Intelligence Ceiling and TCO Trap
- Dashboard components ("cards") built on "datasets."
- Each dataset requires setup, transformation (Magic ETL), and ongoing maintenance.
- AI Chat works with datasets, but quality is dependent on 'AI Readiness' metadata, creating an **Intelligence Ceiling**.
- Consumption pricing is directly tied to cards/datasets usage, contributing to the **TCO Trap**.
- **Impact**: This model creates complexity, IT dependency, and unpredictable costs, limiting the operationalization of **Domain Intelligence**.

### The DomoGPT Reality (2024): A Bolt-On LLM with an Investigation Gap
- Announced as an "AI Service Layer" with model flexibility (OpenAI default, Amazon Bedrock models available).
- Functions as Natural Language to SQL but fundamentally lacks **Autonomous Investigation** capabilities.
- It translates queries but cannot execute multi-step, hypothesis-driven reasoning like Scoop's **Investigation Coordinator**.
- Still requires 'AI Readiness' metadata for quality, highlighting the lack of **Encoded Expertise** in its core architecture.
- **Impact**: A bolt-on LLM strategy creates a significant **Investigation Gap**, preventing deep, context-aware problem-solving.

### The Consumption Pricing Trap: Unpredictable Costs for Operational Intelligence
- The "1% of revenue" model scales unpredictably with company size, leading to the **TCO Trap**.
- Cards/datasets usage directly drives costs, making budgeting for **Domain Intelligence** challenging.
- Documented "1120% renewal increase" highlights the severe financial risk.
- **Impact**: Undermines the predictable cost structure essential for enterprise adoption of an **analytical application platform**.

### The Portal Dependency: Workflow Disruption for True Integration
- Domo's dashboard-first architecture necessitates a portal-first workflow, leading to **Workflow Disruption**.
- DomoGPT, while an LLM, does not enable users to escape the portal for full analysis.
- Excel plugin exists, but formulas are disabled "for security," further hindering **True Workflow Integration**.
- No native Slack integration (requires Workato/n8n custom development).
- PowerPoint add-in requires manual visual insertion.
- **Impact**: Prevents seamless integration of **Domain Intelligence** into users' native operational environments.

---

## MAINTENANCE SCHEDULE

**Quarterly Review**:
- [ ] Check if Excel formula policy changes
- [ ] Verify DomoGPT evolution (multi-pass investigation added?)
- [ ] Review consumption pricing model changes
- [ ] Update AI Readiness metadata requirements

**Version History**:
- 2025-09-28: Initial version based on BUA 62/100. Portal prison (30%), AI hype vs reality (25%), cost explosion (20%).

---

**Template Version**: 1.1
**Created**: September 28, 2025
**Competitor BUA Score**: 62/100 (Category B - Good for dashboards, not investigation)