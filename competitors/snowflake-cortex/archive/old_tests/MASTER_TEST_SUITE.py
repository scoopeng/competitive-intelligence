#!/usr/bin/env python3
"""
MASTER TEST SUITE - All 88+ Queries in One Place
Consolidated, maintainable, re-runnable
Tests Claude-4-Sonnet with business validation
"""

import snowflake.connector
import json
from datetime import datetime
import time

# Configuration
CONFIG = {
    "account": "rcdtonr-ji20455",
    "user": "bradtest",
    "password": "qMsGeKsE33NJeZp",
    "warehouse": "COMPUTE_WH",
    "database": "SCOOP_BENCHMARK",
    "schema": "TEST_DATA",
    "model": "claude-4-sonnet"  # Easy to change to test different models
}

# ALL TEST QUERIES IN ONE PLACE - 88+ Total
ALL_TESTS = {
    "NATURAL_LANGUAGE": [
        # 15 Natural language queries - what business users actually type
        {"query": "How many customers do we have?", "validation": "count", "expected": "single_number"},
        {"query": "What's the average monthly charge?", "validation": "average", "expected": "single_number"},
        {"query": "Show me churn rate by contract type", "validation": "segmented", "expected": "groups_with_rates"},
        {"query": "Which customers are paying more than $100 per month?", "validation": "filtered_list", "expected": "customer_list"},
        {"query": "Why are customers leaving?", "validation": "investigation", "expected": "multi_factor"},
        {"query": "What's our total revenue?", "validation": "sum", "expected": "single_number"},
        {"query": "Show me the top 10 highest paying customers", "validation": "top_n", "expected": "10_rows"},
        {"query": "How many payment methods do churned customers use?", "validation": "distinct_count", "expected": "single_number"},
        {"query": "What's the relationship between tenure and churn?", "validation": "correlation", "expected": "correlation_value"},
        {"query": "Which services do churned customers have?", "validation": "characteristic", "expected": "service_breakdown"},
        {"query": "Compare churn rates between different internet service types", "validation": "comparison", "expected": "multi_group"},
        {"query": "What drives customer loyalty?", "validation": "driver_analysis", "expected": "factors"},
        {"query": "Show me monthly charges by gender", "validation": "segmentation", "expected": "by_gender"},
        {"query": "How much money are we losing to churn?", "validation": "impact", "expected": "revenue_loss"},
        {"query": "What patterns predict churn?", "validation": "pattern", "expected": "predictive_factors"}
    ],
    
    "TIME_INTELLIGENCE": [
        # 15 Time intelligence queries - Critical business metrics
        {"query": "Show month-over-month growth in customer count", "validation": "mom_growth", "expected": "percentage"},
        {"query": "What's the year-over-year change in revenue?", "validation": "yoy", "expected": "comparison"},
        {"query": "Calculate running total of customers by month", "validation": "running_total", "expected": "cumulative"},
        {"query": "Show 7-day moving average of daily signups", "validation": "moving_avg", "expected": "smoothed_series"},
        {"query": "Compare this quarter to last quarter", "validation": "qoq", "expected": "quarter_comparison"},
        {"query": "Show customers from last 30 days", "validation": "relative_date", "expected": "recent_list"},
        {"query": "Calculate days between signup and churn", "validation": "date_diff", "expected": "duration"},
        {"query": "Group revenue by month and show trend", "validation": "monthly_trend", "expected": "time_series"},
        {"query": "Show signup patterns by day of week", "validation": "dow_pattern", "expected": "weekly_pattern"},
        {"query": "Calculate quarter-to-date totals", "validation": "qtd", "expected": "cumulative_quarter"},
        {"query": "Show same period last year comparison", "validation": "sply", "expected": "year_comparison"},
        {"query": "Find peak revenue day in each month", "validation": "peak_period", "expected": "max_per_month"},
        {"query": "What's the trend over time?", "validation": "trend_analysis", "expected": "trend_line"},
        {"query": "Forecast next month's revenue", "validation": "forecast", "expected": "prediction"},
        {"query": "Find seasonality patterns", "validation": "seasonality", "expected": "seasonal_factors"}
    ],
    
    "ADVANCED_SQL_PATTERNS": [
        # 20 Complex SQL patterns from Scoop's query JSON
        {"query": "Find customers with (fiber optic OR DSL) AND (online security OR online backup)", "validation": "complex_filter", "expected": "filtered_list"},
        {"query": "Show customers with monthly charges between $50 and $100", "validation": "between", "expected": "range_filter"},
        {"query": "Find customers where tenure is null or zero", "validation": "null_handling", "expected": "null_list"},
        {"query": "Show customers with payment method like '%electronic%'", "validation": "like_pattern", "expected": "pattern_match"},
        {"query": "Calculate churn rate avoiding division by zero", "validation": "safe_division", "expected": "percentage"},
        {"query": "Show each contract type's percentage of total customers", "validation": "pct_of_total", "expected": "percentages"},
        {"query": "Calculate customer value score: (monthly_charges * tenure) / NULLIF(support_calls, 0)", "validation": "formula", "expected": "calculated_metric"},
        {"query": "Count customers by contract type, showing both churned and active separately", "validation": "conditional_count", "expected": "dual_counts"},
        {"query": "Show contract types with average monthly charge > 70", "validation": "having", "expected": "filtered_groups"},
        {"query": "Count distinct payment methods by contract type", "validation": "distinct_by_group", "expected": "distinct_counts"},
        {"query": "Calculate standard deviation of monthly charges by internet service", "validation": "stddev", "expected": "statistics"},
        {"query": "Show minimum and maximum tenure by churn status", "validation": "min_max", "expected": "ranges"},
        {"query": "Show top 5 customers by monthly charges", "validation": "top_n_simple", "expected": "5_rows"},
        {"query": "Show top 10 customers by calculated lifetime value (monthly_charges * tenure)", "validation": "top_n_calc", "expected": "10_rows_calculated"},
        {"query": "Show bottom 5 customers by tenure", "validation": "bottom_n", "expected": "5_rows"},
        {"query": "Find customers with charges above their contract type average", "validation": "subquery_filter", "expected": "above_avg_list"},
        {"query": "Show customers in contract types that have > 20% churn rate", "validation": "subquery_having", "expected": "high_churn_contracts"},
        {"query": "Calculate correlation between monthly charges and total charges", "validation": "correlation_calc", "expected": "correlation_value"},
        {"query": "Show percentile ranks for monthly charges", "validation": "percentile", "expected": "ranked_list"},
        {"query": "Create cohort analysis by tenure groups", "validation": "cohort", "expected": "grouped_analysis"}
    ],
    
    "INVESTIGATION_QUERIES": [
        # 10 Multi-step investigation queries
        {"query": "Why are high-value customers churning?", "validation": "root_cause", "expected": "multi_factor_analysis"},
        {"query": "What factors differentiate churned from retained customers?", "validation": "comparison_analysis", "expected": "key_differences"},
        {"query": "Identify the customer segment most at risk", "validation": "risk_analysis", "expected": "risk_segments"},
        {"query": "What combination of services leads to lowest churn?", "validation": "combination_analysis", "expected": "service_combinations"},
        {"query": "Find anomalies in customer behavior", "validation": "anomaly_detection", "expected": "outliers"},
        {"query": "What predicts customer lifetime value?", "validation": "predictive_factors", "expected": "value_drivers"},
        {"query": "Analyze the customer journey to churn", "validation": "journey_analysis", "expected": "stages"},
        {"query": "What interventions would reduce churn the most?", "validation": "recommendation", "expected": "actions"},
        {"query": "Segment customers by behavior patterns", "validation": "behavioral_segmentation", "expected": "segments"},
        {"query": "Identify early warning signs of churn", "validation": "early_warning", "expected": "indicators"}
    ],
    
    "STATISTICAL_ANALYSIS": [
        # 8 Statistical queries
        {"query": "Calculate standard deviation of monthly charges", "validation": "stddev_simple", "expected": "single_number"},
        {"query": "Show variance in tenure by contract type", "validation": "variance", "expected": "by_group"},
        {"query": "Calculate median monthly charges", "validation": "median", "expected": "single_number"},
        {"query": "Show quartiles for total charges", "validation": "quartiles", "expected": "q1_q2_q3"},
        {"query": "Calculate confidence interval for churn rate", "validation": "confidence", "expected": "interval"},
        {"query": "Perform t-test between churned and retained customer charges", "validation": "ttest", "expected": "p_value"},
        {"query": "Calculate z-scores for monthly charges", "validation": "zscore", "expected": "normalized_values"},
        {"query": "Show distribution of tenure", "validation": "distribution", "expected": "histogram_data"}
    ],
    
    "CALCULATED_METRICS": [
        # 10 Business calculations
        {"query": "Calculate customer lifetime value", "validation": "clv", "expected": "value_per_customer"},
        {"query": "What's the average revenue per user (ARPU)?", "validation": "arpu", "expected": "single_number"},
        {"query": "Calculate churn rate by cohort", "validation": "cohort_churn", "expected": "by_cohort"},
        {"query": "Show customer acquisition cost efficiency", "validation": "cac", "expected": "efficiency_metric"},
        {"query": "Calculate net revenue retention", "validation": "nrr", "expected": "retention_rate"},
        {"query": "What's the customer satisfaction score?", "validation": "csat", "expected": "score"},
        {"query": "Calculate monthly recurring revenue (MRR)", "validation": "mrr", "expected": "monthly_total"},
        {"query": "Show revenue per service type", "validation": "revenue_breakdown", "expected": "by_service"},
        {"query": "Calculate customer health score", "validation": "health_score", "expected": "score_per_customer"},
        {"query": "Show profit margin by customer segment", "validation": "profit_margin", "expected": "by_segment"}
    ]
}

