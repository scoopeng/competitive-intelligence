# Battle Card: Snowflake Cortex

**BUPAF Score**: 13/50 (Category D - Marketing Mirage)  
**Market Position**: Text-to-SQL with vendor lock-in  
**Key Weakness**: 6-12 month migration, $1.6M annual cost

---

## Quick Win Discovery Questions
1. "What's your total Snowflake compute cost including Cortex?"
2. "How long would migration take from your current warehouse?"
3. "Can Cortex investigate WHY metrics changed?"

## Killer Facts
- **$1.6M annual cost** for 200 users (compute + queries + maintenance)
- **6-12 month migration** to Snowflake required first
- **Complete vendor lock-in** - data must live in Snowflake
- **No investigation** - Single SQL queries only
- **No ML capabilities** despite marketing claims
- **Per-query charging** creates budget uncertainty

## Head-to-Head

| Factor | Snowflake Cortex | Scoop | Your Win |
|--------|------------------|-------|----------|
| Total Cost | $1.6M/year | $3,588/year | "457x more expensive" |
| Migration | 6-12 months | 30 seconds | "Year vs instant" |
| Investigation | ❌ SQL only | ✅ Multi-hypothesis | "Can't find root causes" |
| ML Capabilities | ❌ None | ✅ ML_GROUP/ML_PERIOD | "SQL isn't ML" |
| Vendor Lock | ❌ Complete | ✅ Any data source | "Trapped in Snowflake" |
| Schema Evolution | ❌ Breaks | ✅ Automatic | "2-4 weeks per change" |

## Workflow Integration Gap

**Snowflake Reality**: Another portal with SQL results
- No Excel integration - export CSVs manually
- No PowerPoint capability - copy/paste screenshots
- No native Slack - build custom bots (2-4 weeks)

**Scoop Advantage**: Work in YOUR tools
- =SCOOP() Excel formulas with live refresh
- PowerPoint generation in 30 seconds
- Native Slack integration immediately

**Time Impact**: 3+ hours manual work per report for Snowflake users

## Objection Handlers

**"We're already on Snowflake"**  
"That's why Cortex seems appealing, but you'll pay $1.6M annually for text-to-SQL that can't investigate problems. Scoop works with your Snowflake data at $3,588/year and actually finds root causes."

**"Snowflake is enterprise-grade"**  
"For data warehousing, yes. For analytics, Cortex is just SQL queries with massive costs. It can't explain why metrics changed or adapt when you add columns."

**"It's integrated with our data"**  
"But not with your tools. No Excel formulas, no PowerPoint generation, no Slack. You'll spend 3+ hours per report on manual work."

## The Winning Pitch
"Snowflake Cortex costs $1.6M annually and requires complete data migration to Snowflake - a 6-12 month project. After that investment, you get single SQL queries that can't investigate problems, break on schema changes, and trap your data in their ecosystem. Scoop connects to your existing Snowflake in 30 seconds, costs $3,588/year, and actually investigates WHY metrics change - delivering answers in Excel, PowerPoint, and Slack where you work."

## Proof Points
- Calculate their actual Snowflake costs (shocking)
- Show schema evolution (Cortex fails)
- Demo investigation vs single query
- Demonstrate =SCOOP() formulas in Excel

## Red Flags
- No customer success stories
- Hidden compute costs explode budgets
- Requires Snowflake Enterprise edition
- No semantic layer without additional tools
- Forces complete architectural change

## Verify This Yourself

### Vendor Lock-in Reality
1. Visit: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst
2. Find: "Data stays within Snowflake's governance boundary"
3. Confirm: "no data, including metadata or prompts, leaves Snowflake"

### Token-Based Pricing Structure
1. Visit: https://yukidata.com/blog/snowflake-cortex-pricing/
2. Search: "Token costs vary based on the specific Cortex model"
3. Reality: "More documents = higher indexing costs"

### Migration Warning from Snowflake
1. Visit: https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql
2. Find: "Snowflake strongly discourages the use of Azure OpenAI models"
3. Warning: "Snowflake anticipates deprecating support"

### Cost Management Issues
1. Visit: https://www.linkedin.com/pulse/understanding-managing-costs-snowflake-cortex-akash-pandey-ox9pe
2. Quote: "Snowflake Cortex pricing can easily get out of hand"
3. Problem: Unpredictable usage-based costs

### Compute Cost Reality
1. Visit: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-costs
2. Find: "Charged per gigabyte-month of indexed data"
3. Calculate: 500GB logs = massive indexing costs

### Optimization Requirements
1. Visit: https://atlan.com/know/snowflake/snowflake-cortex-explained/
2. Find: "Stay on top with strong cost optimization strategy"
3. Reality: Requires dedicated cost management

---

*Use when: Snowflake customers, Cost-conscious buyers, Multi-source data needs, Want actual AI not SQL*