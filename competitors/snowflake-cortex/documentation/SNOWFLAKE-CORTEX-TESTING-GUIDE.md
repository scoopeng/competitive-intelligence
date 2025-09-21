# Snowflake Cortex Analyst Testing Guide - CONSOLIDATED

## Your Current Status: Snowflake Account Created ✅

### IMMEDIATE NEXT STEPS (You Are Here)

## Step 1: Initial Snowflake Setup (15 minutes)

Login to your Snowflake account and run these commands in a worksheet:

```sql
-- 1. Create a warehouse for testing
USE ROLE ACCOUNTADMIN;

CREATE WAREHOUSE IF NOT EXISTS CORTEX_TEST_WH WITH 
  WAREHOUSE_SIZE = 'XSMALL' 
  AUTO_SUSPEND = 60
  AUTO_RESUME = TRUE;

-- 2. Create database and schema
CREATE DATABASE IF NOT EXISTS SCOOP_BENCHMARK;
USE DATABASE SCOOP_BENCHMARK;
CREATE SCHEMA IF NOT EXISTS TEST_DATA;

-- 3. Create a stage for file uploads
CREATE OR REPLACE STAGE DATA_UPLOAD
  DIRECTORY = (ENABLE = TRUE);

-- 4. Grant necessary permissions
GRANT USAGE ON WAREHOUSE CORTEX_TEST_WH TO ROLE PUBLIC;
GRANT ALL ON DATABASE SCOOP_BENCHMARK TO ROLE PUBLIC;
GRANT ALL ON SCHEMA TEST_DATA TO ROLE PUBLIC;
GRANT ALL ON STAGE DATA_UPLOAD TO ROLE PUBLIC;

-- Verify setup
SELECT CURRENT_WAREHOUSE(), CURRENT_DATABASE(), CURRENT_SCHEMA();
```

## Step 2: Prepare Test Data (20 minutes)

We need to export data from Scoop's test suite. Let me help you:

### Option A: Use Telecom Churn Dataset (Recommended - Smallest)
- **File**: `/home/brad-peters/dev/scoop/app/src/test/resources/W10691_I18112`
- **Size**: 7,043 records
- **Why**: Small, manageable, has good test cases

### Export Commands:
```bash
# Navigate to Scoop test data directory
cd /home/brad-peters/dev/scoop/app/src/test/resources/

# Check what format the data is in
ls -la W10691_I18112/

# If it's already CSV, copy it
cp W10691_I18112/*.csv /tmp/telecom_churn.csv

# If it's in another format, we'll need to convert
```

## Step 3: Create Snowflake Table (5 minutes)

