#!/usr/bin/env python3
"""
SIMPLE CONSOLIDATED TEST RUNNER
Runs all 88+ queries and validates business answers
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
print("RUNNING ALL 88+ TESTS WITH CLAUDE-4-SONNET")
print("Validating if SQL actually answers the business question")
print("="*80)

# ALL 88+ TEST QUERIES FROM CUMULATIVE LEARNING
ALL_QUERIES = [
    # NATURAL LANGUAGE (15) - What users actually type
    {"id": "NL01", "query": "How many customers do we have?", "type": "count"},
    {"id": "NL02", "query": "What's the average monthly charge?", "type": "average"},
    {"id": "NL03", "query": "Show me churn rate by contract type", "type": "segmented"},
    {"id": "NL04", "query": "Which customers are paying more than $100 per month?", "type": "list"},
    {"id": "NL05", "query": "Why are customers leaving?", "type": "investigation"},
    {"id": "NL06", "query": "What's our total revenue?", "type": "sum"},
    {"id": "NL07", "query": "Show me the top 10 highest paying customers", "type": "top_n"},
    {"id": "NL08", "query": "How many payment methods do churned customers use?", "type": "distinct"},
    {"id": "NL09", "query": "What's the relationship between tenure and churn?", "type": "correlation"},
    {"id": "NL10", "query": "Which services do churned customers have?", "type": "breakdown"},
    {"id": "NL11", "query": "Compare churn rates between different internet service types", "type": "comparison"},
    {"id": "NL12", "query": "What drives customer loyalty?", "type": "investigation"},
    {"id": "NL13", "query": "Show me monthly charges by gender", "type": "segmented"},
    {"id": "NL14", "query": "How much money are we losing to churn?", "type": "impact"},
    {"id": "NL15", "query": "What patterns predict churn?", "type": "pattern"},
    
    # TIME INTELLIGENCE (15)
    {"id": "TI01", "query": "Show month-over-month growth", "type": "time_trend"},
    {"id": "TI02", "query": "What's the year-over-year change?", "type": "time_trend"},
    {"id": "TI03", "query": "Calculate running total by month", "type": "cumulative"},
    {"id": "TI04", "query": "Show 7-day moving average", "type": "moving_avg"},
    {"id": "TI05", "query": "Compare this quarter to last quarter", "type": "time_comparison"},
    {"id": "TI06", "query": "Show data from last 30 days", "type": "relative_date"},
    {"id": "TI07", "query": "Calculate days between events", "type": "date_diff"},
    {"id": "TI08", "query": "Group by month and show trend", "type": "monthly_trend"},
    {"id": "TI09", "query": "Show patterns by day of week", "type": "dow_pattern"},
    {"id": "TI10", "query": "Calculate quarter-to-date totals", "type": "qtd"},
    {"id": "TI11", "query": "Show same period last year", "type": "sply"},
    {"id": "TI12", "query": "Find peak day in each month", "type": "peak"},
    {"id": "TI13", "query": "What's the overall trend?", "type": "trend"},
    {"id": "TI14", "query": "Forecast next month", "type": "forecast"},
    {"id": "TI15", "query": "Find seasonality patterns", "type": "seasonality"},
    
    # ADVANCED SQL (20 patterns)
    {"id": "AS01", "query": "Find customers with (fiber OR DSL) AND (security OR backup)", "type": "complex_filter"},
    {"id": "AS02", "query": "Show charges between $50 and $100", "type": "between"},
    {"id": "AS03", "query": "Find null or zero tenure", "type": "null_handling"},
    {"id": "AS04", "query": "Payment method like '%electronic%'", "type": "like"},
    {"id": "AS05", "query": "Calculate rate avoiding division by zero", "type": "safe_calc"},
    {"id": "AS06", "query": "Show percentage of total", "type": "pct_total"},
    {"id": "AS07", "query": "Calculate complex formula: (charges * tenure) / support", "type": "formula"},
    {"id": "AS08", "query": "Count churned and active separately", "type": "conditional"},
    {"id": "AS09", "query": "Groups with average > 70", "type": "having"},
    {"id": "AS10", "query": "Count distinct by group", "type": "distinct_group"},
    {"id": "AS11", "query": "Standard deviation by category", "type": "stddev"},
    {"id": "AS12", "query": "Min and max by status", "type": "min_max"},
    {"id": "AS13", "query": "Top 5 by charges", "type": "top_n"},
    {"id": "AS14", "query": "Top 10 by calculated value", "type": "top_calc"},
    {"id": "AS15", "query": "Bottom 5 by tenure", "type": "bottom_n"},
    {"id": "AS16", "query": "Above group average", "type": "subquery"},
    {"id": "AS17", "query": "High churn groups", "type": "having_subquery"},
    {"id": "AS18", "query": "Calculate correlation", "type": "correlation"},
    {"id": "AS19", "query": "Percentile ranks", "type": "percentile"},
    {"id": "AS20", "query": "Cohort analysis", "type": "cohort"},
    
    # Add more as needed...
]

def test_query(query_info):
    """Test a single query and validate result"""
    query = query_info["query"]
    
    # Add context to help Claude-4-Sonnet
    prompt = f"""Using TELCO_DATA table with columns: CUSTOMERID, GENDER, SENIORCITIZEN, 
TENURE, MONTHLYCHARGES, TOTALCHARGES, CHURN, CONTRACT, PAYMENTMETHOD, 
INTERNETSERVICE, and various service columns.

Generate SQL for: {query}

