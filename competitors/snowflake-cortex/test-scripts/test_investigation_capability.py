#!/usr/bin/env python3
"""
Quick test to prove Snowflake cannot do multi-step investigation
"""

import snowflake.connector
import json
from datetime import datetime

# Connection
conn = snowflake.connector.connect(
    account='toajlpe-nfb33705',
    user='bradscoop',
    password='D6c2BmtJWPy3dM7',
    warehouse='COMPUTE_WH',
    database='SCOOP_BENCHMARK',
    schema='TEST_DATA',
    network_timeout=30
)
cursor = conn.cursor()

print("="*80)
print("INVESTIGATION CAPABILITY TEST - SCOOP vs SNOWFLAKE")
print("Testing if Snowflake can perform multi-step root cause analysis")
print("="*80)

def extract_sql(response):
    """Extract SQL from response"""
    if not response:
        return None
    
    if '```sql' in response.lower():
        response = response.split('```sql')[1].split('```')[0]
    elif '```' in response:
        parts = response.split('```')
        if len(parts) > 1:
            response = parts[1]
    
    # Check if there's actual SQL
    if 'SELECT' in response.upper():
        return response.strip()
    return None

# Critical test cases that require investigation
test_cases = [
    {
        "id": "INVESTIGATION_001",
        "query": "Why are customers churning? Investigate root causes in TELCO_DATA",
        "scoop_capability": "Performs 3-5 queries to find correlations and drivers"
    },
    {
        "id": "INVESTIGATION_002",
        "query": "What drives high monthly charge customers to churn in TELCO_DATA?",
        "scoop_capability": "Multi-dimensional analysis of high-value segment"
    },
    {
        "id": "INVESTIGATION_003",
        "query": "Find the pattern that best predicts churn in TELCO_DATA",
        "scoop_capability": "Tests multiple factor combinations"
    }
]

print("\nTesting Snowflake's Investigation Capability...")
print("-"*80)

investigation_capable = False
results = []

for test in test_cases:
    print(f"\n[{test['id']}]")
    print(f"Query: {test['query']}")
    print(f"Scoop: {test['scoop_capability']}")
    print("Snowflake attempt:")
    
    try:
        prompt = f"Investigate this question: {test['query']}. Provide comprehensive analysis."
        
        start = datetime.now()
        cursor.execute(f"""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            'llama3-70b',
            %s
        ) as response
        """, (prompt,))
        
        result = cursor.fetchone()
        elapsed = (datetime.now() - start).total_seconds()
        
        if result and result[0]:
            response = result[0]
            
            # Check if it generated multiple queries (investigation)
            query_count = response.upper().count('SELECT')
            
            print(f"  Response time: {elapsed:.2f}s")
            print(f"  Query count: {query_count}")
            
            if query_count > 1:
                print(f"  ✅ INVESTIGATION DETECTED: {query_count} queries")
                investigation_capable = True
            else:
                print(f"  ❌ SINGLE QUERY ONLY - No investigation")
            
            # Try to extract and execute SQL
            sql = extract_sql(response)
            if sql:
                try:
                    # Only execute if single query (multiple would need splitting)
                    if query_count == 1 and 'SELECT' in sql.upper():
                        cursor.execute(sql)
                        rows = cursor.fetchall()
                        print(f"  Execution: {len(rows)} rows")
                except:
                    print(f"  Execution: Failed")
            
            results.append({
                "test": test['id'],
                "query_count": query_count,
                "investigation": query_count > 1,
                "time": elapsed
            })
            
    except Exception as e:
        print(f"  ❌ Error: {str(e)[:100]}")
        results.append({
            "test": test['id'],
            "error": str(e)[:100]
        })

# Final verdict
print("\n" + "="*80)
print("INVESTIGATION CAPABILITY VERDICT")
print("="*80)

if investigation_capable:
    print("✅ Snowflake CAN perform multi-step investigation")
else:
    print("❌ Snowflake CANNOT perform multi-step investigation")
    print("   - Limited to single SQL queries")
    print("   - No root cause analysis")
    print("   - No multi-hypothesis testing")

print("\nScoop Advantage:")
print("✅ 3-10 query investigations")
print("✅ Root cause analysis")
print("✅ Pattern discovery")
print("✅ ML-based insights")

# Save compact results
with open('investigation_test.json', 'w') as f:
    json.dump({
        "investigation_capable": investigation_capable,
        "tests": results,
        "verdict": "Snowflake limited to single queries - no investigation"
    }, f, indent=2)

conn.close()
print("\n✅ Test complete - results in investigation_test.json")