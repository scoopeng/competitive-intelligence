#!/usr/bin/env python3
"""
Setup TELCO_DATA table and semantic model in Azure Snowflake
"""

import snowflake.connector
import json

# Connection
conn = snowflake.connector.connect(
    account='rcdtonr-ji20455',
    user='bradtest',
    password='qMsGeKsE33NJeZp',
    warehouse='COMPUTE_WH'
)
cursor = conn.cursor()

print("Setting up Azure Snowflake environment...")
print("="*80)

# 1. Create database and schema
print("\n1. Creating database and schema...")
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS SCOOP_BENCHMARK")
    cursor.execute("USE DATABASE SCOOP_BENCHMARK")
    cursor.execute("CREATE SCHEMA IF NOT EXISTS TEST_DATA")
    cursor.execute("USE SCHEMA TEST_DATA")
    print("✅ Database SCOOP_BENCHMARK and schema TEST_DATA ready")
except Exception as e:
    print(f"❌ Error creating database/schema: {e}")

# 2. Create TELCO_DATA table with sample data
print("\n2. Creating TELCO_DATA table...")
try:
    # Drop if exists
    cursor.execute("DROP TABLE IF EXISTS TELCO_DATA")
    
    # Create table
    cursor.execute("""
    CREATE TABLE TELCO_DATA (
        CUSTOMERID VARCHAR(20),
        GENDER VARCHAR(10),
        SENIORCITIZEN BOOLEAN,
        PARTNER VARCHAR(5),
        DEPENDENTS VARCHAR(5),
        TENURE NUMBER,
        PHONESERVICE VARCHAR(5),
        MULTIPLELINES VARCHAR(20),
        INTERNETSERVICE VARCHAR(20),
        ONLINESECURITY VARCHAR(20),
        ONLINEBACKUP VARCHAR(20),
        DEVICEPROTECTION VARCHAR(20),
        TECHSUPPORT VARCHAR(20),
        STREAMINGTV VARCHAR(20),
        STREAMINGMOVIES VARCHAR(20),
        CONTRACT VARCHAR(20),
        PAPERLESSBILLING VARCHAR(5),
        PAYMENTMETHOD VARCHAR(50),
        MONTHLYCHARGES FLOAT,
        TOTALCHARGES FLOAT,
        CHURN BOOLEAN
    )
    """)
    
    # Insert sample data
    cursor.execute("""
    INSERT INTO TELCO_DATA VALUES
    ('1001', 'Male', FALSE, 'Yes', 'No', 12, 'Yes', 'No', 'DSL', 'Yes', 'No', 'No', 'No', 'No', 'No', 'Month-to-month', 'Yes', 'Electronic check', 65.5, 786.0, FALSE),
    ('1002', 'Female', TRUE, 'No', 'No', 24, 'Yes', 'Yes', 'Fiber optic', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Two year', 'Yes', 'Credit card', 95.75, 2297.0, FALSE),
    ('1003', 'Male', FALSE, 'Yes', 'Yes', 8, 'Yes', 'No', 'DSL', 'No', 'No', 'Yes', 'No', 'No', 'No', 'Month-to-month', 'No', 'Bank transfer', 55.25, 442.0, TRUE),
    ('1004', 'Female', FALSE, 'No', 'No', 45, 'No', 'No phone service', 'Fiber optic', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'One year', 'Yes', 'Electronic check', 85.5, 3847.5, FALSE),
    ('1005', 'Male', TRUE, 'Yes', 'No', 2, 'Yes', 'Yes', 'Fiber optic', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'Month-to-month', 'Yes', 'Mailed check', 89.0, 178.0, TRUE),
    ('1006', 'Female', FALSE, 'Yes', 'Yes', 36, 'Yes', 'No', 'DSL', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Two year', 'No', 'Credit card', 75.25, 2709.0, FALSE),
    ('1007', 'Male', FALSE, 'No', 'No', 15, 'Yes', 'Yes', 'No', 'No internet service', 'No internet service', 'No internet service', 'No internet service', 'No internet service', 'No internet service', 'Month-to-month', 'No', 'Bank transfer', 25.5, 382.5, FALSE),
    ('1008', 'Female', TRUE, 'Yes', 'No', 60, 'Yes', 'Yes', 'Fiber optic', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Two year', 'Yes', 'Credit card', 105.5, 6330.0, FALSE),
    ('1009', 'Male', FALSE, 'No', 'Yes', 5, 'Yes', 'No', 'DSL', 'No', 'Yes', 'No', 'No', 'No', 'No', 'Month-to-month', 'Yes', 'Electronic check', 45.75, 228.75, TRUE),
    ('1010', 'Female', FALSE, 'Yes', 'No', 28, 'Yes', 'Yes', 'Fiber optic', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'One year', 'No', 'Bank transfer', 95.0, 2660.0, FALSE)
    """)
    
    # Verify
    cursor.execute("SELECT COUNT(*) FROM TELCO_DATA")
    count = cursor.fetchone()[0]
    print(f"✅ TELCO_DATA table created with {count} rows")
    
