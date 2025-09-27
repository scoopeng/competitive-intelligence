# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 🚨 CURRENT PROJECT: Deep Competitor Research - Manual Execution

### The Strategy
Execute comprehensive competitor research manually using a consolidated template that produces customer-story-driven intelligence with quantified evidence and maintains a complete research library.

### The Approach
```
Manual Research → Consolidated Template → 41+ Searches → Rich Research Output with URL Library
```

### The Research Process (90-120 minutes per competitor)
1. **Phase 0** - Existing Assets Check (5 min)
   - Check archive and existing research
   - Inventory what's already known
   - Build on existing work
2. **Phase 1** - Deep Discovery & Customer Stories (40-50 min)
   - Customer story mining via G2, Reddit, LinkedIn (17 searches)
   - Industry vertical analysis (healthcare, finance, retail, etc.)
   - Implementation horror stories and switching decisions
3. **Phase 2** - Technical Reality & Competitive Context (30-35 min)
   - Quantified performance data (24 searches)
   - Competitive positioning research and win/loss analysis
   - True TCO including hidden costs and professional services
4. **Phase 3** - Analysis & Rich Sales Enablement (20-25 min)
   - Evidence-based BUA scoring with customer quotes
   - Customer-story-driven battle cards and sales materials
   - Industry-specific objection handlers

### How to Execute
```
1. Copy COMPETITOR_RESEARCH_TEMPLATE.md to competitors/[name]/RESEARCH_CHECKLIST.md
2. Replace {COMPETITOR} with actual name throughout
3. Work through the checklist systematically
4. Build research library as you go (every URL investigated)
5. Check off tasks as completed
6. Can reset and re-run specific phases as needed
```

### Key Files
- **COMPETITOR_RESEARCH_TEMPLATE.md** - Master research checklist
- **RESEARCH_QA_CHECKLIST.md** - Quality assurance standards (REQUIRED before publishing)
- **competitors/[name]/RESEARCH_CHECKLIST.md** - Per-competitor tracking
- **competitors/[name]/evidence/research_library.md** - URL documentation

## Repository Overview

This is a **competitive intelligence documentation repository** for Scoop Analytics, focused on analyzing competitors in the business analytics/BI space through the lens of **business user empowerment**.

### Core Philosophy
- **Business User Autonomy Framework**: Business User Power Assessment - evaluates what users can actually do alone
- **Evidence-Based**: Every claim must have verifiable proof
- **Quality First**: All research must pass RESEARCH_QA_CHECKLIST.md before publishing
- **Preservation-Focused**: Never delete research, only archive if proven wrong
- **Incremental Growth**: Small, methodical improvements over time

## Project Structure

### Root Documents (9 Essential Files)
```
/competitive-intelligence/
├── README.md                  # Navigation & overview
├── COMPETITIVE_SUMMARY.md     # Executive synthesis
├── POSITIONING_GUIDE.md       # Sales messaging
├── SCOOP_CAPABILITIES.md      # Technical differentiators
├── EVIDENCE_VAULT.md          # All source URLs
├── RESEARCH_ROADMAP.md        # Priorities + incremental plan
├── METHODOLOGY.md             # How we work + BUA integration
├── QUICK_START.md            # 2-minute sales prep
└── CLAUDE.md                 # THIS FILE - Project context
```

### Competitor Structure (Current State)
```
competitors/[name]/
├── README.md                       # Navigation
├── BATTLE_CARD.md                 # Sales quick reference (machine-generated)
├── COMPETITIVE_STRATEGY.md        # 🆕 Human-editable positioning strategy
├── research/                      # ALL research (preserve everything!)
│   └── [unlimited docs...]        # Technical, pricing, customer research
├── evidence/                      # Proof & sources
│   ├── framework_scoring.md       # Machine-generated BUA scores
│   ├── research_library.md        # URL documentation
│   └── screenshots/
├── outputs/                       # Web-ready content
│   └── web_comparison.md          # Machine-generated from strategy + scoring
└── tests/                         # Any validation code
```

**Key Innovation**: `COMPETITIVE_STRATEGY.md` allows human strategic decisions (emphasis levels, scenarios, positioning) that machine generation reads to customize output per competitor weakness.

## Competitive Strategy Framework (🆕 September 2025)

### The Enhancement
**Problem**: Generic template missed competitor-specific weaknesses. Snowflake Cortex (NO UI) got same 10% UI emphasis as Power BI (has Teams).

**Solution**: Human-editable `COMPETITIVE_STRATEGY.md` per competitor that machine generation reads.