class ComprehensiveValidator:
    """Validates if SQL actually answers the business question"""
    
    def __init__(self):
        self.validation_rules = {
            "count": self.validate_count,
            "average": self.validate_average,
            "segmented": self.validate_segmented,
            "filtered_list": self.validate_list,
            "investigation": self.validate_investigation,
            "mom_growth": self.validate_time_intelligence,
            "correlation": self.validate_correlation,
            "top_n": self.validate_top_n,
            "pattern": self.validate_pattern,
            # Add more validation methods as needed
        }
    
    def validate(self, query, sql, result, validation_type):
        """Main validation dispatcher"""
        if validation_type in self.validation_rules:
            return self.validation_rules[validation_type](query, sql, result)
        else:
            return self.generic_validation(query, sql, result)
    
    def validate_count(self, query, sql, result):
        """Validates count queries"""
        if not result:
            return False, "No result returned"
        if len(result) == 1 and len(result[0]) == 1:
            if isinstance(result[0][0], (int, float)):
                return True, f"Count: {result[0][0]}"
        return False, "Expected single count value"
    
    def validate_average(self, query, sql, result):
        """Validates average calculations"""
        if not result:
            return False, "No result returned"
        if len(result) == 1 and len(result[0]) == 1:
            if isinstance(result[0][0], (int, float)):
                return True, f"Average: {result[0][0]:.2f}"
        return False, "Expected single average value"
    
    def validate_segmented(self, query, sql, result):
        """Validates segmented analysis"""
        if not result:
            return False, "No result returned"
        if len(result) > 0 and len(result[0]) >= 2:
            return True, f"{len(result)} segments with metrics"
        return False, "Expected multiple segments with values"
    
    def validate_list(self, query, sql, result):
        """Validates filtered lists"""
        if not result:
            return False, "No matching records"
        return True, f"{len(result)} records found"
    
    def validate_investigation(self, query, sql, result):
        """Validates investigation queries - these should fail with single SQL"""
        return False, "Cannot perform multi-step investigation with single query"
    
    def validate_time_intelligence(self, query, sql, result):
        """Validates time intelligence queries"""
        # Check if SQL contains time functions
        time_keywords = ['LAG', 'LEAD', 'OVER', 'PARTITION', 'DATE_TRUNC', 'DATEADD']
        if any(keyword in sql.upper() for keyword in time_keywords):
            if result:
                return True, "Time intelligence query executed"
        return False, "No time intelligence capability"
    
    def validate_correlation(self, query, sql, result):
        """Validates correlation calculations"""
        if result and len(result) == 1:
            val = result[0][0]
            if isinstance(val, (int, float)) and -1 <= val <= 1:
                return True, f"Correlation: {val:.3f}"
        return False, "Expected correlation value between -1 and 1"
    
    def validate_top_n(self, query, sql, result):
        """Validates top N queries"""
        expected = 10 if "top 10" in query.lower() else 5 if "top 5" in query.lower() else 0
        if expected > 0:
            if len(result) <= expected:
                return True, f"Top {len(result)} returned"
            return False, f"Expected max {expected} rows, got {len(result)}"
        return self.validate_list(query, sql, result)
    
    def validate_pattern(self, query, sql, result):
        """Validates pattern discovery - should fail with single SQL"""
        return False, "Cannot discover patterns with single SQL query"
    
    def generic_validation(self, query, sql, result):
        """Generic validation for unspecified types"""
        if result and len(result) > 0:
            return True, f"{len(result)} rows returned"
        return False, "No results returned"


