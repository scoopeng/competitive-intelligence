# BUA Framework Scoring - ThoughtSpot

**Competitor**: ThoughtSpot
**Date Scored**: September 27, 2025
**Last Updated**: September 30, 2025 (Understanding dimension rescored)
**Scored By**: AI Competitive Intelligence System
**Total Score**: 45/100 (45%, Category C - Moderate)
**Framework Version**: Business User Autonomy Framework v2.0 (100-point system)

---

## Dimension 1: Autonomy (11/20)

### Setup (5/8)
**Score**: 5/8
**Evidence**:
- **Timeline**: 2-4 weeks standard deployment (not "instant" as marketed)
- Requires IT configuration and data modeling first
- Environment setup (Dev/Prod) separation required
- Training videos, webinars, whitepapers required
- Must prepare "search-able" content before business users can access
**Source**:
- Phase 2 functionality analysis: "2-4 weeks for basic deployment"
- BATTLE_CARD: "2-4 weeks minimum"
**Reasoning**: Faster than some competitors but still requires significant IT setup. Not true self-service.

### Questions (4/6)
**Score**: 4/6
**Evidence**:
- Natural language search interface (good UX)
- BUT requires exact terminology matching
- Pre-built data models needed for "search-able" content
- Search paradigm less flexible than conversational
- Business users need to learn "search syntax"
**Source**: Multiple sources on search limitations
**Reasoning**: NL search works but requires specific terminology. Better than SQL but not true conversational freedom.

### Speed (2/6)
**Score**: 2/6
**Evidence**:
- 2-4 weeks minimum to first insight
- IT dependency for setup
- Data modeling required before use
- Consultant dependency common
**Source**: Phase 2 analysis, multiple implementation timelines
**Reasoning**: Cannot get value quickly. IT project, not instant insight.

**Total Autonomy**: 11/20

---

## Dimension 2: Flow (6/20)

### Native Integration (0/8)
**Score**: 0/8
**Evidence**:
- **Excel**: ZERO formula support - "Never learned how to do a VLOOKUP properly" (their marketing)
- **Slack**: One-way push only (not bidirectional), OAuth admin approval required
- **PowerPoint**: ZERO generation capability - must screenshot manually
- **Portal-only**: Must access ThoughtSpot interface for all analysis
**Source**:
- Phase 2: "ThoughtSpot has ZERO formula support vs Scoop's 150+ Excel functions"
- "No PowerPoint generation capability"
- BATTLE_CARD: "Zero Excel formulas"
**Reasoning**: Complete failure on workflow integration. Portal prison with one-way Slack notifications.

### Portal Prison (0/6)
**Score**: 0/6
**Evidence**:
- Must use ThoughtSpot portal for all analysis
- Search interface is separate login
- Slack integration is one-way push only
- Cannot work in Excel (no formulas)
- "Another portal to check" per BATTLE_CARD
**Source**: Multiple sources confirming portal dependency
**Reasoning**: 100% portal-dependent. No escape to native tools.

### Interface Simplicity (6/6)
**Score**: 6/6
**Evidence**:
- Search interface is intuitive for simple queries
- Natural language processing works
- BUT requires learning exact terminology
- Pre-built content needed
- "Search paradigm requires exact matches" per BATTLE_CARD
**Source**: Multiple usability reviews
**Reasoning**: Search is simple conceptually, but has learning curve for terminology.

**Total Flow**: 6/20

---

## Dimension 3: Understanding (8/20)

### Agentic Investigation Depth (2/8)
**Score**: 2/8
**Evidence**:
- **Marketing claim**: "Multi-dimensional analysis"
- **Reality**: Single query responses, NOT true agentic investigation
- "Change Analysis" shows WHAT changed, not WHY
- No probe dependencies - each query is independent
- No investigation planning or multi-round execution
- No hypothesis testing across multiple queries
- No context retention between searches
- User must manually run separate searches for follow-up
- Can't autonomously investigate root causes - only describe changes
**Source**:
- ThoughtSpot product documentation
- Phase 2 analysis: "True 3-10 query investigations vs single 'deep' query"
- BATTLE_CARD: "Can't investigate 'why' - only 'what'"
**Reasoning**: Single-query answers with basic drill-downs. Better than static dashboards (0 points) but far from autonomous agentic investigation. User must know what to ask next - no probe dependencies, no investigation planning. Scores 2/8 for single query capability.

**Key missing capabilities for higher scores**:
- ❌ No multi-round investigation planning
- ❌ No probe dependencies (later queries using earlier results)
- ❌ No automatic hypothesis testing
- ❌ No synthesis across multiple probe results
- ❌ User drives every step - not AI-driven

