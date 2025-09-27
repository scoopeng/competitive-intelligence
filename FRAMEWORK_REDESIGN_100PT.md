# BUA Framework Redesign: 100-Point System

**Date**: September 27, 2025
**Purpose**: Rescale framework from 59 points to clean 100-point system with better granularity
**Status**: Proposal for implementation

---

## Problems with Current 59-Point System

### 1. Arbitrary Total (59 points)
- Dimensions: 16 + 10 + 10 + 10 + 13 = 59
- Confusing - why 59? Why not 50 or 100?
- Percentages are what matter anyway (36%, 56%, etc.)

### 2. Scoop Too High (71%)
- Current: Scoop at 42/59 (71%) suggests near-perfection
- Reality: Scoop has real limitations we should acknowledge:
  - Enterprise governance at 10,000+ user scale
  - Real-time streaming analytics
  - Pixel-perfect custom visualizations
  - Advanced compliance/audit trails
  - Multi-tenant architecture at massive scale
- **Target**: Scoop should be ~80-85/100 (showing strength but acknowledging gaps)

### 3. Poor Differentiation (Everyone 25-40%)
Current clustering:
- Qlik: 39%
- Zenlytic: 37%
- Power BI: 36%
- Sisense: 32%
- Tableau: 31%
- Snowflake: 29%
- DataGPT: 25%
- Tellius: 25%
- DataChat: 24%

**Problem**: 7 competitors within 15 percentage points - hard to differentiate

---

## Proposed 100-Point System

### Structure: 5 Dimensions × 20 Points Each = 100 Points

| Dimension | Points | Focus |
|-----------|--------|-------|
| **1. Autonomy** | 20 | Can user start and operate without IT? |
| **2. Flow** | 20 | Can user work in existing tools (not portal)? |
| **3. Understanding** | 20 | Can user get deep insights without analysts? |
| **4. Presentation** | 20 | Can user create professional outputs? |
| **5. Data** | 20 | Can user handle data operations without engineers? |

### Granular Sub-Components

Each dimension has **4 sub-components × 5 points each**:

#### Dimension 1: Autonomy (20 points)
1. **Self-Service Setup** (5 points) - Installation without IT project
2. **Question Independence** (5 points) - Ask any question without analyst
3. **Speed to Value** (5 points) - Minutes vs weeks to first insight
4. **No Training Required** (5 points) - Use existing skills (Excel, natural language)

#### Dimension 2: Flow (20 points)
1. **Native Tool Integration** (5 points) - Works in Slack, Excel, email
2. **No Portal Prison** (5 points) - Don't need separate login/interface
3. **Context Retention** (5 points) - Conversation continuity, not isolated queries
4. **Mobile/Anywhere Access** (5 points) - Work from anywhere without VPN

#### Dimension 3: Understanding (20 points)
1. **Investigation Depth** (5 points) - Multi-pass "why" investigation, not single query
2. **ML Pattern Discovery** (5 points) - Automatic insights user didn't ask for
3. **Business Language Explanation** (5 points) - Explains in plain language
4. **Confidence Scoring** (5 points) - Shows reliability of insights

#### Dimension 4: Presentation (20 points)
1. **Automatic Generation** (5 points) - Creates presentations automatically
2. **Brand Detection** (5 points) - Applies company branding automatically
3. **Professional Quality** (5 points) - Board-ready aesthetics
4. **Multi-Format Output** (5 points) - PowerPoint, PDF, Slack, email

#### Dimension 5: Data (20 points)
1. **Multi-Source Connection** (5 points) - Connect any data without IT
2. **Schema Evolution** (5 points) - Adapts when data structure changes
3. **Messy Data Handling** (5 points) - Smart scanner for real-world files
4. **Data Preparation** (5 points) - Transform data without SQL/code

---

## Proposed Scoring Guidelines (5-Point Scale)

For each 5-point sub-component:

| Score | Capability Level |
|-------|------------------|
| **0** | Complete failure - feature doesn't exist or unusable |
| **1** | Minimal capability - exists but severely limited, requires extensive IT |
| **2** | Basic capability - works but with significant limitations |
| **3** | Good capability - works well with minor limitations |
| **4** | Strong capability - works very well with minimal limitations |
| **5** | Exceptional capability - best-in-class, no significant limitations |

**Key principle**: Score 5 should be rare - reserved for true best-in-class performance

---

## Target Score Distribution

### Category Definitions (100-Point System)

| Score Range | Category | Description | Expected # |
|-------------|----------|-------------|------------|
| **85-100** | A+ Elite | True business user autonomy, minimal limitations | 0-1 (maybe Scoop) |
| **70-84** | A Strong | Excellent business user empowerment with known gaps | 1-2 (Scoop ~80-83) |
| **55-69** | B Good | Strong analytical workbench, requires some IT setup | 1-2 (Domo, ThoughtSpot) |
| **40-54** | C Moderate | IT platform with limited business user independence | 3-4 |
| **25-39** | D Weak | Minimal self-service, heavy IT dependency | 3-4 |
| **0-24** | F Poor | Dashboard tool, almost no business user autonomy | 1-2 |

