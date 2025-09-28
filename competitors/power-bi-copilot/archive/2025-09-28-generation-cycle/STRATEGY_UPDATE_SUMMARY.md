# Power BI Copilot Strategy Update - September 28, 2025

## Summary of Changes

**Total modifications**: ~800 words added/modified across 6 sections
**Strategy approach**: Investigation-first positioning with "AI Data Analyst vs Text-to-Query Tool" framework
**Emphasis shift**: Investigation 20% → 30%, Cost 25% → 20%, Nondeterminism 25% → 15%

---

## Section-by-Section Changes

### 1. PRIMARY WEAKNESSES (Enhanced #3)

**Before**:
- #3: "Single-Query Limitation (No Investigation)" - 20% emphasis
- Brief explanation of no follow-ups

**After**:
- #3: "Bounded by Semantic Models & Cannot Investigate" - 30% emphasis
- **Three sub-limitations explained**:
  1. Cannot investigate "why" (multi-step analysis)
  2. Cannot handle complex "what" (subqueries: top N, thresholds, multi-condition filtering)
  3. Semantic model prison (business users bounded by IT definitions)
- Examples: "Show opportunities from top 5 reps by win rate" requires 1-2 weeks IT DAX work

**Severity updated**: Weakness #2 reduced from "Critical" to "High" (LLM models may improve)

---

### 2. KEY SCENARIOS (Reordered + Enhanced)

**Before order**:
1. $67K Question That Fails (cost + nondeterminism)
2. 14 Weeks to Hello World (time)
3. Follow-Up That Doesn't Work (investigation)
4. Excel Copilot Upsell (cost)

**After order**:
1. **Investigation That Can't Continue** (PRIMARY - moved from #3)
2. **Complex Question That Requires IT** (NEW - subquery example)
3. $67K Question That Fails (cost + nondeterminism)
4. 14 Weeks to Hello World (time)
5. Excel Copilot Upsell (cost)

**New Scenario 2 details**:
- VP asks: "Show me deals from our top 5 reps by win rate"
- Power BI can't do without IT building custom DAX (1-2 weeks)
- Scoop: automatic subquery generation (3 seconds)
- Shows concrete "complex what" limitation

---

### 3. TALKING POINTS (Investigation-First)

**Before lead points**:
1. "$67K infrastructure tax for unreliable results"
2. "14 weeks vs 30 seconds"
3. "Same question, different answers"

**After lead points**:
1. **"Text-to-query vs AI data analyst"** (positioning frame)
2. **"Can't investigate why or handle complex what"** (investigation)
3. **"One question at a time, no follow-ups"** (single-turn)
4. "$67K infrastructure tax + 14-week setup" (cost/time - combined, demoted)

**New "Always Mention" items**:
- Multi-pass investigation (3-10 queries)
- **Subquery generation** (top N, thresholds, complex filtering)
- Deterministic results
- Excel formula engine
- No semantic model required

**New "De-Emphasize" item**:
- Nondeterminism (acknowledge but models may improve)

---

### 4. CONTENT DISTRIBUTION (30% Investigation)

**Before**:
- Cost: 25% (~1,875 words)
- Nondeterminism: 20% (~1,500 words)
- Investigation: 20% (~1,500 words)

**After**:
- **Investigation: 30% (~2,250 words)** ⬆️ +10%
  - Multi-pass investigation: 750 words
  - Complex "what" questions (subqueries): 600 words
  - No follow-ups: 450 words
  - Root cause examples: 450 words
- Cost: 20% (~1,500 words) ⬇️ -5%
- Nondeterminism: 15% (~1,125 words) ⬇️ -10%

**Rationale updated**:
> "Investigation limitation (30%) is architectural and harder for Microsoft to fix than nondeterminism (which may improve with better LLM models). Cost ($67K, 20%) is still a door-opener. Nondeterminism (15%) is real but may decrease as models improve."

---

### 5. COMPETITIVE POSITIONING (Above the Fold)

**Before one-sentence**:
> "Power BI Copilot is a nondeterministic Q&A add-on requiring $67K/year infrastructure for Microsoft Power BI users, Scoop is a deterministic investigation platform..."

**After one-sentence**:
> "Power BI Copilot is a **text-to-query interface bounded by IT-built semantic models**—handles simple 'what' questions only, **cannot investigate 'why' or handle complex analytical filtering**, requires $67K/year infrastructure and delivers nondeterministic results. Scoop is an **AI data analyst**—handles complex 'what' and 'why' questions through multi-pass investigation, works on any data, zero infrastructure, deterministic results."

**New elevator pitch** (investigation-first):
- Opens with: "Power BI Copilot is two things: primarily for analysts (70%), secondarily for business users (30%)"
- Emphasizes: Can't investigate "why" or handle complex filtering
- Cites Microsoft: "Copilot doesn't answer follow-up questions" + "Can't answer questions that require generating new insights"
- Closes with: "Power BI Copilot shows you the data. Scoop investigates and explains."

