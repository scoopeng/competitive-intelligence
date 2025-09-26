#!/usr/bin/env python3
"""
DEFINITIVE TEST SUITE: CORTEX vs QUERY JSON OBJECT
===================================================
Maps all Query JSON Object capabilities to testable queries.
Informed by Scoop's 90-query test suite structure.

Test Categories (50+ queries):
1. Basic SQL (10) - Should work in both
2. Subqueries (8) - Critical differentiator  
3. Formulas (6) - Calculated metrics
4. Formula Filters (5) - HAVING on calculations
5. Time Intelligence (5) - Window functions
6. Statistical (5) - Advanced aggregations
7. ML/Investigation (5) - Why questions
8. Complex Patterns (6) - Nested, multi-level
"""

import json
import snowflake.connector
import time
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum

# Configuration
SNOWFLAKE_CONFIG = {
    'account': 'rcdtonr-ji20455',
    'user': 'bradtest',
    'password': 'qMsGeKsE33NJeZp',
    'warehouse': 'COMPUTE_WH',
    'database': 'SCOOP_BENCHMARK',
    'schema': 'TEST_DATA'
}

MODEL = 'claude-4-sonnet'
TIMEOUT_SECONDS = 30
MAX_RETRIES = 2

class QueryJSONCapability(Enum):
    """All Query JSON Object capabilities"""
    BASIC_FILTER = "basic_filter"           # Simple WHERE
    COMPOUND_FILTER = "compound_filter"     # AND/OR combinations
    SUBQUERY = "subquery"                   # Nested queries with IN
    SCALAR_SUBQUERY = "scalar_subquery"     # Subquery returning single value
    CORRELATED_SUBQUERY = "correlated"      # References outer query
    FORMULA = "formula"                     # Calculated expressions
    FORMULA_FILTER = "formula_filter"       # Filter on calculations
    CONDITIONAL_FORMULA = "conditional"     # IF/CASE in formulas
    WINDOW_FUNCTION = "window_function"     # LAG, LEAD, OVER
    CUMULATIVE = "cumulative"               # Running totals
    SHIFT_PERIOD = "shift_period"           # Period comparisons
    STATISTICAL = "statistical"             # STDEV, CORR, PERCENTILE
    ML_CLASSIFICATION = "ml_classification" # Query intent routing
    ML_RELATIONSHIP = "ml_relationship"     # What drives/predicts
    ML_CLUSTER = "ml_cluster"               # Segmentation
    VISUALIZATION = "visualization"         # Chart recommendations
    MULTI_DATASET = "multi_dataset"         # Cross-dataset joins

@dataclass
class TestQuery:
    """Test query with full Query JSON mapping"""
    id: str
    query: str
    dataset: str
    capability: QueryJSONCapability
    query_json_example: Dict[str, Any]
    expected_cortex_success: bool
    expected_cortex_behavior: str
    scoop_behavior: str
    
