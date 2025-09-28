# Power BI Copilot: End-User Capabilities Research

**Date**: September 27, 2025
**Purpose**: Deep dive into what business users (report consumers) can actually do with Copilot vs report creators
**Key Question**: Is Copilot primarily for analysts building reports or business users consuming them?

---

## Executive Summary

**Primary Finding**: Power BI Copilot has TWO distinct modes with very different capabilities:

1. **Report Creator Mode** (Desktop + Service) - PRIMARY FOCUS
   - Target: Data analysts, BI developers, report authors
   - Can create reports, write DAX, build semantic models
   - Heavy marketing emphasis, most documentation

2. **Business User Mode** (Copilot Pane + Standalone) - SECONDARY CAPABILITY
   - Target: Report consumers, business users
   - Can ask questions about pre-built content
   - Limited to semantic model scope defined by IT/analysts
   - CANNOT do investigation, forecasting, or deep insights

**Critical Distinction**: Business users are **constrained to asking questions within the boundaries IT/analysts defined**. They cannot explore beyond the semantic model structure.

---

## What Business Users CAN Do

### Copilot Pane (In Reports)
**Scope**: Limited to the open report + its underlying semantic model

**Capabilities**:
- ✅ Summarize the report or specific topics
- ✅ Ask questions about data **in the semantic model**
- ✅ Generate new visuals from semantic model data
- ✅ Request ad-hoc calculations (e.g., "year-over-year growth", "ratio of X to Y")
- ✅ Filter by dimensions in the model (time, region, etc.)

**Example Supported Questions**:
- "What were the top 5 selling products in North America last month?"
- "Calculate the ratio of cosmetic product orders to all products"
- "Summarize sales trends shown in this report"

**Source**: Microsoft Learn - "Ask Copilot for data from your model"

### Standalone Copilot Experience (May 2025+)
**Scope**: Can query ANY report or semantic model user has access to

**Capabilities**:
- ✅ Find and analyze reports across workspace
- ✅ Query semantic models directly (not just open report)
- ✅ Create visuals from semantic model data
- ✅ Use measures and data fields in the model
- ✅ Row-level security (RLS) is enforced based on permissions

**Key Quote**: "Finds and answers questions about any data you have access to" - BUT this means "data in semantic models you have permission to access"

**Source**: Microsoft Learn - "Standalone Copilot experience in Power BI"

---

## What Business Users CANNOT Do

### Documented Limitations (Microsoft Official)

**❌ Cannot Generate Deep Insights**:
- No anomaly detection
- No forecasting ("How many books will we sell next year?")
- No "why" investigations ("Why do sales go down every July?")
- **Source**: Microsoft docs explicitly state "Can't currently answer questions that require generating new insights"

**❌ Cannot Do Follow-Up Context**:
- "Copilot doesn't answer follow-up questions. One question at a time."
- No conversation memory between queries
- Each question is isolated
- **Source**: Microsoft Power BI documentation

**❌ Cannot Explore Outside Semantic Model Boundaries**:
- Limited to tables/fields IT/analysts included in semantic model
- Cannot query source databases directly
- Cannot create new data relationships on the fly
- Must work within model structure report creator defined

**❌ Cannot Work With Unprepared Data**:
- "Data needs to be prepared to work with Copilot"
- "Model owners need to invest in prepping their data"
- Without prep: "generic, inaccurate, or even misleading outputs"
- **Source**: Microsoft Learn - Copilot overview

### Technical Constraints

**Geographic Limitations**:
- Not available in: India West, Indonesia Central, Korea South, Malaysia West, New Zealand North, Qatar Central, Taiwan North, Taiwan North West, UAE Central, France South, Germany North, Norway West
- Sovereign clouds unsupported (GPU availability)

**Language Limitations**:
- English only (officially supported)
- Multilingual prompts "may occasionally return relevant responses" but not supported

**Infrastructure Requirements**:
- Requires F64/P1 capacity minimum ($67K/year)
- 24-hour activation wait after F64 provisioning
- Semantic model must be created by IT/analysts first

---

## The Semantic Model Constraint (Critical)

### What IS a Semantic Model?
A pre-built data structure that defines:
- Which tables and fields are exposed
- How tables relate to each other
- What calculations (measures) are available
- Security rules (RLS) limiting data access

### The Constraint for Business Users

**Built by**: IT, data analysts, BI developers (not business users)
**Typical Timeline**: 6-12 weeks to build
**Required Skills**: DAX, Power BI modeling, data architecture

**Business Users Cannot**:
- ❌ Add new tables or data sources
- ❌ Create new relationships between tables
- ❌ Query data not included in model
- ❌ Bypass RLS restrictions
- ❌ Modify model structure

**Business Users Can Only**:
- ✅ Query within model boundaries
- ✅ Use pre-defined measures
- ✅ Combine fields IT exposed
- ✅ Filter by dimensions IT included

### Example Constraint

**Scenario**: Business user wants to analyze customer churn by support ticket volume

**If Semantic Model Includes**:
- ✅ Customer table
- ✅ Churn date field
- ✅ Support tickets table
- ✅ Relationship between customers and tickets
- ✅ Pre-built measures for churn rate

**Then**: User can ask "Show me churn rate by number of support tickets" ✅

**If Semantic Model Does NOT Include**:
- ❌ Support ticket escalation data
- ❌ Relationship to product defects table
- ❌ Customer satisfaction scores

**Then**: User CANNOT explore those dimensions, even if data exists in source systems ❌

**Critical Point**: Business users are **prisoners of the semantic model**. They can only explore what IT/analysts pre-configured.

---

## Primary vs Secondary Use Cases

### PRIMARY Use Case (Heavy Marketing Focus)

**Target**: Report creators, data analysts, BI developers

