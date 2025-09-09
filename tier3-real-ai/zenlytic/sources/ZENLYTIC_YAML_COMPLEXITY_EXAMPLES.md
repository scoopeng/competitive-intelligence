# Zenlytic YAML Configuration Complexity Examples
## Real-World Examples Showing Why Business Users Can't Use This

**Document Purpose**: Demonstrate the actual complexity of Zenlytic's YAML requirements
**Key Finding**: These configurations require SQL, programming concepts, and technical expertise

---

## Example 1: Basic Customer View (What Zenlytic Calls "Simple")

```yaml
# views/customers.yml
version: 1
type: view
name: customers
model_name: production_db
sql_table_name: analytics.dim_customers
label: "Customer Data"
description: "Customer profile and demographic information"

# Even basic fields require technical knowledge
fields:
  - dimension: customer_id
    type: string
    primary_key: yes
    sql: ${TABLE}.customer_unique_id
    description: "Unique identifier for each customer"
    
  - dimension: created_date
    type: time
    timeframes: [raw, date, week, month, quarter, year]
    sql: ${TABLE}.registration_timestamp
    convert_tz: yes
    
  - dimension: customer_segment
    type: string
    sql: |
      CASE 
        WHEN ${lifetime_value} > 1000 THEN 'High Value'
        WHEN ${lifetime_value} > 500 THEN 'Medium Value'
        ELSE 'Low Value'
      END
    
  - measure: count
    type: count
    drill_fields: [customer_id, created_date, city, state]
    
  - measure: lifetime_value
    type: sum
    sql: ${TABLE}.ltv_calculated
    value_format_name: usd
    description: "Total customer lifetime value"
```

**Business User Barriers:**
- Must understand SQL CASE statements
- Need to know database schema
- Requires understanding of data types
- Must manage drill field relationships

---

## Example 2: Order Analysis View with Derived Table

```yaml
# views/order_analysis.yml
type: view
name: order_analysis
model_name: production_db

# This is where it gets complex - derived tables require SQL
derived_table:
  sql: |
    WITH order_metrics AS (
      SELECT 
        o.order_id,
        o.customer_id,
        o.order_date,
        o.total_amount,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY o.order_date) as order_number,
        DATEDIFF('day', LAG(o.order_date) OVER (PARTITION BY o.customer_id ORDER BY o.order_date), o.order_date) as days_since_last_order,
        COUNT(*) OVER (PARTITION BY o.customer_id) as total_customer_orders,
        SUM(o.total_amount) OVER (PARTITION BY o.customer_id) as customer_total_spent
      FROM orders o
      WHERE o.status = 'completed'
    ),
    customer_segments AS (
      SELECT
        customer_id,
        CASE 
          WHEN total_customer_orders = 1 THEN 'New'
          WHEN total_customer_orders BETWEEN 2 AND 5 THEN 'Active'
          ELSE 'Loyal'
        END as customer_type
      FROM order_metrics
      GROUP BY customer_id, total_customer_orders
    )
    SELECT 
      om.*,
      cs.customer_type,
      c.email,
      c.acquisition_channel
    FROM order_metrics om
    JOIN customer_segments cs ON om.customer_id = cs.customer_id
    JOIN customers c ON om.customer_id = c.id
  
  # Materialization settings - more complexity
  datagroup_trigger: orders_datagroup
  indexes: [customer_id, order_date]
  partition_keys: [order_date]
  cluster_keys: [customer_id]

fields:
  - dimension: order_id
    primary_key: yes
    
  - dimension: customer_type
    type: string
    description: "New, Active, or Loyal based on order count"
    
  - dimension: days_since_last_order
    type: number
    description: "Days between orders for repeat customers"
    
  - measure: avg_days_between_orders
    type: average
    sql: ${days_since_last_order}
    filters:
      order_number: ">1"
      
  - measure: repeat_rate
    type: number
    sql: |
      COUNT(DISTINCT CASE WHEN ${order_number} > 1 THEN ${customer_id} END) * 1.0 / 
      NULLIF(COUNT(DISTINCT ${customer_id}), 0)
    value_format_name: percent_2
```

**Why Business Users Can't Handle This:**
- Complex SQL with CTEs (Common Table Expressions)
- Window functions (ROW_NUMBER, LAG, etc.)
- Multiple joins
- Partitioning and clustering concepts
- Performance optimization settings

---

## Example 3: Revenue Metrics with Time-Based Calculations

```yaml
# views/revenue_metrics.yml
type: view
name: revenue_metrics
model_name: production_db
sql_table_name: analytics.fact_revenue

fields:
  # Complex time-based comparisons
  - measure: revenue_current_period
    type: sum
    sql: ${TABLE}.revenue
    
  - measure: revenue_previous_period
    type: sum
    sql: ${TABLE}.revenue
    filters:
      created_date: "last period"
      
  - measure: revenue_growth
    type: number
    sql: |
      (${revenue_current_period} - ${revenue_previous_period}) / 
      NULLIF(${revenue_previous_period}, 0)
    value_format_name: percent_2
    
  - measure: revenue_running_total
    type: running_total
    sql: ${revenue_current_period}
    direction: "column"
    
  # Cohort analysis - requires advanced SQL
  - measure: cohort_retention_rate
    type: number
    sql: |
      COUNT(DISTINCT CASE 
        WHEN DATEDIFF('month', ${customers.created_date}, ${created_date}) = {% parameter cohort_month %}
        THEN ${customer_id} 
      END) * 1.0 /
      NULLIF(COUNT(DISTINCT CASE 
        WHEN DATEDIFF('month', ${customers.created_date}, ${created_date}) = 0
        THEN ${customer_id} 
      END), 0)
    
  - parameter: cohort_month
    type: number
    allowed_value: {label: "Month 1" value: "1"}
    allowed_value: {label: "Month 2" value: "2"}
    allowed_value: {label: "Month 3" value: "3"}
```

