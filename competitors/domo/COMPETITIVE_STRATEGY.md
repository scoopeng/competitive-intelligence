# Competitive Strategy: Domo

**Last Updated**: September 28, 2025
**Maintained By**: Human (strategic positioning decisions)
**Used By**: web_comparison generation, battle card generation, sales enablement

---

## 1. PRIMARY WEAKNESSES (Rank Top 3)

**#1: Portal Prison + Dashboard-First Architecture** (Severity: Critical | Defensibility: Architectural)
- **Evidence**: BUA Portal Prison 0/6, Native Integration 4/8. AI Chat (DomoGPT) CAN query datasets but quality depends on AI Readiness metadata configuration. Excel formulas DISABLED for security ("Domo disables any formulas in Excel files before export"). NO native Slack integration (requires Workato/n8n). PowerPoint add-in requires manual one-visual-at-a-time insertion. "Portal prison" per BATTLE_CARD.
- **Why It Matters**: Dashboard-first architecture from 2010s DNA. Even with DomoGPT, users must log into portal, configure datasets with AI Readiness metadata, work within Domo environment. Cannot use Excel VLOOKUP, SUMIFS, or any formulas with live Domo data. "Business users find it complicated" - requires training to navigate Workbench, Analyzer, multiple tools.
- **Our Advantage**: Scoop native in Slack, Excel (150+ formulas with live data), automatic PowerPoint. Work where you already work, no portal dependency.
- **Defensibility**: Architectural—dashboard-first platform architecture requires portal. Excel formula disabling is "security" decision but reflects limited integration model. Would require complete re-architecture for native tools.
- **Emphasis Level**: 30% of web comparison

**#2: AI Hype vs AI Reality (Bolt-On LLM)** (Severity: High | Defensibility: Architectural + Temporal)
- **Evidence**: BUA Investigation 8/8 shows AutoML exists but "single query paradigm, not multi-pass investigation." DomoGPT launched as LLM layer (OpenAI default, Amazon Bedrock models). AI Service Layer offers flexible model selection BUT platform wasn't built as agentic/AI-first. "Can't investigate WHY metrics changed across business" per BATTLE_CARD. "Mr. Roboto is statistics from 2017" - pre-LLM era.
- **Why It Matters**: Domo built 2010s as dashboard platform, bolted LLM on top 2023-2024. DomoGPT does NL-to-SQL but cannot do multi-pass investigation (3-10 automated queries). No hypothesis testing, no automated root cause analysis. AI Readiness metadata required for quality—still IT dependency. Platform architecture predates agentic AI by decade.
- **Our Advantage**: Scoop built from ground up for AI investigation. Multi-pass reasoning engine (3-10 queries), hypothesis testing, ML validation. Not LLM-to-SQL, true investigation.
- **Defensibility**: Mixed—bolt-on LLM is Architectural (cannot retrofit investigation engine), but models may improve (Temporal). Emphasize investigation gap over LLM quality.
- **Emphasis Level**: 25% of web comparison

**#3: Consumption Pricing + Cost Explosion** (Severity: Critical | Defensibility: Strategic)
- **Evidence**: BUA score notes "$95,800 for 100 users" (not advertised $10K), "$134K average annual cost." "1% of company revenue" (actual customer quote). "1120% renewal increase" documented case. Consumption model drives unpredictable costs. "28 users find it expensive especially for small companies" (G2). "Pricing chaos: Expensive and hard to understand pricing" (Capterra).
- **Why It Matters**: Consumption pricing model creates renewal shock. Cards/datasets usage-based billing = unpredictable costs. Small businesses report "not a target customer group." 27x more expensive than Scoop for 100 users ($95,800 vs $3,588). "1% of revenue" means $1M company pays $10K—pricing scales with company size regardless of value.
- **Our Advantage**: Scoop flat $3,588 annual. No consumption surprises, no renewal shock, no pricing complexity.
- **Defensibility**: Strategic—chose consumption pricing model. Could change but currently baked into business model and revenue growth strategy.
- **Emphasis Level**: 20% of web comparison

