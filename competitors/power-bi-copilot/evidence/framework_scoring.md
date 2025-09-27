# BUA Framework Scoring - Power BI Copilot

**Competitor**: Power BI Copilot
**Date Scored**: September 27, 2025
**Scored By**: Competitive Intelligence Team
**Total Score**: 32/100 (32%, Category D - Weak)
**Previous Score**: 21/59 (rescaled to 100-point system)
**Previous Score**: 14/50 (28%, Category D - Marketing Mirage)

---

## Summary

Power BI Copilot scores 32/100 (32%) in the Business User Autonomy Framework, placing it in **Category D - Weak**. This reflects Microsoft's architectural choice to prioritize IT control and governance over business user independence.

**Key Strengths**:
- Natural language query interface
- Microsoft ecosystem integration
- Enterprise-grade governance

**Critical Limitations**:
- Requires F64 capacity ($67K/year infrastructure tax)
- Requires IT-maintained semantic models
- Single-query only (no investigation capability)
- Nondeterministic behavior (Microsoft's own admission)
- No Excel formula support (requires separate $30/user Copilot Pro)
- Gartner finding: Only 3% of IT leaders find significant value

---

## Category: D - Weak (25-39 points / 25-39%)

**Definition**: Weak self-service capabilities, mostly IT-dependent platform.

**Power BI Copilot Reality**:
- Requires extensive IT setup (F64 capacity, semantic models)
- Natural language interface exists but constrained to IT-built models
- Single query paradigm (no follow-up investigation)
- Portal-dependent (no Slack integration, limited Excel)
- Ongoing IT maintenance burden for semantic models

**Why Not Higher**: Despite being from Microsoft, Power BI Copilot requires IT for setup, semantic modeling, capacity management, and ongoing maintenance. Business users cannot operate independently.

**Why Not Lower**: Has natural language interface and AI capabilities, better than minimal capability tools (Category F).

---

## Detailed Scoring

### Dimension 1: Autonomy (7/20)

#### Setup (2/8)
**Score**: 2/8
**Evidence**:
- Requires F64 capacity provisioning ($67K/year minimum)
- 24-hour wait after F64 activation
- IT must build semantic model before Copilot works
- Data warehouse setup required (Azure Synapse or compatible)
- 14+ weeks typical implementation timeline
**Source**: Microsoft Fabric documentation, customer implementations
**Reasoning**: Extensive IT project, not self-service setup.

#### Questions (3/6)
**Score**: 3/6
**Evidence**:
- Natural language query interface exists
- BUT: "Copilot doesn't answer follow-up questions. One question at a time" (Microsoft docs)
- "Can't currently answer questions that require generating new insights" (Microsoft docs)
- Constrained to semantic model scope (IT-defined)
**Source**: Microsoft official documentation
**Reasoning**: Has NL interface but severely limited capabilities.

#### Speed (2/6)
**Score**: 2/6
**Evidence**:
- 2-5 seconds for queries once semantic model ready
- BUT: 14+ weeks before users can ask first question
- Dependent on semantic model performance
**Reasoning**: Fast execution but extremely slow time-to-value.

#### Time to First Insight (1/3)
**Score**: 1/3
**Evidence**:
- 14+ weeks minimum (F64 provisioning + model building)
- IT project required before business users can use
- $40K-$80K implementation cost
**Source**: Industry standard Power BI Copilot implementations
**Reasoning**: Months to value, not minutes.

#### Governed Self-Service (1/3)
**Score**: 1/3
**Evidence**:
- Has governance features (row-level security, etc.)
- BUT: So restrictive that business users can't operate independently
- IT controls all data access via semantic model
**Reasoning**: Governance exists but blocks self-service.

**Total Autonomy**: 7/20

---

### Dimension 2: Flow (6/20)

#### Native Integration (3/8)
**Score**: 3/8
**Evidence**:
- **Excel**: No formula support in Power BI Copilot (requires separate $30/user Copilot Pro)
- **Slack**: Not supported (Teams only)
- **PowerPoint**: Manual export required
- Portal-dependent for all Copilot features
**Source**: Microsoft documentation
**Reasoning**: Some integration but mostly manual export workflows.

#### Portal Prison (0/6)
**Score**: 0/6
**Evidence**:
- Must use Power BI portal for all Copilot features
- No Slack integration ("Teams only" - Microsoft ecosystem lock-in)
- Cannot escape portal to work in native tools
- "No dedicated Copilot REST APIs exist" (Microsoft docs)
**Source**: Microsoft documentation
**Reasoning**: 100% portal-dependent.

#### Interface Simplicity (3/6)
**Score**: 3/6
**Evidence**:
- Natural language interface is simple
- BUT: Still requires understanding of semantic model structure
- Users must know what's in the model IT built
- DAX required for custom calculations
**Reasoning**: NL helps but complexity remains.

**Total Flow**: 6/20

---

### Dimension 3: Understanding (7/20)

#### Investigation (2/8)
**Score**: 2/8
**Evidence**:
- Single query only: "One question at a time" (Microsoft docs)
- No follow-up capability
- "Can't currently answer questions that require generating new insights"
- No multi-pass investigation
- No hypothesis testing
**Source**: Microsoft official documentation
**Reasoning**: Answers "what" but can't investigate "why".

#### ML (0/6)
**Score**: 0/6
**Evidence**:
- Power BI Copilot has no ML capabilities
- No automatic pattern discovery
- No clustering or decision trees
- Must export to external ML tools
**Reasoning**: No ML features in Copilot.

#### Explanation (5/6)
**Score**: 5/6
**Evidence**:
- Provides natural language explanations of queries
- Shows SQL generated (transparency)
- Explains data in business language
- WARNING: "Nondeterministic" outputs (Microsoft admits)
**Source**: Microsoft documentation
**Reasoning**: Does explain results, scores full points despite quality concerns.

**Total Understanding**: 7/20

---

### Dimension 4: Presentation (6/20)

#### Automatic Generation (3/8)
**Score**: 3/8
**Evidence**:
- Can generate basic visuals from queries
- Manual export to PowerPoint required
- No automatic presentation creation
- Each visual requires manual insertion
**Reasoning**: Some automation but manual assembly.

#### Brand Control (1/6)
**Score**: 1/6
**Evidence**:
- Power BI has theming capabilities
- Limited brand control in Copilot outputs
- Visuals use Power BI default styles
**Reasoning**: Basic branding exists.

#### Distribution (2/6)
**Score**: 2/6
**Evidence**:
- Can share Power BI reports
- No automatic email/Slack distribution from Copilot
- Must use Power BI sharing workflows
**Reasoning**: Manual distribution required.

**Total Presentation**: 6/20

---

### Dimension 5: Data (6/20)

#### Multi-Source (1/4)
**Score**: 1/4
**Evidence**:
- Semantic model can include multiple sources
- BUT: IT must integrate sources in model first
- Business users can't connect new sources themselves
- All sources must be pre-configured in F64
**Reasoning**: Multi-source possible but IT-dependent.

#### Schema Evolution (0/8)
**Score**: 0/8
**Evidence**:
- Semantic model breaks when source data changes
- 14-day rebuild typical when column added
- $225K-$480K/year maintenance burden (0.5-1 FTE)
- 30-50 reports break per year on schema changes
**Source**: Customer reports, industry standard maintenance costs
**Reasoning**: Complete failure on schema evolution - this is Power BI's Achilles heel.

#### Data Quality (3/4)
**Score**: 3/4
**Evidence**:
- Semantic model requires pre-cleaned data
- No smart scanner for messy data
- BUT: Data quality features exist in Power BI platform
**Reasoning**: Requires clean data but has quality tools.

#### Data Prep (2/4)
**Score**: 2/4
**Evidence**:
- Requires DAX expertise (3-6 months learning curve)
- Power Query available but separate tool
- Business users can't do data prep without IT
**Reasoning**: Capabilities exist but not accessible to business users.

**Total Data**: 6/20

---

## Comparison to Previous Scoring Systems

| Dimension | Old (50pt) | 59pt | New (100pt) | Percentage |
|-----------|-----------|------|-------------|------------|
| Autonomy | 3/10 | 6/16 | 7/20 | 35% |
| Flow | 2/10 | 3/10 | 6/20 | 30% |
| Understanding | 3/10 | 4/10 | 7/20 | 35% |
| Presentation | 2/10 | 4/10 | 6/20 | 30% |
| Data | 4/10 | 4/13 | 6/20 | 30% |
| **Total** | **14/50** | **21/59** | **32/100** | **32%** |
| **Category** | **D** | **C** | **D** | **Weak** |

**Why the Category Changed**:
- 100-point system uses stricter category thresholds
- Category D: 25-39 points (Weak self-service)
- 32/100 falls into Category D range
- Better reflects the reality of extensive IT dependency

**Consistent Issues Across All Scoring Systems**:
- Requires extensive IT involvement (F64, semantic models)
- No business user autonomy (setup, modeling, maintenance all IT)
- Schema evolution remains complete failure (0/8 in new framework)
- Single-query limitation prevents true investigation

---

## Key Differentiators vs Scoop

### 1. Schema Evolution (Power BI: 0/8, Scoop: 6/8)
- **Power BI Copilot**: Semantic model breaks, 14-day rebuild, $225K-$480K/year maintenance
- **Scoop**: Automatic adaptation, zero maintenance, $675K-$1.4M savings over 3 years

### 2. Investigation Depth (Power BI: 2/8, Scoop: 8/8)
- **Power BI Copilot**: Single query only, no follow-up, "can't generate new insights"
- **Scoop**: Multi-pass investigation (3-10 queries), automatic hypothesis testing

### 3. Autonomy (Power BI: 7/20, Scoop: 18/20)
- **Power BI Copilot**: Requires F64 ($67K), IT-built models, 14+ weeks setup
- **Scoop**: 30-second setup, no IT required, no infrastructure tax

### 4. Excel Integration (Power BI: 0, Scoop: 150+ functions)
- **Power BI Copilot**: No Excel formulas (requires separate $30/user Copilot Pro)
- **Scoop**: Native spreadsheet engine with 150+ Excel functions

### 5. Deterministic Results (Power BI: No, Scoop: Yes)
- **Power BI Copilot**: "Nondeterministic behavior" - same question, different answers
- **Scoop**: Deterministic - same question always produces identical result

---

## Evidence Sources

### Microsoft's Own Admissions
- "Nondeterministic... not guaranteed to produce the same answer": https://learn.microsoft.com/en-us/fabric/fundamentals/copilot-power-bi-privacy-security
- "Generic, inaccurate, or even misleading outputs": https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai
- "One question at a time" + "Can't answer questions requiring new insights": Microsoft documentation

### Third-Party Research
- **Gartner Survey (2025)**: Only 3% of IT leaders find significant value (123 surveyed)
- **GoCollectiv Case Study**: $300M SaaS platform, 30-day implementation, 12% adoption
- **Data Goblins Expert**: "In BI, these mistakes can get you fired"

### Pricing
- **F64 Capacity**: $67,392/year ($5,616/month reserved)
- **Power BI Pro**: $14/user/month ($168/year)
- **Excel Copilot Pro**: $30/user/month ($360/year) - separate subscription

---

## Conclusion

Power BI Copilot scores 32/100 (32%, Category D - Weak) because it:
- **Requires IT infrastructure** ($67K F64 capacity)
- **Requires IT semantic models** (breaks on schema changes)
- **Limited to single queries** (no investigation)
- **Nondeterministic results** (Microsoft's own warning)
- **No business user autonomy** (IT-dependent for everything)

This is not a criticism of Microsoft's product design - Power BI optimizes for governance, IT control, and enterprise scalability (Gartner's Categories 1-4). BUA measures a different dimension: business user independence (Gartner's missing 5th category).

Organizations that prioritize IT control and centralized governance should consider Power BI. Organizations that prioritize business user autonomy and speed to insight should consider Scoop.

---

**Last Updated**: September 27, 2025
**Next Review**: When Microsoft releases significant Copilot updates