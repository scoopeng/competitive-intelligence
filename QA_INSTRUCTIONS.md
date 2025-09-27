# QA Instructions for 100-Point Framework Verification

**Purpose**: Verify all competitive intelligence files are correct and consistent with the 100-point BUA framework.

**Context**: We just completed a major framework redesign from arbitrary 59-point to clean 100-point system. All 12 competitors have been rescored and all files updated.

---

## What to Verify

### 1. Framework Scoring Files (12 files)
**Location**: `/home/ubuntu/dev/competitive-intelligence/competitors/*/evidence/framework_scoring.md`

**Check Each File For**:
- ✅ **Header** shows: `Total Score: X/100 (Y%, Category Z)`
- ✅ **Dimensions** all show `/20` (not /10, /16, /13, etc.)
- ✅ **Sub-components** match this structure:
  - Autonomy (/20): Setup /8, Questions /6, Speed /6
  - Flow (/20): Native Integration /8, Portal Prison /6, Interface Simplicity /6
  - Understanding (/20): Investigation /8, ML /6, Explanation /6
  - Presentation (/20): Automatic Generation /8, Brand Control /6, Distribution /6
  - Data (/20): Multi-Source /4, Schema Evolution /8, Data Quality /4, Data Prep /4
- ✅ **Math is correct**: Sub-components add to dimension, dimensions add to total
- ✅ **Category matches score**:
  - A+ Elite (85-100)
  - A Strong (70-84)
  - B Good (55-69)
  - C Moderate (40-54)
  - C Weak (25-39)
  - D Poor (0-24)
- ✅ **No old references**: No "/50", "/59", "BUPAF", "Marketing Mirage"
- ✅ **Date**: September 27, 2025 or later

**Expected Scores** (verify these exactly):
```
Scoop: 82/100 (A Strong)
Domo: 62/100 (B Good)
ThoughtSpot: 56/100 (B Good)
Qlik: 46/100 (C Moderate)
Zenlytic: 44/100 (C Moderate)
Sisense: 38/100 (C Moderate)
Tableau Pulse: 36/100 (C Weak)
Snowflake Cortex: 34/100 (C Weak)
Power BI Copilot: 32/100 (C Weak)
DataGPT: 30/100 (C Weak)
Tellius: 30/100 (C Weak)
DataChat: 28/100 (D Poor)
```

### 2. Battle Cards (11 files)
**Location**: `/home/ubuntu/dev/competitive-intelligence/competitors/*/BATTLE_CARD.md`

**Check Each File For**:
- ✅ **Header** shows: `BUA Score: X/100 (Y%, Category Z)`
- ✅ **Score matches** framework_scoring.md
- ✅ **Category name** is correct (not old names)
- ✅ **No "/50" or "/59"** anywhere

### 3. README Files (11 files)
**Location**: `/home/ubuntu/dev/competitive-intelligence/competitors/*/README.md`

**Check Each File For**:
- ✅ **BUA Score** (if mentioned) matches framework_scoring.md
- ✅ **Category** matches framework_scoring.md
- ✅ **No "BUPAF"** (should be "BUA")
- ✅ **No "/50" or "/59"** in scoring references

### 4. Web Comparisons (11 files)
**Location**: `/home/ubuntu/dev/competitive-intelligence/competitors/*/outputs/web_comparison.md`

**Check Each File For**:
- ✅ **File exists**
- ✅ **Header** shows competitor score as X/100
- ✅ **Last Updated**: September 27, 2025
- ✅ **Score matches** framework_scoring.md
- ✅ **Word count**: 4,000+ words minimum
- ✅ **No old references**: No /50, /59, BUPAF

### 5. Core Framework Document (1 file)
**Location**: `/home/ubuntu/dev/competitive-intelligence/framework/BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md`

**Check**:
- ✅ **Structure**: Shows 5 dimensions × 20 points = 100 total
- ✅ **Categories**: Use 100-point ranges (not 50-point)
- ✅ **Examples**: Use 100-point scores
- ✅ **No old references**: No /50, /59 system

---

## How to Verify Mathematical Accuracy

For each framework_scoring.md file:

1. **Extract dimension scores** from these lines:
   - `## Dimension 1: Autonomy (X/20)`
   - `## Dimension 2: Flow (X/20)`
   - `## Dimension 3: Understanding (X/20)`
   - `## Dimension 4: Presentation (X/20)`
   - `## Dimension 5: Data (X/20)`

2. **Add them up**: Sum of all 5 dimensions

3. **Compare to header**: Does sum match `Total Score: X/100`?

4. **Check sub-components**: Do they add to dimension total?