---

## 2. KEY SCENARIOS

**Scenario 1: The Dashboard Dependency Trap**
- **When to Use**: AI Chat discussions and self-service claims
- **Story**: "Domo's AI Chat can query datasets—but quality requires AI Readiness metadata configuration by IT. Best results come from well-prepared datasets with business context. That's still IT dependency, just with NL interface. Scoop: zero configuration, immediate investigation, no metadata layer needed."
- **Expected Impact**: Clarifies that DomoGPT doesn't eliminate IT dependency, just adds NL interface to portal.

**Scenario 2: The 1120% Renewal Shock**
- **When to Use**: Renewal discussions and cost concerns
- **Story**: "One customer documented 1120% renewal increase—from predictable to pricing chaos. Another said Domo costs '1% of company revenue.' That's $100K for $10M company, $1M for $100M company. Consumption pricing makes costs unpredictable. Scoop: $3,588 flat, forever. No surprises, no renewal shock."
- **Expected Impact**: Cost explosion story validates pricing concerns, especially for renewals.

**Scenario 3: Excel Formula Disabled**
- **When to Use**: When prospect has Excel-heavy workflows
- **Story**: "Domo officially disables Excel formulas 'for security' before export. Business analyst needs VLOOKUP to match customer segments? Download CSV, rebuild formulas manually, lose live connection. Scoop: VLOOKUP works natively with 150+ other functions. Live data, real formulas."
- **Expected Impact**: Excel power users immediately understand workflow gap.

---

## 3. TALKING POINTS

**Lead With**:
1. **"Portal prison with AI chatbot"** - *Because DomoGPT requires portal login, AI Readiness metadata, Domo environment*
2. **"1120% renewal increase documented"** - *Because actual customer case validates consumption pricing explosion*
3. **"Excel formulas disabled for security"** - *Because official policy creates workflow gap*

**Always Mention**:
4. **Bolt-on LLM vs investigation** (NL-to-SQL ≠ multi-pass investigation)
5. **$95,800 for 100 users** (vs advertised $10K)
6. **AI Readiness metadata requirement** (IT dependency persists)

**De-Emphasize**:
- **#1 in Dresner study** (true for dashboards, acknowledge it)
- **1000+ connectors** (impressive number, focus on configuration burden instead)
- **DomoGPT capabilities** (decent LLM integration, emphasize investigation gap not LLM quality)

---

## 4. CONTENT DISTRIBUTION

**Recommended Mix**:
- **Portal Prison + Dashboard-First**: 30% (~2,250 words)
- **AI Hype vs Reality**: 25% (~1,875 words)
- **Consumption Pricing Explosion**: 20% (~1,500 words)
- **Cards/Datasets Complexity**: 15% (~1,125 words)
- **Setup & Maintenance**: 10% (~750 words)

**Rationale**: Portal prison is architectural and complete (0/6). AI hype needs clarification (bolt-on LLM, not investigation platform). Cost explosion is strategic but severe (1120% increases). Cards/datasets model creates complexity.

---

## 5. PROOF POINTS

**From Framework Scoring**:
- **BUA Total**: 62/100 (Category B - Good for dashboards, not investigation)
- **Portal Prison**: 0/6
- **Native Integration**: 4/8 (Excel exists but formulas disabled)
- **Investigation**: 8/8 (AutoML exists but single-query)

**From Research**:
- "1120% renewal increase" (documented case)
- "1% of company revenue" (customer quote)
- "$95,800 for 100 users" (vs $10K advertised)
- "$134K average annual cost" (industry data)
- "Domo disables any formulas in Excel files before export" (official docs)
- "Business users find it complicated" (competitive intelligence)
- "49 users mentioned high learning curve" (G2)
- "28 users find it expensive" (G2)

---

## 6. WIN CONDITIONS