---

## Example 4: Access Control and Security

```yaml
# views/sensitive_data.yml
type: view
name: sensitive_data
model_name: production_db
sql_table_name: analytics.user_pii

# Access control requires understanding of security concepts
required_access_grants: [executive_team, data_team]

access_filters:
  - field: region
    user_attribute: user_region
  - field: department
    user_attribute: user_department

fields:
  - dimension: email
    type: string
    sql: |
      CASE 
        WHEN '{{ _user_attributes["can_see_pii"] }}' = 'yes' 
        THEN ${TABLE}.email
        ELSE 'REDACTED'
      END
      
  - dimension: ssn
    type: string
    sql: |
      CASE 
        WHEN '{{ _user_attributes["security_level"] }}' >= '5'
        THEN ${TABLE}.ssn_encrypted
        ELSE 'HIDDEN'
      END
    tags: ["pii", "sensitive"]
```

---

## Example 5: Multi-Table Joins Configuration

```yaml
# models/ecommerce_model.yml
version: 1
type: model
name: ecommerce_model
connection: warehouse_prod

# Join configuration requires understanding of database relationships
joins:
  - name: orders_to_customers
    relationship: many_to_one
    sql_on: ${orders.customer_id} = ${customers.customer_id}
    
  - name: orders_to_products
    relationship: many_to_many
    sql_on: ${order_items.order_id} = ${orders.order_id}
    fields: [order_items.product_id]
    
  - name: products_to_categories
    relationship: many_to_one
    sql_on: |
      ${products.category_id} = ${categories.category_id}
      AND ${products.is_active} = TRUE
    type: left_outer
    
# Fan-out join handling - advanced concept
allow_fanouts: [orders, order_items]

# Performance optimization
aggregate_awareness:
  - name: daily_summary
    dimensions: [created_date, product_category]
    measures: [total_revenue, order_count]
    time_dimension: created_date
    granularity: day
```

---

## Example 6: The "Simple" Customer Count Query

Here's what Zenlytic requires just to enable "How many customers do we have?"

```yaml
# First, create the model connection
# models/main_model.yml
version: 1
type: model
name: main_model
connection: production_warehouse
timezone: UTC

---

# Then create the customer view
# views/dim_customers.yml
type: view
name: dim_customers
model_name: main_model
sql_table_name: analytics.dim_customers
label: "Customers"

fields:
  - dimension: customer_id
    type: string
    primary_key: yes
    hidden: no
    sql: ${TABLE}.customer_id
    
  - dimension: is_active
    type: yesno
    sql: ${TABLE}.status = 'active'
    
  - measure: customer_count
    label: "Total Customers"
    type: count_distinct
    sql: ${customer_id}
    description: "Use for 'how many customers' questions"
    zoe_description: "Total number of unique customers. Use this when users ask about customer count, number of customers, or how many customers."
    drill_fields: [customer_id, created_date, customer_name]
    
  - measure: active_customer_count
    label: "Active Customers"
    type: count_distinct
    sql: ${customer_id}
    filters:
      is_active: "yes"
```

**Just for a Simple Count:**
- Need to set up model
- Configure connection
- Create view
- Define primary key
- Create measure
- Add descriptions for AI
- Configure drill fields

---

## The Reality Check

### What Marketing Says:
"No technical knowledge required"

### What You Actually Need to Know:
1. **SQL Expertise**
   - JOINs (inner, left outer, many-to-many)
   - Window functions
   - CTEs (Common Table Expressions)
   - CASE statements
   - Aggregate functions

2. **Programming Concepts**
   - YAML syntax and indentation
   - Variable substitution (${TABLE})
   - Templating syntax
   - Conditional logic
   - Parameter handling

3. **Database Knowledge**
   - Schema structure
   - Table relationships
   - Primary/foreign keys
   - Indexes and partitions
   - Performance optimization

4. **Version Control**
   - Git commands
   - Branch management
   - Merge conflicts
   - Deploy keys

5. **Security & Governance**
   - Access grants
   - Row-level security
   - User attributes
   - PII handling

---

## Business User Attempting This

### Scenario: Marketing Manager Wants to Add "Customer Acquisition Cost"

**What They'd Need to Do:**

1. Clone the Git repository
2. Create a new branch
3. Find the right YAML file
4. Write SQL calculation:
```yaml
- measure: customer_acquisition_cost
    type: number
    sql: |
      SUM(${marketing_spend.amount}) / 
      NULLIF(COUNT(DISTINCT ${customer_id}), 0)
    value_format_name: usd
```
5. Handle the inevitable errors
6. Commit and push changes
7. Create pull request
8. Deploy to production

**Reality**: They'll email the data team instead.

---

## Conclusion

These examples clearly demonstrate that Zenlytic's YAML configuration is not accessible to business users. Despite marketing claims of "no SQL required" and "self-serve analytics," the reality is that every aspect of the system requires technical expertise that business users don't have and shouldn't need.