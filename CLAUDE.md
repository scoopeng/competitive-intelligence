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
- **QUALITY_STANDARDS.md** - Quality assurance standards (REQUIRED before publishing)
- **competitors/[name]/RESEARCH_CHECKLIST.md** - Per-competitor tracking
- **competitors/[name]/evidence/research_library.md** - URL documentation

## Repository Overview

This is a **competitive intelligence documentation repository** for Scoop Analytics, focused on analyzing competitors in the business analytics/BI space through the lens of **business user empowerment**.

### Core Philosophy
- **Business User Autonomy Framework**: Business User Power Assessment - evaluates what users can actually do alone
- **Evidence-Based**: Every claim must have verifiable proof
- **Quality First**: All research must pass QUALITY_STANDARDS.md before publishing
- **Preservation-Focused**: Never delete research, only archive if proven wrong
- **Incremental Growth**: Small, methodical improvements over time

## Project Structure

### Root Documents (14 Essential Files)
```
/competitive-intelligence/
├── START_HERE.md                      # ⭐ Quick context for new sessions (START HERE!)
├── README.md                          # Complete navigation & overview
├── CLAUDE.md                          # THIS FILE - AI assistant guidance
├── QUICK_START.md                     # 2-minute sales prep
├── COMPETITIVE_SUMMARY.md             # Executive synthesis
├── POSITIONING_GUIDE.md               # Sales messaging
├── SCOOP_CAPABILITIES.md              # Technical differentiators
├── CAPABILITY_MATRIX.md               # 26-capability platform comparison
├── EVIDENCE_VAULT.md                  # All source URLs
├── METHODOLOGY.md                     # How we work + BUA integration
├── COMPETITIVE_STRATEGY_FRAMEWORK.md  # Strategy file system
├── QUALITY_STANDARDS.md               # Quality assurance (consolidated)
├── RESEARCH_ROADMAP.md                # Priorities + incremental plan
└── CHANGELOG.md                       # Update tracking
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

## Web Content Generation Framework (September 2025)

### 🚨 Pricing & TCO Guidance (September 28, 2025 - CRITICAL)

**NEVER include specific Scoop dollar amounts in web comparisons.** Scoop's pricing is evolving and specific claims will become outdated.

#### The Problem
Early web comparisons contained wildly inconsistent Scoop pricing:
- ThoughtSpot comparison: "$3,588 for 200 users" ($18/user/year) ❌
- Qlik comparison: "$240,000 for 200 users" ($1,200/user/year) ❌
- Snowflake comparison: "$72,000 for 200 users" ($360/user/year) ❌

**67x variance** between highest and lowest claims for same user count = credibility disaster.

#### The Solution: TCO Framework (Cost Category Elimination)

**Traditional BI platforms have 6 cost categories. Scoop has 1.**

```
Traditional BI TCO = Licenses + Implementation + Training + Maintenance + Consultants + Productivity Loss
                   = 1x      + 2-4x           + 0.5-2x  + 1-2x        + 1-3x        + 2-4x
                   = 7.5x - 16x the license cost

Scoop TCO = Software subscription only
          = 1x (everything else is $0)
