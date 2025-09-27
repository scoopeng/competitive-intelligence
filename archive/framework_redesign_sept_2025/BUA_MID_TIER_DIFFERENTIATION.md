# BUA Components That Differentiate Mid-Tier Competitors

**Date**: September 27, 2025
**Purpose**: Identify BUA components where Power BI, Qlik, ThoughtSpot, Tableau Pulse, etc. meaningfully differ

---

## Problem Statement

Current framework creates variance between Scoop/Domo vs everyone else, but mid-tier competitors (scoring 11-20/50) are clustered together. Need components that:
- Genuinely measure business user autonomy
- Create variance among mid-tier (not just Scoop/Domo advantages)
- Are paradigm-agnostic (not dashboard-biased)

---

## Candidate Components

### 1. Self-Service Permissions (0-3 points)

**What it measures**: Can business users control who sees their insights without IT?

**Why BUA**: Autonomous users need to share selectively without waiting for IT to set permissions.

**Scoring**:
- **3/3**: Business users set permissions themselves (share with person/team/org)
- **2/3**: Business users request permissions, quick approval workflow
- **1/3**: IT controls all permissions, slow approval
- **0/3**: No sharing permissions or IT-only

**Expected Distribution**:
- **Power BI**: 3/3 (workspaces, share with AD groups, self-service)
- **Qlik**: 2/3 (governed but business users can share within rules)
- **ThoughtSpot**: 2/3 (row-level security but users can share)
- **Domo**: 3/3 (self-service sharing)
- **Sisense**: 2/3 (some self-service)
- **Tableau Pulse**: 2/3 (metric-level permissions)
- **Scoop**: 3/3 (Slack channels = instant permissions)
- **Zenlytic**: 1/3 (IT-controlled)
- **DataGPT**: 1/3 (limited sharing)
- **Tellius**: 1/3 (IT-controlled)
- **DataChat**: 0/3 (no documented sharing)
- **Snowflake**: 0/3 (SQL permissions, not business user)

**Creates variance?**: ✅ YES - Power BI/Domo/Scoop at 3, several at 2, several at 0-1

---

### 2. Time to First Insight (0-3 points)

**What it measures**: How long before a NEW business user gets their first useful insight?

**Why BUA**: True autonomy = minimal time investment to get value.

**Scoring**:
- **3/3**: <5 minutes to first insight (no setup, no training)
- **2/3**: <1 hour to first insight (minimal setup or training)
- **1/3**: 1-8 hours to first insight (significant training required)
- **0/3**: Days/weeks to first insight (requires IT setup + extensive training)

**Expected Distribution**:
- **Scoop**: 3/3 (<30 seconds after Slack auth)
- **Tableau Pulse**: 3/3 (metrics delivered instantly)
- **DataGPT**: 2/3 (fast but some setup)
- **Domo**: 2/3 (fast once set up, but setup takes time)
- **ThoughtSpot**: 1/3 (requires semantic layer, then fast)
- **Power BI**: 1/3 (steep learning curve, many hours of training)
- **Qlik**: 0/3 (58% fail certification, hour-long loads)
- **Sisense**: 1/3 (dashboard training required)
- **Zenlytic**: 2/3 (semantic layer helps, but setup required)
- **Tellius**: 1/3 (complex interface)
- **DataChat**: 1/3 (GEL complexity)
- **Snowflake**: 0/3 (SQL knowledge required)

**Creates variance?**: ✅ YES - Scoop/Tableau Pulse at 3, several at 2, several at 0-1

**Differentiates mid-tier?**: ✅ YES - Tableau Pulse (3) vs Power BI (1) vs Qlik (0)

---

### 3. API/Automation Access (0-2 points)

**What it measures**: Can business users automate repetitive tasks without developers?

**Why BUA**: Power users need to automate without calling engineering.

**Scoring**:
- **2/2**: Business-user-friendly automation (workflows, scheduled tasks, easy API)
- **1/2**: Developer-required API but accessible
- **0/2**: No API or developer-only access

