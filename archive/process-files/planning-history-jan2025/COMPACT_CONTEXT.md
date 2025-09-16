# Compact Context for AI Sessions - Competitive Intelligence

**Last Updated**: January 2025  
**Purpose**: Quick orientation for fresh AI sessions

## Core Identity
**Scoop = Your AI Data Analyst**
- This is what gets them in the door
- Everything else supports this core identity
- We investigate (3-10 queries), find root causes, explain with ML

## The Critical Differentiator
**We live in the tools business users actually use:**
- **Excel**: =SCOOP() formulas that refresh live (not exports)
- **PowerPoint**: Import deck → Add live data → Export with brand (unique capability)
- **Slack**: 30-second setup for full analysis (not bot commands)
- **Google Sheets**: Native plugin for cloud users

## Framework Status
- **BUPAF**: 50-point scale (was 40)
- **5 Dimensions**: Independence, Analytical Depth, Workflow, Communication, Visual Intelligence
- **Scoop Score**: 46/50 (92%)
- **Next Competitor**: Domo at 29/50 (58%)

## Unique Technical Capabilities (Moats)
1. **Investigation Engine**: Multi-pass reasoning (3-10 queries)
2. **Schema Evolution**: Automatic without breaking (100% fail rate for competitors)
3. **Explanatory ML**: ML_GROUP/ML_PERIOD with J48/M5 Rules
4. **PowerPoint AI**: Brand color extraction using ColorThief (nobody else has this)
5. **Canvas System**: 1600x900 pixel-perfect with live data overlay

## Strategic Positioning Rules

### When to Hammer "Your Tools"
**Against NL-SQL** (Snowflake Cortex, Zenlytic, DataGPT):
- "They query in their portal. We analyze in your Excel."
- "3-4 hours to get to PowerPoint vs 30 seconds"

### When It's Secondary
**Against Enterprise BI** (Tableau, Power BI):
- Lead with investigation/ML capabilities
- "Your tools" is supporting point only

## Key Messages by Competitor Type

### vs NL-SQL Tools
"Why learn their portal when Scoop works in your Excel?"

### vs Enterprise BI
"They visualize what happened. We investigate why and what to do."

### vs Analyst Tools
"They need data teams. You need 30 seconds."

## The Math
- **Traditional path**: Portal → Export → Clean → Excel → PowerPoint = 3-4 hours
- **Scoop path**: Ask → Get answer in your tool = 30 seconds
- **Weekly time saved**: 17.5 hours per user

## Files to Never Modify Without Reading First
1. `framework/BUSINESS_USER_POWER_FRAMEWORK.md` - The scoring methodology
2. `competitor-details.json` - All competitor profiles and scores
3. `SCOOP_VISUAL_INTELLIGENCE_DISCOVERY.md` - PowerPoint AI discovery

## Current Initiative (January 2025)
**INCREMENTAL updates only** - Adding "Your Tools" positioning strategically without losing any technical depth. See `INCREMENTAL_UPDATE_PLAN_JAN2025.md` for detailed tasks.

## Quick Command Reference
```bash
# See current state
cat INCREMENTAL_UPDATE_PLAN_JAN2025.md

# Check framework
grep -A 10 "Visual Intelligence" framework/BUSINESS_USER_POWER_FRAMEWORK.md

# See competitor scores
jq '.[] | {vendor: .meta.vendor, score: .meta.score}' competitor-details.json
```

## Remember
- We're not replacing BI - we're your AI Data Analyst
- Technical capabilities are real differentiators - don't minimize them
- "Your tools" devastates small players, supports against big ones
- NEVER delete content - only add and refine