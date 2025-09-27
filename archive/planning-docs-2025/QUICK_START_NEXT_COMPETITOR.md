# Quick Start: Generate Next Competitor Web Comparison

**Template for executing web comparison generation efficiently**

---

## Pre-Flight Checklist (5 min)

Run this command to see current status:
```bash
./check_web_comparison_status.sh
```

**Select next competitor from Tier 1**:
1. ⏳ Tableau Pulse (18/59, 31%, Category C) - NEXT
2. ⏳ ThoughtSpot (28/59, 47%, Category B)
3. ⏳ Snowflake Cortex (17/59, 29%, Category C)

---

## Step 1: Review Existing Research (10-15 min)

### Files to Read
```bash
# Replace {competitor} with actual name (e.g., tableau-pulse)

# 1. Framework scoring (understand the 21/59 breakdown)
cat competitors/{competitor}/evidence/framework_scoring.md

# 2. Battle card (key talking points)
cat competitors/{competitor}/BATTLE_CARD.md

# 3. Research library (evidence for claims)
ls competitors/{competitor}/evidence/
```

### What to Extract
- [ ] **Score Breakdown**: Which dimensions are weakest? (these are differentiators)
- [ ] **Key Limitations**: Top 3 documented weaknesses
- [ ] **Valid Use Cases**: When does competitor actually make sense?
- [ ] **Evidence Sources**: Where are the documented claims?

### Quick Notes Template
```markdown
**Competitor**: {name}
**Score**: X/59 (Y%, Category Z)

**Top 3 Weaknesses** (lowest dimension scores):
1. {dimension}: {score}/{max} - {why it's weak}
2. {dimension}: {score}/{max} - {why it's weak}
3. {dimension}: {score}/{max} - {why it's weak}

**Valid Use Cases** (be honest):
- When: {scenario where competitor fits}
- Who: {type of org that should consider it}

**Key Evidence**:
- {critical fact with source}
- {competitor admission with URL}
- {third-party research}
```

---

## Step 2: Generate Web Comparison (30-45 min)

### Prompt to Use

```
I need to generate a web comparison for {COMPETITOR} using the 59-point BUA framework.

Context:
- BUA Score: {X/59} ({Y%}, Category {Z})
- Template: templates/WEB_COMPARISON_TEMPLATE.md
- Reference Example: competitors/power-bi-copilot/outputs/web_comparison.md
- Framework Scoring: competitors/{competitor}/evidence/framework_scoring.md

Apply the lessons from Power BI Copilot update (POWER_BI_UPDATE_SUMMARY.md):
1. Tone: Confident, not aggressive - no sarcasm or "failure rate" language
2. Balance: Acknowledge valid competitor use cases honestly
3. Transparency: Include Scoop cost breakdown
4. Evidence: All specific claims have sources

Key differentiators for {COMPETITOR}:
1. {weakness 1 from framework scoring}
2. {weakness 2 from framework scoring}
3. {weakness 3 from framework scoring}

Generate the web comparison following WEB_COMPARISON_TEMPLATE.md structure.
Target length: 5,000-8,000 words.
```

### Generation Options

**Option A: Full Generation (faster)**
- Prompt AI to generate entire comparison in one go
- Good for: Straightforward competitors with standard patterns

**Option B: Phased Execution (better quality)**
- Phase 1: Foundation & Scoop Revolution (35-40K chars)
- Phase 2: Capability Analysis (40-45K chars)
- Phase 3: Business Impact (35-40K chars)
- Phase 4: Consolidation (150K final)
- Good for: Complex competitors or when you want more control

**Recommendation for Tier 1**: Use Option A, review, refine if needed.

---

## Step 3: Quality Check (10-15 min)

### Automated Checks
```bash
# Check score references
grep -c "{X}/59" competitors/{competitor}/outputs/web_comparison.md
# Should be 3-5 instances

# Check category references
grep -c "Category {Z}" competitors/{competitor}/outputs/web_comparison.md
# Should be 3-5 instances

# Check for banned phrases
grep -i "failure rate" competitors/{competitor}/outputs/web_comparison.md
# Should be 0 results (unless technical failure)

grep -i "willing to accept" competitors/{competitor}/outputs/web_comparison.md
# Should be 0 results (sarcastic tone)
```

### Manual Review Checklist

**Scoring & Framework**:
- [ ] BUA score stated as X/59 (Y%, Category Z) consistently
- [ ] Category definition correct (A/B/C/D)
- [ ] Framework explanation mentions 59-point system
- [ ] No references to old 50-point scoring

**Tone & Balance**:
- [ ] No "failure rate" language (unless technical failure)
- [ ] No sarcastic or dismissive language
- [ ] "Consider {Competitor} if" section is respectful
- [ ] Valid competitor use cases acknowledged
- [ ] Confidence without aggression

**Cost & Transparency**:
- [ ] Scoop cost breakdown included
- [ ] All dollar amounts >$1K have sources or methodology
- [ ] Hidden costs section has specific examples
- [ ] 3-year TCO comparison included