**We Win When**:
1. **Renewal discussions** - 1120% increase story resonates
2. **Cost-conscious** - 27x price difference ($95,800 vs $3,588)
3. **Excel power users** - Formulas disabled creates gap
4. **Investigation needed** - Dashboard narration vs root cause analysis
5. **Small/mid-market** - "Not a target customer group" per reviews

**We Lose When**:
- Large enterprise specifically wants dashboard platform (#1 in Dresner)
- Company already invested heavily in Domo ecosystem (sunk cost)
- IT team comfortable with cards/datasets model
- Dashboard-first workflow is acceptable (not investigation-first)

---

## 7. COMPETITIVE POSITIONING

**Product Type Classification**:
- **What They Really Are**: Dashboard-first BI platform with bolt-on LLM (2010s architecture + 2024 AI layer)
- **What We Really Are**: AI data analyst with zero configuration
- **Their Primary Audience**: IT teams building dashboards for enterprise
- **Our Primary Audience**: Business users with Excel skills
- **Key Difference**: Dashboard-first + consumption pricing vs investigation-first + flat pricing

**One-Sentence Position**:
"Domo is a dashboard-first BI platform requiring portal login, IT-configured AI Readiness metadata, and consumption pricing ($95K-$134K annually with 1120% renewal increases), with Excel formulas disabled, while Scoop is an AI data analyst with zero configuration, native Excel/Slack/PowerPoint integration, costing $3,588 flat"

**Key Contrast**:
| Dimension | Domo | Scoop |
|-----------|------|-------|
| **Product Type** | Dashboard platform + LLM | AI data analyst |
| **Architecture** | Dashboard-first (2010s) | Investigation-first |
| **AI** | Bolt-on LLM (DomoGPT 2024) | Built for AI investigation |
| **Annual Cost (100 users)** | $95,800+ | $3,588 flat |
| **Excel** | Formulas disabled | 150+ functions |
| **PowerPoint** | Manual one-at-a-time | Automatic generation |
| **Slack** | Requires third-party | Native integration |
| **Investigation** | NL-to-SQL (single query) | Multi-pass (7+ queries) |
| **Pricing Model** | Consumption (unpredictable) | Flat (predictable) |

---

## 8. AVOID OVER-CLAIMING

**Don't Say**:
- "Domo has no AI" - *DomoGPT exists, focus on bolt-on vs native*
- "AI Chat requires dashboards" - *Can query datasets, but requires AI Readiness metadata*
- "No connectors" - *1000+ connectors exist, focus on configuration burden*

**Instead Say**:
- "Bolt-on LLM to 2010s dashboard platform, not built for AI investigation" - *Accurate*
- "DomoGPT quality depends on IT-configured AI Readiness metadata" - *Fair*
- "1000+ connectors but each requires configuration and maintenance" - *True*

---

## 9. DOMO-SPECIFIC INSIGHTS

### The Cards/Datasets Model
- Dashboard components ("cards") built on "datasets"
- Each dataset requires setup, transformation (Magic ETL), maintenance
- AI Chat works with datasets BUT quality depends on metadata
- Consumption pricing tied to cards/datasets usage
- Creates complexity: "Business users find it complicated"

### The DomoGPT Reality (2024)
- Announced as "AI Service Layer" with model flexibility
- Uses OpenAI as default, Amazon Bedrock models available
- Natural language to SQL but NOT multi-pass investigation
- Shows SQL transparency (users can see/edit)
- Still requires AI Readiness metadata for quality
- Hosted in Domo's AWS environment (security focus)

### The Consumption Pricing Trap
- "1% of revenue" model scales with company size
- Cards/datasets usage drives costs unpredictably
- Renewal shock: "1120% increase" documented
- Small businesses: "Not a target customer group"
- Hidden costs: Query-based pricing includes system processes

### The Portal Dependency
- Dashboard-first architecture = portal-first workflow
- AI Chat doesn't escape portal (must log in)
- Excel plugin exists but formulas disabled "for security"
- No native Slack (requires Workato/n8n custom)
- PowerPoint add-in requires manual visual insertion

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