### Architecture
```
Human writes:   COMPETITIVE_STRATEGY.md (positioning decisions)
                         ↓
Machine reads:  framework_scoring.md (BUA data)
                + COMPETITIVE_STRATEGY.md (strategy)
                         ↓
Machine generates: web_comparison.md (customized output)
```

### 10-Section Strategy File Structure
1. **Primary Weaknesses** - Rank top 3 with emphasis levels (e.g., "UI: 30%")
2. **Key Scenarios** - Stories that expose weaknesses
3. **Talking Points** - What to emphasize/de-emphasize
4. **Content Distribution** - Word count allocation (7,500 words)
5. **Proof Points** - Evidence from BUA scores + research
6. **Win Conditions** - When we win/lose (be honest)
7. **Positioning** - One-sentence + elevator pitch
8. **Avoid Over-Claiming** - Credibility guardrails
9. **Custom Content Blocks** - Competitor-specific examples
10. **Sales Guidance** - Discovery questions, objections

### Example: Content Shift Based on Competitor Weakness

**DEFAULT** (Generic template):
- UI/Workflow: 10% | Excel: 20% | ML: 15% | Cost: 20%

**SNOWFLAKE CORTEX** (No UI):
- UI/Workflow: 30% ⬆️ (0/8 Native Integration)
- Investigation: 25% ⬆️ (0/8 Investigation)
- Cost: 15% ⬇️ (comparable pricing)

**POWER BI COPILOT** (Cost + Reliability):
- Cost: 25% ⬆️ ($67K F64 tax)
- Reliability: 20% ⬆️ (nondeterminism, 3% satisfaction)
- UI: 8% ⬇️ (Teams integration ok)

### Key Files
- **`competitors/SHARED/COMPETITIVE_STRATEGY_TEMPLATE.md`** - Master template with examples
- **`competitors/[name]/COMPETITIVE_STRATEGY.md`** - Per-competitor strategy (human-editable)
- **`COMPETITIVE_STRATEGY_FRAMEWORK.md`** - Complete documentation

### Status
✅ Template created
✅ Snowflake Cortex example (30% UI emphasis)
✅ Power BI Copilot example (25% cost emphasis)
🔄 Rollout to remaining 9 competitors planned

---

## Web Content Generation Framework (December 2025)

### Critical Quality Standards
- **60/40 Rule**: 60% showcasing Scoop innovation, 40% competitor comparison
- **Mandatory Capabilities Checklist**: 40 items that MUST be included
- **All Departments Coverage**: 9 departments minimum
- **Positive Data Team Messaging**: "We enable, not replace"
- **Competitor-Specific Emphasis**: Use COMPETITIVE_STRATEGY.md to customize

### Files for Web Comparison Generation
- **`WEB_COMPARISON_TEMPLATE.md`** - Base template (150K+ chars target)
- **`WEB_COMPARISON_PHASED_EXECUTION.md`** - 4-phase execution framework
- **`competitors/SHARED/`** - Reusable components library
- **`competitors/[name]/COMPETITIVE_STRATEGY.md`** - 🆕 Competitor-specific customization

### Generation Workflow
```bash
# Read competitor strategy file first
cat competitors/[name]/COMPETITIVE_STRATEGY.md

# Then generate with customized emphasis
"Generate web comparison for [competitor] using strategy file"
```

**Output**: `competitors/[name]/outputs/web_comparison.md`
- AEO-optimized for answer engines
- 7,500+ words with competitor-specific emphasis
- Evidence-based, credible, balanced

## Key Principles

1. **Research is Gold**: Never delete, always preserve
2. **Evidence Required**: No claims without proof
3. **BUA Guides**: Focus on business user empowerment
4. **Credibility First**: Better to understate than exaggerate
5. **Incremental Progress**: Small steps, checkpoint often
6. **Build Up More Than Tear Down**: 60% Scoop innovation, 40% competitor gaps
7. **Enable Don't Replace**: Positive messaging for data teams
8. **Comprehensive Coverage**: All audiences, all capabilities

## Current Status (September 2025)

### Framework Redesign ✅ COMPLETE
- **100-Point BUA Framework**: All 12 competitors rescored
- **Mathematical Verification**: All dimension sums = totals
- **Competitive Strategy Files**: Template + 2 examples created
- **Final Scores**: Scoop 82/100 (A Strong) to DataChat 17/100 (D Poor)

