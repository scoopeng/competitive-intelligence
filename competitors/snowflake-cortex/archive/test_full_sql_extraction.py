#!/usr/bin/env python3
"""
Extract and analyze the EXACT SQL that CORTEX.COMPLETE generates
"""

import snowflake.connector
import json
import re

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
print("FULL SQL EXTRACTION - WHAT EXACTLY IS BEING GENERATED?")
print("="*80)

# First, get the actual schema
print("\nActual TELCO_DATA schema:")
cursor.execute("DESCRIBE TABLE TELCO_DATA")
columns = cursor.fetchall()
print("Columns: ", [col[0] for col in columns[:10]])  # First 10 columns

# Test queries that should generate SQL
test_queries = [
    {
        "id": "SQL_001",
        "query": "How many rows are in the TELCO_DATA table?",
    },
    {
        "id": "SQL_002",
        "query": "What's the average MONTHLYCHARGES in TELCO_DATA table?",
    },
    {
        "id": "SQL_003",
        "query": "Show me churn rate from TELCO_DATA table",
    },
    {
        "id": "SQL_004",
        "query": "Count distinct PAYMENTMETHOD values in TELCO_DATA table",
    },
    {
        "id": "SQL_005",
        "query": f"Using TELCO_DATA table with columns {[col[0] for col in columns[:5]]}, count the rows",
    }
]

def extract_sql(response):
    """Extract ALL SQL from response"""
    sql_statements = []
    
    # Method 1: Look for SELECT statements
    if 'SELECT' in response.upper():
        # Find all SELECT statements
        parts = response.split('SELECT')
        for i, part in enumerate(parts[1:], 1):
            # Reconstruct SELECT statement
            sql = 'SELECT' + part
            
            # Find end of SQL (various markers)
            end_markers = [';', '```', '\n\n', 'This', 'The query', 'Note:']
            min_end = len(sql)
            for marker in end_markers:
                if marker in sql:
                    min_end = min(min_end, sql.find(marker))
            
            sql = sql[:min_end].strip()
            if 'FROM' in sql.upper():
                sql_statements.append(sql)
    
    return sql_statements

results = []

for test in test_queries:
    print(f"\n{'='*60}")
    print(f"[{test['id']}] Query: {test['query']}")
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
            print(response[:500])
            if len(response) > 500:
                print("...")
            
            # Extract SQL
            sql_statements = extract_sql(response)
            
            if sql_statements:
                print(f"\nEXTRACTED SQL STATEMENTS ({len(sql_statements)}):")
                for i, sql in enumerate(sql_statements, 1):
                    print(f"\nStatement {i}:")
                    print(sql)
                    
                    # Try to execute
                    try:
                        cursor.execute(sql)
                        rows = cursor.fetchall()
                        print(f"✅ EXECUTED: {len(rows)} rows")
                        if rows and len(rows) <= 3:
                            print(f"   Result: {rows}")
                    except Exception as e:
                        print(f"❌ ERROR: {e}")
                        
                        # Analyze the error
                        error_str = str(e)
                        if 'invalid identifier' in error_str.lower():
                            # Extract the bad column name
                            match = re.search(r"invalid identifier '([^']+)'", error_str)
                            if match:
                                bad_col = match.group(1)
                                print(f"   → Model guessed column: '{bad_col}'")
                                print(f"   → Actual columns include: {[col[0] for col in columns if bad_col[:3].upper() in col[0]]}")
                        
                results.append({
                    "query": test['query'],
                    "sql_generated": True,
                    "sql_count": len(sql_statements),
                    "any_executed": any([True for sql in sql_statements if try_execute(cursor, sql)])
                })
            else:
                print("\n❌ NO SQL FOUND IN RESPONSE")
                results.append({
                    "query": test['query'],
                    "sql_generated": False
                })
                
    except Exception as e:
        print(f"ERROR: {str(e)}")

def try_execute(cursor, sql):
    try:
        cursor.execute(sql)
        return True
    except:
        return False

# Summary
print("\n" + "="*80)
print("SQL GENERATION ANALYSIS")
print("="*80)

successful = sum(1 for r in results if r.get('any_executed', False))
generated = sum(1 for r in results if r.get('sql_generated', False))

print(f"\nSQL Generation: {generated}/{len(results)} queries generated SQL")
print(f"SQL Execution: {successful}/{generated} generated SQL executed successfully")
print("\nKey Issue: Column name guessing - model doesn't know actual schema")

conn.close()