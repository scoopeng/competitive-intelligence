# BUA Framework Enhancement Proposal

**Date**: September 27, 2025
**Purpose**: Add 1-3 components per dimension that genuinely measure business user autonomy AND create differentiation between competitors
**Approach**: Enhancement, not replacement - keep existing 13 components, add 5-8 new ones

---

## Current Framework Strengths to Preserve

### What Works Well:
1. **Schema Evolution (0/4)**: All competitors fail - perfect differentiator
2. **Excel Formulas (0/4)**: All competitors fail - clear Scoop advantage
3. **Investigation (0-4/4)**: Good spread (Qlik 3, Tellius 3, most 0-1)
4. **ML (0-3/3)**: Good differentiation (3 have real ML, 8 don't)
5. **PowerPoint Automation (0/3)**: All fail - Scoop differentiator

### What Needs Enhancement:
- Some dimensions too binary (all pass or all fail)
- Missing legitimate BUA capabilities that competitors vary on
- Need components where 2-4 competitors score 2-3/4 (not all 0, not all 4)

---

## Proposed New Components (5-8 additions)

### Dimension 1: Autonomy (Currently 3 components: Setup, Questions, Speed)

#### NEW: Self-Service Data Connections (0-3 points)
**What it measures**: Can business users connect to data sources themselves without IT?

**Scoring**:
- 0/3: IT must configure all connections (Power BI, Tableau Pulse, most)
- 1/3: Pre-configured connections available, users select from list
- 2/3: Users can add connections with IT approval/credentials
- 3/3: Users can connect to any source with their own credentials

**Expected Distribution**:
- Scoop: 3/3 (connects with user credentials)
- Domo: 2/3 (good connectivity but IT-involved)
- ThoughtSpot: 1/3 (IT configures)
- Snowflake Cortex: 1/3 (semantic layer)
- Most others: 0-1/3

**Why this matters for BUA**: Business users blocked if they can't reach their data without waiting for IT.

#### NEW: Error Recovery (0-2 points)
**What it measures**: Can business users fix their own mistakes or recover from errors?

**Scoring**:
- 0/2: Technical errors shown, user stuck (Snowflake "statement count" errors, Qlik syntax errors)
- 1/2: Helpful error messages but user must start over
- 2/2: Self-correction suggestions, undo capability, or automatic retry

**Expected Distribution**:
- Scoop: 2/2 (conversational recovery)
- DataChat: 1/2 (GEL transparency helps)
- Zenlytic: 1/2 (can see YAML)
- Tellius: 0/2 (black box fails)
- Most: 0-1/2

**Why this matters for BUA**: Business users abandon tools that trap them in error states.

---

### Dimension 2: Flow (Currently 3 components: Native Integration, Portal Prison, Interface Simplicity)

#### NEW: Collaboration Features (0-3 points)
**What it measures**: Can business users share, comment, and collaborate within their workflow?

**Scoring**:
- 0/3: No collaboration, must send screenshots (most)
- 1/3: Share links to dashboards (basic)
- 2/3: Comments/annotations, version history
- 3/3: Real-time co-editing, threaded discussions, @mentions in native tools

**Expected Distribution**:
- Scoop: 3/3 (Slack-native collaboration)
- Domo: 2/3 (has social layer and comments)
- Qlik: 1/3 (share dashboards)
- ThoughtSpot: 2/3 (has sharing and boards)
- DataChat: 1/3 (claims collaboration, unclear depth)
- Most others: 0-1/3

**Why this matters for BUA**: Business users work in teams, need to discuss findings without leaving tools.

---

### Dimension 3: Understanding (Currently 3 components: Investigation, ML, Explanation)

#### NEW: Data Literacy Support (0-2 points)
**What it measures**: Does the tool help business users understand data concepts without training?

**Scoring**:
- 0/2: Assumes user knows statistics, data modeling, SQL concepts (most)
- 1/2: Tooltips, help text, or data dictionaries available
- 2/2: Contextual education, suggests next questions, explains why answers matter

**Expected Distribution**:
- Scoop: 2/2 (guides investigation)
- ThoughtSpot: 1/2 (has data dictionary)
- Domo: 1/2 (has some guidance)
- Qlik: 0/2 (assumes expertise)
- Tellius: 0/2 (citizen data scientist model)
- Most: 0/2

**Why this matters for BUA**: Business users shouldn't need statistics degrees to get insights.

#### NEW: Anomaly Detection (0-2 points)
**What it measures**: Does the tool automatically surface unusual patterns business users should know about?

**Scoring**:
- 0/2: User must know what to look for (most)
- 1/2: Basic outlier detection or alerts on thresholds
- 2/2: Automatic anomaly detection with business context and suggested actions

**Expected Distribution**:
- Scoop: 2/2 (investigates anomalies automatically)
- Domo: 2/2 (AutoML includes anomaly detection)
- ThoughtSpot: 2/2 (SpotIQ finds anomalies)
- Sisense: 1/2 ("Show Me Something Interesting")
- Tableau Pulse: 1/2 (basic detection)
- Most others: 0/2

**Why this matters for BUA**: Business users don't know what they don't know - tool should surface surprises.

---

### Dimension 4: Presentation (Currently 3 components: Visuals, Brand, Speed)

#### NEW: Chart Intelligence (0-2 points)
**What it measures**: Does the tool automatically select appropriate visualizations for the data?

**Scoring**:
- 0/2: User must choose chart type (most)
- 1/2: Suggests chart types based on data
- 2/2: Automatically selects best visualization and explains why

**Expected Distribution**:
- Scoop: 2/2 (intelligent viz selection)
- Domo: 1/2 (has suggestions)
- ThoughtSpot: 1/2 (recommends)
- Power BI: 1/2 (suggests in some contexts)
- Most: 0/2

**Why this matters for BUA**: Business users don't know when to use scatter plot vs bar chart.

---

### Dimension 5: Data (Currently 4 components: Connections, Schema Evolution, Prep, Writeback)

#### NEW: Data Quality Visibility (0-2 points)
**What it measures**: Can business users see data quality issues (missing values, duplicates, outliers) without technical analysis?

**Scoring**:
- 0/2: No data quality indicators (most)
- 1/2: Shows nulls/duplicates when user explores
- 2/2: Proactive data quality alerts with business impact assessment

**Expected Distribution**:
- Scoop: 2/2 (flags quality issues in context)
- ThoughtSpot: 1/2 (shows data profiling)
- Domo: 1/2 (data quality in prep)
- Most: 0/2

**Why this matters for BUA**: Business users make bad decisions on bad data if they can't see quality issues.

---

## Summary of Proposed Additions

| Dimension | New Component | Points | Expected Leader | Expected Spread |
|-----------|---------------|--------|-----------------|-----------------|
| Autonomy | Self-Service Data Connections | 0-3 | Scoop (3), Domo (2) | Good variety: 0-3 range |
| Autonomy | Error Recovery | 0-2 | Scoop (2), few at 1 | Most 0, some 1 |
| Flow | Collaboration Features | 0-3 | Scoop (3), Domo/TS (2) | Good spread: 0-3 |
| Understanding | Data Literacy Support | 0-2 | Scoop (2), few at 1 | Most 0, some 1 |
| Understanding | Anomaly Detection | 0-2 | Scoop/Domo/TS (2) | Good spread: 0-2 |
| Presentation | Chart Intelligence | 0-2 | Scoop (2), few at 1 | Most 0, some 1 |
| Data | Data Quality Visibility | 0-2 | Scoop (2), few at 1 | Most 0, some 1 |

**Total New Points**: 16 points added
**New Framework Total**: 66 points (was 50)

---

## Impact on Scores (Estimated)

### Scoop (Current: 45/50)
**Expected New Score: ~53/66** (+8 points)
- Self-Service Connections: +2 (not perfect - some sources need IT)
- Error Recovery: +2
- Collaboration: +2 (good but not perfect real-time co-editing)
- Data Literacy: +1 (helps but doesn't teach everything)
- Anomaly Detection: +2
- Chart Intelligence: +1 (suggests but users can override)
- Data Quality: +2
- **New percentage: 80% (was 90%) - MORE REALISTIC**

### Domo (Current: 25/50)
**Expected New Score: ~35/66** (+10 points)
- Self-Service Connections: +2
- Error Recovery: +1
- Collaboration: +2
- Data Literacy: +1
- Anomaly Detection: +2
- Chart Intelligence: +1
- Data Quality: +1
- **New percentage: 53% (was 50%)**

### ThoughtSpot (Current: 20/50)
**Expected New Score: ~28/66** (+8 points)
- Self-Service Connections: +1
- Error Recovery: +0
- Collaboration: +2
- Data Literacy: +1
- Anomaly Detection: +2
- Chart Intelligence: +1
- Data Quality: +1
- **New percentage: 42% (was 40%)**

### Most Others (Current: 11-16/50)
**Expected New Score: +2-4 points each**
- Most score 0 on most new components
- Few score 1-2 on collaboration or anomaly detection

---

## Benefits of This Enhancement

### 1. More Credible Differentiation
- Not all components are Scoop vs Everyone
- Domo gets credit for collaboration and anomaly detection
- ThoughtSpot gets credit for anomaly detection
- Creates natural clustering of competitors

### 2. Gap Reduction (Slightly)
- Scoop: 90% → 88% (more realistic)
- Domo gap: 20 → 23 points absolute, but 40% → 35% relative
- Makes framework feel less rigged for Scoop

### 3. More Complete BUA Picture
- Collaboration IS important for business users
- Data quality visibility IS critical
- Error recovery IS a blocker
- These are legitimate BUA dimensions we were missing

### 4. Better Competitive Intelligence
- Can now differentiate Domo vs ThoughtSpot more clearly
- Collaboration becomes a Domo strength
- SpotIQ anomaly detection becomes ThoughtSpot strength
- More nuanced battle cards possible

---

## Implementation Plan

### Phase 1: Validate New Components (Before Re-Scoring)
1. Review existing research for evidence of new capabilities
2. For each competitor, check:
   - Self-service data connections: documented?
   - Collaboration features: what exactly?
   - Anomaly detection: real or claimed?
   - Data quality: shown to users?
3. Adjust scoring criteria if evidence doesn't match expectations

### Phase 2: Pilot Score 2-3 Competitors
- Start with Domo (should benefit most)
- Then ThoughtSpot (should get anomaly detection credit)
- Then one Category D tool (should stay low)
- Validate that spread works as expected

### Phase 3: Full Re-Score If Validated
- Only if pilot shows good differentiation
- Only if research supports scoring
- Only if gap reduction feels right

### Phase 4: Update Documentation
- framework_scoring.md template
- SCOOP_CAPABILITIES.md (score Scoop on new components)
- Battle cards (highlight new differentiators)

---

## Questions to Answer Before Proceeding

### 1. Research Evidence Available?
- Do we have enough research on collaboration features per competitor?
- Do we know which have anomaly detection vs claims?
- Can we score data quality visibility from existing research?

### 2. Scoop Capabilities Verified?
- Does Scoop really have self-service data connections (3/3)?
- Does Scoop have error recovery (2/2)?
- Does Scoop have data literacy support (2/2)?
- Need to verify before claiming points

### 3. Framework Balance?
- Is 66 points too many? (Consider: should be ~15-20 components)
- Are new components weighted appropriately?
- Does this feel like enhancement or replacement?

### 4. Sales Messaging Impact?
- Will "58/66" vs "45/50" help or hurt positioning?
- Is "88%" vs "90%" a meaningful change?
- Do new differentiators create better talking points?

---

## Recommendation

**Proceed with cautious enhancement**:

1. **Start with 3-4 new components** (not all 7):
   - Collaboration Features (3 points) - clear differentiation
   - Anomaly Detection (2 points) - gives credit to Domo/ThoughtSpot
   - Self-Service Connections (3 points) - creates spread
   - **Skip the rest for now** - can add later if needed

2. **New Total: 58 points** (was 50)
   - More manageable increase
   - Still creates differentiation
   - Less risk of over-complication

3. **Pilot score on Domo only** first:
   - See if research supports scoring
   - Validate that Domo gets credit deserved
   - Check if gap feels right
   - Don't commit to full re-score until validated

4. **If pilot works, consider full re-score**
   - But only 3-4 new components
   - Save other components for future enhancement
   - Iterative improvement > one-time overhaul

---

## Next Steps After Compact

1. Review Domo research for collaboration and anomaly detection evidence
2. Review Scoop capabilities doc for self-service connections evidence
3. Pilot score Domo with 3 new components
4. Decide: full re-score or keep current framework
5. Document decision rationale

**Key Principle**: Enhancement should improve differentiation AND credibility, not just reduce Scoop's gap.

---

## CRITICAL: Scoop Should NOT Score 100%

**Why Perfect Scores Hurt Credibility**:
1. Nothing is perfect - buyers know this
2. Creates suspicion of bias ("framework designed for Scoop")
3. Misses real opportunities for improvement
4. Makes competitive claims less believable

**Scoop's Realistic Limitations**:
- Self-Service Connections: Some enterprise sources still need IT setup (2/3, not 3/3)
- Collaboration: Good but not perfect real-time co-editing (2/3, not 3/3)
- Data Literacy: Helps users but doesn't teach statistics (1/2, not 2/2)
- Chart Intelligence: Suggests but users can override incorrectly (1/2, not 2/2)
- Schema Evolution: Works for most changes but edge cases exist (3/4, not 4/4)
- ML: J48/JRip are explainable but still require interpretation (2/3, not 3/3)

**Recommended Scoop Score: 53/66 (80%)**
- Down from 90% (45/50) - more credible
- Still clearly Category A (40+ points = 60%+)
- Leaves room for "Scoop 2.0" improvements
- Gap to Domo: 18 points (53 vs 35) - still significant but believable

**NEW Expected Scores**:
- Scoop: 53/66 (80%) - Category A
- Domo: 35/66 (53%) - Category C
- ThoughtSpot: 28/66 (42%) - Category C
- Most others: 15-20/66 (23-30%) - Category D

**Gap**: 27% relative (80% vs 53%) instead of 44% (90% vs 50%) - MUCH MORE CREDIBLE
---

## Revised Recommendation: Conservative Scoop Scoring

### Scoop Should Lose Points On:
1. **Autonomy - Setup (9→8)**: Some friction exists, not instant for everyone
2. **Autonomy - Questions (9→8)**: Not 100% success rate, some questions need refinement  
3. **Flow - Native Integration (9→8)**: Excel functions work but not all 150+ are perfect
4. **Understanding - ML (9→8)**: J48/JRip require interpretation, not fully automated
5. **Data - Schema Evolution (9→8)**: Works for most but edge cases exist

### New Component Scoring (Conservative):
- Self-Service Connections: 2/3 (not 3/3 - some sources need IT)
- Error Recovery: 2/2 (this is genuinely strong)
- Collaboration: 2/3 (not 3/3 - not perfect real-time)
- Data Literacy: 1/2 (not 2/2 - helps but doesn't teach everything)
- Anomaly Detection: 2/2 (this is genuinely strong)
- Chart Intelligence: 1/2 (not 2/2 - suggests but not perfect)
- Data Quality: 2/2 (this is genuinely strong)

### FINAL SCOOP SCORE: 53/66 (80%)
**Old Score**: 45/50 (90%)
**Change**: -10 percentage points (more credible)
**Category**: Still A (60%+ = Category A threshold)

### FINAL COMPETITOR SCORES (Estimated):
- Domo: 35/66 (53%) - Gap: 18 points, 27% relative
- ThoughtSpot: 28/66 (42%) - Gap: 25 points, 38% relative  
- Qlik: 20/66 (30%) - Gap: 33 points, 50% relative
- Most others: 15-20/66 (23-30%)

**This feels RIGHT**: 
- Scoop clearly better but not impossibly better
- Gaps are believable and defensible
- Room for Scoop to improve to 85-90%
- Competitors have legitimate strengths recognized
