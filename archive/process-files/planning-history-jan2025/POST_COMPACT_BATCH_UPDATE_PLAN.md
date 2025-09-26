# Post-Compact Batch Update Plan

## Current State Before Compact
- ✅ Critical customer docs fixed (README, Executive Presentation)
- ✅ All 11 battle cards complete with 50-point scoring
- ✅ Scoop at realistic 38/50 (76%) in key documents
- ❌ ~43 files still have 40-point references in category folders

## Smart Batch Update Strategy

### Phase 1: Identify Update Patterns
The 40-point references follow predictable patterns:
- Score mentions: "18/40", "36/40", etc.
- Category ranges: "36-40 points", "15-25 points"
- Framework refs: "40 points maximum", "40-point scale"

### Phase 2: Create Sed Script for Batch Updates

#### Pattern 1: Direct Score Replacements
```bash
# Create mapping file for scores
cat > score_mappings.txt << EOF
s/36\/40/38\/50/g
s/24\/40/29\/50/g
s/20\/40/25\/50/g  # Note: Some may need manual review
s/18\/40/23\/50/g
s/16\/40/20\/50/g
s/15\/40/18\/50/g
s/13\/40/17\/50/g
s/12\/40/15\/50/g
s/11\/40/13\/50/g
s/10\/40/12\/50/g
s/9\/40/11\/50/g
s/5\/40/6\/50/g
EOF
```

#### Pattern 2: Category Range Updates
```bash
cat > category_mappings.txt << EOF
s/36-40 points/45-50 points/g
s/26-35 points/33-44 points/g
s/15-25 points/19-32 points/g
s/0-14 points/0-18 points/g
s/40 points maximum/50 points maximum/g
s/40-point/50-point/g
s/(40 points max)/(50 points max)/g
s/TOTAL: X\/40/TOTAL: X\/50/g
EOF
```

### Phase 3: Files to Batch Update

#### Safe for Automatic Update (Clear patterns)
```bash
# Category README files
category-c-analyst/README.md
category-d-mirages/README.md

# Framework templates
framework/BUPAF_EXECUTION_PLAN.md
framework/COMPETITOR_ANALYSIS_TEMPLATE.md
```

#### Need Manual Review (Complex scoring)
```bash
# These have complex analyses that may need context
category-c-analyst/*/COMPREHENSIVE_BUPAF_ANALYSIS.md
category-d-mirages/*/COMPREHENSIVE_BUPAF_ANALYSIS.md
category-d-mirages/tableau-pulse/bupaf-analysis.md
```

### Phase 4: Archive vs Update Decision

#### Archive These (Outdated methodology)
- Files with "COMPREHENSIVE_BUPAF_ANALYSIS" that use old framework
- Old webflow specs with outdated scores
- Session history files

#### Update These (Still relevant)
- Category README files
- Framework templates
- Current analysis files

### Phase 5: Execution Script

```bash
#!/bin/bash
# Post-compact batch update script

# Backup first
git checkout -b batch-update-50-point
git commit -am "Checkpoint before batch update"

# Step 1: Update category READMEs
for file in category-*/README.md; do
  sed -i.bak -f score_mappings.txt "$file"
  sed -i -f category_mappings.txt "$file"
done

# Step 2: Update framework files
for file in framework/*.md; do
  sed -i.bak -f score_mappings.txt "$file"
  sed -i -f category_mappings.txt "$file"
done

# Step 3: Archive old comprehensive analyses
mkdir -p archive/old-40-point-analyses
mv category-*/*/COMPREHENSIVE_BUPAF_ANALYSIS.md archive/old-40-point-analyses/

# Step 4: Update QUICK_COMPARISON_MATRIX (already partially done)
sed -i.bak 's/above 35\/40/above 44\/50/g' results/QUICK_COMPARISON_MATRIX.md
sed -i 's/next best: 20\/40/next best: 25\/50/g' results/QUICK_COMPARISON_MATRIX.md

# Step 5: Commit in batches
git add category-*/README.md
git commit -m "Batch update: Category READMEs to 50-point scale"

git add framework/*.md
git commit -m "Batch update: Framework files to 50-point scale"

git add archive/old-40-point-analyses
git commit -m "Archive: Move old 40-point analyses"
```

## Manual Review Checklist After Batch

1. **Verify Scoop Score**: Should be 38/50 (76%) everywhere
2. **Check Category Thresholds**: 
   - A: 45-50
   - B: 33-44  
   - C: 19-32
   - D: 0-18
3. **Validate Competitor Scores**: Match our matrix
4. **Test Navigation**: Ensure no broken references

## Files That MUST Stay on 40-point (Archived)
- Everything in `/archive/` - these are historical
- They should get a header: "ARCHIVED - Uses outdated 40-point scoring"

## Quick Validation Commands

```bash
# After batch update, check remaining 40-point refs
grep -r "/40" . --include="*.md" --exclude-dir=archive | wc -l
# Should be near 0

# Verify Scoop score consistency
grep -r "38/50" . --include="*.md" | wc -l
# Should match number of files mentioning Scoop score

# Check for missed patterns
grep -r "40 points" . --include="*.md" --exclude-dir=archive
```

## Time Estimate
- Batch script execution: 5 minutes
- Manual review: 30 minutes
- Validation: 15 minutes
- **Total: ~1 hour post-compact**

## Why This Works
1. **Pattern-based**: Most updates follow clear patterns
2. **Safe backups**: Everything backed up before changes
3. **Incremental commits**: Easy to rollback if issues
4. **Archive vs update**: Clear decision criteria
5. **Validation built-in**: Commands to verify success

## Next Session Startup Commands
```bash
# After compact, start here:
cd /home/brad-peters/dev/competitive-intelligence
git status
cat POST_COMPACT_BATCH_UPDATE_PLAN.md

# Run the batch update
chmod +x batch_update_50point.sh
./batch_update_50point.sh

# Validate
grep -r "/40" . --include="*.md" --exclude-dir=archive | wc -l
```

---

**Key Point**: This plan turns a 70-file manual update into a 1-hour mostly-automated process with clear validation.