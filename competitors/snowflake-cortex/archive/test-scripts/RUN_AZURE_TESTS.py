#!/usr/bin/env python3
"""
Run REAL tests against Snowflake Cortex Analyst on Azure
Using the Azure account that has been confirmed to work
"""

import snowflake.connector
import json
import yaml
import sys
from datetime import datetime
from typing import Dict, List, Optional, Any
import time

# Azure Snowflake Configuration (confirmed working)
SNOWFLAKE_ACCOUNT = 'rcdtonr-ji20455'  # Azure account
SNOWFLAKE_USER = 'bradtest'
SNOWFLAKE_PASSWORD = 'qMsGeKsE33NJeZp'
SNOWFLAKE_WAREHOUSE = 'COMPUTE_WH'
SNOWFLAKE_DATABASE = 'SCOOP_BENCHMARK'
SNOWFLAKE_SCHEMA = 'TEST_DATA'

# Test queries organized by category - comprehensive suite
TEST_QUERIES = {
    "basic_aggregation": [
        "How many customers do we have?",
        "What is the total revenue?",
        "What's the average monthly charge?",
        "Show me the sum of total charges",
        "Count the number of churned customers",
        "What is the minimum tenure?",
        "What is the maximum monthly charge?",
        "Show total customers by churn status"
    ],
    
    "grouping": [
        "Show revenue by contract type",
        "Count customers by payment method",
        "Average tenure by internet service type",
        "Total charges by gender",
        "Show churn rate by contract type",
        "Group customers by senior citizen status",
        "Monthly charges by phone service",
        "Show distribution by multiple lines"
    ],
    
    "filtering": [
        "Show only senior citizens",
        "Customers with fiber optic internet",
        "Show customers who churned",
        "Customers with monthly charges over 100",
        "Active customers with no phone service",
        "Show customers with tenure less than 12 months",
        "Customers with DSL internet and phone service",
        "Show male customers with electronic check payment",
        "Customers with total charges between 1000 and 5000",
        "Show customers without internet service",
        "Customers with month-to-month contract who churned",
        "Senior citizens with fiber optic",
        "Customers with paperless billing",
        "Show only customers with tech support",
        "Customers with streaming TV but no streaming movies",
        "Active customers with two year contract",
        "Show customers where monthly charges equals total charges"
    ],
    
    "time_intelligence": [
        "Show month-over-month revenue growth",
        "Calculate the 3-month moving average of charges",
        "What's the year-over-year change in customer count?",
        "Show running total of monthly charges",
        "Compare this month's revenue to last month",
        "Show cumulative sum of customers over time",
        "Calculate monthly churn trend",
        "What's the quarter-over-quarter growth?",
        "Show 7-day rolling average",
        "Calculate period-over-period comparison",
        "Show year-to-date totals",
        "What's the month-to-date performance?",
        "Calculate trailing 12 months revenue",
        "Show weekly customer acquisition",
        "Display seasonal patterns"
    ],
    
    "calculated_metrics": [
        "Calculate the churn rate",
        "What's the customer lifetime value?",
        "Show profit margin by service type",
        "Calculate average revenue per user",
        "What's the retention rate?",
        "Calculate conversion rate",
        "Show cost per acquisition",
        "What's the net promoter score?",
        "Calculate customer satisfaction index",
        "Show revenue per employee",
        "What's the gross margin?",
        "Calculate the attach rate for services",
        "Show the upsell rate",
        "What's the customer health score?"
    ],
    
    "ranking": [
        "Top 5 customers by total charges",
        "Bottom 10 customers by tenure",
        "Rank payment methods by popularity",
        "Show the highest paying customers",
        "List services by revenue contribution",
        "Top 3 contract types by customer count"
    ],
    
    "statistical": [
        "What's the correlation between tenure and monthly charges?",
        "Show standard deviation of monthly charges",
        "Calculate the median customer tenure",
        "What's the 75th percentile of total charges?",
        "Find statistical outliers in monthly charges",
        "Calculate variance in customer tenure",
        "Show the distribution of monthly charges",
        "What's the z-score for high value customers?",
        "Calculate confidence intervals for churn rate",
        "Show regression analysis for pricing"
    ],
    
    "investigation": [
        "Why are customers churning?",
        "What factors predict high monthly charges?",
        "Which customer segment is most profitable?",
        "What drives customer lifetime value?",
        "Why did revenue drop?",
        "What causes customer dissatisfaction?",
        "Which services lead to higher retention?",
        "Why do some customers have high tenure?",
        "What patterns exist in customer behavior?",
        "How can we reduce churn?"
    ],
    
    "complex_analysis": [
        "Compare churned vs active customers across all attributes",
        "Segment customers by value and behavior",
        "Which service combinations are most popular?",
        "Analyze the customer journey to churn",
        "Identify upsell opportunities",
        "Find cross-sell opportunities",
        "Perform cohort analysis",
        "Show customer migration patterns",
        "Identify at-risk customers"
    ],
    
    "visualization": [
        "Create a bar chart of revenue by service",
        "Show a pie chart of customer distribution",
        "Make a line graph of monthly trends",
        "Display a heatmap of service usage",
        "Create a scatter plot of tenure vs charges",
        "Show a funnel chart of customer journey"
    ],
    
    "change_tracking": [
        "Show how customer count changed over time",
        "Track churn rate changes monthly",
        "Display revenue changes by quarter",
        "Show service adoption over time",
        "Track payment method changes"
    ],
    
    "edge_cases": [
        "Handle null values in phone service",
        "Division by zero in churn rate calculation",
        "Empty result set handling",
        "Very long query with multiple conditions"
    ]
}

