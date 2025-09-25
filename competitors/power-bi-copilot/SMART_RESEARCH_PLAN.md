# Smart Research Plan - Power BI Copilot

## Pass 1: Comprehensive Evidence Gathering (30 minutes)

### Objective
Gather ALL evidence about Power BI Copilot limitations in one comprehensive research session.

### Search Queries to Execute
1. "Power BI Copilot problems limitations 2024 2025"
2. "Power BI Copilot nondeterministic outputs inconsistent results"
3. "Power BI Copilot hallucination wrong data misleading"
4. "Power BI Copilot pricing hidden costs enterprise"
5. "Power BI Copilot vs ChatGPT comparison limitations"
6. "site:g2.com Power BI negative reviews complaints"
7. "site:reddit.com Power BI Copilot doesn't work issues"
8. "site:community.fabric.microsoft.com Copilot problems"
9. "Power BI Copilot GPU throttling performance"
10. "Power BI Copilot data preparation requirements"

### Documentation to Fetch
- Microsoft official Copilot documentation
- Pricing pages (both Power BI and Fabric)
- Community forum top issues
- Expert reviews and benchmarks

### Output Structure
Save ALL findings in `research/comprehensive_findings.md`:
```markdown
# Comprehensive Power BI Copilot Research
## Date: [timestamp]

### 1. Licensing & Pricing Issues
[All findings with sources]

### 2. Technical Limitations
[All findings with sources]

### 3. Accuracy & Reliability Problems
[All findings with sources]

### 4. Customer Complaints
[Direct quotes with sources]

### 5. Comparison to Alternatives
[How it fails vs ChatGPT, Claude, etc]
```

### Success Criteria
- [ ] At least 20 distinct problems documented
- [ ] At least 30 source URLs collected
- [ ] At least 10 customer quotes captured
- [ ] Pricing fully documented
- [ ] Technical limitations verified

---

## Pass 2: Analysis & Battle Card Update (15 minutes)

### Objective
Analyze findings and create sales-ready documentation.

### Tasks
1. Read `research/comprehensive_findings.md`
2. Score BUPAF dimensions based on evidence
3. Update BATTLE_CARD.md with:
   - Top 5 fatal flaws
   - Pricing comparison
   - Key differentiators vs Scoop
4. Create `outputs/sales_talking_points.md`
5. Update EVIDENCE_VAULT.md with all sources

### Success Criteria
- [ ] BUPAF scored with evidence
- [ ] Battle card updated
- [ ] Sales points documented
- [ ] All sources in vault

---

## Execution Instructions

### For Pass 1:
```bash
claude --print --timeout 1800 "
Read SMART_RESEARCH_PLAN.md Pass 1 section.
Execute ALL searches listed.
Fetch documentation.
Save comprehensive findings.
Be thorough - this is our ONE chance to gather everything.
Output 'PASS 1 COMPLETE' when done.
"
```

### For Pass 2:
```bash
claude --print --timeout 900 "
Read SMART_RESEARCH_PLAN.md Pass 2 section.
Read research/comprehensive_findings.md.
Complete all analysis tasks.
Output 'PASS 2 COMPLETE' when done.
"
```

## Why This Works Better

1. **Comprehensive**: Gets everything in 2 passes vs 50 steps
2. **Context Preserved**: Each pass has full context
3. **Efficient**: 45 minutes total vs hours
4. **Quality**: Deep research, not surface level
5. **Clear Success**: Defined criteria to check