# BUPAF → BUA Migration Plan

**Date**: September 27, 2025
**Reason**: Framework renamed from "Business User Power Assessment Framework (BUPAF)" to "Business User Autonomy Framework" with BUA Score

---

## Replacement Rules

### Acronym Replacements
- `BUPAF` → `BUA` (Business User Autonomy)
- `BUPAF Score` → `BUA Score`
- `BUPAF Framework` → `Business User Autonomy Framework`
- `BUPAF Analysis` → `BUA Analysis`
- `BUPAF Scoring` → `BUA Scoring`

### File/URL Replacements
- `BUPAF_COMPARISON_TEMPLATE.md` → `BUA_COMPARISON_TEMPLATE.md`
- `bupaf_scoring.md` → `bua_scoring.md`
- `bupaf_evidence.md` → `bua_evidence.md`

### Score References
- `X/50 (BUPAF)` → `X/50 (BUA Score)`
- `BUPAF: 15/50` → `BUA Score: 15/50`

### Category References (keep as-is)
- Category A, B, C, D remain unchanged
- Just update "BUPAF Score" → "BUA Score" in category descriptions

---

## Files to Update (72 files, 274 references)

### Root Documentation (8 files)
- [ ] CHANGELOG.md
- [ ] CLAUDE.md
- [ ] FRAMEWORK_ROLLOUT_PLAN.md
- [ ] METHODOLOGY.md
- [ ] QUICK_START.md
- [ ] README.md
- [ ] RESEARCH_ROADMAP.md
- [ ] SESSION_CONTINUATION_SEP27.md

### Templates (5 files)
- [ ] templates/BATTLE_CARD_TEMPLATE.md
- [ ] templates/BUPAF_COMPARISON_TEMPLATE.md → RENAME to BUA_COMPARISON_TEMPLATE.md
- [ ] templates/COMPETITOR_TEMPLATE.md
- [ ] templates/README_TEMPLATE.md
- [ ] templates/WEB_COMPARISON_TEMPLATE.md

### Framework (2 files)
- [ ] framework/BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md
- [ ] framework/README.md

### Results (3 files)
- [ ] results/EXECUTIVE_PRESENTATION_BUPAF_RESULTS.md
- [ ] results/QUICK_COMPARISON_MATRIX.md
- [ ] results/SALES_POSITIONING_GUIDE.md

### Competitor Files (54 files across 11 competitors)

**Power BI Copilot** (7 files)
- [ ] competitors/power-bi-copilot/BATTLE_CARD.md
- [ ] competitors/power-bi-copilot/DEEP_ANALYSIS.md
- [ ] competitors/power-bi-copilot/README.md
- [ ] competitors/power-bi-copilot/RESEARCH_CHECKLIST.md
- [ ] competitors/power-bi-copilot/evidence/phase4_sales_enablement.md
- [ ] competitors/power-bi-copilot/outputs/web_comparison.md
- [ ] competitors/power-bi-copilot/research/bupaf_scoring.md → RENAME to bua_scoring.md

**Tableau Pulse** (6 files)
- [ ] competitors/tableau-pulse/BATTLE_CARD.md
- [ ] competitors/tableau-pulse/DEEP_ANALYSIS.md
- [ ] competitors/tableau-pulse/README.md
- [ ] competitors/tableau-pulse/RESEARCH_CHECKLIST.md
- [ ] competitors/tableau-pulse/evidence/phase4_sales_enablement.md
- [ ] competitors/tableau-pulse/evidence/research_library_chunk1.md
- [ ] competitors/tableau-pulse/research/existing_research.md

**ThoughtSpot** (4 files)
- [ ] competitors/thoughtspot/BATTLE_CARD.md
- [ ] competitors/thoughtspot/README.md
- [ ] competitors/thoughtspot/RESEARCH_CHECKLIST.md
- [ ] competitors/thoughtspot/evidence/phase4_sales_enablement.md

