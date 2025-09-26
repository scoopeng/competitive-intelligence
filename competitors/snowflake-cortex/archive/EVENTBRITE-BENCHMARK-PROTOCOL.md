# EventBrite Benchmark Protocol: Scoop vs Cortex Analyst

## How EventBrite Can Test TODAY

### Since EventBrite Has Enterprise Snowflake:

#### Step 1: Access Cortex Analyst (10 minutes)
1. Log into **Snowsight** (your Snowflake web UI)
2. Go to **Streamlit** section
3. Click **+ Streamlit App**
4. Use the Cortex Analyst template or quickstart

**OR**

Use the official quickstart:
https://quickstarts.snowflake.com/guide/getting_started_with_cortex_analyst/

#### Step 2: Prepare Test Data
Use your actual EventBrite data or the sample revenue data:
- Event attendance metrics
- Organizer behavior data  
- Revenue/ticketing data
- Churn/retention metrics

#### Step 3: Create/Use Semantic Model
This is where it gets complex - you need a YAML file defining your data:
```yaml
semantic_model:
  name: eventbrite_analytics
  tables:
    - name: events
      columns:
        - name: attendance
        - name: revenue
        - name: organizer_id
```

---

## The Benchmark Test Suite

### Test Category 1: Basic Queries (Both Should Pass)
1. "What was total revenue last month?"
2. "Show attendance by event type"
3. "List top 10 organizers by revenue"

**What to measure**:
- Response time
- Accuracy
- Ease of asking

### Test Category 2: Investigation Queries (Scoop Advantage)
1. **"Why did event attendance drop last quarter?"**
   - Cortex: Single query showing attendance numbers
   - Scoop: Multi-query investigation finding root causes

2. **"What factors predict organizer churn?"**
   - Cortex: Cannot do predictive analysis
   - Scoop: ML-based pattern discovery

3. **"Find the relationship between pricing and attendance"**
   - Cortex: Basic correlation if any
   - Scoop: Multi-dimensional analysis

### Test Category 3: Business User Tests (Critical)
Have a non-technical team member:
1. Upload a new spreadsheet
2. Ask a business question
3. Get actionable insights

**Measure**:
- Can they do it without IT?
- Time to first answer
- Quality of insights

### Test Category 4: Complex Multi-Step Analysis
**"Which combination of event features, timing, and pricing maximizes attendance?"**

This requires:
- Testing multiple variables
- Finding interactions
- Discovering patterns

**Expected**:
- Cortex: Cannot perform multi-step analysis
- Scoop: Tests combinations, finds optimal mix

---

## Scoring Framework

### Evaluate Each System On:

| Criterion | Weight | Cortex Analyst | Scoop |
|-----------|--------|---------------|-------|
| **Setup Time** | 20% | Hours/Days with semantic model | 30 seconds |
| **Investigation Depth** | 30% | Single queries only | 3-10 query analysis |
| **Business User Ready** | 25% | Needs IT for semantic model | Full self-service |
| **Answer Quality** | 15% | Surface metrics | Root cause analysis |
| **Integration** | 10% | Snowflake UI only | Excel, Slack, PowerPoint |

---

## The Killer Demonstration

### Test This Specific Scenario:
**"Our event attendance dropped 30% last month. Why?"**

#### Watch What Happens:

**Cortex Analyst** will likely:
1. Show you attendance numbers by category
2. Maybe break down by time period
3. Stop there

**Scoop** will:
1. Analyze attendance by multiple dimensions
2. Correlate with external factors
3. Identify specific segments affected
4. Find root causes
5. Suggest actions

**This single test reveals everything.**

---

## If Cortex Analyst Isn't Set Up Yet

### The Setup Process Itself is the Test:

**Track for Cortex Analyst**:
1. Time to create semantic model
2. Technical expertise required
3. Iterations needed to get it working
4. Limitations discovered

**Compare to Scoop**:
1. Connect to Snowflake: 10 seconds
2. Ask first question: 20 seconds
3. Get investigation: 30 seconds total

---

## Questions to Ask Snowflake

1. **"Can we test Cortex Analyst with our data right now?"**
   - If no: Why not?
   - If yes: How long to set up?

2. **"Can it investigate why metrics change?"**
   - Ask for demonstration
   - Count number of queries executed

3. **"Can business users work independently?"**
   - Who creates semantic models?
   - What happens when schema changes?

4. **"Show us multi-step reasoning"**
   - Not just SQL generation
   - Actual investigation

---

## Documentation Template

### For Each Test Query, Document:

**Query**: [The question asked]

**Cortex Analyst**:
- Setup required: [semantic model, etc.]
- Response time: [seconds]
- Query count: [usually 1]
- Answer depth: [surface/deep]
- Business readiness: [IT required?]

**Scoop**:
- Setup required: [none]
- Response time: [seconds]
- Query count: [3-10 for investigation]
- Answer depth: [root cause]
- Business readiness: [immediate]

---

## The Decision Matrix

### Cortex Analyst Makes Sense If:
- ❌ You only need basic metrics (use regular BI)
- ❌ IT will manage everything (defeats purpose)
- ❌ Investigation isn't important (why use AI?)
- ❌ You're locked into Snowflake (still limited)

### Scoop Makes Sense If:
- ✅ You need to know WHY things happen
- ✅ Business users need independence
- ✅ You want insights in your workflow
- ✅ You value investigation over dashboards

---

## Next Steps for EventBrite

1. **Today**: Try the Streamlit Cortex Analyst demo
2. **Document**: Setup complexity and limitations
3. **Test**: The investigation scenarios above
4. **Compare**: Time, depth, and independence
5. **Decide**: Based on actual capabilities, not promises

---

*Remember: The question isn't "Can we add Cortex Analyst?" but "Can Cortex Analyst actually investigate problems?" Our testing says no.*