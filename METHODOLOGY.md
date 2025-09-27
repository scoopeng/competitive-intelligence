# Competitive Intelligence Methodology

**Current Process**: 3-Chunk Deep Research (90-120 minutes per competitor)
**Focus**: Customer-story-driven intelligence with quantified evidence
**Goal**: Enterprise-grade sales enablement materials
**Framework**: BUA (Business User Power Assessment Framework) guides all analysis

---

## How BUA Guides the System

### The System Architecture
```
Business User Autonomy Framework (The Lens)
    ↓ guides
Competitor Research (The Content)
    ↓ synthesizes into
Standard Outputs (The Products)
    ↓ feeds
Customer-Facing Materials (The Value)
```

### BUA is the Lens, Not the Constraint
The framework ensures we research what matters for business users:
- **Independence**: Can they work alone?
- **Analytical Depth**: Can they investigate, not just query?
- **Workflow Integration**: Does it work where they work?
- **Business Communication**: Can they understand the output?
- **Visual Intelligence**: Is it presentation-ready?

But it doesn't limit what you research or how you document it.

---

## Core Principles

1. **Preserve Everything**: Never delete research. All documents are valuable.
2. **Flexible Growth**: Each competitor can have unlimited research documents
3. **Standard Outputs**: Generate consistent documents from diverse research
4. **Single Source**: Each competitor folder is the source of truth for that competitor
5. **Incremental Building**: Start anywhere, build towards completeness

---

## Repository Structure

```
/competitive-intelligence/
│
├── README.md                         # Repository overview
├── METHODOLOGY.md                    # This document
├── RESEARCH_PRIORITIES.md            # What to research next
│
├── templates/                        # Standard document templates
│   ├── README_TEMPLATE.md           # Competitor folder navigation
│   ├── BATTLE_CARD_TEMPLATE.md      # Sales reference format
│   ├── TECHNICAL_ANALYSIS_TEMPLATE.md
│   ├── PRICING_ANALYSIS_TEMPLATE.md
│   ├── CUSTOMER_EVIDENCE_TEMPLATE.md
│   └── WEB_CONTENT_TEMPLATE.md
│
├── competitors/                      # All competitor research
│   ├── [competitor-name]/
│   │   ├── README.md                # Navigation & summary
│   │   ├── BATTLE_CARD.md           # Standardized sales tool
│   │   │
│   │   ├── research/                # ALL research documents
│   │   │   ├── [any-research].md    # Preserved, never deleted
│   │   │   ├── technical-analysis.md
│   │   │   ├── customer-feedback.md
│   │   │   ├── pricing-investigation.md
│   │   │   └── [working-notes].md
│   │   │
│   │   ├── evidence/                # Proof & sources
│   │   │   ├── links.md
│   │   │   ├── screenshots/
│   │   │   └── quotes.md
│   │   │
│   │   ├── outputs/                 # Generated content
│   │   │   ├── web-comparison.md
│   │   │   ├── landing-page.md
│   │   │   ├── email-campaign.md
│   │   │   └── exec-summary.md
│   │   │
│   │   └── tests/                   # Any test code
│   │       └── [test-files]
│   │
│   ├── snowflake-cortex/            # Example: extensive research
│   │   ├── README.md
│   │   ├── BATTLE_CARD.md           # Generated from research/
│   │   ├── research/                # 20+ documents preserved
│   │   │   ├── CONSOLIDATED_TECHNICAL_ANALYSIS.md
│   │   │   ├── REAL_DIFFERENTIATORS.md
│   │   │   ├── PROJECT_SUMMARY.md
│   │   │   ├── MASTER_ANALYSIS_PLAN.md
│   │   │   └── [all other research...]
│   │   ├── evidence/
│   │   ├── outputs/
│   │   └── tests/
│   │
│   └── [other competitors...]
│
├── synthesis/                        # Cross-competitor aggregation
│   ├── MASTER_COMPARISON.md        # Generated from all
│   ├── BUA_SCORES.md             # Pulled from all
│   ├── PRICING_MATRIX.md           # Aggregated pricing
│   └── web-api/                    # For webflow
│       └── all-competitors.json
│
├── framework/                        # Methodologies & guides
│   ├── BUA.md
│   ├── RESEARCH_GUIDE.md
│   └── SYNTHESIS_GUIDE.md
│
└── archive/                          # Historical versions
```

---

## How It Works

### 1. Research Phase (Messy & Creative)
Add ANY research document to `competitors/[name]/research/`:
- Technical investigations
- Customer interview notes
- Pricing analysis
- Competitive testing
- Working theories
- Random discoveries

**No restrictions. Just document everything.**

### 2. Evidence Collection (Ongoing)
Store all proof in `competitors/[name]/evidence/`:
- URLs with dates
- Screenshots
- Customer quotes
- Documentation excerpts
- Benchmarks

### 3. Synthesis Phase (Standardization)
Generate standard documents FROM the research:

#### BATTLE_CARD.md Generation
```python
# Pulls from:
- research/*.md (key findings)
- evidence/*.md (proof points)
- outputs/*.md (messaging)

# Produces:
- Standardized battle card using template
```

#### Output Content Generation
Create multiple output types in `outputs/`:
- web-comparison.md (for website)
- landing-page.md (for campaigns)
- email-campaign.md (for outreach)
- exec-summary.md (for leadership)
- api-content.json (for automation)