### Recent Commits
- `1e449e3` - Framework redesign completion summary
- `d0d54fb` - Competitive strategy framework documentation
- `c9b87df` - Strategy files for Snowflake & Power BI
- `71bf0aa` - Fix final 3 mathematical errors
- `c1bbee6` - Fix 9 mathematical errors from QA
- `e973c31` - Complete 100-point framework redesign

### Next Priorities
1. **Rollout COMPETITIVE_STRATEGY.md** to remaining 9 competitors
2. **Generate web comparisons** using strategy files for customized emphasis
3. **Quarterly maintenance** of existing strategy files

## Common Development Tasks

### Running Improvement Plan
```bash
# Check what needs work
cat COMPETITOR_COMPLETENESS_ANALYSIS.md

# View detailed plan
cat COMPETITOR_IMPROVEMENT_PLAN.md

# Start autonomous improvement
./start_improvement.sh

# Check progress
./check_improvement_status.sh
cat competitors/[name]/IMPROVEMENT_PROGRESS.md
```

### Running Snowflake Cortex Tests
```bash
# Install required dependencies
pip install snowflake-connector-python

# Run the main test suite
python3 competitors/snowflake-cortex/DEFINITIVE_TEST_SUITE.py

# Verify test results
python3 competitors/snowflake-cortex/verify_results.py
```

### Searching for Competitor Information
```bash
# Find specific claims across all competitors
grep -r "SEARCH_TERM" competitors/

# List all competitors
ls competitors/

# Check evidence URLs
cat EVIDENCE_VAULT.md

# Search archives for lost research
find archive/ -name "*competitor-name*"
```

### Repository Navigation
- **Sales Teams**: Start with `QUICK_START.md` and battle cards in `competitors/*/BATTLE_CARD.md`
- **Technical Analysis**: Deep dives in `competitors/*/research/` folders
- **Evidence Verification**: All source URLs in `EVIDENCE_VAULT.md`
- **Methodology**: BUA framework in `framework/` directory
- **Progress Tracking**: `COMPETITOR_COMPLETENESS_ANALYSIS.md`

## High-Level Architecture

### Content Structure
```
/competitive-intelligence/
├── Core Documentation (8 files)
│   ├── README.md                    # Main overview & quick access
│   ├── COMPETITIVE_SUMMARY.md       # Executive overview
│   ├── POSITIONING_GUIDE.md         # Sales messaging framework
│   ├── SCOOP_CAPABILITIES.md        # Technical differentiators
│   ├── EVIDENCE_VAULT.md           # All source URLs
│   ├── QUICK_START.md              # 2-minute sales prep
│   ├── CONTRIBUTING.md             # Maintenance guide
│   └── CHANGELOG.md                # Update tracking
│
├── competitors/                    # 11 competitor folders
│   └── [competitor-name]/         
│       ├── README.md              # Navigation & summary
│       ├── BATTLE_CARD.md         # Sales quick reference
│       └── [analysis files]       # Deep technical analysis
│
├── framework/                      # BUA methodology
├── results/                        # Executive presentations
├── evidence/                       # Screenshots & proof
└── archive/                        # Historical files
```

### Key Competitor Research Areas
1. **Snowflake Cortex**: Most extensive analysis with Python test suite (20+ files)
2. **Domo**: Portal prison and AI capabilities analysis
3. **ThoughtSpot**: Accuracy benchmarking evidence
4. **Others**: Each with battle cards and specific limitation evidence

### BUA Scoring Framework
- **Total Score**: 50 points (5 dimensions × 10 points each)
- **Categories**: 
  - A (35-50): Business Empowerment
  - B (25-34): Analyst Workbench
  - C (15-24): Enterprise Platform
  - D (0-14): Marketing Mirage

## Maintenance Guidelines

### When Adding New Competitors
1. Create folder in `competitors/[name]/`
2. Add `README.md` for navigation
3. Create `BATTLE_CARD.md` for sales
4. Document all evidence with source URLs and dates

### When Updating Existing Content
1. Verify all evidence URLs still work
2. Update pricing if changed
3. Add date to "Last Updated" field
4. Document changes in `CHANGELOG.md`

### Evidence Standards
- Always include source URL and date
- Prefer official vendor documentation
- Document exact quotes when possible
- No speculation without evidence

## Python Testing Dependencies

For running Snowflake tests:
- `snowflake-connector-python`
- Standard library: `json`, `time`, `datetime`, `typing`, `dataclasses`, `enum`

Note: No package management files (requirements.txt, etc.) exist - dependencies are managed manually.