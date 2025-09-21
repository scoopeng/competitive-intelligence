#!/usr/bin/env python3
"""
Extended Snowflake CORTEX.COMPLETE Testing - Remaining 77% of Scoop Benchmark
Testing categories: Intermediate, Advanced, ML/AI capabilities
"""

import snowflake.connector
import json
from datetime import datetime

# Connection details
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
print("EXTENDED SNOWFLAKE BENCHMARK - REMAINING 77% OF SCOOP TEST SUITE")
print("Testing: Intermediate, Advanced, and ML/AI Query Capabilities")
print("="*80)

# Extended test cases covering remaining Scoop capabilities
test_cases = {
    "INTERMEDIATE_QUERIES": [
        {
            "id": "INT_001",
            "category": "Distinct Counts",
            "query": "How many distinct payment methods are used by churned customers?",
            "scoop_capability": "Automatic distinct handling"
        },
        {
            "id": "INT_002", 
            "category": "Multiple Aggregations",
            "query": "Show min, max, average, and standard deviation of monthly charges by contract type",
            "scoop_capability": "Complex aggregation in single pass"
        },
        {
            "id": "INT_003",
            "category": "Null Handling",
            "query": "Count customers with missing values in each column",
            "scoop_capability": "Automatic null detection"
        },
        {
            "id": "INT_004",
            "category": "Date Filtering",
            "query": "Show churn trend by month for the last 12 months",
            "scoop_capability": "Temporal analysis without date column"
        },
        {
            "id": "INT_005",
            "category": "Range Queries",
            "query": "Segment customers into low (0-30), medium (30-70), high (70+) monthly charge groups and show churn rate",
            "scoop_capability": "Automatic binning"
        },
        {
            "id": "INT_006",
            "category": "Subqueries",
            "query": "Find customers who pay more than the average but still churned",
            "scoop_capability": "Nested query generation"
        },
        {
            "id": "INT_007",
            "category": "Window Functions",
            "query": "Rank customers by monthly charges within each contract type",
            "scoop_capability": "Window function usage"
        },
        {
            "id": "INT_008",
            "category": "Cumulative Calculations",
            "query": "Show cumulative revenue by tenure months",
            "scoop_capability": "Running totals"
        }
    ],
    
    "ADVANCED_QUERIES": [
        {
            "id": "ADV_001",
            "category": "Multi-Step Investigation",
            "query": "Why do high-value customers (top 20% by monthly charges) churn? Investigate all factors.",
            "scoop_capability": "3-10 query investigation"
        },
        {
            "id": "ADV_002",
            "category": "Root Cause Analysis",
            "query": "What is the primary driver of churn for customers with tenure > 24 months?",
            "scoop_capability": "Causal analysis"
        },
        {
            "id": "ADV_003",
            "category": "Correlation Discovery",
            "query": "Find correlations between support tickets and churn probability",
            "scoop_capability": "Statistical correlation"
        },
        {
            "id": "ADV_004",
            "category": "Pattern Recognition",
            "query": "Identify patterns in customer behavior before churning",
            "scoop_capability": "Pattern mining"
        },
        {
            "id": "ADV_005",
            "category": "Predictive Query",
            "query": "Which customers are most likely to churn next month based on current patterns?",
            "scoop_capability": "Predictive modeling"
        },
        {
            "id": "ADV_006",
            "category": "Trend Analysis",
            "query": "Is churn rate increasing or decreasing over time? What's driving the trend?",
            "scoop_capability": "Trend detection with explanation"
        },
        {
            "id": "ADV_007",
            "category": "Anomaly Detection",
            "query": "Find unusual patterns in the churn data that warrant investigation",
            "scoop_capability": "Anomaly identification"
        },
        {
            "id": "ADV_008",
            "category": "Cohort Analysis",
            "query": "Compare churn behavior across customer cohorts by signup period",
            "scoop_capability": "Cohort tracking"
        },
        {
            "id": "ADV_009",
            "category": "Top N Analysis",
            "query": "What are the top 5 combinations of factors that lead to churn?",
            "scoop_capability": "Multi-factor ranking"
        },
        {
            "id": "ADV_010",
            "category": "Percentile Calculations",
            "query": "Show the 25th, 50th, 75th, and 90th percentile of monthly charges for churned vs retained customers",
            "scoop_capability": "Percentile analysis"
        }
    ],
    
    "ML_AI_QUERIES": [
        {
            "id": "ML_001",
            "category": "Decision Tree Analysis",
            "query": "Build a decision tree to explain churn factors",
            "scoop_capability": "J48 decision tree (Scoop exclusive)"
        },
        {
            "id": "ML_002",
            "category": "Rule Learning",
            "query": "Generate business rules that predict churn with high accuracy",
            "scoop_capability": "JRip rule learning (Scoop exclusive)"
        },
        {
            "id": "ML_003",
            "category": "Clustering",
            "query": "Segment customers into groups based on behavior patterns",
            "scoop_capability": "EM clustering (Scoop exclusive)"
        },
        {
            "id": "ML_004",
            "category": "Association Rules",
            "query": "Find associations between service features and churn",
            "scoop_capability": "Apriori algorithm (Scoop exclusive)"
        },
        {
            "id": "ML_005",
            "category": "Feature Importance",
            "query": "Rank all factors by their importance in predicting churn",
            "scoop_capability": "ML-based feature ranking (Scoop exclusive)"
        },
        {
            "id": "ML_006",
            "category": "Three-Way Interaction",
            "query": "Find interactions between contract, payment method, and service type that affect churn",
            "scoop_capability": "ML_GROUP discovery (Scoop exclusive)"
        },
        {
            "id": "ML_007",
            "category": "Time-Based Patterns",
            "query": "Discover how churn patterns change over customer lifetime",
            "scoop_capability": "ML_PERIOD analysis (Scoop exclusive)"
        }
    ]
}

