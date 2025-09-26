#!/usr/bin/env python3
"""Quick focused test of key capabilities"""

import snowflake.connector
import json
from datetime import datetime
import time

# Azure Snowflake Configuration
SNOWFLAKE_ACCOUNT = 'rcdtonr-ji20455'
SNOWFLAKE_USER = 'bradtest'
SNOWFLAKE_PASSWORD = 'qMsGeKsE33NJeZp'
SNOWFLAKE_WAREHOUSE = 'COMPUTE_WH'
SNOWFLAKE_DATABASE = 'SCOOP_BENCHMARK'
SNOWFLAKE_SCHEMA = 'TEST_DATA'

# Key test queries - 2 from each critical category
KEY_TESTS = {
    "basic_aggregation": [
        "How many customers do we have?",
        "What is the total revenue?"
    ],
    "grouping": [
        "Show revenue by contract type",
        "Count customers by payment method"
    ],
    "filtering": [
        "Show customers with monthly charges over 100",
        "Show only senior citizens"
    ],
    "time_intelligence": [
        "Show month-over-month revenue growth",
        "Calculate running total of monthly charges"
    ],
    "calculated_metrics": [
        "Calculate the churn rate",
        "What's the average revenue per user?"
    ],
    "statistical": [
        "What's the correlation between tenure and monthly charges?",
        "Show standard deviation of monthly charges"
    ],
    "investigation": [
        "Why are customers churning?",
        "What drives customer lifetime value?"
    ],
    "visualization": [
        "Create a bar chart of revenue by service",
        "Show a pie chart of customer distribution"
    ]
}

def test_query(conn, query, category):
    """Test a single query"""
    try:
        cursor = conn.cursor()
        
        # Build prompt for SQL generation
        sql_query = f"""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            'llama3.1-70b',
            'Generate ONLY a SQL query for this question. No explanation needed.
            
            Question: {query}
            
            Table: TELCO_DATA with columns:
            CUSTOMERID, GENDER, SENIORCITIZEN, PARTNER, DEPENDENTS, TENURE,
            PHONESERVICE, MULTIPLELINES, INTERNETSERVICE, ONLINESECURITY,
            ONLINEBACKUP, DEVICEPROTECTION, TECHSUPPORT, STREAMINGTV,
            STREAMINGMOVIES, CONTRACT, PAPERLESSBILLING, PAYMENTMETHOD,
            MONTHLYCHARGES, TOTALCHARGES, CHURN
            
            SQL:'
        ) as response;
        """
        
        start = time.time()
        cursor.execute(sql_query)
        response = cursor.fetchone()[0]
        elapsed = time.time() - start
        
        # Extract SQL
        generated_sql = None
        if response and "SELECT" in response.upper():
            sql_start = response.upper().find("SELECT")
            generated_sql = response[sql_start:].strip()
            if ";" in generated_sql:
                generated_sql = generated_sql[:generated_sql.index(";")+1]
        
        # Test execution
        executes = False
        error = None
        if generated_sql:
            try:
                cursor.execute(generated_sql)
                cursor.fetchall()
                executes = True
            except Exception as e:
                error = str(e)[:100]
        
        cursor.close()
        
        return {
            "query": query,
            "category": category,
            "generated_sql": generated_sql,
            "executes": executes,
            "error": error,
            "time": elapsed
        }
    except Exception as e:
        return {
            "query": query,
            "category": category,
            "error": str(e)[:100],
            "executes": False
        }

def main():
    print("="*80)
    print("SNOWFLAKE CORTEX QUICK TEST - KEY CAPABILITIES")
    print("="*80)
    
    conn = snowflake.connector.connect(
        account=SNOWFLAKE_ACCOUNT,
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA
    )
    print("✅ Connected to Azure Snowflake\n")
    
    results = {}
    total_success = 0
    total_queries = 0
    
    for category, queries in KEY_TESTS.items():
        print(f"\nTesting {category.upper()}:")
        print("-" * 40)
        category_results = []
        
        for query in queries:
            print(f"  {query}")
            result = test_query(conn, query, category)
            category_results.append(result)
            total_queries += 1
            
            if result.get("executes"):
                print(f"    ✅ SUCCESS")
                total_success += 1
            else:
                print(f"    ❌ FAILED: {result.get('error', 'No SQL generated')}")
            
            time.sleep(0.5)  # Rate limit
        
        results[category] = category_results
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    
    print("\n| Category | Success Rate |")
    print("|----------|-------------|")
    
    for category, cat_results in results.items():
        success = sum(1 for r in cat_results if r.get("executes"))
        total = len(cat_results)
        rate = (success/total*100) if total > 0 else 0
        emoji = "✅" if rate > 70 else "⚠️" if rate > 30 else "❌"
        print(f"| {category:<20} | {rate:>5.0f}% {emoji} |")
    
    overall_rate = (total_success/total_queries*100) if total_queries > 0 else 0
    print(f"\nOVERALL: {overall_rate:.1f}% ({total_success}/{total_queries} queries)")
    
    # Save results
    with open('test_results/quick_test_results.json', 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print("\n📊 Results saved to test_results/quick_test_results.json")
    
    # Key findings
    if results.get("time_intelligence"):
        ti_success = sum(1 for r in results["time_intelligence"] if r.get("executes"))
        if ti_success == 0:
            print("\n❌ CRITICAL: Time intelligence completely failed (0% success)")
    
    if results.get("investigation"):
        inv_success = sum(1 for r in results["investigation"] if r.get("executes"))
        if inv_success == 0:
            print("❌ CRITICAL: Investigation queries completely failed (0% success)")
    
    conn.close()

if __name__ == "__main__":
    main()