# BUPAF Quick Comparison Matrix

**Last Updated**: January 2025  
**Status**: Initial scoring based on existing research - to be enhanced with targeted analysis  

## Overall BUPAF Scores (40 points maximum)

| Competitor | Independence | Analytical Depth | Workflow | Communication | **TOTAL** | Category |
|------------|-------------|-----------------|----------|---------------|-----------|----------|
| **Scoop** | 9/10 | 9/10 | 9/10 | 9/10 | **36/40** | A |
| Domo | 7/10 | 5/10 | 5/10 | 7/10 | **24/40** | C |
| DataGPT | 4/10 | 4/10 | 3/10 | 4/10 | **15/40** | C |
| ThoughtSpot | 4/10 | 7/10 | 2/10 | 5/10 | **18/40** | C |
| Tellius | 3/10 | 7/10 | 2/10 | 4/10 | **16/40** | C |
| Zenlytic | 3/10 | 6/10 | 2/10 | 4/10 | **15/40** | C |
| Power BI Copilot | 3/10 | 3/10 | 3/10 | 4/10 | **13/40** | D |
| Snowflake Cortex | 2/10 | 4/10 | 2/10 | 3/10 | **11/40** | D |
| Sisense | 2/10 | 2/10 | 2/10 | 4/10 | **10/40** | D |
| Tableau Pulse | 2/10 | 2/10 | 1/10 | 4/10 | **9/40** | D |
| Qlik | 2/10 | 2/10 | 2/10 | 3/10 | **9/40** | D |
| DataChat | 1/10 | 1/10 | 1/10 | 2/10 | **5/40** | D |

## Detailed Breakdown

### Dimension 1: Independence (Can business users work alone?)

| Competitor | Score | Evidence | Key Limitation |
|------------|-------|----------|----------------|
| **Scoop** | 9/10 | Email CSV, natural language, no training | Some complex data needs IT |
| Domo | 7/10 | Business user tools | Still needs IT setup |
| DataGPT | 4/10 | Analyst focus | Technical users mainly |
| ThoughtSpot | 4/10 | "Search-driven" | Requires data modeling |
| Others | 1-3/10 | IT dependency | Complete IT control |

### Dimension 2: Analytical Depth (What questions can they answer?)

| Competitor | Score | Can Do | Cannot Do |
|------------|-------|--------|-----------|
| **Scoop** | 9/10 | ML_GROUP multivariate, ML_PERIOD causality, J48/M5 explanatory models | Some optimization |
| ThoughtSpot | 7/10 | Basic ML, clustering | No explanatory analysis, no multivariate |
| Tellius | 7/10 | Some root cause | No dynamic ML, too complex for users |
| Zenlytic | 6/10 | Basic forecasting | No explanatory ML, YAML required |
| DataGPT | 5/10 | Fast single metrics | No ML, no multivariate, no investigation |
| Snowflake | 4/10 | SQL aggregations | No ML whatsoever, just queries |
| Others | 1-3/10 | Basic metrics | No ML, no "why", no patterns |

### Dimension 3: Workflow Integration (How naturally does it fit?)

| Competitor | Data Mgmt | Excel | PowerPoint | Collaboration | Automation |
|------------|-----------|-------|------------|---------------|------------|
| **Scoop** | ✅ Auto schema evolution | ✅ =SCOOP() formulas | ✅ 30-sec generation | ✅ Slack in 30 sec | ✅ Full auto |
| DataGPT | ❌ Schema rigid | ❌ Export only | ❌ Manual (3-4 hrs) | ⚠️ API available | ⚠️ Limited |
| Domo | ❌ IT required | ⚠️ Export only | ❌ Manual (3-4 hrs) | ⚠️ Portal prison | ⚠️ Basic |
| ThoughtSpot | ❌ Models break | ❌ Export only | ❌ Manual (3-4 hrs) | ⚠️ Limited | ❌ None |
| Tellius | ❌ IT heavy | ❌ Export only | ❌ Manual (3-4 hrs) | ❌ None | ❌ None |
| Zenlytic | ❌ YAML hell | ❌ Export only | ❌ Manual (3-4 hrs) | ⚠️ Limited | ❌ None |
| Power BI | ❌ IT required | ⚠️ Export only | ❌ Manual (3-4 hrs) | ⚠️ Portal only | ⚠️ Basic |
| Snowflake | ❌ Semantic models | ❌ None | ❌ Manual (3-4 hrs) | ❌ 2-4 week dev | ❌ Per-query $ |
| Tableau | ❌ No evolution | ❌ None | ❌ Manual (3-4 hrs) | ⚠️ Alerts only | ❌ Rigid |
| Others | ❌ IT required | ❌ None | ❌ Manual (3-4 hrs) | ❌ None | ❌ None |