**Expected Distribution**:
- **Power BI**: 2/2 (Power Automate integration, business user friendly)
- **Domo**: 2/2 (workflow automation built-in)
- **Sisense**: 2/2 (API-first, but needs some tech skill)
- **Qlik**: 1/2 (strong API but developer-focused)
- **ThoughtSpot**: 1/2 (REST API but technical)
- **Tableau Pulse**: 1/2 (some automation)
- **Scoop**: 2/2 (Slack workflows, Excel automation)
- **Zenlytic**: 1/2 (API exists)
- **DataGPT**: 1/2 (API exists)
- **Tellius**: 1/2 (API exists)
- **Snowflake**: 1/2 (technical API)
- **DataChat**: 0/2 (NO API documented as weakness)

**Creates variance?**: ⚠️ SOME - Most have APIs, DataChat clearly disadvantaged

**Differentiates mid-tier?**: ✅ YES - Power BI/Domo (2) vs ThoughtSpot/Qlik (1) vs DataChat (0)

---

### 4. Governed Self-Service (0-3 points)

**What it measures**: Can business users explore freely WITHIN guardrails, without breaking governance?

**Why BUA**: Enterprise needs both autonomy AND control. Best platforms enable exploration without risk.

**Scoring**:
- **3/3**: Business users explore freely, governance automatic (row-level security, certified data, can't break anything)
- **2/3**: Governed but users feel constraints (must stay in approved areas)
- **1/3**: Light governance, users can access things they shouldn't
- **0/3**: No governance (risky) or locked down (no exploration)

**Expected Distribution**:
- **ThoughtSpot**: 3/3 (row-level security, semantic layer governance, users explore safely)
- **Qlik**: 3/3 (strong governance model, associative model is governed)
- **Power BI**: 2/3 (AD integration but users can create uncontrolled content)
- **Tableau Pulse**: 3/3 (metrics are governed, users can't break)
- **Domo**: 2/3 (governance exists but not foolproof)
- **Zenlytic**: 3/3 (semantic layer ensures governance)
- **Scoop**: 2/3 (Slack channels provide some governance, but not row-level)
- **Sisense**: 2/3 (embedding provides some governance)
- **DataGPT**: 1/3 (single source, limited governance model)
- **Tellius**: 1/3 (weaker governance)
- **DataChat**: 1/3 (limited governance)
- **Snowflake**: 2/3 (SQL permissions are strong but not business-user-friendly)

**Creates variance?**: ✅ YES - ThoughtSpot/Qlik/Tableau/Zenlytic excel (3), others vary

**Differentiates mid-tier?**: ✅ EXCELLENT - ThoughtSpot/Qlik (3) vs Power BI/Domo (2) vs others (1)

**Scoop advantage?**: ❌ NO - Scoop at 2/3, enterprise platforms WIN here

---

### 5. Multi-Source Analysis (0-3 points)

**What it measures**: Can business users combine data from multiple sources in one analysis?

**Why BUA**: Real business questions span systems. Autonomy = not waiting for IT to join data.

**Scoring**:
- **3/3**: Business users easily combine unlimited sources in single analysis
- **2/3**: Can combine 2-5 sources with some setup
- **1/3**: Can combine sources but requires technical skills
- **0/3**: Single source only or IT must pre-join

**Expected Distribution**:
- **Scoop**: 3/3 (combines sources conversationally)
- **Domo**: 3/3 (strong multi-source capability)
- **ThoughtSpot**: 2/3 (can combine but semantic layer complexity)
- **Power BI**: 3/3 (strong data modeling, business users can combine)
- **Qlik**: 2/3 (associative model combines but setup required)
- **Sisense**: 2/3 (can combine)
- **Tableau Pulse**: 1/3 (metrics are single-source typically)
- **Zenlytic**: 2/3 (semantic layer helps)
- **DataGPT**: 0/3 (SINGLE SOURCE ONLY - documented limitation)
- **Tellius**: 2/3 (can combine)
- **DataChat**: 1/3 (limited multi-source)
- **Snowflake**: 2/3 (SQL joins but technical)

**Creates variance?**: ✅ YES - Wide spread 0-3

**Differentiates mid-tier?**: ✅ YES - Power BI/Domo (3) vs ThoughtSpot/Qlik (2) vs Tableau Pulse (1) vs DataGPT (0)

**Scoop advantage?**: ⚠️ TIES with Domo/Power BI

---

### 6. Scheduled Delivery (0-2 points)

**What it measures**: Can business users schedule reports/insights to be delivered automatically?

**Why BUA**: Autonomous users don't manually run reports daily - they automate.

**Scoring**:
- **2/2**: Business users easily schedule delivery (email, Slack, etc.) with self-service
- **1/2**: Scheduling exists but IT must configure
- **0/2**: No scheduling, manual only

**Expected Distribution**:
- **Tableau Pulse**: 2/2 (core feature - scheduled metric delivery)
- **Domo**: 2/2 (scheduled reports)
- **Power BI**: 2/2 (scheduled refresh + delivery)
- **ThoughtSpot**: 2/2 (scheduled liveboards)
- **Qlik**: 2/2 (scheduled apps)
- **Sisense**: 2/2 (scheduled dashboards)
- **Scoop**: 2/2 (Slack scheduled messages)
- **Zenlytic**: 1/2 (some scheduling)
- **DataGPT**: 1/2 (basic scheduling)
- **Tellius**: 1/2 (limited)
- **DataChat**: 0/2 (no scheduling mentioned)
- **Snowflake**: 0/2 (SQL-based, no delivery)

**Creates variance?**: ⚠️ LIMITED - Most traditional BI has this at 2/2

**Differentiates mid-tier?**: ❌ NO - Most at 2/2, limited spread

---

## Recommended Components to Add

### Tier 1: HIGH VALUE - Add These (8 points)

1. **Governed Self-Service (0-3)**: Creates excellent mid-tier variance
   - ThoughtSpot/Qlik WIN (3), Scoop middle (2), creates real differentiation
   - Measures important BUA capability (explore safely)

2. **Time to First Insight (0-3)**: Creates excellent variance
   - Scoop/Tableau Pulse WIN (3), wide spread among mid-tier
   - Measures critical BUA capability (speed to value)

3. **Multi-Source Analysis (0-3)**: Creates good variance
   - Power BI/Domo/Scoop WIN (3), DataGPT loses (0), mid-tier varies
   - Measures important BUA capability (data integration)

**Subtotal: 9 points added**

### Tier 2: MODERATE VALUE - Consider (3 points)

4. **API/Automation (0-2)**: Some variance
   - Power BI/Domo differentiate, DataChat exposed as 0

5. **Self-Service Permissions (0-3)**: Some variance
   - But maybe overlaps with existing "Interface Simplicity"

### Tier 3: LOW VALUE - Skip

6. **Scheduled Delivery (0-2)**: Too many ties, commodity feature

---

## Impact Analysis: Adding Tier 1 Only (59-Point Framework)

**Add**:
- Governed Self-Service (0-3) → Autonomy dimension
- Time to First Insight (0-3) → Autonomy dimension
- Multi-Source Analysis (0-3) → Data dimension

**New totals**:
- Autonomy: 10 → 13
- Flow: 10 → 10
- Understanding: 10 → 10
- Presentation: 10 → 10
- Data: 10 → 13
- **Total: 50 → 56 points**

### Estimated Scores (56-Point Framework)

| Competitor | Old (50pt) | New (56pt) | Governed | Time-to-Insight | Multi-Source | % Old | % New | Change |
|------------|------------|------------|----------|-----------------|--------------|-------|-------|--------|
| Scoop | 45 | 51 | +2 | +3 | +3 | 90% | 91% | +1% |
| Domo | 25 | 33 | +2 | +2 | +3 | 50% | 59% | +9% |
| ThoughtSpot | 20 | 28 | +3 | +1 | +2 | 40% | 50% | +10% |
| Power BI | 14 | 21 | +2 | +1 | +3 | 28% | 38% | +10% |
| Qlik | 16 | 23 | +3 | +0 | +2 | 32% | 41% | +9% |
| Tableau Pulse | 11 | 18 | +3 | +3 | +1 | 22% | 32% | +10% |
| Zenlytic | 15 | 21 | +3 | +2 | +2 | 30% | 38% | +8% |
| Sisense | 14 | 19 | +2 | +1 | +2 | 28% | 34% | +6% |
| DataGPT | 12 | 15 | +1 | +2 | +0 | 24% | 27% | +3% |
| Tellius | 11 | 15 | +1 | +1 | +2 | 22% | 27% | +5% |
| DataChat | 11 | 14 | +1 | +1 | +1 | 22% | 25% | +3% |
| Snowflake | 13 | 16 | +2 | +0 | +2 | 26% | 29% | +3% |

### Key Insights

**Winners** (gain 9-10%):
- **ThoughtSpot**: 40% → 50% (governance is their strength, reaches Category B)
- **Power BI**: 28% → 38% (multi-source and Microsoft integration)
- **Tableau Pulse**: 22% → 32% (time-to-insight is their thing)
- **Qlik**: 32% → 41% (governance is their strength)

**Losers** (gain <5%):
- **DataGPT**: 24% → 27% (single source exposed, loses multi-source points)
- **DataChat**: 22% → 25% (no advantages on new components)
- **Snowflake**: 26% → 29% (SQL interface hurts time-to-insight)

**Scoop**:
- 90% → 91% (barely changes - not a Scoop advantage set)
- Gap to Domo: 20 pts → 18 pts (40% → 32% relative)

**Category Distribution**:
- **Category A (60%+)**: Scoop only (91%)
- **Category B (40-59%)**: Domo (59%), ThoughtSpot (50%)
- **Category C (25-39%)**: Power BI, Qlik, Zenlytic, Sisense, Tableau Pulse (32-41%)
- **Category D (0-24%)**: DataGPT, Tellius, DataChat, Snowflake (25-29%)

**Mid-tier now clearly differentiated**:
- Qlik (41%) vs Power BI (38%) vs Zenlytic (38%) vs Sisense (34%) vs Tableau Pulse (32%)
- 9-point spread among mid-tier (was 5-point spread)

---

## Validation

### Governed Self-Service: ✅ YES
- ThoughtSpot: Row-level security extensively documented
- Qlik: Governance model documented, "section access"
- Tableau Pulse: Metric governance documented
- Zenlytic: Semantic layer governance documented

### Time to First Insight: ✅ YES
- Qlik: "58% fail certification" + "hour-long loads" documented
- Scoop: 30-second setup documented
- Tableau Pulse: Instant delivery documented
- Power BI: Training requirements documented

### Multi-Source Analysis: ✅ YES
- DataGPT: "Single source only" documented limitation
- Power BI: Data modeling capabilities documented
- Domo: Multi-source documented
- Scoop: Multi-source documented

---

## Recommendation

**✅ ADD TIER 1 COMPONENTS (9 points) → 59-point framework**

Why these 3:
1. ✅ Create variance among mid-tier (ThoughtSpot, Qlik, Power BI, Tableau Pulse differentiate)
2. ✅ Genuine BUA measures (governance, speed, integration)
3. ✅ Scoop doesn't dominate (scores 2-3, not 3 on all)
4. ✅ Evidence exists in current research
5. ✅ Paradigm-agnostic

Impact:
- Mid-tier spread: 5 points → 9 points (80% increase)
- ThoughtSpot/Qlik get credit for governance strength
- Tableau Pulse gets credit for instant delivery
- Power BI gets credit for multi-source
- Scoop gap: 40% → 32% (more credible)