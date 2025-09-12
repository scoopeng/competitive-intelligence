# BUPAF Quick Comparison Matrix

**Last Updated**: January 2025  
**Status**: Initial scoring based on existing research - to be enhanced with targeted analysis  

## Overall BUPAF Scores (40 points maximum)

| Competitor | Independence | Analytical Depth | Workflow | Communication | **TOTAL** | Category |
|------------|-------------|-----------------|----------|---------------|-----------|----------|
| **Scoop** | 9/10 | 9/10 | 9/10 | 9/10 | **36/40** | A |
| DataGPT | 6/10 | 5/10 | 3/10 | 6/10 | **20/40** | C |
| Domo | 5/10 | 4/10 | 4/10 | 5/10 | **18/40** | C |
| ThoughtSpot | 4/10 | 7/10 | 2/10 | 5/10 | **18/40** | C |
| Tellius | 3/10 | 7/10 | 2/10 | 4/10 | **16/40** | C |
| Zenlytic | 3/10 | 3/10 | 2/10 | 7/10 | **15/40** | C |
| Power BI Copilot | 3/10 | 3/10 | 3/10 | 4/10 | **13/40** | D |
| Snowflake Cortex | 2/10 | 4/10 | 3/10 | 3/10 | **12/40** | D |
| Sisense | 2/10 | 2/10 | 2/10 | 4/10 | **10/40** | D |
| Tableau Pulse | 2/10 | 2/10 | 1/10 | 4/10 | **9/40** | D |
| Qlik | 2/10 | 2/10 | 2/10 | 3/10 | **9/40** | D |
| DataChat | 1/10 | 1/10 | 1/10 | 2/10 | **5/40** | D |

## Detailed Breakdown

### Dimension 1: Independence (Can business users work alone?)

| Competitor | Score | Evidence | Key Limitation |
|------------|-------|----------|----------------|
| **Scoop** | 9/10 | Email CSV, natural language, no training | Some complex data needs IT |
| DataGPT | 6/10 | Claims 85% adoption | Needs clean data model |
| Domo | 5/10 | Some self-service | Dashboard-dependent |
| ThoughtSpot | 4/10 | "Search-driven" | Requires data modeling |
| Others | 1-3/10 | IT dependency | Complete IT control |

### Dimension 2: Analytical Depth (What questions can they answer?)

| Competitor | Score | Can Do | Cannot Do |
|------------|-------|--------|-----------|
| **Scoop** | 9/10 | Investigation, ML, prediction | Some optimization |
| ThoughtSpot | 7/10 | ML, clustering | No investigation |
| Tellius | 7/10 | Root cause | Complex for users |
| Zenlytic | 6/10 | Some ML | YAML required |
| DataGPT | 5/10 | Fast analysis | No deep investigation |
| Others | 1-4/10 | Basic metrics | No "why" questions |

### Dimension 3: Workflow Integration (How naturally does it fit?)

| Competitor | Data Mgmt | Excel | PowerPoint | Collaboration | Automation |
|------------|-----------|-------|------------|---------------|------------|
| **Scoop** | ✅ Schema evolution | ✅ Formulas | ✅ Generate | ✅ Slack native | ✅ Full |
| Domo | ❌ IT required | ⚠️ Export | ❌ Manual | ⚠️ Portal | ⚠️ Basic |
| Tableau | ❌ No evolution | ❌ None | ❌ Manual | ⚠️ Alerts | ❌ Rigid |
| PowerBI | ❌ IT required | ⚠️ Export | ❌ Manual | ⚠️ Portal | ⚠️ Basic |
| Others | ❌ IT required | ❌ None | ❌ Manual | ❌ None | ❌ None |

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

### Category C: Analyst Workbenches (15-20 points)
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

## Key Insights

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