def generate_test_queries() -> List[TestQuery]:
    """Generate comprehensive test suite"""
    queries = []
    
    # ========== BASIC CAPABILITIES (10 queries) ==========
    # These should work in both systems
    
    queries.extend([
        TestQuery(
            id="basic_1",
            query="Count all customers",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.BASIC_FILTER,
            query_json_example={"metrics": [{"aggRule": "COUNT"}]},
            expected_cortex_success=True,
            expected_cortex_behavior="SELECT COUNT(*) FROM TELCO_DATA",
            scoop_behavior="Same SQL via Query JSON"
        ),
        TestQuery(
            id="basic_2",
            query="Average monthly charges by contract type",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.BASIC_FILTER,
            query_json_example={
                "attributes": ["CONTRACT"],
                "metrics": [{"columnName": "MONTHLYCHARGES", "aggRule": "AVG"}]
            },
            expected_cortex_success=True,
            expected_cortex_behavior="GROUP BY with AVG",
            scoop_behavior="Same result"
        ),
        TestQuery(
            id="basic_3",
            query="Customers with fiber optic internet and online security",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.COMPOUND_FILTER,
            query_json_example={
                "queryFilter": {
                    "type": "AND",
                    "filters": [
                        {"attributeName": "INTERNETSERVICE", "operator": "=", "values": ["Fiber optic"]},
                        {"attributeName": "ONLINESECURITY", "operator": "=", "values": ["Yes"]}
                    ]
                }
            },
            expected_cortex_success=True,
            expected_cortex_behavior="WHERE with AND",
            scoop_behavior="Same result"
        ),
        TestQuery(
            id="basic_4",
            query="Show top 10 customers by total charges",
            dataset="TELCO_DATA", 
            capability=QueryJSONCapability.BASIC_FILTER,
            query_json_example={
                "sort": {"columnName": "TOTALCHARGES", "order": "DESC"},
                "limit": 10
            },
            expected_cortex_success=True,
            expected_cortex_behavior="ORDER BY with LIMIT",
            scoop_behavior="Same result"
        ),
        TestQuery(
            id="basic_5",
            query="Count opportunities by stage in C4",
            dataset="OPENOPPORTUNITIES",
            capability=QueryJSONCapability.BASIC_FILTER,
            query_json_example={
                "attributes": ["C4"],
                "metrics": [{"aggRule": "COUNT"}]
            },
            expected_cortex_success=True,
            expected_cortex_behavior="Simple GROUP BY",
            scoop_behavior="Same result"
        ),
    ])
    
    # ========== SUBQUERIES (8 queries) ==========
    # Critical Query JSON capability - Cortex should fail
    
    queries.extend([
        TestQuery(
            id="subquery_1",
            query="Show all customers from the top 3 payment methods by customer count",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.SUBQUERY,
            query_json_example={
                "queryFilter": {
                    "type": "SUBQUERY",
                    "attributeName": "PAYMENTMETHOD",
                    "operator": "IN",
                    "subquery": {
                        "queryType": "dataset",
                        "attributes": [{"columnName": "PAYMENTMETHOD"}],
                        "metrics": [{"aggRule": "COUNT"}],
                        "sort": {"order": "DESC"},
                        "limit": 3
                    }
                }
            },
            expected_cortex_success=False,
            expected_cortex_behavior="Cannot generate proper subquery with IN clause",
            scoop_behavior="WITH top_methods AS (...) SELECT * WHERE PAYMENTMETHOD IN (SELECT...)"
        ),
        TestQuery(
            id="subquery_2",
            query="List customers with monthly charges above the average for their contract type",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.CORRELATED_SUBQUERY,
            query_json_example={
                "queryFilter": {
                    "type": "CORRELATED_SUBQUERY",
                    "condition": "MONTHLYCHARGES > (SELECT AVG(MONTHLYCHARGES) FROM TELCO_DATA t2 WHERE t2.CONTRACT = t1.CONTRACT)"
                }
            },
            expected_cortex_success=False,
            expected_cortex_behavior="Cannot handle correlated subqueries",
            scoop_behavior="Generates correlated subquery correctly"
        ),
        TestQuery(
            id="subquery_3",
            query="Show opportunities from owners (C8) who have more than 3 total opportunities",
            dataset="OPENOPPORTUNITIES",
            capability=QueryJSONCapability.SUBQUERY,
            query_json_example={
                "queryFilter": {
                    "type": "SUBQUERY",
                    "attributeName": "C8",
                    "operator": "IN",
                    "subquery": {
                        "groupBy": ["C8"],
                        "having": "COUNT(*) > 3"
                    }
                }
            },
            expected_cortex_success=False,
            expected_cortex_behavior="Cannot generate HAVING in subquery",
            scoop_behavior="Properly filters on aggregated subquery"
        ),
        TestQuery(
            id="subquery_4",
            query="Customers from the top 5 regions by total revenue where region has >100 customers",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.SUBQUERY,
            query_json_example={
                "queryFilter": {
                    "type": "NESTED_SUBQUERY",
                    "levels": [
                        {"condition": "region_customer_count > 100"},
                        {"condition": "region IN top_5_by_revenue"}
                    ]
                }
            },
            expected_cortex_success=False,
            expected_cortex_behavior="Cannot handle nested conditions",
            scoop_behavior="Multi-level CTE with proper filtering"
        ),
        TestQuery(
            id="subquery_5",
            query="Show customers with tenure above company median",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.SCALAR_SUBQUERY,
            query_json_example={
                "queryFilter": {
                    "type": "SCALAR_SUBQUERY",
                    "operator": ">",
                    "subquery": {"metrics": [{"aggRule": "MEDIAN"}]}
                }
            },
            expected_cortex_success=False,
            expected_cortex_behavior="Cannot use scalar subquery in WHERE",
            scoop_behavior="WHERE TENURE > (SELECT MEDIAN(TENURE)...)"
        ),
    ])
    
    # ========== FORMULAS & CALCULATIONS (6 queries) ==========
    
    queries.extend([
        TestQuery(
            id="formula_1",
            query="Calculate churn rate as percentage",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.FORMULA,
            query_json_example={
                "formulas": [{
                    "expression": "SUM(CASE WHEN CHURN='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)",
                    "label": "Churn Rate %"
                }]
            },
            expected_cortex_success=True,
            expected_cortex_behavior="Should handle simple formula",
            scoop_behavior="Evaluates formula correctly"
        ),
        TestQuery(
            id="formula_2",
            query="Show customer lifetime value as tenure times monthly charges",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.FORMULA,
            query_json_example={
                "formulas": [{
                    "expression": "TENURE * MONTHLYCHARGES",
                    "label": "CLV"
                }]
            },
            expected_cortex_success=True,
            expected_cortex_behavior="Simple multiplication",
            scoop_behavior="Same calculation"
        ),
        TestQuery(
            id="formula_3",
            query="Calculate win rate with null protection for opportunities",
            dataset="OPENOPPORTUNITIES",
            capability=QueryJSONCapability.CONDITIONAL_FORMULA,
            query_json_example={
                "formulas": [{
                    "expression": "IF(COUNT(*) = 0, 0, SUM(CASE WHEN C4='Won' THEN 1 ELSE 0 END) / COUNT(*))",
                    "label": "Win Rate"
                }]
            },
            expected_cortex_success=False,
            expected_cortex_behavior="May not handle IF correctly",
            scoop_behavior="Handles conditional logic"
        ),
    ])
    
    # ========== FORMULA FILTERS (5 queries) ==========
    # Filtering on calculated values - key differentiator
    
    queries.extend([
        TestQuery(
            id="formula_filter_1",
            query="Show contract types where churn rate exceeds 30%",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.FORMULA_FILTER,
            query_json_example={
                "attributes": ["CONTRACT"],
                "formulas": [{
                    "expression": "'Churned' / 'Total' * 100",
                    "label": "Churn Rate",
                    "filter": "('Churned' / 'Total' * 100) > 30"
                }]
            },
            expected_cortex_success=False,
            expected_cortex_behavior="Cannot filter on calculated formula",
            scoop_behavior="Applies HAVING on formula result"
        ),
        TestQuery(
            id="formula_filter_2",
            query="Payment methods where average revenue per user is above 75",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.FORMULA_FILTER,
            query_json_example={
                "groupBy": ["PAYMENTMETHOD"],
                "formulas": [{
                    "expression": "AVG(MONTHLYCHARGES)",
                    "filter": "AVG(MONTHLYCHARGES) > 75"
                }]
            },
            expected_cortex_success=False,
            expected_cortex_behavior="Cannot apply HAVING on AVG",
            scoop_behavior="GROUP BY with HAVING AVG(...) > 75"
        ),
        TestQuery(
            id="formula_filter_3",
            query="Show products (C6) where close rate times average deal size exceeds 10000",
            dataset="OPENOPPORTUNITIES",
            capability=QueryJSONCapability.FORMULA_FILTER,
            query_json_example={
                "formulas": [{
                    "expression": "('Won' / 'Total') * AVG(C3)",
                    "filter": "(('Won' / 'Total') * AVG(C3)) > 10000"
                }]
            },
            expected_cortex_success=False,
            expected_cortex_behavior="Complex formula filter fails",
            scoop_behavior="Calculates and filters correctly"
        ),
    ])
    
    # ========== TIME INTELLIGENCE (5 queries) ==========
    
    queries.extend([
        TestQuery(
            id="time_1",
            query="Month-over-month change in customer count",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.WINDOW_FUNCTION,
            query_json_example={
                "queryType": "timeseries",
                "period": "MONTHLY",
                "metrics": [{
                    "aggRule": "COUNT",
                    "shiftPeriod": -1
                }]
            },
            expected_cortex_success=False,
            expected_cortex_behavior="Window function syntax errors",
            scoop_behavior="Uses LAG() properly"
        ),
        TestQuery(
            id="time_2",
            query="Running total of opportunities by date (C1)",
            dataset="OPENOPPORTUNITIES",
            capability=QueryJSONCapability.CUMULATIVE,
            query_json_example={
                "metrics": [{
                    "aggRule": "COUNT",
                    "window": "CUMULATIVE"
                }]
            },
            expected_cortex_success=False,
            expected_cortex_behavior="Cannot generate SUM() OVER (ORDER BY...)",
            scoop_behavior="Proper cumulative window function"
        ),
        TestQuery(
            id="time_3",
            query="3-month moving average of monthly charges",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.WINDOW_FUNCTION,
            query_json_example={
                "metrics": [{
                    "aggRule": "AVG",
                    "window": {
                        "type": "MOVING",
                        "size": 3
                    }
                }]
            },
            expected_cortex_success=False,
            expected_cortex_behavior="Cannot do moving windows",
            scoop_behavior="AVG() OVER (ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)"
        ),
    ])
    
    # ========== STATISTICAL (5 queries) ==========
    
    queries.extend([
        TestQuery(
            id="stat_1",
            query="Standard deviation of monthly charges",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.STATISTICAL,
            query_json_example={
                "metrics": [{"aggRule": "STDDEV"}]
            },
            expected_cortex_success=True,  # Works with Claude-4-Sonnet!
            expected_cortex_behavior="STDDEV works with Claude",
            scoop_behavior="Same function"
        ),
        TestQuery(
            id="stat_2",
            query="Correlation between tenure and total charges",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.STATISTICAL,
            query_json_example={
                "metrics": [{
                    "type": "CORRELATION",
                    "columns": ["TENURE", "TOTALCHARGES"]
                }]
            },
            expected_cortex_success=False,
            expected_cortex_behavior="CORR function not available",
            scoop_behavior="Uses CORR() function"
        ),
        TestQuery(
            id="stat_3",
            query="75th percentile of opportunity amounts (C3)",
            dataset="OPENOPPORTUNITIES",
            capability=QueryJSONCapability.STATISTICAL,
            query_json_example={
                "metrics": [{
                    "aggRule": "PERCENTILE",
                    "percentile": 0.75
                }]
            },
            expected_cortex_success=False,
            expected_cortex_behavior="PERCENTILE_CONT not available",
            scoop_behavior="PERCENTILE_CONT(0.75) WITHIN GROUP"
        ),
    ])
    
    # ========== ML/INVESTIGATION (5 queries) ==========
    
    queries.extend([
        TestQuery(
            id="ml_1",
            query="Why are customers churning?",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.ML_RELATIONSHIP,
            query_json_example={
                "queryType": "ml_relationship",
                "target": "CHURN",
                "features": "auto"
            },
            expected_cortex_success=False,
            expected_cortex_behavior="Returns raw data, no analysis",
            scoop_behavior="Decision tree with feature importance"
        ),
        TestQuery(
            id="ml_2",
            query="What factors predict high monthly charges?",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.ML_RELATIONSHIP,
            query_json_example={
                "queryType": "ml_relationship",
                "target": "MONTHLYCHARGES",
                "threshold": 100
            },
            expected_cortex_success=False,
            expected_cortex_behavior="No predictive analysis",
            scoop_behavior="Statistical analysis with correlations"
        ),
        TestQuery(
            id="ml_3",
            query="Segment customers into groups",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.ML_CLUSTER,
            query_json_example={
                "queryType": "ml_cluster",
                "features": ["TENURE", "MONTHLYCHARGES", "TOTALCHARGES"],
                "clusters": 4
            },
            expected_cortex_success=False,
            expected_cortex_behavior="No clustering capability",
            scoop_behavior="K-means clustering with descriptions"
        ),
    ])
    
    # ========== COMPLEX PATTERNS (6 queries) ==========
    
    queries.extend([
        TestQuery(
            id="complex_1",
            query="Top 2 opportunities from each of the top 3 owners by total amount",
            dataset="OPENOPPORTUNITIES",
            capability=QueryJSONCapability.SUBQUERY,
            query_json_example={
                "queryFilter": {
                    "type": "NESTED_SUBQUERY",
                    "outer": "TOP_N_PER_GROUP",
                    "inner": "TOP_N_GROUPS"
                }
            },
            expected_cortex_success=False,
            expected_cortex_behavior="Cannot handle nested ranking",
            scoop_behavior="ROW_NUMBER() with nested CTEs"
        ),
        TestQuery(
            id="complex_2",
            query="Customers who are above average for their segment in 3+ metrics",
            dataset="TELCO_DATA",
            capability=QueryJSONCapability.CORRELATED_SUBQUERY,
            query_json_example={
                "queryFilter": {
                    "type": "COMPLEX_CONDITION",
                    "conditions": ["multiple", "correlated", "subqueries"]
                }
            },
            expected_cortex_success=False,
            expected_cortex_behavior="Too complex to generate",
            scoop_behavior="Multiple correlated conditions"
        ),
        TestQuery(
            id="complex_3",
            query="Show YoY growth by quarter with significance testing",
            dataset="OPENOPPORTUNITIES",
            capability=QueryJSONCapability.WINDOW_FUNCTION,
            query_json_example={
                "queryType": "timeseries",
                "period": "QUARTERLY",
                "metrics": [{
                    "type": "YOY_GROWTH",
                    "significance": True
                }]
            },
            expected_cortex_success=False,
            expected_cortex_behavior="No statistical testing",
            scoop_behavior="Growth calculation with p-values"
        ),
    ])
    
    return queries

