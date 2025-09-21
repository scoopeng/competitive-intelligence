#!/usr/bin/env python3
"""
Test Azure Snowflake connection and available models
"""

import snowflake.connector
import json

# Azure connection from URL: https://app.snowflake.com/rcdtonr/ji20455
print("Testing Azure Snowflake connection...")
print("Account: rcdtonr-ji20455")

try:
    conn = snowflake.connector.connect(
        account='rcdtonr-ji20455',  # Azure account format
        user='bradtest',
        password='qMsGeKsE33NJeZp',
        warehouse='COMPUTE_WH',
        database='SCOOP_BENCHMARK',
        schema='TEST_DATA'
    )
    cursor = conn.cursor()
    
    print("✅ Connection successful!")
    
    # Test database access
    cursor.execute("SELECT CURRENT_DATABASE(), CURRENT_SCHEMA(), CURRENT_WAREHOUSE()")
    result = cursor.fetchone()
    print(f"Database: {result[0]}")
    print(f"Schema: {result[1]}")
    print(f"Warehouse: {result[2]}")
    
    # Check tables
    cursor.execute("SHOW TABLES IN SCHEMA")
    tables = cursor.fetchall()
    print(f"\nAvailable tables: {len(tables)}")
    for table in tables[:5]:
        print(f"  - {table[1]}")
    
    # Test CORTEX.COMPLETE availability and models
    print("\nTesting CORTEX.COMPLETE models...")
    
    # Try different model names
    models_to_test = [
        'claude-4-sonnet',
        'claude-4-sonnet',
        'claude-3-sonnet',
        'gpt-5',
        'gpt-4',
        'llama3.1-70b',
        'llama3-70b',
        'mistral-large2'
    ]
    
    for model in models_to_test:
        try:
            query = f"""
            SELECT SNOWFLAKE.CORTEX.COMPLETE(
                '{model}',
                'What is 2+2?'
            ) as response
            """
            cursor.execute(query)
            response = cursor.fetchone()[0]
            print(f"✅ {model}: Available (response: {response[:50]}...)")
        except Exception as e:
            if "Unknown model" in str(e):
                print(f"❌ {model}: Not available")
            else:
                print(f"❌ {model}: Error - {str(e)[:100]}")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"❌ Connection failed: {e}")
    import traceback
    traceback.print_exc()