# Domain Intelligence Framework
**The Technical & Strategic Foundation of Scoop Analytics**
*Based on Schema v2.8 and Investigation Coordinator v5.0*

## 1. Definition
**Domain Intelligence** is the systematic encoding of executive expertise into a hierarchical JSON structure that enables autonomous, context-aware investigation. Unlike "Generic AI" (LLMs) that rely on training data and probability, Domain Intelligence relies on explicit, deterministic business rules, patterns, and definitions captured from domain experts.

## 2. The Core Technology: Investigation Coordinator (IC)
The IC is the "brain" of the system, a deterministic state machine that orchestrates investigations using a 3-tier methodology:

*   **Tier 1: Display (What?)** - Retrieves current state data (`DATASET` queries).
*   **Tier 2: Diagnose (Why?)** - Drills down using `ML_GROUP`, `ML_PERIOD`, and `ML_RELATIONSHIP` queries. It applies encoded **Patterns** to detect anomalies.
*   **Tier 3: Decide (Now What?)** - Synthesizes findings into actionable recommendations using `ML` queries.

## 3. The Knowledge Graph: Hierarchical JSON Schema (v2.8)
Expertise is not "trained" into a model; it is **configured** in a structured schema stored in S3. This ensures 100% determinism and zero hallucination for business logic.

### Key Components:
*   **Contexts**: Bounded domains of inquiry (e.g., "Loan Operations", "Inventory Health"). Prevents AI from drifting.
*   **Definitions**: Business terms with precise Excel-like formulas (e.g., `'Revenue' / 'Loan Count'`). These act as "Virtual Metrics" created on-the-fly.
*   **Patterns**: explicit detection expressions (e.g., `IF(sales < AVG(sales), 1, 0)`) that trigger investigations.
*   **Spawn Guidance**: Rules that dictate how to drill down (e.g., "If 'High Defaults' pattern found, drill by [Store, Generation] using `worst_first` strategy").

## 4. The "Encoding" Process (The Moat)
We do not "connect and query." We **encode and scale**.
1.  **Discovery**: 4-hour session with senior executives (COO, VP Ops).
2.  **Capture**: Record their "mental model" - what patterns they look for, what thresholds matter.
3.  **Configuration**: Translate this mental model into the JSON Schema (Patterns, Definitions, Contexts).
4.  **Deployment**: The system now "thinks" like that executive, 24/7, across all data.

## 5. Strategic Differentiation

| Feature | **Generic AI (Copilots)** | **Traditional BI (Dashboards)** | **Scoop Domain Intelligence** |
| :--- | :--- | :--- | :--- |
| **Core Function** | Text-to-SQL Generation | Data Visualization | **Autonomous Investigation** |
| **Context** | None / Generic Training | None / Static Metadata | **Deeply Encoded (JSON)** |
| **Reliability** | Probabilistic (Hallucinates) | Deterministic (Accurate) | **Deterministic Logic + AI Synthesis** |
| **User Mode** | Reactive (Wait for questions) | Reactive (Wait for clicks) | **Proactive (Wakes you up)** |
| **Setup** | "Connect Data" | "Build Dashboards" | **"Encode Expertise"** |

## 6. The "Uncopyable" Advantage
Competitors can copy "Text-to-SQL." They cannot copy the **accumulated learning history** of a specific business.
*   As users correct the system ("No, 'Churn' means X, not Y"), the **Feedback System** updates the JSON schema.
*   The system gets smarter about *that specific client's business* every day.
*   This creates a sticky, compounding asset that generic models can never replicate.

## 7. The Proof: Mapping Architecture to BUA Scores
We use the **Business User Empowerment (BUA) Framework** (`BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md`) to quantify value. Domain Intelligence is the only architecture capable of hitting the "Elite" (85+) category because its components map directly to the hardest scoring rubrics.

### A. The "Understanding" Dimension (20 Points)
**The BUA Rubric**: To score **8/8 on Agentic Investigation Depth**, a system must demonstrate *"Automatic multi-round investigation with probe dependencies"* and *"Hypothesis testing without user prompting."*

**The Domain Intelligence Solution**:
*   **Hypothesis Testing** = `detection_expression` (JSON Schema v2.8)
    *   *How it works:* We explicitly code hypotheses (e.g., `IF(sales < AVG(sales))`) into the schema. The system tests these on every dataset, automatically.
*   **Probe Dependencies** = `spawn_config` & `drill_dimensions`
    *   *How it works:* When a pattern is detected, the `Investigation Coordinator` state machine uses the `spawn_guidance` to determine the next query. It passes the *context* of the first finding (e.g., "West Region") into the filters of the second query. This is the "dependency" the rubric demands.
*   **Result**: Scoop scores 8/8. Snowflake Cortex scores 2/8 (Stateless/Single-Shot).

### B. The "Data" Dimension (20 Points)
**The BUA Rubric**: To score **8/8 on Schema Evolution**, a system must show *"Complete automatic adaptation, zero downtime"* when columns change.

**The Domain Intelligence Solution**:
*   **Adaptation** = **Virtual Metric Layer** (`definitions.json`)
    *   *How it works:* Business definitions (e.g., "Churn") are defined by formulas, not rigid table references. If the underlying table schema changes, Scoop's **Smart Scanner** re-maps the physical columns, but the `definition` (the business logic) remains untouched.
*   **Result**: Scoop scores 6-8/8. Power BI Semantic Models break and require IT intervention (Score 0/8).

### C. The "Autonomy" Dimension (20 Points)
**The BUA Rubric**: To score **8/8 on Self-Service Setup**, a user must achieve value in *"Minutes"* with *"Zero IT involvement."*

**The Domain Intelligence Solution**:
*   **Instant Value** = **Pre-Built Contexts**
    *   *How it works:* While custom encoding takes 4 hours, Scoop ships with "Base Contexts" (Retail, SaaS, Finance) in the `investigation-coordinator` library. A user connects data, and the system immediately applies these standard patterns.
*   **Result**: Scoop scores 18/20 total. Traditional BI requires weeks of modeling (Score 4/20).

### D. The "Generic AI" Failure Mode
Generic LLMs (Copilots) fail the BUA framework because they lack a **State Machine**.
*   They can generate SQL (Tier 1).
*   But without an `Investigation Coordinator` (State Machine), they cannot "plan" a multi-step investigation.
*   They are **stateless**. They don't know that Query 2 depends on the anomaly found in Query 1.
*   Therefore, they are mathematically capped at a low "Understanding" score (max 2/8).