**Evidence & Sources**:
- [ ] Competitor's own documentation quoted
- [ ] Third-party research cited (Gartner, analysts, etc.)
- [ ] Customer quotes included
- [ ] URLs provided for key claims

**Technical Accuracy**:
- [ ] Schema evolution section included (universal differentiator)
- [ ] Three-layer AI Data Scientist explained (if ML relevant)
- [ ] Excel formula comparison accurate (150+ functions)
- [ ] Investigation vs single-query distinction clear

---

## Step 4: Finalize & Document (5 min)

### Save Output
```bash
# Create outputs directory if needed
mkdir -p competitors/{competitor}/outputs

# Save web comparison
# (content should be in: competitors/{competitor}/outputs/web_comparison.md)
```

### Update README
Add link to web comparison in competitor README:
```markdown
### Sales Tools
- **[BATTLE_CARD.md](BATTLE_CARD.md)** - Quick reference
- **[outputs/web_comparison.md](outputs/web_comparison.md)** - Complete comparison (NEW)
```

### Update Tracking
```bash
# Run status check
./check_web_comparison_status.sh

# Update WEB_COMPARISON_UPDATE_PLAN.md tracking table
# Change status from ⏳ Planned to ✅ Complete
```

---

## Step 5: Commit (Optional but Recommended)

```bash
git add competitors/{competitor}/outputs/web_comparison.md
git add competitors/{competitor}/README.md
git commit -m "Generate {Competitor} web comparison with 59-point BUA framework

- Score: {X/59} ({Y%}, Category {Z})
- Applied Power BI learnings (improved tone, cost transparency)
- Complete comparison: setup, capabilities, cost, use cases, FAQ
- Target: {tier} priority competitor"
```

---

## Total Time Estimate

| Phase | Time | Notes |
|-------|------|-------|
| Pre-flight check | 5 min | Status script |
| Review research | 10-15 min | Extract key points |
| Generate comparison | 30-45 min | Full generation |
| Quality check | 10-15 min | Automated + manual |
| Finalize & document | 5 min | Save, update tracking |
| **Total** | **60-85 min** | **1-1.5 hours per competitor** |

---

## Common Issues & Solutions

### Issue: "Not enough evidence for specific claims"
**Solution**: Check `competitors/{competitor}/evidence/` for research library. If missing, either:
1. Soften language: "$40K" → "$30K-$50K range"
2. Add methodology: "$40K (based on industry standard rates)"
3. Remove claim if unverifiable

### Issue: "Score seems wrong for competitor"
**Solution**: Review `framework_scoring.md` for detailed rationale. If score truly seems wrong:
1. Check if framework was updated recently
2. Verify evidence supports the score
3. Consult BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md for rubrics
4. Don't change score without re-scoring with evidence

### Issue: "Tone sounds too aggressive"
**Solution**: Apply these replacements:
- "failure" → "low satisfaction" or "limited adoption"
- "willing to accept" → "can accept" or "have tolerance for"
- "Most Damaging" → "Key Consideration" or "Critical Finding"
- Let competitor's own words speak, avoid editorializing

### Issue: "Competitor has valid strengths, how to handle?"
**Solution**: This is GOOD! Acknowledging strengths builds credibility:
- Use "When to Choose {Competitor}" section to be honest
- Frame as trade-offs, not absolute good/bad
- Example: "If you prioritize governance over speed, {Competitor} excels"

---

## Success Criteria

Before marking complete, verify:
- ✅ Web comparison generated (5,000-8,000 words)
- ✅ 59-point BUA score reflected throughout
- ✅ Category correctly stated everywhere
- ✅ Scoop cost transparency included
- ✅ Tone is confident and balanced (not aggressive)
- ✅ All major claims sourced or methodologized
- ✅ Automated checks pass (score refs, no banned phrases)
- ✅ Manual quality checklist complete
- ✅ README updated with link
- ✅ Status tracking updated

---

## Next Competitor After This One

Check priority order:
```bash
./check_web_comparison_status.sh
```

**Tier 1 Priority**:
1. Tableau Pulse → ThoughtSpot → Snowflake Cortex

**Tier 2 Priority**:
4. Domo → Qlik → Zenlytic

**Tier 3 Priority**:
7. Sisense → DataGPT → Tellius → DataChat

---

## Resources

- **Template**: `templates/WEB_COMPARISON_TEMPLATE.md`
- **Example**: `competitors/power-bi-copilot/outputs/web_comparison.md`
- **Framework**: `framework/BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md`
- **Learnings**: `POWER_BI_UPDATE_SUMMARY.md`
- **Full Plan**: `WEB_COMPARISON_UPDATE_PLAN.md`
- **Status Script**: `./check_web_comparison_status.sh`

---

**Ready to start?** Run:
```bash
./check_web_comparison_status.sh
# Pick next from Tier 1
# Follow steps 1-5 above
# Total time: 1-1.5 hours
```