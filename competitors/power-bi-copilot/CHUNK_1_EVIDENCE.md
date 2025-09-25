# CHUNK 1: Evidence Gathering - Power BI Copilot

## YOUR MISSION
You are a competitive intelligence researcher. Your job is to gather COMPREHENSIVE evidence about Power BI Copilot's problems, limitations, and customer complaints. This is your ONE PASS to gather everything - be thorough.

## CONTEXT
- **Competitor**: Power BI Copilot (Microsoft's AI assistant for Power BI)
- **Our Product**: Scoop (business analytics that actually works)
- **Goal**: Find every problem, limitation, and complaint about Power BI Copilot
- **Output**: Save everything in `research/evidence.md`

## EXECUTION PLAN

### Step 1: Search for Problems & Limitations
Execute these searches using WebSearch:
```
1. "Power BI Copilot problems limitations failures 2024 2025"
2. "Power BI Copilot not working broken issues"
3. "Power BI Copilot nondeterministic inconsistent random outputs"
4. "Power BI Copilot hallucination wrong data misleading incorrect"
5. "Power BI Copilot accuracy reliability trust issues"
```

For EACH search:
- Read through results carefully
- Extract specific problems with quotes
- Note the source URL
- Look for patterns across complaints

### Step 2: Search for Pricing & Licensing Issues
Execute these searches:
```
6. "Power BI Copilot pricing cost expensive"
7. "Power BI Copilot licensing requirements F64 P1"
8. "Power BI Copilot hidden costs enterprise pricing"
9. "Power BI Premium capacity pricing calculator"
```

Extract:
- Exact pricing tiers
- Hidden costs
- Licensing confusion
- Customer shock stories

### Step 3: Mine Review Sites
Execute these searches:
```
10. "site:g2.com Power BI reviews negative problems limitations"
11. "site:capterra.com Power BI cons disadvantages"
12. "site:trustradius.com Power BI issues complaints"
```

Look for:
- Star ratings (especially 1-3 stars)
- Specific customer quotes about problems
- Recurring themes in complaints
- Enterprise customer issues

### Step 4: Search Communities & Forums
Execute these searches:
```
13. "site:reddit.com Power BI Copilot doesn't work help"
14. "site:community.fabric.microsoft.com Copilot error failed"
15. "site:stackoverflow.com Power BI Copilot issues"
16. "site:answers.microsoft.com Power BI Copilot not working"
```

Find:
- Technical problems users face
- Unanswered questions
- Workarounds that don't work
- Frustration levels

### Step 5: Check Official Documentation
Use WebFetch on these URLs:
```
17. https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction
18. https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-enable-power-bi
19. https://learn.microsoft.com/en-us/fabric/get-started/copilot-fabric-overview
```

Look for:
- Admitted limitations
- Regional restrictions
- Technical constraints
- Prerequisites and requirements

### Step 6: Competitor Comparisons
Execute these searches:
```
20. "Power BI Copilot vs ChatGPT comparison"
21. "Power BI Copilot vs Tableau Pulse"
22. "Power BI Copilot alternatives better than"
```

Find:
- Where Power BI loses
- What others do better
- Migration stories

## OUTPUT FORMAT

Create/update `research/evidence.md` with this structure:

```markdown
# Power BI Copilot - Evidence Collection
## Generated: [timestamp]
## Searches Executed: [count]

## 1. CRITICAL PROBLEMS & LIMITATIONS

### [Problem Category 1]
**Finding**: [Specific issue]
**Evidence**: "[Direct quote]"
**Source**: [URL]
**Impact**: [Business impact]

### [Problem Category 2]
...

## 2. PRICING & LICENSING ISSUES

### Actual Costs
- F64 Capacity: $[amount]/month
- P1 Premium: $[amount]/month
- Hidden costs: [list]
**Source**: [URL]

### Licensing Confusion
**Finding**: [Specific issue]
**Customer Quote**: "[Direct quote]"
**Source**: [URL]

## 3. CUSTOMER COMPLAINTS

### From G2.com
**Rating**: [X.X/5 stars]
**Quote**: "[Negative review quote]"
**Reviewer**: [Title/Company if available]
**Source**: [URL]

### From Reddit
**User Complaint**: "[Quote]"
**Context**: [What they were trying to do]
**Source**: [URL]

## 4. TECHNICAL LIMITATIONS

### Official Limitations
**From Microsoft Docs**:
- [Limitation 1]
- [Limitation 2]
**Source**: [URL]

### Community-Discovered Issues
**Issue**: [Description]
**Workaround**: [None/Complex/Doesn't work]
**Source**: [URL]

## 5. COMPARISON FAILURES

### vs ChatGPT
**Power BI Can't**: [Specific capability]
**ChatGPT Can**: [How it does it better]
**Source**: [URL]

## SUMMARY STATISTICS
- Total Problems Found: [count]
- Critical/Blocking Issues: [count]
- Customer Complaints: [count]
- Source URLs Collected: [count]
- Direct Quotes Captured: [count]
```

## SUCCESS CRITERIA
You MUST achieve ALL of these:
- [ ] Execute at least 20 searches
- [ ] Find at least 25 distinct problems/limitations
- [ ] Collect at least 30 source URLs
- [ ] Capture at least 15 direct customer quotes
- [ ] Document exact pricing information
- [ ] Find at least 5 technical limitations from official docs
- [ ] Include at least 10 Reddit/forum complaints

## IMPORTANT NOTES
1. Be THOROUGH - this is our one shot at evidence gathering
2. Include EXACT quotes, not paraphrasing
3. Every claim needs a SOURCE URL
4. Focus on PROBLEMS, not features
5. If you find something damning, dig deeper
6. Save everything - we'll analyze later

## COMPLETION
When done:
1. Verify all success criteria are met
2. Save the file
3. Output: "CHUNK 1 COMPLETE: [X] problems found, [Y] sources collected"

## TIME ESTIMATE
This should take 20-30 minutes to do thoroughly. Take your time.