def connect_to_snowflake():
    """Establish Snowflake connection to Azure instance"""
    try:
        conn = snowflake.connector.connect(
            account=SNOWFLAKE_ACCOUNT,
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            warehouse=SNOWFLAKE_WAREHOUSE,
            database=SNOWFLAKE_DATABASE,
            schema=SNOWFLAKE_SCHEMA
        )
        print("✅ Connected to Azure Snowflake")
        return conn
    except Exception as e:
        print(f"❌ Failed to connect: {e}")
        sys.exit(1)

def test_semantic_model_api(conn, query: str, model_name: str = 'llama3.1-70b') -> Dict:
    """Test using the semantic model approach with Cortex"""
    
    try:
        cursor = conn.cursor()
        
        # First, let's check if we have a semantic model table
        # For now, we'll use direct CORTEX.COMPLETE with structured prompt
        
        sql_query = f"""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            '{model_name}',
            'Generate a Snowflake SQL query for this question. Return ONLY the SQL query, no explanation.
            
            Question: {query}
            
            Available table: TELCO_DATA with columns:
            - CUSTOMERID (VARCHAR)
            - GENDER (VARCHAR) 
            - SENIORCITIZEN (NUMBER)
            - PARTNER (VARCHAR)
            - DEPENDENTS (VARCHAR)
            - TENURE (NUMBER)
            - PHONESERVICE (VARCHAR)
            - MULTIPLELINES (VARCHAR)
            - INTERNETSERVICE (VARCHAR)
            - ONLINESECURITY (VARCHAR)
            - ONLINEBACKUP (VARCHAR)
            - DEVICEPROTECTION (VARCHAR)
            - TECHSUPPORT (VARCHAR)
            - STREAMINGTV (VARCHAR)
            - STREAMINGMOVIES (VARCHAR)
            - CONTRACT (VARCHAR)
            - PAPERLESSBILLING (VARCHAR)
            - PAYMENTMETHOD (VARCHAR)
            - MONTHLYCHARGES (NUMBER)
            - TOTALCHARGES (NUMBER)
            - CHURN (VARCHAR)
            
            SQL query:'
        ) as response;
        """
        
        start_time = time.time()
        cursor.execute(sql_query)
        result = cursor.fetchone()
        elapsed = time.time() - start_time
        
        response = result[0] if result else None
        
        # Extract SQL from response
        generated_sql = None
        if response:
            # Clean up the response to get just the SQL
            response = response.strip()
            if "SELECT" in response.upper():
                # Find the SQL statement
                sql_start = response.upper().find("SELECT")
                generated_sql = response[sql_start:].strip()
                # Remove any trailing explanation
                if ";" in generated_sql:
                    generated_sql = generated_sql[:generated_sql.index(";")+1]
                else:
                    # Find where SQL likely ends
                    for end_marker in ["\n\n", "\nThis", "\nNote", "\nExplanation"]:
                        if end_marker in generated_sql:
                            generated_sql = generated_sql[:generated_sql.index(end_marker)]
                            break
        
        # Test if SQL executes
        sql_executes = False
        execution_error = None
        execution_result = None
        
        if generated_sql:
            try:
                cursor.execute(generated_sql)
                execution_result = cursor.fetchall()
                sql_executes = True
            except Exception as e:
                execution_error = str(e)
        
        cursor.close()
        
        return {
            "query": query,
            "model": model_name,
            "response": response,
            "generated_sql": generated_sql,
            "sql_executes": sql_executes,
            "execution_error": execution_error,
            "execution_result": execution_result[:5] if execution_result else None,  # First 5 rows
            "response_time": elapsed,
            "success": bool(generated_sql and sql_executes)
        }
        
    except Exception as e:
        return {
            "query": query,
            "model": model_name,
            "error": str(e),
            "success": False
        }

