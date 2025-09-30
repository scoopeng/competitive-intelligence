# Understanding Dimension - Revised Rubric
**Date**: September 30, 2025
**Status**: DRAFT - Awaiting Approval

## Core Concept

**Understanding removes dependency on data analysts** by enabling business users to deeply understand WHY things happen, not just WHAT happened.

**Key insight**: "Understanding" means using deep ML to understand relationships and root causes - it's deeper than just poking at a problem. This includes broader agentic investigation with the ability to plan new rounds of probes (queries or ML).

## What This Dimension Measures

Can business users get deep insights (root cause WHY) without needing a data analyst to investigate for them?

**This requires:**
1. **Agentic Investigation** - System autonomously investigates through multiple rounds
2. **Deep ML Understanding** - Explainable models that reveal relationships (not just predictions)
3. **Business-Language Translation** - Complex findings explained clearly

## Revised Scoring Rubric (20 points total)

### Component A: Agentic Investigation Depth (0-8 points)

**What this measures**: Does the system autonomously investigate root causes through multiple rounds of interconnected analysis?

#### 0 points - Static Dashboards
- Shows WHAT happened only
- No investigation capability
- View-only access to pre-built reports
- **Example**: Traditional static BI dashboards

#### 2 points - Single Query Response
- Answers one question at a time
- Basic drill-downs within dashboards
- No follow-up capability
- User sees problem but cannot investigate further
- **Example**: Power BI Copilot ("one question at a time" - Microsoft docs)

#### 4 points - User-Guided Multi-Query
- User CAN ask follow-up questions
- BUT user must know what to ask next
- No automatic hypothesis testing
- System doesn't plan investigation - user drives it
- **Example**: Manual exploration in most BI tools
- **Example**: Qlik associative model (user clicks relationships)

#### 6 points - Semi-Autonomous Investigation
- System suggests next questions
- User must approve/select each step
- Some context retention between queries
- Investigation requires user guidance throughout
- **Example**: AI assistants that suggest follow-ups but wait for approval

#### 8 points - Fully Autonomous Agentic Investigation ✅
- **Automatic multi-round investigation** (2-8+ interconnected probes)
- **Investigation planning** - System generates investigation strategy
- **Probe dependencies** - Later probes use results from earlier ones
  - Example: Probe 1 finds "highest churn in month-to-month contracts"
  - Probe 2 automatically analyzes month-to-month segment deeper
  - Probe 3 compares to other contract types using values from Probe 1
- **Multiple probe types** - Can plan mix of DATASET queries, ML_RELATIONSHIP, ML_GROUP, ML_PERIOD
- **Investigation strategies** - Implements drill-down, causal, temporal, comparative patterns
- **Hypothesis testing** - Tests theories automatically without user prompting
- **Statistical validation** - Confidence intervals, significance testing
- **Synthesis** - Combines findings from all probes into coherent narrative
- **Example**: Scoop's ReasoningEngine with multi-round probe planning

**Key distinction for 8 points**:
- System must **plan ahead** (not just react to user)
- System must **extract values from probe N to inform probe N+1** (probe dependencies)
- System must **decide which probe type** (query vs ML) based on investigation needs
- System must **run multiple rounds** if first round doesn't answer fully

### Component B: Deep ML Understanding (0-6 points)

**What this measures**: Can the system discover patterns and relationships using ML, and explain WHY patterns exist (not just predict)?

#### 0 points - No ML Capabilities
- Manual analysis only
- No pattern discovery
- No predictive capabilities
- **Example**: Basic BI tools, Power BI Copilot

#### 2 points - Basic Statistics as "AI"
- Correlations, trend lines
- Standard deviation, averages
- No real ML models
- Marketing calls it "AI" but it's just descriptive stats
- **Example**: Most tools claiming "AI-powered insights"

#### 4 points - Black-Box Predictive ML
- Real ML models (neural nets, ensemble methods)
- Makes predictions
- BUT cannot explain WHY
- Users see "Customer X likely to churn" but not why
- No decision tree visibility
- No business rules extraction
- **Example**: ThoughtSpot SpotIQ (33.3% accuracy, black-box predictions)

