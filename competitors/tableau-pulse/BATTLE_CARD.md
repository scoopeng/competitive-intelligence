# Battle Card: Tableau Pulse

**BUA Score**: 36/100 (36%, Category C - Weak)
**Parent**: Salesforce
**Key Weakness**: Zero Excel support + Cannot investigate "Why"
**Last Updated**: September 25, 2025

---

## Quick Win Discovery Questions
1. "Are you on Tableau Server or Cloud?" (Pulse only works on Cloud)
2. "Did you see Tableau's warning about hallucinations?"
3. "How much are you paying for view-only users?" ($15/month each)
4. "Can you schedule automated updates?" (No - all manual)
5. "What happens when your schema changes?" (400 errors)

## Top 5 Fatal Flaws
1. **ZERO Excel Formula Support**: No pivot tables, no formulas, requires third-party tools
2. **Cannot Investigate "Why"**: Only "progressive Q&A" - no multi-pass investigation
3. **PowerPoint Requires Rollstack**: Additional $$ for basic export functionality
4. **Time-Series Prison**: Requires daily/weekly data with time dimension
5. **Cloud-Only + Schema Breaks**: Server abandoned, 400 errors on any change

## Head-to-Head

| Factor | Tableau Pulse | Scoop | Your Win |
|--------|---------------|-------|----------|
| Excel Support | ❌ ZERO formulas | ✅ 150+ functions | "Can't even do VLOOKUP" |
| ML Models | ❌ Detection only | ✅ J48, JRip, EM | "Trends vs actual ML" |
| Investigation | ❌ Progressive Q&A | ✅ Multi-pass (3-10) | "Guided tour vs root cause" |
| PowerPoint | ❌ Rollstack required | ✅ Native | "Extra $$ for basics" |
| Data Flexibility | ❌ Time-series only | ✅ Any data | "Can't analyze point-in-time" |

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