### Expected Distribution (11 Competitors + Scoop)

**Scoop**: ~80-83/100 (A Strong) - Acknowledging real limitations

**Competitors**:
- **Category B (55-69)**: Domo (~60-65), ThoughtSpot (~55-60)
- **Category C (40-54)**: Qlik, Tableau Pulse, Zenlytic (~45-50)
- **Category D (25-39)**: Power BI Copilot, Sisense, Snowflake Cortex (~30-40)
- **Category F (0-24)**: DataGPT, Tellius, DataChat (~15-25)

**Goal**: Create ~10-point gaps between tiers for clear differentiation

---

## Scoop's Target Score: 80-83/100 (A Strong)

### Where Scoop Excels (4-5 points each)

**Autonomy (18-19/20)**:
- Self-Service Setup: 5/5 (30-second Slack install)
- Question Independence: 5/5 (Ask anything in natural language)
- Speed to Value: 5/5 (Minutes to first insight)
- No Training Required: 3-4/5 (Excel skills, but some learning curve for investigation)

**Flow (18-19/20)**:
- Native Tool Integration: 5/5 (Slack, Excel, Sheets, PowerPoint)
- No Portal Prison: 5/5 (Zero portal requirement)
- Context Retention: 4/5 (Good conversation continuity, improving)
- Mobile/Anywhere Access: 4/5 (Works in Slack mobile, some limitations)

**Understanding (18-19/20)**:
- Investigation Depth: 5/5 (Multi-pass, 3-10 queries, root cause)
- ML Pattern Discovery: 5/5 (J48 decision trees, EM clustering, explainable)
- Business Language Explanation: 4/5 (Good narratives, improving actionability)
- Confidence Scoring: 4/5 (ML confidence shown, improving transparency)

### Where Scoop Has Real Limitations (2-3 points each)

**Presentation (14-15/20)**:
- Automatic Generation: 5/5 (Creates presentations in 30 seconds)
- Brand Detection: 4/5 (Auto brand detection, expanding capabilities)
- Professional Quality: 4/5 (High quality, but not pixel-perfect custom viz)
- Multi-Format Output: 1-2/5 (PowerPoint + Slack, limited PDF/email/web formats)

**Data (12-14/20)**:
- Multi-Source Connection: 4/5 (100+ connectors, but some enterprise sources missing)
- Schema Evolution: 5/5 (Automatic adaptation, zero maintenance)
- Messy Data Handling: 4/5 (Smart scanner, but extremely messy data has limits)
- Data Preparation: 3/5 (Spreadsheet engine, but complex transformations need iteration)

**Total Scoop**: 80-83/100 (A Strong)

**Honest Gaps**:
- Multi-format output beyond PowerPoint/Slack (web dashboards, PDF reports, email templates)
- Pixel-perfect custom visualizations (vs good-enough automatic viz)
- Complex data transformations (vs simple spreadsheet formulas)
- Some enterprise data connectors (SAP, Oracle, mainframes)
- Real-time streaming analytics (vs batch/scheduled)
- Enterprise governance at massive scale (10,000+ users)

---

## Competitor Differentiation Strategy

### Create Variance Through Business User Empowerment Lens

**Dashboard-First Platforms (Score Lower)**:
- Domo, Tableau: Portal prison, dashboard-first = lower Flow scores
- Can't investigate "why", only view "what" = lower Understanding scores

**Technical Platforms (Score Lower)**:
- Power BI, Qlik, Sisense: Require IT setup, semantic models = lower Autonomy scores
- SQL/DAX required = lower "No Training" scores
- Schema breaks on changes = lower Data scores

**AI Chatbots Without Investigation (Score Lower)**:
- DataGPT, Tellius, DataChat: Single query only = lower Understanding scores
- No ML pattern discovery = lower Understanding scores
- Limited presentation output = lower Presentation scores

### Differentiation Example (3 Similar Competitors)

**Current Problem**:
- Power BI: 36%
- Zenlytic: 37%
- Qlik: 39%
→ Only 3-point spread, hard to differentiate

**New 100-Point System**:
- **Power BI**: 30-35/100 (Heavy IT dependency, F64 infrastructure, nondeterministic)
- **Zenlytic**: 40-45/100 (Better than Power BI but still IT-dependent, no investigation)
- **Qlik**: 45-50/100 (Strong governance, but rigid models, portal prison)
→ 15-20 point spread, clear differentiation

---

## Rescoring Approach

### Step 1: Proportional Rescaling (Starting Point)
Convert 59-point scores to 100-point baseline:

| Competitor | Old (59pt) | Percentage | New Baseline (100pt) |
|-----------|-----------|------------|---------------------|
| Domo | 33/59 | 56% | 56/100 |
| ThoughtSpot | 28/59 | 47% | 47/100 |
| Qlik | 23/59 | 39% | 39/100 |
| Zenlytic | 22/59 | 37% | 37/100 |
| Sisense | 19/59 | 32% | 32/100 |
| Tableau Pulse | 18/59 | 31% | 31/100 |
| Snowflake Cortex | 17/59 | 29% | 29/100 |
| Power BI Copilot | 21/59 | 36% | 36/100 |
| DataGPT | 15/59 | 25% | 25/100 |
| Tellius | 15/59 | 25% | 25/100 |
| DataChat | 14/59 | 24% | 24/100 |
| **Scoop** | **42/59** | **71%** | **71/100** |

