# Web Comparison Update Plan - All Competitors

**Created**: September 27, 2025
**Purpose**: Update all competitor web comparisons to 59-point BUA framework with improved tone
**Status**: Planning Phase

---

## Current State

### Completed ✓
- **Power BI Copilot**: Updated to 21/59, improved tone, added cost transparency

### All Competitors with 59-Point Scores

| Competitor | Score | Category | Status |
|-----------|-------|----------|--------|
| **Power BI Copilot** | 21/59 (36%) | C - IT Platform | ✅ Complete |
| **Domo** | 33/59 (56%) | B - Analyst Workbench | ❌ No web comparison |
| **ThoughtSpot** | 28/59 (47%) | B - Analyst Workbench | ❌ No web comparison |
| **Qlik** | 23/59 (39%) | C - IT Platform | ❌ No web comparison |
| **Zenlytic** | 22/59 (37%) | C - IT Platform | ❌ No web comparison |
| **Sisense** | 19/59 (32%) | C - IT Platform | ❌ No web comparison |
| **Tableau Pulse** | 18/59 (31%) | C - IT Platform | ❌ No web comparison |
| **Snowflake Cortex** | 17/59 (29%) | C - IT Platform | ❌ No web comparison |
| **DataGPT** | 15/59 (25%) | C - IT Platform | ❌ No web comparison |
| **Tellius** | 15/59 (25%) | C - IT Platform | ❌ No web comparison |
| **DataChat** | 14/59 (24%) | D - Dashboard Tool | ❌ No web comparison |

---

## Category Definitions (59-Point Framework)

### Category A: True Self-Service (40-59 points / 68-100%)
Business users fully empowered across all dimensions. Zero IT dependency.

### Category B: Analyst Workbench (24-35 points / 40-59%)
Strong analytical platforms with good investigation and ML capabilities, but require IT setup and portal access.
- **Domo** (33/59, 56%)
- **ThoughtSpot** (28/59, 47%)

### Category C: IT Platform (15-23 points / 25-39%)
Requires IT/analyst involvement for most tasks. Business users have limited independence.
- **Qlik** (23/59, 39%)
- **Power BI Copilot** (21/59, 36%) ✅
- **Zenlytic** (22/59, 37%)
- **Sisense** (19/59, 32%)
- **Tableau Pulse** (18/59, 31%)
- **Snowflake Cortex** (17/59, 29%)
- **DataGPT** (15/59, 25%)
- **Tellius** (15/59, 25%)

### Category D: Dashboard Tool (0-14 points / 0-24%)
Static views, minimal self-service capability.
- **DataChat** (14/59, 24%)

---

## Priority Tiers

### Tier 1: High Priority (Generate First)
**Criteria**: Most common in deals + strong competitive differentiation

1. **Tableau Pulse** (18/59, 31%, Category C)
   - Reason: Tableau is #1 market competitor, Pulse is their AI offering
   - Differentiation: Schema evolution vs rigid Tableau models
   - Deal Frequency: Highest

2. **ThoughtSpot** (28/59, 47%, Category B)
   - Reason: Most similar to Scoop (NL interface, investigation focus)
   - Differentiation: We score higher (42/59 vs 28/59) despite their positioning
   - Deal Frequency: High

3. **Snowflake Cortex** (17/59, 29%, Category C)
   - Reason: Already has extensive research (20+ files, test suite)
   - Differentiation: We have documented accuracy advantage
   - Deal Frequency: Medium-High

### Tier 2: Medium Priority (Generate Second)

4. **Domo** (33/59, 56%, Category B)
   - Reason: Highest score of all competitors, interesting positioning challenge
   - Differentiation: Portal prison vs workflow integration
   - Deal Frequency: Medium

5. **Qlik** (23/59, 39%, Category C)
   - Reason: Legacy market leader, enterprise incumbent
   - Differentiation: Modern AI vs legacy BI architecture
   - Deal Frequency: Medium

6. **Zenlytic** (22/59, 37%, Category C)
   - Reason: Direct competitor in AI analytics space
   - Differentiation: Business user autonomy vs analyst-dependent
   - Deal Frequency: Medium

### Tier 3: Lower Priority (Generate Third)

