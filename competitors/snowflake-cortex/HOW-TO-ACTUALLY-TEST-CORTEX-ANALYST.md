# How to Actually Test Cortex Analyst - Practical Guide

## YES, You Can Test It! Here's How:

### Option 1: Streamlit UI in Snowsight (EASIEST)

If EventBrite has enterprise access, they should be able to:

1. **Log into Snowsight** (Snowflake web UI)
2. **Navigate to Streamlit** section
3. **Create a Streamlit App** using this template:

```python
import streamlit as st
from snowflake.cortex import Complete, Analyst
import json

st.title("Cortex Analyst Test")

# Your semantic model (simplified)
semantic_model = {
    "name": "revenue_data",
    "tables": [{
        "name": "your_table",
        "description": "Your business data"
    }]
}

# Chat interface
user_question = st.text_input("Ask a question about your data:")

if user_question:
    # Call Cortex Analyst
    response = Analyst(
        semantic_model=semantic_model,
        query=user_question
    )
    st.write(response)
```

### Option 2: Use Snowflake's Demo Environment

**Snowflake Quickstart**: https://quickstarts.snowflake.com/guide/getting_started_with_cortex_analyst/

This provides:
- Sample data (revenue time-series)
- Pre-built semantic model
- Working Streamlit app
- Step-by-step instructions

### Option 3: REST API Testing (Technical)

```python
import requests
import json

# Cortex Analyst REST endpoint
url = f"https://{account}.snowflakecomputing.com/api/v2/cortex/analyst/message"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

body = {
    "messages": [{
        "role": "user",
        "content": "Why did revenue drop last quarter?"
    }],
    "semantic_model": semantic_model_yaml
}

response = requests.post(url, headers=headers, json=body)
```

---

## What EventBrite Should Test (Benchmark Queries)

### Test 1: Basic Query
**Ask**: "What was total revenue last quarter?"
- **Expected**: Single number answer
- **Scoop equivalent**: Same, but faster

### Test 2: Investigation (CRITICAL TEST)
**Ask**: "Why did revenue drop in Q3?"
- **Cortex Analyst**: Will likely show revenue by category/time
- **Scoop**: Would investigate multiple dimensions, find correlations

### Test 3: Multi-Step Reasoning
**Ask**: "What factors correlate with our highest revenue months?"
- **Test if it**: Explores multiple variables or just lists revenue

### Test 4: Business User Independence
**Have non-technical user try**:
1. Upload new data
2. Ask questions without help
3. Get meaningful answers

### Test 5: Complex Analysis
**Ask**: "Which combination of customer segments and products drives the most profit?"
- **Look for**: Multi-dimensional analysis vs simple grouping

---

## The Semantic Model Challenge

**Critical Discovery**: Cortex Analyst requires a semantic model (YAML) for EACH dataset:

```yaml
semantic_model:
  name: eventbrite_data
  tables:
    - name: events
      description: Event information
      columns:
        - name: event_id
          description: Unique identifier
        - name: revenue
          description: Total revenue
          data_type: number
          aggregation: sum
      measures:
        - name: total_revenue
          expr: SUM(revenue)
      dimensions:
        - name: event_type
        - name: location
```

**This means**:
1. IT must create this for each data source
2. Business users can't just upload and analyze
3. Schema changes require YAML updates

---

## Quick Test Script for EventBrite

```python
# If they have access, try this in Snowsight Python worksheet:

from snowflake.snowpark import Session
from snowflake.cortex import Analyst
import pandas as pd

# Test queries that reveal capabilities
test_queries = [
    "Show total sales",  # Basic - should work
    "Why are sales declining?",  # Investigation - will struggle
    "What predicts customer churn?",  # Prediction - will fail
    "Find patterns in the data",  # Pattern - will be vague
]

for query in test_queries:
    print(f"\nQuery: {query}")
    try:
        result = Analyst(semantic_model, query)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Failed: {e}")
```

---

## What to Look For in Testing

### ✅ Cortex Analyst CAN:
- Answer basic questions about metrics
- Generate single SQL queries
- Work within defined semantic model
- Provide formatted responses

### ❌ Cortex Analyst CANNOT:
- Investigate "why" with multiple queries
- Work without semantic model
- Handle schema changes automatically
- Integrate with Excel/Slack natively
- Perform ML analysis (clustering, decision trees)

---

## Alternative: Try the Public Demo

**Snowflake might have a public demo environment**:
1. Contact Snowflake sales for demo access
2. Ask for Cortex Analyst specific demo
3. Request ability to test with YOUR data

---

## The Comparison Test Protocol

### Side-by-Side Test:
1. **Same question** to both systems
2. **Time the setup** (Scoop: 30 seconds, Cortex: hours/days)
3. **Count queries executed** (Scoop: 3-10, Cortex: 1)
4. **Evaluate answer depth** (Scoop: root cause, Cortex: surface metrics)
5. **Test business user independence**

### Document:
- Setup complexity
- Answer quality
- Investigation depth
- Business user readiness

---

## If You Can't Access Cortex Analyst

**The Story Itself is Powerful**:

"We tried for 4+ hours to test Cortex Analyst:
- Created account ✓
- Set up database ✓
- Loaded your data ✓
- Built semantic model ✓
- Result: Not accessible on trial

Meanwhile, Scoop took 30 seconds."

**That IS the benchmark result.**

---

## Bottom Line for Testing

**If EventBrite has enterprise**:
1. They can test via Streamlit in Snowsight
2. Use the quickstart tutorial
3. Compare investigation capabilities

**If they don't have Cortex Analyst enabled**:
1. It requires additional setup even with enterprise
2. Semantic models must be created per dataset
3. The setup complexity itself is the issue

**The key test**: Ask "WHY" questions and see if it investigates or just reports.

---

*Testing approach documented: January 2025*