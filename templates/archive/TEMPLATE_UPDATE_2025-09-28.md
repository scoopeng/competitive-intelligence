# Web Comparison Template Update - September 28, 2025

## Overview

**Version**: 2.0-draft → 2.1-draft
**Date**: September 28, 2025
**Trigger**: Power BI Copilot deep research revealed generalizable patterns
**Philosophy**: Additive enhancement, not restructure

---

## What We Changed (4 Surgical Additions)

### Change 1: Added "Question Hierarchy" to Section 2.1 Investigation

**Location**: After "Architecture Comparison" table in Section 2.1
**Words Added**: ~150
**Purpose**: Show that most competitors handle simple "what" but fail on complex "what" and "why"

**What It Adds**:
```
Simple "What" Questions (both handle):
- "Show me revenue by region"
- "How many customers do we have?"

Complex "What" Questions (require analytical filtering):
- "Show opportunities from top 5 sales reps by win rate"
- "Display accounts where lifetime value > $100K and growth > 20%"

"Why" Questions (require investigation):
- "Why did churn increase this quarter?"
- "What caused the revenue drop?"
```

**Key Insight Line**:
> "{COMPETITOR} is a {text-to-query interface / BI tool}—handles simple questions but cannot {SPECIFIC_GAP}. Scoop is an AI data analyst—handles all three question types."

**Applies To**: ThoughtSpot, Tableau Pulse, Power BI Copilot, Domo, Qlik, DataGPT, Tellius, DataChat (8+ of 11 competitors)

**Doesn't Apply To**: Snowflake Cortex (different architecture), possibly Zenlytic (need to verify)

---

### Change 2: Added Optional "Semantic Model Boundary" Block to Section 2.1

**Location**: Immediately after Question Hierarchy
**Words Added**: ~120
**Purpose**: Explain why complex "what" questions fail for semantic model-based competitors

**When to Include**:
- ✅ Power BI (semantic models)
- ✅ ThoughtSpot (models)
- ✅ Tableau (data sources requiring pre-config)
- ✅ Domo (datasets)
- ✅ Qlik (apps)
- ❌ Snowflake Cortex (works on raw SQL)

**What It Explains**:
- Business users bounded by what IT included in model
- Complex questions require IT work (examples: top N, thresholds, multi-condition)
- Typical IT time: 1-2 weeks per pattern
- Scoop: no boundary, automatic subquery generation

**Key Differentiation**:
> "Business users can only query data {IT/ANALYSTS} included in the {MODEL_TYPE}. If {IT/ANALYSTS} didn't include a table or relationship, business users cannot analyze it—even if data exists in source systems."

**Flexibility**: Block is clearly marked "OPTIONAL: include if... skip if..."

---

### Change 3: Added 3 Rows to "At-a-Glance Comparison" Table (Section 1)

**Location**: Between "User Experience" and "Setup & Implementation" sections
**Rows Added**: 3
**Purpose**: Show capability gap immediately, above the fold

**New Section in Table**:
```
| **Question Capabilities** |
| Simple "What" Questions | {✅/⚠️ + DETAILS} | ✅ All questions | {COMPARISON} |
| Complex "What" (Analytical Filtering) | {✅/❌ + EXPLAIN} | ✅ Automatic subqueries | {COMPARISON} |
| "Why" Investigation | {✅/❌ + DETAILS} | ✅ Multi-pass analysis | {COMPARISON} |
```

**Visual Impact**: Readers see ❌❌❌ vs ✅✅✅ pattern immediately

**Why This Works**:
- Scannable (checkmarks)
- Above the fold (Section 1)
- Concrete (not abstract "investigation")

---

### Change 4: Added FAQ Question About Complex Analytical Queries (Section 6)

**Location**: In "Capabilities & Features" subsection of FAQ, after investigation question
**Words Added**: ~40
**Purpose**: Answer specific search query, show gap concretely

**New Question**:
> **Q: Can {COMPETITOR} handle complex analytical questions like "show top performers by calculated metric"?**
> A: {YES/NO}. Questions like "show opportunities from top 5 sales reps by win rate" require {SUBQUERY_OR_ANALYTICAL_FILTERING}. {IF_NO: Explain IT must build custom measures (1-2 weeks)}. Scoop handles these automatically via subquery generation—no pre-work needed.

**SEO/AEO Value**:
- Answers long-tail query
- Uses specific example
- Shows time contrast (1-2 weeks vs immediate)

---

## What We Didn't Change