**Example (Power BI Copilot)**:
- Autonomy: 7/20 (should be 2+3+2 = 7) ✅
- Flow: 6/20 (should be 3+0+3 = 6) ✅
- Understanding: 7/20 (should be 2+0+5 = 7) ✅
- Presentation: 6/20 (should be 3+1+2 = 6) ✅
- Data: 6/20 (should be 1+0+3+2 = 6) ✅
- **Total**: 7+6+7+6+6 = 32/100 ✅

---

## Critical Issues to Flag

**Priority 1 (Blocker)**:
- ❌ Math doesn't add up (dimensions ≠ total)
- ❌ Score mismatch between files (framework_scoring.md vs battle card)
- ❌ Wrong dimension structure (not /20)
- ❌ Category doesn't match score range

**Priority 2 (Important)**:
- ⚠️ Old references still present (/50, /59, BUPAF)
- ⚠️ Missing sub-component scores
- ⚠️ Outdated dates (before Sept 27, 2025)

**Priority 3 (Nice to Fix)**:
- 💡 Web comparison under 4,000 words
- 💡 Missing evidence citations
- 💡 Formatting inconsistencies

---

## QA Report Format

For each category checked, report:

```markdown
### [Category Name] (X/Y files checked)

**Status**: ✅ PASS / ⚠️ MINOR ISSUES / ❌ CRITICAL ISSUES

#### Issues Found:
- **[Priority]** [file_path]: [issue description]
- **[Priority]** [file_path]: [issue description]

#### Files Passing All Checks:
- [list all files with no issues]
```

---

## Final Deliverable

Provide comprehensive QA report with:

1. **Executive Summary**: Pass/fail status
2. **Statistics**: Files checked, pass rate, issue count
3. **Detailed Findings**: By category with specific issues
4. **Priority Issues**: Blockers listed first
5. **Recommendation**: "Ready for production" or "Needs fixes before production"

---

## Quick Verification Commands

```bash
# Check all framework scoring totals
for comp in scoop power-bi-copilot tableau-pulse thoughtspot snowflake-cortex domo qlik zenlytic sisense datagpt tellius datachat; do
  echo "=== $comp ===" 
  grep "Total Score:" /home/ubuntu/dev/competitive-intelligence/competitors/$comp/evidence/framework_scoring.md | head -1
done

# Check for old references in active files
grep -r "/50\|/59\|BUPAF" /home/ubuntu/dev/competitive-intelligence/competitors/*/evidence/framework_scoring.md
grep -r "/50\|/59\|BUPAF" /home/ubuntu/dev/competitive-intelligence/competitors/*/BATTLE_CARD.md
grep -r "/50\|/59\|BUPAF" /home/ubuntu/dev/competitive-intelligence/competitors/*/README.md

# Verify dimension structure
for comp in scoop power-bi-copilot tableau-pulse thoughtspot; do
  echo "=== $comp ===" 
  grep "^## Dimension" /home/ubuntu/dev/competitive-intelligence/competitors/$comp/evidence/framework_scoring.md
done

# Check web comparison existence and word count
for comp in power-bi-copilot tableau-pulse thoughtspot snowflake-cortex domo qlik zenlytic sisense datagpt tellius datachat; do
  file="/home/ubuntu/dev/competitive-intelligence/competitors/$comp/outputs/web_comparison.md"
  if [ -f "$file" ]; then
    wc=$(wc -w "$file" | awk '{print $1}')
    echo "✓ $comp: $wc words"
  else
    echo "✗ $comp: MISSING"
  fi
done
```

---

## Context for QA Agent

**What was done**:
- Rescaled framework from 59-point to 100-point system
- Updated all 12 competitor framework_scoring.md files
- Fixed 8 files with mathematical errors
- Updated 11 battle cards, 11 READMEs, generated 11 web comparisons
- Removed all old framework references from active files
- Committed everything to git

**What needs verification**:
- Math is correct everywhere
- Scores are consistent across all file types
- No old references remain in active files
- Categories match score ranges
- All required files exist and are complete

**Known good files** (verified manually):
- Scoop: 82/100 ✅
- Power BI Copilot: 32/100 ✅
- Domo: 62/100 ✅
- ThoughtSpot: 56/100 ✅

**Files that had issues fixed**:
- Qlik, Tableau Pulse, Zenlytic, Snowflake Cortex (math errors)
- DataChat, DataGPT, Sisense, Tellius (missing structures)

**Expected outcome**: All 12 competitors should pass all checks with no critical issues.

---

**Last Updated**: September 27, 2025  
**Framework Version**: Business User Autonomy Framework (100-point system)  
**Total Files to Check**: 46 files (12 framework_scoring + 11 battle cards + 11 READMEs + 11 web comparisons + 1 core framework)
