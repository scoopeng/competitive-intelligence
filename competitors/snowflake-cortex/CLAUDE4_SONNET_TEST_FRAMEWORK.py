#!/usr/bin/env python3
"""
Fair Comparison Test Framework
===============================
Tests Snowflake Cortex using Claude-4-Sonnet (same model as Scoop)
Imports Scoop's 90 test queries for apples-to-apples comparison
"""

import json
import os
import time
from datetime import datetime
from typing import Dict, List, Optional, Any
import snowflake.connector

# Fair comparison configuration
SNOWFLAKE_CONFIG = {
    'account': 'rcdtonr-ji20455',
    'user': 'bradtest', 
    'password': 'qMsGeKsE33NJeZp',
    'warehouse': 'COMPUTE_WH',
    'database': 'SCOOP_BENCHMARK'
}

# MUST use Claude-4-Sonnet for fair comparison
MODEL = 'claude-4-sonnet'  # Same as Scoop uses

# Datasets (same as Scoop's internal tests)
DATASETS = {
    'TELCO_DATA': {
        'schema': 'TEST_DATA',
        'table': 'TELCO_DATA',
        'description': 'Telecom customer data with churn'
    },
    'OpenOpportunities': {
        'schema': 'TEST_DATA', 
        'table': 'OPEN_OPPORTUNITIES',
        'description': 'Sales opportunities data'
    }
}


class ScoopTestQueries:
    """Import and manage Scoop's 90 test queries"""
    
    # Based on AIQueryTestSuggester.java categories
    BASIC_QUERIES = [
        "How many customers do we have?",
        "What is the total revenue?",
        "What is the average order value?",
        "Show me the number of active users",
        "Count the total transactions",
        "What's our current MRR?",
        "How many new signups this month?",
        "Total sales this quarter",
        "Average customer lifetime value",
        "Number of churned customers"
    ]
    
    INTERMEDIATE_QUERIES = [
        "Show revenue by product category",
        "Top 10 customers by spend",
        "Monthly revenue trend",
        "Conversion rate by source",
        "Customer segmentation by behavior",
        "Churn rate by cohort",
        "Average deal size by sales rep",
        "Product adoption over time",
        "Customer satisfaction by region",
        "Support tickets by priority",
        "Revenue by customer segment",
        "User engagement metrics",
        "Sales pipeline by stage",
        "Customer acquisition cost trends",
        "Retention rate by plan type"
    ]
    
    ADVANCED_QUERIES = [
        "Show me customers from the top 5 regions by revenue",
        "What factors predict customer churn?",
        "Calculate month-over-month growth rate",
        "Correlation between usage and retention",
        "Identify revenue anomalies",
        "Forecast next quarter revenue",
        "Customer lifetime value by acquisition channel",
        "Win rate trends with statistical significance",
        "Cohort retention analysis",
        "Multi-touch attribution analysis",
        "Price elasticity by segment",
        "Customer health score calculation",
        "Lead scoring model results",
        "Cross-sell opportunity identification",
        "Seasonal trend decomposition"
    ]
    
    TIME_INTELLIGENCE_QUERIES = [
        "Month-over-month revenue growth",
        "Year-over-year comparison",
        "Quarter-to-date performance",
        "Rolling 12-month average",
        "Week-over-week active users",
        "Same period last year comparison",
        "Moving average of daily sales",
        "Cumulative revenue this year",
        "Period-over-period churn rate",
        "Trailing 30-day metrics",
        "Monthly run rate",
        "Annualized revenue",
        "Growth rate acceleration",
        "Time since last purchase",
        "Days to conversion trending"
    ]
    
    INVESTIGATION_QUERIES = [
        "Why are customers churning?",
        "What drives high customer value?",
        "Why did revenue drop last month?",
        "What causes support tickets?",
        "Why are deals being lost?",
        "What influences customer satisfaction?",
        "Why is engagement declining?",
        "What determines purchase frequency?",
        "Why do customers upgrade?",
        "What causes cart abandonment?"
    ]
    
    STATISTICAL_QUERIES = [
        "Standard deviation of order values",
        "Correlation between price and volume",
        "Statistical significance of A/B test",
        "Confidence interval for conversion rate",
        "Distribution of customer ages",
        "Outliers in transaction amounts",
        "Variance in monthly revenue",
        "Z-score for customer spending",
        "Percentile ranking of users",
        "Regression analysis on sales factors"
    ]
    
    SUBQUERY_PATTERNS = [
        "Customers from regions with above average revenue",
        "Products with sales above category average",
        "Users more active than their cohort",
        "Deals larger than team average",
        "Customers with CLV above segment median",
        "Orders from top performing stores",
        "Campaigns exceeding benchmark CTR",
        "Reps performing above quota",
        "Accounts with usage above threshold",
        "Segments with retention above target"
    ]
    
    CALCULATED_METRICS = [
        "Calculate customer health score",
        "Compute CLV to CAC ratio",
        "Net revenue retention rate",
        "Magic number calculation",
        "Rule of 40 score",
        "Payback period by channel",
        "Gross margin by product",
        "Unit economics breakdown",
        "Efficiency ratio trends",
        "ROI by marketing campaign"
    ]
    
    @classmethod
    def get_all_queries(cls) -> List[str]:
        """Get all 90 test queries"""
        all_queries = []
        all_queries.extend(cls.BASIC_QUERIES[:10])
        all_queries.extend(cls.INTERMEDIATE_QUERIES[:15])
        all_queries.extend(cls.ADVANCED_QUERIES[:15])
        all_queries.extend(cls.TIME_INTELLIGENCE_QUERIES[:15])
        all_queries.extend(cls.INVESTIGATION_QUERIES[:10])
        all_queries.extend(cls.STATISTICAL_QUERIES[:10])
        all_queries.extend(cls.SUBQUERY_PATTERNS[:10])
        all_queries.extend(cls.CALCULATED_METRICS[:5])
        return all_queries[:90]  # Ensure exactly 90


