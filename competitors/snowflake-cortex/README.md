# Snowflake Cortex Analyst - Competitive Analysis

## Quick Summary
**Snowflake Cortex Analyst is a basic SQL generator, not a business intelligence platform.**
- Architecture: Direct SQL generation vs Scoop's Query JSON Object
- Critical Gap: Cannot handle subqueries, formula filters, or ML capabilities  
- Test Model: Claude-4-Sonnet (fair comparison with Scoop)
- Test Coverage: 50+ queries across 17 Query JSON capabilities

## Resources

### Primary Documents
- **[RESEARCH REPORT](RESEARCH_REPORT_SCOOP_VS_CORTEX.md)** - 10-page technical analysis for data engineers
- **[COMPLETE ANALYSIS](SNOWFLAKE_CORTEX_COMPLETE_ANALYSIS.md)** - Deep technical comparison
- **[START HERE](START_HERE.md)** - Navigation guide for the analysis

### Test Framework
- **[DEFINITIVE TEST SUITE](DEFINITIVE_TEST_SUITE.py)** - 50+ query test suite covering all Query JSON patterns
- **[Semantic Model](semantic_model.yaml)** - Snowflake configuration
- **[Test Results](test_results/)** - JSON outputs with detailed results

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