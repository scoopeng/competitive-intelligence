#!/usr/bin/env python3
"""
Test Intermediate Queries - Fixed SQL extraction
"""

import snowflake.connector
import json
from datetime import datetime
import re

# Connection
conn = snowflake.connector.connect(
    account='rcdtonr-ji20455',
    user='bradtest',
    password='qMsGeKsE33NJeZp',
    warehouse='COMPUTE_WH',
    database='SCOOP_BENCHMARK',
    schema='TEST_DATA'
)
cursor = conn.cursor()

print("="*80)
print("INTERMEDIATE QUERY TESTING - FIXED SQL EXTRACTION")
print("="*80)

def extract_sql(response):
    """Extract clean SQL from response, removing markdown and explanations"""
    if not response:
        return None
    
    # Remove markdown code blocks
    if '```sql' in response:
        response = response.split('```sql')[1].split('```')[0]
    elif '```' in response:
        # Find content between first set of backticks
        parts = response.split('```')
        if len(parts) > 1:
            response = parts[1]
    
    # Extract just the SQL statement
    lines = response.split('\n')
    sql_lines = []
    found_select = False
    
    for line in lines:
        # Skip empty lines before SELECT
        if not found_select and line.strip() == '':
            continue
        
        # Start capturing from SELECT
        if 'SELECT' in line.upper():
            found_select = True
        
        if found_select:
            # Stop at explanation text or markdown
            if line.strip().startswith('This') or line.strip().startswith('The') or '```' in line:
                break
            # Stop at semicolon
            sql_lines.append(line)
            if ';' in line:
                break
    
    sql = '\n'.join(sql_lines).strip()
    
    # Final cleanup - remove any trailing markdown
    if '```' in sql:
        sql = sql.split('```')[0]
    
    return sql if sql and 'SELECT' in sql.upper() else None

# Test cases
test_cases = [
    {
        "id": "INT_001",
        "query": "Count distinct PAYMENTMETHOD values for customers where CHURN is true in TELCO_DATA",
        "category": "Distinct Counts"
    },
    {
        "id": "INT_002", 
        "query": "Calculate minimum, maximum, and average of MONTHLYCHARGES grouped by CONTRACT in TELCO_DATA",
        "category": "Multiple Aggregations"
    },
    {
        "id": "INT_003",
        "query": "Count rows in TELCO_DATA where MONTHLYCHARGES is between 50 and 100",
        "category": "Range Query"
    },
    {
        "id": "INT_004",
        "query": "Select all columns from TELCO_DATA where MONTHLYCHARGES exceeds the average MONTHLYCHARGES",
        "category": "Subquery"
    },
    {
        "id": "INT_005",
        "query": "Select top 10 rows from TELCO_DATA ordered by MONTHLYCHARGES descending",
        "category": "Top N"
    },
    {
        "id": "INT_006",
        "query": "Count customers by INTERNETSERVICE type where CHURN is true in TELCO_DATA",
        "category": "Group By with Filter"
    },
    {
        "id": "INT_007",
        "query": "Calculate churn rate (count where CHURN=true divided by total count) in TELCO_DATA",
        "category": "Calculated Metrics"
    },
    {
        "id": "INT_008",
        "query": "Show PAYMENTMETHOD and average TOTALCHARGES for each payment method in TELCO_DATA",
        "category": "Aggregation by Category"
    }
]

results = []
success_count = 0
fail_count = 0

