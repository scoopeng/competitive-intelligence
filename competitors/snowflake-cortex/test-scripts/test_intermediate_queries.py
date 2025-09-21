#!/usr/bin/env python3
"""
Test Intermediate Queries - Smaller batch to avoid timeout
"""

import snowflake.connector
import json
from datetime import datetime

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
print("INTERMEDIATE QUERY TESTING - SNOWFLAKE CORTEX.COMPLETE")
print("="*80)

# Smaller batch of intermediate tests
test_cases = [
    {
        "id": "INT_001",
        "query": "How many distinct payment methods are used by churned customers in TELCO_DATA?",
        "category": "Distinct Counts"
    },
    {
        "id": "INT_002", 
        "query": "Show min, max, and average MONTHLYCHARGES by CONTRACT type in TELCO_DATA",
        "category": "Multiple Aggregations"
    },
    {
        "id": "INT_003",
        "query": "Count customers with MONTHLYCHARGES between 50 and 100 in TELCO_DATA",
        "category": "Range Query"
    },
    {
        "id": "INT_004",
        "query": "Find customers in TELCO_DATA who pay more than average MONTHLYCHARGES",
        "category": "Subquery"
    },
    {
        "id": "INT_005",
        "query": "Show top 10 customers by MONTHLYCHARGES from TELCO_DATA",
        "category": "Top N"
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
        # Simple prompt
        prompt = f"Generate only SQL for: {test['query']}"
        
        start = datetime.now()
        cursor.execute(f"""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            'claude-3.5-sonnet',
            '{prompt}'
        ) as sql
        """)
        
        result = cursor.fetchone()
        elapsed = (datetime.now() - start).total_seconds()
        
        if result and result[0]:
            sql = result[0]
            
            # Extract SQL
            if 'SELECT' in sql.upper():
                # Find SELECT statement
                sql_start = sql.upper().find('SELECT')
                sql_clean = sql[sql_start:]
                # Remove any trailing explanation
                if '\n\n' in sql_clean:
                    sql_clean = sql_clean.split('\n\n')[0]
                
                print(f"✅ Generated SQL in {elapsed:.2f}s")
                print(f"SQL: {sql_clean[:150]}...")
                
                # Try to execute
                try:
                    cursor.execute(sql_clean)
                    rows = cursor.fetchall()
                    print(f"✅ EXECUTED: {len(rows)} rows returned")
                    success_count += 1
                    
                    results.append({
                        "test_id": test['id'],
                        "category": test['category'],
                        "status": "SUCCESS",
                        "rows_returned": len(rows),
                        "time": elapsed
                    })
                    
                except Exception as e:
                    print(f"❌ EXECUTION FAILED: {str(e)[:100]}")
                    fail_count += 1
                    
                    results.append({
                        "test_id": test['id'],
                        "category": test['category'],
                        "status": "SQL_ERROR",
                        "error": str(e)[:200],
                        "time": elapsed
                    })
            else:
                print(f"❌ No valid SQL generated")
                fail_count += 1
                results.append({
                    "test_id": test['id'],
                    "category": test['category'],
                    "status": "NO_SQL",
                    "response": sql[:200]
                })
        else:
            print(f"❌ No response from CORTEX.COMPLETE")
            fail_count += 1
            
    except Exception as e:
        print(f"❌ ERROR: {str(e)[:100]}")
        fail_count += 1
        results.append({
            "test_id": test['id'],
            "category": test['category'],
            "status": "CORTEX_ERROR",
            "error": str(e)[:200]
        })

# Summary
print("\n" + "="*80)
print("INTERMEDIATE QUERY RESULTS")
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
    print(f"  {cat}: {stats['success']} success, {stats['fail']} fail")

# Save results
with open('intermediate_results.json', 'w') as f:
    json.dump({
        "summary": {
            "total": len(test_cases),
            "success": success_count,
            "fail": fail_count,
            "success_rate": f"{success_count/len(test_cases)*100:.1f}%"
        },
        "details": results
    }, f, indent=2)
    
print("\n✅ Results saved to intermediate_results.json")

conn.close()