### 4. Cross-Competitor Synthesis
Aggregate into `synthesis/`:
- Pull from all battle cards
- Generate master comparisons
- Create pricing matrices
- Build feature tables

---

## Standard Documents (Generated, Not Manual)

### BATTLE_CARD.md
**Generated from**: All research/ documents
**Template**: templates/BATTLE_CARD_TEMPLATE.md
**Contains**:
- Quick facts (pulled from research)
- Killer questions (identified in research)
- Key differentiators (synthesized)
- Pricing reality (from pricing research)
- Objection handlers (from customer evidence)

### README.md
**Purpose**: Navigation for the folder
**Contains**:
- List of all research documents
- Current completeness status
- Key findings summary
- Next research priorities

### Output Documents
**Generated for different audiences**:
- **web-comparison.md**: Website content
- **landing-page.md**: Marketing pages
- **sales-pitch.md**: Sales messaging
- **exec-briefing.md**: Leadership summaries
- **api-content.json**: Automated distribution

---

## Current Research Process: 3-Chunk Method

### CHUNK 1: Deep Discovery & Customer Stories (40-50 minutes)
**Phase 1A**: Archive recovery and existing research review (5 min)
**Phase 1B**: Customer story mining via G2, Reddit, LinkedIn, consultant blogs (25-30 min)
**Phase 1C**: Industry vertical deep dive for compliance/regulatory issues (8-10 min)

**Outputs**: `research/customer_stories.md`, `research/industry_analysis.md`, `evidence/customer_quotes.md`

### CHUNK 2: Technical Reality & Competitive Context (30-35 minutes)
**Phase 2A**: Technical performance analysis with quantified data (12-15 min)
**Phase 2B**: Competitive positioning research and market intelligence (10-12 min)
**Phase 2C**: Economic impact deep dive including hidden costs (8-10 min)

**Outputs**: `research/performance_analysis.md`, `research/competitive_positioning.md`, `research/economic_impact.md`

### CHUNK 3: Analysis & Rich Sales Enablement (20-25 minutes)
**Phase 3A**: Evidence-based BUA scoring with customer quotes (8-10 min)
**Phase 3B**: Rich sales materials creation with customer stories (8-10 min)
**Phase 3C**: Quality assurance and evidence verification (4-5 min)

**Outputs**: Updated `BATTLE_CARD.md`, `outputs/industry_briefings.md`, `research/bupaf_evidence.md`

### Success Metrics
- **Customer Stories**: 10+ implementation experiences
- **Quantified Data**: 15+ specific metrics (response times, costs, limits)
- **Industry Analysis**: 5+ verticals covered
- **Evidence Citations**: Every claim backed by customer quote or quantified data

---

## Example: Snowflake Cortex

### What We Keep (Everything!)
```
snowflake-cortex/research/
├── CONSOLIDATED_TECHNICAL_ANALYSIS.md  # 600+ lines
├── DEFINITIVE_TEST_SUITE.py           # Test code
├── REAL_DIFFERENTIATORS.md            # Key findings
├── PROJECT_SUMMARY.md                 # Overview
├── MASTER_ANALYSIS_PLAN.md            # Methodology
├── CONVERSATION_CONTEXT_REALITY.md    # Specific investigation
├── CORTEX_ANALYST_VS_INTELLIGENCE.md  # Comparison
├── semantic_model.yaml                # Technical artifact
└── [20+ more documents...]            # All preserved
```

### What We Generate
```
snowflake-cortex/
├── BATTLE_CARD.md         # Synthesized from research/
├── README.md              # Navigation & summary
└── outputs/
    ├── web-comparison.md  # For website
    ├── landing-page.md    # For campaigns
    └── api-content.json   # For automation
```

---

## Benefits of This Approach

### 1. Preserves Everything
- No research is lost
- All work has value
- History maintained

### 2. Flexible Research
- Add any document type
- No rigid structure during research
- Creative freedom

### 3. Standardized Outputs
- Consistent battle cards
- Uniform web content
- Reliable API data

### 4. Clear Methodology
- Research → Evidence → Synthesis → Distribution
- Templates ensure consistency
- Scripts handle generation

### 5. Scalable Growth
- Start with one document
- Build incrementally
- No limit on depth

---

## Implementation Plan

### Phase 1: Organize Existing
1. Create templates/ folder with all templates
2. Move existing research into research/ folders
3. Organize evidence into evidence/ folders
4. Keep all existing content

### Phase 2: Generate Standards
1. Create generation scripts
2. Produce BATTLE_CARD.md for each
3. Generate README.md navigation
4. Create initial outputs/

### Phase 3: Build Synthesis
1. Aggregate to synthesis/
2. Create master comparisons
3. Generate API content
4. Enable webflow integration

### Phase 4: Continuous Improvement
1. Keep adding research/
2. Update evidence/
3. Regenerate outputs/
4. Refresh synthesis/

---

## Key Insight

**Research is messy. Outputs are clean.**

We don't force research into templates. We:
1. Let research be organic and complete
2. Preserve everything
3. Generate standardized outputs
4. Maintain consistency through synthesis

This way:
- Researchers have freedom
- Sales gets consistency
- Marketing gets variety
- Nothing is lost

---

*This methodology enables unlimited growth while maintaining order.*