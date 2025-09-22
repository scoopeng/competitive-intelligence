# Detailed Test Analysis: Business Correctness Issues

## Overview
This document provides detailed analysis of specific test failures and business correctness issues discovered during Cortex Analyst testing.

## The Context Stripping Problem (25% of Queries)

### Example 1: Formula Filter Missing Values
**Query**: "Show contract types where churn rate exceeds 30%"
**Cortex SQL**:
```sql
SELECT CONTRACT
FROM TELCO_DATA
GROUP BY CONTRACT
HAVING (COUNT(CASE WHEN CHURN = 'Yes' THEN 1 END) * 100.0 / COUNT(*)) > 30;
```
**Result**: Returns only "Month-to-month"
**Problem**: Doesn't include the actual 60% churn rate
**Business Impact**: Manager can't prioritize - is it 31% or 90%?

### Example 2: ARPU Filter Missing Values  
**Query**: "Payment methods where average revenue per user is above 75"
**Cortex SQL**:
```sql
SELECT PAYMENTMETHOD
FROM TELCO_DATA
GROUP BY PAYMENTMETHOD
HAVING AVG(TOTALCHARGES) > 75;
```
**Result**: Returns payment method names only
**Problem**: No ARPU values included
**Business Impact**: Can't compare which payment method has highest ARPU

## Time Intelligence Failures (67% Failure Rate)

### Example 1: Month-over-Month Change
**Query**: "Month-over-month change in customer count"
**Cortex Attempt**: Complex window function with DATE_TRUNC
**Result**: SQL execution error - no proper date column
**Scoop Solution**: SCOOP_DKEY handles temporal perspectives natively

### Example 2: Moving Averages
**Query**: "3-month moving average of monthly charges"
**Cortex Result**: Calculates per-row moving average (nonsensical)
**Problem**: Doesn't understand time-series aggregation
**Scoop Solution**: Native time-series with period-aware aggregation

## ML Query Failures

### Example: Causal Analysis
**Query**: "Why are customers churning?"
**Cortex Attempt**:
```sql
-- Tried to execute 3 separate queries
SELECT CHURN, COUNT(*) as customer_count...
SELECT 'Tenure Analysis' as analysis_type...
SELECT 'Contract Analysis' as analysis_type...
```
**Error**: "Actual statement count 3 did not match the desired statement count 1"
**Problem**: Cannot perform multi-step analysis
**Scoop Solution**: Multi-probe reasoning with dependency extraction

## Investigation Depth Limitation

### Cortex: Single Query Only
- One SQL statement per question
- No ability to build on previous results
- Cannot perform exploratory analysis

### Scoop: Multi-Step Reasoning
```json
{
  "probe_queries": [
    {
      "probe_id": "churn_by_contract",
      "query": "Show churn rate by contract type"
    },
    {
      "probe_id": "high_risk_analysis",
      "depends_on": ["churn_by_contract"],
      "extraction_rules": {
        "churn_by_contract": [{
          "row_index": 0,
          "column": "Contract",
          "as_placeholder": "contract"
        }]
      },
      "query": "Analyze customers with ${contract} contract"
    }
  ]
}
```

## Summary of Business Impact

### What Users Experience with Cortex:
1. **Incomplete Answers**: Get categories without values
2. **Failed Queries**: Common business questions error out
3. **No Context**: Can't build on previous queries
4. **Limited Analysis**: Single SQL only, no investigation

### What Users Get with Scoop:
1. **Complete Context**: Always includes relevant values
2. **Robust Handling**: Graceful handling of all query types
3. **Progressive Building**: Each query enhances understanding
4. **Deep Analysis**: Multi-step investigations with reasoning

## Test Methodology Notes

All tests run on:
- Same datasets (TELCO_DATA, OPENOPPORTUNITIES)
- Same model (Claude-4-Sonnet)
- Same test framework ([DEFINITIVE_TEST_SUITE.py](./DEFINITIVE_TEST_SUITE.py))
- Raw results in [test_results/](./test_results/)

The 57% business correctness rate represents queries that produced actionable, complete answers that a business user could actually use for decision-making.