#!/usr/bin/env python3
"""
Debug Cortex Analyst API issues
"""

import snowflake.connector
import requests
import json
import yaml

# Configuration
SNOWFLAKE_ACCOUNT = 'toajlpe-nfb33705'
SNOWFLAKE_USER = 'bradscoop'
SNOWFLAKE_PASSWORD = 'D6c2BmtJWPy3dM7'
SNOWFLAKE_WAREHOUSE = 'COMPUTE_WH'
SNOWFLAKE_DATABASE = 'SCOOP_BENCHMARK'
SNOWFLAKE_SCHEMA = 'TEST_DATA'

print("Connecting to Snowflake...")
conn = snowflake.connector.connect(
    account=SNOWFLAKE_ACCOUNT,
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    warehouse=SNOWFLAKE_WAREHOUSE,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA
)
print("✅ Connected")

# Load semantic model
print("\nLoading semantic model...")
with open('semantic_model.yaml', 'r') as f:
    semantic_model = yaml.safe_load(f)
print(f"✅ Loaded semantic model with {len(semantic_model.get('semantic_model', {}).get('tables', []))} tables")

# Try different API approaches
print("\n" + "="*60)
print("TESTING DIFFERENT API APPROACHES")
print("="*60)

# Test 1: Simple query with full semantic model
print("\n1. Testing with full semantic model...")
api_url = f"https://{SNOWFLAKE_ACCOUNT}.snowflakecomputing.com/api/v2/cortex/analyst/message"
token = conn.rest.token if hasattr(conn, 'rest') else None

headers = {
    'Authorization': f'Snowflake Token="{token}"',
    'Content-Type': 'application/json',
}

body = {
    "messages": [{"role": "user", "content": "What is the total number of customers?"}],
    "semantic_model": semantic_model
}

response = requests.post(api_url, headers=headers, json=body)
print(f"Response Status: {response.status_code}")
print(f"Response: {response.text[:500]}")

# Test 2: Try with simplified semantic model
print("\n2. Testing with minimal semantic model...")
minimal_model = {
    "name": "test_model",
    "tables": [{
        "name": "TELCO_DATA",
        "database": "SCOOP_BENCHMARK",
        "schema": "TEST_DATA"
    }]
}

body2 = {
    "messages": [{"role": "user", "content": "SELECT COUNT(*) FROM TELCO_DATA"}],
    "semantic_model": minimal_model
}

response2 = requests.post(api_url, headers=headers, json=body2)
print(f"Response Status: {response2.status_code}")
print(f"Response: {response2.text[:500]}")

# Test 3: Try using CORTEX.COMPLETE instead
print("\n3. Testing CORTEX.COMPLETE function...")
cursor = conn.cursor()
try:
    cursor.execute("""
    SELECT SNOWFLAKE.CORTEX.COMPLETE(
        'llama3-70b',
        'Generate SQL for TELCO_DATA table: What is the total number of rows?'
    ) as generated_sql
    """)
    result = cursor.fetchone()
    print(f"✅ COMPLETE function worked!")
    print(f"Generated SQL: {result[0]}")
except Exception as e:
    print(f"❌ COMPLETE failed: {str(e)[:200]}")

# Test 4: Check if Cortex Analyst is even available
print("\n4. Checking Cortex functions availability...")
try:
    cursor.execute("SHOW FUNCTIONS LIKE '%CORTEX%' IN SCHEMA SNOWFLAKE.CORTEX")
    functions = cursor.fetchall()
    print(f"Found {len(functions)} Cortex functions")
    for func in functions[:5]:
        print(f"  - {func[1]}")
except Exception as e:
    print(f"❌ Error: {e}")

# Test 5: Try Cortex Search instead (might be what's available)
print("\n5. Testing if this is actually Cortex Search...")
try:
    # Cortex Search has different API
    search_url = f"https://{SNOWFLAKE_ACCOUNT}.snowflakecomputing.com/api/v2/cortex/search"
    search_body = {
        "query": "customers",
        "database": "SCOOP_BENCHMARK",
        "schema": "TEST_DATA"
    }
    response3 = requests.post(search_url, headers=headers, json=search_body)
    print(f"Search Response: {response3.status_code}")
    print(f"Response: {response3.text[:200]}")
except Exception as e:
    print(f"❌ Search API error: {e}")

conn.close()

print("\n" + "="*60)
print("DIAGNOSIS")
print("="*60)

if response.status_code == 400:
    print("❌ 400 Bad Request means:")
    print("   1. Cortex Analyst might not be enabled on this account")
    print("   2. The semantic model format might be wrong")
    print("   3. The API endpoint might have changed")
    print("   4. Trial accounts might not have full Cortex Analyst access")
elif response.status_code == 404:
    print("❌ 404 Not Found means:")
    print("   1. The API endpoint doesn't exist")
    print("   2. Cortex Analyst isn't available in this region")
elif response.status_code == 401:
    print("❌ 401 Unauthorized means:")
    print("   1. Authentication token issue")
    print("   2. Permissions not set correctly")

print("\nRECOMMENDATION:")
print("Try creating a Streamlit app in Snowsight instead of using REST API")
print("Or use CORTEX.COMPLETE which seems to be available")