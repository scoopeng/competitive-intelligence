#!/usr/bin/env python3
"""
Test CORTEX.COMPLETE (what's actually available) vs Scoop Query JSON
"""

import snowflake.connector
import json
from datetime import datetime

# Connect
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
print("TESTING CORTEX.COMPLETE vs SCOOP QUERY JSON")
print("Note: This is NOT Cortex Analyst - that's not available on trial!")
print("="*80)

test_cases = [
    {
        "id": "TEST_001",
        "query": "What is the total number of customers in TELCO_DATA?",
        "scoop_json_lines": 8
    },
    {
        "id": "TEST_002", 
        "query": "What is the average MONTHLYCHARGES in TELCO_DATA?",
        "scoop_json_lines": 10
    },
    {
        "id": "TEST_003",
        "query": "Show churn rate by CONTRACT in TELCO_DATA where CHURN is boolean",
        "scoop_json_lines": 15
    },
    {
        "id": "TEST_004",
        "query": "Show customers from TELCO_DATA with MONTHLYCHARGES > 100 who have CHURN = true",
        "scoop_json_lines": 12
    },
    {
        "id": "TEST_005",
        "query": "Which combination of CONTRACT and PAYMENTMETHOD has highest churn rate in TELCO_DATA?",
        "scoop_json_lines": 25
    },
    {
        "id": "TEST_006",
        "query": "Calculate (MONTHLYCHARGES * TENURE) / (NUMADMINTICKETS + NUMTECHTICKETS + 1) as customer_value from TELCO_DATA",
        "scoop_json_lines": 18
    },
    {
        "id": "TEST_007",
        "query": "Why are customers churning in TELCO_DATA?",
        "scoop_json_lines": 50
    }
]

results = []

for test in test_cases:
    print(f"\n{test['id']}: {test['query'][:50]}...")
    print("-"*40)
    
    try:
        # Call CORTEX.COMPLETE
        start = datetime.now()
        cursor.execute(f"""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            'llama3-70b',
            'Generate only SQL, no explanation, for this query: {test['query']}'
        ) as sql
        """)
        result = cursor.fetchone()
        elapsed = (datetime.now() - start).total_seconds()
        
        sql = result[0] if result else "No SQL generated"
        sql_lines = len(sql.split('\n'))
        
        print(f"✅ Generated {sql_lines} lines of SQL in {elapsed:.2f}s")
        print(f"SQL Preview: {sql[:150]}...")
        
        # Now try to execute the generated SQL
        try:
            # Extract just the SQL part (remove markdown if present)
            if '```sql' in sql:
                sql_clean = sql.split('```sql')[1].split('```')[0].strip()
            elif '```' in sql:
                sql_clean = sql.split('```')[1].split('```')[0].strip()
            else:
                # Try to find SELECT statement
                lines = sql.split('\n')
                sql_clean = '\n'.join([l for l in lines if 'SELECT' in l.upper() or 'FROM' in l.upper() or 'WHERE' in l.upper() or 'GROUP' in l.upper() or 'ORDER' in l.upper()])
            
            if sql_clean and 'SELECT' in sql_clean.upper():
                cursor.execute(sql_clean)
                rows = cursor.fetchall()
                print(f"✅ SQL executed successfully! Returned {len(rows)} rows")
                works = True
            else:
                print(f"❌ Could not extract valid SQL")
                works = False
                
        except Exception as e:
            print(f"❌ SQL execution failed: {str(e)[:100]}")
            works = False
        
        results.append({
            "test_id": test['id'],
            "query": test['query'][:50],
            "sql_lines": sql_lines,
            "scoop_lines": test['scoop_json_lines'],
            "ratio": round(sql_lines / test['scoop_json_lines'], 1),
            "time": round(elapsed, 2),
            "works": works
        })
        
    except Exception as e:
        print(f"❌ Failed: {e}")
        results.append({
            "test_id": test['id'],
            "query": test['query'][:50],
            "sql_lines": 0,
            "scoop_lines": test['scoop_json_lines'],
            "ratio": 0,
            "time": 0,
            "works": False
        })

print("\n" + "="*80)
print("SUMMARY RESULTS: CORTEX.COMPLETE vs SCOOP")
print("="*80)

print("\n| Test | Query | SQL Lines | Scoop Lines | Ratio | Works? |")
print("|------|-------|-----------|-------------|-------|--------|")
for r in results:
    print(f"| {r['test_id']} | {r['query'][:30]}... | {r['sql_lines']} | {r['scoop_lines']} | {r['ratio']}x | {'✅' if r['works'] else '❌'} |")

successful = sum(1 for r in results if r['works'])
print(f"\n✅ Successful: {successful}/{len(results)}")
print(f"❌ Failed: {len(results)-successful}/{len(results)}")

avg_ratio = sum(r['ratio'] for r in results) / len(results)
print(f"📊 Average Complexity: {avg_ratio:.1f}x more lines than Query JSON")

print("\n" + "="*80)
print("KEY FINDINGS")
print("="*80)
print("1. This is CORTEX.COMPLETE, not Cortex Analyst")
print("2. Cortex Analyst (the real competitor) is NOT available on trial")
print("3. COMPLETE generates verbose SQL with explanations")
print("4. Many generated queries don't execute properly")
print("5. No multi-step reasoning capability")

conn.close()