### Structure (All Preserved)
- ✅ Same 7 major sections
- ✅ Same subsection order
- ✅ Same table formats
- ✅ Same word count targets

### Existing Guidance (All Preserved)
- ✅ "Capability Selection Strategy" (lines 29-58)
- ✅ Quality Checklist (lines 59-68)
- ✅ All existing optional blocks
- ✅ Template instructions

### Flexibility (All Maintained)
- ✅ Competitor-specific strategy files still control emphasis
- ✅ Optional blocks remain optional
- ✅ Template adapts to different competitor architectures

---

## Why These Changes Work

### 1. Generalizable Pattern

**Power BI Research Finding**: "Text-to-query interface vs AI data analyst"

**Applies Broadly To**:
- ThoughtSpot: Search-based BI (text-to-query for semantic models)
- Tableau Pulse: AI insights on Tableau data sources (bounded by data model)
- Domo: AI Q&A on cards/datasets (bounded by IT configuration)
- Qlik: Insight Advisor (bounded by app definitions)
- DataGPT, Tellius, DataChat: All require schema/model setup

**Pattern**: 9+ out of 11 competitors have:
- ✅ Simple "what" capability (if data is modeled)
- ❌ Complex "what" capability (requires IT pre-work)
- ❌ "Why" investigation (single-turn architecture)

### 2. Concrete, Not Abstract

**Before**: "Investigation limitation"
**After**: "Cannot answer 'show opportunities from top 5 reps by win rate' without IT building custom measures (1-2 weeks)"

**Impact**: Sales can demo this, prospects can test it, technical buyers understand the constraint

### 3. Optional, Not Mandatory

**Semantic Model Boundary block**:
- Clearly marked "Include if... Skip if..."
- Only use when relevant
- Can adapt terminology (DAX measures, calculations, models, datasets)

**Doesn't Force Fit**: Snowflake Cortex comparison won't include this block (works on raw SQL, different architecture)

### 4. Additive, Not Disruptive

**Total additions**: ~310 words
**Sections modified**: 3 (Section 1, Section 2.1, Section 6)
**Structure changes**: 0
**Existing content modified**: 0

**Philosophy**: Enhancement, not overhaul

---

## Applies to These Competitors

### High Confidence (Definitely Use All 4 Additions)
1. ✅ **Power BI Copilot**: Semantic models, DAX measures, single-turn
2. ✅ **ThoughtSpot**: Models, pre-built logic, search (not investigation)
3. ✅ **Tableau Pulse**: Data sources, calculated fields, insights (not investigation)
4. ✅ **Domo**: Cards, datasets, ETL, no investigation
5. ✅ **Qlik**: Apps, load scripts, associative engine bounded by app scope

### Medium Confidence (Likely Use 3 of 4 - Skip Semantic Model Block)
6. ⚠️ **Zenlytic**: Uses semantic layer but claim "metrics layer" - need to verify if this is different
7. ⚠️ **Sisense**: Models but more flexible - need to verify investigation capability

### Low Confidence (Use 1-2 Additions Only)
8. ❌ **Snowflake Cortex**: SQL on raw data (no semantic model boundary) - use Question Hierarchy only, skip semantic model block
9. ❌ **DataGPT/Tellius/DataChat**: Need more research to confirm pattern

### Definitely Use For New Competitors
- Any competitor requiring "data modeling", "semantic models", "pre-built reports"
- Any competitor with single-turn queries (no follow-ups)
- Any competitor that's a "BI tool with AI" vs "AI data analyst"

---

## Impact on Future Comparisons

### When Generating Web Comparisons

**Section 1 (Executive)**: At-a-Glance table now shows question capabilities immediately
- Readers see ❌❌❌ vs ✅✅✅ pattern
- Above the fold positioning

**Section 2.1 (Investigation)**:
- Lead with Question Hierarchy (shows the gap concretely)
- If semantic model applies → include boundary block
- Side-by-side examples show "why" investigation difference

**Section 6 (FAQ)**:
- Complex analytical query question provides SEO/AEO value
- Answers specific long-tail search

### When to Skip Additions

**Semantic Model Boundary block** - Skip if:
- Competitor works on raw data (Snowflake Cortex)
- Competitor has no pre-modeling requirement
- Architecture is fundamentally different

**Question Hierarchy** - Skip if:
- Competitor actually CAN do complex "what" questions (rare)
- Competitor has investigation capabilities (very rare)
- Both tools are similarly limited (unlikely)

---

## Quality Assurance

### Before This Update: Gaps

