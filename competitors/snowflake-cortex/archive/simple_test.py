#!/usr/bin/env python3
import snowflake.connector

# Simple connection test
print("Enter your Snowflake URL (copy from browser):")
print("Example: https://app.snowflake.com/us-west-2/nfb33705/...")
url = input("URL: ").strip()

# Parse the URL to get account
if "app.snowflake.com" in url:
    # Format: https://app.snowflake.com/region/account/...
    parts = url.split("/")
    region = parts[3]
    account = parts[4].upper()
    account_id = f"{account}.{region}"
else:
    # Format: https://account.region.snowflakecomputing.com/...
    parts = url.split("//")[1].split(".")[0]
    account_id = parts

print(f"\nTrying account: {account_id}")

try:
    conn = snowflake.connector.connect(
        account=account_id,
        user='bradscoop',
        password='D6c2BmtJWPy3dM7'
    )
    print("✅ Connected!")
    
    cursor = conn.cursor()
    cursor.execute("SELECT CURRENT_ACCOUNT(), CURRENT_REGION(), CURRENT_DATABASE()")
    result = cursor.fetchone()
    print(f"Account: {result[0]}")
    print(f"Region: {result[1]}")
    print(f"Database: {result[2]}")
    
    conn.close()
    
    print(f"\n✅ Use this in test_cortex_analyst.py: '{account_id}'")
    
except Exception as e:
    print(f"❌ Failed: {e}")