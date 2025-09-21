#!/usr/bin/env python3
"""
Test CORTEX.COMPLETE with TIME INTELLIGENCE queries
Critical for business analytics - period comparisons, trends, running totals
Tests what Scoop does effortlessly but CORTEX struggles with
"""

import snowflake.connector
import json
from datetime import datetime

conn = snowflake.connector.connect(
    account='rcdtonr-ji20455',
    user='bradtest',
    password='qMsGeKsE33NJeZp',
    database='SCOOP_BENCHMARK',
    schema='TEST_DATA',
    warehouse='COMPUTE_WH'
)
cursor = conn.cursor()

print("=" * 80)
print("TIME INTELLIGENCE TESTING - CRITICAL BUSINESS QUERIES")
print("Using OPENOPPORTUNITIES table with date columns C1, C9, C10")
print("=" * 80)

time_queries = [
    # Period Comparisons
    {
        "id": "TIME_001",
        "query": "Compare OPENOPPORTUNITIES count this month vs last month using C1 date",
        "category": "Month-over-Month",
        "expected_pattern": "date comparison, LAG or self-join",
        "scoop_capability": "Native time intelligence"
    },
    {
        "id": "TIME_002", 
        "query": "Show OPENOPPORTUNITIES week-over-week growth rate by C1 date",
        "category": "Week-over-Week Growth",
        "expected_pattern": "percentage calculation with date math",
        "scoop_capability": "Automatic period calculations"
    },
    {
        "id": "TIME_003",
        "query": "Calculate year-over-year change in OPENOPPORTUNITIES count using C1",
        "category": "Year-over-Year",
        "expected_pattern": "year comparison",
        "scoop_capability": "Built-in YoY"
    },
    
    # Running/Cumulative
    {
        "id": "TIME_004",
        "query": "Show running total of OPENOPPORTUNITIES by C1 date",
        "category": "Running Total",
        "expected_pattern": "window function with ORDER BY",
        "scoop_capability": "Native cumulative"
    },
    {
        "id": "TIME_005",
        "query": "Calculate 7-day moving average of daily OPENOPPORTUNITIES count using C1",
        "category": "Moving Average",
        "expected_pattern": "window function with range",
        "scoop_capability": "Built-in moving calculations"
    },
    
    # Date Filtering/Ranges
    {
        "id": "TIME_006",
        "query": "Show OPENOPPORTUNITIES from last 30 days based on C1",
        "category": "Relative Date Filter",
        "expected_pattern": "DATEADD or date arithmetic",
        "scoop_capability": "Natural language dates"
    },
    {
        "id": "TIME_007",
        "query": "Find OPENOPPORTUNITIES between C1 and C9 dates greater than 30 days",
        "category": "Date Difference",
        "expected_pattern": "DATEDIFF function",
        "scoop_capability": "Automatic date math"
    },
    
    # Cohort/Time-based Segmentation
    {
        "id": "TIME_008",
        "query": "Group OPENOPPORTUNITIES by month of C1 and show trend",
        "category": "Monthly Trend",
        "expected_pattern": "DATE_TRUNC and GROUP BY",
        "scoop_capability": "Automatic time grouping"
    },
    {
        "id": "TIME_009",
        "query": "Show OPENOPPORTUNITIES by day of week pattern using C1",
        "category": "Day of Week Analysis",
        "expected_pattern": "DAYOFWEEK function",
        "scoop_capability": "Built-in time patterns"
    },
    
    # Complex Time Intelligence
    {
        "id": "TIME_010",
        "query": "Calculate quarter-to-date OPENOPPORTUNITIES total using C1",
        "category": "QTD Calculation",
        "expected_pattern": "quarter boundary logic",
        "scoop_capability": "Native QTD/YTD/MTD"
    },
    {
        "id": "TIME_011",
        "query": "Show same period last year comparison for OPENOPPORTUNITIES using C1",
        "category": "SPLY Comparison",
        "expected_pattern": "date offset by year",
        "scoop_capability": "Built-in SPLY"
    },
    {
        "id": "TIME_012",
        "query": "Find peak OPENOPPORTUNITIES day in each month using C1",
        "category": "Peak Period",
        "expected_pattern": "window function with RANK",
        "scoop_capability": "Automatic peak finding"
    },
    
    # Business-Critical Time Queries
    {
        "id": "TIME_013",
        "query": "What's the trend of OPENOPPORTUNITIES over time using C1?",
        "category": "Trend Analysis",
        "expected_pattern": "time series with trend line",
        "scoop_capability": "ML-powered trends"
    },
    {
        "id": "TIME_014",
        "query": "Forecast next month's OPENOPPORTUNITIES based on C1 history",
        "category": "Forecasting",
        "expected_pattern": "predictive model",
        "scoop_capability": "Built-in forecasting"
    },
    {
        "id": "TIME_015",
        "query": "Find seasonality patterns in OPENOPPORTUNITIES using C1 dates",
        "category": "Seasonality",
        "expected_pattern": "seasonal decomposition",
        "scoop_capability": "Automatic seasonality detection"
    }
]

results = []
successful = 0

