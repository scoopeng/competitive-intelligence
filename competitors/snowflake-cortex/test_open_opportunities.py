#!/usr/bin/env python3

import snowflake.connector
import json
from datetime import datetime
import os

# Get connection parameters from environment
ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT', 'ry28412.us-east-1')
USER = os.getenv('SNOWFLAKE_USER', 'brad_peters')
PASSWORD = os.getenv('SNOWFLAKE_PASSWORD', 'Ilovelife12!')
DATABASE = 'SCOOP_BENCHMARK'
SCHEMA = 'TEST_DATA'
WAREHOUSE = 'COMPUTE_WH'

def test_open_opportunities_table():
    """Check the OPEN_OPPORTUNITIES table structure and sample data"""
    
    print("=" * 80)
    print("CHECKING OPEN_OPPORTUNITIES TABLE STRUCTURE")
    print("=" * 80)
    
    # Connect to Snowflake
    conn = snowflake.connector.connect(
        account='toajlpe-nfb33705',
        user='bradscoop',
        password='D6c2BmtJWPy3dM7',
        database=DATABASE,
        schema=SCHEMA,
        warehouse=WAREHOUSE
    )
    
    cursor = conn.cursor()
    
    # Get column information
    print("\n1. Table Columns:")
    print("-" * 40)
    cursor.execute("""
        SELECT column_name, data_type 
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE table_name = 'OPEN_OPPORTUNITIES' 
        AND table_schema = 'TEST_DATA'
        ORDER BY ordinal_position
    """)
    
    columns = cursor.fetchall()
    for col_name, col_type in columns:
        print(f"  {col_name}: {col_type}")
    
    # Get sample data
    print("\n2. Sample Data (5 rows):")
    print("-" * 40)
    cursor.execute("SELECT * FROM OPEN_OPPORTUNITIES LIMIT 5")
    
    # Get column names
    col_names = [desc[0] for desc in cursor.description]
    print("Columns:", ", ".join(col_names))
    print()
    
    rows = cursor.fetchall()
    for i, row in enumerate(rows, 1):
        print(f"Row {i}:")
        for col, val in zip(col_names, row):
            print(f"  {col}: {val}")
        print()
    
    # Check date range
    print("\n3. Date Range in Data:")
    print("-" * 40)
    
    # Find date columns
    date_columns = []
    for col_name, col_type in columns:
        if 'DATE' in col_type or 'TIME' in col_type:
            date_columns.append(col_name)
    
    if date_columns:
        print(f"Found date columns: {', '.join(date_columns)}")
        for date_col in date_columns:
            cursor.execute(f"""
                SELECT 
                    MIN({date_col}) as min_date,
                    MAX({date_col}) as max_date,
                    COUNT(DISTINCT {date_col}) as unique_dates
                FROM OPEN_OPPORTUNITIES
                WHERE {date_col} IS NOT NULL
            """)
            result = cursor.fetchone()
            if result:
                print(f"\n  {date_col}:")
                print(f"    Min: {result[0]}")
                print(f"    Max: {result[1]}")
                print(f"    Unique dates: {result[2]}")
    else:
        print("No date/timestamp columns found")
    
    # Get row count
    print("\n4. Table Statistics:")
    print("-" * 40)
    cursor.execute("SELECT COUNT(*) FROM OPEN_OPPORTUNITIES")
    count = cursor.fetchone()[0]
    print(f"Total rows: {count}")
    
    cursor.close()
    conn.close()
    
    return date_columns

if __name__ == "__main__":
    date_cols = test_open_opportunities_table()
    
    if date_cols:
        print("\n" + "=" * 80)
        print("RECOMMENDATION:")
        print("=" * 80)
        print(f"✅ OPEN_OPPORTUNITIES has date columns: {', '.join(date_cols)}")
        print("✅ We should test time intelligence queries with this dataset")
        print("✅ This will expose CORTEX.COMPLETE's limitations with:")
        print("   - Period-over-period comparisons")
        print("   - Running totals")
        print("   - Date windowing")
        print("   - Trend analysis")
    else:
        print("\n⚠️  No date columns found - continue with TELCO_DATA only")