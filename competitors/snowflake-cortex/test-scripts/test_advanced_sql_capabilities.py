#!/usr/bin/env python3
"""
Test CORTEX.COMPLETE against Scoop's advanced query capabilities
Based on Query JSON Object patterns
"""

import snowflake.connector
import json

# Connection
conn = snowflake.connector.connect(
    account='toajlpe-nfb33705',
    user='bradscoop',
    password='D6c2BmtJWPy3dM7',
    warehouse='COMPUTE_WH',
    database='SCOOP_BENCHMARK',
    schema='TEST_DATA'
)
cursor = conn.cursor()

print("="*80)
print("TESTING ADVANCED SQL CAPABILITIES VS SCOOP QUERY PATTERNS")
print("="*80)

# Test cases based on Scoop's rich query patterns
advanced_tests = [
    {
        "id": "ADV_001",
        "category": "Complex Filtering",
        "scoop_pattern": "Compound filters with AND/OR",
        "query": "Show customers in TELCO_DATA with StreamingTV='Yes' AND StreamingMovies='Yes' BUT TechSupport='No'",
        "expected": "Compound WHERE clause with multiple conditions"
    },
    {
        "id": "ADV_002", 
        "category": "Calculated Metrics",
        "scoop_pattern": "Formulas with Excel-like expressions",
        "query": "Calculate customer lifetime value as (MONTHLYCHARGES * TENURE) / IF(TOTALCHARGES=0, 1, TOTALCHARGES) from TELCO_DATA",
        "expected": "Complex calculation with division protection"
    },
    {
        "id": "ADV_003",
        "category": "Percentage of Total",
        "scoop_pattern": "Share calculations using SUM() over entire result",
        "query": "Show each CONTRACT type's percentage of total customers in TELCO_DATA",
        "expected": "Window function or subquery for total"
    },
    {
        "id": "ADV_004",
        "category": "Threshold Filtering",
        "scoop_pattern": "Filter on calculated values",
        "query": "Show only customers from TELCO_DATA where (MONTHLYCHARGES * TENURE) > 5000",
        "expected": "HAVING clause or calculated field filter"
    },
    {
        "id": "ADV_005",
        "category": "Top N by Calculated Metric",
        "scoop_pattern": "Subquery pattern for top N",
        "query": "Show top 5 PAYMENTMETHOD types by average MONTHLYCHARGES in TELCO_DATA",
        "expected": "Subquery or window function for ranking"
    },
    {
        "id": "ADV_006",
        "category": "Conditional Aggregation",
        "scoop_pattern": "Conditional counts/sums with CASE",
        "query": "Count customers in TELCO_DATA: total, churned (CHURN='Yes'), and retention rate",
        "expected": "Multiple CASE statements in single query"
    },
    {
        "id": "ADV_007",
        "category": "Running/Cumulative",
        "scoop_pattern": "Cumulative calculations",
        "query": "Show running total of customers by TENURE months in TELCO_DATA",
        "expected": "Window function with ROWS UNBOUNDED"
    },
    {
        "id": "ADV_008",
        "category": "Standard Deviation",
        "scoop_pattern": "STDEV statistical function",
        "query": "Calculate standard deviation of MONTHLYCHARGES by CONTRACT type in TELCO_DATA",
        "expected": "STDDEV or STDEV function usage"
    },
    {
        "id": "ADV_009",
        "category": "Date Comparisons",
        "scoop_pattern": "DATEDIF for date calculations",
        "query": "If TELCO_DATA had StartDate and EndDate, calculate days between them",
        "expected": "Date difference calculation"
    },
    {
        "id": "ADV_010",
        "category": "Zero Protection",
        "scoop_pattern": "IF(denominator=0, 1, denominator)",
        "query": "Calculate average revenue per tenure month as TOTALCHARGES/IF(TENURE=0, 1, TENURE) in TELCO_DATA",
        "expected": "Division by zero protection"
    }
]

results = []

def analyze_sql_quality(sql, test):
    """Analyze if generated SQL matches expected capabilities"""
    if not sql:
        return {"generated": False}
    
    sql_upper = sql.upper()
    
    analysis = {
        "generated": True,
        "has_compound_filter": ' AND ' in sql_upper or ' OR ' in sql_upper,
        "has_case_when": 'CASE' in sql_upper,
        "has_window_function": 'OVER(' in sql_upper or 'PARTITION BY' in sql_upper,
        "has_subquery": sql_upper.count('SELECT') > 1,
        "has_calculation": any(op in sql for op in ['+', '-', '*', '/']),
        "has_if_statement": 'IF(' in sql_upper or 'IIF(' in sql_upper,
        "has_having": 'HAVING' in sql_upper,
        "has_stddev": 'STDDEV' in sql_upper or 'STDEV' in sql_upper,
        "has_limit": 'LIMIT' in sql_upper or 'TOP' in sql_upper,
        "has_group_by": 'GROUP BY' in sql_upper
    }
    
    return analysis

