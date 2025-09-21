# Archive Index: Key Learnings from Snowflake Cortex Testing Journey

This index documents the valuable insights discovered during our comprehensive testing of Snowflake Cortex Analyst. Each file represents a phase of discovery that contributed to our final understanding.

---

## Testing Evolution & Key Discoveries

### Phase 1: Initial Testing & Setup
**Files**: `CORTEX-ANALYST-TESTING-PLAN.md`, `HOW-TO-ACTUALLY-TEST-CORTEX-ANALYST.md`
- **Key Learning**: Discovered Cortex requires semantic_model.yaml configuration
- **Important**: Found Azure Snowflake instance (rcdtonr-ji20455) that actually works
- **Credentials**: bradtest user on Azure instance confirmed functional

### Phase 2: Model Testing - Claude vs LLaMA
**Files**: `CLAUDE4-SONNET-TEST-RESULTS.md`, `CLAUDE4-TEST-STATUS.md`
- **Key Learning**: Model quality isn't the issue - both Claude and LLaMA fail similarly
- **Critical Finding**: Claude-4-Sonnet: 100% success WITH context, 0% WITHOUT
- **Insight**: The problem is architectural, not model-related (5% difference between models)

### Phase 3: Time Intelligence Deep Dive
**File**: `time_intelligence_results.json`, `FINAL-BENCHMARK-RESULTS.md`
- **Key Learning**: 0% success on ALL 15 time intelligence queries
- **Root Cause**: Model adds markdown backticks (```) to SQL, causing syntax errors
- **Example Failure**: LAG/LEAD/OVER functions all broken
- **Business Impact**: Cannot do MoM, YoY, running totals, moving averages

### Phase 4: The 88+ Query Benchmark
**Files**: `COMPREHENSIVE-CAPABILITY-ANALYSIS.md`, `MASTER-TESTING-SUMMARY.md`
- **Test Scale**: 88+ queries across 12 categories
- **Overall Success**: ~35% for Snowflake vs 100% for Scoop
- **Critical Categories with 0% Success**:
  - Time Intelligence (window functions)
  - Statistical Analysis (STDEV, CORR missing)
  - Investigation (returns data, not insights)
  - Change Tracking (no historical analysis)
  - Visualization (no chart specs)

### Phase 5: Semantic Model Discovery
**File**: `semantic_model.yaml`, `SEMANTIC_VALIDATION_PLAN.md`
- **Key Learning**: Semantic model configuration is required but poorly documented
- **Structure Discovered**: Needs tables, columns, relationships, time_dimensions
- **Limitation**: Even with perfect semantic model, core limitations remain

### Phase 6: UI Testing & Limitations
**Files**: `CORTEX-ANALYST-UI-TEST-PLAN.md`, `SNOWFLAKE-INTELLIGENCE-UI-DEFICIENCIES-ANALYSIS.md`
- **Key Finding**: Snowflake Intelligence UI is just a chatbot interface
- **Missing Features**:
  - No query history preservation
  - No context between queries
  - No visualization capabilities
  - No export options
  - Single query/response paradigm

### Phase 7: Eventbrite Benchmark Protocol
**Files**: `EVENTBRITE-BENCHMARK-PROTOCOL.md`, `EVENTBRITE-CORTEX-ANALYST-EVIDENCE.md`
- **Key Learning**: Created reproducible benchmark for customer demos
- **Killer Queries Identified**:
  1. "Show customers from top 5 regions" (subquery test)
  2. "Month-over-month growth" (window function test)
  3. "Why are customers churning?" (ML test)
- **Result**: Snowflake fails all three

### Phase 8: Investigation Capability Analysis
**Files**: `investigation_test.json`, `CORTEX-ANALYST-FINAL-FINDINGS.md`
- **Key Finding**: "Why" questions return raw data, not analysis
- **Example**: "Why are customers churning?" returns `SELECT * WHERE churn='Yes'`
- **Scoop Comparison**: Returns decision tree with factors and importance

### Phase 9: Subquery Discovery - The Critical Gap
**Files**: `SCOOP-VS-CORTEX-CAPABILITY-ANALYSIS.md`, `CRITICAL-BUSINESS-GAPS-SUMMARY.md`
- **CRITICAL FINDING**: Snowflake cannot generate subqueries
- **Business Pattern**: "Show me X from top N Y by metric Z"
- **Technical Issue**: Cannot express multi-step logic in single query
- **Impact**: Eliminates entire categories of business questions

### Phase 10: Statistical Functions Gap
**File**: `SQL-QUALITY-SUMMARY.md`, Statistical test results
- **Missing Functions**:
  - STDEV (standard deviation)
  - CORR (correlation)
  - PERCENTILE_CONT
  - VARIANCE
  - COVAR_POP/COVAR_SAMP
- **Test Evidence**: "Unknown function STDEV" error message
- **Workaround Attempts**: Manual calculation also fails due to subquery limits

### Phase 11: Sales Positioning Development
**Files**: `BATTLE_CARD.md`, `SALES_PLAYBOOK_SNOWFLAKE_HEAVY_PROSPECT.md`
- **Key Messages Developed**:
  - "SQL generator vs analytics engine"
  - "35% vs 100% success rate"
  - Three killer demo queries
- **Objection Handling**: Responses for "but Snowflake has AI"

### Phase 12: Final Architecture Analysis
**Files**: `REVISED-CORTEX-ANALYSIS.md`, `CORTEX-COMPLETE-FINAL-ANALYSIS.md`
- **Core Insight**: Query JSON Object is the key differentiator
- **Architecture Comparison**:
  - Snowflake: Query → SQL → Result
  - Scoop: Query → Classification → Query JSON → Multi-step Plan → SQL → Result
- **Conclusion**: Gap is architectural, not incremental

---

## Critical Test Evidence Preserved

### Azure Connection That Works
```python
# From test_azure_connection.py
account='rcdtonr-ji20455'  # Azure format
user='bradtest'
warehouse='COMPUTE_WH'
database='SCOOP_BENCHMARK'
```

### The Markdown Backtick Bug
```sql
-- Cortex consistently adds these
SELECT ... FROM TABLE
```  -- Error here
```
This causes "syntax error unexpected '``'" in every complex query.

### The Subquery Pattern That Breaks Everything
```json
// Scoop's SubqueryFilter - Cortex cannot express this
{
  "type": "SUBQUERY",
  "attributeName": "Region",
  "operator": "IN",
  "subquery": {
    // Calculate top N
    // Return for filtering
  }
}
```

---

## Unique Insights by Document

### `COMPACT-CONTEXT.md` & `COMPACT-CONTINUATION-CONTEXT.md`
- Attempted to create minimal context for LLM testing
- Discovered context size doesn't fix architectural issues

### `CRITICAL-TESTING-CLARIFICATION.md`
- Clarified that "investigation" queries are fundamentally different
- Established three-layer validation: Generation → Execution → Semantic

### `EVENTBRITE-REVISED-MESSAGE.md`
- Refined messaging for customer communication
- Focused on verifiable, reproducible failures

### `PRE-COMPACT-STATUS.md`
- Documented state before consolidation
- Preserved testing methodology evolution

### `STREAMLIT-CORTEX-ANALYST-TEST-PROTOCOL.md`
- Attempted Streamlit UI testing approach
- Found UI limitations compound core issues

---

## Test Scripts Preserved

### `archive/test-scripts/`
- `RUN_AZURE_TESTS.py` - Full 90-query suite
- `RUN_QUICK_TEST.py` - 16-query focused test
- `test_connection.py` - Verify Azure connection
- Multiple specialized test variants for different aspects

### Key Test Patterns
1. **Basic Success**: COUNT, SUM, simple GROUP BY (both work)
2. **Subquery Failure**: Top N patterns (Scoop only)
3. **Time Intelligence Failure**: Window functions (Scoop only)
4. **Statistical Failure**: Advanced functions (Scoop only)
5. **ML Failure**: Investigation queries (Scoop only)

---

## Conclusions Validated Across All Tests

1. **Architectural Limitation**: Direct SQL generation prevents complex queries
2. **Not Model-Dependent**: Both Claude and LLaMA fail similarly
3. **Subqueries Critical**: Business questions require multi-step logic
4. **Window Functions Broken**: Time intelligence impossible
5. **No ML Integration**: Cannot answer "why" questions
6. **~35% Success Rate**: Only simple queries work

---

## For Future Reference

All files in archive contain valid findings that contributed to our understanding. The journey from "maybe it's a model issue" to "it's architecturally impossible" is documented across these files. Each test iteration refined our understanding of exactly why and how Cortex fails.

The key insight that emerged: **Query JSON Object enables capabilities that are architecturally impossible with direct SQL generation.**