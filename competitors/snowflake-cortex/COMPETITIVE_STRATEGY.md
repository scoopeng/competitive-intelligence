# Competitive Strategy: Snowflake Cortex

**Last Updated**: November 18, 2025
**Maintained By**: Human (strategic positioning decisions)
**Used By**: web_comparison generation, battle card generation, sales enablement

---

## 1. PRIMARY WEAKNESSES (Rank Top 3)

**#1: Context Blindness (Generic AI)** (Severity: Critical | Defensibility: Architectural)
- **Evidence**: BUA Understanding 2/20 (0/8 Agentic Investigation, 0/6 Explainable ML). Cortex is a generic LLM wrapper that guesses SQL based on schema names.
- **Why It Matters**: It doesn't know your business logic. It guesses "Churn" based on a column name, not your specific definition (e.g., "Churn = cancelled AND tenure > 90 days"). This leads to hallucinations and lack of trust.
- **Our Advantage**: **Domain Intelligence** (Schema v2.8) encodes your expert rules explicitly. We don't guess; we follow your defined logic.
- **Defensibility**: Architectural. Cortex is designed to be "zero-shot" (generic). Scoop is designed to be "encoded" (specific).
- **Emphasis Level**: 35% of web comparison

**#2: Statelessness & Lack of Autonomy** (Severity: Critical | Defensibility: Architectural)
- **Evidence**: BUA Investigation 0/8. Cortex is single-query ("stateless"). It cannot plan a multi-step investigation.
- **Why It Matters**: You ask "Why did margin drop?" Cortex returns a SQL query for the current margin. It cannot autonomously drill down, checking mix, pricing, and inventory in sequence. It waits for you to ask the next question.
- **Our Advantage**: The **Investigation Coordinator**. A 15-module state machine that plans and executes multi-step investigations autonomously.
- **Defensibility**: Architectural. Cortex lacks a state machine; it's just a text-to-SQL translator.
- **Emphasis Level**: 30% of web comparison

**#3: Portal Prison & No Mobile** (Severity: High | Defensibility: Strategic)
- **Evidence**: BUA Flow 2/20. 0/8 Native Integration.
- **Why It Matters**: Executives don't log into Snowflake consoles. They need answers in Slack/Excel.
- **Our Advantage**: Native integration where users work.
- **Defensibility**: Strategic. Snowflake wants you in their console.
- **Emphasis Level**: 20% of web comparison

---

## 2. KEY SCENARIOS (Stories that expose weaknesses)

**Scenario 1: The "Why" Question (Investigation vs Query)**
- **When to Use**: Against the "Text-to-SQL" pitch.
- **Story**: "VP asks 'Why did revenue miss?' Cortex generates a SQL query to show the revenue number (The 'What'). Scoop runs a 7-step investigation to find that a pricing error in the West region caused the drop (The 'Why')."
- **Expected Impact**: Exposes the "Intelligence Ceiling" of generic tools.

**Scenario 2: Mobile Executive Question**
- **When to Use**: Against the "Console-only" limitation.
- **Story**: "CEO texts at 9 PM: 'Cash position?' Cortex needs desktop + VPN. Scoop answers in 30s via Slack mobile."
- **Expected Impact**: Shows Cortex is for engineers, Scoop is for executives.

**Scenario 3: The Hallucination Risk**
- **When to Use**: Trust discussions.
- **Story**: "Ask Cortex for 'Active Users.' It guesses based on table names. Ask Scoop. It uses the exact formula defined in your JSON schema (Active = Login < 7 days + > 1 Action)."
- **Expected Impact**: proves the value of Encoded Expertise vs Generic Guessing.

---

## 3. TALKING POINTS (Emphasis hierarchy)

**Lead With** (Most important - first 1000 words):
1. **"Encoded Expertise vs Generic Guessing"** (Context Blindness) - *Because they guess SQL, we follow rules.*
2. **"Active Investigation vs Passive Querying"** (Autonomy) - *Because they wait for prompts, we wake you up with answers.*
3. **"Business User Autonomy"** (BUA Score) - *Because they score 26/100, we score 82/100.*