#### 6 points - Explainable ML with Deep Understanding ✅
- **Real ML models** with explainability:
  - **Decision Trees** (J48 with 800+ nodes showing decision paths)
  - **Rule Mining** (JRip rules extracted as business logic)
  - **Clustering** (EM clustering with segment definitions)
- **Pattern discovery** - Finds hidden segments, drivers, relationships
- **Causal understanding** - Shows WHAT drives WHAT (not just correlation)
- **Business rules extraction** - "If X and Y, then Z with 85% confidence"
- **Accessible to business users** - Automatic execution, no data scientist required
- **Multiple ML types available**:
  - ML_RELATIONSHIP - What predicts/influences outcome
  - ML_CLUSTER - Natural groupings in data
  - ML_PERIOD - What changed between time periods (using ML comparison)
  - ML_GROUP - How groups differ (using ML to explain differences)
- **Example**: Scoop's Three-Layer AI with J48 decision trees, EM clustering, JRip rules

**Key distinction for 6 points**:
- Must explain WHY (decision paths, rules, segment definitions)
- Must be accessible (automatic, not requiring data scientist)
- Must use real ML algorithms (not just regression or correlation)
- Must extract business-understandable rules

### Component C: Business-Language Explanation (0-6 points)

**What this measures**: Can users understand complex findings and explain them to executives?

#### 0 points - Raw Technical Output
- SQL results, data dumps
- Technical jargon
- Statistical notation
- No narrative or context
- **Example**: Direct database query results

#### 2 points - Basic Summaries with Jargon
- Some narrative text
- BUT still uses statistical terms
- "p-value of 0.03", "R-squared", "standard deviations"
- Requires technical knowledge to interpret
- **Example**: Most analytics tools with "insights" features

#### 4 points - Good Explanations, Some Technical Knowledge Helpful
- Mostly business language
- Some metrics explained
- Generally accessible
- May still reference technical concepts
- User can understand but may struggle to explain to boss
- **Example**: Better BI tools with narrative features

#### 6 points - Complete Business-Language Translation ✅
- **Zero technical jargon** - Pure business language
- **Narratives with context** - Tells a story, not just numbers
- **Actionable recommendations** - Suggests what to do, with reasoning
- **Confidence explained** - "We know this because..." (not just "we found this")
- **Executive-ready** - User can present findings to C-level without help
- **Synthesizes across findings** - Combines multiple probe results into coherent story
- **Example**: Scoop's narrative generation from ML results
  - Translates "J48 tree node: if tenure < 12 AND contract = month-to-month then churn"
  - Into: "New customers on flexible contracts are at highest risk - they haven't invested enough time to commit long-term"

**Key distinction for 6 points**:
- Boss test: Can user explain to their boss without any technical help?
- Context test: Does it explain WHY this matters, not just WHAT was found?
- Action test: Does it suggest what to DO about findings?

## Scoring Examples with New Rubric

### Scoop: 18/20
- **Investigation (8/8)**: Full agentic investigation
  - Multi-round probe planning with dependencies
  - Mix of DATASET, ML_RELATIONSHIP, ML_GROUP queries
  - Automatic hypothesis testing and synthesis
- **ML Understanding (6/6)**: Explainable ML
  - J48 decision trees (800+ nodes)
  - EM clustering with segment definitions
  - JRip business rules extraction
- **Business Explanation (4/6)**: Good narratives
  - Translates ML to business language
  - Provides context and recommendations
  - Room for improvement on actionability specificity

### Power BI Copilot: 4/20 (UNCHANGED - was correct)
- **Investigation (2/8)**: Single query only
  - "One question at a time" per Microsoft docs
  - No follow-up capability
  - No investigation planning
- **ML Understanding (0/6)**: No ML
  - No ML capabilities at all
- **Business Explanation (2/6)**: Basic summaries
  - Nondeterministic outputs
  - Limited narrative quality

### ThoughtSpot: Should be 8/20 (Currently 20/20 ❌)
- **Investigation (2/8)**: Single query responses
  - "Change Analysis" shows WHAT, not WHY
  - No multi-pass investigation
  - User must run separate searches
  - No probe dependencies
- **ML Understanding (4/6)**: Black-box ML
  - SpotIQ provides real ML predictions
  - BUT cannot explain WHY patterns exist
  - 33.3% accuracy (Stanford HAI benchmark)
  - No decision tree or rule visibility