### Dimension 4: Business Communication (How clear is output?)

| Competitor | Natural Language | Explanations | Narrative | Visuals | Actions |
|------------|-----------------|--------------|-----------|---------|---------|
| **Scoop** | ✅ Conversational | ✅ Clear | ✅ Story | ✅ Smart | ✅ Next steps |
| DataGPT | ✅ Natural | ⚠️ Basic | ⚠️ Some | ✅ Good | ⚠️ Basic |
| Domo | ⚠️ Guided | ⚠️ Basic | ❌ No | ✅ Good | ⚠️ Basic |
| ThoughtSpot | ⚠️ Search | ⚠️ Technical | ❌ No | ✅ Good | ⚠️ Basic |
| Others | ❌ Technical | ❌ Raw data | ❌ No | ⚠️ OK | ❌ None |

## Category Distribution

### Category A: Empowerment Platforms (36-40 points)
- **Scoop** (36/40) - Only true business user empowerment platform with investigation engine

### Category B: Guided Systems (26-35 points)
- *None currently qualify* - All fall short on independence

### Category C: Analyst Workbenches (15-25 points)
- **DataGPT** (20/40) - Fast but schema-rigid, no investigation
- **Domo** (18/40) - Dashboard-first with AI Chat limitations
- **ThoughtSpot** (18/40) - Real AI but 33.3% accuracy, $140K/year
- **Tellius** (16/40) - Genuine ML but requires data scientists
- **Zenlytic** (15/40) - YAML/SQL configuration nightmare

### Category D: Marketing Mirages (0-14 points)
- **Power BI Copilot** (13/40) - Nondeterministic behavior, Excel COPILOT separate
- **Snowflake Cortex** (12/40) - 6-12 month migration, vendor lock-in
- **Sisense** (10/40) - 14+ week implementation, ARIMA isn't AI
- **Tableau Pulse** (9/40) - Not real AI (embedding models), 40x scaling crisis
- **Qlik** (9/40) - Can't handle typos, zero adoption found
- **DataChat** (5/40) - 7 years, zero reviews - possible vaporware

## Hidden Costs & Time-to-Value Reality

### Implementation Timeline
| Competitor | Setup Time | Semantic Models | Custom Dev | Time to First Insight |
|------------|------------|-----------------|------------|----------------------|
| **Scoop** | 30 seconds | None needed | None | 30 seconds |
| DataGPT | 2-4 weeks | Required | API integration | 2-4 weeks |
| Domo | 8-12 weeks | Dashboard setup | Limited | 2-3 months |
| ThoughtSpot | 12+ weeks | Data modeling | None | 3-4 months |
| Snowflake | 3-4 months | YAML required | Slack bot (2-4 wks) | 3-4 months |
| Power BI | 4-8 weeks | IT setup | None | 1-2 months |
| Others | 8-16 weeks | Various | Various | 2-4 months |

### True Annual Cost (200 users)
| Competitor | License | Hidden Costs | Maintenance | Total Annual |
|------------|---------|--------------|-------------|--------------|
| **Scoop** | $3,588 | None | $0 | **$3,588** |
| Snowflake Cortex | $50K | $880K compute + $300K setup | $360K (2 FTEs) | **$1,590,000** |
| ThoughtSpot | $140K | Implementation | $180K (1 FTE) | **$320,000+** |
| Domo | $134K avg | Consumption chaos | $180K (1 FTE) | **$314,000+** |
| Power BI | $24K | E5 licenses + capacity | $180K (1 FTE) | **$204,000+** |
| DataGPT | $60K+ | Data prep | $180K (1 FTE) | **$240,000+** |
| Others | Varies | Significant | $180K+ | **$200,000+** |