```

#### What to Say (Defensible)
✅ "Scoop eliminates implementation cost ($0), training cost ($0), and IT maintenance cost ($0)"
✅ "Typical customers see 10x lower TCO"
✅ "No hidden costs: no consultants, no semantic layer maintenance, no productivity loss during rollout"
✅ "Cost advantage comes from eliminating 5 of 6 cost categories, not cheaper licenses"

#### What NOT to Say (Risky)
❌ "Scoop costs $X for Y users" (pricing is evolving)
❌ "Scoop is X% cheaper" based on license price alone (commoditizes platform)
❌ Any specific Scoop annual contract value

#### Why This Works
1. **Defensible regardless of pricing evolution**: If Scoop licenses increase 10x, the $0 categories remain true
2. **Highlights architectural differentiation**: Implementation = $0 because no data modeling required (architectural fact)
3. **Professional positioning**: "Cost elimination" vs "cheaper alternative"
4. **Evidence-based**: Competitor hidden costs are well-documented with sources

#### Implementation in Templates
- **At-a-Glance Table**: "Fraction of traditional BI TCO" (not dollar amounts)
- **Cost Section**: Full table showing 6 categories, why Scoop eliminates 5
- **FAQ**: "What does {COMPETITOR} really cost?" answers with all categories breakdown

See `WEB_COMPARISON_TEMPLATE.md` Section 3 for full TCO table structure.

---

### AI Data Analyst Positioning (September 27, 2025)
Template now includes "AI data analyst you chat with" positioning aligned with homepage and investor deck.

**7 Positioning Touchpoints Added**:
1. TL;DR: "What is Scoop?" positioning statement
2. Comparison table: "User Experience" section (Primary Interface, Learning Curve)
3. Bottom Line: Uses "AI data analyst you chat with" language
4. FAQ: "What is Scoop?" as first question
5. Section openers: "When you chat with Scoop..." bridges positioning to technical depth

**Result**: Technical capabilities now explicitly SUPPORT positioning. Power BI Copilot updated as reference implementation.

### Critical Quality Standards
- **AI Data Analyst First**: Lead with positioning before technical depth
- **60/40 Rule**: 60% showcasing Scoop innovation, 40% competitor comparison
- **Mandatory Capabilities Checklist**: 40 items that MUST be included
- **All Departments Coverage**: 9 departments minimum
- **Positive Data Team Messaging**: "We enable, not replace"
- **Competitor-Specific Emphasis**: Use COMPETITIVE_STRATEGY.md to customize
- **TCO Focus (NOT Pricing)**: Emphasize cost category elimination, avoid specific Scoop dollar amounts (see below)

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

## Current Status (September 28, 2025)

### Competitive Strategy & Web Comparison Progress
**5 of 11 Competitors Complete** (strategy + web comparison)
- ✅ Power BI Copilot (32/100) - v2.0 strategy, deployed
- ✅ Snowflake Cortex (26/100) - v1.1 strategy, generated
- ✅ Tableau Pulse (37/100) - v1.1 strategy, generated
- ✅ Zenlytic (42/100) - v1.1 strategy, generated
- ✅ [One other from previous work]

**Next Priority**: ThoughtSpot (57/100), Domo (62/100), Qlik (47/100)

**Track Progress**: See `COMPETITOR_STATUS.md` for live status tracker

### Template Evolution
- **Strategy Template**: v1.0 → v1.1 (defensibility framework added Sept 28)
  - Weaknesses classified: Architectural | Temporal | Strategic
  - Emphasis allocation: Architectural (highest) > Strategic > Temporal
  - Product type framing in positioning section

- **Web Comparison Template**: v2.0 → v2.1 (generalizable features added Sept 28)
  - Question Hierarchy subsection (Simple/Complex/Why)
  - Semantic Model Boundary block (optional)
  - 3 new At-a-Glance table rows
  - Complex query FAQ for AEO

### 4 Architectural Patterns Identified (September 28)
1. **YAML/Semantic Layer Dependency** - Snowflake Cortex, Zenlytic (IT must maintain definitions)
2. **Portal Prison** - All dashboard-first competitors (no native Excel/Slack/PowerPoint)
3. **Text-to-SQL = One Query Per Question** - Cannot do multi-pass investigation (7+ queries)
4. **Schema/Metric Brittleness** - Tableau Pulse (400 errors), semantic layers break on changes

### Web Comparison Best Practices (Learned Sept 27-28)
- **Investigation-First Strategy**: Multi-pass investigation is architectural differentiator (30% emphasis)
- **Multi-Turn vs Multi-Pass**: Clarify distinction (follow-up questions ≠ automated investigation)
- **Question Hierarchy**: Simple "What" → Complex "What" → "Why" framework
- **Semantic Model Boundary**: When applicable, explain IT dependency clearly
- **CEO Quotes as Evidence**: Credible (Zenlytic CEO: "90% accuracy is absolutely terrible")
- **Defensibility Drives Emphasis**: Architectural limitations > Strategic choices > Temporal gaps

## Current Status (Legacy - Pre-September 28)

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