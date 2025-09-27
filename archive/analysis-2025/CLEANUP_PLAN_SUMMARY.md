# Cleanup Plan: Executive Summary
**Date**: September 27, 2025
**Goal**: Single active template version, clear organization

---

## Key Finding: Version Confusion

**PROBLEM**: Two web comparison templates both appearing active
- `WEB_COMPARISON_TEMPLATE.md` (28K, old approach - 150K chars)
- `WEB_COMPARISON_TEMPLATE_V2_WORKING.md` (48K, new approach - 5-7K words, selective)

**SOLUTION**: Promote V2 as the single active template

---

## Recommended Actions

### 🔴 PHASE 1: Template Consolidation (MUST DO)

**1.1 Promote V2 to Active**
```bash
mkdir -p templates/archive/
mv templates/WEB_COMPARISON_TEMPLATE.md templates/archive/WEB_COMPARISON_TEMPLATE_V1_DEPRECATED.md
mv templates/WEB_COMPARISON_TEMPLATE_V2_WORKING.md templates/WEB_COMPARISON_TEMPLATE.md
```

**1.2 Archive Related Docs**
```bash
mkdir -p templates/archive/v2-development/
mv templates/V2_MISSING_CAPABILITIES.md templates/archive/v2-development/
mv templates/V2_TEMPLATE_AUDIT.md templates/archive/v2-development/
# Keep V2_FINAL_STATUS.md as usage guide (rename to TEMPLATE_USAGE_GUIDE.md)
mv templates/V2_FINAL_STATUS.md templates/TEMPLATE_USAGE_GUIDE.md
```

**1.3 Archive Old Phased Execution**
```bash
# This is for 150K char approach, no longer relevant
mv templates/WEB_COMPARISON_PHASED_EXECUTION.md templates/archive/WEB_COMPARISON_PHASED_EXECUTION_V1.md
```

**1.4 Update References**
Files to update:
- `templates/TEMPLATE_USAGE_GUIDE.md` - Change "V2_WORKING" → "WEB_COMPARISON_TEMPLATE.md"
- `CLAUDE.md` - Update template references if any
- `CHECKPOINT_DECEMBER_2025.md` - Update template name

---

### 🟡 PHASE 2: Root Directory Cleanup (SHOULD DO)

**2.1 Archive Session Files**
```bash
mkdir -p archive/sessions-2025/
mv SESSION_RECOVERY_SEP25.md archive/sessions-2025/
mv SESSION_SUMMARY_DECEMBER_2025.md archive/sessions-2025/
mv SESSION_SUMMARY_SEPT26.md archive/sessions-2025/
```

**2.2 Archive Old Templates**
```bash
mkdir -p archive/old-templates-2025/
mv COMPETITOR_RESEARCH_TEMPLATE.md archive/old-templates-2025/
```

**2.3 Archive Dated Analysis**
```bash
mkdir -p archive/analysis-2025/
mv COMPETITOR_COMPLETENESS_ANALYSIS.md archive/analysis-2025/
```

**2.4 Delete or Archive**
```bash
# Check if redundant with RESEARCH_QA_CHECKLIST.md
mv RESEARCH_BEST_PRACTICES.md archive/old-docs-2025/ # or delete
```

---

### 🟢 PHASE 3: Competitor Folder Cleanup (NICE TO HAVE)

**3.1 Power BI Copilot Process Files**
```bash
mkdir -p competitors/power-bi-copilot/archive/process-2025/
mv competitors/power-bi-copilot/ENHANCEMENT_*.md competitors/power-bi-copilot/archive/process-2025/
mv competitors/power-bi-copilot/FRAMEWORK_VERIFICATION.md competitors/power-bi-copilot/archive/process-2025/
mv competitors/power-bi-copilot/PHASE_COMPLETION_SUMMARY.md competitors/power-bi-copilot/archive/process-2025/
mv competitors/power-bi-copilot/WEB_COMPARISON_EVALUATION.md competitors/power-bi-copilot/archive/process-2025/
mv competitors/power-bi-copilot/SMART_RESEARCH_PLAN.md competitors/power-bi-copilot/archive/process-2025/
mv competitors/power-bi-copilot/business_impact.md competitors/power-bi-copilot/archive/process-2025/
mv competitors/power-bi-copilot/capability_analysis.md competitors/power-bi-copilot/archive/process-2025/
mv competitors/power-bi-copilot/research_foundation.md competitors/power-bi-copilot/archive/process-2025/
```

**3.2 QA Reports**
- Keep for now (small, useful)
- Future: Could consolidate into RESEARCH_CHECKLIST.md final section

