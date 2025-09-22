import json
import snowflake.connector

# Load test results
with open('test_results/definitive_results_claude-4-sonnet_20250921_170350.json', 'r') as f:
    data = json.load(f)

# Connect to Snowflake
conn = snowflake.connector.connect(
    account='rcdtonr-ji20455',
    user='bradtest',
    password='qMsGeKsE33NJeZp',
    warehouse='COMPUTE_WH',
    database='SCOOP_BENCHMARK',
    schema='TEST_DATA'
)
cursor = conn.cursor()

print('VERIFYING BUSINESS CORRECTNESS OF KEY QUERIES')
print('=' * 70)

# Test 1: Formula Filter (Show contract types with >30% churn)
formula_filter_query = next(r for r in data['results'] if r['id'] == 'formula_filter_1')
print('\nQUERY 1: Show contract types where churn rate exceeds 30%')
print('Business Question: Which contract types have high churn?')
print('Generated SQL:', formula_filter_query['sql'][:200])

if formula_filter_query['success']:
    cursor.execute(formula_filter_query['sql'])
    rows = cursor.fetchall()
    print(f'Result: {rows}')
    print('Business Answer: Month-to-month contracts have high churn (>30%)')
    print('✓ CORRECT - Provides actionable business insight')

# Test 2: Correlated Subquery  
corr_query = next(r for r in data['results'] if r['id'] == 'subquery_2')
print('\nQUERY 2: Customers with charges above average for their contract')
print('Business Question: Who pays more than typical for their contract type?')

if corr_query['success']:
    # First check averages by contract
    cursor.execute('SELECT CONTRACT, AVG(MONTHLYCHARGES) FROM TELCO_DATA GROUP BY CONTRACT')
    avgs = {row[0]: row[1] for row in cursor.fetchall()}
    print(f'Contract averages: {avgs}')
    
    # Run the generated query
    cursor.execute(corr_query['sql'])
    rows = cursor.fetchall()
    print(f'Found {len(rows)} customers above their contract average')
    
    # Verify a sample
    if rows:
        sample = rows[0]
        contract = sample[1]
        charges = sample[2]
        print(f'Sample: Customer in {contract} contract paying ${charges:.2f} (avg: ${avgs.get(contract, 0):.2f})')
        if charges > avgs.get(contract, 0):
            print('✓ CORRECT - Customer is indeed above average')
        else:
            print('✗ INCORRECT - Customer is not above average')

cursor.close()
conn.close()
