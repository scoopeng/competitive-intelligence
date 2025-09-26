# QUERY PATTERN COMPARISON: SCOOP VS SNOWFLAKE CORTEX

## The Fundamental Difference

**Scoop**: Query → Query JSON Object → Multi-Step Plan → SQL → Result
**Snowflake**: Query → SQL → Result

This architectural difference determines what's possible.

---

## CRITICAL PATTERN 1: Subqueries for Multi-Step Analysis

### Business Question: "Show me all deals from the top 5 sales reps by win rate"

This requires:
1. Calculate win rate for each rep (won deals / total deals)
2. Identify the top 5 reps by this calculated metric
3. Show all deals from those reps

### Scoop's Solution (Query JSON with SubqueryFilter):
```json
{
  "queryType": "dataset",
  "attributes": [
    {"columnName": "DealName", "label": "Deal"},
    {"columnName": "SalesRep", "label": "Rep"},
    {"columnName": "Amount", "label": "Value"},
    {"columnName": "Stage", "label": "Stage"}
  ],
  "queryFilter": {
    "type": "SUBQUERY",
    "attributeName": "SalesRep",
    "operator": "IN",
    "subquery": {
      "queryType": "dataset",
      "attributes": [{"columnName": "SalesRep", "label": "Rep"}],
      "metrics": [
        {
          "columnName": "DealID",
          "label": "Won",
          "aggRule": "COUNT",
          "filter": {"attributeName": "Stage", "operator": "=", "values": ["Closed Won"]}
        },
        {
          "columnName": "DealID",
          "label": "Total",
          "aggRule": "COUNT"
        }
      ],
      "formulas": [{
        "expression": "'Won' / 'Total'",
        "label": "Win Rate",
        "format": "#.##%"
      }],
      "sort": {"columnName": "Win Rate", "order": "DESC"},
      "limit": 5
    }
  }
}
```

**Result**: Shows individual deal records (not aggregated) from only the top 5 performing reps

### Snowflake's Attempt:
```sql
-- What it tries to generate (with errors):
SELECT * FROM deals WHERE SalesRep IN (
  SELECT SalesRep, COUNT(CASE WHEN Stage = 'Closed Won' THEN 1 END) / COUNT(*) as win_rate
  FROM deals
  GROUP BY SalesRep
  ORDER BY win_rate DESC
  LIMIT 5
)
-- ERROR: Subquery returns multiple columns
```

**What Actually Happens**: 
- Either SQL syntax errors
- Or returns ALL deals (ignores the "top 5" requirement)
- Or aggregates when it should show details

---

## CRITICAL PATTERN 2: Nested Subqueries for Hierarchical Analysis

### Business Question: "Show opportunities from the top 3 reps in the top 2 regions"

This requires:
1. Find the top 2 regions by revenue
2. Within those regions, find the top 3 reps
3. Show all opportunities from those reps

### Scoop's Nested SubqueryFilter:
```json
{
  "queryFilter": {
    "type": "SUBQUERY",
    "attributeName": "SalesRep",
    "operator": "IN",
    "subquery": {
      "attributes": [{"columnName": "SalesRep"}],
      "metrics": [{"columnName": "Amount", "aggRule": "SUM"}],
      "queryFilter": {
        "type": "SUBQUERY",
        "attributeName": "Region",
        "operator": "IN",
        "subquery": {
          "attributes": [{"columnName": "Region"}],
          "metrics": [{"columnName": "Amount", "aggRule": "SUM"}],
          "sort": {"columnName": "Amount", "order": "DESC"},
          "limit": 2
        }
      },
      "sort": {"columnName": "Amount", "order": "DESC"},
      "limit": 3
    }
  }
}
```

### Snowflake:
**Cannot conceptualize or generate this pattern at all**

---

## CRITICAL PATTERN 3: Formula-Based Filtering

### Business Question: "Show only accounts where customer health score > 500"

Where health score = (Monthly Charges × Tenure) / Support Tickets

### Scoop's Formula with Filter:
```json
{
  "formulas": [{
    "expression": "('MonthlyCharges' * 'Tenure') / IF('SupportTickets' = 0, 1, 'SupportTickets')",
    "label": "Health Score",
    "format": "#,##0",
    "filter": "(('MonthlyCharges' * 'Tenure') / IF('SupportTickets' = 0, 1, 'SupportTickets')) > 500"
  }]
}
```

### Snowflake:
**Cannot filter on calculated metrics within the same query**

---

## PATTERN 4: The "Find and Measure" Pattern

### Business Question: "Find customers who churned last month, then analyze their service usage"

This is a two-phase analysis:
1. Identify a cohort (churned customers)
2. Analyze that cohort's characteristics

### Scoop:
```json
{
  "queryFilter": {
    "type": "SUBQUERY",
    "attributeName": "CustomerID",
    "operator": "IN",
    "subquery": {
      "attributes": [{"columnName": "CustomerID"}],
      "queryFilter": {
        "operator": "AND",
        "filters": [
          {"attributeName": "Churn", "operator": "=", "values": ["Yes"]},
          {"attributeName": "ChurnDate", "operator": "BETWEEN", "values": ["2024-01-01", "2024-01-31"]}
        ]
      }
    }
  },
  "attributes": [
    {"columnName": "InternetService", "label": "Internet"},
    {"columnName": "Contract", "label": "Contract Type"}
  ],
  "metrics": [
    {"columnName": "CustomerID", "aggRule": "COUNT", "label": "Customers"},
    {"columnName": "MonthlyCharges", "aggRule": "AVG", "label": "Avg Charges"},
    {"columnName": "Tenure", "aggRule": "AVG", "label": "Avg Tenure"}
  ]
}
```

