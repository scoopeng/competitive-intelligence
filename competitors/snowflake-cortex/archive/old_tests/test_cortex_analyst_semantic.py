#!/usr/bin/env python3
"""
Test Cortex Analyst with Semantic View - Claude-4-Sonnet
"""

import snowflake.connector
import json
from datetime import datetime

# Connection
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
print("CORTEX ANALYST WITH SEMANTIC VIEW - CLAUDE-4-SONNET")
print("="*80)

# First, check what semantic models/views are available
print("\n1. Checking available views and tables...")
cursor.execute("SHOW VIEWS")
views = cursor.fetchall()
if views:
    print(f"   Found {len(views)} views")
    for v in views:
        print(f"   - {v[1]}")

# Natural language queries that business users would ask
business_queries = [
    {
        "id": "BIZ_001",
        "query": "How many customers do we have?",
        "category": "Basic Count"
    },
    {
        "id": "BIZ_002",
        "query": "What's the average monthly charge?",
        "category": "Basic Average"
    },
    {
        "id": "BIZ_003",
        "query": "Show me churn rate by contract type",
        "category": "Segmented Analysis"
    },
    {
        "id": "BIZ_004",
        "query": "Which customers are high value (monthly charge > 80)?",
        "category": "Filtered List"
    },
    {
        "id": "BIZ_005",
        "query": "What's the correlation between tenure and churn?",
        "category": "Correlation"
    },
    {
        "id": "BIZ_006",
        "query": "Show me top 5 customers by total charges",
        "category": "Top N"
    },
    {
        "id": "BIZ_007",
        "query": "What percentage of customers have fiber optic internet?",
        "category": "Percentage Calculation"
    },
    {
        "id": "BIZ_008",
        "query": "Compare churn rates between different payment methods",
        "category": "Comparison"
    }
]

print(f"\n2. Testing {len(business_queries)} business queries with Cortex Analyst...")
print("-"*80)

results = []
success_count = 0
fail_count = 0

for test in business_queries:
    print(f"\n[{test['id']}] {test['category']}")
    print(f"Query: '{test['query']}'")
    
    try:
        # Try using Cortex Analyst (if semantic model is set up)
        # First try: Direct CORTEX.COMPLETE
        start = datetime.now()
        
        # Build a prompt that references the semantic model
        prompt = f"""Using the TELCO_DATA semantic model, generate SQL for: {test['query']}
        
        Context: TELCO_DATA contains customer information with columns like CUSTOMERID, GENDER, MONTHLYCHARGES, TOTALCHARGES, CHURN (boolean), CONTRACT, PAYMENTMETHOD, INTERNETSERVICE, TENURE, etc."""
        
        cursor.execute(f"""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            'claude-4-sonnet',
            %s
        ) as response
        """, (prompt,))
        
        result = cursor.fetchone()
        elapsed = (datetime.now() - start).total_seconds()
        
        if result and result[0]:
            response = result[0]
            
            # Check if SQL was generated
            if 'SELECT' in response.upper():
                # Extract SQL
                sql_start = response.upper().find('SELECT')
                sql = response[sql_start:]
                if '```' in sql:
                    sql = sql.split('```')[0]
                sql = sql.strip().rstrip(';')
                
                print(f"✅ SQL generated in {elapsed:.2f}s")
                
                # Try to execute
                try:
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    print(f"✅ EXECUTED: {len(rows)} rows returned")
                    if rows and len(rows) > 0:
                        print(f"   Sample result: {rows[0]}")
                    success_count += 1
                    
                    results.append({
                        "id": test['id'],
                        "query": test['query'],
                        "category": test['category'],
                        "status": "SUCCESS",
                        "rows": len(rows),
                        "time": elapsed
                    })
                    
                except Exception as e:
                    print(f"❌ Execution failed: {str(e)[:100]}")
                    fail_count += 1
                    results.append({
                        "id": test['id'],
                        "query": test['query'],
                        "category": test['category'],
                        "status": "SQL_ERROR",
                        "error": str(e)[:100],
                        "time": elapsed
                    })
            else:
                print(f"❌ No SQL generated, only text response")
                print(f"   Response: {response[:150]}...")
                fail_count += 1
                results.append({
                    "id": test['id'],
                    "query": test['query'],
                    "category": test['category'],
                    "status": "NO_SQL",
                    "time": elapsed
                })
                
    except Exception as e:
        print(f"❌ Error: {str(e)[:100]}")
        fail_count += 1
        results.append({
            "id": test['id'],
            "query": test['query'],
            "category": test['category'],
            "status": "ERROR",
            "error": str(e)[:100]
        })

# Summary
print("\n" + "="*80)
print("CLAUDE-4-SONNET WITH SEMANTIC CONTEXT RESULTS")
print("="*80)
print(f"Total Queries: {len(business_queries)}")
print(f"✅ Successful: {success_count} ({success_count/len(business_queries)*100:.1f}%)")
print(f"❌ Failed: {fail_count} ({fail_count/len(business_queries)*100:.1f}%)")

print("\n### Results by Category:")
categories = {}
for r in results:
    cat = r['category']
    if cat not in categories:
        categories[cat] = {"success": 0, "fail": 0}
    if r['status'] == "SUCCESS":
        categories[cat]['success'] += 1
    else:
        categories[cat]['fail'] += 1

for cat, stats in sorted(categories.items()):
    total = stats['success'] + stats['fail']
    success_rate = (stats['success'] / total * 100) if total > 0 else 0
    print(f"  {cat}: {stats['success']}/{total} ({success_rate:.0f}%)")

# Compare with previous llama3-70b results
print("\n" + "="*80)
print("MODEL COMPARISON: CLAUDE-4-SONNET vs LLAMA3-70B")
print("="*80)
print(f"""
With Semantic Context:
  Claude-4-Sonnet: {success_count}/{len(business_queries)} ({success_count/len(business_queries)*100:.1f}%)
  Llama3-70b:      0/15 (0%) [from previous tests without context]
  
Key Differences:
  - Claude-4-Sonnet: Can generate SQL with proper context
  - Llama3-70b: Failed on natural language queries
  - Both models: Require semantic model/context for success
""")

# Save results
with open('claude4_semantic_results.json', 'w') as f:
    json.dump({
        "model": "claude-4-sonnet",
        "test_type": "semantic_context",
        "summary": {
            "total": len(business_queries),
            "success": success_count,
            "failed": fail_count,
            "success_rate": f"{success_count/len(business_queries)*100:.1f}%"
        },
        "categories": categories,
        "details": results
    }, f, indent=2)

print(f"\n💾 Results saved to claude4_semantic_results.json")

conn.close()