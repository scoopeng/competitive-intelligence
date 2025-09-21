# Snowflake Cortex Test Status

**Last Updated**: September 21, 2025
**Model**: Claude-4-Sonnet (fair comparison with Scoop)
**Status**: Ready for comprehensive testing

## Test Framework

### Current Setup
- **Framework**: `DEFINITIVE_TEST_SUITE.py`
- **Queries**: 50+ covering all Query JSON Object capabilities
- **Datasets**: TELCO_DATA, OPENOPPORTUNITIES (same as Scoop)
- **Unattended**: Full timeout, retry, and progress tracking

### Query JSON Object Capabilities Tested

| Capability | Tests | Expected Result |
|------------|-------|----------------|
| SUBQUERY | 8 | Cortex fails - cannot nest |
| FORMULA_FILTER | 5 | Cortex fails - no HAVING on calcs |
| WINDOW_FUNCTION | 5 | Cortex fails - syntax errors |
| STATISTICAL | 5 | Mixed - STDDEV works with Claude |
| ML_RELATIONSHIP | 5 | Cortex fails - no analysis |
| CORRELATED_SUBQUERY | 3 | Cortex fails - too complex |
| CONDITIONAL_FORMULA | 3 | Cortex fails - IF not handled |
| CUMULATIVE | 2 | Cortex fails - no running totals |
| BASIC_FILTER | 10 | Both succeed |
| FORMULA | 6 | Mixed results |

## Key Findings (from initial tests)

### With Claude-4-Sonnet:
- ✅ STDDEV works (unlike LLaMA)
- ❌ Subqueries still fail (architectural)
- ❌ Window functions have syntax errors
- ❌ Formula filters cannot be expressed
- ❌ Investigation returns data not insights

### Architectural Difference:
```
Cortex: Natural Language → SQL → Result
Scoop:  Natural Language → Query JSON Object → Multi-step Plan → SQL → Result
```

The Query JSON Object enables capabilities impossible with direct SQL generation.

## To Run Tests

```bash
# Quick test (sample queries)
python3 DEFINITIVE_TEST_SUITE.py

# Full suite (50+ queries)
python3 DEFINITIVE_TEST_SUITE.py --full
```

## Expected Outcomes

### Cortex Should Succeed On:
- Basic aggregations (COUNT, SUM, AVG)
- Simple GROUP BY
- Basic WHERE filters
- ORDER BY and LIMIT
- STDDEV (with Claude-4-Sonnet)

### Cortex Should Fail On:
- Subqueries with IN clause
- Filtering on calculated values
- Window functions (LAG, LEAD)
- Correlated subqueries
- ML/Investigation queries
- Multi-level nested logic

## Files Consolidated

Removed redundant test frameworks:
- ~~CLAUDE4_SONNET_TEST_FRAMEWORK.py~~
- ~~COMPREHENSIVE_TEST_SUITE.py~~
- ~~RUN_CORTEX_TESTS.py~~
- ~~SNOWFLAKE_TEST_FRAMEWORK.py~~
- ~~UNATTENDED_TEST_SUITE.py~~

Single source of truth: **DEFINITIVE_TEST_SUITE.py**