**Always Mention**:
4. **Investigation Coordinator** (The "Brain" that makes us autonomous)
5. **Schema v2.8** (The "Memory" that stores context)
6. **30-second setup** (vs weeks of modeling)

**De-Emphasize**:
- **Cost** (TCO is the closer, not the opener)

---

## 4. CONTENT DISTRIBUTION (Word allocation for 7,500-word comparison)

**Recommended Mix**:
- **Section 1 (Executive Summary)**: 10%
- **Section 2 (Capabilities)**: 60%
  - **Investigation/Context**: 35% (Attack Context Blindness)
  - **Autonomy/Flow**: 25% (Attack Statelessness)
- **Section 3 (Cost/TCO)**: 20% (Cost Elimination)
- **Section 4 (Use Cases)**: 10%

**Rationale**:
Cortex is a "Smart Guesser." We must prove it doesn't understand the business (Context Blindness) and cannot act on its own (Lack of Autonomy).

---

## 5. PROOF POINTS (Evidence to cite)

**From Framework Scoring** (`evidence/framework_scoring.md`):
- **BUA Total**: 26/100 (Category C - Weak)
- **Understanding**: 4/20 (0/8 Investigation) - *Critical Proof of Statelessness*
- **Flow**: 2/20 (0/8 Native Integration)

**From Research**:
- "Actual statement count 3 did not match... 1" - *Proof of single-query limitation.*
- "35% business correctness rate" - *Proof of context blindness.*

---

## 6. WIN CONDITIONS (What makes us win)

**We Win When**:
1. **Accuracy Matters**: They need deterministic answers, not probabilistic guesses.
2. **"Why" Matters**: They need root cause analysis, not just data retrieval.
3. **Mobile/Speed Matters**: They need answers in Slack/Excel, not a console.

**We Lose When**:
- The goal is just "Help Data Engineers write SQL faster." (Cortex is good at this).

---

## 7. COMPETITIVE POSITIONING

**Product Type Classification**:
- **What They Really Are**: Generic LLM Wrapper / SQL Generation Tool
- **What We Really Are**: Domain Intelligence Platform

**One-Sentence Position**:
"Snowflake Cortex is a generic LLM wrapper that guesses SQL; Scoop is a Domain Intelligence Platform that investigates using your encoded expertise."

**Elevator Pitch**:
"Snowflake Cortex uses generic AI to guess SQL queries. It doesn't know your business definitions and can't plan multi-step investigations. Scoop encodes your executive expertise into a Domain Intelligence system. It doesn't guess; it investigates autonomously using your specific rules, finding root causes while you sleep."

**Key Contrast**:
| Dimension | Snowflake Cortex | Scoop |
|-----------|------------------|-------|
| **Product Type** | Generic LLM Wrapper | Domain Intelligence Platform |
| **Logic Source** | Training Data (Guesses) | Encoded Schema (Rules) |
| **Mechanism** | Text-to-SQL (Single Shot) | Investigation Coordinator (Multi-Step) |
| **Autonomy** | Reactive (Waits for prompt) | Proactive (Wakes you up) |

---

## 8. AVOID OVER-CLAIMING

**Don't Say**:
- "Cortex has no AI" - *It has LLMs, they are just generic and stateless.*

**Instead Say**:
- "Cortex suffers from Context Blindness - it doesn't know your specific business rules."

---

## 9. CUSTOM CONTENT BLOCKS

### Example 1: The Investigation vs. Query Gap

**Setup**: User asks "Why did revenue miss?"

**Snowflake Cortex Response (The Query)**:
```
Query: SELECT revenue FROM sales WHERE date = 'Q3'
Result: .2M
Context: None. It answered the "What" but ignored the "Why".
Action Required: User must manually ask "Show me breakdown by region", "Show me breakdown by product", etc.
```

**Scoop Response (The Investigation)**:
```
1. Detected Revenue Miss (-10%)
2. Drilled by Region -> Found West is down 40%
3. Drilled by Product in West -> Found Widget A is down
4. Checked Inventory -> Found Stockout
Result: "Revenue missed by 10% primarily due to Widget A stockouts in the West region."
```

**Business Impact**: Cortex gives you data labor. Scoop gives you executive answers.

---