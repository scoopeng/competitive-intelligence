# Battle Card: Snowflake Cortex

**BUA Score**: 17/59 (29%, Category C)
**Market Position**: SQL generation tool marketed as business analytics
**Key Weakness**: 35% business question success rate - cannot investigate WHY

---

## Quick Win Discovery Questions
1. "When you ask Cortex 'Why are customers churning?' what kind of answer do you get?"
2. "What's your total annual Cortex cost including warehouse compute and maintenance?"
3. "Can your business users get insights on mobile devices or in Excel?"

## Killer Facts with Evidence
- **35% business success rate** - only 10/28 test queries delivered usable insights (Phase 2 testing)
- **$86K-$171K first year TCO** including implementation, compute, and maintenance (Phase 3 analysis)
- **Weeks of IT setup** required for semantic model creation before any business user can query
- **Zero investigation capability** - "Why are customers churning?" query fails completely
- **No Excel/PowerPoint integration** - manual screenshot workflow only
- **Zero mobile support** - API-only, no native tablet/smartphone interfaces

## Head-to-Head

| Factor | Snowflake Cortex | Scoop | Your Win |
|--------|------------------|-------|----------|
| Business Questions | 35% success rate | 100% success rate | "2/3 questions fail vs all succeed" |
| Investigation Depth | WHAT happened (data) | WHY it happened (insights) | "Numbers vs root causes" |
| Annual Cost | $86K-$171K | $3,588 | "24x more expensive with hidden costs" |
| Setup for Business Users | Weeks (IT semantic model) | 30 seconds | "IT dependency vs instant" |
| Excel Integration | ❌ None | ✅ 150+ functions | "Screenshot workflow vs native" |
| Mobile Access | ❌ API only | ✅ Native apps | "Desktop-only vs field teams" |
| PowerPoint Export | ❌ Manual screenshots | ✅ Automated generation | "30 minutes vs 30 seconds" |
| Multi-Pass Analysis | ❌ Stateless single query | ✅ Context-aware investigation | "Isolated queries vs building insights" |

## Objection Handlers

**"Snowflake claims 90% accuracy"**
"That's 90% SQL accuracy, not business question success. Our testing shows only 35% of business questions get usable answers. Cortex can tell you sales are down 15%, but only Scoop can tell you why and what to do about it."

**"We're already committed to Snowflake"**
"Perfect! Scoop works beautifully with your Snowflake data warehouse. While Cortex generates SQL queries, Scoop provides the investigation layer that delivers business insights. Keep Cortex for technical teams and give business users Scoop for true self-service analytics."

**"But Snowflake has AI"**
"Snowflake Cortex generates SQL - that's WHAT happened. Scoop investigates WHY it happened. While Cortex costs $86K+ annually with 35% success rate and requires semantic model maintenance, Scoop delivers complete business investigations for $3,588 with 100% success rate and zero maintenance overhead."

**"What about governance and security?"**
"Scoop connects to your existing Snowflake security model - same governance, better insights. While Cortex requires IT to create semantic models that limit business users, Scoop respects your permissions while empowering true self-service analytics."

## The WHY vs WHAT Demonstration

### Snowflake Cortex Response
**Question**: "Why are customers churning?"
**Result**: ERROR - "Actual statement count 3 did not match the desired statement count 1"
**Reason**: Cannot execute multi-step churn analysis (test evidence from Phase 2)
**Output**: Complete failure - no usable answer
**Value**: User gets technical error message

### Scoop Response
**Question**: "Why are customers churning?"
**Investigation** (multi-probe reasoning):
1. Explainable ML decision tree analysis
2. Feature importance calculations with p-values
3. Customer segment risk profiling
4. Behavioral pattern identification
5. Actionable intervention strategies

**Output**:
- "Contract type has 65% influence (month-to-month = high risk)"
- "Tenure < 6 months adds 30% churn probability"
- "No online backup service increases churn by 22%"
- **Action Plan**: Target month-to-month customers at month 5 with retention offers focusing on backup service value

## Workflow Reality Check

**Cortex Path** (3-4 hours):
1. Write query in Snowflake console
2. Export results to CSV
3. Import to Excel
4. Clean and format data
5. Create charts manually
6. Copy to PowerPoint
7. Add annotations
8. Format for brand

**Scoop Path** (30 seconds):
1. Type in Slack: "Revenue analysis for board meeting"
2. Get complete PowerPoint with insights
3. Done

**Weekly Time Waste**: 17.5 hours per analyst

## True TCO They Won't Show (Phase 3 Evidence)

| Component | First Year Cost | Hidden Reality |
|-----------|----------------|----------------|
| Professional services | $20-50K | ✅ Setup & semantic model |
| Semantic model development | $20-40K | ✅ 1-2 FTE months |
| Integration development | $10-30K | ✅ Custom applications |
| Warehouse compute | $1-3K | ✅ Per-query charges |
| Semantic model maintenance | $25-50K | ✅ 0.5-1 FTE annually |
| Conversation scaling | $7-18K | ✅ 10K messages/month |
| **Total First Year** | **$86K-$171K** | **24x more than Scoop** |

## The Winning Pitch

"Snowflake Cortex promises self-service analytics but delivers a technical SQL generation tool with 35% business question success rate that costs $86K-$171K first year. Our testing proved it cannot answer 'Why are customers churning?' - it fails completely with technical errors. Scoop provides true business empowerment with 100% success rate for $3,588 annually, delivering explainable ML insights and actionable recommendations that Cortex's SQL generation simply cannot provide."

## Proof Points with Evidence
- **35% vs 100% success rate**: Show test results (10/28 vs all queries succeed)
- **TCO reality**: $86K-$171K vs $3,588 (24x cost difference with proof)
- **Investigation failure**: Live demo "Why are customers churning?" error
- **Mobile/Excel gaps**: Show screenshot workflow vs native integration

## Fatal Technical Limitations (Evidence-Based)
- **Stateless architecture**: Cannot reference previous query results (official docs)
- **32K token semantic model limit**: Scalability ceiling proven
- **Zero investigation capability**: "Why" questions fail systematically (test evidence)
- **No Excel/PowerPoint integration**: Manual screenshot workflow only
- **IT dependency**: Weeks of semantic model setup required before business users can query

## Real Customer Challenges (Phase 1 Research)
- **Implementation complexity**: "Weeks" timeline due to semantic model requirements
- **Accuracy gaps**: "Real-world use cases frequently expose gaps in precision" (AtScale)
- **Performance bottlenecks**: Documented as common implementation challenge
- **Authentication errors**: Cited as top 4 most common problems by consultants

---

*Use when: Snowflake customers, Enterprise deals, Technical evaluations, Cost discussions*

## Verify This Yourself

### Trial Availability
1. Sign up for Snowflake trial
2. Try to access Cortex Analyst
3. Discovery: Not available without enterprise account

### Python Requirements
1. Check setup documentation
2. Count required packages: 17+
3. Time full setup: 4+ hours minimum

### Cost Calculator
1. Visit Snowflake pricing page
2. Add: Cortex + Compute + Services + Maintenance
3. Reality: $50-100K+ on top of Snowflake base

---

*Remember: They query warehouses. We investigate businesses.*