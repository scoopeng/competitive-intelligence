# Manual Research Plan - REAL Data Gathering

## The Problem
- The Python script can't access WebFetch/WebSearch (Claude-only tools)
- Installing web scraping libraries requires setup time
- We need REAL competitive intelligence NOW

## The Solution: Manual Research with Claude Tools

### Priority Competitors (Need Immediate Research)
1. **Power BI Copilot** - Most common competitor
2. **Tableau Pulse** - Enterprise deals
3. **ThoughtSpot** - Major competitor
4. **Domo** - Portal prison narrative

### Research Tasks Per Competitor

#### Phase 1: Evidence Gathering
- [ ] Search for negative reviews on G2, Capterra, Reddit
- [ ] Find actual pricing (including hidden costs)
- [ ] Document technical limitations with sources
- [ ] Capture customer complaints with quotes

#### Phase 2: Technical Analysis
- [ ] Check official documentation for limitations
- [ ] Find architecture constraints
- [ ] Identify integration problems
- [ ] Document ML/AI reality vs marketing

#### Phase 3: BUPAF Scoring
- [ ] Score each dimension with evidence
- [ ] Compare to Scoop capabilities
- [ ] Identify fatal flaws

## Manual Research Process

### For each competitor:
1. Use WebSearch to find reviews and complaints
2. Use WebFetch to get documentation details
3. Save findings in `competitors/[name]/research/REAL_EVIDENCE.md`
4. Update battle cards with verified information
5. Create evidence links in EVIDENCE_VAULT.md

## What to Search For

### Power BI Copilot
```
"Power BI Copilot" problems limitations failures
"Power BI Copilot" "doesn't work" OR "not working" OR "broken"
"Power BI Copilot" pricing "hidden costs" enterprise
site:reddit.com "Power BI Copilot" issues
```

### Tableau Pulse
```
"Tableau Pulse" schema "breaks" OR "broken" metrics
"Tableau Pulse" limitations problems 2024 2025
"Tableau Pulse" vs alternatives comparison
site:community.tableau.com Pulse issues problems
```

### ThoughtSpot
```
ThoughtSpot accuracy "33%" benchmark test
ThoughtSpot pricing "per user" enterprise cost
ThoughtSpot "difficult to use" OR "complex" OR "hard to learn"
site:g2.com ThoughtSpot reviews negative
```

### Domo
```
Domo "portal prison" "can't export" "vendor lock"
Domo pricing "hidden costs" "renewal shock"
Domo limitations "can't do" problems
site:reddit.com Domo expensive "not worth"
```

## Output Format

Each research file should contain:
- **Date**: When researched
- **Sources**: URLs that can be verified
- **Quotes**: Exact customer complaints
- **Evidence**: Screenshots or documentation references
- **Impact**: Business consequences

## Next Steps
1. Start with Power BI Copilot (highest priority)
2. Gather real evidence using WebSearch/WebFetch
3. Save in structured format
4. Move to next competitor
5. Update battle cards with findings