for test in test_cases:
    print(f"\n[{test['id']}] {test['category']}")
    print(f"Query: {test['query']}")
    print("-"*40)
    
    try:
        # Detailed prompt with column info
        prompt = f"""Generate SQL for this query: {test['query']}

Important: Return ONLY the SQL statement, no explanations or markdown."""
        
        start = datetime.now()
        cursor.execute(f"""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            'claude-3.5-sonnet',
            %s
        ) as sql
        """, (prompt,))
        
        result = cursor.fetchone()
        elapsed = (datetime.now() - start).total_seconds()
        
        if result and result[0]:
            raw_response = result[0]
            sql_clean = extract_sql(raw_response)
            
            if sql_clean:
                print(f"✅ Generated SQL in {elapsed:.2f}s")
                print(f"SQL: {sql_clean[:200]}...")
                
                # Try to execute
                try:
                    cursor.execute(sql_clean)
                    rows = cursor.fetchall()
                    print(f"✅ EXECUTED: {len(rows)} rows returned")
                    
                    # Show sample result
                    if rows and len(rows) > 0:
                        print(f"Sample result: {rows[0]}")
                    
                    success_count += 1
                    
                    results.append({
                        "test_id": test['id'],
                        "category": test['category'],
                        "status": "SUCCESS",
                        "rows_returned": len(rows),
                        "time": elapsed,
                        "sql": sql_clean
                    })
                    
                except Exception as e:
                    print(f"❌ EXECUTION FAILED: {str(e)[:150]}")
                    fail_count += 1
                    
                    # Analyze error
                    error_type = "Unknown"
                    if "column" in str(e).lower():
                        error_type = "Column Error"
                        print(f"   Issue: Incorrect column name")
                    elif "syntax" in str(e).lower():
                        error_type = "Syntax Error"
                    elif "type" in str(e).lower():
                        error_type = "Type Error"
                    
                    results.append({
                        "test_id": test['id'],
                        "category": test['category'],
                        "status": "SQL_ERROR",
                        "error": str(e)[:200],
                        "error_type": error_type,
                        "time": elapsed,
                        "sql": sql_clean
                    })
            else:
                print(f"❌ Could not extract valid SQL from response")
                print(f"   Raw response: {raw_response[:200]}...")
                fail_count += 1
                results.append({
                    "test_id": test['id'],
                    "category": test['category'],
                    "status": "NO_SQL",
                    "response": raw_response[:500]
                })
        else:
            print(f"❌ No response from CORTEX.COMPLETE")
            fail_count += 1
            
    except Exception as e:
        print(f"❌ ERROR: {str(e)[:150]}")
        fail_count += 1
        results.append({
            "test_id": test['id'],
            "category": test['category'],
            "status": "CORTEX_ERROR",
            "error": str(e)[:200]
        })

# Summary
print("\n" + "="*80)
print("INTERMEDIATE QUERY RESULTS SUMMARY")
print("="*80)
print(f"Tests Run: {len(test_cases)}")
print(f"Successful: {success_count} ({success_count/len(test_cases)*100:.1f}%)")
print(f"Failed: {fail_count} ({fail_count/len(test_cases)*100:.1f}%)")

print("\nResults by Category:")
categories = {}
for r in results:
    cat = r['category']
    if cat not in categories:
        categories[cat] = {"success": 0, "fail": 0}
    if r['status'] == "SUCCESS":
        categories[cat]['success'] += 1
    else:
        categories[cat]['fail'] += 1

for cat, stats in categories.items():
    total = stats['success'] + stats['fail']
    success_rate = (stats['success'] / total * 100) if total > 0 else 0
    print(f"  {cat}: {stats['success']}/{total} ({success_rate:.1f}% success)")

print("\nError Analysis:")
error_types = {}
for r in results:
    if r['status'] == 'SQL_ERROR':
        err_type = r.get('error_type', 'Unknown')
        if err_type not in error_types:
            error_types[err_type] = 0
        error_types[err_type] += 1

for err_type, count in error_types.items():
    print(f"  {err_type}: {count} occurrences")

# Save results
with open('intermediate_results_fixed.json', 'w') as f:
    json.dump({
        "summary": {
            "total": len(test_cases),
            "success": success_count,
            "fail": fail_count,
            "success_rate": f"{success_count/len(test_cases)*100:.1f}%"
        },
        "categories": categories,
        "error_types": error_types,
        "details": results
    }, f, indent=2)
    
print(f"\n✅ Results saved to intermediate_results_fixed.json")

# Combined results with original tests
print("\n" + "="*80)
print("CUMULATIVE BENCHMARK PROGRESS")
print("="*80)
original_tests = 7
original_success = 5
total_tests = original_tests + len(test_cases)
total_success = original_success + success_count

print(f"Original Tests: {original_success}/{original_tests} ({original_success/original_tests*100:.1f}%)")
print(f"Intermediate Tests: {success_count}/{len(test_cases)} ({success_count/len(test_cases)*100:.1f}%)")
print(f"Combined Total: {total_success}/{total_tests} ({total_success/total_tests*100:.1f}%)")
print(f"\nTests Completed: {total_tests}/30+ ({total_tests/30*100:.0f}% of Scoop benchmark)")

conn.close()