### Deep ML Understanding (4/6)
**Score**: 4/6
**Evidence**:
- SpotIQ provides real ML predictions (not fake AI or basic statistics)
- Automated pattern discovery using machine learning
- **BUT: Black box** - no explanations of WHY patterns exist
- No decision tree visibility (no J48/JRip equivalent)
- Can't show business rules or decision paths
- Cannot extract "If X and Y, then Z" rules
- Prediction-only approach, not explanatory
- 33.3% accuracy per Stanford HAI benchmark on complex queries
- Users see "Customer likely to churn" but not WHY
**Source**:
- Phase 2 analysis: "Black box predictions without explanations"
- BATTLE_CARD: "Can't explain WHY patterns exist"
- Stanford HAI benchmark: 33.3% accuracy
**Reasoning**: Has real ML (scores 4/6 for real ML models), rare among competitors. However, black-box predictions cannot score 6/6 which requires explainability. Missing decision trees, rule mining, and business rule extraction that would enable business users to understand WHY.

**What's missing for 6/6**:
- ❌ No decision tree visualization (showing decision paths)
- ❌ No rule extraction ("If tenure <12 AND contract=monthly, then churn")
- ❌ No business-understandable explanations of WHY patterns exist
- ❌ Just predictions without causal understanding

### Business-Language Explanation (2/6)
**Score**: 2/6
**Evidence**:
- Provides insights in natural language
- Shows patterns and trends detected
- BUT: Cannot explain underlying relationships or causation
- No confidence scoring visible to users
- No "why this pattern exists" explanations
- Shows correlations, not causation
- Summaries are descriptive (what happened) not explanatory (why it happened)
- Technical users can interpret, but non-technical users struggle
**Source**:
- Multiple SpotIQ product reviews
- ThoughtSpot documentation on SpotIQ outputs
**Reasoning**: Basic summaries with some natural language (scores 2/6). Better than raw SQL output (0 points) but not true business-language translation. Missing narratives with context, actionable recommendations, and causal reasoning. Cannot pass "boss test" - user would struggle to explain WHY findings matter to executives without additional analysis.

**What's missing for higher scores**:
- ❌ No narratives with business context
- ❌ No actionable recommendations with reasoning
- ❌ No causal explanations (why patterns exist)
- ❌ Not executive-ready without additional interpretation

**Total Understanding**: 8/20 (Investigation: 2/8, ML: 4/6, Explanation: 2/6)

---

## Dimension 4: Presentation (6/20)

### Visuals (4/6)
**Score**: 4/6
**Evidence**:
- Good visualization capabilities
- Interactive dashboards
- Multiple chart types available
- Search-generated visualizations work well
- BUT limited compared to full Tableau/Power BI
**Source**: Multiple product reviews
**Reasoning**: Solid visualization capabilities. Not cutting-edge but functional.

### Brand (0/8)
**Score**: 0/8
**Evidence**:
- No automatic brand detection
- No logo insertion
- No color scheme customization beyond basic theming
- Standard ThoughtSpot branding
- Cannot generate branded presentations
**Source**: No evidence of brand intelligence found
**Reasoning**: Zero brand automation. Manual branding only.

### Speed (2/6)
**Score**: 2/6
**Evidence**:
- **PowerPoint**: ZERO generation - must screenshot and format manually (3+ hours per BATTLE_CARD)
- **Export**: CSV/Excel static exports only
- **Slack**: One-way push (slow, manual)
- "Screenshot hell" workflow documented
**Source**:
- Phase 2: "No PowerPoint generation"
- BATTLE_CARD: "3+ hours manual work per report"
**Reasoning**: Completely manual presentation creation. No automation.

**Total Presentation**: 6/20

---

## Dimension 5: Data (14/20)

### Connections (4/4)
**Score**: 4/4
**Evidence**:
- Wide range of data source connectors
- Enterprise database support
- Cloud and on-premise options
- REST API for custom connections
- Good connectivity story
**Source**: ThoughtSpot documentation
**Reasoning**: Strong connector ecosystem. No major gaps here.

### Schema Evolution (0/8)
**Score**: 0/8
**Evidence**:
- Search-based architecture breaks when column names change
- Requires IT to update search models when schema changes
- No automatic adaptation documented
- "No schema evolution capability" per BATTLE_CARD
- Data modeling must be rebuilt on changes
**Source**: Multiple sources on maintenance burden
**Reasoning**: Universal competitive weakness. Complete failure like all others.

### Prep (4/4)
**Score**: 4/4
**Evidence**:
- Has data prep capabilities
- Can handle transformations
- Embraces ThoughtSpot interface for prep work
- Not as limited as some competitors
**Source**: ThoughtSpot product documentation
**Reasoning**: Adequate data prep for the use case.

### Data Quality (6/4)
**Score**: 6/4
**Evidence**:
- Limited writeback via Workato (third-party)
- No native CRM integration for ML scores
- Can trigger alerts/workflows
- Not fully operational like true writeback
**Source**: Workato integration documentation
**Reasoning**: Some operationalization possible via third-party, but not native.

**Total Data**: 14/20

---

