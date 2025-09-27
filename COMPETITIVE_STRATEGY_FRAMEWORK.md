# Competitive Strategy Framework

**Created**: September 27, 2025
**Status**: Implemented for Snowflake Cortex and Power BI Copilot
**Purpose**: Enable competitor-specific customization while maintaining consistency

---

## The Problem We Solved

**Before**: Generic template applied to all competitors
- Same emphasis for everyone (Excel 20%, ML 15%, Cost 20%, UI 10%)
- Missed competitor-specific weaknesses
- Snowflake Cortex (NO UI) got same 10% UI emphasis as Power BI (has Teams)
- No structured way to capture human strategic insight

**After**: Competitor-specific strategy + generic template
- Human writes `COMPETITIVE_STRATEGY.md` with emphasis levels
- Machine reads strategy + framework scoring to generate customized content
- Snowflake gets 30% UI emphasis (critical gap), Power BI gets 25% cost emphasis ($67K F64 tax)
- Single source of truth per competitor for positioning decisions

---

## Architecture

```
competitors/[name]/
├── COMPETITIVE_STRATEGY.md          # NEW - Human writes this
├── evidence/
│   └── framework_scoring.md         # Machine-generated (BUA scores)
├── BATTLE_CARD.md                   # Machine reads both files above
└── outputs/
    └── web_comparison.md            # Machine reads both files above
```

**Information Flow**:
```
Human writes → COMPETITIVE_STRATEGY.md (strategic decisions)
                     ↓
Machine reads → framework_scoring.md (BUA data) + COMPETITIVE_STRATEGY.md (strategy)
                     ↓
Machine generates → web_comparison.md + BATTLE_CARD.md (customized)
```

---

## File Structure: COMPETITIVE_STRATEGY.md

### 1. PRIMARY WEAKNESSES (Rank Top 3)
- Identify 3 most exploitable weaknesses
- Cite BUA scores as evidence
- Assign severity (Critical/High/Medium)
- Define emphasis level (XX% of web comparison)

**Example**:
```markdown
**#1: No User Interface** (Severity: Critical)
- Evidence: BUA Flow 2/20 (0/8 Native Integration, 0/6 Portal Prison)
- Why It Matters: Business users forced into SQL console, no mobile
- Our Advantage: Slack-native, mobile-ready, auto PowerPoint
- Emphasis Level: 30% of web comparison
```

### 2. KEY SCENARIOS (Stories that expose weaknesses)
- 2-4 real-world scenarios
- Specific, relatable, measurable
- Shows competitor's weakness dramatically

**Example**:
```markdown
**Scenario 1: Mobile Executive Question**
- When to Use: Against competitors with no mobile access
- Story: "CEO texts at 9 PM: 'What's our cash?' Cortex needs desktop+VPN.
  Scoop answers in 30 sec from Slack mobile."
- Expected Impact: Shows Cortex built for data engineers, not executives
```

### 3. TALKING POINTS (Emphasis hierarchy)
- Order by importance
- Top 3 should address primary weaknesses
- "De-emphasize" section prevents wasting words

**Example**:
```markdown
**Lead With**:
1. "Where you work" (Slack vs console) - Because they have NO UI
2. "What you get" (PowerPoint vs SQL) - Because no presentation tools
3. "Investigation vs generation" - Because 0/8 Investigation score

**De-Emphasize**:
- Cost (comparable pricing, not differentiator)
```

### 4. CONTENT DISTRIBUTION (Word allocation)
- Allocate 7,500 words based on competitor weaknesses
- Increase/decrease sections strategically
- Include rationale

**Example**:
```markdown
**Recommended Mix**:
- UI/Workflow: 30% (~2,250 words) ⬆️ MAJOR INCREASE
- Investigation: 25% (~1,875 words)
- Excel: 15% (~1,125 words) ⬇️ reduced
- Cost: 15% (~1,125 words) ⬇️ reduced

**Rationale**: Snowflake has literally NO UI (0/8 Native Integration).
Leading with "where you work" is essential.
```

### 5. PROOF POINTS (Evidence to cite)
- Link to framework_scoring.md
- Pull specific quotes from research
- Include official documentation

### 6. WIN CONDITIONS (When we win/lose)
- Be honest about when Scoop wins
- Acknowledge when competitor is better fit
- Prevents wasted sales cycles

### 7. COMPETITIVE POSITIONING
- One-sentence position
- 30-second elevator pitch
- Key contrast table

### 8. AVOID OVER-CLAIMING (Credibility guardrails)
- List things NOT to say
- Provide evidence-based alternatives
- Prevents credibility damage