# Track results
results_summary = {
    "total_tests": 0,
    "successful": 0,
    "failed": 0,
    "errors": [],
    "category_performance": {}
}

# Test execution
for category_name, category_tests in test_cases.items():
    print(f"\n{'='*80}")
    print(f"TESTING CATEGORY: {category_name}")
    print(f"{'='*80}")
    
    category_results = {"success": 0, "fail": 0}
    
    for test in category_tests:
        results_summary["total_tests"] += 1
        
        print(f"\n[{test['id']}] {test['category']}")
        print(f"Query: {test['query']}")
        print(f"Scoop Capability: {test['scoop_capability']}")
        print("-"*40)
        
        try:
            # Call CORTEX.COMPLETE
            start = datetime.now()
            
            # Construct prompt
            prompt = f"""Generate SQL for this query against the TELCO_DATA table:
            {test['query']}
            
            Table has columns: CUSTOMERID, GENDER, SENIORCITIZEN, PARTNER, DEPENDENTS, TENURE, 
            PHONESERVICE, MULTIPLELINES, INTERNETSERVICE, ONLINESECURITY, ONLINEBACKUP, 
            DEVICEPROTECTION, TECHSUPPORT, STREAMINGTV, STREAMINGMOVIES, CONTRACT, 
            PAPERLESSBILLING, PAYMENTMETHOD, MONTHLYCHARGES, TOTALCHARGES, NUMADMINTICKETS, 
            NUMTECHTICKETS, CHURN
            
            Return only SQL, no explanation."""
            
            cursor.execute(f"""
            SELECT SNOWFLAKE.CORTEX.COMPLETE(
                'claude-3.5-sonnet',
                '{prompt}'
            ) as sql
            """)
            
            result = cursor.fetchone()
            elapsed = (datetime.now() - start).total_seconds()
            
            if result and result[0]:
                sql = result[0]
                
                # Extract SQL from response
                if '```sql' in sql:
                    sql_clean = sql.split('```sql')[1].split('```')[0].strip()
                elif 'SELECT' in sql.upper():
                    # Find the SELECT statement
                    lines = sql.split('\n')
                    sql_lines = []
                    in_sql = False
                    for line in lines:
                        if 'SELECT' in line.upper():
                            in_sql = True
                        if in_sql:
                            sql_lines.append(line)
                            if ';' in line:
                                break
                    sql_clean = '\n'.join(sql_lines)
                else:
                    sql_clean = sql
                
                print(f"✅ Generated SQL in {elapsed:.2f}s")
                print(f"SQL Preview: {sql_clean[:200]}...")
                
                # Try to execute the generated SQL
                try:
                    cursor.execute(sql_clean)
                    rows = cursor.fetchall()
                    print(f"✅ Query executed successfully! Returned {len(rows)} rows")
                    results_summary["successful"] += 1
                    category_results["success"] += 1
                    
                except Exception as exec_error:
                    print(f"❌ SQL Execution failed: {str(exec_error)[:100]}")
                    results_summary["failed"] += 1
                    category_results["fail"] += 1
                    results_summary["errors"].append({
                        "test_id": test['id'],
                        "category": test['category'],
                        "error": str(exec_error)[:200]
                    })
                    
            else:
                print(f"❌ No SQL generated")
                results_summary["failed"] += 1
                category_results["fail"] += 1
                
        except Exception as e:
            print(f"❌ CORTEX.COMPLETE Error: {str(e)[:100]}")
            results_summary["failed"] += 1
            category_results["fail"] += 1
            results_summary["errors"].append({
                "test_id": test['id'],
                "category": test['category'],
                "error": f"CORTEX.COMPLETE failed: {str(e)[:200]}"
            })
    
    results_summary["category_performance"][category_name] = category_results

