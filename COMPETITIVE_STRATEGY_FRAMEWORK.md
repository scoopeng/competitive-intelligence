# Competitive Strategy Framework

**Created**: September 27, 2025
**Updated**: November 18, 2025 (Aligned with Domain Intelligence)
**Status**: Implemented for Snowflake Cortex and Power BI Copilot
**Purpose**: Enable competitor-specific customization using Domain Intelligence positioning

---

## The Problem We Solved

**Before**: Generic template applied to all competitors
- Same emphasis for everyone (Excel 20%, ML 15%, Cost 20%, UI 10%)
- Missed competitor-specific weaknesses (e.g., Hallucination risk in GenAI tools)
- Failed to differentiate "Generic AI" from "Domain Intelligence"
- No structured way to capture human strategic insight

**After**: Competitor-specific strategy + generic template
- Human writes `COMPETITIVE_STRATEGY.md` with emphasis levels based on BUA scores
- Machine reads strategy + framework scoring to generate customized content
- Snowflake Cortex gets 30% "Context Blindness" emphasis (Generic AI), Power BI gets 25% "Passive Dashboard" emphasis
- Single source of truth per competitor for positioning decisions

---

## Architecture

```
competitors/[name]/
├── COMPETITIVE_STRATEGY.md          # NEW - Human writes this (Domain Intelligence Focus)
├── evidence/
│   └── framework_scoring.md         # Machine-generated (BUA scores - The Evidence)
├── BATTLE_CARD.md                   # Machine reads both files above
└── outputs/
    └── web_comparison.md            # Machine reads both files above
```

**Information Flow**:
```
Human writes → COMPETITIVE_STRATEGY.md (Strategic Decisions: "Attack their Context Blindness")
                     ↓
Machine reads → framework_scoring.md (BUA Data: "Investigation Score 2/8")
                     ↓
Machine generates → web_comparison.md (Result: "Unlike Cortex which guesses, Scoop Investigates...")
```

---

## File Structure: COMPETITIVE_STRATEGY.md

### 1. PRIMARY WEAKNESSES (Rank Top 3)
- Identify 3 most exploitable weaknesses using the Domain Intelligence lens:
    - **Context Blindness** (Generic AI)
    - **Passive/Reactive** (Traditional BI)
    - **Portal Prison** (Legacy BI)
- Cite BUA scores as evidence (e.g., Understanding Dimension)
- Assign severity (Critical/High/Medium)

**Example**:
```markdown
**#1: Context Blindness (Generic AI)** (Severity: Critical)
- Evidence: BUA Understanding 2/20 (0/8 Agentic Investigation, 0/6 Explainable ML)
- Why It Matters: Cortex guesses SQL based on schema names, ignoring business logic.
- Our Advantage: Domain Intelligence (Schema v2.8) encodes expert rules.
- Emphasis Level: 30% of web comparison
```

### 2. KEY SCENARIOS (Stories that expose weaknesses)
- Real-world "Day in the Life" contrasts
- Focus on "Investigation" vs "Querying"

**Example**:
```markdown
**Scenario 1: The "Why" Question**
- When to Use: Against Text-to-SQL tools (Cortex, ThoughtSpot)
- Story: "VP asks 'Why did margin drop?' Cortex gives you a SQL query for current margin.
  Scoop runs a multi-step investigation: checks mix, pricing, and inventory."
- Expected Impact: Exposes the "Intelligence Ceiling" of generic tools.
```

### 3. TALKING POINTS (Emphasis hierarchy)
- Order by importance
- Top 3 should address primary weaknesses
- **Lead with Domain Intelligence**: Autonomy, Encoded Expertise, Investigation.

**Example**:
```markdown
**Lead With**:
1. "Encoded Expertise vs Generic Guessing" (Context Blindness)
2. "Active Investigation vs Passive Monitoring" (Autonomy)
3. "Your Tools vs Their Portal" (Flow)

**De-Emphasize**:
- Cost (TCO is the closer, not the opener)
```

### 4. CONTENT DISTRIBUTION (Word allocation)
- Allocate 7,500 words based on competitor weaknesses
- **New Categories**:
    - **Investigation/Context**: (Primary differentiator)
    - **Autonomy/Flow**: (BUA impact)
    - **Data/Schema**: (Technical moat)

**Example**:
```markdown
**Recommended Mix**:
- Investigation/Context: 35% (vs 20% default) ⬆️ Attack Generic AI
- Autonomy/Flow: 25% (vs 20% default)
- Data/Schema: 20% (vs 15% default)
- Cost: 20% (vs 25% default) ⬇️ reduced

**Rationale**: Cortex is a "Smart Guesser." We must prove it doesn't understand the business.
```

### 5. PROOF POINTS (Evidence to cite)
- Link to BUA scores in `framework_scoring.md`
- Pull specific quotes from research (e.g., "Hallucinations")
- Include official documentation

### 6. WIN CONDITIONS (When we win/lose)
- Be honest about when Scoop wins (Operational/Executive/Investigation)
- Acknowledge when competitor is better fit (Strict Reporting/Pixel-Perfect Dashboards)

### 7. COMPETITIVE POSITIONING
- One-sentence position
- 30-second elevator pitch
- Key contrast table

### 8. AVOID OVER-CLAIMING (Credibility guardrails)
- List things NOT to say
- Provide evidence-based alternatives

### 9. CUSTOM CONTENT BLOCKS
- 2-3 competitor-specific examples

### 10. SALES GUIDANCE
- Discovery questions to ask ("Does it know your business rules?")
- Objection handling
- Demo focus areas

---

## Examples: Snowflake Cortex vs Power BI Copilot

### Snowflake Cortex Strategy (Generic AI)

**Primary Weaknesses**:
1. **Context Blindness** (30% emphasis) - It guesses SQL, doesn't know business rules.
2. **No Autonomy** (25% emphasis) - Reactive only.
3. **No UI** (20% emphasis) - Must build your own app.

**Content Distribution**:
- Investigation/Context: 35% ⬆️ Critical gap
- Autonomy: 25% ⬆️ Core failure
- UI/Flow: 20%
- Cost: 20%

**Key Scenario**: "VP asks 'Why?'. Cortex returns a number. Scoop returns a root cause analysis."

**One-Sentence Position**: "Snowflake Cortex is a generic LLM wrapper that guesses SQL; Scoop is a Domain Intelligence Platform that investigates using your encoded expertise."

---

### Power BI Copilot Strategy (Passive BI)

**Primary Weaknesses**:
1. **Passive/Reactive** (25% emphasis) - Still just a dashboard helper.
2. **Context Limited** (25% emphasis) - Trapped in semantic model limits.
3. **Portal Prison** (20% emphasis) - Must log in to Power BI.

**Content Distribution**:
- Investigation/Autonomy: 30% ⬆️ Attack "Passive" nature
- Flow: 25% ⬆️ Attack "Portal"
- Cost: 25% ⬆️ Attack F64 pricing
- Context: 20%

**Key Scenario**: "Dashboards show you *what* happened. You still have to click 50 times to find *why*. Scoop does that clicking for you."

**One-Sentence Position**: "Power BI Copilot is a chat interface for passive dashboards; Scoop is an autonomous investigator that proactively finds answers."

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