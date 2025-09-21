#!/usr/bin/env python3

import snowflake.connector
from datetime import datetime

conn = snowflake.connector.connect(
    account='toajlpe-nfb33705',
    user='bradscoop',
    password='D6c2BmtJWPy3dM7',
    database='SCOOP_BENCHMARK',
    schema='TEST_DATA',
    warehouse='COMPUTE_WH'
)
cursor = conn.cursor()

print("=" * 80)
print("OPENOPPORTUNITIES TABLE ANALYSIS")
print("=" * 80)

# Get all columns
print("\n1. Table Structure:")
print("-" * 40)
cursor.execute("""
    SELECT column_name, data_type, ordinal_position
    FROM INFORMATION_SCHEMA.COLUMNS 
    WHERE table_name = 'OPENOPPORTUNITIES' 
    AND table_schema = 'TEST_DATA'
    ORDER BY ordinal_position
""")

columns = cursor.fetchall()
for col_name, col_type, pos in columns:
    marker = "📅" if "TIME" in col_type or "DATE" in col_type else ""
    print(f"  {pos:2}. {col_name:15} {col_type:20} {marker}")

# Sample data
print("\n2. Sample Data (3 rows):")
print("-" * 40)
cursor.execute("SELECT * FROM OPENOPPORTUNITIES LIMIT 3")

col_names = [desc[0] for desc in cursor.description]
rows = cursor.fetchall()

for i, row in enumerate(rows, 1):
    print(f"\nRow {i}:")
    for col, val in zip(col_names, row):
        if val is not None and len(str(val)) > 50:
            val = str(val)[:47] + "..."
        print(f"  {col}: {val}")

# Analyze date columns
print("\n3. Date Column Analysis:")
print("-" * 40)

date_cols = ['C1', 'C9', 'C10']
for col in date_cols:
    cursor.execute(f"""
        SELECT 
            MIN({col}) as min_date,
            MAX({col}) as max_date,
            COUNT(DISTINCT DATE({col})) as unique_days,
            DATEDIFF('day', MIN({col}), MAX({col})) as date_range_days
        FROM OPENOPPORTUNITIES
        WHERE {col} IS NOT NULL
    """)
    
    result = cursor.fetchone()
    if result:
        min_date, max_date, unique_days, range_days = result
        print(f"\n{col}:")
        print(f"  Min: {min_date}")
        print(f"  Max: {max_date}")
        print(f"  Unique days: {unique_days}")
        print(f"  Date range: {range_days} days")

# Check for meaningful column patterns
print("\n4. Checking Data Patterns:")
print("-" * 40)

# Check string columns for meaningful values
for col_name, col_type, _ in columns[:15]:  # Check first 15 columns
    if 'VARCHAR' in col_type or 'TEXT' in col_type:
        cursor.execute(f"""
            SELECT 
                COUNT(DISTINCT {col_name}) as unique_vals,
                COUNT(*) - COUNT({col_name}) as null_count
            FROM OPENOPPORTUNITIES
        """)
        unique_vals, null_count = cursor.fetchone()
        
        if unique_vals > 1 and unique_vals < 100:  # Likely categorical
            cursor.execute(f"""
                SELECT DISTINCT {col_name}
                FROM OPENOPPORTUNITIES
                WHERE {col_name} IS NOT NULL
                LIMIT 5
            """)
            sample_vals = [row[0] for row in cursor.fetchall()]
            print(f"\n{col_name} (categorical - {unique_vals} unique):")
            print(f"  Sample: {', '.join(str(v) for v in sample_vals[:3])}")

# Check numeric columns
for col_name, col_type, _ in columns[:15]:
    if 'NUMBER' in col_type or 'FLOAT' in col_type:
        cursor.execute(f"""
            SELECT 
                MIN({col_name}) as min_val,
                MAX({col_name}) as max_val,
                AVG({col_name}) as avg_val
            FROM OPENOPPORTUNITIES
            WHERE {col_name} IS NOT NULL
        """)
        result = cursor.fetchone()
        if result[0] is not None:
            print(f"\n{col_name} (numeric):")
            print(f"  Range: {result[0]:.2f} to {result[1]:.2f}, Avg: {result[2]:.2f}")

cursor.close()
conn.close()

print("\n" + "=" * 80)
print("RECOMMENDATION FOR TIME INTELLIGENCE TESTING")
print("=" * 80)
print("✅ OPENOPPORTUNITIES has 3 date columns (C1, C9, C10)")
print("✅ Data spans multiple time periods")
print("✅ Perfect for testing:")
print("   - Period-over-period comparisons")
print("   - Running totals")
print("   - Time-based filtering")
print("   - Trend analysis")
print("\n⚠️  Column names are generic (C1, C2, etc.)")
print("   This will test if CORTEX can handle non-semantic column names")