**Key Contrast table enhanced**:
- Added row: "Product Type" (Text-to-query vs AI data analyst)
- Added row: "Simple 'What' Questions" (Both ✅)
- Added row: "Complex 'What' Questions" (❌ vs ✅)
- Added row: "Why Investigation" (❌ vs ✅)

---

### 6. SALES GUIDANCE (Investigation-First Discovery)

**New lead discovery question**:
> "When your business users ask 'why did revenue drop?'—does Power BI Copilot investigate root cause or just show the data?"

**New second discovery question**:
> "Can business users ask complex analytical questions like 'show accounts where revenue grew more than 20% this quarter' without IT building custom DAX measures?"

**Updated objection handlers** (all 4 rewritten):

1. **"Isn't Copilot the natural next step?"**
   - Now opens with: "Power BI Copilot is primarily for analysts (70%), not business users (30%)"
   - Emphasizes: "Text-to-query interface" vs "AI data analyst"
   - Cites: Microsoft's explicit limitations

2. **"Microsoft will improve over time"**
   - Now says: "Investigation limitation is architectural, not just nondeterminism"
   - "Semantic model approach is fundamental to their design"
   - "Nondeterminism may improve, but investigation gap remains"

3. **"We're a Microsoft shop"**
   - Now says: "Power BI Copilot primarily designed for analysts, not business user investigation"
   - "3% satisfaction rate reflects gap between what business users need (investigation) and what it provides (text-to-query)"

4. **"F64 cost is already budgeted"**
   - Now leads with: "Fundamental challenges remain—can't investigate 'why', can't handle complex filtering, bounded by semantic model"
   - De-emphasizes cost, emphasizes capability gap

**Demo Focus Areas reordered**:
1. **Investigation demo** (PRIMARY - moved to #1)
2. **Complex query demo** (NEW #2 - subquery example)
3. Determinism demo
4. Cost calculator
5. 30-second setup
6. Excel formulas

---

## What Stayed the Same

✅ **Top 3 weakness structure** (cost, nondeterminism, investigation)
✅ **All proof points** (BUA scores, Gartner stats, Microsoft quotes)
✅ **Win conditions** (when we win/lose)
✅ **Avoid over-claiming** (credibility guardrails)
✅ **Custom content blocks** (nondeterminism CFO example, investigation VP example)
✅ **Maintenance schedule**

---

## Strategic Rationale

### Why Investigation-First?

1. **Defensibility**: Investigation limitation is architectural (semantic model approach), harder for Microsoft to fix than nondeterminism (which may improve with better LLM models)

2. **Breadth**: Investigation encompasses both:
   - "Why" questions (multi-pass analysis)
   - Complex "what" questions (subqueries, analytical filtering)
   - Semantic model boundary (can only query what IT built)

3. **Market positioning**: "AI Data Analyst vs Text-to-Query Tool" is clearer differentiation than "both have chat, ours is better"

4. **Sales enablement**: Gives concrete examples (subqueries) and discovery questions to expose limitation

### Why Reduce Nondeterminism Emphasis?

- LLM models improve over time (OpenAI GPT-5, Anthropic Claude 4, etc.)
- Microsoft may reduce (but not eliminate) nondeterminism
- Investigation gap is structural and won't improve with better models
- Still mention nondeterminism (15%), just don't lead with it

### Why Keep Cost Emphasis at 20%?

- Still a door-opener ($67K sticker shock)
- Combines well with other points (infrastructure + limited capability)
- But secondary to investigation capability gap

---

## Impact on Web Comparison Generation

When generating web comparisons using this strategy:

**Section 2 (Capabilities) - 4,000 words total**:
- **Investigation section**: 2,250 words (30%)
  - Lead with multi-pass investigation examples
  - Include 4+ subquery patterns (top N, thresholds, multi-condition, time comparison)
  - Explain semantic model boundary with concrete examples
  - Show Microsoft quotes: "Can't answer questions that require generating new insights"

- **Cost section**: 1,500 words (20%)
  - Still hit F64 $67K infrastructure tax
  - Include 14-week timeline
  - Excel Copilot upsell angle

- **Nondeterminism section**: 1,125 words (15%)
  - Show the problem (same Q → different A)
  - Cite Gartner 3% satisfaction
  - Acknowledge models may improve but emphasize as supporting point

**TL;DR / Executive Summary**:
- Lead with "AI data analyst vs text-to-query" positioning
- Emphasize investigation limitation first
- Cost and nondeterminism as supporting points

---

## Next Steps

1. **Generate new web comparison** using updated strategy (ready to execute)
2. **Update battle card** to reflect investigation-first approach
3. **Test with sales team** - get feedback on "AI data analyst vs text-to-query" framing
4. **Monitor Microsoft updates** - track if they add investigation capabilities or improve nondeterminism

---

**Strategy Version**: 2.0 (Investigation-First)
**Last Updated**: September 28, 2025
**Changes**: Investigation 30% (up from 20%), Cost 20% (down from 25%), Nondeterminism 15% (down from 25%)
**New Positioning**: "AI Data Analyst vs Text-to-Query Tool"