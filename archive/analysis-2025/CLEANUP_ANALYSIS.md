# Repository Cleanup Analysis
**Date**: September 27, 2025
**Focus**: Recent files added, template consolidation, version control

---

## Current State: Template Files

### Templates Directory Analysis

| File | Size | Status | Action |
|------|------|--------|--------|
| **WEB_COMPARISON_TEMPLATE_V2_WORKING.md** | 48K | ✅ ACTIVE | **RENAME** to WEB_COMPARISON_TEMPLATE.md |
| WEB_COMPARISON_TEMPLATE.md | 28K | ⚠️ OLD VERSION | **ARCHIVE** |
| WEB_COMPARISON_PHASED_EXECUTION.md | 13K | ⚠️ REFERENCES OLD | **UPDATE** or **ARCHIVE** |
| V2_FINAL_STATUS.md | 14K | 📄 DOCUMENTATION | **KEEP** (usage guide) |
| V2_MISSING_CAPABILITIES.md | 13K | 📄 ANALYSIS | **ARCHIVE** (historical) |
| V2_TEMPLATE_AUDIT.md | 16K | 📄 ANALYSIS | **ARCHIVE** (historical) |
| WEB_CONTENT_SPEC.md | 9.4K | ⚠️ OLD SPEC | **ARCHIVE** or **DELETE** |
| BATTLE_CARD_TEMPLATE.md | 3.1K | ✅ ACTIVE | **KEEP** |
| COMPETITOR_TEMPLATE.md | 8.8K | ✅ ACTIVE | **KEEP** |
| README_TEMPLATE.md | 3.5K | ✅ ACTIVE | **KEEP** |
| RESEARCH_GUIDE.md | 7.2K | ✅ ACTIVE | **KEEP** |

### PROBLEM: Multiple Versions Active

**Current confusion**:
- `WEB_COMPARISON_TEMPLATE.md` (old, 28K)
- `WEB_COMPARISON_TEMPLATE_V2_WORKING.md` (new, 48K)

**Solution**:
1. Rename V2_WORKING → WEB_COMPARISON_TEMPLATE.md (replace old)
2. Archive old version → templates/archive/WEB_COMPARISON_TEMPLATE_V1.md
3. Update any references in other docs

---

## Root Directory Analysis

### Session/Process Files (Should Archive)

| File | Size | Purpose | Action |
|------|------|---------|--------|
| SESSION_RECOVERY_SEP25.md | 7.9K | Recovery notes | **ARCHIVE** → archive/sessions/ |
| SESSION_SUMMARY_DECEMBER_2025.md | 6.9K | Session notes | **ARCHIVE** → archive/sessions/ |
| SESSION_SUMMARY_SEPT26.md | 3.1K | Session notes | **ARCHIVE** → archive/sessions/ |
| COMPETITOR_RESEARCH_TEMPLATE.md | 24K | Old research template | **ARCHIVE** → archive/old-templates/ |
| RESEARCH_BEST_PRACTICES.md | 2.7K | Consolidated elsewhere | **ARCHIVE** or **DELETE** |

### Analysis Files (Keep or Archive)

| File | Size | Purpose | Action |
|------|------|---------|--------|
| CHECKPOINT_DECEMBER_2025.md | 4.3K | Framework validation | **KEEP** (historical milestone) |
| COMPETITOR_COMPLETENESS_ANALYSIS.md | 9.3K | Status snapshot | **ARCHIVE** → archive/analysis/ (dated) |
| V2_TEMPLATE_AUDIT.md (in root?) | - | Should be in templates/ | **CHECK** if duplicate |

### Active Core Files (Keep)

| File | Size | Purpose | Status |
|------|------|---------|--------|
| README.md | 17K | Repository navigation | ✅ ACTIVE |
| CLAUDE.md | 12K | Claude Code instructions | ✅ ACTIVE |
| METHODOLOGY.md | 11K | BUPAF methodology | ✅ ACTIVE |
| SCOOP_CAPABILITIES.md | 17K | Product truth source | ✅ ACTIVE |
| RESEARCH_QA_CHECKLIST.md | 13K | Quality standards | ✅ ACTIVE |
| POSITIONING_GUIDE.md | 7.0K | Sales positioning | ✅ ACTIVE |
| COMPETITIVE_SUMMARY.md | 6.5K | Executive summary | ✅ ACTIVE |
| EVIDENCE_VAULT.md | 16K | Source URLs | ✅ ACTIVE |
| RESEARCH_ROADMAP.md | 9.0K | Priorities | ✅ ACTIVE |
| CHANGELOG.md | 2.9K | Change tracking | ✅ ACTIVE |