**Problem**: Template didn't distinguish between:
- Simple queries (most tools handle)
- Complex analytical queries (most tools fail)
- Investigation (almost all tools fail)

**Result**: Comparisons might undersell Scoop's advantages for semantic model-based competitors

### After This Update: Improvements

**Now Template Captures**:
- ✅ Three-tier question hierarchy (simple/complex/why)
- ✅ Semantic model boundary pattern (when applicable)
- ✅ Concrete examples of complex questions
- ✅ IT time required for complex questions (1-2 weeks typical)

**Result**: Comparisons will show capability gaps more clearly while remaining credible

---

## Examples of Usage

### Example 1: Power BI Copilot Comparison

**Section 1 At-a-Glance Table**:
```
| Simple "What" Questions | ✅ Works (if in semantic model) | ✅ All questions | Both handle |
| Complex "What" (Analytical Filtering) | ❌ Requires IT DAX (1-2 weeks) | ✅ Automatic subqueries | Scoop 1-2 weeks faster |
| "Why" Investigation | ❌ Single-turn only | ✅ Multi-pass analysis | Critical gap |
```

**Section 2.1 Question Hierarchy**:
- Simple "what": ✅ Both handle
- Complex "what": ❌ Power BI needs custom DAX measures
- "Why": ❌ Microsoft docs: "Can't answer questions that require generating new insights"
- Key Insight: "Power BI Copilot is a text-to-query interface—handles simple questions but cannot generate complex analytical logic on the fly or investigate beyond single queries."

**Section 2.1 Semantic Model Block**:
- ✅ Include (Power BI has semantic models)
- Examples: "Top 5 reps by win rate", "Accounts where LTV > $100K"
- IT time: 1-2 weeks per pattern
- Scoop: 3 seconds

### Example 2: Snowflake Cortex Comparison

**Section 1 At-a-Glance Table**:
```
| Simple "What" Questions | ✅ SQL queries | ✅ All questions | Both handle |
| Complex "What" (Analytical Filtering) | ✅ SQL subqueries (requires SQL expertise) | ✅ Automatic subqueries | Scoop no SQL needed |
| "Why" Investigation | ❌ Single SQL queries only | ✅ Multi-pass analysis | Critical gap |
```

**Section 2.1 Question Hierarchy**:
- Simple "what": ✅ Both handle
- Complex "what": ✅ Snowflake can do with SQL BUT requires SQL expertise
- "Why": ❌ Snowflake single queries, no investigation
- Key Insight: "Snowflake Cortex is a SQL generation tool—handles simple and complex queries but requires SQL expertise and cannot investigate beyond single queries."

**Section 2.1 Semantic Model Block**:
- ❌ Skip (Snowflake works on raw data, no semantic model)

---

## Testing Checklist

Before using template for next competitor:

- [ ] Check if competitor requires semantic models/pre-modeling
- [ ] If YES → use all 4 additions
- [ ] If NO → use 3 additions (skip semantic model block)
- [ ] Verify competitor can/cannot handle complex "what" questions
- [ ] Test specific example: "show opportunities from top 5 reps by win rate"
- [ ] Document IT time required for complex questions (if applicable)
- [ ] Ensure examples match competitor's terminology

---

## Success Metrics

**How We'll Know This Works**:

1. **Sales Feedback**: Do these examples resonate? Can sales demo the gap?
2. **Prospect Questions**: Do prospects ask about complex analytical queries?
3. **Consistency**: Do all semantic model-based competitors show same pattern?
4. **Credibility**: Does framing feel fair (not overselling)?

**Review After**: 3 competitor comparisons using updated template
**Target Competitors**: ThoughtSpot, Tableau Pulse, Domo (all semantic model-based)

---

## Summary

**What Changed**: 4 surgical additions (~310 words)
**Why**: Power BI research revealed generalizable "text-to-query vs AI data analyst" pattern
**Applies To**: 8-9 of 11 competitors (all semantic model-based tools)
**Philosophy**: Additive enhancement, optional blocks, concrete examples
**Risk**: Low (doesn't force fit, clearly marked optional)
**Benefit**: Shows capability gaps more clearly while maintaining credibility

**Next Step**: Use updated template for next competitor comparison (suggest: ThoughtSpot or Tableau Pulse to validate pattern)

---

**Version**: Template 2.1-draft
**Updated**: September 28, 2025
**Changes**: Question Hierarchy, Semantic Model Boundary (optional), 3 table rows, 1 FAQ question
**Status**: Ready for use