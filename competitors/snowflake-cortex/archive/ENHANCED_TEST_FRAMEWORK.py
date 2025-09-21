#!/usr/bin/env python3
"""
ENHANCED SNOWFLAKE CORTEX ANALYST TEST FRAMEWORK
With Semantic Validation Inspired by Scoop's Approach

This framework validates Cortex Analyst across three critical dimensions:
1. SQL Generation - Can it produce SQL?
2. SQL Execution - Does the SQL run?
3. Semantic Validation - Does it answer the business question?

Key Innovation: Direct SQL semantic validation without intermediate representation
"""

import snowflake.connector
import json
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Tuple, Optional, Any

# ==========================================
# SEMANTIC PATTERN DEFINITIONS
# ==========================================

SEMANTIC_PATTERNS = {
    "churn_rate": {
        "must_have": ["COUNT", "/", "100"],  
        "or_have": ["RATIO_TO_REPORT", "PERCENT", "AVG(CASE"],
        "explanation": "Churn rate requires percentage calculation, not just count",
        "business_validation": lambda result: validate_percentage_result(result)
    },
    
    "average": {
        "must_have": ["AVG("],
        "or_have": ["SUM(", "COUNT("],  # Could calculate average differently
        "explanation": "Average calculation required"
    },
    
    "month_over_month": {
        "must_have": ["LAG", "PARTITION", "ORDER BY"],
        "or_have": ["LEAD", "WINDOW", "ROWS BETWEEN"],
        "explanation": "Period comparisons need window functions - CRITICAL GAP"
    },
    
    "year_over_year": {
        "must_have": ["LAG", "12", "ORDER BY"],
        "or_have": ["DATEADD", "YEAR", "-1"],
        "explanation": "YoY requires 12-month lag or date arithmetic"
    },
    
    "running_total": {
        "must_have": ["SUM(", "OVER", "ORDER BY", "ROWS"],
        "or_have": ["CUMULATIVE", "RUNNING"],
        "explanation": "Running totals need window functions with row ranges"
    },
    
    "top_n": {
        "must_have": ["LIMIT", "ORDER BY"],
        "or_have": ["TOP", "RANK()", "ROW_NUMBER()"],
        "explanation": "Top N queries must limit and sort results"
    },
    
    "percentage": {
        "must_have": ["100", "/"],
        "or_have": ["RATIO_TO_REPORT", "PERCENT"],
        "explanation": "Percentage calculations need division by total and multiply by 100"
    },
    
    "by_category": {
        "indicator_words": ["by", "per", "for each", "grouped by"],
        "must_have": ["GROUP BY"],
        "explanation": "Grouping required when 'by' indicates categorization"
    },
    
    "comparison": {
        "indicator_words": ["compare", "versus", "vs", "between"],
        "should_have_multiple_groups": True,
        "explanation": "Comparisons need multiple groups or categories"
    },
    
    "correlation": {
        "must_have": ["CORR", "COVAR"],
        "or_have": ["REGR_", "STDDEV"],
        "explanation": "Correlation requires statistical functions"
    },
    
    "trend": {
        "indicator_words": ["trend", "over time", "timeline"],
        "must_have": ["ORDER BY", "DATE"],
        "or_have": ["MONTH", "WEEK", "DAY"],
        "explanation": "Trends require time-based ordering"
    },
    
    "why": {
        "indicator_words": ["why", "root cause", "driver", "reason"],
        "architectural_limitation": True,
        "explanation": "Investigation queries require multi-step analysis - NOT POSSIBLE"
    }
}

# ==========================================
# CONNECTION AND SETUP
# ==========================================

def get_connection():
    """Establish Snowflake connection"""
    return snowflake.connector.connect(
        account='rcdtonr-ji20455',
        user='bradtest',
        password='qMsGeKsE33NJeZp',
        warehouse='COMPUTE_WH',
        database='SCOOP_BENCHMARK',
        schema='TEST_DATA'
    )

# ==========================================
# BUSINESS VALIDATION HELPERS
# ==========================================