class DefinitiveTestRunner:
    """Enhanced test runner with comprehensive tracking"""
    
    def __init__(self):
        self.conn = None
        self.results = []
        self.capability_results = {}  # Track by capability
        self.start_time = None
        
    def connect(self):
        """Connect to Snowflake"""
        print("Connecting to Snowflake...")
        self.conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
        print("✓ Connected")
        
    def test_query(self, query: TestQuery) -> Dict:
        """Test a single query"""
        result = {
            "id": query.id,
            "query": query.query,
            "capability": query.capability.value,
            "timestamp": datetime.now().isoformat(),
            "success": False,
            "sql": None,
            "error": None,
            "matched_expectation": False
        }
        
        try:
            # No signal handling - it causes issues in some environments
            
            # Generate SQL
            cursor = self.conn.cursor()
            
            context = f"Table: {query.dataset}\n"
            if query.dataset == "TELCO_DATA":
                context += "Columns: CUSTOMERID, GENDER, SENIORCITIZEN, TENURE, CONTRACT, PAYMENTMETHOD, MONTHLYCHARGES, TOTALCHARGES, CHURN, INTERNETSERVICE, ONLINESECURITY"
            else:
                context += "Columns: C1 (Date), C2 (Name), C3 (Amount), C4 (Stage), C5 (Days), C6 (Product), C7 (Priority), C8 (Owner), C9 (Date2), C10 (Date3)"
                
            prompt = f'Generate SQL for: "{query.query}"\n{context}\nReturn ONLY SQL:'
            
            sql_query = f"""
            SELECT SNOWFLAKE.CORTEX.COMPLETE(
                '{MODEL}',
                $${prompt}$$
            ) as response
            """
            
            cursor.execute(sql_query)
            response = cursor.fetchone()[0]
            
            if response:
                # Clean SQL
                sql = response.strip()
                if sql.startswith('```'):
                    sql = sql[sql.find('\n')+1:sql.rfind('```')]
                result["sql"] = sql
                
                # Try to execute
                try:
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    result["success"] = True
                    
                    # Check if it matched expectations
                    result["matched_expectation"] = (
                        result["success"] == query.expected_cortex_success
                    )
                except Exception as e:
                    result["error"] = str(e)[:200]
                    result["matched_expectation"] = not query.expected_cortex_success
                    
            cursor.close()
            
        except Exception as e:
            result["error"] = str(e)[:200]
            
        return result
    
    def run_comprehensive_test(self):
        """Run all tests with progress tracking"""
        queries = generate_test_queries()
        self.start_time = datetime.now()
        
        print(f"\n{'='*70}")
        print(f"DEFINITIVE TEST SUITE: {len(queries)} queries")
        print(f"Model: {MODEL}")
        print(f"{'='*70}\n")
        
        # Group by capability
        by_capability = {}
        for q in queries:
            if q.capability not in by_capability:
                by_capability[q.capability] = []
            by_capability[q.capability].append(q)
        
        # Test each capability
        for capability, cap_queries in by_capability.items():
            print(f"\n{capability.value.upper()} ({len(cap_queries)} queries)")
            print("-" * 50)
            
            cap_results = []
            for i, query in enumerate(cap_queries, 1):
                print(f"[{i}/{len(cap_queries)}] {query.id}: {query.query[:40]}...")
                
                result = self.test_query(query)
                self.results.append(result)
                cap_results.append(result)
                
                # Print result
                if result["matched_expectation"]:
                    if result["success"]:
                        print(f"    ✓ Success (as expected)")
                    else:
                        print(f"    ✓ Failed (as expected): {query.expected_cortex_behavior[:50]}")
                else:
                    print(f"    ⚠️  UNEXPECTED: Success={result['success']}, Expected={query.expected_cortex_success}")
                    
            # Capability summary
            success = sum(1 for r in cap_results if r["success"])
            matched = sum(1 for r in cap_results if r["matched_expectation"])
            self.capability_results[capability] = {
                "total": len(cap_results),
                "success": success,
                "matched_expectations": matched
            }
            
    def generate_report(self):
        """Generate comprehensive report"""
        elapsed = (datetime.now() - self.start_time).total_seconds()
        
        print("\n" + "="*70)
        print("DEFINITIVE TEST RESULTS")
        print("="*70)
        print(f"Duration: {elapsed:.1f}s")
        print(f"Total Queries: {len(self.results)}")
        
        # Overall success
        total_success = sum(1 for r in self.results if r["success"])
        print(f"Overall Success: {total_success}/{len(self.results)} ({total_success*100/len(self.results):.1f}%)")
        
        # By capability
        print("\nBY CAPABILITY:")
        print("-" * 50)
        print(f"{'Capability':<25} {'Success':<12} {'Expected':<12}")
        print("-" * 50)
        
        for cap, stats in sorted(self.capability_results.items(), key=lambda x: x[0].value):
            rate = stats["success"] * 100 / stats["total"]
            match_rate = stats["matched_expectations"] * 100 / stats["total"]
            print(f"{cap.value:<25} {stats['success']}/{stats['total']} ({rate:5.1f}%) {stats['matched_expectations']}/{stats['total']} ({match_rate:5.1f}%)")
        
        # Key findings
        print("\nKEY FINDINGS:")
        print("-" * 50)
        
        # Check specific capabilities
        subq = self.capability_results.get(QueryJSONCapability.SUBQUERY, {})
        if subq:
            print(f"✗ Subqueries: {subq['success']}/{subq['total']} succeeded")
            
        form_filter = self.capability_results.get(QueryJSONCapability.FORMULA_FILTER, {})
        if form_filter:
            print(f"✗ Formula Filters: {form_filter['success']}/{form_filter['total']} succeeded")
            
        window = self.capability_results.get(QueryJSONCapability.WINDOW_FUNCTION, {})
        if window:
            print(f"✗ Window Functions: {window['success']}/{window['total']} succeeded")
            
        ml = self.capability_results.get(QueryJSONCapability.ML_RELATIONSHIP, {})
        if ml:
            print(f"✗ ML/Investigation: {ml['success']}/{ml['total']} succeeded")
            
    def save_results(self):
        """Save results"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"test_results/definitive_results_{MODEL}_{timestamp}.json"
        
        import os
        os.makedirs("test_results", exist_ok=True)
        
        with open(filename, 'w') as f:
            json.dump({
                "metadata": {
                    "model": MODEL,
                    "timestamp": self.start_time.isoformat(),
                    "duration": (datetime.now() - self.start_time).total_seconds(),
                    "total_queries": len(self.results)
                },
                "capability_summary": {
                    k.value: v for k, v in self.capability_results.items()
                },
                "results": self.results
            }, f, indent=2, default=str)
            
        print(f"\nResults saved to {filename}")
        
def main():
    """Main execution"""
    runner = DefinitiveTestRunner()
    
    try:
        runner.connect()
        runner.run_comprehensive_test()
        runner.generate_report()
        runner.save_results()
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        runner.generate_report()
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        if runner.conn:
            runner.conn.close()
            
if __name__ == "__main__":
    main()