### 9. CUSTOM CONTENT BLOCKS
- 2-3 competitor-specific examples
- Copy-paste ready for web comparison
- Highly specific, dramatic contrasts

### 10. SALES GUIDANCE
- Discovery questions to ask
- Objection handling
- Demo focus areas

---

## Examples: Snowflake Cortex vs Power BI Copilot

### Snowflake Cortex Strategy

**Primary Weaknesses**:
1. **No UI** (30% emphasis) - 0/8 Native Integration, 0/6 Portal Prison
2. **Investigation Failure** (25% emphasis) - 0/8 Investigation score
3. **IT Dependency** (20% emphasis) - 0/8 Setup score

**Content Distribution**:
- UI/Workflow: 30% (vs 10% default) ⬆️ Critical gap
- Investigation: 25% (vs 15% default) ⬆️ Core failure
- Cost: 15% (vs 20% default) ⬇️ Comparable pricing
- ML: 10% (vs 15% default) ⬇️ They have basic stats

**Key Scenario**: "CEO texts at 9 PM: 'What's our cash position?' Cortex: desktop+VPN required. Scoop: Slack mobile, 30 seconds."

**One-Sentence Position**: "Snowflake Cortex is a SQL generation tool for data engineers working in Snowflake console, Scoop is a business analytics platform for Excel users working in Slack"

---

### Power BI Copilot Strategy

**Primary Weaknesses**:
1. **$67K Infrastructure Tax** (25% emphasis) - F64 capacity mandatory
2. **Nondeterministic** (25% emphasis) - 3% satisfaction (Gartner)
3. **Single-Query** (20% emphasis) - No follow-ups

**Content Distribution**:
- Cost/Infrastructure: 25% (vs 15% default) ⬆️ Major pain
- Reliability: 20% (vs 10% default) ⬆️ Nondeterminism
- Investigation: 20% (vs 15% default) ⬆️ Limitation
- UI: 8% (vs 15% default) ⬇️ Teams integration ok

**Key Scenario**: "You pay $67K/year for F64. Ask 'What caused Q3 revenue drop?' twice. Get two different answers. Which do you trust for board presentation?"

**One-Sentence Position**: "Power BI Copilot is a nondeterministic Q&A add-on requiring $67K/year infrastructure, Scoop is a deterministic investigation platform with zero infrastructure costs"

---

## How to Use This Framework

### For New Competitor Research:

1. **Complete framework_scoring.md** (machine-generated from research)
   - Produces BUA scores (X/100)
   - Identifies dimension weaknesses

2. **Write COMPETITIVE_STRATEGY.md** (human strategic decisions)
   - Review BUA scores to identify weaknesses
   - Use template at `competitors/SHARED/COMPETITIVE_STRATEGY_TEMPLATE.md`
   - Fill in all 10 sections
   - Takes 2-3 hours to write thoroughly

3. **Generate web_comparison.md** (machine reads both files)
   - Reads strategy for emphasis levels and scenarios
   - Reads framework_scoring for BUA data and evidence
   - Applies content distribution from Section 4
   - Uses custom examples from Section 9

### For Updating Existing Competitors:

1. **Quarterly review** of COMPETITIVE_STRATEGY.md
   - Check if competitor launched new features
   - Update BUA scores if capabilities changed
   - Adjust emphasis levels if needed
   - Update proof points with new evidence

2. **Triggered updates**:
   - Competitor announces major product changes → Update immediately
   - Win/loss analysis reveals new patterns → Adjust win conditions
   - Sales reports different objections → Update talking points

---

## Benefits of This Approach

### ✅ Single Source of Truth
- One file per competitor for all strategic decisions
- No confusion about where to update positioning
- Version controlled (git tracks changes)

### ✅ Evidence-Based
- Section 5 forces linking to framework_scoring.md
- Proof points must be documented
- "Avoid Over-Claiming" prevents unsupported statements

### ✅ Flexible Emphasis
- Can dial UI emphasis up (Snowflake 30%) or down (Power BI 8%)
- Machine respects these weights when generating
- Competitor-specific without being ad-hoc

### ✅ Prevents Over-Rotation
- "De-Emphasize" section prevents wasting words
- "We Lose When" acknowledges competitor strengths
- "Avoid Over-Claiming" maintains credibility

### ✅ Reusable Content
- Section 9 (Custom Content Blocks) are copy-paste ready
- Section 2 (Scenarios) work across sales materials
- Section 7 (Positioning) is elevator-pitch ready

### ✅ Sales Enablement
- Section 10 provides discovery questions
- Objection handling built-in
- Demo focus areas specified

---

## Current Status

