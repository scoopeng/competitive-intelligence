# Competitive Strategy: Power BI Copilot

**Last Updated**: November 18, 2025
**Maintained By**: Human (strategic positioning decisions)
**Used By**: web_comparison generation, battle card generation, sales enablement

---

## 1. PRIMARY WEAKNESSES (Rank Top 3)

**#1: Stateless Query Engine vs. Autonomous Investigator** (Severity: Critical | Defensibility: Architectural)
- **Evidence**: BUA Investigation 0/8. Microsoft docs admit "Copilot doesn't answer follow-up questions" and "Can't currently answer questions that require generating new insights." It is a stateless text-to-DAX generator.
- **Why It Matters**: It cannot investigate "why." It can only answer "what." It generates a single query per question and forgets the context immediately. It lacks a state machine to orchestrate multi-step problem solving.
- **Our Advantage**: **Investigation Coordinator**. A 15-module state machine that executes a multi-step "Display-Diagnose-Decide" workflow autonomously.
- **Defensibility**: Architectural. They are building a query assistant; we are building an analytical application platform.
- **Emphasis Level**: 35% of web comparison

**#2: Architectural Dependency & Cost** (Severity: High | Defensibility: Strategic)
- **Evidence**: BUA Setup 2/8. Requires F64 capacity ($67K/year minimum) + Semantic Model creation (weeks/months). Business users are blocked until IT builds the model and provisions the capacity.
- **Why It Matters**: High barrier to entry. You pay a "tax" before you get a single answer. The model is rigid; changes require IT intervention.
- **Our Advantage**: Zero infrastructure tax. **Schema Evolution** (v2.8) adapts automatically. 30-second setup.
- **Defensibility**: Strategic. Microsoft's model depends on selling Azure capacity (Fabric).
- **Emphasis Level**: 30% of web comparison

**#3: Context Blindness & Reliability** (Severity: High | Defensibility: Intrinsic to LLMs)
- **Evidence**: "Nondeterministic behavior" admission. Gartner: 53% cite "inaccurate results." It guesses DAX based on schema names, lacking deep business context.
- **Why It Matters**: Inconsistent answers destroy trust. "Why did revenue drop?" yields different answers on different days.
- **Our Advantage**: **Encoded Expertise**. We use your specific business rules defined in the schema (`definitions.json`). Deterministic execution.
- **Defensibility**: Intrinsic. Generic LLMs guess; Domain Intelligence Systems follow rules.
- **Emphasis Level**: 25% of web comparison

---

## 2. KEY SCENARIOS (Stories that expose weaknesses)

**Scenario 1: The "Why" Question (Investigation vs Query)**
- **When to Use**: Against the "AI Assistant" pitch.
- **Story**: "Ask Copilot 'Why is pipeline down?'. It generates a DAX query to show the pipeline number. It stops there. Ask Scoop. Our **Investigation Coordinator** tests 7 hypotheses (Rep productivity, Lead quality, Seasonality), finds the root cause (New reps ramping slowly), and proposes an action plan."
- **Expected Impact**: Exposes the difference between a "Chatbot" and a "Domain Intelligence Platform."

**Scenario 2: The $67K Barrier**
- **When to Use**: When discussing TCO and agility.
- **Story**: "To answer your first question with Copilot, you need an F64 capacity ($67K/year) and a semantic model (weeks of IT). With Scoop, you connect your data and get answers in 30 seconds. We eliminate the infrastructure tax entirely."
- **Expected Impact**: Highlights the massive efficiency gap.

**Scenario 3: The Complex "What" (Subquery Generation)**
- **When to Use**: When discussing analytical depth.
- **Story**: "Ask 'Show opportunities from top 5 reps by win rate.' Copilot fails because it requires complex subqueries (calculate rate -> rank -> filter). It needs IT to build a custom DAX measure. Scoop's engine generates the necessary subqueries automatically."
- **Expected Impact**: Proves Scoop is a more capable analytical engine, not just a chat interface.

---

## 3. TALKING POINTS (Emphasis hierarchy)

**Lead With** (Most important - first 1000 words):
1.  **"Encoded Expertise vs Generic LLM Wrapper"** - *They guess DAX; we follow your business rules.*
2.  **"Autonomous Investigator vs Stateless Query Engine"** - *They answer one question; we solve the problem.*
3.  **"Eliminated Labor vs Infrastructure Tax"** - *We remove the work; they add to the bill.*

**Always Mention**:
4.  **Investigation Coordinator** (The architectural differentiator)
5.  **Schema v2.8** (The context engine)
6.  **Deterministic Reliability** (Trust)