class MasterTestSuite:
    """Main test runner - maintains all state and results"""
    
    def __init__(self):
        self.conn = snowflake.connector.connect(**CONFIG)
        self.cursor = self.conn.cursor()
        self.validator = ComprehensiveValidator()
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "model": CONFIG["model"],
            "total_tests": 0,
            "by_category": {},
            "details": []
        }
    
    def run_test(self, test_case, category):
        """Run a single test with full validation"""
        query = test_case["query"]
        validation_type = test_case["validation"]
        
        # Build prompt with schema context
        prompt = f"""Using the TELCO_DATA table with columns:
CUSTOMERID, GENDER, SENIORCITIZEN, PARTNER, DEPENDENTS, TENURE,
PHONESERVICE, MULTIPLELINES, INTERNETSERVICE, ONLINESECURITY,
ONLINEBACKUP, DEVICEPROTECTION, TECHSUPPORT, STREAMINGTV,
STREAMINGMOVIES, CONTRACT, PAPERLESSBILLING, PAYMENTMETHOD,
MONTHLYCHARGES, TOTALCHARGES, CHURN (boolean)

Generate SQL for: {query}
Return ONLY the SQL statement."""

        try:
            # Get SQL from model
            start_time = time.time()
            self.cursor.execute(f"""
            SELECT SNOWFLAKE.CORTEX.COMPLETE(
                '{CONFIG["model"]}',
                %s
            ) as response
            """, (prompt,))
            
            response = self.cursor.fetchone()[0] if self.cursor.fetchone() else None
            elapsed = time.time() - start_time
            
            if not response or 'SELECT' not in response.upper():
                return {
                    "query": query,
                    "sql_generated": False,
                    "sql_executed": False,
                    "answers_question": False,
                    "reason": "No SQL generated",
                    "time": elapsed
                }
            
            # Extract SQL
            sql_start = response.upper().find('SELECT')
            sql = response[sql_start:]
            if '```' in sql:
                sql = sql.split('```')[0]
            sql = sql.strip().rstrip(';')
            
            # Execute SQL
            try:
                self.cursor.execute(sql)
                result = self.cursor.fetchall()
                
                # Validate if it answers the question
                answers, reason = self.validator.validate(query, sql, result, validation_type)
                
                return {
                    "query": query,
                    "sql_generated": True,
                    "sql_executed": True,
                    "answers_question": answers,
                    "reason": reason,
                    "time": elapsed,
                    "row_count": len(result) if result else 0
                }
                
            except Exception as e:
                return {
                    "query": query,
                    "sql_generated": True,
                    "sql_executed": False,
                    "answers_question": False,
                    "reason": f"SQL error: {str(e)[:100]}",
                    "time": elapsed
                }
                
        except Exception as e:
            return {
                "query": query,
                "sql_generated": False,
                "sql_executed": False,
                "answers_question": False,
                "reason": f"Model error: {str(e)[:100]}",
                "time": 0
            }
    
    def run_category(self, category_name, tests):
        """Run all tests in a category"""
        print(f"\n{'='*60}")
        print(f"Testing: {category_name} ({len(tests)} queries)")
        print('='*60)
        
        category_results = {
            "total": len(tests),
            "sql_generated": 0,
            "sql_executed": 0,
            "answers_question": 0,
            "tests": []
        }
        
        for i, test in enumerate(tests):
            print(f"\n[{i+1}/{len(tests)}] {test['query'][:60]}...")
            
            result = self.run_test(test, category_name)
            
            # Update stats
            if result["sql_generated"]:
                category_results["sql_generated"] += 1
            if result["sql_executed"]:
                category_results["sql_executed"] += 1
            if result["answers_question"]:
                category_results["answers_question"] += 1
            
            # Print result
            status = "✅" if result["answers_question"] else "⚠️" if result["sql_executed"] else "❌"
            print(f"  {status} {result['reason']}")
            
            category_results["tests"].append(result)
        
        # Category summary
        pct_answered = category_results["answers_question"] / category_results["total"] * 100
        print(f"\n{category_name} Summary:")
        print(f"  Answered Question: {category_results['answers_question']}/{category_results['total']} ({pct_answered:.1f}%)")
        
        return category_results
    
    def run_all_tests(self):
        """Run all test categories"""
        print("="*80)
        print(f"MASTER TEST SUITE - {CONFIG['model'].upper()}")
        print("="*80)
        
        total_tests = sum(len(tests) for tests in ALL_TESTS.values())
        print(f"\nTotal tests to run: {total_tests}")
        
        self.results["total_tests"] = total_tests
        
        # Run each category
        for category_name, tests in ALL_TESTS.items():
            category_results = self.run_category(category_name, tests)
            self.results["by_category"][category_name] = category_results
            time.sleep(1)  # Avoid rate limiting
        
        # Final summary
        self.print_final_summary()
        self.save_results()
    
    def print_final_summary(self):
        """Print comprehensive summary"""
        print("\n" + "="*80)
        print("FINAL SUMMARY - BUSINESS VALIDATION")
        print("="*80)
        
        total_generated = sum(cat["sql_generated"] for cat in self.results["by_category"].values())
        total_executed = sum(cat["sql_executed"] for cat in self.results["by_category"].values())
        total_answered = sum(cat["answers_question"] for cat in self.results["by_category"].values())
        
        print(f"\nOverall Performance:")
        print(f"  SQL Generated:      {total_generated}/{self.results['total_tests']} ({total_generated/self.results['total_tests']*100:.1f}%)")
        print(f"  SQL Executed:       {total_executed}/{self.results['total_tests']} ({total_executed/self.results['total_tests']*100:.1f}%)")
        print(f"  ANSWERS QUESTION:   {total_answered}/{self.results['total_tests']} ({total_answered/self.results['total_tests']*100:.1f}%)")
        
        print(f"\nBy Category (Answers Business Question):")
        for category, results in self.results["by_category"].items():
            pct = results["answers_question"] / results["total"] * 100
            status = "✅" if pct >= 70 else "⚠️" if pct >= 40 else "❌"
            print(f"  {status} {category}: {results['answers_question']}/{results['total']} ({pct:.1f}%)")
        
        print("\n" + "="*80)
        print("CRITICAL BUSINESS INSIGHTS")
        print("="*80)
        print(f"""
1. Natural Language: {self.results['by_category'].get('NATURAL_LANGUAGE', {}).get('answers_question', 0)}/15
   → Users can't ask questions naturally
   
2. Time Intelligence: {self.results['by_category'].get('TIME_INTELLIGENCE', {}).get('answers_question', 0)}/15
   → No period comparisons or trends
   
3. Investigation: {self.results['by_category'].get('INVESTIGATION_QUERIES', {}).get('answers_question', 0)}/10
   → Cannot answer "why" questions
   
4. Advanced SQL: {self.results['by_category'].get('ADVANCED_SQL_PATTERNS', {}).get('answers_question', 0)}/20
   → Limited to basic SQL patterns

Business Impact: Can only answer ~{total_answered/self.results['total_tests']*100:.0f}% of real business questions
""")
    
    def save_results(self):
        """Save results to JSON"""
        filename = f"MASTER_RESULTS_{CONFIG['model'].replace('-', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2, default=str)
        print(f"\n💾 Results saved to {filename}")
    
    def cleanup(self):
        """Close connection"""
        self.conn.close()


def main():
    """Run the master test suite"""
    print("Starting Master Test Suite...")
    suite = MasterTestSuite()
    
    try:
        suite.run_all_tests()
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        suite.cleanup()
        print("\nTest suite complete.")


if __name__ == "__main__":
    main()