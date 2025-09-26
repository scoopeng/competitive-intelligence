#!/usr/bin/env python3
"""Quick connection test"""

import snowflake.connector
import sys

# Azure Snowflake Configuration
SNOWFLAKE_ACCOUNT = 'rcdtonr-ji20455'
SNOWFLAKE_USER = 'bradtest'
SNOWFLAKE_PASSWORD = 'qMsGeKsE33NJeZp'
SNOWFLAKE_WAREHOUSE = 'COMPUTE_WH'
SNOWFLAKE_DATABASE = 'SCOOP_BENCHMARK'
SNOWFLAKE_SCHEMA = 'TEST_DATA'

print("Testing connection to Azure Snowflake...")
print(f"Account: {SNOWFLAKE_ACCOUNT}")

try:
    conn = snowflake.connector.connect(
        account=SNOWFLAKE_ACCOUNT,
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA
    )
    print("✅ Connected successfully!")
    
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM TELCO_DATA")
    count = cursor.fetchone()[0]
    print(f"✅ TELCO_DATA table has {count} rows")
    
    # Test CORTEX.COMPLETE
    print("\nTesting CORTEX.COMPLETE with llama3.1-70b...")
    cursor.execute("""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            'llama3.1-70b',
            'What is 2+2?'
        )
    """)
    result = cursor.fetchone()[0]
    print(f"✅ Model responded: {result[:100]}...")
    
    conn.close()
    print("\n✅ All tests passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)