**De-Emphasize** (Minor mentions only):
- **Microsoft ecosystem** (Power BI has strong MS integration, don't pretend it doesn't)
- **Enterprise governance** (they have good RLS/governance features)
- **Teams integration** (We have Slack, they have Teams; it's a wash).

---

## 4. CONTENT DISTRIBUTION (Word allocation for 7,500-word comparison)

**Recommended Mix**:
- **Section 1 (Executive Summary)**: 10%
- **Section 2 (Capabilities)**: 60%
    - **Investigation/Autonomy**: 35% (The core differentiator)
    - **Architecture/Cost**: 25% (The efficiency argument)
- **Section 3 (Reliability/Trust)**: 20% (The "Nondeterministic" weakness)
- **Section 4 (Use Cases)**: 10%

**Rationale**:
Power BI Copilot is the quintessential "Generic AI" product. We must contrast our "Domain Intelligence" architecture against their "LLM Wrapper" limitations.

---

## 5. PROOF POINTS (Evidence to cite)

**From Framework Scoring** (`evidence/framework_scoring.md`):
- **BUA Investigation**: 0/8 (Stateless)
- **BUA Setup**: 2/8 (F64 + Semantic Model)
- **Reliability**: "Nondeterministic" (Microsoft admission)

**From Research**:
- "Copilot doesn't answer follow-up questions" - Microsoft Docs
- "Can't currently answer questions that require generating new insights" - Microsoft Docs

---

## 6. WIN CONDITIONS (What makes us win)

**We Win When**:
1.  **The user needs "Why"**: Root cause analysis is required.
2.  **Speed matters**: They can't wait weeks for semantic models.
3.  **Cost matters**: The $67K starting price is a barrier.
4.  **Accuracy matters**: They need deterministic answers.

**We Lose When**:
- The organization is 100% committed to the Microsoft ecosystem regardless of capability gaps.
- The primary need is just simple dashboard generation (Copilot is okay at this).

---

## 7. COMPETITIVE POSITIONING

**One-Sentence Position**:
"Power BI Copilot is a stateless DAX generator for analysts; Scoop is a Domain Intelligence Platform that autonomously investigates business problems for executives."

**Elevator Pitch** (30 seconds):
"Power BI Copilot is designed to help analysts write DAX code faster. It requires expensive capacity ($67K/year) and rigid semantic models. It answers 'what' but cannot investigate 'why' because it is stateless. Scoop is a Domain Intelligence Platform. It encodes your expertise, adapts to data changes instantly, and uses an Investigation Coordinator to autonomously find root causes and actionable insights. We don't just generate queries; we solve business problems."

**Key Contrast**:
| Dimension | Power BI Copilot | Scoop |
|-----------|------------------|-------|
| **Product Type** | Generic LLM Wrapper / DAX Generator | Domain Intelligence Platform |
| **Core Mechanism** | Stateless Text-to-DAX | Investigation Coordinator (State Machine) |
| **Context** | Blind (Guesses based on names) | Encoded (Uses Schema v2.8 Rules) |
| **Infrastructure** | Heavy ($67K/year F64) | Zero (SaaS) |
| **Reliability** | Nondeterministic | Deterministic |

---

## 8. AVOID OVER-CLAIMING (Credibility guardrails)

**Don't Say** (Risks credibility):
- "Copilot creates fake data" - *It creates nondeterministic answers, which is different.*
- "Microsoft can't do AI" - *They have great AI, but this specific product implementation is limited by its architecture.*

**Instead Say** (Evidence-based alternatives):
- "Copilot is nondeterministic by design, which creates risk for decision making."
- "Copilot is stateless, meaning it cannot conduct multi-step investigations."

---

## 9. CUSTOM CONTENT BLOCKS (Competitor-specific examples)

### Example 1: The Investigation Gap

**User**: "Why is margin declining?"

**Power BI Copilot**:
- **Action**: Generates DAX for `SUM(Margin)`.
- **Result**: "Margin is 12%."
- **Next Step**: User must ask "Check costs", "Check pricing", "Check mix".
- **Outcome**: User does the work.

**Scoop**:
- **Action**: **Investigation Coordinator** triggers.
- **Step 1**: Identifies decline.
- **Step 2**: Drills into Cost Components (via Schema).
- **Step 3**: Identifies "Raw Material Surge".
- **Step 4**: Checks Supplier pricing.
- **Result**: "Margin declined due to 15% hike in steel prices from Supplier X."
- **Outcome**: Scoop does the work.

---
