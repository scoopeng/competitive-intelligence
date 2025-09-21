#!/usr/bin/env python3
"""
Test Cortex Analyst proper API with semantic model
"""

import snowflake.connector
import json
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
print("TESTING CORTEX ANALYST PROPER API")
print("="*80)

# Check for Cortex Analyst functions
print("\n1. Checking available Cortex functions...")
try:
    cursor.execute("SHOW FUNCTIONS LIKE '%CORTEX%'")
    functions = cursor.fetchall()
    if functions:
        print(f"Found {len(functions)} Cortex functions:")
        for f in functions[:10]:  # Show first 10
            print(f"  - {f[1]}")
except Exception as e:
    print(f"Error listing functions: {e}")

# Check for semantic models
print("\n2. Checking for semantic models...")
try:
    cursor.execute("SHOW STAGES")
    stages = cursor.fetchall()
    print(f"Found {len(stages)} stages")
    for s in stages:
        if 'SEMANTIC' in s[1].upper():
            print(f"  - {s[1]} (potential semantic model stage)")
except Exception as e:
    print(f"Error: {e}")

# Try different Cortex Analyst patterns
print("\n3. Testing Cortex Analyst patterns...")

test_patterns = [
    {
        "name": "CORTEX.ANALYST",
        "query": """
        SELECT SNOWFLAKE.CORTEX.ANALYST(
            'How many customers do we have?',
            '@SEMANTIC_MODELS/semantic_model.yaml'
        )
        """
    },
    {
        "name": "CORTEX.COMPLETE with semantic reference",
        "query": """
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            'claude-4-sonnet',
            CONCAT(
                'Using the semantic model for TELCO_DATA, ',
                'generate SQL to count total customers'
            )
        )
        """
    },
    {
        "name": "CORTEX.QUERY",
        "query": """
        SELECT SNOWFLAKE.CORTEX.QUERY(
            'How many customers are in TELCO_DATA?'
        )
        """
    }
]

for pattern in test_patterns:
    print(f"\nTesting: {pattern['name']}")
    print("-"*40)
    try:
        cursor.execute(pattern['query'])
        result = cursor.fetchone()
        if result:
            print(f"✅ Success!")
            print(f"   Result: {str(result[0])[:200]}...")
        else:
            print("❌ No result returned")
    except Exception as e:
        error_msg = str(e)
        if "Unknown function" in error_msg:
            print(f"❌ Function not available")
        elif "not authorized" in error_msg:
            print(f"❌ Not authorized")
        else:
            print(f"❌ Error: {error_msg[:150]}")

# Test with actual semantic model if view exists
print("\n4. Testing with semantic view (if exists)...")
try:
    # Check for semantic view
    cursor.execute("SHOW VIEWS")
    views = cursor.fetchall()
    semantic_views = [v for v in views if 'SEMANTIC' in v[1].upper() or 'ANALYST' in v[1].upper()]
    
    if semantic_views:
        print(f"Found semantic views: {[v[1] for v in semantic_views]}")
        
        # Test query against semantic view
        view_name = semantic_views[0][1]
        print(f"\nQuerying semantic view: {view_name}")
        
        test_queries = [
            "How many customers?",
            "Average monthly charges?",
            "Churn rate by contract type?"
        ]
        
        for q in test_queries:
            print(f"\nQuery: '{q}'")
            try:
                # Try using the view with CORTEX.COMPLETE
                prompt = f"""
                Using the {view_name} semantic view, generate and execute SQL for: {q}
                Return only the SQL statement.
                """
                
                cursor.execute(f"""
                SELECT SNOWFLAKE.CORTEX.COMPLETE(
                    'claude-4-sonnet',
                    %s
                )
                """, (prompt,))
                
                result = cursor.fetchone()
                if result and result[0]:
                    response = result[0]
                    if 'SELECT' in response.upper():
                        print("✅ SQL generated")
                    else:
                        print("❌ No SQL in response")
                        
            except Exception as e:
                print(f"❌ Error: {str(e)[:100]}")
    else:
        print("No semantic views found")
        
except Exception as e:
    print(f"Error checking views: {e}")

print("\n" + "="*80)
print("CONCLUSIONS")
print("="*80)
print("""
Based on testing:
1. CORTEX.ANALYST function may not be available in this account
2. CORTEX.COMPLETE is the primary function available
3. Semantic model must be referenced explicitly in prompts
4. Success depends on providing table/column context
""")

conn.close()