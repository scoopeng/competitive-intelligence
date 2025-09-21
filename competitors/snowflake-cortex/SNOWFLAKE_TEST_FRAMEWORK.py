#!/usr/bin/env python3
"""
SNOWFLAKE CORTEX ANALYST TEST FRAMEWORK
========================================
Clean, rigorous testing framework matching Scoop's methodology.

Architecture:
- Progressive complexity testing (Basic → Intermediate → Advanced → Edge)
- Three-layer validation (Generation → Execution → Semantic)
- Batch processing with retry logic
- Structured test cases with metadata
- Single source of truth
"""

import json
import os
import sys
import time
import argparse
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict
from enum import Enum
import snowflake.connector
from snowflake.connector import DictCursor


class TestComplexity(Enum):
    """Test complexity levels matching Scoop's progression"""
    BASIC = "basic"           # Queries 1-10: Core fundamentals
    INTERMEDIATE = "intermediate"  # Queries 11-20: Single-query features  
    ADVANCED = "advanced"      # Queries 21-30: Complex features
    EDGE = "edge"             # Queries 31+: Edge cases & limits


class TestCategory(Enum):
    """Query categories for comprehensive coverage"""
    BASIC_AGGREGATION = "basic_aggregation"
    GROUPING = "grouping"
    FILTERING = "filtering"
    TIME_INTELLIGENCE = "time_intelligence"
    CALCULATED_METRICS = "calculated_metrics"
    VISUALIZATION = "visualization"
    RANKING = "ranking"
    STATISTICAL = "statistical"
    COMPLEX_ANALYSIS = "complex_analysis"
    INVESTIGATION = "investigation"
    CHANGE_TRACKING = "change_tracking"
    EDGE_CASES = "edge_cases"


@dataclass
class TestCase:
    """Structured test case matching Scoop's format"""
    test_id: str
    query: str
    description: str
    category: TestCategory
    complexity: TestComplexity
    expected_capabilities: Dict[str, bool]  # What Scoop can do
    snowflake_prediction: Dict[str, bool]   # What we expect Snowflake to do
    validation_criteria: Dict[str, Any]
    metadata: Dict[str, Any]
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization"""
        result = asdict(self)
        result['category'] = self.category.value
        result['complexity'] = self.complexity.value
        return result


@dataclass
class TestResult:
    """Test execution result with three-layer validation"""
    test_id: str
    timestamp: str
    
    # Layer 1: SQL Generation
    sql_generated: bool
    generated_sql: Optional[str]
    generation_error: Optional[str]
    
    # Layer 2: SQL Execution
    sql_executed: bool
    execution_result: Optional[Any]
    execution_error: Optional[str]
    
    # Layer 3: Semantic Validation
    semantically_correct: bool
    semantic_analysis: Optional[str]
    
    # Overall
    passed: bool
    failure_category: Optional[str]
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization"""
        return asdict(self)


