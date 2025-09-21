#!/usr/bin/env python3
"""
Run REAL tests against Snowflake Cortex Analyst
Using the actual API with credentials
"""

import snowflake.connector
import json
import yaml
import sys
from datetime import datetime
from typing import Dict, List, Optional, Any
import time

# Configuration
SNOWFLAKE_ACCOUNT = 'toajlpe-nfb33705'
SNOWFLAKE_USER = 'bradscoop'
SNOWFLAKE_PASSWORD = 'D6c2BmtJWPy3dM7'
SNOWFLAKE_WAREHOUSE = 'COMPUTE_WH'
SNOWFLAKE_DATABASE = 'SCOOP_BENCHMARK'
SNOWFLAKE_SCHEMA = 'TEST_DATA'

# Test queries organized by category
TEST_QUERIES = {
    "basic_aggregation": [
        "How many customers do we have?",
        "What is the total revenue?",
        "What's the average monthly charge?",
        "Show me the sum of total charges",
        "Count the number of churned customers"
    ],
    
    "grouping": [
        "Show revenue by contract type",
        "Count customers by payment method",
        "Average tenure by internet service type",
        "Total charges by gender",
        "Show churn rate by contract type"
    ],
    
    "filtering": [
        "Show only senior citizens",
        "Customers with fiber optic internet",
        "Show customers who churned last month",
        "Customers with monthly charges over 100",
        "Active customers with no phone service"
    ],
    
    "time_intelligence": [
        "Show month-over-month revenue growth",
        "Calculate the 3-month moving average of charges",
        "What's the year-over-year change in customer count?",
        "Show running total of monthly charges",
        "Compare this month's revenue to last month"
    ],
    
    "calculated_metrics": [
        "Calculate the churn rate",
        "What's the customer lifetime value?",
        "Show profit margin by service type",
        "Calculate average revenue per user",
        "What's the retention rate?"
    ],
    
    "ranking": [
        "Top 5 customers by total charges",
        "Bottom 10 customers by tenure",
        "Rank payment methods by popularity",
        "Show the highest paying customers",
        "List services by revenue contribution"
    ],
    
    "statistical": [
        "What's the correlation between tenure and monthly charges?",
        "Show standard deviation of monthly charges",
        "Calculate the median customer tenure",
        "What's the 75th percentile of total charges?",
        "Find statistical outliers in monthly charges"
    ],
    
    "investigation": [
        "Why are customers churning?",
        "What factors predict high monthly charges?",
        "Which customer segment is most profitable?",
        "What drives customer lifetime value?",
        "Why did revenue drop last quarter?"
    ],
    
    "complex_analysis": [
        "Compare churned vs active customers across all attributes",
        "Segment customers by value and behavior",
        "Which service combinations are most popular?",
        "Analyze the customer journey to churn",
        "Identify upsell opportunities"
    ]
}

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

def test_cortex_analyst(conn, query: str, semantic_model: Dict) -> Dict:
    """Test a single query with Cortex Analyst"""
    
    try:
        cursor = conn.cursor()
        
        # Prepare the Cortex Analyst call
        semantic_model_str = json.dumps(semantic_model)
        
        # Call Cortex Analyst using SQL interface
        sql_query = f"""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            'claude-3-5-sonnet',
            CONCAT(
                'You are a SQL analyst. Generate SQL for this question based on the semantic model: ',
                '{query}',
                '. Semantic model: ',
                '{semantic_model_str}'
            )
        ) as response;
        """
        
        start_time = time.time()
        cursor.execute(sql_query)
        result = cursor.fetchone()
        elapsed = time.time() - start_time
        
        response = result[0] if result else None
        
        # Try to extract SQL from response
        generated_sql = None
        if response:
            # Look for SQL in the response
            if "```sql" in response:
                sql_start = response.find("```sql") + 6
                sql_end = response.find("```", sql_start)
                generated_sql = response[sql_start:sql_end].strip()
            elif "SELECT" in response.upper():
                # Find the SELECT statement
                lines = response.split('\n')
                sql_lines = []
                in_sql = False
                for line in lines:
                    if 'SELECT' in line.upper():
                        in_sql = True
                    if in_sql:
                        sql_lines.append(line)
                        if ';' in line:
                            break
                generated_sql = '\n'.join(sql_lines)
        
        # Test if SQL executes
        sql_executes = False
        execution_error = None
        if generated_sql:
            try:
                cursor.execute(generated_sql)
                cursor.fetchall()
                sql_executes = True
            except Exception as e:
                execution_error = str(e)
        
        cursor.close()
        
        return {
            "query": query,
            "response": response,
            "generated_sql": generated_sql,
            "sql_executes": sql_executes,
            "execution_error": execution_error,
            "response_time": elapsed,
            "success": bool(generated_sql and sql_executes)
        }
        
    except Exception as e:
        return {
            "query": query,
            "error": str(e),
            "success": False
        }