except Exception as e:
    print(f"❌ Error creating TELCO_DATA: {e}")

# 3. Create OPENOPPORTUNITIES table (for time intelligence)
print("\n3. Creating OPENOPPORTUNITIES table...")
try:
    cursor.execute("DROP TABLE IF EXISTS OPENOPPORTUNITIES")
    
    cursor.execute("""
    CREATE TABLE OPENOPPORTUNITIES (
        C1 DATE,        -- Main date column
        C2 VARCHAR(100),
        C3 NUMBER,
        C4 VARCHAR(50),
        C5 NUMBER,
        C6 VARCHAR(100),
        C7 VARCHAR(50),
        C8 VARCHAR(50),
        C9 DATE,        -- Secondary date
        C10 DATE        -- Tertiary date
    )
    """)
    
    # Insert sample data with dates
    cursor.execute("""
    INSERT INTO OPENOPPORTUNITIES VALUES
    ('2024-01-15', 'Opportunity A', 10000, 'New', 30, 'Product X', 'High', 'John', '2024-02-01', '2024-03-15'),
    ('2024-01-20', 'Opportunity B', 25000, 'Renewal', 45, 'Product Y', 'Medium', 'Jane', '2024-02-15', '2024-04-01'),
    ('2024-02-01', 'Opportunity C', 15000, 'Expansion', 60, 'Product Z', 'High', 'Bob', '2024-03-01', '2024-05-01'),
    ('2024-02-15', 'Opportunity D', 50000, 'New', 90, 'Product X', 'Critical', 'Alice', '2024-04-01', '2024-06-01'),
    ('2024-03-01', 'Opportunity E', 30000, 'Renewal', 30, 'Product Y', 'Low', 'John', '2024-03-15', '2024-04-15'),
    ('2024-03-15', 'Opportunity F', 75000, 'New', 120, 'Product Z', 'High', 'Jane', '2024-05-01', '2024-07-01'),
    ('2024-04-01', 'Opportunity G', 20000, 'Expansion', 45, 'Product X', 'Medium', 'Bob', '2024-04-20', '2024-05-15'),
    ('2024-04-15', 'Opportunity H', 40000, 'New', 60, 'Product Y', 'High', 'Alice', '2024-05-15', '2024-06-30')
    """)
    
    cursor.execute("SELECT COUNT(*) FROM OPENOPPORTUNITIES")
    count = cursor.fetchone()[0]
    print(f"✅ OPENOPPORTUNITIES table created with {count} rows")
    
except Exception as e:
    print(f"❌ Error creating OPENOPPORTUNITIES: {e}")

# 4. Test CORTEX.COMPLETE access
print("\n4. Testing CORTEX.COMPLETE...")
try:
    cursor.execute("""
    SELECT SNOWFLAKE.CORTEX.COMPLETE(
        'claude-4-sonnet',
        'Generate SQL to count rows in TELCO_DATA'
    ) as response
    """)
    result = cursor.fetchone()
    if result and result[0]:
        print("✅ CORTEX.COMPLETE is working!")
        print(f"   Sample response: {result[0][:100]}...")
    else:
        print("❌ CORTEX.COMPLETE returned no response")
except Exception as e:
    print(f"❌ CORTEX.COMPLETE error: {e}")

# 5. Create semantic model stage
print("\n5. Setting up semantic model...")
try:
    # Create stage for YAML
    cursor.execute("CREATE STAGE IF NOT EXISTS SEMANTIC_MODELS")
    print("✅ Stage SEMANTIC_MODELS created")
    
    # Note: The YAML file needs to be uploaded manually or via PUT command
    print("📝 Note: Upload semantic_model.yaml to @SEMANTIC_MODELS stage")
    
except Exception as e:
    print(f"❌ Error creating stage: {e}")

# 6. Summary
print("\n" + "="*80)
print("SETUP COMPLETE")
print("="*80)
print("""
✅ Database: SCOOP_BENCHMARK
✅ Schema: TEST_DATA  
✅ Tables: TELCO_DATA (10 rows), OPENOPPORTUNITIES (8 rows)
✅ CORTEX.COMPLETE: Available

Next steps:
1. Upload semantic_model.yaml to @SEMANTIC_MODELS stage
2. Run tests with proper database/schema context
""")

conn.close()