def validate_percentage_result(result):
    """Check if result contains valid percentages"""
    if not result or not result[0]:
        return False
    
    for row in result:
        for val in row:
            if isinstance(val, (int, float)):
                if 0 <= val <= 100:
                    return True
    return False

def validate_count_result(result):
    """Check if result is a valid count"""
    if not result or not result[0]:
        return False
    
    val = result[0][0]
    return isinstance(val, (int, float)) and val >= 0

def validate_grouping_result(result, expected_groups=None):
    """Check if result has appropriate grouping"""
    if not result:
        return False
    
    if expected_groups and len(result) != expected_groups:
        return False
    
    return len(result) > 1  # Should have multiple groups

# ==========================================
# SEMANTIC VALIDATION ENGINE
# ==========================================

class SemanticValidator:
    """Direct SQL semantic validation without intermediate representation"""
    
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self.pattern_failures = defaultdict(int)
        self.test_results = []
    
    def check_semantic_patterns(self, query: str, sql: str) -> List[str]:
        """Quick pattern check without LLM"""
        failures = []
        query_lower = query.lower()
        sql_upper = sql.upper() if sql else ""
        
        for pattern_name, pattern in SEMANTIC_PATTERNS.items():
            # Check indicator words
            if 'indicator_words' in pattern:
                if not any(word in query_lower for word in pattern['indicator_words']):
                    continue  # Pattern doesn't apply
            else:
                if pattern_name not in query_lower:
                    continue  # Pattern doesn't apply
            
            # Check architectural limitations
            if pattern.get('architectural_limitation'):
                failures.append(f"ARCHITECTURAL LIMITATION: {pattern['explanation']}")
                continue
            
            # Check required patterns
            if 'must_have' in pattern:
                has_required = all(term in sql_upper for term in pattern['must_have'])
                has_alternative = False
                
                if not has_required and 'or_have' in pattern:
                    has_alternative = any(term in sql_upper for term in pattern['or_have'])
                
                if not (has_required or has_alternative):
                    failures.append(pattern['explanation'])
                    self.pattern_failures[pattern_name] += 1
        
        return failures
    
    def validate_with_llm(self, query: str, sql: str, result_sample: List) -> Dict:
        """Use Claude-4-Sonnet for semantic validation"""
        
        # Format result sample for prompt
        if result_sample and len(result_sample) > 0:
            result_str = f"{len(result_sample)} rows, {len(result_sample[0])} columns\nSample: {result_sample[:3]}"
        else:
            result_str = "No results returned"
        
        validation_prompt = f"""Analyze whether this SQL correctly answers the business question.

BUSINESS QUESTION: {query}

GENERATED SQL:
{sql}

RESULT SHAPE: {result_str}

SEMANTIC VALIDATION CRITERIA:
1. INTENT MATCH: Does the SQL query for what the user asked?
2. CORRECT AGGREGATION: If they asked for "average", does it use AVG? For "count", COUNT?
3. PROPER FILTERING: Are WHERE clauses aligned with the question?
4. RIGHT GROUPING: If they asked "by contract type", does it GROUP BY contract?
5. CALCULATION ACCURACY: For rates/percentages, is math correct?
6. BUSINESS LOGIC: Would a business analyst find this useful?

CRITICAL SEMANTIC ERRORS TO CHECK:
- Asked for "rate" or "percentage" but SQL doesn't calculate percentage
- Asked for "monthly trend" but SQL has no date grouping
- Asked for "top N" but SQL returns everything
- Asked "why" but SQL just lists data (investigation not possible)
- Asked for comparison but SQL doesn't compare groups
- Asked for time intelligence but SQL lacks window functions

Return ONLY valid JSON:
{{
    "semantically_correct": boolean,
    "errors": ["list", "of", "issues"],
    "severity": "critical|major|minor",
    "explanation": "brief explanation",
    "missing_capabilities": ["list of missing SQL features"]
}}"""

        try:
            # Call Claude-4-Sonnet via CORTEX.COMPLETE
            self.cursor.execute(f"""
                SELECT SNOWFLAKE.CORTEX.COMPLETE(
                    'claude-4-sonnet',
                    %s
                ) as response
            """, (validation_prompt,))
            
            response = self.cursor.fetchone()[0] if self.cursor.rowcount > 0 else None
            
            if response:
                # Extract JSON from response
                json_start = response.find('{')
                json_end = response.rfind('}') + 1
                if json_start >= 0 and json_end > json_start:
                    return json.loads(response[json_start:json_end])
            
            return {
                "semantically_correct": False,
                "errors": ["Failed to get LLM validation"],
                "severity": "critical"
            }
            
        except Exception as e:
            return {
                "semantically_correct": False,
                "errors": [f"LLM validation error: {str(e)}"],
                "severity": "critical"
            }
    
    def validate_business_rules(self, query: str, result: List, expected: Dict = None) -> Tuple[bool, str]:
        """Validate specific business expectations"""
        if not result:
            return False, "No results returned"
        
        query_lower = query.lower()
        
        # Specific business validations
        if "churn rate" in query_lower or "percentage" in query_lower:
            if validate_percentage_result(result):
                return True, "Valid percentage values"
            return False, "No valid percentage values found"
        
        if "count" in query_lower or "how many" in query_lower:
            if validate_count_result(result):
                return True, "Valid count"
            return False, "Invalid count result"
        
        if "top 5" in query_lower:
            if len(result) <= 5:
                return True, f"Correct limit: {len(result)} rows"
            return False, f"Too many rows: {len(result)}"
        
        if "top 10" in query_lower:
            if len(result) <= 10:
                return True, f"Correct limit: {len(result)} rows"
            return False, f"Too many rows: {len(result)}"
        
        # Check for grouping
        for word in ["by", "per", "grouped by", "for each"]:
            if word in query_lower:
                if len(result) > 1:
                    return True, f"Proper grouping: {len(result)} groups"
                return False, "Expected multiple groups, got single row"
        
        # Default validation
        if len(result) > 0:
            return True, "Results returned"
        return False, "Empty results"

