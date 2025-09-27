# START HERE - Competitive Intelligence Repository

**Last Updated**: September 27, 2025
**Status**: Production Ready
**Framework**: 100-Point BUA System

---

## Quick Status

### ✅ Completed
- **100-Point Framework**: All 12 competitors rescored
- **Mathematical Verification**: All dimension sums = totals (verified)
- **Web Comparisons**: 11 competitors (7,000+ words each)
- **Competitive Strategy Framework**: Template + 2 examples

### 🔄 In Progress
- Rollout COMPETITIVE_STRATEGY.md to remaining 9 competitors
- Generate customized web comparisons using strategy files

---

## Final Scores (100-Point BUA Framework)

```
Rank  Competitor         Score      Category       Gap to Scoop
----  -----------------  ---------  -------------  ------------
  1   Scoop              82/100     A Strong       —
  2   Domo               62/100     B Good         -20
  3   ThoughtSpot        57/100     B Good         -25
  4   Qlik               47/100     C Moderate     -35
  5   Zenlytic           42/100     C Moderate     -40
  6   Tableau Pulse      37/100     C Weak         -45
  7   Power BI Copilot   32/100     D Weak         -50
  8   Sisense            28/100     C Weak         -54
  9   Snowflake Cortex   26/100     C Weak         -56
 10   DataGPT            22/100     D Poor         -60
 11   Tellius            22/100     D Poor         -60
 12   DataChat           17/100     D Poor         -65
```

**Category Ranges**:
- A+ Elite (85-100) | A Strong (70-84) | B Good (55-69)
- C Moderate (40-54) | C Weak (25-39) | D Poor (0-24)

---

## 🆕 Competitive Strategy Framework

### The Enhancement (September 2025)

**Problem**: Generic template applied to all competitors missed specific weaknesses.

**Solution**: Human-editable `COMPETITIVE_STRATEGY.md` per competitor.

**Example**:
- Snowflake Cortex (NO UI): 30% UI emphasis vs 10% default
- Power BI Copilot ($67K tax): 25% cost emphasis vs 15% default

### Architecture
```
Human writes:    COMPETITIVE_STRATEGY.md (positioning strategy)
                          ↓
Machine reads:   framework_scoring.md (BUA data)
                 + COMPETITIVE_STRATEGY.md (strategy)
                          ↓
Machine generates: web_comparison.md (customized output)
                   BATTLE_CARD.md (customized output)
```

### 10-Section Strategy File
1. Primary Weaknesses (top 3 with emphasis levels)
2. Key Scenarios (stories that expose gaps)
3. Talking Points (what to emphasize/de-emphasize)
4. Content Distribution (word count allocation)
5. Proof Points (evidence from BUA + research)
6. Win Conditions (when we win/lose)
7. Positioning (one-sentence + elevator pitch)
8. Avoid Over-Claiming (credibility guardrails)
9. Custom Content Blocks (competitor-specific examples)
10. Sales Guidance (discovery questions, objections)

### Current Examples
✅ **Snowflake Cortex**: `competitors/snowflake-cortex/COMPETITIVE_STRATEGY.md`
- Primary weakness: No UI (30% emphasis)
- Key scenario: "CEO texts at 9 PM from phone"
- Position: "SQL tool for engineers vs analytics for business users"

✅ **Power BI Copilot**: `competitors/power-bi-copilot/COMPETITIVE_STRATEGY.md`
- Primary weakness: $67K infrastructure + nondeterminism (50% combined)
- Key scenario: "Same question, different answers"
- Position: "Nondeterministic add-on vs deterministic platform"

### Template Location
`competitors/SHARED/COMPETITIVE_STRATEGY_TEMPLATE.md`

---

## Repository Structure

```
/competitive-intelligence/
├── START_HERE.md                     # THIS FILE - Quick context
├── COMPETITIVE_STRATEGY_FRAMEWORK.md # Framework documentation
├── FRAMEWORK_REDESIGN_COMPLETE.md    # 100-point completion summary
├── CLAUDE.md                         # AI assistant guidance
│
├── framework/
│   └── BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md  # 100-point BUA framework
│
├── competitors/
│   ├── SHARED/
│   │   ├── COMPETITIVE_STRATEGY_TEMPLATE.md    # Strategy template
│   │   └── [reusable components]
│   │
│   └── [competitor-name]/
│       ├── README.md                           # Navigation
│       ├── BATTLE_CARD.md                     # Sales quick reference
│       ├── COMPETITIVE_STRATEGY.md            # 🆕 Human-editable strategy
│       ├── evidence/
│       │   ├── framework_scoring.md           # Machine-generated BUA
│       │   └── research_library.md            # URL documentation
│       └── outputs/
│           └── web_comparison.md              # Machine-generated (7,500+ words)
│
└── archive/                          # Historical files preserved
```

---

## Key Principles

1. **Research is Gold**: Never delete, always preserve
2. **Evidence Required**: No claims without proof (BUA scores + research)
3. **Credibility First**: Better to understate than exaggerate
4. **Competitor-Specific**: Use strategy files to customize emphasis
5. **Incremental Growth**: Small, methodical improvements over time
6. **Build Up > Tear Down**: 60% Scoop innovation, 40% competitor gaps

---

## Common Tasks

### For New Competitor Analysis:

1. **Complete research** using `COMPETITOR_RESEARCH_TEMPLATE.md`
2. **Generate framework_scoring.md** (BUA scores from research)
3. **Write COMPETITIVE_STRATEGY.md** using template
   - Identify top 3 weaknesses from BUA scores
   - Define emphasis levels (e.g., "UI: 30%")
   - Write 2-3 key scenarios
   - Define win conditions
