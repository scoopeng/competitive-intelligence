#!/usr/bin/env python3
"""
Test Snowflake connection formats
"""

import snowflake.connector

# Try different account formats
account_formats = [
    'nfb33705.toajlpe',
    'NFB33705.toajlpe',
    'toajlpe.nfb33705',
    'toajlpe.NFB33705',
    'nfb33705',
    'NFB33705',
    'toajlpe-nfb33705',
    'TOAJLPE-NFB33705',
]

user = 'bradscoop'
password = 'D6c2BmtJWPy3dM7'

print("Testing Snowflake connection formats...")
print("="*50)

for account in account_formats:
    print(f"\nTrying: {account}")
    try:
        conn = snowflake.connector.connect(
            account=account,
            user=user,
            password=password,
            login_timeout=5
        )
        print(f"✅ SUCCESS with format: {account}")
        
        # Test query
        cursor = conn.cursor()
        cursor.execute("SELECT CURRENT_ACCOUNT(), CURRENT_REGION()")
        result = cursor.fetchone()
        print(f"   Account: {result[0]}, Region: {result[1]}")
        conn.close()
        break
    except Exception as e:
        print(f"❌ Failed: {str(e)[:100]}")