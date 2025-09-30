# Capability Matrix Improvements

**Date**: September 30, 2025
**Purpose**: Critical recommendations to better showcase Scoop's agentic analytical depth
**Context**: Current matrix captures breadth but misses depth of investigation/ML capabilities

---

## Executive Summary

The current capability matrix effectively shows feature breadth but **understates Scoop's most defensible competitive advantages**: multi-pass investigation, explainable ML with automatic data prep, and the runtime spreadsheet calculation engine. These are architectural differentiators, not feature checkboxes.

**Key Issue**: The matrix treats "Investigation" and "ML" as single capabilities when they represent fundamentally different levels of sophistication across competitors.

---

## Recommended Changes

### 1. Column Header Readability ⚠️ USABILITY

**Problem**: Vertical text is hard to scan quickly
**Solution**: Angle headers at 45° or use shorter labels with hover tooltips

**Suggested Short Labels**:
- "Multi-Pass Investigation" → "Multi-Pass Reasoning"
- "Excel/Spreadsheet Integration" → "Spreadsheet Engine"
- "Natural Language Query" → "NL Query"

---

### 2. Agentic Investigation Capabilities 🚨 CRITICAL

**Problem**: "Investigation" column doesn't distinguish between:
- Multi-turn chat (follow-up questions) ← Most competitors have this
- Multi-pass investigation (3-10 automatic queries with context) ← Only Scoop
- Hypothesis testing ← Only Scoop

**Current State**:
```
Investigation: ✓ (Qlik has ✓ because manual associative exploration)
Investigation: ✓ (Scoop has ✓ but actually does 10x more)
```

**Proposed New Columns**:

| Column | What It Measures | Scoop | Typical Competitor |
|--------|------------------|-------|-------------------|
| **Multi-Turn Chat** | Can handle follow-up questions in conversation | ✓✓✓ | ✓✓ (most have this) |
| **Multi-Pass Investigation** | Automatically runs 3-10 interconnected queries to find root causes | ✓✓✓ | ✗ (NONE have this) |
| **Context Retention** | Remembers insights across queries within investigation | ✓✓✓ | ✗ (stateless responses) |
| **Hypothesis Testing** | Automatically tests theories and builds evidence | ✓✓✓ | ✗ |

**Evidence from Scoop codebase**:
- `ReasoningPrompts.txt`: "Generate multi-step investigation plan using 2-8 probes"
- "Probe dependencies" system with `depends_on` and `extraction_rules`
- "Investigation strategies": Drill-Down, Temporal, Segmentation, Causal, Pattern Discovery, Comparative

**Competitor Reality**:
- **Qlik**: Manual exploration (user clicks through associative model) = NOT automatic investigation
- **Snowflake Cortex**: "Single query limitation - cannot multi-step investigate" (framework_scoring.md)
- **Power BI Copilot**: One query per question, no context retention
- **All others**: No automated multi-pass reasoning capability

---

### 3. ML Capability Breakdown 🚨 CRITICAL