**Capabilities**:
- Generate report pages automatically
- Write DAX queries
- Create semantic model descriptions
- Suggest report topics and layouts
- Build dashboards faster

**Documentation Evidence**:
- Most docs under `/create-reports/` path
- Heavy emphasis on "create reports faster"
- DAX generation prominently featured
- Semantic model creation tools

**Quote from Data Goblins Analysis**:
"Primarily targeted at intermediate report creators and data professionals. Not recommended for novice users due to potential errors."

### SECONDARY Use Case (Limited Capability)

**Target**: Business users, report consumers

**Capabilities**:
- Ask questions about existing reports
- Query semantic models IT built
- Generate ad-hoc visuals from model data
- Get report summaries

**The Reality**: Business users can do **Q&A on top of pre-built content**, not open-ended data exploration.

**Marketing vs Reality**:
- **Microsoft Claims**: "Business users can ask questions and get insights"
- **Reality**: "Business users can ask questions **within the semantic model scope IT defined**"

---

## Comparison to Traditional Power BI Q&A Visual

**Important Context**: Power BI has had Q&A capability for years (before Copilot)

**Q&A Visual** (Traditional):
- Natural language queries on semantic models
- "Isn't reliant on generative AI" (Microsoft docs)
- Requires synonym mapping for field names
- Limited to model scope

**Copilot Enhancement to Q&A**:
- Automatically suggests synonyms (minor improvement)
- Better natural language understanding
- **Same fundamental constraint**: Limited to semantic model

**Key Insight**: Copilot didn't fundamentally change what business users can do—it made existing Q&A slightly better at understanding questions. The semantic model boundary remains.

---

## Independent Analysis: Data Goblins Perspective

**Source**: data-goblins.com/power-bi/copilot-in-power-bi

**Key Observations**:

**Primary Users**:
- "Primarily targeted at intermediate report creators and data professionals"
- "Not recommended for novice users"
- Requires "significant technical understanding to use effectively"

**Real-World Usability**:
- "Currently feels like a solution looking for a problem"
- "Some scenarios show potential, but many use cases seem unconvincing"
- "Outputs require careful validation"
- "Mistakes are possible" (per tool's own disclaimer)

**Critical Dependencies**:
- Quality depends heavily on prompt engineering
- Data model quality critical
- Semantic model setup determines success
- "Requires significant investment to make work well"

**Conclusion**: "An evolving technology with promise but current limitations... not yet a comprehensive replacement for human expertise"

---

## The Core Constraint Summary

### What "Ask Questions About Your Data" Really Means

**Microsoft's Framing**: "Business users can ask questions about their data"

**Technical Reality**: "Business users can ask questions about **data in IT-built semantic models**, within the structure IT defined, limited to relationships IT created, using measures IT configured"

### The Workflow Dependency

```
IT/Analyst Work (6-12 weeks):
1. Build semantic model
2. Define tables, relationships, measures
3. Configure security (RLS)
4. Test and deploy

↓

Business User Access:
5. Ask questions within model boundaries
6. Cannot explore beyond model scope
7. Cannot investigate "why" (no follow-ups)
8. Cannot forecast or detect anomalies
```

**Critical Point**: Business users are **downstream consumers** of IT-built infrastructure, not autonomous explorers.

---

## Implications for Competitive Positioning

### Current Frame (What We Said)
"Power BI Copilot: AI-powered Q&A for business users with limitations (single query, nondeterministic, expensive)"

### More Accurate Frame
"Power BI Copilot: Two products in one
1. **Primary**: AI assistant for analysts building dashboards (report creation focus)
2. **Secondary**: Limited Q&A for business users on IT-built content (cannot investigate, cannot explore beyond semantic model)"

### The Sharper Contrast

**Power BI Copilot World**:
- Analysts build semantic models (6-12 weeks)
- Analysts create reports/dashboards
- Business users ask questions about pre-built content
- **Copilot makes analysts more productive**, business users still dependent

**Scoop World**:
- No semantic model needed
- No report building phase
- Business users chat directly with AI data analyst
- **Copilot replaces need for analyst-built infrastructure** for most business user needs

### What This Changes

**Not "Both have chat, Scoop is better"**

**But Rather**: "Power BI: AI helps analysts build faster. Scoop: AI replaces the build phase"

---

## Sources

1. Microsoft Learn - "Overview of Copilot for Power BI"
   - https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction

2. Microsoft Learn - "Ask Copilot for data from your model"
   - https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-ask-data-question

3. Microsoft Learn - "Standalone Copilot experience in Power BI"
   - https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-chat-with-data-standalone

4. Microsoft Learn - "Enhance Q&A with Copilot for Power BI"
   - https://learn.microsoft.com/en-us/power-bi/natural-language/q-and-a-copilot-enhancements

5. Data Goblins - "Myths, Magic, and Copilot for Power BI"
   - https://data-goblins.com/power-bi/copilot-in-power-bi

6. Microsoft Power BI Blog - Various 2025 feature summaries

---

## Key Quotes for Competitive Use

**Microsoft's Own Limitations**:
- "Copilot doesn't answer follow-up questions. One question at a time."
- "Can't currently answer questions that require generating new insights"
- "Data needs to be prepared to work with Copilot"
- Outputs can be "generic, inaccurate, or even misleading"

**Independent Analysis** (Data Goblins):
- "Primarily targeted at intermediate report creators and data professionals"
- "Currently feels like a solution looking for a problem"
- "Requires significant technical understanding to use effectively"

**Semantic Model Dependency**:
- "Model owners need to invest in prepping their data"
- Business users can query "using the measures and other data fields in your model" (limited to model scope)

---

**Last Updated**: September 27, 2025
**Research Status**: Complete - Ready for competitive strategy update