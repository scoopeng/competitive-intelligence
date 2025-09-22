# Cortex Analyst vs Snowflake Intelligence: Understanding the Distinction

## Executive Summary
Snowflake has two distinct offerings that are often confused. Understanding the difference is critical for competitive positioning.

## The Two Products

### Cortex Analyst (Generally Available)
- **What it is**: SQL generation engine
- **Input**: Natural language questions + semantic model
- **Output**: SQL queries and tabular results
- **Visualizations**: NONE
- **State Management**: NONE (completely stateless)
- **Availability**: Generally available

### Snowflake Intelligence (Preview - Aug 2025)
- **What it is**: UI wrapper around Cortex Analyst with basic charting
- **Input**: Natural language questions
- **Output**: SQL results + basic charts (bar, line, pie)
- **Visualizations**: 3 basic chart types only
- **State Management**: NONE (still stateless)
- **Availability**: Preview only

## Critical Limitations That Persist

### 1. Both Are Fundamentally Stateless
Even with Intelligence's UI:
- Cannot reference previous results ("drill into that")
- Cannot accumulate filters progressively
- Each query starts completely fresh
- No conversation context preserved

### 2. No Visualization State Management
Intelligence can create charts but:
- Cannot switch chart type without re-querying
- "Make that a bar chart" → Must start over
- No preservation of axes, colors, or configuration
- Compare to Scoop: Instant switching between 15+ chart types

### 3. Limited Chart Types
Intelligence offers only:
- Bar chart
- Line chart  
- Pie chart

Missing advanced visualizations:
- Heatmaps
- Scatter plots
- Treemaps
- Box plots
- Sankey diagrams
- Geographic maps
- And 10+ more in Scoop

## Competitive Positioning

### Don't Say
"Cortex has no visualizations" - Intelligence preview does have basic charts

### Do Say
"Even Snowflake Intelligence can't switch between its 3 chart types without re-querying. Scoop instantly switches between 15+ visualization types because we maintain complete state."

### The Killer Demo
1. In Snowflake Intelligence: "Show sales by region" → Get bar chart
2. "Switch to pie chart" → ERROR or complete re-query
3. In Scoop: Same query → Instant switch to any of 15+ chart types
4. "Now show that as a heatmap" → Instant transformation

## Architecture Comparison

### Snowflake Architecture
```
User Query → Cortex Analyst → SQL → Results
                ↓
    Intelligence adds basic charting
         (still stateless)
```

### Scoop Architecture  
```
User Query → ChatContext (maintains state) → Query JSON → Multi-stage execution
                ↓                               ↓
    Preserved visualization config        Progressive filtering
    (instant chart switching)           (conversation building)
```

## Business Impact

### For Business Users
- **Snowflake**: Must formulate complete questions every time
- **Scoop**: Natural conversation that builds understanding

### For Analysts
- **Snowflake**: Basic charts, no advanced analytics
- **Scoop**: ML insights, statistical analysis, predictive modeling

### For Enterprises
- **Snowflake**: Requires semantic model maintenance
- **Scoop**: Self-learning system with automatic optimization

## The Bottom Line

Snowflake Intelligence adds basic charting to Cortex Analyst but doesn't address the fundamental architectural limitations:
1. Still stateless (no conversation context)
2. No visualization state management
3. Limited to 3 basic chart types
4. No ML or advanced analytics

Scoop's stateful architecture with complete visualization preservation represents a generational leap beyond what Snowflake offers, even in their preview Intelligence product.