# Snowflake Cortex Analyst - Competitive Analysis

## Quick Summary
**Snowflake Cortex Analyst is a basic SQL generator, not a business intelligence platform.**
- Success Rate: 68.8% overall, but 0% on complex queries
- Critical Gap: No subqueries, window functions, or ML capabilities
- Verdict: Architectural limitations make it unsuitable for real BI

## Resources

### Primary Analysis
- **[COMPLETE ANALYSIS](SNOWFLAKE_CORTEX_COMPLETE_ANALYSIS.md)** - Comprehensive competitive analysis with test results, architectural comparison, and business impact

### Test Framework
- **[Test Framework](SNOWFLAKE_TEST_FRAMEWORK.py)** - Clean testing framework for benchmarking
- **[Semantic Model](semantic_model.yaml)** - Snowflake configuration
- **[Test Results](test_results/)** - JSON outputs from testing

### Archive
- **[Archive](archive/)** - Previous iterations and detailed test scripts

## Three Killer Limitations

### 1. No Subqueries
**Cannot answer**: "Show me customers from top 5 regions"
- Scoop: ✅ Handles via Query JSON SubqueryFilter  
- Snowflake: ❌ Cannot express multi-step logic

### 2. No Window Functions  
**Cannot answer**: "Show month-over-month growth"
- Scoop: ✅ Full time intelligence support
- Snowflake: ❌ 0% success on ALL time queries

### 3. No Investigation
**Cannot answer**: "Why are customers churning?"
- Scoop: ✅ ML analysis with decision trees
- Snowflake: ❌ Returns raw data, no insights

## The Proof Query

**"Show all opportunities from the top 5 sales reps by win rate"**

This single query demonstrates Snowflake's inability to:
- Calculate derived metrics (win rate = won/total)
- Use subqueries to find top performers
- Filter main results by subquery output

Scoop handles this elegantly. Snowflake cannot express it at all.

## For Sales Teams

When prospects mention Snowflake Cortex Analyst, ask them to demo these queries:
1. "Show customers from your top 5 regions" (tests subqueries)
2. "Calculate month-over-month growth" (tests window functions)
3. "Why are customers churning?" (tests ML/investigation)

Snowflake will fail all three.