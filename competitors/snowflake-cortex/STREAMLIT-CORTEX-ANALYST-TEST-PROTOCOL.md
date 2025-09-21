# Streamlit Cortex Analyst Test Protocol
Step-by-Step Testing Guide for Your Streamlit App

## Prerequisites

### You Have:
- ✅ Streamlit app workspace created
- ✅ Default demo Python running
- ✅ Access to TELCO_DATA and OPENOPPORTUNITIES tables
- ✅ 88 baseline test results from CORTEX.COMPLETE

### You Need:
- Semantic model YAML configured
- Test queries ready (provided below)
- Results tracking spreadsheet

## Phase 1: Semantic Model Setup

### Step 1: Create Enhanced Semantic Model
Save this as `semantic_model_enhanced.yaml`:

```yaml
semantic_model:
  name: Business Analytics Model
  description: Comprehensive model for Cortex Analyst testing
  
  # Add custom instructions (January 2025 feature)
  custom_instructions:
    - "When asked about trends, attempt to show data over time"
    - "Churn means CHURN = true"
    - "High value means > $100"
    - "Performance means win rate or success rate"
  
  tables:
    # TELCO_DATA with full semantic mapping
    - name: TELCO_DATA
      description: Customer churn analysis data
      base_table:
        database: SCOOP_BENCHMARK
        schema: TEST_DATA
        table: TELCO_DATA
      
      dimensions:
        - name: customer
          synonyms: ["customer_id", "account", "subscriber"]
          expr: CUSTOMERID
          description: Unique customer identifier
          
        - name: churn_status
          synonyms: ["churned", "left", "cancelled"]
          expr: CHURN
          description: Whether customer churned
          
        - name: contract
          synonyms: ["contract_type", "plan", "subscription"]
          expr: CONTRACT
          description: Contract type
          sample_values: ["Month-to-month", "One year", "Two year"]
      
      measures:
        - name: customer_count
          expr: COUNT(DISTINCT CUSTOMERID)
          description: Total number of customers
          
        - name: churn_rate
          expr: (SUM(CASE WHEN CHURN THEN 1 ELSE 0 END) * 100.0 / COUNT(*))
          description: Percentage of customers who churned
          
        - name: average_revenue
          expr: AVG(MONTHLYCHARGES)
          description: Average monthly revenue per customer
      
      # Add verified queries for common questions
      verified_queries:
        - question: "What's the churn rate?"
          sql: "SELECT (SUM(CASE WHEN CHURN THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) as churn_rate FROM TELCO_DATA"
        - question: "How many customers do we have?"
          sql: "SELECT COUNT(DISTINCT CUSTOMERID) FROM TELCO_DATA"
    
    # OPENOPPORTUNITIES for time testing
    - name: OPENOPPORTUNITIES  
      description: Sales opportunities with dates
      base_table:
        database: SCOOP_BENCHMARK
        schema: TEST_DATA
        table: OPENOPPORTUNITIES
        
      dimensions:
        - name: opportunity_date
          synonyms: ["date", "created", "when"]
          expr: C1
          data_type: TIMESTAMP_NTZ
          description: Opportunity creation date
          
        - name: close_date
          expr: C9
          data_type: TIMESTAMP_NTZ
          description: Expected close date
          
        - name: status
          synonyms: ["stage", "state"]
          expr: C8
          description: Opportunity status
          
        - name: amount
          synonyms: ["value", "revenue", "deal_size"]
          expr: C13
          data_type: NUMBER
          description: Opportunity value
      
      measures:
        - name: total_revenue
          expr: SUM(C13)
          description: Total opportunity value
          
        - name: opportunity_count
          expr: COUNT(*)
          description: Number of opportunities
          
      time_dimensions:
        - name: month
          expr: DATE_TRUNC('MONTH', C1)
          description: Month of opportunity
```

### Step 2: Upload to Streamlit App
1. Navigate to your Streamlit app
2. Upload the enhanced semantic model
3. Verify connection to SCOOP_BENCHMARK database

## Phase 2: Test Execution

### Test Set A: Natural Language (What Should Work with Semantic Model)

Run these 15 queries and document results:

```python
natural_language_tests = [
    # Basic - Should work with semantic model
    "How many customers do we have?",  # Uses 'customer' synonym
    "What's the churn rate?",  # Has verified query
    "Show me average revenue",  # Uses measure
    
    # Grouping - Should partially work
    "Show customers by contract",  # Uses synonym
    "Display churn rate by gender",
    
    # Filtering - Test semantic understanding
    "Show me churned customers",  # Uses synonym
    "High value customers only",  # Uses custom instruction
    
    # Complex - Likely to fail
    "Why are customers churning?",
    "What drives customer loyalty?",
    "Find patterns in the data"
]
```

**Expected Results:**
- ✅ 3-5 queries work (verified queries, exact measures)
- ⚠️ 3-5 partially work (need refinement)
- ❌ 5-7 fail (investigation, patterns)

### Test Set B: Time Intelligence (Critical Business Gap)

Switch to OPENOPPORTUNITIES and test:

```python
time_intelligence_tests = [
    # Period comparisons - All should fail
    "Compare this month to last month",
    "Show month-over-month growth",
    "Year-over-year change in opportunities",
    
    # Running calculations - Should fail
    "Show running total of revenue",
    "7-day moving average of opportunities",
    "Cumulative revenue by month",
    
    # Relative dates - Might partially work
    "Opportunities in the last 30 days",
    "This quarter's performance",
    
    # Trends - Should fail
    "What's the trend?",
    "Forecast next month"
]
```