class SnowflakeTestFramework:
    """Main test framework matching Scoop's rigor"""
    
    def __init__(self, connection_params: Dict[str, str]):
        self.connection_params = connection_params
        self.conn = None
        self.test_cases: List[TestCase] = []
        self.results: List[TestResult] = []
        self.semantic_model = self._load_semantic_model()
        
    def _load_semantic_model(self) -> Dict:
        """Load Snowflake semantic model configuration"""
        model_path = "semantic_model.yaml"
        if os.path.exists(model_path):
            import yaml
            with open(model_path, 'r') as f:
                return yaml.safe_load(f)
        return {}
        
    def connect(self):
        """Establish Snowflake connection"""
        self.conn = snowflake.connector.connect(**self.connection_params)
        
    def generate_test_cases(self) -> List[TestCase]:
        """Generate progressive test cases like Scoop's AIQueryTestSuggester"""
        test_cases = []
        test_id_counter = 0
        
        # BASIC COMPLEXITY (1-10)
        basic_queries = [
            ("How many customers do we have?", TestCategory.BASIC_AGGREGATION, 
             {"sql_generation": True, "correct_function": True}),
            ("What is the total revenue?", TestCategory.BASIC_AGGREGATION,
             {"sql_generation": True, "correct_function": True}),
            ("Show revenue by product category", TestCategory.GROUPING,
             {"sql_generation": True, "has_group_by": True}),
            ("Show only active customers", TestCategory.FILTERING,
             {"sql_generation": True, "has_where": True}),
            ("Show monthly revenue trend", TestCategory.TIME_INTELLIGENCE,
             {"sql_generation": True, "time_grouping": False}),  # Snowflake fails
            ("Calculate profit margin", TestCategory.CALCULATED_METRICS,
             {"sql_generation": True, "has_calculation": True}),
            ("Number of customers by region", TestCategory.GROUPING,
             {"sql_generation": True, "has_group_by": True}),
            ("Show last quarter's sales", TestCategory.FILTERING,
             {"sql_generation": True, "date_filter": True}),
            ("Show revenue and customer count by category", TestCategory.GROUPING,
             {"sql_generation": True, "multiple_metrics": True}),
            ("Top 5 products by revenue", TestCategory.RANKING,
             {"sql_generation": True, "has_limit": True})
        ]
        
        for query, category, snowflake_pred in basic_queries:
            test_id_counter += 1
            test_cases.append(TestCase(
                test_id=f"cortex_{test_id_counter:03d}_{category.value}",
                query=query,
                description=f"Test {category.value} capability",
                category=category,
                complexity=TestComplexity.BASIC,
                expected_capabilities={"scoop": True},
                snowflake_prediction=snowflake_pred,
                validation_criteria={
                    "must_have_sql": True,
                    "must_execute": snowflake_pred.get("sql_generation", False)
                },
                metadata={"created": datetime.now().isoformat()}
            ))
        
        # INTERMEDIATE COMPLEXITY (11-20)
        intermediate_queries = [
            ("Active customers in California", TestCategory.FILTERING,
             {"sql_generation": True, "compound_filter": True}),
            ("Customers in CA or NY", TestCategory.FILTERING,
             {"sql_generation": True, "or_condition": True}),
            ("Show monthly revenue with previous month comparison", TestCategory.TIME_INTELLIGENCE,
             {"sql_generation": True, "lag_function": False}),  # Snowflake fails
            ("Calculate market share percentage by region", TestCategory.CALCULATED_METRICS,
             {"sql_generation": True, "percentage_calc": False}),
            ("Revenue for premium customers", TestCategory.FILTERING,
             {"sql_generation": True, "conditional_calc": True}),
            ("Sales by region and product", TestCategory.GROUPING,
             {"sql_generation": True, "multi_group": True}),
            ("Unique customers by month", TestCategory.GROUPING,
             {"sql_generation": True, "count_distinct": True}),
            ("Earliest and latest order dates", TestCategory.BASIC_AGGREGATION,
             {"sql_generation": True, "min_max": True}),
            ("Growth rate calculation", TestCategory.CALCULATED_METRICS,
             {"sql_generation": True, "growth_calc": False}),  # Snowflake fails
            ("Weekly sales trends", TestCategory.TIME_INTELLIGENCE,
             {"sql_generation": True, "weekly_grouping": False})  # Snowflake fails
        ]
        
        for query, category, snowflake_pred in intermediate_queries:
            test_id_counter += 1
            test_cases.append(TestCase(
                test_id=f"cortex_{test_id_counter:03d}_{category.value}",
                query=query,
                description=f"Test intermediate {category.value}",
                category=category,
                complexity=TestComplexity.INTERMEDIATE,
                expected_capabilities={"scoop": True},
                snowflake_prediction=snowflake_pred,
                validation_criteria={
                    "must_have_sql": True,
                    "semantic_match": snowflake_pred.get("sql_generation", False)
                },
                metadata={"created": datetime.now().isoformat()}
            ))
        
        # ADVANCED COMPLEXITY (21-30)
        advanced_queries = [
            ("Revenue from top 5 customers", TestCategory.COMPLEX_ANALYSIS,
             {"sql_generation": True, "subquery": False}),  # Snowflake fails
            ("Products with >$10K monthly sales", TestCategory.FILTERING,
             {"sql_generation": True, "threshold_filter": True}),
            ("Accounts with win rate > 40%", TestCategory.CALCULATED_METRICS,
             {"sql_generation": True, "formula_filter": False}),
            ("Weighted scoring calculation", TestCategory.CALCULATED_METRICS,
             {"sql_generation": True, "complex_formula": False}),
            ("Running total of sales", TestCategory.TIME_INTELLIGENCE,
             {"sql_generation": True, "window_function": False}),  # Snowflake fails
            ("Forecast vs actual comparison", TestCategory.COMPLEX_ANALYSIS,
             {"sql_generation": True, "date_comparison": False}),
            ("Customers without email", TestCategory.FILTERING,
             {"sql_generation": True, "null_handling": True}),
            ("Orders between $1000 and $5000", TestCategory.FILTERING,
             {"sql_generation": True, "between_operator": True}),
            ("Companies ending in Corp", TestCategory.FILTERING,
             {"sql_generation": True, "like_operator": True}),
            ("Top customers in top regions", TestCategory.COMPLEX_ANALYSIS,
             {"sql_generation": True, "nested_subquery": False})  # Snowflake fails
        ]
        
        for query, category, snowflake_pred in advanced_queries:
            test_id_counter += 1
            test_cases.append(TestCase(
                test_id=f"cortex_{test_id_counter:03d}_{category.value}",
                query=query,
                description=f"Test advanced {category.value}",
                category=category,
                complexity=TestComplexity.ADVANCED,
                expected_capabilities={"scoop": True},
                snowflake_prediction=snowflake_pred,
                validation_criteria={
                    "must_have_sql": True,
                    "complex_validation": True
                },
                metadata={"created": datetime.now().isoformat()}
            ))
        
        # Store test cases
        self.test_cases = test_cases
        return test_cases
    
    def execute_test_batch(self, test_cases: List[TestCase], batch_size: int = 4) -> List[TestResult]:
        """Execute tests in batches with retry logic like Scoop's analyzer"""
        results = []
        failed_cases = []
        
        print(f"\n=== PHASE 1: Batch Testing (batch size: {batch_size}) ===")
        
        # Phase 1: Batch processing
        for i in range(0, len(test_cases), batch_size):
            batch = test_cases[i:min(i + batch_size, len(test_cases))]
            print(f"Testing batch {i//batch_size + 1}/{(len(test_cases) + batch_size - 1)//batch_size}")
            
            for test_case in batch:
                result = self._execute_single_test(test_case)
                results.append(result)
                
                if not result.passed:
                    failed_cases.append((test_case, result))
        
        # Phase 2: Retry failed cases individually
        if failed_cases:
            print(f"\n=== PHASE 2: Individual Retry for {len(failed_cases)} failures ===")
            for test_case, original_result in failed_cases:
                print(f"Retrying: {test_case.test_id}")
                retry_result = self._execute_single_test(test_case, retry=True)
                
                # Update result if retry succeeded
                if retry_result.passed and not original_result.passed:
                    idx = results.index(original_result)
                    results[idx] = retry_result
                    print(f"  ✓ Retry succeeded for {test_case.test_id}")
        
        self.results = results
        return results
    
    def _execute_single_test(self, test_case: TestCase, retry: bool = False) -> TestResult:
        """Execute a single test with three-layer validation"""
        result = TestResult(
            test_id=test_case.test_id,
            timestamp=datetime.now().isoformat(),
            sql_generated=False,
            generated_sql=None,
            generation_error=None,
            sql_executed=False,
            execution_result=None,
            execution_error=None,
            semantically_correct=False,
            semantic_analysis=None,
            passed=False,
            failure_category=None
        )
        
        try:
            # Layer 1: SQL Generation
            generated_sql = self._generate_sql_via_cortex(test_case.query)
            if generated_sql:
                result.sql_generated = True
                result.generated_sql = generated_sql
            else:
                result.generation_error = "No SQL generated"
                result.failure_category = "generation_failed"
                return result
            
            # Layer 2: SQL Execution
            if self.conn:
                try:
                    cursor = self.conn.cursor(DictCursor)
                    cursor.execute(generated_sql)
                    result.execution_result = cursor.fetchall()
                    result.sql_executed = True
                    cursor.close()
                except Exception as e:
                    result.execution_error = str(e)
                    result.failure_category = "execution_failed"
                    return result
            
            # Layer 3: Semantic Validation
            result.semantically_correct = self._validate_semantic_correctness(
                test_case, generated_sql, result.execution_result
            )
            
            if not result.semantically_correct:
                result.semantic_analysis = f"SQL doesn't answer the question: {test_case.query}"
                result.failure_category = "semantic_mismatch"
            else:
                result.passed = True
                
        except Exception as e:
            result.generation_error = str(e)
            result.failure_category = "exception"
        
        return result
    
    def _generate_sql_via_cortex(self, query: str) -> Optional[str]:
        """Generate SQL using Cortex Analyst API"""
        # This would call the actual Cortex Analyst API
        # For now, returning a placeholder
        if not self.conn:
            return None
            
        try:
            # Call Cortex Analyst
            cursor = self.conn.cursor()
            cursor.execute(f"""
                SELECT CORTEX_ANALYST(
                    '{query}',
                    '{json.dumps(self.semantic_model)}'
                )
            """)
            response = cursor.fetchone()[0]
            cursor.close()
            
            if response and 'sql' in response:
                return response['sql']
        except:
            pass
        
        return None
    
    def _validate_semantic_correctness(self, test_case: TestCase, sql: str, result: Any) -> bool:
        """Validate if the SQL semantically answers the question"""
        # Check for expected SQL patterns based on test case
        validations = test_case.validation_criteria
        
        if validations.get("must_have_sql") and not sql:
            return False
            
        # Check for specific SQL features
        sql_lower = sql.lower() if sql else ""
        
        if test_case.category == TestCategory.TIME_INTELLIGENCE:
            # Should have time-based operations
            if not any(func in sql_lower for func in ['lag', 'lead', 'over', 'partition']):
                if 'month' in test_case.query.lower() or 'year' in test_case.query.lower():
                    return False
                    
        elif test_case.category == TestCategory.GROUPING:
            # Should have GROUP BY
            if 'group by' not in sql_lower and 'by' in test_case.query.lower():
                return False
                
        elif test_case.category == TestCategory.INVESTIGATION:
            # Cannot be done in single SQL
            return False
            
        return True
    
    def generate_report(self) -> str:
        """Generate comprehensive test report"""
        if not self.results:
            return "No test results available"
        
        # Calculate statistics
        total = len(self.results)
        passed = sum(1 for r in self.results if r.passed)
        
        # Group by category
        by_category = {}
        for test_case, result in zip(self.test_cases, self.results):
            cat = test_case.category.value
            if cat not in by_category:
                by_category[cat] = {"total": 0, "passed": 0}
            by_category[cat]["total"] += 1
            if result.passed:
                by_category[cat]["passed"] += 1
        
        # Build report
        report = []
        report.append("# SNOWFLAKE CORTEX ANALYST TEST REPORT")
        report.append(f"Generated: {datetime.now().isoformat()}")
        report.append("")
        report.append("## Overall Results")
        report.append(f"- **Total Tests**: {total}")
        report.append(f"- **Passed**: {passed} ({passed*100/total:.1f}%)")
        report.append(f"- **Failed**: {total-passed} ({(total-passed)*100/total:.1f}%)")
        report.append("")
        
        report.append("## Results by Category")
        report.append("| Category | Passed | Total | Success Rate |")
        report.append("|----------|--------|-------|-------------|")
        
        for cat in TestCategory:
            if cat.value in by_category:
                stats = by_category[cat.value]
                rate = stats["passed"] * 100 / stats["total"]
                emoji = "✅" if rate > 80 else "⚠️" if rate > 50 else "❌"
                report.append(f"| {cat.value} | {stats['passed']} | {stats['total']} | {rate:.0f}% {emoji} |")
        
        report.append("")
        report.append("## Failure Analysis")
        
        # Group failures by category
        failures = {}
        for test_case, result in zip(self.test_cases, self.results):
            if not result.passed and result.failure_category:
                if result.failure_category not in failures:
                    failures[result.failure_category] = []
                failures[result.failure_category].append(test_case.query)
        
        for failure_type, queries in failures.items():
            report.append(f"\n### {failure_type.replace('_', ' ').title()}")
            for q in queries[:5]:  # Show first 5 examples
                report.append(f"- \"{q}\"")
            if len(queries) > 5:
                report.append(f"- ... and {len(queries)-5} more")
        
        return "\n".join(report)
    
    def save_results(self, output_dir: str = "test_results"):
        """Save test results and report"""
        os.makedirs(output_dir, exist_ok=True)
        
        # Save test cases
        with open(f"{output_dir}/test_cases.json", "w") as f:
            json.dump([tc.to_dict() for tc in self.test_cases], f, indent=2)
        
        # Save results
        with open(f"{output_dir}/results.json", "w") as f:
            json.dump([r.to_dict() for r in self.results], f, indent=2)
        
        # Save report
        with open(f"{output_dir}/report.md", "w") as f:
            f.write(self.generate_report())
        
        print(f"\nResults saved to {output_dir}/")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Snowflake Cortex Analyst Test Framework")
    parser.add_argument("--quick", action="store_true", help="Run quick test (5 per category)")
    parser.add_argument("--category", help="Test specific category")
    parser.add_argument("--complexity", help="Test specific complexity level")
    
    args = parser.parse_args()
    
    # Connection parameters (would come from config)
    connection_params = {
        "account": os.getenv("SNOWFLAKE_ACCOUNT"),
        "user": os.getenv("SNOWFLAKE_USER"),
        "password": os.getenv("SNOWFLAKE_PASSWORD"),
        "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
        "database": os.getenv("SNOWFLAKE_DATABASE"),
        "schema": os.getenv("SNOWFLAKE_SCHEMA")
    }
    
    # Initialize framework
    framework = SnowflakeTestFramework(connection_params)
    
    # Generate test cases
    print("Generating test cases...")
    test_cases = framework.generate_test_cases()
    
    # Filter if needed
    if args.category:
        test_cases = [tc for tc in test_cases if tc.category.value == args.category]
    if args.complexity:
        test_cases = [tc for tc in test_cases if tc.complexity.value == args.complexity]
    if args.quick:
        test_cases = test_cases[:5]
    
    print(f"Running {len(test_cases)} test cases...")
    
    # Connect and execute (skip if no credentials)
    if all(connection_params.values()):
        try:
            framework.connect()
            framework.execute_test_batch(test_cases)
        finally:
            if framework.conn:
                framework.conn.close()
    else:
        print("\n⚠️  No Snowflake credentials found. Running in demo mode...")
        print("Set environment variables to connect:")
        print("  export SNOWFLAKE_ACCOUNT=your_account")
        print("  export SNOWFLAKE_USER=your_user")
        print("  export SNOWFLAKE_PASSWORD=your_password")
        print("\nGenerating test cases only...")
    
    # Generate and save report
    framework.save_results()
    print("\n" + framework.generate_report())


if __name__ == "__main__":
    main()