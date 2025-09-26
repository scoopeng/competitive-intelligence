#!/usr/bin/env python3
"""
Test if providing database context helps CORTEX.COMPLETE generate SQL
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
print("TESTING CONTEXT AWARENESS - DOES PROVIDING CONTEXT HELP?")
print("="*80)

# Test variations with increasing context
test_variations = [
    {
        "id": "CTX_001",
        "query": "How many customers do we have?",
        "description": "Pure natural language"
    },
    {
        "id": "CTX_002", 
        "query": "How many customers do we have in the TELCO_DATA table?",
        "description": "Natural + table name"
    },
    {
        "id": "CTX_003",
        "query": "Using the TELCO_DATA table in the TEST_DATA schema, how many customers do we have?",
        "description": "Natural + full context"
    },
    {
        "id": "CTX_004",
        "query": """Given a table TELCO_DATA with columns like CUSTOMERID, CHURN, MONTHLYCHARGES, etc.
        How many customers do we have?""",
        "description": "Natural + schema hints"
    },
    {
        "id": "CTX_005",
        "query": """Context: You have access to TELCO_DATA table.
        Task: Generate SQL to count how many customers we have.""",
        "description": "Explicit context + task"
    },
    {
        "id": "CTX_006",
        "query": "SELECT COUNT(*) FROM TELCO_DATA;",
        "description": "Direct SQL (control)"
    }
]

results = []

for test in test_variations:
    print(f"\n[{test['id']}] {test['description']}")
    print(f"Query: {test['query'][:80]}...")
    print("-"*50)
    
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
            
            # Check for SQL
            has_select = 'SELECT' in response.upper()
            has_from = 'FROM' in response.upper()
            has_telco = 'TELCO' in response.upper()
            
            print(f"Response characteristics:")
            print(f"  - Has SELECT: {has_select}")
            print(f"  - Has FROM: {has_from}")
            print(f"  - Mentions TELCO_DATA: {has_telco}")
            
            if has_select and has_from:
                print("✅ SQL GENERATED")
                
                # Try to extract and test
                sql_start = response.upper().find('SELECT')
                sql_portion = response[sql_start:]
                
                # Clean
                if '```' in sql_portion:
                    sql_portion = sql_portion.split('```')[0]
                if ';' in sql_portion:
                    sql_portion = sql_portion.split(';')[0] + ';'
                    
                sql_clean = sql_portion.strip()
                
                try:
                    cursor.execute(sql_clean)
                    rows = cursor.fetchone()
                    print(f"   EXECUTED: Result = {rows}")
                    success = True
                except Exception as e:
                    print(f"   EXECUTION ERROR: {str(e)[:100]}")
                    success = False
                    
                results.append({
                    "id": test['id'],
                    "description": test['description'],
                    "sql_generated": True,
                    "sql_executed": success,
                    "mentions_telco": has_telco
                })
            else:
                print("❌ NO SQL GENERATED")
                print(f"   Response type: {response[:100]}...")
                
                results.append({
                    "id": test['id'],
                    "description": test['description'],
                    "sql_generated": False,
                    "sql_executed": False,
                    "mentions_telco": has_telco
                })
                
    except Exception as e:
        print(f"ERROR: {str(e)[:100]}")
        results.append({
            "id": test['id'],
            "description": test['description'],
            "error": str(e)[:100]
        })

# Summary
print("\n" + "="*80)
print("CONTEXT AWARENESS RESULTS")
print("="*80)

print("\n| Context Level | SQL Generated | SQL Executed | Mentions Table |")
print("|---------------|---------------|--------------|----------------|")
for r in results:
    if 'error' not in r:
        sql_gen = "✅" if r['sql_generated'] else "❌"
        sql_exec = "✅" if r['sql_executed'] else "❌"
        mentions = "✅" if r['mentions_telco'] else "❌"
        print(f"| {r['description'][:25]:25} | {sql_gen:^13} | {sql_exec:^12} | {mentions:^14} |")

# Key finding
natural_success = sum(1 for r in results[:5] if r.get('sql_executed', False))
print(f"\nNatural language variations that worked: {natural_success}/5")

with open('context_awareness_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print("\n💾 Results saved to context_awareness_results.json")

conn.close()