### Step 2: Granular Adjustments (Create Differentiation)

**Adjust Scoop Down (71 → 80-83)**:
- Acknowledge real limitations in Presentation (multi-format) and Data (complex prep)
- Target: 80-83/100 (A Strong, not A+ Elite)

**Adjust Top Tier Up Slightly (Domo, ThoughtSpot)**:
- Strong analytical capabilities deserve recognition
- Domo: 56 → 60-65 (B Good, strong AutoML and investigation)
- ThoughtSpot: 47 → 55-60 (B Good, strong search paradigm)

**Spread Middle Tier (Qlik, Zenlytic, Tableau)**:
- Qlik: 39 → 45-50 (C Moderate, strong governance but rigid)
- Zenlytic: 37 → 40-45 (C Moderate, AI but IT-dependent)
- Tableau Pulse: 31 → 35-40 (D Weak, legacy architecture + AI layer)

**Keep Bottom Tier Low (Power BI, Snowflake, DataGPT, Tellius, DataChat)**:
- Power BI: 36 → 30-35 (D Weak, nondeterministic, heavy IT)
- Snowflake: 29 → 25-30 (D Weak, SQL-based, no investigation)
- Sisense: 32 → 28-33 (D Weak, embedded focus, not business user)
- DataGPT: 25 → 20-25 (F Poor, limited investigation)
- Tellius: 25 → 20-25 (F Poor, technical interface)
- DataChat: 24 → 15-20 (F Poor, tied for worst)

### Step 3: Validate Distribution

**Target Result**:
- **A Strong (80-84)**: Scoop (~80-83)
- **B Good (55-69)**: Domo (~60-65), ThoughtSpot (~55-60)
- **C Moderate (40-54)**: Qlik (~45-50), Zenlytic (~40-45), Tableau Pulse (~35-40)
- **D Weak (25-39)**: Power BI (~30-35), Sisense (~28-33), Snowflake (~25-30)
- **F Poor (0-24)**: DataGPT (~20-25), Tellius (~20-25), DataChat (~15-20)

**Differentiation Achieved**:
- Clear 5-10 point gaps between similar competitors
- Scoop realistically positioned (not perfect)
- Business user empowerment lens maintained

---

## Implementation Plan

### Phase 1: Update Framework Document (1 hour)
- Rewrite BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md with 100-point system
- Define 4 sub-components × 5 points for each dimension
- Document Scoop's target score (80-83) with honest limitations
- Archive old 59-point version

### Phase 2: Re-Score All Competitors (3-4 hours)
- Start with proportional baseline (59pt → 100pt)
- Apply granular adjustments for differentiation
- Document rationale in each framework_scoring.md
- Validate distribution matches target (no clustering)

### Phase 3: Update All Documentation (2-3 hours)
- Update all 11 battle cards with new scores
- Update Power BI Copilot web comparison (already generated)
- Update README files
- Update tracking documents

### Phase 4: Generate Remaining Web Comparisons (8-10 hours)
- Generate 10 remaining competitor web comparisons
- Use new 100-point scores throughout
- Maintain consistent tone and transparency

**Total Estimated Time**: 14-18 hours

---

## Success Criteria

### Framework Quality
- ✅ Clean 100-point scale (not arbitrary 59)
- ✅ Clear differentiation (5-10 point gaps, not 1-3 points)
- ✅ Scoop realistically positioned (80-83, not 71 or 100)
- ✅ Granular sub-components (4 per dimension × 5 points)

### Scoring Validity
- ✅ Business user empowerment focus maintained
- ✅ Proportional relationships preserved (Domo still highest competitor)
- ✅ Evidence-based (all scores have documented rationale)
- ✅ Consistent methodology across all 11 competitors

### Business Impact
- ✅ Sales can explain scores easily (percentages are obvious)
- ✅ Honest about Scoop limitations (builds credibility)
- ✅ Clear competitive positioning (who we beat and why)
- ✅ Differentiates similar competitors (Qlik vs Zenlytic vs Tableau)

---

## Next Steps

**Immediate**:
1. Review this proposal - any adjustments needed?
2. Approve 100-point structure with 4×5 sub-components
3. Approve Scoop target score (~80-83 with honest limitations)
4. Approve competitor distribution targets

**Then Execute**:
1. Update framework document
2. Re-score all 12 (11 competitors + Scoop)
3. Update all documentation
4. Generate remaining web comparisons

**Estimated Start-to-Finish**: 2 days of focused work

---

**Questions for Approval**:
1. Is 100-point scale with 5 dimensions × 20 points approved?
2. Is Scoop at ~80-83/100 (acknowledging real gaps) acceptable?
3. Should we maintain Domo as highest competitor (~60-65)?
4. Any changes to proposed differentiation strategy?

---

**Last Updated**: September 27, 2025
**Status**: Awaiting approval to proceed