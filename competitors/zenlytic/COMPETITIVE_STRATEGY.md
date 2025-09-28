# Competitive Strategy: Zenlytic

**Last Updated**: September 28, 2025
**Maintained By**: Human (strategic positioning decisions)
**Used By**: web_comparison generation, battle card generation, sales enablement

---

## 1. PRIMARY WEAKNESSES (Rank Top 3)

**#1: YAML Semantic Layer Dependency** (Severity: Critical | Defensibility: Architectural)
- **Evidence**: BUA Setup 4/8, Questions 4/6. "Maintainers maintain metric definitions in YAML files" (Zenlytic docs). GitHub repository required for version control. 75-80% automated setup still requires YAML configuration. CEO admits "90% accuracy is absolutely terrible" and "self-service analytics is not there yet."
- **Why It Matters**: Like Snowflake Cortex, requires IT to define semantic layer in YAML before business users can query. "Cognitive layer" is just semantic layer + LLM text-to-SQL. Schema changes require YAML updates and GitHub commits. Not true self-service.
- **Our Advantage**: Scoop requires zero data modeling. No YAML files, no GitHub repos, no semantic layer maintenance. 30 seconds to start asking questions.
- **Defensibility**: Architectural—text-to-SQL approach requires semantic layer to map natural language correctly. "Cognitive layer" doesn't eliminate this requirement.
- **Emphasis Level**: 30% of web comparison

**#2: No Native Tool Integration** (Severity: Critical | Defensibility: Strategic)
- **Evidence**: BUA Flow 4/20 (Native Integration 0/8, Portal Prison 0/6). NO Excel integration, NO PowerPoint, NO mobile apps (iOS/Android). Web platform only. Positions as "Excel replacement" not integration.
- **Why It Matters**: Business users trapped in Zenlytic web portal. Cannot work in Excel with formulas. No PowerPoint generation. No mobile access. Must context-switch away from existing workflows.
- **Our Advantage**: Scoop native in Slack, Excel (150+ formulas), automatic PowerPoint, mobile via Slack. Work where you already work.
- **Defensibility**: Strategic—chose web-first approach over native tool integration. Could add but hasn't prioritized.
- **Emphasis Level**: 25% of web comparison

**#3: Text-to-SQL Architecture (One Query Per Question)** (Severity: High | Defensibility: Architectural)
- **Evidence**: BUA Investigation 4/8. Text-to-SQL with "Zoë" AI assistant. CEO admits accuracy issues. Cannot do multi-pass investigation—each question generates one SQL query.
- **Why It Matters**: Like Snowflake, can answer "what" questions but cannot investigate "why" with multiple automated queries. Cannot test hypotheses, run 7+ queries for root cause analysis.
- **Our Advantage**: Scoop's multi-pass investigation (3-10 automated queries), hypothesis testing, ML validation. Built for "why" questions.
- **Defensibility**: Architectural—text-to-SQL systems generate one query per question. Multi-pass investigation requires reasoning engine.
- **Emphasis Level**: 20% of web comparison

---

## 2. KEY SCENARIOS

**Scenario 1: The YAML Bottleneck**
- **When to Use**: IT dependency and time-to-value discussions
- **Story**: "Business user needs to analyze new data source. Zenlytic: IT defines YAML semantic layer, commits to GitHub, configures mappings (days). Scoop: Connect data source (30 seconds), start asking questions immediately."
- **Expected Impact**: YAML requirement perpetuates IT gatekeeping like Snowflake.

**Scenario 2: Excel Power User Blocked**
- **When to Use**: When prospect has Excel-heavy workflows
- **Story**: "Business analyst needs VLOOKUP to match customer data. Zenlytic positions as 'Excel replacement'—forces web portal, zero formula support. Scoop: Use VLOOKUP natively in Excel with 150+ other functions. Don't replace Excel, enhance it."
- **Expected Impact**: Excel replacement is non-starter for Excel power users.

**Scenario 3: CEO's Own Admission**
- **When to Use**: When discussing accuracy and readiness
- **Story**: "Zenlytic CEO publicly states '90% accuracy is absolutely terrible' and 'self-service analytics is not there yet.' That's honest but concerning. Scoop: Deterministic results with ML confidence scoring. Production-ready, not aspirational."
- **Expected Impact**: CEO's own words validate concerns about maturity.

---

## 3. TALKING POINTS

**Lead With**:
1. **"YAML semantic layer like Snowflake"** - *Because requires IT to maintain metric definitions in YAML files*
2. **"Web-only portal prison"** - *Because zero Excel/PowerPoint/mobile integration*
3. **"Text-to-SQL not investigation"** - *Because one query per question, no multi-pass*