---

## After Cleanup: Final Structure

### Active Templates
```
templates/
├── WEB_COMPARISON_TEMPLATE.md          # ✅ ACTIVE (was V2_WORKING)
├── TEMPLATE_USAGE_GUIDE.md             # 📄 HOW TO USE (was V2_FINAL_STATUS)
├── BATTLE_CARD_TEMPLATE.md             # ✅ ACTIVE
├── COMPETITOR_TEMPLATE.md              # ✅ ACTIVE
├── README_TEMPLATE.md                  # ✅ ACTIVE
├── RESEARCH_GUIDE.md                   # ✅ ACTIVE
└── archive/                            # Historical versions
```

### Active Root Files
```
/
├── README.md                           # ✅ Navigation
├── CLAUDE.md                           # ✅ Instructions for Claude
├── METHODOLOGY.md                      # ✅ BUPAF framework
├── SCOOP_CAPABILITIES.md               # ✅ Product truth
├── RESEARCH_QA_CHECKLIST.md            # ✅ Quality standards
├── POSITIONING_GUIDE.md                # ✅ Sales positioning
├── COMPETITIVE_SUMMARY.md              # ✅ Executive summary
├── EVIDENCE_VAULT.md                   # ✅ Source URLs
├── RESEARCH_ROADMAP.md                 # ✅ Priorities
├── CHANGELOG.md                        # ✅ Change tracking
├── CHECKPOINT_DECEMBER_2025.md         # 📄 Milestone
└── archive/                            # Historical files
```

---

## References to Update

### Critical Updates (must change):
1. **templates/TEMPLATE_USAGE_GUIDE.md**
   - Find: "WEB_COMPARISON_TEMPLATE_V2_WORKING.md"
   - Replace: "WEB_COMPARISON_TEMPLATE.md"
   - Count: Multiple references throughout

2. **CLAUDE.md**
   - Check for web comparison template references
   - Update if needed

3. **CHECKPOINT_DECEMBER_2025.md**
   - Find: "WEB_COMPARISON_TEMPLATE.md" references
   - Verify they refer to new version
   - Update if needed

---

## Verification Commands

**Before cleanup - check references**:
```bash
grep -r "V2_WORKING" --include="*.md" . | grep -v ".git"
grep -r "WEB_COMPARISON_TEMPLATE" --include="*.md" . | grep -v ".git" | wc -l
```

**After cleanup - verify**:
```bash
# Should find no V2_WORKING references
grep -r "V2_WORKING" --include="*.md" . | grep -v ".git" | grep -v "archive"

# Should find clear active template
ls -lh templates/WEB_COMPARISON_TEMPLATE.md

# Should find usage guide
ls -lh templates/TEMPLATE_USAGE_GUIDE.md
```

---

## Benefits

### Clarity
- ✅ Single active web comparison template
- ✅ Clear naming (not "V2_WORKING")
- ✅ Usage guide properly named

### Discoverability
- ✅ New contributors know which template to use
- ✅ No confusion about versions
- ✅ Historical work preserved but separated

### Maintainability
- ✅ Updates go to one place
- ✅ No duplicate maintenance
- ✅ Clear active vs archived distinction

---

## Risk Mitigation

### Nothing Deleted
- All files moved to archive/
- Can retrieve anything if needed
- Git history preserved

### Tested Approach
- Checked for references before moving
- Only 2 docs reference V2_WORKING (both being archived)
- Low risk of broken links

### Reversible
- Simple git revert if issues found
- Archive locations documented
- Can restore original structure

---

## Execution Time Estimate

- **Phase 1** (critical): 10 minutes
  - Move files: 2 minutes
  - Update references: 5 minutes
  - Verify: 3 minutes

- **Phase 2** (cleanup): 5 minutes
  - Move session files: 1 minute
  - Move old templates: 1 minute
  - Move analysis files: 1 minute
  - Verify: 2 minutes

- **Phase 3** (nice to have): 5 minutes
  - Power BI cleanup: 3 minutes
  - Verify: 2 minutes

**Total**: 20 minutes for complete cleanup

---

## Recommendation

**Do Phase 1 NOW** (critical for clarity):
- Single active template
- Clear naming
- Updated references

**Do Phase 2 SOON** (good housekeeping):
- Clean root directory
- Archive session files
- Better organization

**Do Phase 3 LATER** (optional):
- Competitor folder cleanup
- Nice to have, not urgent

---

*Analysis in: CLEANUP_ANALYSIS.md (detailed breakdown)*
*This document: Quick reference for execution*