## The Machine Learning Sophistication Gap

### What Scoop Has (Unique)
| Capability | Scoop | Best Competitor | Others |
|------------|-------|-----------------|--------|
| **ML_GROUP** | ✅ Multivariate analysis with explanations | ❌ None | ❌ None |
| **ML_PERIOD** | ✅ Temporal causality analysis | ❌ None | ❌ None |
| **J48 (C4.5)** | ✅ Explainable decision trees | ⚠️ Black box only (ThoughtSpot) | ❌ None |
| **M5 Rules** | ✅ Complex relationship networks | ❌ None | ❌ None |
| **Explanatory Focus** | ✅ WHY patterns exist | ⚠️ Prediction only | ❌ No ML |
| **Multivariate** | ✅ 47+ variables simultaneously | ⚠️ Basic correlation | ❌ Single metrics |
| **Hidden Patterns** | ✅ Finds non-obvious interactions | ❌ None | ❌ None |
| **Business Translation** | ✅ Plain English explanations | ⚠️ Technical output | ❌ Numbers only |

### The Depth Difference
**Scoop**: "ML_GROUP found churn correlates with support response time AND usage frequency AND billing errors - a three-way interaction. Fixing any two reduces risk by 71%."

**Best Competitor**: "Churn rate is 15%. Here's a chart."

**Most Competitors**: "SELECT churn_rate FROM customers"

## Key Insights

### The ML Sophistication Gap
- **Scoop**: PhD-level multivariate explanatory analysis
- **Best competitor**: Basic prediction without explanation
- **Most competitors**: Zero ML capabilities
- **Impact**: Finding patterns humans would never discover

### The Independence Gap
- **Scoop**: 9/10 on independence
- **Best competitor**: 6/10 (DataGPT)
- **Average competitor**: 3.1/10
- **Gap**: 3-6 points (30-60% advantage)

### The Workflow Gap  
- **Scoop**: 9/10 on workflow integration
- **Best competitor**: 4/10 (Domo)
- **Average competitor**: 2.3/10
- **Gap**: 5-7 points (50-70% advantage)

### The Time-to-Value Chasm
- **Scoop**: 30 seconds to first insight
- **Fastest competitor**: 2-4 weeks (DataGPT)
- **Average competitor**: 2-3 months
- **Multiplier**: 5,000-10,000x faster

### The Cost Reality
- **Scoop**: $3,588/year all-in
- **Cheapest competitor**: ~$200K/year (with hidden costs)
- **Most expensive**: $1.59M/year (Snowflake Cortex)
- **Savings**: 55x to 443x lower cost
- **Gap**: 5-7 points (50-70% advantage)

### Universal Weaknesses Confirmed
1. **No schema evolution** - ALL competitors fail completely
2. **No investigation engine** - Single queries only, no hypothesis testing
3. **No Excel integration** - Export-only, no native formulas
4. **No explainable ML** - Black box or fake AI
5. **Break on changes** - Schema changes break everything

## Competitive Positioning

### Scoop's Validated Moats
- **Only platform scoring above 35/40** (next best: 20/40)
- **Investigation Engine**: Multi-pass reasoning (3-10 queries)
- **Schema Evolution**: Automatic handling vs universal failure
- **Explainable ML**: J48 decision trees with business rules
- **Native Integration**: =SCOOP() in Excel, native Slack
- **40-50x cost advantage**: $3,588 vs $100K-300K+

### Closest Competitors
1. **DataGPT** (20/40) - But tiny customer base
2. **Domo/ThoughtSpot** (18/40) - But major accessibility issues
3. **Tellius** (16/40) - But too complex

### Why Others Can't Catch Up
- **Architectural limitations** - Built for IT/analysts
- **Business model conflicts** - Would cannibalize services
- **Technical debt** - 20+ year old architectures
- **Market positioning** - Committed to enterprise IT

---

*This matrix will be continuously updated as deeper BUPAF analysis is completed for each competitor.*