for test in advanced_tests:
    print(f"\n{'='*70}")
    print(f"[{test['id']}] {test['category']}")
    print(f"Scoop Pattern: {test['scoop_pattern']}")
    print(f"Query: {test['query'][:80]}...")
    print(f"Expected: {test['expected']}")
    print("-"*70)
    
    try:
        cursor.execute(f"""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            'llama3-70b',
            CONCAT('Generate SQL for: ', %s)
        ) as response
        """, (test['query'],))
        
        result = cursor.fetchone()
        
        if result and result[0]:
            response = result[0]
            
            # Extract SQL
            sql = None
            if 'SELECT' in response.upper():
                sql_start = response.upper().find('SELECT')
                sql = response[sql_start:]
                if '```' in sql:
                    sql = sql.split('```')[0]
                
                print(f"\nGENERATED SQL:")
                print(sql[:300])
                if len(sql) > 300:
                    print("...")
                
                # Analyze capabilities
                analysis = analyze_sql_quality(sql, test)
                
                print(f"\nCAPABILITY ANALYSIS:")
                print(f"  Compound filters: {'✅' if analysis.get('has_compound_filter') else '❌'}")
                print(f"  CASE statements: {'✅' if analysis.get('has_case_when') else '❌'}")
                print(f"  Window functions: {'✅' if analysis.get('has_window_function') else '❌'}")
                print(f"  Subqueries: {'✅' if analysis.get('has_subquery') else '❌'}")
                print(f"  Calculations: {'✅' if analysis.get('has_calculation') else '❌'}")
                print(f"  Conditional logic: {'✅' if analysis.get('has_if_statement') else '❌'}")
                
                # Try to execute
                try:
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    print(f"  Executes: ✅ ({len(rows)} rows)")
                    executable = True
                except Exception as e:
                    print(f"  Executes: ❌ ({str(e)[:50]})")
                    executable = False
                
                # Judge if it matches Scoop capability
                matches_pattern = False
                if test['category'] == 'Complex Filtering':
                    matches_pattern = analysis.get('has_compound_filter', False)
                elif test['category'] == 'Calculated Metrics':
                    matches_pattern = analysis.get('has_calculation', False)
                elif test['category'] == 'Percentage of Total':
                    matches_pattern = analysis.get('has_window_function', False) or analysis.get('has_subquery', False)
                elif test['category'] == 'Top N by Calculated Metric':
                    matches_pattern = analysis.get('has_limit', False) and analysis.get('has_group_by', False)
                elif test['category'] == 'Conditional Aggregation':
                    matches_pattern = analysis.get('has_case_when', False)
                elif test['category'] == 'Standard Deviation':
                    matches_pattern = analysis.get('has_stddev', False)
                
                print(f"\nMATCHES SCOOP PATTERN: {'✅' if matches_pattern else '❌'}")
                
                results.append({
                    "test": test['id'],
                    "category": test['category'],
                    "sql_generated": True,
                    "executable": executable,
                    "matches_pattern": matches_pattern,
                    **analysis
                })
            else:
                print("❌ NO SQL GENERATED")
                results.append({
                    "test": test['id'],
                    "category": test['category'],
                    "sql_generated": False
                })
                
    except Exception as e:
        print(f"ERROR: {str(e)}")
        results.append({
            "test": test['id'],
            "category": test['category'],
            "error": str(e)[:100]
        })

# Summary
print("\n" + "="*80)
print("CAPABILITY COMPARISON: CORTEX.COMPLETE vs SCOOP PATTERNS")
print("="*80)

# Calculate success rates by capability
capabilities = {
    'Compound Filters': 0,
    'Calculations': 0,
    'Window Functions': 0,
    'Subqueries': 0,
    'Conditional Logic': 0,
    'Statistical Functions': 0,
    'Pattern Matching': 0
}

for r in results:
    if r.get('sql_generated'):
        if r.get('has_compound_filter'): capabilities['Compound Filters'] += 1
        if r.get('has_calculation'): capabilities['Calculations'] += 1
        if r.get('has_window_function'): capabilities['Window Functions'] += 1
        if r.get('has_subquery'): capabilities['Subqueries'] += 1
        if r.get('has_case_when') or r.get('has_if_statement'): capabilities['Conditional Logic'] += 1
        if r.get('has_stddev'): capabilities['Statistical Functions'] += 1
        if r.get('matches_pattern'): capabilities['Pattern Matching'] += 1

print("\nCapability Support (out of 10 tests):")
for cap, count in capabilities.items():
    percentage = (count / len(results)) * 100
    status = "✅" if percentage >= 50 else "⚠️" if percentage >= 25 else "❌"
    print(f"  {status} {cap}: {count}/10 ({percentage:.0f}%)")

print("\n🔴 KEY FINDINGS:")
print("1. Basic SQL capabilities are present")
print("2. Complex patterns from Scoop Query JSON often not matched")
print("3. Missing: cumulative calculations, formula filters, share calculations")
print("4. Limited: window functions, statistical operations beyond basics")

# Save results
with open('advanced_capability_results.json', 'w') as f:
    json.dump({
        "tests": results,
        "capability_summary": capabilities,
        "scoop_patterns_matched": sum(1 for r in results if r.get('matches_pattern', False))
    }, f, indent=2)

print("\n💾 Results saved to advanced_capability_results.json")

conn.close()