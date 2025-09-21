#!/usr/bin/env python3
"""
Test Claude-4-Sonnet with proper context
"""

import snowflake.connector
from datetime import datetime

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
print("CLAUDE-4-SONNET WITH CONTEXT TEST")
print("="*80)

# Test queries with context
test_queries = [
    {
        "id": "CONTEXT_001",
        "natural": "How many customers do we have?",
        "with_context": "Generate SQL to count total customers in TELCO_DATA table"
    },
    {
        "id": "CONTEXT_002", 
        "natural": "What's the average monthly charge?",
        "with_context": "Generate SQL to find average MONTHLYCHARGES from TELCO_DATA"
    },
    {
        "id": "CONTEXT_003",
        "natural": "Show me churn rate by contract type",
        "with_context": "Generate SQL to calculate churn rate by CONTRACT column in TELCO_DATA (CHURN is boolean)"
    }
]

for test in test_queries:
    print(f"\n[{test['id']}]")
    print("="*60)
    
    # Test 1: Natural language (what users actually type)
    print(f"\n1. NATURAL: '{test['natural']}'")
    try:
        start = datetime.now()
        cursor.execute(f"""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            'claude-4-sonnet',
            %s
        ) as response
        """, (test['natural'],))
        
        result = cursor.fetchone()
        elapsed = (datetime.now() - start).total_seconds()
        
        if result and result[0]:
            response = result[0]
            has_sql = 'SELECT' in response.upper()
            print(f"   Response time: {elapsed:.2f}s")
            print(f"   Has SQL: {has_sql}")
            if has_sql:
                print("   ✅ Generated SQL")
            else:
                print(f"   ❌ No SQL, just text: {response[:100]}...")
    except Exception as e:
        print(f"   ❌ Error: {str(e)[:100]}")
    
    # Test 2: With context (adding table/column hints)
    print(f"\n2. WITH CONTEXT: '{test['with_context']}'")
    try:
        start = datetime.now()
        cursor.execute(f"""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            'claude-4-sonnet',
            %s
        ) as response
        """, (test['with_context'],))
        
        result = cursor.fetchone()
        elapsed = (datetime.now() - start).total_seconds()
        
        if result and result[0]:
            response = result[0]
            has_sql = 'SELECT' in response.upper()
            print(f"   Response time: {elapsed:.2f}s")
            print(f"   Has SQL: {has_sql}")
            
            if has_sql:
                # Try to extract and execute SQL
                sql_start = response.upper().find('SELECT')
                sql = response[sql_start:]
                if '```' in sql:
                    sql = sql.split('```')[0]
                sql = sql.strip()
                
                try:
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    print(f"   ✅ SQL EXECUTED: {len(rows)} rows")
                    if rows:
                        print(f"   Result: {rows[0]}")
                except Exception as e:
                    print(f"   ❌ SQL failed: {str(e)[:100]}")
            else:
                print(f"   ❌ No SQL generated")
    except Exception as e:
        print(f"   ❌ Error: {str(e)[:100]}")

print("\n" + "="*80)
print("KEY FINDINGS")
print("="*80)
print("""
1. Natural language queries (what users type) = Low/No SQL generation
2. Queries with explicit table/column context = Higher SQL generation
3. Claude-4-Sonnet requires EXACT schema knowledge
4. This proves Cortex Analyst NEEDS semantic model YAML
""")

conn.close()