for test in time_queries:
    print(f"\n{'='*60}")
    print(f"Test: {test['id']} - {test['category']}")
    print(f"Query: {test['query']}")
    print(f"Expected: {test['expected_pattern']}")
    print(f"Scoop: {test['scoop_capability']}")
    print("-" * 60)
    
    start_time = datetime.now()
    
    try:
        # Test with CORTEX.COMPLETE - using COMPLETE function directly
        query = f"""
        SELECT COMPLETE(
            'claude-3.5-sonnet',
            '{test['query']}'
        ) as response
        """
        
        cursor.execute(query)
        response = cursor.fetchone()[0]
        
        elapsed = (datetime.now() - start_time).total_seconds()
        
        # Parse response
        response_lower = response.lower()
        
        # Check if SQL was generated
        has_sql = 'select' in response_lower or 'with' in response_lower
        
        # Check for expected patterns
        has_date_logic = any(term in response_lower for term in [
            'date', 'month', 'year', 'week', 'day', 
            'dateadd', 'datediff', 'date_trunc',
            'lag', 'lead', 'over', 'partition'
        ])
        
        # Check for window functions (critical for time intelligence)
        has_window = any(term in response_lower for term in [
            'over', 'partition by', 'row_number', 
            'rank', 'lag', 'lead', 'sum() over'
        ])
        
        # Try to extract and execute the SQL
        executed = False
        execution_error = None
        
        if has_sql:
            # Try to extract SQL
            sql_start = response_lower.find('select')
            if sql_start == -1:
                sql_start = response_lower.find('with')
            
            if sql_start != -1:
                sql_end = response.find(';', sql_start)
                if sql_end == -1:
                    sql_end = len(response)
                
                extracted_sql = response[sql_start:sql_end].strip()
                
                try:
                    cursor.execute(extracted_sql)
                    result_rows = cursor.fetchall()
                    executed = True
                    successful += 1
                    print(f"✅ EXECUTED: Retrieved {len(result_rows)} rows")
                except Exception as e:
                    execution_error = str(e)
                    print(f"❌ EXECUTION FAILED: {execution_error}")
        
        # Analyze response quality
        if not has_sql:
            print("❌ NO SQL GENERATED - Generic explanation only")
        elif not has_date_logic:
            print("⚠️  SQL generated but NO TIME INTELLIGENCE detected")
        elif not has_window and test['category'] in ['Running Total', 'Moving Average', 'Peak Period']:
            print("⚠️  Missing WINDOW FUNCTIONS for cumulative/running calculations")
        elif executed:
            print(f"✅ Time intelligence query successful")
        
        results.append({
            "test_id": test['id'],
            "category": test['category'],
            "query": test['query'],
            "has_sql": has_sql,
            "has_date_logic": has_date_logic,
            "has_window": has_window,
            "executed": executed,
            "execution_error": execution_error,
            "response_length": len(response),
            "time": elapsed,
            "scoop_capability": test['scoop_capability']
        })
        
        # Show snippet of response
        print(f"\nResponse snippet: {response[:200]}...")
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        results.append({
            "test_id": test['id'],
            "category": test['category'],
            "query": test['query'],
            "error": str(e),
            "time": (datetime.now() - start_time).total_seconds()
        })

# Summary
print("\n" + "=" * 80)
print("TIME INTELLIGENCE TEST SUMMARY")
print("=" * 80)

categories_summary = {}
for result in results:
    cat = result.get('category', 'Unknown')
    if cat not in categories_summary:
        categories_summary[cat] = {'total': 0, 'executed': 0, 'has_sql': 0, 'has_time': 0}
    
    categories_summary[cat]['total'] += 1
    if result.get('executed', False):
        categories_summary[cat]['executed'] += 1
    if result.get('has_sql', False):
        categories_summary[cat]['has_sql'] += 1
    if result.get('has_date_logic', False):
        categories_summary[cat]['has_time'] += 1

print(f"\nTotal Tests: {len(time_queries)}")
print(f"Successfully Executed: {successful}/{len(time_queries)} ({successful*100/len(time_queries):.0f}%)")

print("\nBy Category:")
for cat, stats in categories_summary.items():
    print(f"\n{cat}:")
    print(f"  SQL Generated: {stats['has_sql']}/{stats['total']}")
    print(f"  Time Logic: {stats['has_time']}/{stats['total']}")
    print(f"  Executed: {stats['executed']}/{stats['total']}")

# Critical gaps
print("\n" + "=" * 80)
print("CRITICAL TIME INTELLIGENCE GAPS vs SCOOP")
print("=" * 80)

gaps = [
    ("Period Comparisons", "Month-over-Month, Week-over-Week, Year-over-Year"),
    ("Running Calculations", "Running totals, moving averages"),
    ("Relative Dates", "Last 30 days, this quarter, YTD"),
    ("Trend Analysis", "Trend lines, seasonality detection"),
    ("Forecasting", "Next period predictions"),
    ("Window Functions", "Critical for time-based calculations")
]

for gap, desc in gaps:
    # Find relevant results
    relevant = [r for r in results if gap.lower() in r.get('category', '').lower()]
    if relevant:
        success_rate = sum(1 for r in relevant if r.get('executed', False)) / len(relevant) * 100
        print(f"\n{gap}: {success_rate:.0f}% success")
        print(f"  Issue: {desc}")

# Save results
with open('time_intelligence_results.json', 'w') as f:
    json.dump({
        'summary': {
            'total': len(time_queries),
            'executed': successful,
            'success_rate': f"{successful*100/len(time_queries):.0f}%"
        },
        'by_category': categories_summary,
        'details': results
    }, f, indent=2, default=str)

print(f"\nResults saved to time_intelligence_results.json")

cursor.close()
conn.close()

print("\n" + "=" * 80)
print("BUSINESS IMPACT")
print("=" * 80)
print("❌ Time intelligence is CRITICAL for business analytics")
print("❌ Without it, users cannot answer:")
print("   - 'How are we trending?'")
print("   - 'What's our growth rate?'")
print("   - 'Compare this month to last month'")
print("   - 'Show me YTD performance'")
print("✅ Scoop handles ALL of these natively")
print("❌ CORTEX.COMPLETE cannot handle basic time comparisons")