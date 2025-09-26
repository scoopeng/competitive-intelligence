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
   - Evidence-based BUPAF scoring with customer quotes
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
- **competitors/[name]/RESEARCH_CHECKLIST.md** - Per-competitor tracking
- **competitors/[name]/evidence/research_library.md** - URL documentation

## Repository Overview

This is a **competitive intelligence documentation repository** for Scoop Analytics, focused on analyzing competitors in the business analytics/BI space through the lens of **business user empowerment**.

### Core Philosophy
- **BUPAF Framework**: Business User Power Assessment - evaluates what users can actually do alone
- **Evidence-Based**: Every claim must have verifiable proof
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
├── METHODOLOGY.md             # How we work + BUPAF integration
├── QUICK_START.md            # 2-minute sales prep
└── CLAUDE.md                 # THIS FILE - Project context
```

### Competitor Structure (Goal State)
```
competitors/[name]/
├── README.md                    # Navigation
├── BATTLE_CARD.md              # Sales quick reference
├── research/                   # ALL research (preserve everything!)
│   └── [unlimited docs...]     # Technical, pricing, customer research
├── evidence/                   # Proof & sources
│   ├── links.md
│   ├── quotes.md
│   └── screenshots/
├── outputs/                    # Web-ready content
│   ├── web_comparison.md      # 150K char AEO-optimized comparison
│   ├── landing_page.md
│   └── email_campaigns.md
└── tests/                      # Any validation code
```

## Web Content Generation Framework (Updated December 2025)

### Critical Learnings from Power BI Copilot Evaluation
**Problem Identified**: Previous comparisons were 80% negative (tearing down competitor) and only 20% positive (building up Scoop). This missed key Scoop capabilities and narrowed audience appeal.

**Solution Implemented**: Templates now enforce:
- **60/40 Rule**: 60% showcasing Scoop innovation, 40% competitor comparison
- **Mandatory Capabilities Checklist**: 40 items that MUST be included
- **All Departments Coverage**: 9 departments minimum
- **Positive Data Team Messaging**: "We enable, not replace"

### Files for Web Comparison Generation
- **`WEB_COMPARISON_TEMPLATE.md`** - Master template with mandatory checklists (150K chars)
- **`WEB_COMPARISON_PHASED_EXECUTION.md`** - 4-phase execution framework with explicit SHARED/ references
- **`competitors/SHARED/`** - Reusable components library:
  - `README.md` - How to use shared components
  - `scoop_capabilities_checklist.md` - 40-item mandatory verification
  - `agentic_analytics_section.md` - Multi-agent architecture content
  - `embeddable_analytics_section.md` - Platform embedding capabilities (NOT SDKs)

### The 4-Phase Execution Framework
1. **Phase 1**: Foundation & Scoop Revolution (35-40K chars)
   - MUST lead with Agentic Analytics explanation
   - Include Progressive Analysis modes (Quick/Deep)
   - Show statistical validation examples
   
2. **Phase 2**: Capability Analysis (40-45K chars)
   - Cover ALL 40 items from capability checklist
   - List all 150+ Excel functions
   - Explain ML with business rules output
   
3. **Phase 3**: Department & Industry Impact (40-45K chars)
   - ALL 9 departments required
   - Minimum 4 industries
   - Positive data team enablement
   
4. **Phase 4**: Consolidation & Quality Check (150K+ final)
   - Verify all checklists complete
   - Ensure 60/40 positive ratio
   - Professional tone throughout
2. **Phase 2**: Capability Analysis (40-45K chars) - Features, architecture, Scoop advantages
3. **Phase 3**: Business Impact (35-40K chars) - Scenarios, ROI, workflows
4. **Phase 4**: Consolidation & AEO (150K final) - Merge, optimize for AI/SEO

**Execution**:
```bash
# Step-by-step (recommended for quality):
"Generate Phase 1 foundation for Power BI Copilot"
# Review output, then proceed to Phase 2, etc.

# Or quick generation (if confident):
"Generate complete web comparison for Power BI Copilot using phased execution framework"
```

**Output**: `competitors/[name]/outputs/web_comparison.md`
- AEO-optimized for answer engines (Perplexity, ChatGPT, Google SGE)
- 150K characters across 3 Webflow fields
- Credible, balanced, capability-focused content

## Key Principles

1. **Research is Gold**: Never delete, always preserve
2. **Evidence Required**: No claims without proof
3. **BUPAF Guides**: Focus on business user empowerment
4. **Credibility First**: Better to understate than exaggerate
5. **Incremental Progress**: Small steps, checkpoint often
6. **Build Up More Than Tear Down**: 60% Scoop innovation, 40% competitor gaps
7. **Enable Don't Replace**: Positive messaging for data teams
8. **Comprehensive Coverage**: All audiences, all capabilities

## Current Priorities

### Phase 1: Stabilize Foundation (This Week)
- Fix inflated claims (✅ Snowflake $1.6M removed)
- Archive planning docs (✅ Root cleaned)
- Apply BUPAF scoring consistently

### Phase 2: Deepen Priority Competitors (Next 2 Weeks)
Priority order based on deal frequency:
1. **Power BI Copilot** - Most common, only 40% done
2. **Tableau Pulse** - Enterprise deals, schema issues
3. **ThoughtSpot** - Major gap at 25%
4. **Domo** - 70% done, needs organization

### Phase 3: Complete Repository (Month)
- All competitors >70% complete
- Web outputs for all
- Automated updates working

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
- **Methodology**: BUPAF framework in `framework/` directory
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
├── framework/                      # BUPAF methodology
├── results/                        # Executive presentations
├── evidence/                       # Screenshots & proof
└── archive/                        # Historical files
```

### Key Competitor Research Areas
1. **Snowflake Cortex**: Most extensive analysis with Python test suite (20+ files)
2. **Domo**: Portal prison and AI capabilities analysis
3. **ThoughtSpot**: Accuracy benchmarking evidence
4. **Others**: Each with battle cards and specific limitation evidence

### BUPAF Scoring Framework
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