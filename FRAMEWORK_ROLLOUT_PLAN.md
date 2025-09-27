# Framework Rollout Plan - Business User Empowerment v2.0

**Created**: September 27, 2025
**Target Completion**: October 15, 2025 (3 weeks)
**Status**: Planning

---

## What Changed

### Old BUPAF → New Framework
- **Old**: Browse, Understand, Predict, Act, Fix (overlap, missing moats)
- **New**: Autonomy, Flow, Understanding, Presentation, Data (distinct, covers all moats)

### Key Improvements
1. All 5 dimensions are distinct (no overlap)
2. Covers all 5 Scoop moats explicitly
3. Clear pattern: removes dependencies on IT/portal/analyst/designer/engineer
4. Better measures holistic business user empowerment

---

## Execution Plan (3 Phases)

### Phase 1: Update Templates & Documentation (Week 1)
**Goal**: All templates and foundational docs reflect new framework

#### Tasks
1. **Update BUPAF_COMPARISON_TEMPLATE.md**
   - Replace old framework explanation with new 5 dimensions
   - Update Section 1 (BUPAF scoring table)
   - Update Section 2 dimension selection guidance
   - Add scoring rubrics for each dimension
   - **Estimated time**: 2-3 hours

2. **Update CLAUDE.md**
   - Reference new framework location
   - Update any BUPAF mentions
   - **Estimated time**: 30 minutes

3. **Update METHODOLOGY.md**
   - Replace old BUPAF explanation with new framework
   - Link to framework/BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md
   - **Estimated time**: 1 hour

4. **Update README.md**
   - Update framework references
   - Link to new framework document
   - **Estimated time**: 30 minutes

**Phase 1 Deliverable**: All templates ready to use with new framework

---

### Phase 2: Re-Score Priority Competitors (Week 2)
**Goal**: Top 4 competitors scored with new framework

#### Priority Order (Based on Deal Frequency)
1. **Power BI Copilot**
2. **Tableau Pulse**
3. **ThoughtSpot**
4. **Domo**

#### Tasks Per Competitor
For each competitor:
1. **Score using new rubrics** (1-2 hours)
   - Review existing evidence
   - Apply 0-10 scoring for each dimension
   - Document rationale in evidence folder

2. **Update BATTLE_CARD.md** (30 minutes)
   - Replace old BUPAF score with new score
   - Update dimension breakdown table
   - Refresh key evidence

3. **Update README.md** (15 minutes)
   - Update quick summary with new score
   - Update key differentiators section

**Phase 2 Deliverable**: Top 4 competitors scored and documented

#### Detailed Scoring Process