**Always Mention**:
4. **CEO accuracy admission** (90% terrible, not ready)
5. **Excel replacement vs integration** (replace vs enhance)
6. **30-second setup** (vs days of YAML configuration)

**De-Emphasize**:
- **75-80% automated setup** (still requires YAML, acknowledge automation)
- **Conversational interface** (they have Zoë AI assistant, focus on architecture)

---

## 4. CONTENT DISTRIBUTION

**Recommended Mix**:
- **YAML Semantic Layer**: 30% (~2,250 words)
- **No Native Tools**: 25% (~1,875 words)
- **Text-to-SQL vs Investigation**: 20% (~1,500 words)
- **Setup & Maintenance**: 15% (~1,125 words)
- **Cost/Accuracy**: 10% (~750 words)

**Rationale**: YAML requirement is architectural like Snowflake. Portal prison is complete (0/8 native integration). Text-to-SQL limitation prevents investigation.

---

## 5. PROOF POINTS

**From Framework Scoring**:
- **BUA Total**: 42/100 (Category C - Moderate)
- **Native Integration**: 0/8
- **Portal Prison**: 0/6
- **Setup**: 4/8 (better than Snowflake due to automation, but YAML still required)
- **Investigation**: 4/8 (text-to-SQL limitation)

**From Research**:
- "Maintainers maintain metric definitions in YAML files" (Zenlytic docs)
- "90% accuracy is absolutely terrible" (CEO quote)
- "Self-service analytics is not there yet" (CEO quote)
- "NO Excel integration or export found" (Phase 2)
- "NO PowerPoint integration" (Phase 2)
- "NO mobile apps exist for iOS/Android" (Phase 3)

---

## 6. WIN CONDITIONS

**We Win When**:
1. **Excel power users** - They force web portal, we enhance Excel natively
2. **No YAML tolerance** - They require IT semantic layer, we need zero modeling
3. **Multi-pass investigation needed** - They do text-to-SQL, we do automated investigation
4. **Mobile access required** - They have no mobile apps, we have Slack mobile
5. **PowerPoint critical** - They have none, we generate automatically

**We Lose When**:
- Company wants to replace Excel entirely (not enhance)
- Technical users comfortable with YAML/GitHub workflows
- dbt/Looker semantic layers already exist (they can import)

---

## 7. COMPETITIVE POSITIONING

**Product Type Classification**:
- **What They Really Are**: Text-to-SQL platform with YAML semantic layer (Snowflake-like architecture, web UI)
- **What We Really Are**: AI data analyst with zero configuration
- **Their Primary Audience**: Technical analysts comfortable with YAML
- **Our Primary Audience**: Business users with Excel skills
- **Key Difference**: YAML semantic layer vs adaptive query generation

**One-Sentence Position**:
"Zenlytic is a text-to-SQL platform requiring YAML semantic layer configuration with web-only access, Scoop is an AI data analyst with zero configuration and native Excel/Slack/PowerPoint integration"

**Key Contrast**:
| Dimension | Zenlytic | Scoop |
|-----------|----------|-------|
| **Product Type** | Text-to-SQL with YAML layer | AI data analyst |
| **Setup** | Days (YAML + GitHub) | 30 seconds |
| **Excel** | NO (positions as replacement) | YES (150+ formulas) |
| **PowerPoint** | NO | Automatic generation |
| **Mobile** | NO | Slack mobile native |
| **Investigation** | Text-to-SQL (one query) | Multi-pass (7+ queries) |
| **Semantic Layer** | YAML required | Zero configuration |

---

## 8. AVOID OVER-CLAIMING

**Don't Say**:
- "Zenlytic has no NL interface" - *They have Zoë conversational AI*
- "Zero automation" - *75-80% automated setup is real*
- "No dbt integration" - *They can import dbt/Looker definitions*

**Instead Say**:
- "Text-to-SQL architecture with YAML semantic layer requirement" - *Accurate*
- "75-80% automated setup still requires YAML configuration" - *Fair*
- "CEO admits '90% accuracy is absolutely terrible'" - *His own words*

---

## MAINTENANCE SCHEDULE

**Quarterly Review**:
- [ ] Check if YAML requirement eliminated
- [ ] Verify Excel/PowerPoint integration status
- [ ] Review mobile app launches
- [ ] Update CEO statements on accuracy/readiness

**Version History**:
- 2025-09-28: Initial version based on BUA 42/100. YAML semantic layer (30%), no native tools (25%), text-to-SQL architecture (20%).

---

**Template Version**: 1.1
**Created**: September 28, 2025
**Competitor BUA Score**: 42/100 (Category C - Moderate)