- **Business Explanation (2/6)**: Shows correlations
  - Describes patterns found
  - Cannot explain underlying relationships
  - No causal reasoning

### Qlik: Should be 6/20 (Currently 15/20 ❌)
- **Investigation (4/8)**: User-guided clicking
  - Associative model lets user explore relationships
  - BUT user must manually click through
  - No automatic investigation
  - No probe dependencies or planning
  - User drives, not AI
- **ML Understanding (0/6)**: Not accessible
  - Qlik Predict exists but "requires data science understanding"
  - Not automatic
  - Not accessible to business users
- **Business Explanation (2/6)**: Basic narratives
  - Narrative generation exists
  - Limited explanation of causality

### Domo: Need to evaluate (Currently 18/20 - likely too high ❌)
- **Investigation (?)**: Need to verify if they have multi-pass investigation
- **ML Understanding (?)**: Do they have explainable ML or just predictive?
- **Business Explanation (?)**: Quality of narratives?

## Key Differentiators for High Scores (16-20 points)

### Must Have for 16+ points:
1. **Multi-round investigation** (not just multi-query with user driving)
2. **Probe dependencies** (later analysis uses earlier results)
3. **Explainable ML** (decision trees/rules, not just predictions)
4. **Autonomous planning** (system decides what to investigate next)
5. **Business-language synthesis** (executive-ready explanations)

### What Doesn't Qualify:
- ❌ User asking multiple follow-up questions (that's user-driven, not agentic)
- ❌ Clicking through associative model (that's manual exploration)
- ❌ Black-box ML predictions (need explainability)
- ❌ "SpotIQ found anomalies" without explaining why they're anomalies
- ❌ Basic statistical analysis marketed as "AI"

## The Agentic Investigation Test

**Question**: "Why did sales drop 15% in Q3?"

### Low Score (2-4 points):
- Tool returns: "Sales were $850K in Q3 vs $1M in Q2"
- User must then ask: "Which regions dropped?"
- User must then ask: "Why did West region drop?"
- User must then ask: "Which products in West region?"
- **Tool never drives the investigation**

### Medium Score (6 points):
- Tool suggests: "Would you like to see by region?"
- User clicks "Yes"
- Tool suggests: "West region dropped most. Drill into West?"
- User clicks "Yes"
- **Tool suggests but user must approve each step**

### High Score (8 points):
- Tool automatically executes investigation plan:
  - **Probe 1**: Identify regions with largest drops
  - **Probe 2**: Analyze West region (found in Probe 1) by product
  - **Probe 3**: Compare West region to other regions using ML_GROUP
  - **Probe 4**: Analyze timing - when did drop start in West?
  - **Probe 5**: ML_RELATIONSHIP - what factors predict drops in West?
  - **Synthesis**: "West region sales dropped 40% starting July 15th when your top sales rep left. The drop was concentrated in enterprise accounts (>$50K). ML analysis shows 'days since last contact' is now 3x higher in West than other regions. Recommend immediate territory reassignment."
- **System planned and executed entire investigation autonomously**

## Next Steps

1. **Get approval on this revised rubric**
2. **Rescore all 12 competitors** using strict evidence
3. **Update BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md** with new Understanding section
4. **Document evidence** for each competitor's score in their framework_scoring.md
5. **Update battle cards** and comparison pages with corrected scores

## Questions for Approval

1. **Does this capture what "Understanding" means?**
   - Deep ML to understand relationships (not just surface-level)
   - Agentic investigation with multi-round probe planning
   - Explains WHY, not just WHAT

2. **Is the 8-point Investigation rubric clear enough?**
   - Key distinction: Probe dependencies (query N uses results from query N-1)
   - System plans rounds (can do multiple rounds if needed)
   - Mix of query types (DATASET, ML_RELATIONSHIP, ML_GROUP, ML_PERIOD)

3. **Is the 6-point ML Understanding rubric correct?**
   - Explainable (decision trees, rules) vs black-box (predictions only)
   - Accessible (automatic) vs requires data scientist
   - Multiple ML types (relationship, clustering, group comparison, period comparison)

4. **Anything missing or wrong?**

---

**Once approved, this will dramatically widen Scoop's competitive gap on the dimension that matters most.**