4. **Generate web_comparison.md** reading both files above
5. **Generate BATTLE_CARD.md** for sales team

### For Updating Existing Competitors:

**Quarterly Review**:
- Check if competitor launched new features
- Update BUA scores if capabilities changed
- Adjust COMPETITIVE_STRATEGY.md emphasis levels
- Regenerate web_comparison.md with new strategy

**Triggered Updates**:
- Competitor announces major changes → Update immediately
- Win/loss analysis reveals new patterns → Update win conditions
- Sales reports different objections → Update talking points

### For Sales Enablement:

1. **Quick reference**: Read `competitors/[name]/BATTLE_CARD.md`
2. **Deep dive**: Read `competitors/[name]/outputs/web_comparison.md`
3. **Discovery questions**: Check `COMPETITIVE_STRATEGY.md` Section 10
4. **Positioning**: Use elevator pitch from `COMPETITIVE_STRATEGY.md` Section 7

---

## Verification Commands

### Check BUA Score Mathematical Accuracy
```bash
for comp in scoop power-bi-copilot tableau-pulse thoughtspot snowflake-cortex domo qlik zenlytic sisense datagpt tellius datachat; do
  file="competitors/$comp/evidence/framework_scoring.md"
  total=$(grep "Total Score" "$file" | head -1 | grep -oE "[0-9]+/100" | cut -d/ -f1)
  dims=$(grep -E "^##+ Dimension [0-9]:" "$file" | grep -oE "[0-9]+/20" | cut -d/ -f1 | paste -sd+ | bc)
  if [ "$total" = "$dims" ]; then
    echo "✓ $comp: $total = $dims"
  else
    echo "✗ $comp: $total ≠ $dims"
  fi
done
```

Expected: All 12 show ✓

### List All Competitors with BUA Scores
```bash
for comp in competitors/*/evidence/framework_scoring.md; do
  name=$(basename $(dirname $(dirname $comp)))
  score=$(grep "Total Score:" "$comp" | head -1 | grep -oE "[0-9]+/100")
  category=$(grep "Category" "$comp" | head -1 | grep -oE "Category [A-D]+ [^)]*" | sed 's/Category //')
  printf "%-20s %s  %s\n" "$name" "$score" "$category"
done | sort -t'/' -k1 -rn
```

### Check Strategy File Status
```bash
echo "=== COMPETITIVE_STRATEGY.md STATUS ==="
for comp in scoop power-bi-copilot tableau-pulse thoughtspot snowflake-cortex domo qlik zenlytic sisense datagpt tellius datachat; do
  if [ -f "competitors/$comp/COMPETITIVE_STRATEGY.md" ]; then
    echo "✓ $comp: Strategy file exists"
  else
    echo "✗ $comp: NO STRATEGY FILE (needs creation)"
  fi
done
```

---

## Reference Documents

### Core Framework
- **`framework/BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md`** - 100-point BUA framework definition
- **`COMPETITIVE_STRATEGY_FRAMEWORK.md`** - Strategy file framework and usage

### Examples & Templates
- **`competitors/SHARED/COMPETITIVE_STRATEGY_TEMPLATE.md`** - Master template
- **`competitors/snowflake-cortex/COMPETITIVE_STRATEGY.md`** - Example (No UI competitor)
- **`competitors/power-bi-copilot/COMPETITIVE_STRATEGY.md`** - Example (Cost + reliability)

### Quality & Process
- **`QUALITY_STANDARDS.md`** - Quality assurance (framework verification, research standards, best practices)

### AI Assistant Guidance
- **`CLAUDE.md`** - Complete project context for AI assistant
- Includes research process, framework details, common tasks

---

## Recent Major Updates

### September 27, 2025 - Framework Redesign Complete
- ✅ Rescaled from 59-point to 100-point system
- ✅ All 12 competitors rescored (17-82 range)
- ✅ Fixed 12 mathematical errors (dimension sums now match totals)
- ✅ Generated 11 web comparisons (7,000+ words each)
- ✅ Created competitive strategy framework
- ✅ Implemented 2 strategy file examples

### Git Commits (Most Recent)
```
d0d54fb  Add comprehensive framework documentation
c9b87df  Add COMPETITIVE_STRATEGY framework for positioning
1e449e3  Add framework redesign completion summary
4690635  Update documentation to reflect completion
71bf0aa  Fix remaining 3 mathematical errors
c1bbee6  Fix 9 mathematical errors
e973c31  Complete 100-point BUA framework redesign
```

---

## Next Session Quick Start

1. **Review current status**: You're here ✓
2. **Check competitor to work on**: See "Strategy File Status" above
3. **Read template**: `competitors/SHARED/COMPETITIVE_STRATEGY_TEMPLATE.md`
4. **Read examples**: Snowflake Cortex or Power BI Copilot strategy files
5. **Create new strategy file**: Copy template, customize for competitor
6. **Generate web comparison**: Use strategy file for customized emphasis

---

## Questions?

- **Framework questions**: See `COMPETITIVE_STRATEGY_FRAMEWORK.md`
- **BUA scoring questions**: See `framework/BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md`
- **AI assistant context**: See `CLAUDE.md`
- **Template usage**: See `competitors/SHARED/COMPETITIVE_STRATEGY_TEMPLATE.md`

---

**Status**: Production Ready
**Framework Version**: 1.0 (100-point system)
**Last Verified**: September 27, 2025