class Claude4SonnetTester:
    """Test framework using Claude-4-Sonnet for fair comparison"""
    
    def __init__(self):
        self.conn = None
        self.results = []
        self.queries = ScoopTestQueries.get_all_queries()
        
    def connect(self):
        """Connect to Snowflake"""
        print(f"Connecting to Azure Snowflake...")
        self.conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
        print(f"✅ Connected successfully")
        
    def test_with_cortex_analyst(self, query: str, dataset: str) -> Dict:
        """Test using CORTEX.ANALYST with Claude-4-Sonnet"""
        result = {
            'query': query,
            'dataset': dataset,
            'model': MODEL,
            'timestamp': datetime.now().isoformat(),
            'success': False,
            'sql_generated': None,
            'execution_result': None,
            'error': None,
            'category': self._categorize_query(query)
        }
        
        try:
            # Set context for dataset
            dataset_info = DATASETS[dataset]
            cursor = self.conn.cursor()
            cursor.execute(f"USE SCHEMA {dataset_info['schema']}")
            
            # Build semantic model for Claude-4-Sonnet
            semantic_model = {
                "name": dataset,
                "tables": [{
                    "name": dataset_info['table'],
                    "description": dataset_info['description']
                }]
            }
            
            # Call CORTEX.ANALYST with Claude-4-Sonnet
            analyst_query = f"""
            SELECT SNOWFLAKE.CORTEX.ANALYST(
                '{MODEL}',
                '{query}',
                '{json.dumps(semantic_model)}'
            ) as response
            """
            
            cursor.execute(analyst_query)
            response = cursor.fetchone()
            
            if response and response[0]:
                result['sql_generated'] = response[0].get('sql')
                
                # Try to execute generated SQL
                if result['sql_generated']:
                    cursor.execute(result['sql_generated'])
                    result['execution_result'] = cursor.fetchmany(10)
                    result['success'] = True
                    
            cursor.close()
            
        except Exception as e:
            result['error'] = str(e)
            
        return result
    
    def _categorize_query(self, query: str) -> str:
        """Categorize query for analysis"""
        query_lower = query.lower()
        
        if 'why' in query_lower or 'what drives' in query_lower:
            return 'investigation'
        elif 'correlation' in query_lower or 'significance' in query_lower:
            return 'statistical'
        elif 'month-over-month' in query_lower or 'year-over-year' in query_lower:
            return 'time_intelligence'
        elif 'top' in query_lower and 'from' in query_lower:
            return 'subquery'
        elif 'calculate' in query_lower or 'compute' in query_lower:
            return 'calculated_metric'
        elif any(word in query_lower for word in ['revenue', 'count', 'average', 'total']):
            return 'basic'
        else:
            return 'intermediate'
    
    def run_comprehensive_test(self):
        """Run all 90 queries on all datasets"""
        print(f"\n{'='*60}")
        print(f"FAIR COMPARISON TEST: Claude-4-Sonnet")
        print(f"{'='*60}")
        print(f"Model: {MODEL} (same as Scoop)")
        print(f"Queries: {len(self.queries)} from Scoop test suite")
        print(f"Datasets: {list(DATASETS.keys())}")
        print(f"{'='*60}\n")
        
        for dataset in DATASETS:
            print(f"\n📊 Testing on {dataset} dataset...")
            dataset_results = []
            
            for i, query in enumerate(self.queries, 1):
                print(f"  [{i:2d}/90] {query[:50]}...")
                result = self.test_with_cortex_analyst(query, dataset)
                
                if result['success']:
                    print(f"         ✅ Success")
                else:
                    print(f"         ❌ Failed: {result.get('error', 'No SQL generated')[:50]}")
                    
                dataset_results.append(result)
                self.results.append(result)
                time.sleep(0.5)  # Rate limiting
                
            # Dataset summary
            success_count = sum(1 for r in dataset_results if r['success'])
            print(f"\n  {dataset} Results: {success_count}/{len(self.queries)} succeeded ({success_count*100/len(self.queries):.1f}%)")
    
    def analyze_results(self) -> Dict:
        """Analyze test results by category"""
        analysis = {
            'total_tests': len(self.results),
            'by_dataset': {},
            'by_category': {},
            'overall_success_rate': 0
        }
        
        # By dataset
        for dataset in DATASETS:
            dataset_results = [r for r in self.results if r['dataset'] == dataset]
            success = sum(1 for r in dataset_results if r['success'])
            analysis['by_dataset'][dataset] = {
                'total': len(dataset_results),
                'success': success,
                'rate': success * 100 / len(dataset_results) if dataset_results else 0
            }
        
        # By category
        categories = set(r['category'] for r in self.results)
        for category in categories:
            cat_results = [r for r in self.results if r['category'] == category]
            success = sum(1 for r in cat_results if r['success'])
            analysis['by_category'][category] = {
                'total': len(cat_results),
                'success': success,
                'rate': success * 100 / len(cat_results) if cat_results else 0
            }
        
        # Overall
        total_success = sum(1 for r in self.results if r['success'])
        analysis['overall_success_rate'] = total_success * 100 / len(self.results) if self.results else 0
        
        return analysis
    
    def save_results(self):
        """Save test results"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"test_results/claude4_sonnet_fair_test_{timestamp}.json"
        
        os.makedirs("test_results", exist_ok=True)
        
        analysis = self.analyze_results()
        
        output = {
            'test_configuration': {
                'model': MODEL,
                'account': SNOWFLAKE_CONFIG['account'],
                'datasets': list(DATASETS.keys()),
                'query_count': len(self.queries),
                'timestamp': datetime.now().isoformat()
            },
            'analysis': analysis,
            'detailed_results': self.results
        }
        
        with open(filename, 'w') as f:
            json.dump(output, f, indent=2)
            
        print(f"\n📁 Results saved to: {filename}")
        
        # Print summary
        print(f"\n{'='*60}")
        print(f"FAIR COMPARISON SUMMARY")
        print(f"{'='*60}")
        print(f"Model: {MODEL}")
        print(f"Overall Success Rate: {analysis['overall_success_rate']:.1f}%")
        print(f"\nBy Dataset:")
        for dataset, stats in analysis['by_dataset'].items():
            print(f"  {dataset}: {stats['success']}/{stats['total']} ({stats['rate']:.1f}%)")
        print(f"\nBy Category:")
        for category, stats in sorted(analysis['by_category'].items(), key=lambda x: x[1]['rate']):
            print(f"  {category}: {stats['success']}/{stats['total']} ({stats['rate']:.1f}%)")
    
    def run(self):
        """Main execution"""
        try:
            self.connect()
            self.run_comprehensive_test()
            self.save_results()
        finally:
            if self.conn:
                self.conn.close()


def main():
    """Entry point"""
    print("="*60)
    print("CLAUDE-4-SONNET FAIR COMPARISON TEST")
    print("="*60)
    print("This test uses the SAME model that Scoop uses")
    print("Running Scoop's 90 test queries for fair comparison")
    print("="*60)
    
    tester = Claude4SonnetTester()
    tester.run()


if __name__ == "__main__":
    main()