## Score Summary

| Dimension | Score | Key Weakness |
|-----------|-------|--------------|
| Autonomy | 4/10 | 2-4 week setup, requires IT for data modeling and search content |
| Flow | 2/10 | Portal prison, zero Excel formulas, no PowerPoint generation |
| Understanding | 7/10 | Has real ML but black box only, single queries not investigation |
| Presentation | 2/10 | Manual PowerPoint creation, no brand automation, screenshot workflow |
| Data | 5/10 | **No schema evolution** (universal failure), but good connectors |
| **TOTAL** | **20/50** | **Category C - IT Platform** |

---

## Category: C - IT Platform (15-24 points)

**Definition**: Enterprise platforms that empower IT teams and analysts, but not business users directly. Require significant setup and maintenance.

**ThoughtSpot Reality**:
- Built for IT teams, marketed to business users
- Real ML (rare) but not explainable
- Search paradigm better than SQL but still requires IT setup
- $137K-$500K annual cost for enterprise
- Needs 96 CPUs/600GB RAM for 2-3TB data (infrastructure heavy)

---

## Key Differentiators vs Scoop (45/50)

### 1. **Flow Dimension** Gap
- **Scoop**: 9/10 (Excel formulas, native PowerPoint, Slack)
- **ThoughtSpot**: 2/10 (zero Excel formulas, no PowerPoint, portal only)
- **Impact**: Scoop works where you work. ThoughtSpot is portal prison with 3+ hour manual reporting.

### 2. **Data Dimension** Gap
- **Scoop**: 9/10 (automatic schema evolution)
- **ThoughtSpot**: 5/10 (0/4 on schema component - complete failure, but strong connectors)
- **Impact**: Schema changes break ThoughtSpot search models. Scoop adapts instantly.

### 3. **Autonomy Dimension** Gap
- **Scoop**: 9/10 (30-second setup)
- **ThoughtSpot**: 4/10 (2-4 weeks, IT-dependent)
- **Impact**: Weeks of IT setup vs instant value.

### 4. **Understanding Dimension** Gap
- **Scoop**: 9/10 (multi-pass investigation + explainable ML)
- **ThoughtSpot**: 7/10 (real ML but black box, single queries)
- **Impact**: Scoop explains WHY with business rules. ThoughtSpot predicts without explanation.

### 5. **Presentation Dimension** Gap
- **Scoop**: 9/10 (auto PowerPoint, brand intelligence)
- **ThoughtSpot**: 2/10 (screenshot hell, 3+ hours manual work)
- **Impact**: 30 seconds vs 3+ hours per presentation.

---

## Scoring Rationale: Why 20/50

**Strong Points**:
- **Real ML** (rare among competitors) - gives 3/3 on ML component
- **Good connectors** - gives 2/2 on connections
- **Adequate data prep** - gives 2/2 on prep

**Weak Points**:
- **Zero Excel formulas** - automatic 0/4 on Native Integration
- **Portal prison** - 0/3 on Portal component
- **No schema evolution** - automatic 0/4 (universal failure)
- **No PowerPoint generation** - 0/3 on Speed component
- **2-4 week setup** - penalizes Autonomy

**Why Higher Than Tableau Pulse (11/50)?**
- Has real ML (Tableau has detection only)
- Better investigation capabilities (even if limited)
- Stronger data connectivity
- More mature platform

**Why Lower Than Domo (estimate ~25-27/50)?**
- Worse workflow integration
- More IT-dependent setup
- Higher infrastructure requirements

---

## Key Evidence

**Cost Reality**:
- "$500k/yr for 20 people" (actual customer quote - Reddit)
- $137,000-$500,000 typical enterprise cost
- 40-140x more expensive than Scoop ($3,588)

**Performance Issues**:
- "Crashed with all our data" (customer quote)
- 96 CPUs/600GB RAM needed for 2-3TB
- 1-minute query timeout (kills long-running queries)

**Healthcare Exclusion**:
- Legal docs: "shall not upload PHI"
- Cannot handle HIPAA data
- Major industry limitation

**Accuracy**:
- 33.3% accuracy in Stanford HAI benchmark
- 2 out of 3 queries fail
- Black box predictions without explanations

---

## Validation Notes

**Score is defensible because**:
- ThoughtSpot is genuinely better than many competitors at ML (has real models)
- But BUA framework measures business user independence, not IT platform maturity
- 20/50 accurately reflects "good for analysts/IT, not for business users"
- Gartner rates highly for traditional BI (Categories 1-4), not business user autonomy (Category 5)

**This is a "Analyst Workbench"** not a business user tool:
- IT sets up search models → Analysts use search → Business users consume dashboards
- Not true self-service despite marketing claims
- Real value requires technical skills and IT support

---

**Last Updated**: September 27, 2025
**Framework Version**: Business User Autonomy 
**Confidence**: High (based on comprehensive research across 4 phases)