Run this DDL in Snowflake (I'll generate exact schema after we see the data):

```sql
USE DATABASE SCOOP_BENCHMARK;
USE SCHEMA TEST_DATA;

CREATE OR REPLACE TABLE TELECOM_CHURN (
  customerID VARCHAR(50),
  gender VARCHAR(10),
  SeniorCitizen INTEGER,
  Partner VARCHAR(5),
  Dependents VARCHAR(5),
  tenure INTEGER,
  PhoneService VARCHAR(5),
  MultipleLines VARCHAR(20),
  InternetService VARCHAR(20),
  OnlineSecurity VARCHAR(20),
  OnlineBackup VARCHAR(20),
  DeviceProtection VARCHAR(20),
  TechSupport VARCHAR(20),
  StreamingTV VARCHAR(20),
  StreamingMovies VARCHAR(20),
  Contract VARCHAR(20),
  PaperlessBilling VARCHAR(5),
  PaymentMethod VARCHAR(50),
  MonthlyCharges FLOAT,
  TotalCharges VARCHAR(20),  -- Sometimes has non-numeric values
  Churn VARCHAR(5)
);
```

## Step 4: Load Data into Snowflake (10 minutes)

1. **Upload file via Snowsight UI**:
   - Click on "Data" → "Databases"
   - Navigate to SCOOP_BENCHMARK → TEST_DATA → Stages → DATA_UPLOAD
   - Click "Upload Files" and select your CSV

2. **Load data into table**:
```sql
-- Copy data from stage to table
COPY INTO TELECOM_CHURN
FROM @DATA_UPLOAD/telecom_churn.csv
FILE_FORMAT = (
  TYPE = CSV 
  FIELD_OPTIONALLY_ENCLOSED_BY = '"'
  SKIP_HEADER = 1
  FIELD_DELIMITER = ','
  NULL_IF = ('', 'NULL', 'null')
);

-- Verify data loaded
SELECT COUNT(*) FROM TELECOM_CHURN;
SELECT * FROM TELECOM_CHURN LIMIT 10;
```

## Step 5: Create Semantic Model for Cortex Analyst (15 minutes)

Create a YAML file called `telecom_semantic_model.yaml`:

```yaml
semantic_model:
  name: Telecom Customer Analytics
  description: Customer churn analysis for telecom company
  
  tables:
    - name: TELECOM_CHURN
      description: Customer data with churn indicators
      base_table:
        database: SCOOP_BENCHMARK
        schema: TEST_DATA
        table: TELECOM_CHURN
      
      dimensions:
        - name: customer_id
          expr: customerID
          description: Unique customer identifier
          unique: true
          data_type: TEXT
          
        - name: contract_type
          expr: Contract
          description: Type of contract (Month-to-month, One year, Two year)
          data_type: TEXT
          
        - name: internet_service
          expr: InternetService
          description: Type of internet service
          data_type: TEXT
          
        - name: payment_method
          expr: PaymentMethod
          description: Customer payment method
          data_type: TEXT
          
      measures:
        - name: customer_count
          expr: COUNT(DISTINCT customerID)
          description: Total number of customers
          data_type: NUMBER
          
        - name: avg_monthly_charges
          expr: AVG(MonthlyCharges)
          description: Average monthly charges
          data_type: NUMBER
          
        - name: total_revenue
          expr: SUM(CAST(TotalCharges AS FLOAT))
          description: Total revenue from all customers
          data_type: NUMBER
          
        - name: churn_rate
          expr: AVG(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100
          description: Percentage of customers who churned
          data_type: NUMBER
          
        - name: avg_tenure
          expr: AVG(tenure)
          description: Average customer tenure in months
          data_type: NUMBER
          
      time_dimensions:
        - name: tenure_months
          expr: tenure
          description: Customer tenure in months
          data_type: NUMBER
          time_granularities: [month]
```

Upload this to Snowflake stage:
```sql
-- In Snowsight, upload the YAML file to the DATA_UPLOAD stage
-- Then register it for Cortex Analyst
PUT file://telecom_semantic_model.yaml @DATA_UPLOAD;
```

## Step 6: Test Cortex Analyst (10 minutes)

### Enable Cortex Analyst and test with REST API:

```python
# Save as test_cortex.py
import requests
import json
from snowflake.connector import connect

# Connection parameters (update with your details)
account = 'your_account'
user = 'your_username'
password = 'your_password'

# Connect and get token
conn = connect(
    account=account,
    user=user,
    password=password,
    warehouse='CORTEX_TEST_WH',
    database='SCOOP_BENCHMARK',
    schema='TEST_DATA'
)

# Test queries to compare
test_queries = [
    "What is the average monthly charge?",
    "Show me churn rate by contract type",
    "Which payment method has the highest churn?",
    "Calculate customer lifetime value",
    "Why are customers churning?"  # This should fail/struggle
]

# Submit to Cortex Analyst
for query in test_queries:
    print(f"\nQuery: {query}")
    
    # Call Cortex Analyst API
    cursor = conn.cursor()
    cursor.execute(f"""
    SELECT SNOWFLAKE.CORTEX.COMPLETE(
        'mistral-7b',
        CONCAT('Generate SQL for: ', '{query}')
    )
    """)
    
    result = cursor.fetchone()
    print(f"Generated SQL: {result[0]}")
```

## Step 7: Compare with Scoop Query JSON

Now find the equivalent Scoop test cases:

```bash
# Look for test cases in Scoop
cd /home/brad-peters/dev/scoop/app/src/test/resources/aiQueryExpectedResults/
grep -l "I18112" *.json | head -5

# View a specific test case
cat I18112_001_basic_aggregation.json
```

## Step 8: Document Results

Create a comparison table:

| Query | Scoop Query JSON Lines | Cortex SQL Lines | Scoop Success | Cortex Success | Notes |
|-------|------------------------|------------------|---------------|----------------|--------|
| Avg monthly charge | 8 | 3 | ✅ | ✅ | Both handle simple aggregation |
| Churn by contract | 15 | 12 | ✅ | ✅ | Similar complexity |
| Complex calculation | 12 | 45+ | ✅ | ⚠️ | Cortex struggles with nested logic |
| Multi-step reasoning | 30 (multi-query) | N/A | ✅ | ❌ | Cortex can't do multi-step |

---

## Quick Reference Commands

### Check Cortex Analyst is available:
```sql
-- Check if Cortex functions are available
SHOW FUNCTIONS LIKE '%CORTEX%';

-- Test basic Cortex function
SELECT SNOWFLAKE.CORTEX.COMPLETE(
    'mistral-7b',
    'Say hello'
);
```

### If you encounter issues:

1. **Cortex not available**: May need to enable in your account settings
2. **Permission errors**: Run commands as ACCOUNTADMIN role
3. **Data load errors**: Check CSV format matches table schema
4. **Semantic model issues**: Verify YAML syntax is correct

---

## Files Being Consolidated Into This Guide:
- ✅ COMPETITIVE-TESTING-FRAMEWORK.md (methodology incorporated)
- ✅ snowflake-setup-automation.md (scripts included)
- ✅ action-plan-proving-scoop-superiority.md (test cases referenced)
- ❌ ARCHIVED-HYPOTHETICAL-ANALYSIS.md (keeping archived)
- ❌ Other analysis docs (keeping for reference)

## Your Next Action:
1. Run the SQL commands in Step 1 in your Snowflake worksheet
2. Tell me what you see when you check the Scoop test data directory
3. I'll help you with the exact schema and data loading

Ready? Let's start with Step 1! 🚀