**Domo** (4 files)
- [ ] competitors/domo/BATTLE_CARD.md
- [ ] competitors/domo/README.md
- [ ] competitors/domo/RESEARCH_CHECKLIST.md
- [ ] competitors/domo/evidence/phase4_sales_enablement.md

**Qlik** (5 files)
- [ ] competitors/qlik/BATTLE_CARD.md
- [ ] competitors/qlik/QA_REPORT.md
- [ ] competitors/qlik/README.md
- [ ] competitors/qlik/RESEARCH_CHECKLIST.md
- [ ] competitors/qlik/RESEARCH_SUMMARY.md
- [ ] competitors/qlik/research/bupaf_evidence.md → RENAME to bua_evidence.md

**Snowflake Cortex** (4 files)
- [ ] competitors/snowflake-cortex/BATTLE_CARD.md
- [ ] competitors/snowflake-cortex/RESEARCH_CHECKLIST.md
- [ ] competitors/snowflake-cortex/evidence/phase2_functionality_analysis.md
- [ ] competitors/snowflake-cortex/evidence/phase4_sales_enablement.md
- [ ] competitors/snowflake-cortex/research/existing_research.md

**Zenlytic** (4 files)
- [ ] competitors/zenlytic/BATTLE_CARD.md
- [ ] competitors/zenlytic/README.md
- [ ] competitors/zenlytic/RESEARCH_CHECKLIST.md
- [ ] competitors/zenlytic/evidence/phase4_sales_enablement.md

**DataChat** (5 files)
- [ ] competitors/datachat/BATTLE_CARD.md
- [ ] competitors/datachat/README.md
- [ ] competitors/datachat/RESEARCH_CHECKLIST.md
- [ ] competitors/datachat/evidence/phase2_functionality_analysis.md
- [ ] competitors/datachat/evidence/phase4_sales_enablement.md

**DataGPT** (5 files)
- [ ] competitors/datagpt/BATTLE_CARD.md
- [ ] competitors/datagpt/README.md
- [ ] competitors/datagpt/RESEARCH_CHECKLIST.md
- [ ] competitors/datagpt/evidence/phase4_sales_enablement.md
- [ ] competitors/datagpt/research/existing_research.md

**Sisense** (5 files)
- [ ] competitors/sisense/BATTLE_CARD.md
- [ ] competitors/sisense/README.md
- [ ] competitors/sisense/RESEARCH_CHECKLIST.md
- [ ] competitors/sisense/evidence/phase4_sales_enablement.md
- [ ] competitors/sisense/research/existing_research.md

**Tellius** (5 files)
- [ ] competitors/tellius/BATTLE_CARD.md
- [ ] competitors/tellius/QA_REPORT.md
- [ ] competitors/tellius/README.md
- [ ] competitors/tellius/RESEARCH_CHECKLIST.md
- [ ] competitors/tellius/evidence/phase4_sales_enablement.md
- [ ] competitors/tellius/research/existing_research.md

**Competitors README**
- [ ] competitors/README.md

---

## Execution Strategy

### Phase 1: Core Documentation & Templates (13 files)
Update root docs, templates, and framework files first
**Time**: 30-45 minutes

### Phase 2: Competitor Files - Batch 1 (Priority 4 competitors - 20 files)
Power BI Copilot, Tableau Pulse, ThoughtSpot, Domo
**Time**: 45-60 minutes

### Phase 3: Competitor Files - Batch 2 (Remaining 7 competitors - 34 files)
All others
**Time**: 60-90 minutes

### Phase 4: Verification & Cleanup
- Search for any remaining "BUPAF" references
- Verify all file renames completed
- Test that no broken links exist
**Time**: 15-30 minutes

**Total Estimated Time**: 2.5-4 hours

---

## Post-Migration Checklist

- [ ] All 274 BUPAF references replaced with BUA
- [ ] All files with "bupaf" in filename renamed
- [ ] All broken links fixed
- [ ] Framework README updated
- [ ] CLAUDE.md updated with new terminology
- [ ] Templates updated
- [ ] No remaining BUPAF references (verify with grep)

---

**Status**: Planning
**Start Date**: [When ready]
**Completion Target**: Same day