# CRITICAL DISCOVERY: Snowflake's Pseudo-Stateful Architecture

## Executive Summary  
**UPDATE**: Snowflake Intelligence claims "stateful multi-turn conversations" but has a critical limitation - it cannot reference previous SQL results. It remembers what you asked but not what it showed you. This pseudo-statefulness breaks common user patterns like "tell me more about the third item".

## Evidence from Official Sources

### 1. Snowflake's Own Documentation States:
> "Large language models like the ones used by Cortex Analyst **do not store state between requests**. The full history is processed for each new query in a conversation, with corresponding compute cost that increases with each round."
- Source: Snowflake Documentation, Cortex Analyst User Guide

### 2. Critical Limitation - Cannot Access Previous Results:
> "Cortex Analyst doesn't have access to results from previous SQL queries. For example, if you first ask 'What are my products?' and then ask 'What is the revenue of the second product?', Cortex Analyst cannot refer to the list of products from the first query."
- Source: Official Cortex Analyst Documentation

**What Snowflake Claims as "Stateful":**
- Passes conversation history with each request
- Can understand context like "What about Europe?" after asking about Asia
- Maintains semantic understanding through conversation

**The Critical Gap:**
- Cannot reference actual data from previous results
- Each turn generates completely new SQL from scratch
- No access to previous result sets or visualizations

### 3. GitHub Implementation Analysis

#### From cortex_analyst_streaming_demo.py:
```python
def get_conversation_history() -> list[dict[str, Any]]:
    messages = []
    for msg in st.session_state.messages:
        # Simply converts messages to text
        text_content = "\n".join([c for c in msg["content"] if isinstance(c, str)])
        m["content"] = [{"type": "text", "text": text_content}]
        messages.append(m)
    return messages
```

**What's Missing:**
- No filter accumulation
- No visualization type preservation
- No semantic understanding of references
- No context beyond raw message history

#### From cortex_analyst_sis_demo_app.py:
```python
def get_analyst_response(messages: List[Dict]):
    # Just passes message history to API
    request_body = {
        "messages": messages,
        "semantic_model_file": semantic_model_file,
    }
    # Each call is independent
```

## Scoop's Stateful Architecture - The Fundamental Difference

### 1. Rich Context Management (ChatContext.java)
```java
public class ChatContext {
    public AIQuery currentQuery;                      // Active query object
    public ObjectNode currentVisualizationNode;       // Preserved visualization
    public List<String> prompts = new ArrayList<>();  // Full conversation
    public QueryFilter lastQueryFilter;               // Accumulating filters
    public FilterInvestigationResult lastInvestigationResult;
    public String sessionId = UUID.randomUUID();      // Persistent session
}
```

### 2. Contextual Understanding
```java
// Scoop understands "that" and "previous"
if (isRefinement) {
    // Preserve visualization type but allow data to change
    currentChatContext.lastVisualizationNode = currentChatContext.currentVisualizationNode;
}
```

### 3. Progressive Filter Building
```java
// Filters accumulate across conversation
if (currentChatContext.lastQueryFilter != null) {
    queryFilter = QueryFilter.combine(queryFilter, currentChatContext.lastQueryFilter);
}
```

## Business Impact Comparison

### Snowflake Intelligence Limitations (Pseudo-Stateful):
1. **Cannot reference specific results** - "Show details for row 3" fails
2. **Cannot build on actual data** - "Calculate variance of those values" fails  
3. **Must re-query for chart changes** - "Make that a pie chart" requires full re-execution
4. **No visualization state** - Cannot preserve axes, colors, or configuration
5. **Limited to 3 chart types** - Bar, line, pie only (vs Scoop's 15+)

### Scoop Capabilities (Stateful):
1. **"Show that by region"** ✓ Knows what "that" refers to
2. **"Drill into Q1"** ✓ Adds filter while preserving context
3. **"Compare to last year"** ✓ Maintains all previous filters
4. **"Switch to a line chart"** ✓ Changes visualization while keeping data/query
5. **"Now make it a bar chart"** ✓ Instant visualization change, no re-query
6. **Progressive complexity** ✓ Each query builds on previous

## Real User Session Example

### In Snowflake Intelligence (with basic charting):
```
User: "Show revenue by product"
Intelligence: [Returns bar chart with products]

User: "What's the revenue for the third product?"
Intelligence: ERROR - Cannot reference specific products from result

User: "Switch to a pie chart"
Intelligence: [Must completely re-query, cannot just change viz type]

User: "Drill into ProductC"
Intelligence: ERROR - Doesn't know what ProductC is from previous chart
```

### In Scoop:
```
User: "Show revenue by product"
Scoop: [Returns bar chart with all products]

User: "For the top 3"
Scoop: [Filters to top 3, keeps bar chart]

User: "Switch to a line chart"
Scoop: [Instantly changes to line chart, same data]

User: "Actually make it a pie chart"
Scoop: [Changes to pie chart, preserves top 3 filter]

User: "Add last year comparison"
Scoop: [Adds comparison, switches to grouped bar chart automatically]

User: "Back to a line chart"
Scoop: [Changes visualization, maintains all context and filters]
```

## Architectural Implications

### Cortex's Stateless REST API:
- Each request independent
- Full history resent every time
- Linear cost increase with conversation length
- No session management
- Client must manage all state

### Scoop's Stateful Architecture:
- Persistent ChatContext per session
- Efficient incremental processing
- True multi-turn conversations
- Server-side state management
- Rich context preservation

## The Verdict

This isn't just a feature difference - it's a **fundamental architectural limitation**. Cortex Analyst is essentially a stateless SQL generator that takes text input. Scoop is a stateful conversation platform that understands context, maintains session state, and enables progressive analysis building.

**For business users, this means:**
- Cortex: Start over with each question
- Scoop: Have a real conversation with your data

**This is not something Snowflake can easily fix** - it would require a complete architectural redesign to add proper state management, context preservation, and result accessibility.