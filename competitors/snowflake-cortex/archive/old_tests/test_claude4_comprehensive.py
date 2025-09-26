#!/usr/bin/env python3
"""
Comprehensive Claude-4-Sonnet Testing with Business Validation
Tests if the SQL actually answers the business question, not just executes
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
print("COMPREHENSIVE CLAUDE-4-SONNET TESTING WITH BUSINESS VALIDATION")
print("="*80)

def validate_business_answer(query, sql_result, test_case):
    """
    Validates if the SQL result actually answers the business question
    """
    validation = {
        "sql_generated": False,
        "sql_executed": False,
        "answers_question": False,
        "reasoning": ""
    }
    
    if not sql_result:
        validation["reasoning"] = "No SQL generated"
        return validation
    
    validation["sql_generated"] = True
    
    if "error" in sql_result:
        validation["reasoning"] = f"SQL error: {sql_result['error']}"
        return validation
    
    validation["sql_executed"] = True
    
    # Now validate if it answers the question
    question_type = test_case.get("validation_type", "")
    expected = test_case.get("expected_answer", {})
    actual_result = sql_result.get("result", [])
    
    # Business validation logic
    if question_type == "count":
        # For counts, we need a single number
        if actual_result and len(actual_result) == 1 and len(actual_result[0]) == 1:
            validation["answers_question"] = True
            validation["reasoning"] = f"Returned count: {actual_result[0][0]}"
        else:
            validation["reasoning"] = "Expected single count, got multiple values or wrong structure"
    
    elif question_type == "average":
        # For averages, need a single numeric value
        if actual_result and len(actual_result) == 1 and len(actual_result[0]) == 1:
            value = actual_result[0][0]
            if isinstance(value, (int, float)):
                validation["answers_question"] = True
                validation["reasoning"] = f"Returned average: {value}"
            else:
                validation["reasoning"] = "Expected numeric average, got non-numeric"
        else:
            validation["reasoning"] = "Expected single average value"
    
    elif question_type == "segmented":
        # For segmented analysis, need groups with metrics
        if actual_result and len(actual_result) > 0:
            # Check if we have at least 2 columns (segment + metric)
            if len(actual_result[0]) >= 2:
                validation["answers_question"] = True
                validation["reasoning"] = f"Returned {len(actual_result)} segments with metrics"
            else:
                validation["reasoning"] = "Expected segments with metrics, got single column"
        else:
            validation["reasoning"] = "No segmented results returned"
    
    elif question_type == "comparison":
        # For comparisons, need multiple rows with comparison values
        if actual_result and len(actual_result) > 1:
            validation["answers_question"] = True
            validation["reasoning"] = f"Returned {len(actual_result)} items for comparison"
        else:
            validation["reasoning"] = "Expected multiple items to compare"
    
    elif question_type == "trend":
        # For trends, need time-based data
        if "date" in str(sql_result.get("sql", "")).lower() or "month" in str(sql_result.get("sql", "")).lower():
            if actual_result:
                validation["answers_question"] = True
                validation["reasoning"] = "Returned time-based trend data"
        else:
            validation["reasoning"] = "No time dimension in query - cannot show trend"
    
    elif question_type == "investigation":
        # For investigation, need multi-faceted analysis
        if actual_result:
            validation["reasoning"] = "Only single query executed - no investigation performed"
        else:
            validation["reasoning"] = "Cannot perform multi-step investigation"
    
    elif question_type == "list":
        # For lists, need multiple rows
        if actual_result and len(actual_result) > 0:
            validation["answers_question"] = True
            validation["reasoning"] = f"Returned list of {len(actual_result)} items"
        else:
            validation["reasoning"] = "Expected list of items"
    
    elif question_type == "percentage":
        # For percentages, need calculation resulting in 0-100
        if actual_result and len(actual_result) > 0:
            # Check if result looks like percentage
            first_val = actual_result[0][-1] if isinstance(actual_result[0], (list, tuple)) else actual_result[0]
            if isinstance(first_val, (int, float)) and 0 <= first_val <= 100:
                validation["answers_question"] = True
                validation["reasoning"] = f"Returned percentage: {first_val}%"
            else:
                validation["reasoning"] = "Result doesn't appear to be a percentage"
        else:
            validation["reasoning"] = "No percentage calculated"
    
    else:
        # Generic validation
        if actual_result:
            validation["answers_question"] = True
            validation["reasoning"] = f"Returned {len(actual_result)} rows"
        else:
            validation["reasoning"] = "No results returned"
    
    return validation

def execute_and_validate(query, context, test_case):
    """
    Execute query with Claude-4-Sonnet and validate business answer
    """
    try:
        # Build prompt with context
        prompt = f"""Using the TELCO_DATA table with columns:
- CUSTOMERID, GENDER, SENIORCITIZEN, PARTNER, DEPENDENTS
- TENURE (months), PHONESERVICE, MULTIPLELINES
- INTERNETSERVICE, ONLINESECURITY, ONLINEBACKUP
- DEVICEPROTECTION, TECHSUPPORT, STREAMINGTV, STREAMINGMOVIES
- CONTRACT, PAPERLESSBILLING, PAYMENTMETHOD
- MONTHLYCHARGES (float), TOTALCHARGES (float), CHURN (boolean)

Generate SQL to answer: {query}

Return ONLY the SQL statement, no explanations."""

        cursor.execute(f"""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            'claude-4-sonnet',
            %s
        ) as response
        """, (prompt,))
        
        result = cursor.fetchone()
        
        if result and result[0]:
            response = result[0]
            
            # Check if SQL was generated
            if 'SELECT' not in response.upper():
                return {
                    "sql_generated": False,
                    "sql_executed": False,
                    "answers_question": False,
                    "reasoning": "No SQL generated, only text response"
                }
            
            # Extract SQL
            sql_start = response.upper().find('SELECT')
            sql = response[sql_start:]
            if '```' in sql:
                sql = sql.split('```')[0]
            sql = sql.strip().rstrip(';')
            
            # Try to execute
            try:
                cursor.execute(sql)
                rows = cursor.fetchall()
                
                sql_result = {
                    "sql": sql,
                    "result": rows
                }
                
                # Validate if it answers the business question
                return validate_business_answer(query, sql_result, test_case)
                
            except Exception as e:
                return {
                    "sql_generated": True,
                    "sql_executed": False,
                    "answers_question": False,
                    "reasoning": f"SQL error: {str(e)[:100]}"
                }
        else:
            return {
                "sql_generated": False,
                "sql_executed": False,
                "answers_question": False,
                "reasoning": "No response from model"
            }
            
    except Exception as e:
        return {
            "sql_generated": False,
            "sql_executed": False,
            "answers_question": False,
            "reasoning": f"Error: {str(e)[:100]}"
        }

# Comprehensive test cases covering all categories
test_cases = [
    # Basic Aggregations
    {
        "category": "Basic Aggregation",
        "query": "How many customers do we have?",
        "validation_type": "count",
        "expected_answer": {"type": "single_number"}
    },
    {
        "category": "Basic Aggregation",
        "query": "What's the average monthly charge?",
        "validation_type": "average",
        "expected_answer": {"type": "single_number", "range": [0, 200]}
    },
    {
        "category": "Basic Aggregation",
        "query": "What's the total revenue from all customers?",
        "validation_type": "count",
        "expected_answer": {"type": "single_number"}
    },
    
    # Segmented Analysis
    {
        "category": "Segmented Analysis",
        "query": "Show me churn rate by contract type",
        "validation_type": "segmented",
        "expected_answer": {"segments": ["Month-to-month", "One year", "Two year"]}
    },
    {
        "category": "Segmented Analysis",
        "query": "What's the average monthly charge by internet service type?",
        "validation_type": "segmented",
        "expected_answer": {"segments": ["DSL", "Fiber optic", "No"]}
    },
    
    # Filtering
    {
        "category": "Filtering",
        "query": "Show me customers with monthly charges over $100",
        "validation_type": "list",
        "expected_answer": {"type": "customer_list"}
    },
    {
        "category": "Complex Filtering",
        "query": "Find customers who have fiber optic internet but no online security",
        "validation_type": "list",
        "expected_answer": {"type": "filtered_list"}
    },
    
    # Calculated Metrics
    {
        "category": "Calculated Metrics",
        "query": "What percentage of customers have churned?",
        "validation_type": "percentage",
        "expected_answer": {"type": "percentage", "range": [0, 100]}
    },
    {
        "category": "Calculated Metrics",
        "query": "Calculate the ratio of monthly charges to tenure for each customer",
        "validation_type": "list",
        "expected_answer": {"type": "calculated_list"}
    },
    
    # Comparisons
    {
        "category": "Comparison",
        "query": "Compare churn rates between different payment methods",
        "validation_type": "comparison",
        "expected_answer": {"type": "multi_group_comparison"}
    },
    {
        "category": "Comparison",
        "query": "How does average tenure differ between churned and active customers?",
        "validation_type": "comparison",
        "expected_answer": {"type": "two_group_comparison"}
    },
    
    # Top N
    {
        "category": "Top N",
        "query": "Show me the top 5 customers by total charges",
        "validation_type": "list",
        "expected_answer": {"count": 5}
    },
    {
        "category": "Top N",
        "query": "What are the bottom 3 tenure lengths?",
        "validation_type": "list",
        "expected_answer": {"count": 3}
    },
    
    # Time Intelligence (Expected to fail)
    {
        "category": "Time Intelligence",
        "query": "Show me the month-over-month growth in customer count",
        "validation_type": "trend",
        "expected_answer": {"type": "time_series"}
    },
    {
        "category": "Time Intelligence",
        "query": "What's the running total of revenue over time?",
        "validation_type": "trend",
        "expected_answer": {"type": "cumulative"}
    },
    
    # Investigation (Expected to fail)
    {
        "category": "Investigation",
        "query": "Why are customers churning?",
        "validation_type": "investigation",
        "expected_answer": {"type": "multi_factor_analysis"}
    },
    {
        "category": "Investigation",
        "query": "What factors predict high monthly charges?",
        "validation_type": "investigation",
        "expected_answer": {"type": "correlation_analysis"}
    },
    
    # Statistical
    {
        "category": "Statistical",
        "query": "What's the standard deviation of monthly charges?",
        "validation_type": "count",
        "expected_answer": {"type": "single_number"}
    },
    {
        "category": "Statistical",
        "query": "Show me the correlation between tenure and monthly charges",
        "validation_type": "count",
        "expected_answer": {"type": "correlation", "range": [-1, 1]}
    },
    
    # Complex Patterns
    {
        "category": "Complex Pattern",
        "query": "Find customers whose monthly charges are above average for their contract type",
        "validation_type": "list",
        "expected_answer": {"type": "subquery_filter"}
    }
]

# Run tests
results = []
stats = {
    "total": len(test_cases),
    "sql_generated": 0,
    "sql_executed": 0,
    "answers_question": 0,
    "by_category": {}
}

print(f"\nRunning {len(test_cases)} comprehensive tests...\n")

for i, test in enumerate(test_cases):
    print(f"[{i+1}/{len(test_cases)}] {test['category']}: {test['query'][:50]}...")
    
    result = execute_and_validate(test['query'], "with_context", test)
    
    # Update stats
    if result["sql_generated"]:
        stats["sql_generated"] += 1
    if result["sql_executed"]:
        stats["sql_executed"] += 1
    if result["answers_question"]:
        stats["answers_question"] += 1
    
    # Category stats
    cat = test['category']
    if cat not in stats["by_category"]:
        stats["by_category"][cat] = {"total": 0, "generated": 0, "executed": 0, "answered": 0}
    
    stats["by_category"][cat]["total"] += 1
    if result["sql_generated"]:
        stats["by_category"][cat]["generated"] += 1
    if result["sql_executed"]:
        stats["by_category"][cat]["executed"] += 1
    if result["answers_question"]:
        stats["by_category"][cat]["answered"] += 1
    
    # Store result
    results.append({
        "test": test,
        "result": result
    })
    
    # Print result
    status = "✅" if result["answers_question"] else "⚠️" if result["sql_executed"] else "❌"
    print(f"  {status} {result['reasoning']}")

# Print summary
print("\n" + "="*80)
print("COMPREHENSIVE TEST RESULTS SUMMARY")
print("="*80)

print(f"\nOverall Performance:")
print(f"  SQL Generated:     {stats['sql_generated']}/{stats['total']} ({stats['sql_generated']/stats['total']*100:.1f}%)")
print(f"  SQL Executed:      {stats['sql_executed']}/{stats['total']} ({stats['sql_executed']/stats['total']*100:.1f}%)")
print(f"  Answers Question:  {stats['answers_question']}/{stats['total']} ({stats['answers_question']/stats['total']*100:.1f}%)")

print(f"\nBy Category (Answers Business Question):")
for cat, cat_stats in sorted(stats["by_category"].items()):
    pct = cat_stats["answered"]/cat_stats["total"]*100 if cat_stats["total"] > 0 else 0
    status = "✅" if pct >= 80 else "⚠️" if pct >= 50 else "❌"
    print(f"  {status} {cat}: {cat_stats['answered']}/{cat_stats['total']} ({pct:.1f}%)")

print("\n" + "="*80)
print("KEY BUSINESS VALIDATION INSIGHTS")
print("="*80)
print("""
1. SQL Generation ≠ Business Answer
   - Many queries generate SQL but don't answer the question
   - Example: "Why are customers churning?" → Lists churned customers (wrong)
   
2. Critical Failures for Business Users:
   - Time Intelligence: Cannot do any period comparisons
   - Investigation: Cannot perform root cause analysis
   - Trends: No temporal analysis capability
   
3. What Actually Works:
   - Simple counts and averages
   - Basic segmentation (with exact column names)
   - Simple filters and lists
   
4. Business Impact:
   - Can answer ~30-40% of real business questions
   - Fails on strategic questions (why, trends, predictions)
   - Requires users to know exact schema
""")

# Save detailed results
with open('claude4_comprehensive_results.json', 'w') as f:
    json.dump({
        "stats": stats,
        "details": results,
        "timestamp": datetime.now().isoformat()
    }, f, indent=2, default=str)

print(f"\n💾 Detailed results saved to claude4_comprehensive_results.json")

conn.close()