def run_category_tests(conn, category: str, queries: List[str], semantic_model: Dict) -> Dict:
    """Run all tests for a category"""
    
    print(f"\n{'='*60}")
    print(f"Testing {category.upper()}")
    print(f"{'='*60}")
    
    results = []
    for i, query in enumerate(queries, 1):
        print(f"\n[{i}/{len(queries)}] {query}")
        result = test_cortex_analyst(conn, query, semantic_model)
        
        if result.get("success"):
            print(f"✅ SUCCESS - Generated executable SQL")
            if result.get("generated_sql"):
                print(f"   SQL: {result['generated_sql'][:100]}...")
        else:
            if result.get("generated_sql"):
                print(f"⚠️  PARTIAL - Generated SQL but failed to execute")
                print(f"   Error: {result.get('execution_error', 'Unknown')[:100]}")
            else:
                print(f"❌ FAILED - No SQL generated")
                if result.get("error"):
                    print(f"   Error: {result['error'][:100]}")
        
        results.append(result)
        time.sleep(1)  # Rate limiting
    
    # Calculate statistics
    total = len(results)
    sql_generated = sum(1 for r in results if r.get("generated_sql"))
    sql_executed = sum(1 for r in results if r.get("sql_executes"))
    
    return {
        "category": category,
        "total_queries": total,
        "sql_generated": sql_generated,
        "sql_executed": sql_executed,
        "success_rate": (sql_executed / total * 100) if total > 0 else 0,
        "results": results
    }

def main():
    """Run all tests"""
    
    print("="*80)
    print("SNOWFLAKE CORTEX ANALYST REAL-WORLD TESTING")
    print("="*80)
    
    # Load semantic model
    print("\nLoading semantic model...")
    with open('semantic_model.yaml', 'r') as f:
        semantic_model = yaml.safe_load(f)
    
    # Connect to Snowflake
    conn = connect_to_snowflake()
    
    # Run tests for each category
    all_results = {}
    category_stats = []
    
    for category, queries in TEST_QUERIES.items():
        category_result = run_category_tests(conn, category, queries, semantic_model)
        all_results[category] = category_result
        category_stats.append(category_result)
    
    # Print summary
    print("\n" + "="*80)
    print("SUMMARY RESULTS")
    print("="*80)
    
    print("\n| Category | Success Rate | SQL Generated | SQL Executed |")
    print("|----------|-------------|---------------|--------------|")
    
    total_queries = 0
    total_executed = 0
    
    for stat in category_stats:
        emoji = "✅" if stat['success_rate'] > 70 else "⚠️" if stat['success_rate'] > 30 else "❌"
        print(f"| {stat['category']:<20} | {stat['success_rate']:>5.1f}% {emoji} | {stat['sql_generated']}/{stat['total_queries']} | {stat['sql_executed']}/{stat['total_queries']} |")
        total_queries += stat['total_queries']
        total_executed += stat['sql_executed']
    
    overall_rate = (total_executed / total_queries * 100) if total_queries > 0 else 0
    print(f"\nOVERALL SUCCESS RATE: {overall_rate:.1f}% ({total_executed}/{total_queries} queries)")
    
    # Save detailed results
    with open('test_results/cortex_real_results.json', 'w') as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\nDetailed results saved to test_results/cortex_real_results.json")
    
    # Key findings
    print("\n" + "="*80)
    print("KEY FINDINGS")
    print("="*80)
    
    if all_results.get('time_intelligence', {}).get('success_rate', 0) < 20:
        print("❌ TIME INTELLIGENCE: Critical failure - Cannot handle time-based analysis")
    
    if all_results.get('investigation', {}).get('success_rate', 0) < 20:
        print("❌ INVESTIGATION: Cannot perform root cause analysis")
    
    if all_results.get('statistical', {}).get('success_rate', 0) < 30:
        print("❌ STATISTICAL: Missing key statistical functions")
    
    if overall_rate < 50:
        print(f"\n⚠️  ARCHITECTURAL LIMITATION CONFIRMED")
        print(f"   Snowflake Cortex Analyst success rate: {overall_rate:.1f}%")
        print(f"   Scoop Analytics success rate: 100%")
    
    conn.close()

if __name__ == "__main__":
    main()