# Battle Card: Tableau Pulse

**BUPAF Score**: 11/50 (Category D - Marketing Mirage)  
**Parent**: Salesforce  
**Key Weakness**: Not real AI, just embedding models

---

## Quick Win Discovery Questions
1. "What happens when you add a new column to your data?"
2. "Can Pulse investigate WHY metrics changed?"
3. "Does it work outside of Tableau dashboards?"

## Killer Facts
- **NOT using LLMs** - Their own admission: embedding models only
- **Schema breaks everything** - "Pulse metrics can break" on column changes
- **40x cost explosion** - Tableau at scale requires massive infrastructure
- **No investigation** - Single metrics only, no hypothesis testing

## Head-to-Head

| Factor | Tableau Pulse | Scoop | Your Win |
|--------|---------------|-------|----------|
| Real AI | ❌ Embedding models | ✅ LLM + ML | "Not real AI by their admission" |
| Schema Evolution | ❌ Breaks on changes | ✅ Automatic | "Add a column, everything breaks" |
| Investigation | ❌ Single metrics | ✅ Multi-hypothesis | "Can't answer WHY" |
| Setup Time | Weeks/Months | 30 seconds | "Immediate value" |
| Business Users | ❌ Need Tableau first | ✅ Independent | "Dashboard prison" |

## Workflow Integration Gap

**Tableau Reality**: Screenshot hell for every presentation
- No native Excel formulas - export static CSVs
- PowerPoint requires screenshots, paste, format (2-3 hours)
- No Slack integration - check another dashboard

**Scoop Advantage**: Live data in YOUR tools
- =SCOOP() formulas with automatic refresh
- Board-ready PowerPoint in 30 seconds
- Full analysis without leaving Slack

**Time Impact**: 3+ hours manual work per report for Tableau users

## Objection Handlers

**"Salesforce backs Tableau"**  
"Which is why they're stuck with 20-year-old architecture. Salesforce can't innovate here without breaking their billion-dollar Tableau business."

**"It has AI insights"**  
"They specifically say they're NOT using LLMs because of 'latency and hallucination risks.' It's embedding models from 2018, not AI."

**"Gartner rates them highly"**  
"For dashboards, not AI. Notice Pulse is barely mentioned in analyst reports? It's a feature, not a platform."

## The Winning Pitch
"Tableau Pulse isn't AI - it's embedding models that generate metric summaries. When your data structure changes, Pulse breaks. When you ask WHY something happened, it can't investigate. You need Tableau dashboards first, then Pulse can describe them. That's not analytics - it's expensive narration. Scoop investigates like an analyst, handles schema changes automatically, and works in 30 seconds - not months."

## Proof Points
- Show schema evolution (they fail completely)
- Demo investigation (they can't do it)
- Calculate TCO (40x higher minimum)
- Ask for Pulse-specific references (they don't exist)

## Verify This Yourself

### Data Requirements Limitations
1. Visit: https://interworks.com/blog/2023/12/14/5-things-to-consider-when-using-tableau-pulse/
2. Find: "Single point in time values will not produce a valid metric"
3. Note: Works only with regular data (daily/weekly), not quarterly/yearly

### Pre-aggregated Fields Break
1. Visit: https://interworks.com/blog/2023/12/14/5-things-to-consider-when-using-tableau-pulse/
2. Find: "400: Bad Request error" for calculated fields
3. Confirm: Pre-aggregated measures don't work

### Metric Proliferation Problem
1. Visit: https://www.theinformationlab.nl/en/2024/03/22/tableau-pulse-is-out-here-is-what-you-need-to-know/
2. Search: "What started as one metric can quickly turn into many"
3. Reality: Each filter combination creates new metric

### Permission Control Issues
1. Visit: https://help.tableau.com/current/online/en-us/pulse_intro.htm
2. Find: "Users see all metrics from all published data sources"
3. Problem: No granular control over metric access

### Salesforce Dependency
1. Read: https://medium.com/centric-tech-views/tableau-pulse-transform-your-bi-with-real-time-alerts-and-ai-b5e149a1a90e
2. Find: "reliance on Salesforce connectors"
3. Issue: "limitation of Tableau's AI strategy"

### Limited Analytics Capabilities
1. Visit: https://b-eye.com/blog/tableau-pulse-real-time-personalized-analytics/
2. Find: "Beta version does not support table calculations"
3. Limitation: Can't create advanced metrics

---
*Use when: Enterprise with Tableau investment, Looking for real AI, Frustrated with implementation complexity*