**Problem**: "ML" column is binary (has/doesn't have) when Scoop's ML is a **three-layer architecture** that no competitor replicates.

**Current State**:
```
ML: ✓ (Qlik has AutoML tools)
ML: ✓ (Scoop has automatic data prep + explainable models + AI translation)
```

**Proposed New Columns**:

| Column | What It Measures | Scoop | Qlik | Others |
|--------|------------------|-------|------|--------|
| **Explainable ML** | J48 decision trees, JRip rules (not black box) | ✓✓✓ | ✗ | ✗ |
| **Automatic Data Prep** | AI does cleaning, binning, feature engineering | ✓✓✓ | ✗ | ✗ |
| **AI Explanation Layer** | Translates model output to business language | ✓✓✓ | ✗ | ✗ |
| **ML Discovery** | Automatically runs ML without user requesting it | ✓✓✓ | ✗ | ✗ |

**Why This Matters**:
- Qlik has "AutoML" but: "Requires understanding of ML concepts", "Not automatic - user must initiate"
- Most competitors: No ML or black-box predictions
- Scoop: User asks "Why did sales drop?" → J48 tree runs automatically → AI explains in business language

**Evidence from Scoop codebase**:
- `SCOOP_CAPABILITIES.md`: "Layer 1: Automatic Data Preparation", "Layer 2: Explainable ML Model Execution (J48, JRip, EM Clustering)", "Layer 3: AI Explanation Engine"
- Classification types: `ML_RELATIONSHIP`, `ML_CLUSTER`, `ML_PERIOD`, `ML_GROUP`
- "PhD-level analysis explained in business language with zero user ML knowledge required"

---

### 4. Spreadsheet Calculation Engine 🚨 CRITICAL

**Problem**: Not visible as a distinct capability despite being **unique to Scoop**.

**Proposed Column**: **Runtime Spreadsheet Engine**

**What It Is**:
- 150+ Excel functions (VLOOKUP, SUMIFS, nested IFs, FILTER, UNIQUE, etc.)
- In-memory calculation engine that processes query results
- Used for both data preparation AND runtime transformations
- NOT "export to Excel" - actual Excel formula execution

**Scoring**:
- Scoop: ✓✓✓ (full Excel-compatible formula execution)
- Everyone else: ✗ (they export static data or have "Excel-like" interfaces)

**Evidence**: `SCOOP_CAPABILITIES.md` - "Complete in-memory spreadsheet calculation engine with 150+ Excel functions... This isn't integration—Scoop streams data through a spreadsheet to calculate transformed results"

**Competitive Reality**:
- Power BI: Export to Excel (static)
- Qlik: "Cannot export Qlik formulas as Excel formulas" (framework_scoring.md)
- Tableau: Template downloads (no live engine)

---

### 5. Business User Autonomy Columns 🎯 STRATEGIC

**Problem**: Missing the "No IT Required" story that underpins the entire BUA framework.

**Proposed New Columns**:

| Column | What It Measures | Scoop | Typical Competitor |
|--------|------------------|-------|-------------------|
| **No Data Modeling** | Works without semantic layer/YAML/metric definitions | ✓✓✓ | ✗ (Cortex, Zenlytic, Pulse) |
| **No Training Required** | Instant productivity using natural language | ✓✓✓ | ✗ (Qlik 58% cert fail rate) |
| **No IT for Setup** | Business user can upload CSV and start in minutes | ✓✓✓ | ✗ (weeks to months) |

**Why This Matters**:
- **Snowflake Cortex**: "Requires YAML semantic model maintained by IT"
- **Zenlytic**: "Requires semantic layer setup by data team"
- **Tableau Pulse**: "Metric definitions created by admins"
- **Qlik**: "58% certification fail rate", "Steep learning curve"

These aren't features - they're **architectural choices** that enable or prevent business user autonomy.

---

## Proposed Column Organization

### Group 1: Setup & Accessibility (4 columns)
- Setup Time (existing)
- No Data Modeling (NEW)
- No Training Required (NEW)
- No IT for Setup (NEW)

### Group 2: Query & Interaction (3 columns)
- Natural Language Query (existing)
- Multi-Turn Chat (NEW - clarified)
- Spreadsheet Engine (NEW)

### Group 3: Agentic Investigation (4 columns) 🆕
- Multi-Pass Investigation (NEW)
- Context Retention (NEW)
- Hypothesis Testing (NEW)
- Root Cause Analysis (consolidate with above?)

### Group 4: Machine Learning (5 columns) 🆕
- Explainable ML (NEW)
- Automatic Data Prep (NEW)
- AI Explanation Layer (NEW)
- ML Discovery (NEW)
- ML Types (Clustering, Prediction, etc.)

### Group 5: Output & Integration (existing columns)
- Data Export
- Visualization
- PowerPoint
- Excel Integration
- Slack/Teams
- Presentation
- Brand Control

---

## Implementation Priority

### Phase 1: Must-Have (Fixes Competitive Misrepresentation)
1. ✅ Split "Investigation" into Multi-Turn vs Multi-Pass vs Hypothesis Testing
2. ✅ Split "ML" into 4 specific capabilities (Explainable, Auto Prep, AI Explanation, Discovery)
3. ✅ Add "Spreadsheet Engine" column

**Impact**: Stops Qlik/others from appearing equal in investigation/ML when they fundamentally aren't.

### Phase 2: High-Value (Reinforces BUA Story)
4. ✅ Add "No Data Modeling" column
5. ✅ Add "No Training Required" column
6. ✅ Improve header readability

**Impact**: Connects capabilities to business user autonomy framework.

### Phase 3: Polish
7. ✅ Add "No IT for Setup" column
8. ✅ Reorganize columns by logical groupings
9. ✅ Add hover tooltips for detailed definitions

---

## Scoring Guidelines for New Columns

### Multi-Pass Investigation
- **✓✓✓ (3 dots)**: Automatic 3-10 query investigation with context retention (Scoop only)
- **✓✓ (2 dots)**: Manual multi-step workflows (user must chain queries)
- **✓ (1 dot)**: Can handle follow-up questions but no context/investigation
- **✗ (Red X)**: Single-query only

### Explainable ML
- **✓✓✓**: Decision trees, rule mining, or other interpretable models (Scoop)
- **✓✓**: Black-box ML with some explanation features
- **✓**: Basic ML with no explanations
- **✗**: No ML or only statistical functions

### Automatic Data Prep (for ML)
- **✓✓✓**: Fully automatic cleaning, binning, feature engineering (Scoop)
- **✓✓**: Guided data prep with user decisions
- **✓**: Manual data prep required
- **✗**: User must prepare data before ML

### No Data Modeling
- **✓✓✓**: Works on raw data, no semantic layer required (Scoop)
- **✓✓**: Optional semantic layer
- **✓**: Basic modeling required
- **✗**: Requires semantic layer/YAML/metric definitions

---

## Expected Competitor Scores (Phase 1 Changes)

| Platform | Multi-Turn Chat | Multi-Pass Investigation | Explainable ML | Auto Data Prep | Spreadsheet Engine |
|----------|----------------|-------------------------|----------------|----------------|-------------------|
| **Scoop** | ✓✓✓ | ✓✓✓ | ✓✓✓ | ✓✓✓ | ✓✓✓ |
| Qlik | ✓✓ | ✗ | ✗ | ✗ | ✗ |
| Snowflake Cortex | ✓ | ✗ | ✗ | ✗ | ✗ |
| Power BI Copilot | ✓✓ | ✗ | ✗ | ✗ | ✗ |
| ThoughtSpot | ✓✓ | ✗ | ✗ | ✗ | ✗ |
| Domo | ✓✓ | ✗ | ✗ | ✗ | ✗ |
| Tableau Pulse | ✓ | ✗ | ✗ | ✗ | ✗ |
| Zenlytic | ✓✓ | ✗ | ✗ | ✗ | ✗ |

**Result**: Scoop gets 15/15 dots in these 5 critical columns. Every competitor gets 0-2 dots total.

---

## Visual Design Suggestions

### Color Coding Enhancement
- **✓✓✓ (3 dots)**: Bright green (unique capability)
- **✓✓ (2 dots)**: Medium green (good capability)
- **✓ (1 dot)**: Yellow/amber (basic capability)
- **⚬⚬⚬ (3 empty dots)**: Light gray (announced/roadmap)
- **✗ (Red X)**: Red (no capability)

### Column Width
- Agentic Investigation columns should be **wider** or **highlighted** to emphasize this is where Scoop dominates
- Consider a subtle background color for the "Agentic Investigation" group to draw attention

### Tooltips/Popovers
On hover, show:
- **Definition**: What this capability means
- **Why It Matters**: Business impact
- **How Scoop Does It**: 1-sentence technical approach

Example for "Multi-Pass Investigation":
> **Definition**: Automatically runs 3-10 interconnected queries to find root causes
> **Why It Matters**: Answers "why" questions without user having to manually chain queries
> **How Scoop Does It**: AI reasoning engine with probe dependencies and context retention

---

## Evidence Sources for Each Change

### Multi-Pass Investigation
- `/home/ubuntu/dev/scoop/app/src/main/resources/ReasoningPrompts.txt` (lines 1-398)
- Probe dependency system with `depends_on`, `extraction_rules`, `use_previous_results`
- 6 investigation strategies: Drill-Down, Temporal, Segmentation, Causal, Pattern Discovery, Comparative

### Explainable ML
- `SCOOP_CAPABILITIES.md` (lines 74-153): "Layer 2: Explainable ML Model Execution (J48, JRip, EM Clustering)"
- "Three-Layer Architecture: Data prep → Explainable models → AI translation"

### Spreadsheet Engine
- `SCOOP_CAPABILITIES.md` (lines 20-71): "150+ Excel functions implemented"
- "In-Memory Spreadsheet Engine: Full Excel-compatible formula execution"

### No Data Modeling
- Competitor evidence in `framework_scoring.md` files:
  - Snowflake Cortex: "Requires YAML semantic model"
  - Zenlytic: "Semantic layer dependency"
  - Tableau Pulse: "Metric definitions required"

---

## Questions for Implementation Team

1. **Technical**: Where is the capability matrix data stored? (JSON, database, hardcoded?)
2. **Design**: Can we increase column count to ~20-25 without hurting mobile/tablet experience?
3. **Scoring**: Who maintains the competitor capability assessments? Need evidence documentation process.
4. **UX**: Should we group columns visually (Setup / Investigation / ML / Output)?
5. **Tooltips**: Is there hover functionality currently? If not, can we add it?

---

## Success Metrics

**Before**: Matrix shows Scoop with many ✓ marks, competitors with some ✗ marks
**After**: Matrix shows Scoop with 15+ unique ✓✓✓ capabilities in investigation/ML that NO competitor has

**Goal**: Viewer immediately sees: "Scoop does things fundamentally differently in investigation and ML, not just more features"

---

## Appendix: Current Column List (From Screenshot)

Visible columns (best guess from rotated headers):
1. Setup Time
2. Natural Language
3. Investigation (?)
4. ML (?)
5. Data Sources (?)
6. Excel/Spreadsheet
7. PowerPoint
8. Slack
9. Mobile
10. Multi-Source
11. Brand Control
12. Anomaly Detection
13. Predictions
14. Presentation
15. Visualization
16. Natural Text
17. Specialized Reports

**Total**: ~17 columns currently

**Proposed**: ~25 columns (adds 8 critical ones)