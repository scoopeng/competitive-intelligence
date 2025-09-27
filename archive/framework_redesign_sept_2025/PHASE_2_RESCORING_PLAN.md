# Phase 2: Re-Scoring Execution Plan

**Created**: September 27, 2025
**Goal**: Re-score all 11 competitors with new BUA Framework v2.0
**Timeline**: 2-3 weeks
**Output**: Updated scores + web comparison pages for all competitors

---

## Overview

### What We're Doing
1. **Re-score** each competitor using new 5-dimension framework (Autonomy, Flow, Understanding, Presentation, Data)
2. **Update** all competitor files with new BUA scores (replacing old BUPAF scores)
3. **Generate** comprehensive web comparison pages using WEB_COMPARISON_TEMPLATE.md
4. **Validate** all content passes quality checks

### New Framework Dimensions
| Dimension | What It Measures | Points |
|-----------|------------------|--------|
| Autonomy | Self-service without IT (setup, questions, speed) | 0-10 |
| Flow | Work in existing tools (Excel/Slack), no portal | 0-10 |
| Understanding | Deep insights without analysts (investigation, ML) | 0-10 |
| Presentation | Professional output without designers | 0-10 |
| Data | Handle data ops without engineers (schema evolution) | 0-10 |
| **TOTAL** | **Business User Autonomy** | **0-50** |

---

## Competitor Priority Order

Based on deal frequency and research completeness:

### Tier 1: High Priority (Complete First)
1. **Power BI Copilot** - ✅ Already scored (14/50) + web comparison complete
2. **Tableau Pulse** - Research 70% complete, frequent competitor
3. **ThoughtSpot** - Research 25% complete, needs deep dive
4. **Domo** - Research 70% complete, established competitor

### Tier 2: Medium Priority
5. **Snowflake Cortex** - Research 100% complete, enterprise deals
6. **DataGPT** - Research 50% complete, emerging competitor
7. **Zenlytic** - Research 100% complete, niche competitor

### Tier 3: Lower Priority (But Complete All)
8. **Tellius** - Research 40% complete, analyst workbench
9. **Sisense** - Research 30% complete, marketing mirage
10. **Qlik Insight Advisor** - Research 40% complete, legacy platform
11. **DataChat** - Research 100% complete, vaporware

---

## Re-Scoring Process (Per Competitor)

### Step 1: Review Existing Evidence (30 min)
**Files to Review**:
- `competitors/[name]/RESEARCH_CHECKLIST.md` (if exists)
- `competitors/[name]/BATTLE_CARD.md`
- `competitors/[name]/research/*.md` files
- `competitors/[name]/evidence/*.md` files

**What to Extract**:
- Setup time and IT requirements
- Tool integration (Excel, Slack, PowerPoint)
- Investigation capabilities (single vs multi-pass)
- ML capabilities (algorithms, explainability)
- Schema evolution handling
- Customer quotes about limitations

### Step 2: Score Each Dimension (45 min)

Use detailed rubrics from `framework/BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md`:

**Autonomy (0-10)**:
- Setup (0-4): Connection time, prerequisites, IT involvement
- Questions (0-3): NL quality, query flexibility, training required
- Speed (0-3): Time to first insight, implementation timeline

**Flow (0-10)**:
- Integration (0-4): Excel/Slack/PowerPoint/Mobile native support
- Portal (0-3): Portal requirement vs tool-native
- Interface (0-3): NL quality, learning curve, simplicity

**Understanding (0-10)**:
- Investigation (0-4): Single query vs multi-pass, hypothesis testing
- ML (0-3): Pattern discovery, algorithms, business translation
- Explanation (0-3): Plain English insights, confidence scoring

**Presentation (0-10)**:
- Visuals (0-3): Chart quality, customization, intelligence
- Brand (0-4): Logo detection, color schemes, consistency
- Speed (0-3): PowerPoint generation, formats, automation

**Data (0-10)**:
- Connections (0-2): Number and ease of connectors
- Schema (0-4): Evolution handling, IT dependency
- Prep (0-2): Data cleaning, transformation capabilities
- Writeback (0-2): CRM/operational system integration

### Step 3: Document Scoring Rationale (30 min)

Create `competitors/[name]/evidence/framework_scoring_v2.md`:

