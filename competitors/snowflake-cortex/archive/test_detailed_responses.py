#!/usr/bin/env python3
"""
Examine FULL responses from CORTEX.COMPLETE to understand what's actually being generated
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
    schema='TEST_DATA'
)
cursor = conn.cursor()

print("="*80)
print("DETAILED RESPONSE ANALYSIS - WHAT IS CORTEX.COMPLETE ACTUALLY GENERATING?")
print("="*80)

# Test a few key queries to see FULL responses
test_queries = [
    {
        "id": "DETAIL_001",
        "query": "How many customers do we have?",
        "category": "Simple Count"
    },
    {
        "id": "DETAIL_002",
        "query": "Generate SQL to count rows in TELCO_DATA table",
        "category": "Explicit SQL Request"
    },
    {
        "id": "DETAIL_003",
        "query": "What's the average MONTHLYCHARGES in TELCO_DATA?",
        "category": "With Table Name"
    },
    {
        "id": "DETAIL_004",
        "query": "SQL query: What's the average monthly charge?",
        "category": "SQL Prefix"
    },
    {
        "id": "DETAIL_005",
        "query": "Write a SQL query to show churn rate by contract type",
        "category": "Explicit SQL Instruction"
    }
]

results = []

for test in test_queries:
    print(f"\n[{test['id']}] Testing: {test['category']}")
    print(f"Query: \"{test['query']}\"")
    print("-"*60)
    
    try:
        cursor.execute(f"""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            'llama3-70b',
            %s
        ) as response
        """, (test['query'],))
        
        result = cursor.fetchone()
        
        if result and result[0]:
            response = result[0]
            print(f"\nFULL RESPONSE:")
            print("="*40)
            print(response)
            print("="*40)
            
            # Analyze response
            has_select = 'SELECT' in response.upper()
            has_from = 'FROM' in response.upper()
            looks_like_sql = has_select and has_from
            
            print(f"\nANALYSIS:")
            print(f"- Contains SELECT: {has_select}")
            print(f"- Contains FROM: {has_from}")
            print(f"- Looks like SQL: {looks_like_sql}")
            
            if looks_like_sql:
                # Try to extract and execute SQL
                print("\nAttempting to extract SQL...")
                
                # Find SQL portion
                sql_start = response.upper().find('SELECT')
                if sql_start >= 0:
                    sql_portion = response[sql_start:]
                    
                    # Clean it up
                    if '```' in sql_portion:
                        sql_portion = sql_portion.split('```')[0]
                    
                    # Remove explanatory text after SQL
                    lines = sql_portion.split('\n')
                    sql_lines = []
                    for line in lines:
                        if line.strip().startswith('--') or line.strip().startswith('#'):
                            continue
                        if line.strip() and not line.strip().startswith('This') and not line.strip().startswith('The'):
                            sql_lines.append(line)
                        if ';' in line:
                            break
                    
                    sql_clean = '\n'.join(sql_lines).strip()
                    print(f"Extracted SQL:\n{sql_clean}")
                    
                    # Try to execute
                    try:
                        cursor.execute(sql_clean)
                        rows = cursor.fetchall()
                        print(f"✅ SQL EXECUTED SUCCESSFULLY: {len(rows)} rows")
                        if rows and len(rows) > 0:
                            print(f"Sample result: {rows[0]}")
                    except Exception as e:
                        print(f"❌ SQL EXECUTION ERROR: {str(e)[:200]}")
                        
            results.append({
                "query": test['query'],
                "category": test['category'],
                "has_sql": looks_like_sql,
                "response_length": len(response),
                "response_preview": response[:500]
            })
            
        else:
            print("No response received")
            
    except Exception as e:
        print(f"ERROR: {str(e)}")

# Summary
print("\n" + "="*80)
print("SUMMARY OF RESPONSE PATTERNS")
print("="*80)

sql_generated = sum(1 for r in results if r.get('has_sql', False))
total = len(results)

print(f"\nSQL Generation Rate: {sql_generated}/{total} ({sql_generated/total*100:.0f}%)")
print("\nBy Category:")
for r in results:
    status = "✅ SQL" if r.get('has_sql') else "❌ No SQL"
    print(f"  {status} - {r['category']}: \"{r['query']}\"")

# Save detailed results
with open('detailed_response_analysis.json', 'w') as f:
    json.dump(results, f, indent=2)

print("\n💾 Detailed results saved to detailed_response_analysis.json")

conn.close()