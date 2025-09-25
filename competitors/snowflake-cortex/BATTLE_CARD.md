# Battle Card: Snowflake Cortex

**BUPAF Score**: 13/50 (Category D - Marketing Mirage)
**Market Position**: SQL generation for data warehouse
**Key Weakness**: WHY vs WHAT - No investigation capability

---

## Quick Win Discovery Questions
1. "Can Cortex tell you WHY metrics changed, or just WHAT changed?"
2. "What's your total annual Cortex cost including compute?"
3. "Can business users use it without Python setup?"

## Killer Facts
- **$50K-100K+/year** implementation and compute costs (on top of Snowflake)
- **4+ hours setup** with 17 Python packages
- **NOT available** on trial accounts
- **Single SQL only** - no multi-pass investigation
- **No ML analysis** - just aggregations
- **Vendor lock-in** - data never leaves Snowflake

## Head-to-Head

| Factor | Snowflake Cortex | Scoop | Your Win |
|--------|------------------|-------|----------|
| Core Capability | WHAT happened | WHY it happened | "SQL vs Investigation" |
| Annual Cost | $50K-100K+ | $3,588 | "15-30x more expensive" |
| Investigation | ❌ Single query | ✅ 3-10 passes | "One question vs root cause" |
| ML Analysis | ❌ None | ✅ J48, JRip, EM | "Aggregation vs discovery" |
| Setup Time | 4+ hours, Python | 30 seconds | "Developer vs instant" |
| Business Users | ❌ Need technical | ✅ Natural language | "Python or English?" |
| Workflow | Snowflake console | Excel/PowerPoint/Slack | "Their portal or your tools" |
| Schema Changes | ❌ Breaks queries | ✅ Auto-evolution | "Maintenance nightmare" |

## Objection Handlers

**"Snowflake is the industry standard"**
"For data warehousing, absolutely. But Cortex is just SQL generation - it can't investigate WHY metrics changed. You're paying $50-100K+/year for single queries when Scoop delivers multi-pass investigation for $3,588."

**"We're already on Snowflake"**
"Perfect for data storage. But why pay 15-30x more for basic SQL when you could have actual investigation? Cortex can't do root cause analysis, ML discovery, or explain changes - it just queries what you already have."

**"Cortex has AI capabilities"**
"It has LLM-to-SQL translation. That's not investigation. Ask it 'Why did churn increase?' and you get a GROUP BY. Ask Scoop and you get decision trees showing exact customer segments and causes."

## The WHY vs WHAT Demonstration

### Snowflake Cortex Response
**Question**: "Why did revenue drop in Q4?"
**Result**:
```sql
SELECT quarter, SUM(revenue)
FROM sales
GROUP BY quarter
```
**Output**: "Q4: $1.2M (down 23%)"
**Value**: You already knew this

### Scoop Response
**Question**: "Why did revenue drop in Q4?"
**Investigation** (3-10 queries):
1. Identifies top declining segments
2. Discovers product mix changes
3. Finds customer behavior patterns
4. Reveals competitor actions
5. Provides ML decision tree

**Output**:
- "Enterprise segment down 67% due to contract delays"
- "3 key accounts citing feature gap vs competitor X"
- "ML shows: IF deal_size > $100K AND industry = 'Finance' THEN delay_probability = 89%"
- **Action Plan**: Focus on these 5 accounts, address these 2 features

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

## Cost Breakdown They Won't Show

| Component | Annual Cost | Hidden |
|-----------|------------|--------|
| Cortex Implementation | $20-50K | ❌ Not on trials |
| Compute (queries) | $20-40K+ | ✅ Per-query charges |
| Professional services | $10-20K | ✅ Setup & training |
| Semantic model maintenance | 1-2 FTEs | ✅ Ongoing work |
| **Total Reality** | **$50-100K+** | **Plus Snowflake base** |

## The Winning Pitch

"Snowflake Cortex generates SQL queries - that's WHAT happened. Scoop investigates WHY it happened through multi-pass reasoning and ML analysis. While Cortex adds $50-100K+/year in costs and requires Python setup, Scoop costs $3,588 flat and works in 30 seconds. More importantly, Cortex can't tell you why customers are churning, just that they are. Scoop delivers the complete investigation with decision trees showing exact causes and what to do about them."

## Proof Points
- Demo multi-pass investigation vs single SQL
- Show Python setup requirements
- Calculate true TCO with compute costs
- Demonstrate ML insights they can't provide

## Technical Limitations They Hide
- No multi-pass reasoning (architectural limit)
- No ML capabilities (just SQL)
- No schema evolution (queries break)
- No workflow integration (warehouse only)
- Requires semantic model maintenance

## Customer Pain Points
- "We spent 3 months setting up semantic models"
- "Every new question needs IT involvement"
- "Costs spiral with query volume"
- "Can't explain variance, just shows it"

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