```markdown
# BUA Framework Scoring v2.0

**Competitor**: [Name]
**Date Scored**: [Date]
**Scored By**: [Name]
**Total Score**: X/50 (Category [A/B/C/D])

---

## Dimension 1: Autonomy (X/10)

### Setup (X/4)
**Score**: X/4
**Evidence**: [Specific proof - setup time, prerequisites, IT requirements]
**Source**: [URL + date accessed]

### Questions (X/3)
**Score**: X/3
**Evidence**: [NL support quality, query flexibility, constraints]
**Source**: [URL + date accessed]

### Speed (X/3)
**Score**: X/3
**Evidence**: [Time from signup to first insight, training needed]
**Source**: [URL + date accessed]

**Total Autonomy**: X/10

---

[Continue for all 5 dimensions...]

---

## Score Category

**Total**: X/50
**Category**: [A/B/C/D]

- Category A (40-50): True Self-Service
- Category B (25-39): Analyst Workbench
- Category C (15-24): IT Platform
- Category D (0-14): Dashboard Tool

## Key Differentiators vs Scoop (45/50)

1. **[Dimension]**: Scoop [X/10] vs [Competitor] [Y/10] - [Why gap exists]
2. **[Dimension]**: Scoop [X/10] vs [Competitor] [Y/10] - [Why gap exists]
3. **[Dimension]**: Scoop [X/10] vs [Competitor] [Y/10] - [Why gap exists]
```

### Step 4: Update Competitor Files (45 min)

**4a. Update BATTLE_CARD.md**:
- Replace BUPAF score with BUA score (header + fatal flaws section)
- Update score breakdown table with new 5 dimensions
- Refresh any outdated evidence

**4b. Update README.md** (if exists):
- Replace BUPAF score with BUA score
- Update quick summary section
- Add link to framework_scoring_v2.md

**4c. Update other research files**:
- Find/replace BUPAF → BUA throughout folder
- Update any score references

### Step 5: Generate Web Comparison Page (3-4 hours)

Use `templates/WEB_COMPARISON_TEMPLATE.md`:

**Required Sections** (5,000-7,000 words):
1. Executive Comparison (800 words)
2. Capability Deep Dive (3,000 words)
3. Cost Analysis (1,200 words)
4. Use Cases & Scenarios (600 words)
5. Evidence & Sources (400 words)
6. FAQ (800 words) - **Must include BUA framework FAQ**
7. Next Steps (200 words)

**Output**: `competitors/[name]/outputs/web_comparison.md`

**Quality Checks**:
- [ ] All 7 sections present
- [ ] BUA Score referenced (not BUPAF)
- [ ] BUA framework FAQ included
- [ ] Three-Layer AI referenced
- [ ] 150+ Excel functions mentioned
- [ ] Investigation Engine explained
- [ ] Schema Evolution section included
- [ ] Evidence-based (sources cited)
- [ ] Professional tone
- [ ] 5,000-7,000 word target met

### Step 6: Quality Validation (30 min)

Run through `RESEARCH_QA_CHECKLIST.md`:
- [ ] All claims have sources
- [ ] No speculation without evidence
- [ ] Dates on all URLs
- [ ] No inflated numbers
- [ ] Professional tone maintained
- [ ] BUA framework properly explained

**Total Time Per Competitor**: 6-7 hours

---

## Execution Workflow

### Week 1: Tier 1 Competitors
**Mon**: Tableau Pulse (re-score + web comparison)
**Tue-Wed**: ThoughtSpot (may need additional research)
**Thu**: Domo (re-score + web comparison)
**Fri**: Review and quality check

### Week 2: Tier 2 Competitors
**Mon**: Snowflake Cortex
**Tue**: DataGPT
**Wed**: Zenlytic
**Thu**: Review and quality check
**Fri**: Buffer/catch-up

### Week 3: Tier 3 Competitors
**Mon**: Tellius
**Tue**: Sisense
**Wed**: Qlik
**Thu**: DataChat
**Fri**: Final review of all 11 competitors

---

## Deliverables Checklist

For each of 11 competitors:
- [ ] `evidence/framework_scoring_v2.md` created
- [ ] BATTLE_CARD.md updated (BUPAF→BUA)
- [ ] README.md updated (BUPAF→BUA) if exists
- [ ] All research files updated (BUPAF→BUA)
- [ ] `outputs/web_comparison.md` generated
- [ ] Quality validation passed

**Final Deliverable**: 11 re-scored competitors with comprehensive web comparisons

---

## Success Criteria

✅ All 11 competitors scored with new BUA Framework v2.0
✅ All BUPAF references replaced with BUA in competitor folders
✅ All competitors have comprehensive web comparison pages
✅ All content passes RESEARCH_QA_CHECKLIST.md
✅ Scores are defensible with documented evidence
✅ Ready for website publication and sales enablement

---

## Notes

- **Power BI Copilot**: Already complete (14/50 score validated)
- **Research Gaps**: May need additional research for some competitors (ThoughtSpot, Sisense, Qlik)
- **Parallel Work**: Can generate web comparisons in parallel with scoring if evidence is complete
- **Template Usage**: Use WEB_COMPARISON_TEMPLATE.md (not BUA_COMPARISON_TEMPLATE.md) for all web pages