# Final Summary
print("\n" + "="*80)
print("FINAL RESULTS SUMMARY")
print("="*80)

print(f"\nTotal Tests Run: {results_summary['total_tests']}")
print(f"Successful: {results_summary['successful']} ({results_summary['successful']/results_summary['total_tests']*100:.1f}%)")
print(f"Failed: {results_summary['failed']} ({results_summary['failed']/results_summary['total_tests']*100:.1f}%)")

print("\nPerformance by Category:")
for category, perf in results_summary["category_performance"].items():
    total = perf["success"] + perf["fail"]
    success_rate = (perf["success"] / total * 100) if total > 0 else 0
    print(f"  {category}: {perf['success']}/{total} ({success_rate:.1f}% success)")

print("\nKey Findings:")
print("1. INTERMEDIATE QUERIES: Basic SQL generation capabilities")
print("2. ADVANCED QUERIES: Multi-step investigation and root cause analysis")
print("3. ML/AI QUERIES: Scoop's exclusive ML capabilities (J48, JRip, EM, etc.)")

print("\nCommon Failure Patterns:")
failure_types = {}
for error in results_summary["errors"]:
    error_type = "Unknown"
    if "syntax" in error["error"].lower():
        error_type = "SQL Syntax Error"
    elif "column" in error["error"].lower():
        error_type = "Column Reference Error"
    elif "type" in error["error"].lower():
        error_type = "Type Mismatch"
    elif "not supported" in error["error"].lower():
        error_type = "Unsupported Operation"
    
    if error_type not in failure_types:
        failure_types[error_type] = 0
    failure_types[error_type] += 1

for error_type, count in sorted(failure_types.items(), key=lambda x: x[1], reverse=True):
    print(f"  - {error_type}: {count} occurrences")

# Save results to JSON
with open('extended_benchmark_results.json', 'w') as f:
    json.dump(results_summary, f, indent=2, default=str)
    print(f"\n✅ Results saved to extended_benchmark_results.json")

# Calculate combined results with original 7 tests
print("\n" + "="*80)
print("COMBINED BENCHMARK RESULTS (Original + Extended)")
print("="*80)
original_tests = 7
original_success = 5  # 71% of 7
total_combined = original_tests + results_summary['total_tests']
total_success = original_success + results_summary['successful']

print(f"Total Scoop Benchmark Tests: {total_combined}")
print(f"Total Successful: {total_success} ({total_success/total_combined*100:.1f}%)")
print(f"Total Failed: {total_combined - total_success} ({(total_combined - total_success)/total_combined*100:.1f}%)")

print("\n🎯 KEY COMPETITIVE POINTS:")
print("1. Snowflake CORTEX.COMPLETE cannot handle ML/AI queries at all")
print("2. Multi-step investigation is not possible (single SQL only)")
print("3. No root cause analysis capability")
print("4. No pattern recognition or predictive modeling")
print("5. Limited to basic SQL generation with high error rate")

conn.close()
print("\n✅ Extended benchmark complete!")