# Simplified Repository Structure - Focus on Incremental Growth

**Philosophy**: Everything lives in competitor folders. Master documents aggregate from there.
**Goal**: Avoid sprawl, enable incremental research, maintain single source of truth

---

## Proposed Structure (Simple & Scalable)

```
/competitive-intelligence/
│
├── README.md                         # Overview & navigation
├── MASTER_COMPARISON.md              # Aggregated from all competitors
├── RESEARCH_PRIORITIES.md            # What to research next
│
├── competitors/                      # ALL content lives here
│   ├── _TEMPLATE/                   # Standard structure
│   │   ├── README.md                # Navigation
│   │   ├── ANALYSIS.md              # Deep research (grows over time)
│   │   ├── BATTLE_CARD.md           # Sales quick reference
│   │   ├── EVIDENCE.md              # Links, quotes, proof
│   │   └── CONTENT.md               # Web-ready content
│   │
│   ├── snowflake-cortex/            # Example: most complete
│   │   ├── README.md
│   │   ├── ANALYSIS.md              # All technical analysis here
│   │   ├── BATTLE_CARD.md           # Generated from ANALYSIS
│   │   ├── EVIDENCE.md              # All sources & proof
│   │   ├── CONTENT.md               # Web/marketing content
│   │   └── tests/                   # Any test code
│   │
│   └── [other competitors...]       # Same structure
│
├── synthesis/                        # Aggregated views (generated)
│   ├── BUPAF_SCORES.md             # Pull from all ANALYSIS.md
│   ├── PRICING_MATRIX.md           # Pull from all competitors
│   ├── FEATURE_COMPARISON.md       # Pull from all competitors
│   └── WEB_CONTENT_ALL.json        # For webflow API
│
├── framework/                        # Methodologies
│   └── BUPAF.md                    # Scoring framework
│
├── evidence/                         # Shared screenshots/assets
│   └── [images, pdfs, etc]
│
└── archive/                          # Historical versions
```

---

## Key Principles

### 1. Everything in Competitor Folders
- **ANALYSIS.md**: Growing document with all research
- **BATTLE_CARD.md**: Extracted key points for sales
- **EVIDENCE.md**: All URLs, quotes, sources
- **CONTENT.md**: Marketing/web content

### 2. Master Documents Aggregate
- Don't duplicate content
- Pull from competitor folders
- Use scripts to generate synthesis
- Single source of truth

### 3. Incremental Growth Pattern
```
Start → Basic research in ANALYSIS.md
     → Add evidence to EVIDENCE.md
     → Generate BATTLE_CARD.md
     → Create CONTENT.md for web
     → Aggregate to synthesis/
```

### 4. No Sprawl Rules
- Max 5 files per competitor (plus tests/assets)
- No duplicate information
- Master docs are views, not storage
- Content library lives in synthesis/

---

## File Purposes (Clear & Distinct)

### In Each Competitor Folder:

#### ANALYSIS.md (The Brain)
```markdown
# [Competitor] Analysis

## Current Understanding
[Everything we know, growing over time]

## Architecture & Technology
[Technical deep dive]

## Capabilities
[What they can/can't do]

## Limitations & Weaknesses
[With evidence]

## Pricing Reality
[True costs]

## Customer Feedback
[Quotes and patterns]

## Our Advantages
[How we win]

## Research Notes
[Questions, gaps, todos]
```

#### BATTLE_CARD.md (The Weapon)
```markdown
# Quick competitive guide for sales
[Extracted from ANALYSIS.md]
[Updated when ANALYSIS updates]
```

#### EVIDENCE.md (The Proof)
```markdown
# All sources and evidence
[URLs with dates]
[Customer quotes]
[Screenshots references]
[Documentation links]
```

#### CONTENT.md (The Marketing)
```markdown
# Web-ready content
[Landing page copy]
[Comparison points]
[Value props]
[Can be JSON or Markdown]
```

---

## How It Grows

