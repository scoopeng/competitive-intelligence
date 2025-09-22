# Snowflake Cortex Analyst Testing: Project Summary

## Executive Summary
Testing of Snowflake's Cortex Analyst reveals that only 57% of queries produce business-usable answers. The failures are due to fundamental architectural limitations, not SQL generation issues.

**CRITICAL DISCOVERY**: Cortex Analyst is fundamentally stateless - confirmed by Snowflake's own documentation. It cannot reference previous results or maintain context between queries. This is an architectural limitation, not a feature gap.

## Key Findings

### 1. Stateless Architecture (Game-Changing Discovery)
- **Evidence**: Snowflake docs state "Cortex Analyst doesn't have access to results from previous SQL queries"
- **Impact**: Cannot say "drill into that" or "show the previous result by region"
- **Business Impact**: Users must formulate complete, standalone questions every time
- **Details**: See [STATEFUL_VS_STATELESS_CRITICAL_COMPARISON.md](./STATEFUL_VS_STATELESS_CRITICAL_COMPARISON.md)

### 2. The 92.9% Success Rate is Misleading
- **SQL Generation**: 26/28 queries generated valid SQL
- **Business Usability**: Only 57% produced actionable answers
- **Context Stripping**: 25% return results without needed values
- **Example**: "Show contracts where churn > 30%" returns "Month-to-month" without the 60% rate

### 3. Time Intelligence Failures (67% Failure Rate)
- "Month-over-month change" → SQL execution error
- "3-month moving average" → Nonsensical per-row calculations
- Root cause: Complex DATE_TRUNC arithmetic that fails without proper date columns

### 4. No Multi-Step Reasoning
- "Why are customers churning?" → Attempted 3 queries, Snowflake rejected
- Cannot perform investigative analysis
- Limited to single SQL queries

### 5. Limited Visualization Capabilities
- **Cortex Analyst**: SQL results only, no visualizations
- **Snowflake Intelligence (Preview)**: Only 3 basic chart types (bar, line, pie)
- **Critical**: Cannot switch chart types without re-querying (no state preservation)
- Cannot say "make that a bar chart" - must start over with new query
- No advanced visualizations (heatmaps, scatter plots, treemaps, etc.)

### 6. No Conversation Context
- Each query independent
- Cannot accumulate filters progressively
- Must repeat all context in every query

## Scoop's Fundamental Advantages

### Stateful Architecture (ChatContext.java)
```java
public class ChatContext {
    public AIQuery currentQuery;
    public ObjectNode currentVisualizationNode;  // FULL visualization state
    public List<String> prompts;  // Full conversation
    public QueryFilter lastQueryFilter;  // Accumulating filters
    public String sessionId;  // Persistent session
}
```

**Critical**: The `currentVisualizationNode` maintains complete chart configuration - type, axes, colors, everything. Users can freely switch between 15+ chart types without re-querying. Snowflake Intelligence cannot do this even with its 3 basic chart types.

### What This Enables
1. **"Show that by region"** - Knows what "that" refers to
2. **"Drill into Q1"** - Adds filter while preserving context
3. **"Switch to a line chart"** - Instant visualization change, no re-query
4. **"Now make it a pie chart"** - Changes chart type, preserves all data and filters
5. **"Compare to last year"** - Maintains all previous context
6. **Progressive complexity** - Each query builds on previous

### Multi-Channel Rich Experience
- **WebSocket**: Real-time progress updates, rich visualizations
- **Slack**: Native blocks, interactive elements, deck sharing
- **API**: Full programmatic access with state management

## Strategic Implications

### For Sales
**Lead with the stateless limitation** - This is not something Snowflake can patch or update. It requires fundamental architectural redesign. Every business user understands the frustration of having to repeat themselves.

### Positioning Statement
"While Cortex generates SQL from text, Scoop enables actual conversations with your data. Cortex can't even reference its previous answer - imagine asking 'What are my top products?' then 'Show revenue for the second one' and being told it doesn't know what products it just showed you. That's Cortex today."

### Competitive Advantages That Cannot Be Matched
1. **Stateful conversations** - Architectural advantage
2. **Multi-probe reasoning** - Requires investigation engine
3. **SCOOP_DKEY temporal system** - Native multi-date perspectives
4. **Progressive filter building** - Needs context preservation
5. **Intelligent visualization with instant switching** - 15+ chart types vs 3 basic types

## Test Methodology
- **Test Suite**: [DEFINITIVE_TEST_SUITE.py](./DEFINITIVE_TEST_SUITE.py) - 28 queries
- **Datasets**: TELCO_DATA (7,043 rows), OPENOPPORTUNITIES (50,000 rows)
- **Model**: Claude-4-Sonnet (Anthropic's latest)
- **Categories**: Subqueries, formulas, window functions, ML queries
- **Results**: [test_results/](./test_results/) directory

## Documentation Structure
- **[INDEX.md](./INDEX.md)** - Complete navigation and overview
- **[CONSOLIDATED_TECHNICAL_ANALYSIS.md](./CONSOLIDATED_TECHNICAL_ANALYSIS.md)** - Full technical deep dive
- **[STATEFUL_VS_STATELESS_CRITICAL_COMPARISON.md](./STATEFUL_VS_STATELESS_CRITICAL_COMPARISON.md)** - The killer differentiator
- **[MASTER_ANALYSIS_PLAN.md](./MASTER_ANALYSIS_PLAN.md)** - Systematic analysis methodology

## Bottom Line
Cortex Analyst is a stateless SQL generator. Scoop is a stateful conversation platform. This fundamental difference cannot be overcome without Snowflake completely redesigning their product.

For enterprise users who need to explore data through natural conversation, the choice is clear.