7. **Sisense** (19/59, 32%, Category C)
8. **DataGPT** (15/59, 25%, Category C)
9. **Tellius** (15/59, 25%, Category C)
10. **DataChat** (14/59, 24%, Category D)

---

## Execution Approach

### Phase 1: Template Refinement (Based on Power BI Learnings)

**What Worked**:
- Cost analysis with detailed breakdowns
- Capability deep dive with side-by-side examples
- Schema evolution section (universal differentiator)
- Three-layer AI Data Scientist explanation

**What Needed Improvement**:
- Tone consistency (avoid aggressive language)
- "Failure rate" framing → "satisfaction rate" framing
- Add Scoop cost transparency upfront
- Balance (acknowledge competitor strengths)

**Template Updates Needed**:
1. Add "Tone Guidelines" section to template
2. Add mandatory "Scoop Cost Breakdown" section
3. Add "Balance Check" - every section must acknowledge valid competitor use case
4. Ban "failure rate" language unless technically accurate

### Phase 2: Competitor-Specific Research (Per Competitor)

**Before generating web comparison, ensure:**
1. ✅ Framework scoring complete (59-point)
2. ✅ Battle card updated with 59-point score
3. ✅ Research library has evidence for claims
4. ⚠️ Identify competitor's top 3 weaknesses vs Scoop
5. ⚠️ Identify competitor's valid use cases (honesty builds credibility)

### Phase 3: Generation & Review (Per Competitor)

**Step 1: Pre-Generation Checklist**
- [ ] Read framework_scoring.md for detailed scoring rationale
- [ ] Read BATTLE_CARD.md for key talking points
- [ ] Read research library for evidence
- [ ] Identify 3-5 key differentiators from scoring breakdown

**Step 2: Generate Using Template**
- Use `templates/WEB_COMPARISON_TEMPLATE.md` as base
- Follow phased execution if needed (for longer content)
- Apply Power BI learnings (tone, balance, transparency)

**Step 3: Quality Checks**
- [ ] All BUA references use 59-point scoring (X/59, Y%)
- [ ] Category correctly stated (A/B/C/D with description)
- [ ] No "failure rate" language (unless technical failure)
- [ ] Scoop cost breakdown included
- [ ] Balanced acknowledgment of competitor strengths
- [ ] All specific claims have sources or methodology
- [ ] Tone is confident, not aggressive

**Step 4: Output**
- Save to: `competitors/[name]/outputs/web_comparison.md`
- Update README.md with link to web comparison
- Document completion in this plan

---

## Estimated Timeline

### Sequential Approach (1 at a time)
- Tier 1 (3 competitors): 3-4 hours (1-1.5 hours each)
- Tier 2 (3 competitors): 3-4 hours
- Tier 3 (4 competitors): 4-5 hours
- **Total**: 10-13 hours

### Parallel Approach (batch processing)
- Research phase (all): 2 hours
- Generation (batches of 3): 6-8 hours
- Review/refinement: 2-3 hours
- **Total**: 10-13 hours (same time, better flow)

**Recommendation**: Sequential for Tier 1 (learn from each), parallel for Tier 2-3 (apply learnings)

---

## Key Differentiators by Competitor

### Tableau Pulse (18/59)
1. **Schema Evolution** - Tableau models break on data changes, Scoop adapts
2. **Investigation Depth** - Single query vs multi-pass investigation
3. **Excel Integration** - No native Excel formulas vs 150+ functions

### ThoughtSpot (28/59)
1. **Business User Autonomy** - Still requires IT setup, we don't
2. **ML Explanation** - Black box vs explainable (J48/JRip)
3. **Cost** - $200K+ vs simpler pricing

### Snowflake Cortex (17/59)
1. **Accuracy** - Documented test failures vs deterministic results
2. **Natural Language** - SQL generation vs investigation
3. **Cost** - Compute charges vs predictable pricing

### Domo (33/59) - Highest Competitor Score!
1. **Portal Prison** - Must use Domo portal vs Slack/Excel workflow
2. **Excel Limitations** - Formulas disabled vs 150+ native functions
3. **Investigation** - Dashboard narration vs root cause analysis

