#!/usr/bin/env python3

import snowflake.connector

# Connect to Snowflake
conn = snowflake.connector.connect(
    account='toajlpe-nfb33705',
    user='bradscoop',
    password='D6c2BmtJWPy3dM7',
    database='SCOOP_BENCHMARK',
    schema='TEST_DATA',
    warehouse='COMPUTE_WH'
)
cursor = conn.cursor()

print("Available tables in SCOOP_BENCHMARK.TEST_DATA:")
print("-" * 50)

cursor.execute("""
    SELECT table_name, row_count
    FROM INFORMATION_SCHEMA.TABLES 
    WHERE table_schema = 'TEST_DATA'
    ORDER BY table_name
""")

tables = cursor.fetchall()
for table_name, row_count in tables:
    print(f"{table_name}: {row_count} rows")

print("\n\nChecking for tables with date columns:")
print("-" * 50)

cursor.execute("""
    SELECT DISTINCT 
        t.table_name,
        c.column_name,
        c.data_type
    FROM INFORMATION_SCHEMA.TABLES t
    JOIN INFORMATION_SCHEMA.COLUMNS c 
        ON t.table_name = c.table_name 
        AND t.table_schema = c.table_schema
    WHERE t.table_schema = 'TEST_DATA'
    AND (c.data_type LIKE '%DATE%' OR c.data_type LIKE '%TIME%')
    ORDER BY t.table_name, c.column_name
""")

date_tables = cursor.fetchall()
if date_tables:
    current_table = None
    for table_name, col_name, col_type in date_tables:
        if current_table != table_name:
            print(f"\n{table_name}:")
            current_table = table_name
        print(f"  {col_name}: {col_type}")
else:
    print("No tables with date/time columns found")

cursor.close()
conn.close()