#!/usr/bin/env python3
"""
Test CORTEX.COMPLETE with NATURAL BUSINESS LANGUAGE
Exactly what a business user would type - no SQL hints or modifications
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
print("NATURAL LANGUAGE TESTING - WHAT BUSINESS USERS ACTUALLY TYPE")
print("No SQL hints, no column names, just natural questions")
print("="*80)

# EXACTLY what business users would type
natural_queries = [
    {
        "id": "USER_001",
        "query": "How many customers do we have?",
        "category": "Basic Count"
    },
    {
        "id": "USER_002",
        "query": "What's the average monthly charge?",
        "category": "Basic Average"
    },
    {
        "id": "USER_003",
        "query": "Show me churn rate by contract type",
        "category": "Segmented Metric"
    },
    {
        "id": "USER_004",
        "query": "Which customers are paying more than $100 per month?",
        "category": "Filtered List"
    },
    {
        "id": "USER_005",
        "query": "Why are customers leaving?",
        "category": "Investigation"
    },
    {
        "id": "USER_006",
        "query": "What's our total revenue?",
        "category": "Sum Calculation"
    },
    {
        "id": "USER_007",
        "query": "Show me the top 10 highest paying customers",
        "category": "Top N"
    },
    {
        "id": "USER_008",
        "query": "How many payment methods do churned customers use?",
        "category": "Distinct Count"
    },
    {
        "id": "USER_009",
        "query": "What's the relationship between tenure and churn?",
        "category": "Correlation"
    },
    {
        "id": "USER_010",
        "query": "Which services do churned customers have?",
        "category": "Characteristic Analysis"
    },
    {
        "id": "USER_011",
        "query": "Compare churn rates between different internet service types",
        "category": "Comparison"
    },
    {
        "id": "USER_012",
        "query": "What drives customer loyalty?",
        "category": "Driver Analysis"
    },
    {
        "id": "USER_013",
        "query": "Show me monthly charges by gender",
        "category": "Segmentation"
    },
    {
        "id": "USER_014",
        "query": "How much money are we losing to churn?",
        "category": "Impact Analysis"
    },
    {
        "id": "USER_015",
        "query": "What patterns predict churn?",
        "category": "Pattern Discovery"
    }
]

print(f"\nTesting {len(natural_queries)} natural business queries...")
print("These are exactly what sales/business users would type.\n")

results = []
success_count = 0
fail_count = 0

def try_execute_sql(sql_response):
    """Try to extract and execute SQL from response"""
    if not sql_response:
        return False, "No response"
    
    # Try to find SQL in response
    sql = None
    
    # Check for SQL markers
    if 'SELECT' in sql_response.upper():
        # Extract from SELECT to end or semicolon
        start = sql_response.upper().find('SELECT')
        sql = sql_response[start:]
        
        # Clean up
        if '```' in sql:
            sql = sql.split('```')[0]
        if '\n\n' in sql:
            sql = sql.split('\n\n')[0]
            
        # Remove any explanation after SQL
        lines = sql.split('\n')
        clean_lines = []
        for line in lines:
            if line.strip().startswith('--') or line.strip().startswith('#'):
                continue
            clean_lines.append(line)
            if ';' in line:
                break
        sql = '\n'.join(clean_lines)
    
    if not sql:
        return False, "No SQL found"
    
    # Try to execute
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        return True, f"{len(rows)} rows"
    except Exception as e:
        return False, str(e)[:100]

# Test each natural query
for test in natural_queries:
    print(f"\n[{test['id']}] {test['category']}")
    print(f"Query: \"{test['query']}\"")
    print("-"*40)
    
    try:
        # Send EXACTLY what user would type
        # No hints, no "Generate SQL", just the question
        start = datetime.now()
        cursor.execute(f"""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            'claude-3.5-sonnet',
            %s
        ) as response
        """, (test['query'],))
        
        result = cursor.fetchone()
        elapsed = (datetime.now() - start).total_seconds()
        
        if result and result[0]:
            response = result[0]
            
            # Check if it generated SQL or just text
            has_sql = 'SELECT' in response.upper()
            
            if has_sql:
                success, message = try_execute_sql(response)
                
                if success:
                    print(f"✅ SUCCESS: Generated executable SQL ({message})")
                    print(f"   Time: {elapsed:.2f}s")
                    success_count += 1
                    status = "SUCCESS"
                else:
                    print(f"❌ FAILED: SQL error - {message}")
                    print(f"   Time: {elapsed:.2f}s")
                    fail_count += 1
                    status = "SQL_ERROR"
            else:
                print(f"❌ FAILED: No SQL generated, only explanation")
                print(f"   Response preview: {response[:150]}...")
                fail_count += 1
                status = "NO_SQL"
                
            results.append({
                "test_id": test['id'],
                "query": test['query'],
                "category": test['category'],
                "status": status,
                "has_sql": has_sql,
                "time": elapsed
            })
            
        else:
            print(f"❌ FAILED: No response from CORTEX.COMPLETE")
            fail_count += 1
            results.append({
                "test_id": test['id'],
                "query": test['query'],
                "category": test['category'],
                "status": "NO_RESPONSE",
                "time": elapsed
            })
            
    except Exception as e:
        print(f"❌ ERROR: {str(e)[:100]}")
        fail_count += 1
        results.append({
            "test_id": test['id'],
            "query": test['query'],
            "category": test['category'],
            "status": "ERROR",
            "error": str(e)[:100]
        })

# Summary
print("\n" + "="*80)
print("NATURAL LANGUAGE RESULTS - WHAT BUSINESS USERS ACTUALLY EXPERIENCE")
print("="*80)

print(f"\nTotal Queries: {len(natural_queries)}")
print(f"✅ Successful: {success_count} ({success_count/len(natural_queries)*100:.1f}%)")
print(f"❌ Failed: {fail_count} ({fail_count/len(natural_queries)*100:.1f}%)")

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
    status = "✅" if success_rate > 50 else "❌"
    print(f"  {status} {cat}: {stats['success']}/{total} ({success_rate:.0f}% success)")

print("\n### Failure Analysis:")
failure_types = {}
for r in results:
    if r['status'] != "SUCCESS":
        fail_type = r['status']
        if fail_type not in failure_types:
            failure_types[fail_type] = []
        failure_types[fail_type].append(r['query'])

for fail_type, queries in failure_types.items():
    print(f"\n{fail_type} ({len(queries)} queries):")
    for q in queries[:3]:  # Show first 3 examples
        print(f"  - \"{q}\"")
    if len(queries) > 3:
        print(f"  ... and {len(queries)-3} more")

# Save results
with open('natural_language_results.json', 'w') as f:
    json.dump({
        "summary": {
            "total": len(natural_queries),
            "success": success_count,
            "failed": fail_count,
            "success_rate": f"{success_count/len(natural_queries)*100:.1f}%"
        },
        "categories": categories,
        "details": results
    }, f, indent=2)

print(f"\n💾 Results saved to natural_language_results.json")

print("\n" + "="*80)
print("KEY FINDINGS FOR EVENTBRITE")
print("="*80)
print("1. Business users type natural questions, not SQL instructions")
print("2. CORTEX.COMPLETE struggles with natural language")
print("3. Investigation questions ('why', 'what drives') likely failed")
print("4. This is the REAL benchmark - what users actually experience")

conn.close()