**Note**: Domo scores high (56%) but still in Category B because they excel at analyst empowerment but lack true business user autonomy.

---

## Success Criteria

### Per-Competitor
- [ ] Web comparison generated (5,000-8,000 words)
- [ ] 59-point BUA score reflected throughout
- [ ] Category correctly stated everywhere
- [ ] Scoop cost transparency included
- [ ] Tone is confident and balanced (not aggressive)
- [ ] All major claims sourced

### Overall Project
- [ ] All 11 competitors have web comparisons
- [ ] Consistent tone across all comparisons
- [ ] Consistent framework application
- [ ] Sales team can use for any competitive deal

---

## Templates & Resources

### Primary Template
- **File**: `templates/WEB_COMPARISON_TEMPLATE.md`
- **Version**: 2.0 (updated with 59-point framework)
- **Length Target**: 5,000-8,000 words (~30-48K characters)

### Reference Materials
- **Framework**: `framework/BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md` (59-point system)
- **Example**: `competitors/power-bi-copilot/outputs/web_comparison.md` (completed)
- **Tone Guide**: `webflow-competitive-platform/CONTENT-ANALYSIS-power-bi-copilot.md`

### Shared Components
- **Location**: `competitors/SHARED/`
- **Files**:
  - `scoop_capabilities_checklist.md` (40-item verification)
  - `agentic_analytics_section.md` (multi-agent architecture)
  - `embeddable_analytics_section.md` (platform embedding)

---

## Next Steps

### Immediate (Today)
1. **Review this plan** with stakeholders for prioritization feedback
2. **Start Tier 1, Competitor 1**: Tableau Pulse
   - Read existing research
   - Generate web comparison
   - Apply Power BI learnings

### This Week
- Complete Tier 1 (Tableau Pulse, ThoughtSpot, Snowflake Cortex)
- Review consistency across all 4 completed comparisons
- Refine template if needed based on learnings

### Next Week
- Complete Tier 2 (Domo, Qlik, Zenlytic)
- Begin Tier 3

### Target Completion
- **All 11 competitors**: Within 2 weeks
- **Sales enablement ready**: End of month

---

## Tracking Progress

| Competitor | Score | Status | Date | Notes |
|-----------|-------|--------|------|-------|
| Power BI Copilot | 21/59 (36%, C) | ✅ Complete | Sep 27 | Baseline example |
| Tableau Pulse | 18/59 (31%, C) | 🔄 Next | - | Tier 1 priority |
| ThoughtSpot | 28/59 (47%, B) | ⏳ Planned | - | Tier 1 priority |
| Snowflake Cortex | 17/59 (29%, C) | ⏳ Planned | - | Tier 1 priority |
| Domo | 33/59 (56%, B) | ⏳ Planned | - | Tier 2 priority |
| Qlik | 23/59 (39%, C) | ⏳ Planned | - | Tier 2 priority |
| Zenlytic | 22/59 (37%, C) | ⏳ Planned | - | Tier 2 priority |
| Sisense | 19/59 (32%, C) | ⏳ Planned | - | Tier 3 priority |
| DataGPT | 15/59 (25%, C) | ⏳ Planned | - | Tier 3 priority |
| Tellius | 15/59 (25%, C) | ⏳ Planned | - | Tier 3 priority |
| DataChat | 14/59 (24%, D) | ⏳ Planned | - | Tier 3 priority |

**Legend**:
- ✅ Complete
- 🔄 In Progress
- ⏳ Planned
- ⚠️ Blocked

---

## Questions for Stakeholders

1. **Priority Confirmation**: Do you agree with Tier 1 priorities (Tableau Pulse, ThoughtSpot, Snowflake Cortex)?
2. **Timeline**: Is 2-week completion realistic, or should we focus on Tier 1 first?
3. **Review Process**: Who should review comparisons before deployment?
4. **Scoop Pricing**: What guidance for cost transparency? (Currently using "~$180K" placeholder)
5. **Deployment**: Where will these web comparisons be published? (Webflow? Internal wiki?)

---

**Last Updated**: September 27, 2025
**Owner**: Competitive Intelligence Team
**Next Review**: After Tier 1 completion