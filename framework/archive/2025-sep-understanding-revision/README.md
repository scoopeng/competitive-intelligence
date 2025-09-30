# Understanding Dimension Revision - September 2025

**Date**: September 30, 2025
**Status**: Completed and integrated into main framework

## What Happened

During deep review of the BUA Framework, we discovered that the Understanding dimension scoring was misaligned with Scoop's actual capabilities. The rubric was too vague and led to systematic overscoring of competitors.

## The Problem

**Old rubric** (vague language):
- 6 points: "Multi-pass investigation but user must guide it"
- 8 points: "Automatic multi-pass investigation"

**Result**:
- Qlik scored 15/20 for "associative model" (just clicking through relationships)
- ThoughtSpot scored 20/20 despite NO multi-pass investigation
- The dimension didn't capture **true agentic analytical capabilities**

## The Solution

**New rubric** (precise criteria):
- Emphasizes **probe dependencies** (query N uses results from query N-1)
- Distinguishes **explainable ML** (decision trees, rules) vs **black-box** (predictions only)
- Adds "Agentic Investigation Test" with concrete examples
- Makes clear: manual clicking ≠ autonomous investigation

## Key Changes

### Component A: Investigation → Agentic Investigation Depth
- Added probe dependency requirement
- Added investigation planning requirement
- Added multiple probe types (DATASET, ML_RELATIONSHIP, ML_GROUP, ML_PERIOD)
- Clarified: system must plan ahead, not just respond to user

### Component B: ML Pattern Discovery → Deep ML Understanding
- Emphasized explainability (decision trees/rules vs black-box)
- Added accessibility requirement (no data scientist needed)
- Listed specific ML types (J48, EM clustering, JRip rules)

### Component C: Business-Language Explanation
- Added "boss test" - can user explain to boss without help?
- Emphasized zero jargon requirement
- Added example transformation (technical → business)

## Impact on Scores

| Competitor | Old | New | Change |
|------------|-----|-----|--------|
| Scoop | 18/20 | 18/20 | ✅ Unchanged |
| Power BI | 7/20 | 7/20 | ✅ Unchanged |
| ThoughtSpot | 20/20 | 8/20 | ⬇️ -12 points |
| Qlik | 15/20 | 6/20 | ⬇️ -9 points |
| Domo | 18/20 | 8/20 | ⬇️ -10 points |

**Result**: Scoop's competitive advantage on Understanding dimension is now accurately reflected.

## Files in This Archive

1. **UNDERSTANDING_DIMENSION_ANALYSIS.md** (438 lines)
   - Deep dive into the problem
   - Analysis of Scoop's actual capabilities from source code
   - Comparison of what competitors actually do vs claims
   - Detailed recommendations

2. **UNDERSTANDING_DIMENSION_REVISED.md** (299 lines)
   - Draft of new rubric with precise criteria
   - Scoring examples for each level
   - The Agentic Investigation Test
   - Questions for approval

## Integration

The revised Understanding dimension was integrated into:
- `BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md` (lines 270-444)
- All 12 competitor `framework_scoring.md` files rescored
- All affected Webflow pages redeployed

## Lessons Learned

1. **Vague rubrics lead to scoring drift** - "user must guide it" is too subjective
2. **Probe dependencies are the key differentiator** - this is true agentic behavior
3. **Explainable vs black-box ML matters** - predictions without explanations aren't empowering
4. **Examples prevent misinterpretation** - "Agentic Investigation Test" makes expectations concrete

---

**Archived**: September 30, 2025
**Integrated into**: BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md v2.0