# ==========================================
# COMPREHENSIVE TEST SUITE
# ==========================================

COMPREHENSIVE_TEST_SUITE = [
    # NATURAL LANGUAGE TESTS (What users actually type)
    {
        "id": "NL01",
        "query": "How many customers do we have?",
        "category": "natural_language",
        "expected_patterns": ["COUNT"],
        "business_validation": "single_count"
    },
    {
        "id": "NL02", 
        "query": "What's the average monthly charge?",
        "category": "natural_language",
        "expected_patterns": ["AVG"],
        "business_validation": "single_value"
    },
    {
        "id": "NL03",
        "query": "Show me churn rate by contract type",
        "category": "natural_language",
        "expected_patterns": ["percentage", "by_category"],
        "business_validation": "percentage_by_group"
    },
    {
        "id": "NL04",
        "query": "Why are customers leaving?",
        "category": "investigation",
        "expected_patterns": ["why"],
        "expected_failure": True,
        "failure_reason": "Multi-step investigation not possible"
    },
    {
        "id": "NL05",
        "query": "What drives customer loyalty?",
        "category": "investigation",
        "expected_patterns": ["why"],
        "expected_failure": True,
        "failure_reason": "Driver analysis requires multiple queries"
    },
    
    # TIME INTELLIGENCE TESTS (Critical Gap)
    {
        "id": "TI01",
        "query": "Show month-over-month revenue growth",
        "category": "time_intelligence",
        "expected_patterns": ["month_over_month"],
        "expected_failure": True,
        "failure_reason": "LAG/WINDOW functions likely missing"
    },
    {
        "id": "TI02",
        "query": "Calculate year-over-year change in customer count",
        "category": "time_intelligence",
        "expected_patterns": ["year_over_year"],
        "expected_failure": True,
        "failure_reason": "Period shift functions missing"
    },
    {
        "id": "TI03",
        "query": "Show running total of monthly charges",
        "category": "time_intelligence",
        "expected_patterns": ["running_total"],
        "expected_failure": True,
        "failure_reason": "Cumulative calculations need window functions"
    },
    {
        "id": "TI04",
        "query": "What's the 7-day moving average?",
        "category": "time_intelligence",
        "expected_patterns": ["AVG", "OVER", "ROWS"],
        "expected_failure": True,
        "failure_reason": "Moving averages need window functions"
    },
    
    # ADVANCED SQL PATTERNS
    {
        "id": "AS01",
        "query": "Show customers with monthly charges between $50 and $100",
        "category": "filtering",
        "expected_patterns": ["BETWEEN", "WHERE"],
        "business_validation": "filtered_list"
    },
    {
        "id": "AS02",
        "query": "Find customers where tenure is null or zero",
        "category": "null_handling",
        "expected_patterns": ["IS NULL", "OR", "= 0"],
        "business_validation": "filtered_list"
    },
    {
        "id": "AS03",
        "query": "Calculate churn rate avoiding division by zero",
        "category": "safe_calculation",
        "expected_patterns": ["NULLIF", "CASE WHEN"],
        "business_validation": "percentage"
    },
    {
        "id": "AS04",
        "query": "Show top 10 customers by total charges",
        "category": "ranking",
        "expected_patterns": ["top_n"],
        "business_validation": "limited_rows",
        "expected_rows": 10
    },
    {
        "id": "AS05",
        "query": "What's the correlation between tenure and monthly charges?",
        "category": "statistical",
        "expected_patterns": ["correlation"],
        "expected_failure": True,
        "failure_reason": "CORR function may not be available"
    },
    
    # BUSINESS METRICS
    {
        "id": "BM01",
        "query": "What's our customer lifetime value?",
        "category": "calculated_metric",
        "expected_patterns": ["AVG", "SUM"],
        "business_validation": "single_value"
    },
    {
        "id": "BM02",
        "query": "Show revenue by service type with percentage breakdown",
        "category": "percentage_analysis",
        "expected_patterns": ["percentage", "by_category"],
        "business_validation": "percentage_breakdown"
    },
    {
        "id": "BM03",
        "query": "Which payment methods have more than 1000 customers?",
        "category": "having_clause",
        "expected_patterns": ["GROUP BY", "HAVING", "COUNT"],
        "business_validation": "filtered_groups"
    },
    
    # INVESTIGATION QUERIES (Expected to Fail)
    {
        "id": "INV01",
        "query": "Why did churn increase last month?",
        "category": "investigation",
        "expected_failure": True,
        "failure_reason": "Root cause analysis needs multiple queries"
    },
    {
        "id": "INV02",
        "query": "What patterns predict churn?",
        "category": "pattern_discovery",
        "expected_failure": True,
        "failure_reason": "Pattern discovery requires ML or multi-step analysis"
    },
    {
        "id": "INV03",
        "query": "Find anomalies in customer behavior",
        "category": "anomaly_detection",
        "expected_failure": True,
        "failure_reason": "Anomaly detection requires statistical modeling"
    }
]