**Step 1: Evidence Review**
- Read existing research (RESEARCH_CHECKLIST.md, evidence/*)
- Identify evidence for each dimension
- Note gaps (may need additional research)

**Step 2: Apply Detailed Rubrics**
- Use scoring rubrics from BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md
- Score each sub-component (e.g., Autonomy = Setup + Question Independence + Speed)
- Document specific evidence for each sub-component score

**Step 3: Document Rationale**
Create `competitors/[name]/evidence/framework_scoring.md`:
```markdown
# Business User Empowerment Framework Scoring

**Competitor**: [Name]
**Date Scored**: [Date]
**Total Score**: X/50 (Category [A/B/C/D])

---

## Dimension 1: Autonomy (X/10)

### Component A: Self-Service Setup (X/4)
**Score**: X/4
**Evidence**: [Specific proof of setup process, time required, IT involvement]
**Source**: [URLs]

### Component B: Question Independence (X/3)
**Score**: X/3
**Evidence**: [NL support, query flexibility, constraints]
**Source**: [URLs]

### Component C: Speed to Value (X/3)
**Score**: X/3
**Evidence**: [Time from signup to first insight, training required]
**Source**: [URLs]

**Total Autonomy**: X/10

---

## Dimension 2: Flow (X/10)

### Component A: Native Integration (X/4)
**Score**: X/4
**Evidence**: [Slack/Excel/Mobile/PPT integration details]
**Source**: [URLs]

### Component B: No Portal Prison (X/3)
**Score**: X/3
**Evidence**: [Portal requirement or lack thereof]
**Source**: [URLs]

### Component C: Interface Simplicity (X/3)
**Score**: X/3
**Evidence**: [NL quality, learning curve, technical requirements]
**Source**: [URLs]

**Total Flow**: X/10

---

[Continue for all 5 dimensions with sub-components]
```

---

### Phase 3: Generate BUPAF Comparison Pages (Week 3)
**Goal**: New focused BUPAF comparison pages for top 4 competitors

#### Tasks Per Competitor
1. **Generate BUPAF comparison page** (2-3 hours)
   - Use BUPAF_COMPARISON_TEMPLATE.md
   - Target: 2,000-3,000 words
   - Focus on 2-3 dimensions where competitor fails worst
   - Emphasize chat/agentic analytics positioning
   - **Output**: `competitors/[name]/outputs/bupaf_comparison.md`

2. **Quality check** (30 minutes)
   - Verify all evidence sourced
   - Check tone (empathetic, educational, not preachy)
   - Ensure business user language (not technical)

3. **Update competitor README** (15 minutes)
   - Add link to new BUPAF comparison
   - Update "Files in This Folder" section

**Phase 3 Deliverable**: 4 focused BUPAF comparison pages ready for outbound marketing

---

## Rollout Schedule

### Week 1 (Sep 28 - Oct 4): Templates & Documentation
- **Mon-Tue**: Update BUPAF_COMPARISON_TEMPLATE.md
- **Wed**: Update CLAUDE.md, METHODOLOGY.md, README.md
- **Thu-Fri**: Review and test template with example

### Week 2 (Oct 5 - Oct 11): Re-Score Competitors
- **Mon**: Power BI Copilot scoring
- **Tue**: Tableau Pulse scoring
- **Wed**: ThoughtSpot scoring
- **Thu**: Domo scoring
- **Fri**: Review all scores, ensure consistency

### Week 3 (Oct 12 - Oct 18): Generate Comparison Pages
- **Mon**: Power BI Copilot BUPAF comparison
- **Tue**: Tableau Pulse BUPAF comparison
- **Wed**: ThoughtSpot BUPAF comparison
- **Thu**: Domo BUPAF comparison
- **Fri**: Quality check all pages, final review

---

## Success Criteria

### Phase 1 Complete When:
- [ ] BUPAF_COMPARISON_TEMPLATE.md fully updated with new framework
- [ ] All root documentation references new framework
- [ ] Template tested with one example (Power BI)

### Phase 2 Complete When:
- [ ] All 4 priority competitors scored with rationale documented
- [ ] All 4 battle cards updated with new scores
- [ ] Scoring methodology is consistent across competitors

### Phase 3 Complete When:
- [ ] 4 focused BUPAF comparison pages generated (2-3K words each)
- [ ] All pages pass quality check
- [ ] Sales team has new outbound marketing content

---

## Remaining Competitors (Phase 4 - Future)

After top 4, score and create BUPAF comparisons for:
5. **Snowflake Cortex** (heavy IT dependency angle)
6. **Zenlytic** (semantic model maintenance)
7. **Databricks AI/BI** (technical complexity)
8. **Sigma** (spreadsheet interface but limited depth)
9. **Hex** (analyst tool, not business user)
10. **Mode** (technical, SQL-required)
11. **Looker** (semantic model nightmare)

**Timeline**: 1-2 competitors per week, complete by end of November

---

## Considerations & Risks

### Potential Issues
1. **Scoring consistency**: Need to ensure rubrics applied uniformly
   - **Mitigation**: Document rationale, review all scores before finalizing

2. **Evidence gaps**: May discover we need more research on some dimensions
   - **Mitigation**: Note gaps, conduct targeted research as needed

3. **Template iteration**: First BUPAF comparison may reveal template improvements
   - **Mitigation**: Update template as we learn, regenerate if needed

### Open Questions
1. Should we archive old BUPAF references or update in place?
   - **Recommendation**: Update in place for active docs, archive old framework doc

2. Do we need to update web_comparison.md files with new scores?
   - **Recommendation**: No - web comparisons are comprehensive, BUPAF comparisons are focused. Keep separate.

3. Should we create a migration guide explaining old → new mapping?
   - **Recommendation**: Yes - add section to BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md

---

## Resources Needed

### Time Estimate
- **Phase 1**: 5-6 hours (templates & docs)
- **Phase 2**: 10-12 hours (4 competitors × 2.5 hours)
- **Phase 3**: 12-16 hours (4 competitors × 3-4 hours)
- **Total**: 27-34 hours over 3 weeks

### People
- **Primary**: Claude Code (execution)
- **Review**: User (direction, approval, quality check)

### Tools
- Templates: BUPAF_COMPARISON_TEMPLATE.md
- Framework: BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md
- Evidence: Existing research in competitors/*/evidence/

---

## Communication Plan

### Internal
- **Week 1 end**: Share updated framework document with team
- **Week 2 end**: Share new competitor scores
- **Week 3 end**: Share BUPAF comparison pages for review

### External (Future)
- BUPAF comparison pages can be used for:
  - LinkedIn posts (dimension-specific insights)
  - Email campaigns (targeted by competitor)
  - Sales conversations (framework-based positioning)
  - Blog posts (thought leadership on business user empowerment)

---

## Next Immediate Actions

1. **Start Phase 1**: Update BUPAF_COMPARISON_TEMPLATE.md
2. **Test template**: Generate Power BI Copilot BUPAF comparison as proof of concept
3. **Iterate**: Refine template based on first generation
4. **Proceed**: Continue with remaining Phase 1 tasks

---

**Plan Owner**: Competitive Intelligence Project
**Review Date**: October 1, 2025 (after Phase 1 complete)
**Last Updated**: September 27, 2025