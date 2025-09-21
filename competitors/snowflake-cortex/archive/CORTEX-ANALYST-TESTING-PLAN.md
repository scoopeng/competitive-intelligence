# Cortex Analyst Testing Plan

## Context from CORTEX.COMPLETE Testing

We've completed comprehensive testing of CORTEX.COMPLETE (73 queries tested), which is the underlying LLM for Cortex Analyst. Key findings:
- 0% success with natural language
- 60-70% success with table context for basic queries
- 0% capability for investigation, time intelligence, or multi-step analysis

## Next Phase: Cortex Analyst UI Testing

### What Cortex Analyst Adds on Top of COMPLETE:
1. **Semantic Model** - Maps business terms to database schema
2. **Streamlit UI** - Visual interface vs API calls
3. **Context Management** - Maintains table/column context

### What It CANNOT Fix:
1. Single-query limitation (no multi-step investigation)
2. Lack of statistical depth
3. No time intelligence
4. No pattern discovery
5. No "why" analysis capability

## Testing Approach for Cortex Analyst

### Option 1: EventBrite Tests It Themselves
Since they have enterprise Snowflake:
1. Use the Streamlit template
2. Create semantic model for their data
3. Run the same 73 queries we tested
4. Document the experience

### Option 2: Create Test Protocol
Document exactly how to test:
1. Setup requirements
2. Semantic model creation
3. Query test suite
4. Scoring criteria

### Key Test Categories to Run:
1. **Natural Language** (15 queries) - Will semantic model help?
2. **Investigation** (10 queries) - Can it answer "why"?
3. **Time Intelligence** (5 queries) - Period comparisons?
4. **Advanced Patterns** (20 queries) - Scoop capabilities?

## Expected Results

Based on CORTEX.COMPLETE limitations:

### What Will Improve with Cortex Analyst:
- Natural language → table mapping (semantic model helps)
- Column name accuracy (semantic model provides)
- Business term understanding (semantic layer)

### What Will NOT Improve:
- Investigation capability (still single query)
- Time intelligence (no period shifting)
- Statistical depth (limited to basic functions)
- Multi-step analysis (architecture limitation)
- Pattern discovery (no ML integration)

## Files to Keep for Cortex Analyst Testing

### Core Test Scripts:
- `test_natural_language.py` - Baseline for comparison
- `test_comprehensive_patterns.py` - Scoop capability benchmark
- `test_investigation_capability.py` - "Why" questions

### Results for Comparison:
- `natural_language_results.json` - 0% baseline
- `comprehensive_pattern_results.json` - Pattern capabilities
- `intermediate_results_fixed.json` - SQL-instructed baseline

### Documentation:
- `MASTER-TESTING-SUMMARY.md` - Complete findings
- `EVENTBRITE-BENCHMARK-PROTOCOL.md` - How to test
- `HOW-TO-ACTUALLY-TEST-CORTEX-ANALYST.md` - Practical guide

## Key Questions for Cortex Analyst

1. Does the semantic model overcome natural language failures?
2. Can it handle investigation queries with semantic layer?
3. Does the UI enable multi-step analysis somehow?
4. What's the actual setup time and complexity?
5. Can business users work independently?

## Success Criteria

For Cortex Analyst to be viable for EventBrite:
- [ ] >80% success on natural language queries
- [ ] Ability to answer "why" questions
- [ ] Multi-step investigation capability
- [ ] No SQL knowledge required
- [ ] Business user independence

Based on CORTEX.COMPLETE testing, we expect:
- Natural language: Improved but not 80%
- Investigation: Still impossible
- Multi-step: Not supported
- SQL knowledge: Hidden but limited by capabilities
- Independence: Requires IT for semantic model

## Next Steps

1. **Clean Environment**: Archive COMPLETE-specific tests
2. **Prepare Protocols**: Update testing guides for Analyst
3. **Set Expectations**: Document what's possible/impossible
4. **Enable EventBrite**: Provide clear testing instructions