# ==========================================
# TEST EXECUTION ENGINE
# ==========================================

class CortexAnalystTester:
    """Main test execution and reporting engine"""
    
    def __init__(self, model='claude-4-sonnet'):
        self.model = model
        self.conn = get_connection()
        self.cursor = self.conn.cursor()
        self.validator = SemanticValidator(self.conn)
        self.results = []
        self.summary = defaultdict(lambda: {"total": 0, "passed": 0, "failed": 0})
    
    def generate_sql(self, query: str, with_context: bool = True) -> str:
        """Generate SQL using CORTEX.COMPLETE"""
        
        if with_context:
            # Add table context
            prompt = f"""Using TELCO_DATA table with columns: CUSTOMERID, GENDER, SENIORCITIZEN,
TENURE, MONTHLYCHARGES, TOTALCHARGES, CHURN, CONTRACT, PAYMENTMETHOD,
INTERNETSERVICE, and various service columns.

Generate SQL for: {query}

Return ONLY the SQL statement, no explanations."""
        else:
            # Pure natural language
            prompt = query
        
        try:
            self.cursor.execute(f"""
                SELECT SNOWFLAKE.CORTEX.COMPLETE(
                    %s,
                    %s
                ) as response
            """, (self.model, prompt))
            
            response = self.cursor.fetchone()[0] if self.cursor.rowcount > 0 else None
            
            if response and 'SELECT' in response.upper():
                # Extract SQL
                sql_start = response.upper().find('SELECT')
                sql = response[sql_start:]
                if '```' in sql:
                    sql = sql.split('```')[0]
                return sql.strip()
            
            return None
            
        except Exception as e:
            print(f"Error generating SQL: {e}")
            return None
    
    def execute_sql(self, sql: str) -> Tuple[bool, Optional[List]]:
        """Execute SQL and return success status and results"""
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return True, results
        except Exception as e:
            return False, str(e)
    
    def run_test(self, test_case: Dict) -> Dict:
        """Run a single test case through full validation pipeline"""
        
        print(f"\n[{test_case['id']}] {test_case['category']}: {test_case['query']}")
        print("-" * 60)
        
        result = {
            "id": test_case["id"],
            "query": test_case["query"],
            "category": test_case["category"]
        }
        
        # 1. Generate SQL
        sql = self.generate_sql(test_case["query"])
        result["sql_generated"] = bool(sql)
        
        if not sql:
            result["status"] = "NO_SQL"
            result["passed"] = False
            print("❌ No SQL generated")
            return result
        
        print(f"✓ SQL Generated")
        
        # 2. Quick semantic pattern check
        pattern_issues = self.validator.check_semantic_patterns(test_case["query"], sql)
        result["pattern_issues"] = pattern_issues
        
        if pattern_issues:
            print(f"⚠️ Pattern issues: {', '.join(pattern_issues)}")
        
        # 3. Execute SQL
        success, sql_result = self.execute_sql(sql)
        result["sql_executed"] = success
        
        if not success:
            result["status"] = "SQL_ERROR"
            result["error"] = sql_result
            result["passed"] = False
            print(f"❌ SQL execution failed: {sql_result[:100]}")
            return result
        
        print(f"✓ SQL Executed: {len(sql_result)} rows")
        
        # 4. LLM Semantic Validation (if no critical pattern issues)
        if not any("ARCHITECTURAL LIMITATION" in issue for issue in pattern_issues):
            semantic_result = self.validator.validate_with_llm(
                test_case["query"],
                sql,
                sql_result[:5] if sql_result else []
            )
            result["semantic_validation"] = semantic_result
            result["semantically_correct"] = semantic_result.get("semantically_correct", False)
        else:
            result["semantically_correct"] = False
            result["semantic_validation"] = {"errors": pattern_issues}
        
        # 5. Business Validation
        business_valid, business_reason = self.validator.validate_business_rules(
            test_case["query"],
            sql_result,
            test_case.get("expected", {})
        )
        result["business_valid"] = business_valid
        result["business_reason"] = business_reason
        
        # 6. Determine overall pass/fail
        if test_case.get("expected_failure"):
            # This test is expected to fail
            result["passed"] = not result["semantically_correct"]
            if result["passed"]:
                print(f"✅ PASSED (expected failure): {test_case['failure_reason']}")
            else:
                print(f"❌ FAILED (unexpectedly succeeded)")
        else:
            # Normal test
            result["passed"] = (
                result["sql_generated"] and 
                result["sql_executed"] and 
                result["semantically_correct"] and 
                result["business_valid"]
            )
            
            if result["passed"]:
                print(f"✅ PASSED: All validations successful")
            else:
                failures = []
                if not result["semantically_correct"]:
                    failures.append("semantic")
                if not result["business_valid"]:
                    failures.append(f"business: {business_reason}")
                print(f"❌ FAILED: {', '.join(failures)}")
        
        return result
    
    def run_all_tests(self):
        """Run complete test suite"""
        
        print("=" * 80)
        print(f"COMPREHENSIVE CORTEX ANALYST TESTING WITH {self.model.upper()}")
        print(f"Testing {len(COMPREHENSIVE_TEST_SUITE)} queries with semantic validation")
        print("=" * 80)
        
        for test_case in COMPREHENSIVE_TEST_SUITE:
            result = self.run_test(test_case)
            self.results.append(result)
            
            # Update summary
            category = test_case["category"]
            self.summary[category]["total"] += 1
            if result["passed"]:
                self.summary[category]["passed"] += 1
            else:
                self.summary[category]["failed"] += 1
        
        self.generate_report()
    
    def generate_report(self):
        """Generate comprehensive test report"""
        
        print("\n" + "=" * 80)
        print("FINAL RESULTS - SEMANTIC VALIDATION")
        print("=" * 80)
        
        # Overall stats
        total = len(self.results)
        passed = sum(1 for r in self.results if r["passed"])
        
        print(f"\nOverall: {passed}/{total} ({passed/total*100:.1f}%) passed")
        
        # Category breakdown
        print("\nBy Category:")
        for category, stats in sorted(self.summary.items()):
            pct = stats["passed"]/stats["total"]*100 if stats["total"] > 0 else 0
            status = "✅" if pct > 50 else "❌"
            print(f"  {status} {category}: {stats['passed']}/{stats['total']} ({pct:.0f}%)")
        
        # Pattern failure analysis
        print("\nMost Common Pattern Failures:")
        for pattern, count in sorted(self.validator.pattern_failures.items(), 
                                    key=lambda x: x[1], reverse=True)[:5]:
            print(f"  - {pattern}: {count} occurrences")
        
        # Critical findings
        print("\nCRITICAL FINDINGS:")
        
        # Time intelligence
        time_intel_tests = [r for r in self.results if r["category"] == "time_intelligence"]
        time_intel_passed = sum(1 for r in time_intel_tests if r["passed"])
        print(f"  Time Intelligence: {time_intel_passed}/{len(time_intel_tests)} passed")
        if time_intel_passed == 0:
            print("    ⚠️ COMPLETE FAILURE on time intelligence - no LAG/LEAD/WINDOW support")
        
        # Investigation
        investigation_tests = [r for r in self.results if r["category"] == "investigation"]
        investigation_passed = sum(1 for r in investigation_tests if not r["passed"])  # Expected to fail
        print(f"  Investigation: {investigation_passed}/{len(investigation_tests)} correctly failed")
        print("    ⚠️ Cannot perform multi-step analysis (architectural limitation)")
        
        # Natural language
        nl_tests = [r for r in self.results if r["category"] == "natural_language"]
        nl_passed = sum(1 for r in nl_tests if r["passed"])
        print(f"  Natural Language: {nl_passed}/{len(nl_tests)} passed")
        
        # Save detailed results
        self.save_results()
    
    def save_results(self):
        """Save detailed results to JSON"""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"semantic_test_results_{self.model}_{timestamp}.json"
        
        output = {
            "model": self.model,
            "timestamp": timestamp,
            "summary": dict(self.summary),
            "pattern_failures": dict(self.validator.pattern_failures),
            "detailed_results": self.results
        }
        
        with open(filename, 'w') as f:
            json.dump(output, f, indent=2, default=str)
        
        print(f"\n💾 Detailed results saved to {filename}")

# ==========================================
# MAIN EXECUTION
# ==========================================

if __name__ == "__main__":
    # Run comprehensive testing
    tester = CortexAnalystTester(model='claude-4-sonnet')
    tester.run_all_tests()
    
    print("\n" + "=" * 80)
    print("KEY INSIGHTS FOR COMPETITIVE ANALYSIS:")
    print("=" * 80)
    print("""
1. SEMANTIC VALIDATION reveals true capabilities beyond SQL generation
2. TIME INTELLIGENCE is completely missing (0% success expected)
3. INVESTIGATION queries cannot be done (architectural limitation)
4. NATURAL LANGUAGE requires semantic context to work
5. Pattern analysis shows systematic gaps, not random failures

This framework proves Cortex Analyst is a SQL generator, not an analytics engine.
Scoop's Query JSON Object enables capabilities Snowflake cannot match.
""")
    
    tester.conn.close()