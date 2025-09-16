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

---
*Use when: Enterprise with Tableau investment, Looking for real AI, Frustrated with implementation complexity*