# Platform Capability Scoring Rubric

This rubric defines how to score platform capabilities objectively based on evidence.

---

## Binary Capabilities (Yes/No)

These are objective features that either exist or don't:

### Integration Capabilities

| Capability | YES Criteria | NO Criteria |
|------------|-------------|------------|
| **Excel Plugin** | Has native Excel add-in or plugin that works inside Excel | No Excel integration or export-only |
| **Slack App** | Has Slack app with analysis capabilities | No Slack integration or notifications-only |
| **CSV Upload** | Supports direct CSV/Excel file upload | No file upload capability |
| **API Connect** | Has API connectors for data sources | No API connectivity |
| **Semantic Model Required** | Requires IT to build semantic model first | Works without semantic model |
| **PowerPoint Generation** | Can generate PowerPoint slides automatically | No PowerPoint generation |
| **Scheduled Reports** | Supports automated scheduled reports | No scheduling capability |
| **Anomaly Detection** | Has automatic anomaly detection | No anomaly detection |
| **Predictive Analytics** | Has predictive/forecasting capabilities | No predictive features |

---

## Scaled Capabilities (0-3)

These capabilities have degrees of quality/depth:

### Natural Language Quality (0-3)

| Score | Criteria | Evidence Examples |
|-------|----------|-------------------|
| **0** | No natural language | SQL/code only, technical query language |
| **1** | Basic keyword search | Simple filters, limited understanding |
| **2** | Good NL with constraints | Understands questions but limited flexibility |
| **3** | Excellent conversational | Full context, pronouns, follow-ups |

### Investigation Depth (0-3)

| Score | Criteria | Evidence Examples |
|-------|----------|-------------------|
| **0** | Single query only | No follow-up capability, one question at a time |
| **1** | Manual follow-up | User can ask follow-ups manually |
| **2** | Guided investigation | Some automatic drilling, suggested questions |
| **3** | Full multi-pass | Automatic 3-10 query investigation to find root cause |

### Root Cause Analysis (0-3)

| Score | Criteria | Evidence Examples |
|-------|----------|-------------------|
| **0** | No why analysis | Shows what happened, not why |
| **1** | Basic why | Simple explanations, surface level |
| **2** | Good analysis | Identifies key drivers and factors |
| **3** | Deep root cause | Automatically finds underlying causes through investigation |

### Visualization Quality (0-3)

| Score | Criteria | Evidence Examples |
|-------|----------|-------------------|
| **0** | Basic charts only | Simple bar/line charts |
| **1** | Standard BI visuals | Common chart types, basic formatting |
| **2** | Good visualizations | Smart chart selection, good design |
| **3** | Exceptional visuals | Publication-ready, automatic best visualization |

### Narrative Generation (0-3)

| Score | Criteria | Evidence Examples |
|-------|----------|-------------------|
| **0** | No narratives | Numbers only, no text |
| **1** | Basic descriptions | Simple text like "Sales increased 10%" |
| **2** | Good explanations | Context and key insights in text |
| **3** | Full narratives | Publication-ready analysis with context, insights, recommendations |

### Setup Complexity (0-3)

| Score | Criteria | Time to First Insight |
|-------|----------|----------------------|
| **0** | Complex IT project | Months (3+ months typical) |
| **1** | Standard implementation | Weeks (2-8 weeks typical) |
| **2** | Quick setup | Days (1-5 days typical) |
| **3** | Instant self-service | Minutes (< 1 hour) |

---

## Evidence Requirements

For each score, evidence must include:
1. **Direct quote** from vendor documentation or testing
2. **Source** (doc link, test result, customer review)
3. **Date** of evidence

Example:
```markdown
### Natural Language Quality: 2/3
**Evidence**: "Copilot doesn't answer follow-up questions. One question at a time"
**Source**: Microsoft Documentation, Copilot Limitations
**Date**: September 2024
**Reasoning**: Has NL but significant constraints on conversation flow
```

---

## Scoring Process

1. **Review evidence file** for each platform
2. **Apply rubric** consistently across all platforms
3. **Document reasoning** for each score
4. **Update quarterly** based on new evidence

---

## Visual Display Guidelines

### Binary (Yes/No):
- ✓ (green) = YES
- ✗ (red) = NO
- — (gray) = Unknown/Not Applicable

### Scaled (0-3):
- ○○○ = 0 (None)
- ●○○ = 1 (Basic)
- ●●○ = 2 (Good)
- ●●● = 3 (Excellent)

### Colors:
- 0 = #dc2626 (red)
- 1 = #f59e0b (amber)
- 2 = #84cc16 (lime)
- 3 = #10b981 (emerald)

---

## Platform Scoring Template

```markdown
# Platform Name

## Binary Capabilities
- Excel Plugin: Yes/No
- Slack App: Yes/No
- CSV Upload: Yes/No
- API Connect: Yes/No
- Semantic Model Required: Yes/No
- PowerPoint Generation: Yes/No
- Scheduled Reports: Yes/No
- Anomaly Detection: Yes/No
- Predictive Analytics: Yes/No

## Scaled Capabilities
- Natural Language: 0-3
- Investigation Depth: 0-3
- Root Cause Analysis: 0-3
- Visualization Quality: 0-3
- Narrative Generation: 0-3
- Setup Complexity: 0-3
```