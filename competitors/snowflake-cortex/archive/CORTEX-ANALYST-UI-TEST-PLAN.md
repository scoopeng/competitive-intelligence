# Cortex Analyst UI Test Plan
Based on 73+ CORTEX.COMPLETE Tests

## What We Know from CORTEX.COMPLETE Testing

### Baseline Results (73 queries tested):
- **0% success** with natural language (no table context)
- **65% execution** with explicit table/column names  
- **0% investigation** capability ("why" questions)
- **0% time intelligence** (no period comparisons)
- **0% window functions** (no running totals)
- **50% Scoop pattern match** at best

## What Cortex Analyst UI Adds

### The Semantic Model (YAML):
```yaml
semantic_model:
  tables:
    - name: TELCO_DATA
      dimensions:
        - name: customer_id
          expr: CUSTOMERID  # Maps business term to column
        - name: churn_status
          expr: CHURN
      measures:
        - name: churn_rate
          expr: (SUM(CASE WHEN CHURN THEN 1 ELSE 0 END) * 100.0 / COUNT(*))
```

### Expected Improvements:
✅ Natural language → column mapping
✅ Business terms understood
✅ Predefined measures available
✅ Visual interface vs API calls

### What CANNOT Be Fixed:
❌ Single query limitation (architecture)
❌ No multi-step investigation
❌ No time intelligence
❌ No ML integration
❌ No pattern discovery

## Test Categories for UI

### Category 1: Natural Language Mapping (15 queries)
**Testing:** Does semantic model fix the 0% natural language problem?

```
Test the SAME 15 queries from natural_language_results.json:
- "How many customers do we have?" 
- "What's the average monthly charge?"
- "Why are customers leaving?"
```

**Expected Result:**
- Basic counts/averages: Should work (80%+)
- Investigation queries: Will still fail (0%)

### Category 2: Business Terms (10 queries)
**Testing:** Can it map business language to database columns?

```
New queries using business terms from semantic model:
- "Show me customer count" (uses measure)
- "What's the churn rate?" (uses calculated measure)
- "Filter by contract type" (uses dimension alias)
```

**Expected Result:**
- Should work if terms match semantic model exactly
- Fails if user uses synonyms not in YAML

### Category 3: Time Intelligence (15 queries)
**Testing:** Does UI enable any time capabilities?

```
Using OPENOPPORTUNITIES with dates:
- "Compare this month to last month"
- "Show running total over time"
- "What's the trend?"
```

**Expected Result:**
- Will fail - UI cannot fix architectural limitation
- Critical gap for business users

### Category 4: Complex Patterns (20 queries)
**Testing:** Scoop Query JSON capabilities

```
Same 20 patterns from comprehensive_pattern_results.json:
- Compound filters (AND/OR)
- Calculated fields
- Window functions
- Subqueries
```

**Expected Result:**
- Same as COMPLETE: 50-60% success
- Window functions still impossible

### Category 5: Investigation (10 queries)
**Testing:** Can UI enable "why" analysis?

```
Critical business questions:
- "Why did sales drop?"
- "What drives customer success?"
- "Find patterns in the data"
```

**Expected Result:**
- 0% - Cannot do multi-step reasoning
- Cannot investigate causation

## Step-by-Step Testing Protocol

### Setup Phase:
1. Configure semantic model in Streamlit app
2. Connect to SCOOP_BENCHMARK database
3. Point to TELCO_DATA and OPENOPPORTUNITIES tables

### Test Execution:

#### Round 1: Natural Language
- Run all 15 natural language queries through UI
- Document which now work with semantic model
- Compare to 0% baseline

#### Round 2: Time Intelligence  
- Switch to OPENOPPORTUNITIES table
- Run 15 time-based queries
- Document failures (expected 0% success)

#### Round 3: Complex Patterns
- Run 20 Scoop patterns
- Compare to COMPLETE baseline (65% execution)
- Note if UI helps or hinders

#### Round 4: Investigation
- Try 10 "why" questions
- Document that these still fail
- Critical business gap

### Documentation:
For each query, capture:
1. Query text
2. Did it generate SQL?
3. Did SQL execute?
4. Did it answer the business question?
5. Time taken
6. User experience notes

## Critical Questions to Answer

### 1. Natural Language Improvement
- **Baseline:** 0% without context
- **With UI:** What % improves?
- **Remaining gap:** What still fails?

### 2. Setup Complexity
- Time to configure semantic model?
- Technical expertise required?
- Maintenance burden?

### 3. Business User Independence
- Can they work without IT support?
- What breaks when they go off-script?
- Error messages helpful?

### 4. Performance
- Response time vs COMPLETE API?
- Timeout issues?
- Concurrent user support?

## Success Criteria

For Cortex Analyst to be viable:

### Minimum Bar:
- [ ] 80%+ success on natural language with semantic model
- [ ] No SQL knowledge required for basic queries
- [ ] Setup in < 1 hour
- [ ] Business users can work independently

### Reality Check (based on COMPLETE testing):
- Natural language: May improve to 60-70%
- Complex queries: Still capped at 50%
- Investigation: Still 0%
- Time intelligence: Still 0%

## Expected Findings

Based on CORTEX.COMPLETE limitations:

### Will Improve:
✅ Natural language understanding (with exact term matches)
✅ Basic aggregations more accessible
✅ Column name mapping

### Won't Improve:
❌ "Why" questions (investigation)
❌ Period comparisons
❌ Running totals
❌ Trend analysis
❌ Pattern discovery
❌ Multi-step reasoning

## The Bottom Line

**Cortex Analyst UI is lipstick on a pig:**
- Makes basic SQL generation prettier
- Doesn't fix fundamental limitations
- Still can't do what Scoop does natively

**Business Impact:**
- Users still need SQL for anything complex
- IT still required for semantic model
- Still can't answer critical business questions

## Test Data Summary

**Total queries to test through UI:** 70
- 15 Natural language (repeat from COMPLETE)
- 10 Business terms (new)
- 15 Time intelligence (new with dates)
- 20 Complex patterns (repeat from COMPLETE)
- 10 Investigation (repeat from COMPLETE)

**Comparison baseline:** 88 total queries tested
- 73 on CORTEX.COMPLETE
- 15 new time intelligence tests
- All documented with success rates

This gives us comprehensive evidence of:
1. What the semantic model actually fixes
2. What architectural limits persist
3. Real business impact of limitations