---

## Competitor Folders: Analysis Files to Clean

### Power BI Copilot (Most Cluttered)

**Process Files** (can archive):
- ENHANCEMENT_REQUIRED.md (4.2K) - process notes
- ENHANCEMENT_SUMMARY.md (6.0K) - process notes
- FRAMEWORK_VERIFICATION.md (4.5K) - process notes
- PHASE_COMPLETION_SUMMARY.md (3.4K) - process notes
- WEB_COMPARISON_EVALUATION.md (9.3K) - process notes
- SMART_RESEARCH_PLAN.md (3.0K) - old plan
- business_impact.md (17K) - working doc
- capability_analysis.md (12K) - working doc
- research_foundation.md (7.1K) - working doc

**Keep**:
- README.md
- BATTLE_CARD.md
- RESEARCH_CHECKLIST.md
- evidence/* (all)
- outputs/web_comparison.md (final)

**Action**: Move process files to competitors/power-bi-copilot/archive/process-2025/

### Other Competitors: QA Reports

Files like:
- datachat/QA_REPORT.md
- qlik/QA_REPORT.md
- tellius/QA_REPORT.md

**Action**: These are useful quality checks - KEEP for now, but could consolidate into RESEARCH_CHECKLIST.md as a final section

### Snowflake Cortex: Already Well Archived

- Large archive/ directory already exists
- Current files are clean
- No action needed

---

## Proposed Cleanup Actions

### PHASE 1: Template Consolidation (CRITICAL)

**Renames** (replace old with new):
```bash
# Backup old version
mv templates/WEB_COMPARISON_TEMPLATE.md templates/archive/WEB_COMPARISON_TEMPLATE_V1_DEPRECATED.md

# Promote V2 to active
mv templates/WEB_COMPARISON_TEMPLATE_V2_WORKING.md templates/WEB_COMPARISON_TEMPLATE.md

# Update references in other files
```

**Archive analysis docs**:
```bash
mkdir -p templates/archive/v2-development/
mv templates/V2_MISSING_CAPABILITIES.md templates/archive/v2-development/
mv templates/V2_TEMPLATE_AUDIT.md templates/archive/v2-development/
# Keep V2_FINAL_STATUS.md as usage guide
```

**Update V2_FINAL_STATUS.md references**:
- Change all references from "V2_WORKING" to "WEB_COMPARISON_TEMPLATE.md"

---

### PHASE 2: Root Directory Cleanup

**Archive session files**:
```bash
mkdir -p archive/sessions-2025/
mv SESSION_RECOVERY_SEP25.md archive/sessions-2025/
mv SESSION_SUMMARY_DECEMBER_2025.md archive/sessions-2025/
mv SESSION_SUMMARY_SEPT26.md archive/sessions-2025/
```

**Archive old templates**:
```bash
mkdir -p archive/old-templates-2025/
mv COMPETITOR_RESEARCH_TEMPLATE.md archive/old-templates-2025/
```

**Archive or delete**:
```bash
# These might be redundant with RESEARCH_QA_CHECKLIST.md
mv RESEARCH_BEST_PRACTICES.md archive/old-docs-2025/ # or delete
```

**Archive dated analysis**:
```bash
mkdir -p archive/analysis-2025/
mv COMPETITOR_COMPLETENESS_ANALYSIS.md archive/analysis-2025/
```

---

### PHASE 3: Competitor Folder Cleanup

**Power BI Copilot**:
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

**Other competitors** (if needed):
```bash
# QA reports can stay for now - they're small and useful
# Could consolidate later into RESEARCH_CHECKLIST.md
```

---

### PHASE 4: Update References

Files that may reference old template names:

**Check and update**:
1. `CLAUDE.md` - Update web comparison template references
2. `templates/WEB_COMPARISON_PHASED_EXECUTION.md` - Update or archive
3. `templates/V2_FINAL_STATUS.md` - Update all "V2_WORKING" references
4. `CHECKPOINT_DECEMBER_2025.md` - Update template name references
5. `README.md` - Verify template links are correct

---

## Final Structure After Cleanup

### templates/ Directory

```
templates/
├── WEB_COMPARISON_TEMPLATE.md          # ✅ ACTIVE (was V2_WORKING)
├── WEB_COMPARISON_PHASED_EXECUTION.md  # ✅ ACTIVE (or archive if obsolete)
├── V2_FINAL_STATUS.md                  # 📄 USAGE GUIDE
├── BATTLE_CARD_TEMPLATE.md             # ✅ ACTIVE
├── COMPETITOR_TEMPLATE.md              # ✅ ACTIVE
├── README_TEMPLATE.md                  # ✅ ACTIVE
├── RESEARCH_GUIDE.md                   # ✅ ACTIVE
└── archive/
    ├── WEB_COMPARISON_TEMPLATE_V1_DEPRECATED.md
    ├── WEB_CONTENT_SPEC.md (if archived)
    └── v2-development/
        ├── V2_MISSING_CAPABILITIES.md
        └── V2_TEMPLATE_AUDIT.md
```

### Root Directory

```
/
├── README.md                           # ✅ ACTIVE
├── CLAUDE.md                           # ✅ ACTIVE
├── METHODOLOGY.md                      # ✅ ACTIVE
├── SCOOP_CAPABILITIES.md               # ✅ ACTIVE
├── RESEARCH_QA_CHECKLIST.md            # ✅ ACTIVE
├── POSITIONING_GUIDE.md                # ✅ ACTIVE
├── COMPETITIVE_SUMMARY.md              # ✅ ACTIVE
├── EVIDENCE_VAULT.md                   # ✅ ACTIVE
├── RESEARCH_ROADMAP.md                 # ✅ ACTIVE
├── CHANGELOG.md                        # ✅ ACTIVE
├── CHECKPOINT_DECEMBER_2025.md         # 📄 MILESTONE
└── archive/
    ├── sessions-2025/
    │   ├── SESSION_RECOVERY_SEP25.md
    │   ├── SESSION_SUMMARY_DECEMBER_2025.md
    │   └── SESSION_SUMMARY_SEPT26.md
    ├── old-templates-2025/
    │   └── COMPETITOR_RESEARCH_TEMPLATE.md
    └── analysis-2025/
        └── COMPETITOR_COMPLETENESS_ANALYSIS.md
```

### Competitor Folders

```
competitors/{name}/
├── README.md                           # ✅ ACTIVE
├── BATTLE_CARD.md                      # ✅ ACTIVE
├── RESEARCH_CHECKLIST.md               # ✅ ACTIVE
├── evidence/                           # ✅ ACTIVE (all files)
├── research/                           # ✅ ACTIVE (consolidated)
├── outputs/                            # ✅ ACTIVE (web comparison, etc.)
└── archive/                            # 📄 PROCESS DOCS (if needed)
```

---

## Benefits of Cleanup

### Clarity
- One active template, clearly named
- No confusion about which version to use
- Historical work preserved but separated

### Maintainability
- Easier to find current files
- Process docs archived but accessible
- Clear "active vs historical" distinction

### Repository Size
- Not deleting anything (can always retrieve)
- Just organizing better
- Future: Could delete truly obsolete files

---

## Execution Priority

### MUST DO (Critical for clarity):
1. **Rename V2_WORKING → WEB_COMPARISON_TEMPLATE.md**
2. **Archive old WEB_COMPARISON_TEMPLATE.md**
3. **Update V2_FINAL_STATUS.md references**
4. **Update CLAUDE.md references**

### SHOULD DO (Cleanup):
5. Archive session files
6. Archive old templates
7. Clean Power BI process files
8. Update or archive WEB_COMPARISON_PHASED_EXECUTION.md

### NICE TO HAVE (Organization):
9. Archive dated analysis files
10. Consolidate QA reports (future)
11. Review and cleanup archive/ directories (future)

---

## Risk Assessment

### Low Risk
- Archiving session files (never referenced)
- Archiving analysis docs (historical)
- Moving process files (not referenced elsewhere)

### Medium Risk
- Renaming active template (must update references)
- Archiving WEB_COMPARISON_PHASED_EXECUTION.md (check if still used)

### To Verify Before Acting
1. Does anything reference "V2_WORKING"? (grep check)
2. Is WEB_COMPARISON_PHASED_EXECUTION.md still relevant?
3. Are there any hard-coded paths in scripts?

---

*Analysis Complete: Ready for execution*
*Recommendation: Start with Phase 1 (template consolidation), then Phase 2 (root cleanup)*