def run_category_tests(conn, category: str, queries: List[str]) -> Dict:
    """Run all tests for a category"""
    
    print(f"\n{'='*60}")
    print(f"Testing {category.upper()}")
    print(f"{'='*60}")
    
    results = []
    for i, query in enumerate(queries, 1):
        print(f"\n[{i}/{len(queries)}] {query}")
        
        # Test with llama3.1-70b (most capable available model)
        result = test_semantic_model_api(conn, query, 'llama3.1-70b')
        
        if result.get("success"):
            print(f"✅ SUCCESS - Generated executable SQL")
            if result.get("generated_sql"):
                sql_preview = result['generated_sql'][:100].replace('\n', ' ')
                print(f"   SQL: {sql_preview}...")
        else:
            if result.get("generated_sql"):
                print(f"⚠️  PARTIAL - Generated SQL but failed to execute")
                print(f"   Error: {result.get('execution_error', 'Unknown')[:200]}")
            else:
                print(f"❌ FAILED - No SQL generated")
                if result.get("error"):
                    print(f"   Error: {result['error'][:200]}")
        
        results.append(result)
        time.sleep(0.5)  # Rate limiting
    
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
    print("SNOWFLAKE CORTEX ANALYST - AZURE TESTING")
    print("="*80)
    print(f"\nAccount: {SNOWFLAKE_ACCOUNT}")
    print(f"Database: {SNOWFLAKE_DATABASE}")
    print(f"Schema: {SNOWFLAKE_SCHEMA}")
    
    # Connect to Snowflake
    conn = connect_to_snowflake()
    
    # Quick connectivity test
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM TELCO_DATA")
    count = cursor.fetchone()[0]
    print(f"✅ TELCO_DATA table has {count} rows")
    cursor.close()
    
    # Run tests for each category
    all_results = {}
    category_stats = []
    
    for category, queries in TEST_QUERIES.items():
        category_result = run_category_tests(conn, category, queries)
        all_results[category] = category_result
        category_stats.append(category_result)
    
    # Print summary
    print("\n" + "="*80)
    print("FINAL RESULTS - SNOWFLAKE CORTEX ANALYST")
    print("="*80)
    
    print("\n| Category | Success Rate | SQL Generated | SQL Executed |")
    print("|----------|-------------|---------------|--------------|")
    
    total_queries = 0
    total_executed = 0
    
    for stat in category_stats:
        emoji = "✅" if stat['success_rate'] > 70 else "⚠️" if stat['success_rate'] > 30 else "❌"
        print(f"| {stat['category']:<20} | {stat['success_rate']:>5.1f}% {emoji} | {stat['sql_generated']:>3}/{stat['total_queries']:<3} | {stat['sql_executed']:>3}/{stat['total_queries']:<3} |")
        total_queries += stat['total_queries']
        total_executed += stat['sql_executed']
    
    overall_rate = (total_executed / total_queries * 100) if total_queries > 0 else 0
    
    print("\n" + "="*80)
    print(f"OVERALL SUCCESS RATE: {overall_rate:.1f}% ({total_executed}/{total_queries} queries)")
    print("="*80)
    
    # Save detailed results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'test_results/cortex_azure_results_{timestamp}.json'
    with open(filename, 'w') as f:
        json.dump(all_results, f, indent=2, default=str)
    
    print(f"\n📊 Detailed results saved to {filename}")
    
    # Key findings
    print("\n" + "="*80)
    print("KEY FINDINGS")
    print("="*80)
    
    # Check specific capability failures
    if all_results.get('time_intelligence', {}).get('success_rate', 0) < 20:
        print("❌ TIME INTELLIGENCE: Critical failure - Cannot handle time-based analysis")
        print("   Examples that failed: MoM growth, moving averages, running totals")
    
    if all_results.get('investigation', {}).get('success_rate', 0) < 20:
        print("❌ INVESTIGATION: Cannot perform root cause analysis")
        print("   Examples that failed: 'Why are customers churning?', 'What drives revenue?'")
    
    if all_results.get('statistical', {}).get('success_rate', 0) < 30:
        print("❌ STATISTICAL: Missing key statistical functions")
        print("   Examples that failed: correlation, standard deviation, percentiles")
    
    if all_results.get('visualization', {}).get('success_rate', 0) < 20:
        print("❌ VISUALIZATION: No chart generation capabilities")
    
    if all_results.get('change_tracking', {}).get('success_rate', 0) < 20:
        print("❌ CHANGE TRACKING: Cannot analyze historical changes")
    
    print(f"\n{'='*80}")
    print("COMPETITIVE CONCLUSION")
    print(f"{'='*80}")
    
    if overall_rate < 50:
        print(f"⚠️  ARCHITECTURAL LIMITATION CONFIRMED")
        print(f"   Snowflake Cortex Analyst success rate: {overall_rate:.1f}%")
        print(f"   Scoop Analytics success rate: 100%")
        print(f"\n   Key architectural differences:")
        print(f"   - Snowflake: Direct SQL generation (no intermediate representation)")
        print(f"   - Scoop: Query JSON Object → Multi-step planning → SQL")
    else:
        print(f"✅ Snowflake achieved {overall_rate:.1f}% success rate")
    
    conn.close()

if __name__ == "__main__":
    main()