### Snowflake:
Would require manual two-step process:
1. First query to find churned customers
2. Second query to analyze them
**Cannot do this in one operation**

---

## PATTERN 5: Time Intelligence Failures (From Real Tests)

### Business Question: "Show month-over-month revenue growth"

### What Scoop Does:
```json
{
  "queryType": "timeseries",
  "period": "Monthly",
  "metrics": [
    {
      "columnName": "Revenue",
      "label": "Current",
      "byDate": "CloseDate"
    },
    {
      "columnName": "Revenue",
      "label": "Previous",
      "byDate": "CloseDate",
      "shiftPeriod": "Monthly",
      "numPeriodsShifted": -1,
      "display": "hidden"
    }
  ],
  "formulas": [{
    "expression": "('Current' - 'Previous') / 'Previous'",
    "label": "MoM Growth",
    "format": "#.##%"
  }]
}
```

### What Snowflake Generated (Real Test):
```sql
SELECT 
    EXTRACT(MONTH FROM TO_DATE(TENURE, 'YYYY-MM')) AS month,
    SUM(MONTHLYCHARGES) AS revenue,
    LAG(SUM(MONTHLYCHARGES), 1, 0) OVER (ORDER BY EXTRACT(MONTH FROM TO_DATE(TENURE, 'YYYY-MM'))) AS prev_month_revenue,
    (SUM(MONTHLYCHARGES) - LAG(SUM(MONTHLYCHARGES), 1, 0) OVER (ORDER BY EXTRACT(MONTH FROM TO_DATE(TENURE, 'YYYY-MM')))) / 
    LAG(SUM(MONTHLYCHARGES), 1, 0) OVER (ORDER BY EXTRACT(MONTH FROM TO_DATE(TENURE, 'YYYY-MM'))) AS growth
FROM 
    TELCO_DATA
GROUP BY 
    EXTRACT(MONTH FROM TO_DATE(TENURE, 'YYYY-MM'))
ORDER BY 
    month
```
```
```

**Error**: "syntax error line 13 at position 0 unexpected '``'"
**Problem**: Model adds markdown backticks to SQL, plus TENURE is not a date field

---

## PATTERN 6: Investigation Queries

### Business Question: "Why are customers churning?"

### What Users Expect:
- Multi-factor analysis
- Correlation identification
- Statistical significance
- Actionable insights

### What Scoop Does (ML_RELATIONSHIP classification):
1. Identifies this as an investigation query
2. Launches decision tree analysis
3. Returns factors like:
   - "Contract type = Month-to-month increases churn by 45%"
   - "No online security increases churn by 30%"
   - "Tenure < 12 months increases churn by 25%"

### What Snowflake Does (Real Test):
```sql
SELECT GENDER, SENIORCITIZEN, PARTNER, DEPENDENTS, TENURE, 
       PHONESERVICE, MULTIPLELINES, INTERNETSERVICE, ONLINESECURITY, 
       ONLINEBACKUP, DEVICEPROTECTION, TECHSUPPORT, STREAMINGTV, 
       STREAMINGMOVIES, CONTRACT, PAPERLESSBILLING, PAYMENTMETHOD, 
       MONTHLYCHARGES, TOTALCHARGES 
FROM TELCO_DATA 
WHERE CHURN = 'Yes'
```

**Result**: Just returns raw data of churned customers, no analysis of "why"

---

## THE PATTERN HIERARCHY

### Level 1: Basic SQL (Both Can Do)
- Simple aggregations
- Basic filtering
- Simple GROUP BY

### Level 2: Advanced SQL (Scoop Only)
- Window functions (LAG, LEAD, OVER)
- Statistical functions (STDEV, CORR)
- Complex JOINs

### Level 3: Subquery Patterns (Scoop Only)
- Top N by calculated metric
- Find cohort, then analyze
- Hierarchical filtering

### Level 4: Formula-Based Logic (Scoop Only)
- Filter on calculated values
- Conditional aggregations
- Complex business metrics

### Level 5: Multi-Pass Analysis (Scoop Only)
- Classification before execution
- ML integration
- Investigation capabilities

---

## BUSINESS IMPACT

### Real Questions Snowflake Cannot Answer:

1. **"Show me customers from our top 5 markets"**
   - Requires: Subquery to identify top markets
   - Snowflake: ❌ Cannot chain operations

2. **"Find deals where win rate exceeds team average"**
   - Requires: Calculate team average, then filter
   - Snowflake: ❌ Cannot filter on calculations

3. **"What's driving churn in our enterprise segment?"**
   - Requires: ML analysis, decision trees
   - Snowflake: ❌ Returns raw data only

4. **"Show quarterly growth trends with running totals"**
   - Requires: Window functions
   - Snowflake: ❌ Syntax errors with LAG/OVER

5. **"Identify outliers in customer behavior"**
   - Requires: Statistical functions
   - Snowflake: ❌ Missing STDEV, percentiles

### The Verdict

Snowflake Cortex Analyst can only handle queries that could be written as simple, single-table SQL statements. Any query requiring:
- Multi-step logic
- Calculated filtering  
- Window functions
- Statistical analysis
- Investigation

...will fail.

This is not a model limitation—it's an architectural constraint. Without Query JSON Object's ability to express complex analytical patterns, Snowflake is limited to basic SQL generation, making it unsuitable for real business intelligence.