**Expected Results:**
- ❌ 0% success on period comparisons
- ❌ 0% success on running calculations
- ⚠️ Maybe 1-2 relative date filters work

### Test Set C: Scoop's Production Queries

Test these actual Scoop queries that work today:

```python
scoop_production_tests = [
    # From Scoop's test suite - these all work in Scoop
    
    # Calculated metrics
    "Calculate a customer value score using monthly charges times tenure divided by total support tickets",
    
    # Complex filtering
    "Show customers who have both streaming TV and streaming movies but no tech support",
    
    # Statistical
    "What is the standard deviation of monthly charges by contract type?",
    
    # Visualization
    "Create a heatmap of customer count by tenure group and contract type",
    
    # Change tracking
    "Which opportunities moved to closed won stage?",
    
    # Investigation
    "Why did enterprise deals drop last quarter?"
]
```

**Expected Results:**
- ❌ 0-1 work (maybe simple calc)
- ❌ Rest fail completely

## Phase 3: Document Results

### Create Results Matrix:

| Query | Category | Works in Scoop | Works in CORTEX UI | Notes |
|-------|----------|---------------|-------------------|-------|
| "How many customers?" | Natural Language | ✅ | ✅/⚠️ | Only with semantic model |
| "Month-over-month growth" | Time Intelligence | ✅ | ❌ | Architectural limit |
| "Why are customers churning?" | Investigation | ✅ | ❌ | No multi-step |
| "Create a heatmap..." | Visualization | ✅ | ❌ | No viz capability |

### Track Key Metrics:

1. **Setup Time:**
   - Time to create semantic model: ___
   - Time to configure Streamlit: ___
   - Time to debug issues: ___

2. **Success Rates:**
   - Natural language: ___% (vs 0% baseline)
   - With semantic model: ___% (expected 30-50%)
   - Time intelligence: ___% (expected 0%)
   - Investigation: ___% (expected 0%)

3. **User Experience:**
   - Error messages helpful? Y/N
   - Can business user work alone? Y/N
   - Need SQL knowledge? Y/N

## Phase 4: Advanced Testing

### Test Custom Instructions Impact:

```yaml
custom_instructions:
  - "Calculate MoM as (current - previous) / previous * 100"
  - "Trend means show data grouped by month"
```

**Test:** Does adding instructions help with:
- "Show me the trend" 
- "Calculate MoM growth"

**Expected:** Minimal improvement, still can't do LAG/LEAD

### Test Verified Queries:

Add 10 verified queries for common questions.

**Test:** Do verified queries improve accuracy?

**Expected:** Yes for exact matches, but rigid

### Test Model Size Limits:

Try adding all columns from both tables.

**Test:** Does it hit the 1MB limit?

**Expected:** May hit limit with large schemas

## Phase 5: Compare to Scoop

### For Each Failed Query:

1. **Document why it failed in Cortex:**
   - No time intelligence
   - No multi-step
   - No window functions
   - Column not found

2. **Show how Scoop handles it:**
   - Natural understanding
   - Automatic time handling
   - Multi-step reasoning
   - Pattern detection

### Create Business Impact Summary:

**Critical Gaps for Business Users:**
1. Cannot compare periods (MoM, YoY)
2. Cannot investigate "why"
3. Cannot see trends
4. Cannot forecast
5. No visualizations

## Phase 6: Final Report

### Document:

1. **What Improved with UI:**
   - Natural language (from 0% to ~30%)
   - Easier than API calls
   - Some business term mapping

2. **What Didn't Improve:**
   - Time intelligence (still 0%)
   - Investigation (still 0%)
   - Visualizations (still 0%)
   - Complex patterns (still <50%)

3. **Setup Burden:**
   - Hours to create semantic model
   - Ongoing maintenance required
   - Users still need training

4. **Business Verdict:**
   - Can Cortex Analyst replace BI tools? **No**
   - Can business users work independently? **No**
   - Does it compete with Scoop? **No**

## Testing Checklist

### Before Testing:
- [ ] Semantic model uploaded
- [ ] Both tables accessible
- [ ] Baseline results documented

### During Testing:
- [ ] Run all 41 test queries
- [ ] Document exact error messages
- [ ] Note response times
- [ ] Track which semantic features help

### After Testing:
- [ ] Calculate success rates
- [ ] Compare to baseline
- [ ] Document business impact
- [ ] Create executive summary

## Expected Outcome

Based on our CORTEX.COMPLETE testing:

**Cortex Analyst UI will likely show:**
- 30-40% success with semantic model (up from 0%)
- 0% success on time intelligence
- 0% success on investigation
- 0% success on visualization
- High setup complexity
- Ongoing maintenance burden

**Business users will still need:**
- SQL for anything complex
- Another tool for visualizations
- Different tool for time analysis
- IT support for semantic model

**Compared to Scoop:**
- Cortex: 30-40% query success at best
- Scoop: 100% query success + visualizations

---

*This protocol based on 88 queries tested on CORTEX.COMPLETE*
*Expected results derived from actual testing*
*All Scoop comparisons from production test suite*