### Phase 1: Initial Research
```
competitors/new-competitor/
├── ANALYSIS.md (start documenting)
└── EVIDENCE.md (collect sources)
```

### Phase 2: Sales Enablement
```
competitors/new-competitor/
├── ANALYSIS.md (more complete)
├── EVIDENCE.md (verified sources)
└── BATTLE_CARD.md (generated from analysis)
```

### Phase 3: Marketing Ready
```
competitors/new-competitor/
├── ANALYSIS.md (comprehensive)
├── EVIDENCE.md (extensive proof)
├── BATTLE_CARD.md (battle-tested)
└── CONTENT.md (web-ready)
```

---

## Aggregation Strategy

### Instead of COMPETITIVE_CONTENT_LIBRARY.md:
```python
# generate_content_library.py
for competitor in competitors:
    read competitor/CONTENT.md
    extract reusable elements

output synthesis/CONTENT_LIBRARY.md
```

### Instead of manual pricing tables:
```python
# generate_pricing_matrix.py
for competitor in competitors:
    read competitor/ANALYSIS.md#pricing
    extract pricing data

output synthesis/PRICING_MATRIX.md
```

### For webflow integration:
```python
# generate_web_content.py
for competitor in competitors:
    read competitor/CONTENT.md
    format for API

output synthesis/WEB_CONTENT_ALL.json
```

---

## Benefits of This Approach

### 1. No Sprawl
- Fixed structure per competitor
- Clear file purposes
- No duplication

### 2. Incremental Growth
- Start small (just ANALYSIS.md)
- Add as you research
- Natural progression

### 3. Single Source of Truth
- Everything in competitor folder
- Masters aggregate, don't store
- Easy to maintain

### 4. Scalable
- Add competitors easily
- Template ensures consistency
- Scripts handle aggregation

### 5. Clear Ownership
- Each competitor folder is complete
- No hunting across files
- Easy to assign research

---

## Migration Plan (Simple)

### Step 1: Create Template
```bash
mkdir competitors/_TEMPLATE
# Create 4 standard files
```

### Step 2: Consolidate Existing
For each competitor:
1. Merge all content into ANALYSIS.md
2. Extract evidence to EVIDENCE.md
3. Keep BATTLE_CARD.md
4. Create CONTENT.md from any web content

### Step 3: Remove Sprawl
1. Delete COMPETITIVE_CONTENT_LIBRARY.md
2. Delete WEB_CONTENT_SPEC.md (move to framework/)
3. Delete COMPETITOR_TEMPLATE.md (use _TEMPLATE folder)
4. Keep only essential root files

### Step 4: Create Aggregation
1. Write simple Python scripts
2. Generate synthesis/ folder
3. Set up cron/hooks for updates

---

## What Root Files Remain

### Essential Only:
- **README.md** - Navigation and overview
- **RESEARCH_PRIORITIES.md** - What to research next
- **MASTER_COMPARISON.md** - Generated from all competitors

### Everything Else:
- Lives in competitors/[name]/
- Or gets generated to synthesis/
- Or archives to archive/

---

## Example: How Snowflake Cortex Would Look

```
competitors/snowflake-cortex/
├── README.md         # "Start with ANALYSIS.md"
├── ANALYSIS.md       # 500+ lines of everything
├── BATTLE_CARD.md    # 150 lines for sales
├── EVIDENCE.md       # 50+ URLs and sources
├── CONTENT.md        # Web-ready copy
└── tests/           # Python test suite
```

All Snowflake content in one place. No hunting.

---

## The Key Insight

**Don't maintain the same information in multiple places.**

Instead:
1. Research goes in ANALYSIS.md
2. Evidence goes in EVIDENCE.md
3. Sales points extracted to BATTLE_CARD.md
4. Web content prepared in CONTENT.md
5. Everything else is generated

This way:
- Update one place
- Scripts propagate changes
- No sync issues
- No sprawl

---

*This structure scales infinitely while staying simple.*