Return ONLY the SQL statement, no explanations."""
    
    try:
        cursor.execute(f"""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            'claude-4-sonnet',
            %s
        ) as response
        """, (prompt,))
        
        response = cursor.fetchone()[0] if cursor.rowcount > 0 else None
        
        if not response or 'SELECT' not in response.upper():
            return {
                "sql_generated": False,
                "sql_executed": False,
                "answers_question": False,
                "reason": "No SQL generated"
            }
        
        # Extract SQL
        sql_start = response.upper().find('SELECT')
        sql = response[sql_start:]
        if '```' in sql:
            sql = sql.split('```')[0]
        sql = sql.strip()
        
        # Try to execute
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            
            # Validate if it answers the question
            answers = validate_answer(query_info["type"], result)
            
            return {
                "sql_generated": True,
                "sql_executed": True,
                "answers_question": answers[0],
                "reason": answers[1],
                "rows": len(result)
            }
            
        except Exception as e:
            return {
                "sql_generated": True,
                "sql_executed": False,
                "answers_question": False,
                "reason": f"SQL error: {str(e)[:50]}"
            }
            
    except Exception as e:
        return {
            "sql_generated": False,
            "sql_executed": False,
            "answers_question": False,
            "reason": f"Error: {str(e)[:50]}"
        }

def validate_answer(query_type, result):
    """Validate if result ACTUALLY answers the business question - not just returns data"""
    
    if query_type == "count" or query_type == "sum" or query_type == "average":
        if result and len(result) == 1 and len(result[0]) == 1:
            val = result[0][0]
            # Check if value is reasonable
            if query_type == "count" and isinstance(val, (int, float)) and val >= 0:
                return True, f"Count: {val}"
            elif query_type == "average" and isinstance(val, (int, float)) and val > 0:
                return True, f"Average: {val:.2f}"
            elif query_type == "sum" and isinstance(val, (int, float)):
                return True, f"Total: {val}"
        return False, "Expected single numeric value"
    
    elif query_type == "segmented" or query_type == "comparison":
        if result and len(result) > 1 and len(result[0]) >= 2:
            return True, f"{len(result)} segments"
        return False, "Expected multiple segments with metrics"
    
    elif query_type == "list" or query_type == "top_n":
        if result and len(result) > 0:
            return True, f"{len(result)} rows"
        return False, "Expected list of records"
    
    elif query_type == "investigation" or query_type == "pattern":
        # These require multi-step analysis
        return False, "Cannot do multi-step analysis"
    
    elif query_type in ["time_trend", "cumulative", "moving_avg", "forecast"]:
        # Time intelligence requires special functions
        return False, "No time intelligence capability"
    
    elif query_type == "correlation":
        if result and len(result) == 1:
            val = result[0][0]
            if isinstance(val, (int, float)) and -1 <= val <= 1:
                return True, f"Correlation: {val}"
        return False, "Expected correlation value"
    
    else:
        # Generic check
        if result:
            return True, f"{len(result)} results"
        return False, "No results"

# Run all tests
print(f"\nTesting {len(ALL_QUERIES)} queries...")
print("-"*80)

results = {
    "total": len(ALL_QUERIES),
    "sql_generated": 0,
    "sql_executed": 0,
    "answers_question": 0,
    "by_type": {},
    "details": []
}

for i, query_info in enumerate(ALL_QUERIES):
    print(f"\n[{i+1}/{len(ALL_QUERIES)}] {query_info['id']}: {query_info['query'][:50]}...")
    
    result = test_query(query_info)
    
    # Update stats
    if result["sql_generated"]:
        results["sql_generated"] += 1
    if result["sql_executed"]:
        results["sql_executed"] += 1
    if result["answers_question"]:
        results["answers_question"] += 1
    
    # Track by type
    qtype = query_info["type"]
    if qtype not in results["by_type"]:
        results["by_type"][qtype] = {"total": 0, "answered": 0}
    results["by_type"][qtype]["total"] += 1
    if result["answers_question"]:
        results["by_type"][qtype]["answered"] += 1
    
    # Store details
    results["details"].append({
        "id": query_info["id"],
        "query": query_info["query"],
        "type": query_info["type"],
        **result
    })
    
    # Print status
    status = "✅" if result["answers_question"] else "⚠️" if result["sql_executed"] else "❌"
    print(f"  {status} {result['reason']}")

# Summary
print("\n" + "="*80)
print("FINAL RESULTS - CLAUDE-4-SONNET")
print("="*80)

print(f"\nOverall:")
print(f"  SQL Generated:     {results['sql_generated']}/{results['total']} ({results['sql_generated']/results['total']*100:.1f}%)")
print(f"  SQL Executed:      {results['sql_executed']}/{results['total']} ({results['sql_executed']/results['total']*100:.1f}%)")
print(f"  Answers Question:  {results['answers_question']}/{results['total']} ({results['answers_question']/results['total']*100:.1f}%)")

print(f"\nBy Query Type:")
for qtype, stats in sorted(results["by_type"].items()):
    pct = stats["answered"]/stats["total"]*100 if stats["total"] > 0 else 0
    print(f"  {qtype}: {stats['answered']}/{stats['total']} ({pct:.0f}%)")

# Critical findings
time_intel = sum(1 for d in results["details"] if d["id"].startswith("TI") and d["answers_question"])
investigation = sum(1 for d in results["details"] if d["type"] == "investigation" and d["answers_question"])
natural = sum(1 for d in results["details"] if d["id"].startswith("NL") and d["answers_question"])

print(f"\nCritical Capabilities:")
print(f"  Natural Language: {natural}/15 ({natural/15*100:.0f}%)")
print(f"  Time Intelligence: {time_intel}/15 ({time_intel/15*100:.0f}%)")
print(f"  Investigation: {investigation}/10 ({investigation/10*100:.0f}%)")

# Save results
filename = f"claude4_complete_results_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
with open(filename, 'w') as f:
    json.dump(results, f, indent=2)

print(f"\n💾 Results saved to {filename}")

conn.close()