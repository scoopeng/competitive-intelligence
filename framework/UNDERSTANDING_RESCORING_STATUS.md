# Understanding Dimension Rescoring Status
**Date**: September 30, 2025
**Status**: In Progress (3 of 12 complete)

## Completed Rescoring ✅

### 1. ThoughtSpot: 57→45 (-12 pts, B→C)
- Investigation: 8→2 (single query, no probe dependencies)
- ML: 6→4 (black-box SpotIQ, no explainability)
- Explanation: 6→2 (correlations, not causation)
- **File updated**: ✅ competitors/thoughtspot/evidence/framework_scoring.md

### 2. Domo: 62→52 (-10 pts, B→C)
- Investigation: 8→2 (user-triggered, not autonomous)
- ML: 6→4 (AutoML but black-box)
- Explanation: 4→2 (surface-level narratives)
- **File updated**: ✅ competitors/domo/evidence/framework_scoring.md

### 3. Qlik: 47→38 (-9 pts, C→D)
- Investigation: 8→4 (associative model = user clicking, not agentic)
- ML: 0→0 (not accessible to business users)
- Explanation: 6→2 (visual relationships, not business narratives)
- **File updated**: ✅ competitors/qlik/evidence/framework_scoring.md

## Verified Correct (No Change Needed) ✅

### 4. Power BI Copilot: 32/100 (Understanding: 7/20)
- Already correctly scored with new rubric
- Investigation: 2/8 (single query - Microsoft admits this)
- ML: 0/6 (no ML capabilities)
- Explanation: 5/6 (basic summaries, nondeterministic)
- **Action**: Update component names to match new rubric

### 5. Scoop: 82/100 (Understanding: 18/20)
- Already correctly scored
- Investigation: 8/8 (full agentic with probe dependencies)
- ML: 6/6 (explainable J48, EM, JRip)
- Explanation: 4/6 (business narratives, improving actionability)
- **Action**: Update to reference new rubric terminology

## Remaining Rescoring Needed

### 6. Tableau Pulse: Currently 10/20 → Expect ~8/20 (-2 pts)
- Needs analysis of investigation capabilities
- Likely single query, no ML
- **File**: competitors/tableau-pulse/evidence/framework_scoring.md

### 7. Snowflake Cortex: Currently 8/20 → Expect ~4/20 (-4 pts)
- LLM wrapper, no investigation
- No ML (just LLM)
- **File**: competitors/snowflake-cortex/evidence/framework_scoring.md

### 8. Sisense: Currently 8/20 → Expect ~4/20 (-4 pts)
- Basic embedded analytics
- No investigation capabilities
- **File**: competitors/sisense/evidence/framework_scoring.md

### 9. Tellius: Currently 10/20 → Expect ~6/20 (-4 pts)
- Need to verify ML explainability
- Likely some ML but need to check if explainable
- **File**: competitors/tellius/evidence/framework_scoring.md

### 10. DataGPT: Currently 6/20 → Expect ~4/20 (-2 pts)
- Narrative generation but no investigation
- **File**: competitors/datagpt/evidence/framework_scoring.md

### 11. DataChat: Currently 6/20 → Expect ~4/20 (-2 pts)
- Conversational but single-query
- **File**: competitors/datachat/evidence/framework_scoring.md

### 12. Zenlytic: Currently 12/20 → Expect ~6/20 (-6 pts)
- Need to verify ML capabilities
- **File**: competitors/zenlytic/evidence/framework_scoring.md

## Expected Final Scores

| Competitor | Current Total | New Total | Change | New Category |
|------------|--------------|-----------|--------|--------------|
| **Scoop** | 82 | 82 | ✅ 0 | A (Strong) |
| **Domo** | 62 | 52 | ⬇️ -10 | C (Moderate) |
| **ThoughtSpot** | 57 | 45 | ⬇️ -12 | C (Moderate) |
| **Qlik** | 47 | 38 | ⬇️ -9 | D (Weak) |
| **Zenlytic** | 42 | ~36 | ⬇️ -6 | D (Weak) |
| **Tableau Pulse** | 37 | ~35 | ⬇️ -2 | D (Weak) |
| **Power BI Copilot** | 32 | 32 | ✅ 0 | D (Weak) |
| **Tellius** | 30 | ~26 | ⬇️ -4 | D (Weak) |
| **Snowflake Cortex** | 26 | ~22 | ⬇️ -4 | F (Poor) |
| **Sisense** | 20 | ~16 | ⬇️ -4 | F (Poor) |
| **DataGPT** | 18 | ~16 | ⬇️ -2 | F (Poor) |
| **DataChat** | 17 | ~15 | ⬇️ -2 | F (Poor) |

## Key Insights from Rescoring

**What we learned**:
1. **Vague rubrics caused systematic overscoring** - "multi-pass investigation" was interpreted too loosely
2. **Probe dependencies are the key differentiator** - this is what makes investigation truly agentic
3. **Explainable vs black-box ML matters** - predictions without causal understanding don't empower users
4. **Manual clicking ≠ autonomous investigation** - Qlik's associative model is powerful but user-driven

**Impact on competitive positioning**:
- Scoop's lead on Understanding now accurately reflected (18/20 vs competitors' 2-8/20)
- Gap widened on the dimension that matters most (agentic analytical capabilities)
- Only Scoop has true probe dependencies and explainable ML

## Next Steps

1. **Complete remaining 7 competitor rescoring**
   - Use same strict criteria as ThoughtSpot, Domo, Qlik
   - Document evidence for each score change
   - Update total scores and categories

2. **Update Power BI and Scoop**
   - Change component names to match new rubric
   - Keep scores the same (already correct)

3. **Commit all changes**
   - Create comprehensive commit message
   - Document rescoring methodology

4. **Redeploy to Webflow**
   - Deploy all 12 competitor pages
   - Update BUA research document
   - Verify all pages load correctly

---

**Status**: 3 of 12 complete (25%)
**Time estimate**: ~30-45 min to complete remaining 9
**Next competitor**: Tableau Pulse (smallest change, -2 pts)