### Completed ✅
- **Template**: `competitors/SHARED/COMPETITIVE_STRATEGY_TEMPLATE.md`
- **Snowflake Cortex**: Full strategy file with 30% UI emphasis
- **Power BI Copilot**: Full strategy file with 25% cost emphasis

### Planned 🔄
- **Phase 1** (This Week): DataGPT, Tellius (weak UI competitors)
- **Phase 2** (Next Week): Domo, Qlik, Sisense (portal prison)
- **Phase 3** (Later): ThoughtSpot, Tableau, Zenlytic (lower priority)

### Rollout Plan

**Week 1**: Test framework with 2 competitors
- ✅ Snowflake Cortex (extreme UI gap)
- ✅ Power BI Copilot (cost + reliability)
- Validate structure works
- Iterate on template

**Week 2**: Expand to weak-UI competitors
- DataGPT (chat-only, no Excel/PowerPoint)
- Tellius (portal-dependent, limited mobile)
- Sisense (weak UI, no Slack)

**Week 3**: Portal prison competitors
- Domo (0/6 Portal Prison, no native Excel)
- Qlik (desktop app, portal-dependent)

**Week 4**: Remaining competitors
- ThoughtSpot (better UX, smaller gaps)
- Tableau Pulse (2018 tech, Salesforce only)
- Zenlytic (chat interface, limited)

---

## Maintenance Guidelines

### When to Update Strategy File:

**Quarterly** (Every 3 months):
- [ ] Check if competitor has launched new features
- [ ] Re-run framework scoring if capabilities changed
- [ ] Update pricing information
- [ ] Verify proof points still accurate

**Triggered** (Update immediately when):
- Competitor announces major product changes
- BUA dimension scores change by >3 points
- Win/loss analysis reveals new patterns
- Sales team reports different objections than expected

### Red Flags (Update Needed):

- Sales says "That objection doesn't come up anymore"
- Competitor launches feature that addresses primary weakness
- Win rate drops significantly in specific scenarios
- New Gartner/Forrester reports with updated data

---

## Integration with Existing Files

### COMPETITIVE_STRATEGY.md does NOT replace:

- **framework_scoring.md** (machine-generated BUA scores)
- **BATTLE_CARD.md** (generated from strategy + scoring)
- **README.md** (navigation)
- **research/** (all research preserved)

### COMPETITIVE_STRATEGY.md complements:

- **framework_scoring.md**: Provides BUA data (what are the facts?)
- **COMPETITIVE_STRATEGY.md**: Provides positioning (how should we position?)
- **web_comparison.md**: Uses both to generate customized comparison

---

## Success Metrics

### Before Framework:
- Generic template applied to all
- UI emphasis: 10% for everyone
- No structured strategic decisions
- Ad-hoc positioning changes

### After Framework:
- Competitor-specific emphasis
- UI emphasis: 30% (Snowflake) to 8% (Power BI) based on weakness
- Structured 10-section strategy
- Version-controlled positioning decisions

### Qualitative Goals:
- Web comparisons should lead with competitor's biggest weakness
- Sales team should have clear discovery questions
- Positioning should be evidence-based and honest
- Content allocation should reflect buyer priorities

---

## Questions & Answers

**Q: Why not embed this in framework_scoring.md?**
A: Framework scoring is machine-generated and shouldn't be human-edited. Mixing data with strategy causes confusion.

**Q: Why 10 sections? Isn't that too much?**
A: You can fill sections briefly. Template provides structure, not rigidity. Some sections (custom examples) are optional but powerful.

**Q: What if competitor improves and weaknesses change?**
A: Quarterly review schedule catches this. Update strategy file, re-generate web comparison. Version control shows what changed and why.

**Q: How long to write initial strategy file?**
A: 2-3 hours if you use template and have framework_scoring.md done. Sections 1-4 are quick (evidence-based). Sections 9-10 take more thought (examples, sales guidance).

**Q: Can we automate any of this?**
A: Sections 1, 5 could be partially auto-generated from BUA scores. But human judgment on emphasis levels and scenarios is valuable. Hybrid approach is best.

---

## Next Steps

1. ✅ Create template and examples (DONE)
2. ✅ Implement for Snowflake Cortex and Power BI Copilot (DONE)
3. 🔄 Test generation of web_comparison.md using strategy files
4. 🔄 Iterate on template based on learnings
5. 🔄 Roll out to remaining 9 competitors

**Documentation Updated**: This file, CLAUDE.md, START_HERE.md

---

**Created**: September 27, 2025
**Last Updated**: September 27, 2025
**Status**: Framework Complete, Rollout Beginning