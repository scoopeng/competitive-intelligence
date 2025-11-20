# Competitive Strategy Framework

**Created**: September 27, 2025
**Updated**: November 19, 2025 (Aligned with Intelligence Layer Strategy)
**Status**: Implemented for Snowflake Cortex and Power BI Copilot
**Purpose**: Enable competitor-specific customization using Domain Intelligence positioning

---

## The Problem We Solved

**Before**: Generic "Kill Shot" attacks
- "Your tool is bad because X"
- created friction with partners (Snowflake/Microsoft)
- missed the "Enhancement" opportunity

**After**: "The Capability Ladder" positioning
- "Your tool is excellent at Level 1/2; we add Level 4"
- Positions Scoop as the *inevitable* next layer
- Validates customer's existing investments while proving the need for Scoop

---

## The Capability Ladder (Strategic Framework)

We frame the market as a stack, not a zero-sum war.

*   **Level 1: Data Infrastructure** (Snowflake, Databricks)
    *   *Role*: Store and process data at scale.
    *   *Scoop Position*: "We are the Intelligence Layer that makes your data speak business."
*   **Level 2: Visualization** (Tableau, Power BI)
    *   *Role*: Show *what* happened.
    *   *Scoop Position*: "You show the chart; we explain *why* it changed."
*   **Level 3: Translation** (Text-to-SQL, Copilots)
    *   *Role*: Turn text into queries (Semantic Aware).
    *   *Scoop Position*: "You translate language; we investigate logic."
*   **Level 4: Domain Intelligence** (Scoop)
    *   *Role*: Operationalize expert reasoning (Outcome Aware).

---

## File Structure: COMPETITIVE_STRATEGY.md

### 1. PRIMARY WEAKNESSES (Rank Top 3)
- Identify 3 most exploitable gaps using the **Context Maturity Model**:
    - **Stuck at Level 2 (Semantic Aware)**: Generic AI knows definitions but not logic, *leading to confidently wrong answers and eroding trust*.
    - **The Searchlight Problem (Passive)**: Great tools, but requires manual looking, *leading to 95% of operational issues going unaddressed*.
    - **The Scarcity Trap (Manual)**: Experts can't review everything, *resulting in millions of dollars in missed revenue opportunities*.
- Cite BUA scores as evidence.

**Example**:
```markdown
**#1: Stuck at Level 2 (Semantic Context)** (Severity: Critical)
- Evidence: BUA Understanding 2/20. Knows "Revenue" = "Sales" but not "Revenue" != "Trials".
- Why It Matters: Generic AI guesses at logic, resulting in "confidently wrong" answers and eroding business trust.
- Our Advantage: Encoded Expertise (Level 4 Context) delivers deterministic, outcome-aware intelligence.
- Emphasis Level: 30% of web comparison
```

### 2. KEY SCENARIOS (Stories that expose weaknesses)
- Real-world "Day in the Life" contrasts
- Focus on "Scaling/Coverage" vs "Manual Hunting"

**Example**:
```markdown
**Scenario 1: The "Monday Morning" Test**
- When to Use: Against Legacy BI (Power BI, Tableau)
- Story: "You have 500 stores. Monday morning, can you review all 500?
  Scoop reviews 100% of them before you wake up."
- Expected Impact: Exposes the hidden cost of manual analysis limitations (The Scarcity Trap).
```

### 3. TALKING POINTS (Emphasis hierarchy)
- Order by importance
- **Lead with Enhancement**: "We complete your stack."

**Example**:
```markdown
**Lead With**:
1. "The Intelligence Layer" (Partnership Narrative)
2. "The Digital Detective" (Active Investigation)
3. "Omnipresent Intelligence" (Coverage)

**De-Emphasize**:
- "Cheaper" (TCO is the enabler, not the lead)
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

**Rationale**: Cortex is a "Search Engine." We are a "Detective."
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
1. **Stuck at Level 2 (Semantic Context)** (30% emphasis) - Guesses SQL, *leading to confidently wrong answers and eroding business trust*.
2. **The Search Engine Problem** (25% emphasis) - Reactive only, *requires humans to proactively hunt for insights*.
3. **No UI** (20% emphasis) - Must build your own app, *creating IT dependency and slow time-to-value*.

**Content Distribution**:
- Investigation/Context: 35% ⬆️ Critical gap
- Autonomy: 25% ⬆️ Core failure
- UI/Flow: 20%
- Cost: 20%

**Key Scenario**: "VP asks 'Why?'. Cortex returns a number (maybe wrong). Scoop returns a root cause based on your rules."

**One-Sentence Position**: "Snowflake provides the powerful Data Layer; Scoop provides the Intelligence Layer that makes it speak business."

---

### Power BI Copilot Strategy (Passive BI)

**Primary Weaknesses**:
1. **The Scarcity Trap (Passive/Manual)** (25% emphasis) - Dashboards require manual analysis, *leading to 95% of operational issues going unaddressed due to limited expert bandwidth*.
2. **Context Limited** (25% emphasis) - Trapped in semantic model limits, *cannot understand complex business logic beyond simple definitions*.
3. **Portal Prison** (20% emphasis) - Must log in to Power BI, *creating workflow friction and limiting real-time impact*.

**Content Distribution**:
- Investigation/Autonomy: 30% ⬆️ Attack "Passive/Scarcity" nature
- Flow: 25% ⬆️ Attack "Portal"
- Cost: 25% ⬆️ Attack F64 pricing
- Context: 20%

**Key Scenario**: "Dashboards show you *what* happened. Scoop investigates *why* and tells you in Slack."

**One-Sentence Position**: "Power BI visualizes the data; Scoop investigates the why, scaling expert reasoning to every decision."

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
**Last Updated**: November 19, 2025
**Status**: Framework Complete, Rollout Beginning