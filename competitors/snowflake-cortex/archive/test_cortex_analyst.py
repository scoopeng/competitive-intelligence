#!/usr/bin/env python3
"""
Test Cortex Analyst vs Scoop Query JSON
This uses the REAL Cortex Analyst API (with Claude/GPT-4)
"""

import snowflake.connector
import requests
import json
import yaml
from datetime import datetime
import sys

# Configuration - UPDATE THESE
SNOWFLAKE_ACCOUNT = 'toajlpe-nfb33705'  # Working format!
SNOWFLAKE_USER = 'bradscoop'
SNOWFLAKE_PASSWORD = 'D6c2BmtJWPy3dM7'
SNOWFLAKE_WAREHOUSE = 'COMPUTE_WH'
SNOWFLAKE_DATABASE = 'SCOOP_BENCHMARK'
SNOWFLAKE_SCHEMA = 'TEST_DATA'

def connect_to_snowflake():
    """Establish Snowflake connection"""
    try:
        conn = snowflake.connector.connect(
            account=SNOWFLAKE_ACCOUNT,
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            warehouse=SNOWFLAKE_WAREHOUSE,
            database=SNOWFLAKE_DATABASE,
            schema=SNOWFLAKE_SCHEMA
        )
        print("✅ Connected to Snowflake")
        return conn
    except Exception as e:
        print(f"❌ Failed to connect: {e}")
        sys.exit(1)

def test_cortex_analyst(conn, semantic_model_path, query):
    """Call Cortex Analyst API with a query"""
    
    # Read semantic model
    with open(semantic_model_path, 'r') as f:
        semantic_model = yaml.safe_load(f)
    
    # Get auth token from connection
    token = conn.rest.token if hasattr(conn, 'rest') else None
    
    # Construct API URL
    api_url = f"https://{SNOWFLAKE_ACCOUNT}.snowflakecomputing.com/api/v2/cortex/analyst/message"
    
    # Headers
    headers = {
        'Authorization': f'Snowflake Token="{token}"',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    # Request body
    body = {
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ],
        "semantic_model": semantic_model
    }
    
    # Make request
    try:
        response = requests.post(api_url, headers=headers, json=body)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Status {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": str(e)}

def run_test_suite():
    """Run all test queries"""
    
    # Connect
    conn = connect_to_snowflake()
    
    # Test queries matching Scoop's test suite
    test_cases = [
        {
            "id": "TEST_001",
            "category": "Basic Aggregation",
            "query": "What is the total number of customers?",
            "scoop_json_lines": 8,
            "expected_sql_complexity": "Simple SELECT COUNT"
        },
        {
            "id": "TEST_002", 
            "category": "Basic Aggregation",
            "query": "What is the average monthly charge?",
            "scoop_json_lines": 10,
            "expected_sql_complexity": "Simple SELECT AVG"
        },
        {
            "id": "TEST_003",
            "category": "Grouped Analysis",
            "query": "Show churn rate by contract type",
            "scoop_json_lines": 15,
            "expected_sql_complexity": "GROUP BY with calculated percentage"
        },
        {
            "id": "TEST_004",
            "category": "Complex Filter",
            "query": "Show customers with high monthly charges (over 100) who churned",
            "scoop_json_lines": 12,
            "expected_sql_complexity": "WHERE with multiple conditions"
        },
        {
            "id": "TEST_005",
            "category": "Multi-Dimensional",
            "query": "Which combination of contract type and payment method has the highest churn rate?",
            "scoop_json_lines": 25,
            "expected_sql_complexity": "Multiple GROUP BY with HAVING"
        },
        {
            "id": "TEST_006",
            "category": "Complex Calculation",
            "query": "Calculate customer lifetime value as monthly charges times tenure divided by number of tickets plus one",
            "scoop_json_lines": 18,
            "expected_sql_complexity": "Complex arithmetic with NULL handling"
        },
        {
            "id": "TEST_007",
            "category": "Subquery Required",
            "query": "Show customers from the top 3 contracts by customer count",
            "scoop_json_lines": 20,
            "expected_sql_complexity": "Subquery or CTE required"
        },
        {
            "id": "TEST_008",
            "category": "Why Question",
            "query": "Why are customers churning?",
            "scoop_json_lines": 50,  # Multi-step reasoning in Scoop
            "expected_sql_complexity": "Cannot answer with single SQL"
        },
        {
            "id": "TEST_009",
            "category": "Correlation Analysis",
            "query": "What factors correlate most strongly with churn?",
            "scoop_json_lines": 45,  # ML analysis in Scoop
            "expected_sql_complexity": "Would need complex correlation SQL"
        },
        {
            "id": "TEST_010",
            "category": "Trend Analysis", 
            "query": "How does churn rate change with tenure?",
            "scoop_json_lines": 22,
            "expected_sql_complexity": "GROUP BY with ordering"
        }
    ]
    
    # Results storage
    results = []
    
    print("\n" + "="*80)
    print("CORTEX ANALYST vs SCOOP COMPARISON TEST")
    print("="*80)
    
    for test in test_cases:
        print(f"\n📊 {test['id']}: {test['category']}")
        print(f"❓ Query: {test['query']}")
        print("-"*40)
        
        # Call Cortex Analyst
        start_time = datetime.now()
        response = test_cortex_analyst(conn, 'semantic_model.yaml', test['query'])
        elapsed = (datetime.now() - start_time).total_seconds()
        
        if 'error' in response:
            print(f"❌ Error: {response['error']}")
            sql = None
            sql_lines = 0
            success = False
        else:
            sql = response.get('sql', 'No SQL returned')
            sql_lines = len(sql.split('\n')) if sql else 0
            success = True
            
            print(f"✅ SQL Generated ({sql_lines} lines, {elapsed:.2f}s):")
            print(sql[:500] + "..." if len(sql) > 500 else sql)
        
        # Compare with Scoop
        print(f"\n📈 Comparison:")
        print(f"   Scoop Query JSON: {test['scoop_json_lines']} lines")
        print(f"   Cortex SQL: {sql_lines} lines")
        print(f"   Complexity Ratio: {sql_lines/test['scoop_json_lines']:.1f}x")
        
        # Store result
        results.append({
            "test_id": test['id'],
            "category": test['category'],
            "query": test['query'],
            "cortex_success": success,
            "cortex_sql_lines": sql_lines,
            "scoop_json_lines": test['scoop_json_lines'],
            "complexity_ratio": sql_lines/test['scoop_json_lines'] if test['scoop_json_lines'] > 0 else 0,
            "execution_time": elapsed,
            "sql": sql
        })
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY RESULTS")
    print("="*80)
    
    successful = sum(1 for r in results if r['cortex_success'])
    print(f"\n✅ Successful: {successful}/{len(results)}")
    print(f"❌ Failed: {len(results)-successful}/{len(results)}")
    
    avg_ratio = sum(r['complexity_ratio'] for r in results) / len(results)
    print(f"📊 Average Complexity Ratio: {avg_ratio:.1f}x more SQL lines than Query JSON")
    
    # Save results
    with open('cortex_analyst_test_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n💾 Results saved to cortex_analyst_test_results.json")
    
    conn.close()

if __name__ == "__main__":
    print("🚀 Starting Cortex Analyst Testing")
    print("Make sure to update the configuration variables in this script!")
    print("")
    
    # Check if semantic model exists
    import os
    if not os.path.exists('semantic_model.yaml'):
        print("❌ semantic_model.yaml not found!")
        print("Create it first using the provided template")
        sys.exit(1)
    
    run_test_suite()