# Competitive Intelligence Research Guide

**Purpose**: Deep methodology and thinking for thorough competitive analysis  
**Note**: START_HERE.md has the quick-start version. This is for when you need depth.

## Core Philosophy

**We're building a competitive intelligence library that:**
1. Proves most "AI analytics" are fake (just chatbots on dashboards)
2. Shows where real competitors have limitations
3. Provides evidence-based ammunition for sales
4. Enables credible competitive content with source attribution
5. Identifies exactly where and why Scoop wins

**Key Principles:**
- Truth over marketing (what products ACTUALLY do)
- Evidence everything (screenshots are gold)
- Source attribution (every claim traceable)
- Focus on user reality (not vendor claims)
- Think sales enablement (how does this help win?)

## Research Methodology

### For Each Competitor: The Deep Dive

#### 1. Initial Reconnaissance (45 min)
**Objective**: Understand their positioning and claims

**Website Analysis:**
- Homepage - Screenshot main value props
- Product pages - What do they claim to do?
- About/Company - Funding, size, focus
- Customers - Logos, case studies, industries
- Blog/Resources - Recent announcements, priorities

**Key Questions:**
- What do they claim to be?
- Who do they target?
- What's their core message?
- How do they position vs competition?

#### 2. Documentation Investigation (1 hour)
**Objective**: Find the truth behind marketing

**Documentation Deep Dive:**
- Getting started guide - How complex really?
- Feature documentation - What's actually there?
- Admin guides - IT requirements revealed
- API docs - Integration reality
- Training/Certification - Skills actually needed

**Red Flags to Find:**
- No mention of algorithms = no real AI
- "Contact sales for setup" = complex/expensive
- Extensive prerequisites = not self-service
- Missing capabilities = opportunity for Scoop

#### 3. Pricing Intelligence (30 min)
**Objective**: Understand true total cost

**Pricing Research:**
- Published pricing (screenshot everything)
- Tier limitations (users, data, features)
- Hidden requirements (parent products needed?)
- Implementation costs (professional services?)
- Training costs (certification required?)

**TCO Calculation:**
- License fees
- Implementation services
- Training/certification
- Maintenance/support
- Hidden technical requirements

#### 4. Demo/Video Analysis (45 min)
**Objective**: See the product reality

**Video Research:**
- Official demos - What do they actually show?
- User tutorials - How hard is it really?
- Conference talks - What do they emphasize?
- Webinars - Live Q&A reveals limitations

**Screenshot Key Moments:**
- Actual interface (not mockups)
- Setup process complexity
- Query interfaces
- Result limitations
- Error messages

#### 5. User Reality Mining (1 hour)
**Objective**: Find what users actually experience

**Review Sites:**
- G2 - Filter by most recent, most critical
- Capterra - Look for detailed reviews
- TrustRadius - Often more technical
- Gartner Peer Insights - Enterprise reality

**Community Research:**
- Reddit - Search "[competitor] problems"
- Stack Overflow - Technical issues
- Official forums - Common complaints
- LinkedIn - User posts/complaints

**Key Patterns:**
- Setup took longer than promised
- Requires more technical skill
- Hidden costs discovered
- Features don't work as advertised
- Performance issues at scale

#### 6. Competitive Analysis (45 min)
**Objective**: Position Scoop to win

**Capability Comparison:**
- Create feature matrix vs Scoop
- Identify missing capabilities
- Document technical requirements
- Calculate time to value difference
- Note integration limitations

**Win/Loss Scenarios:**
- Where they might win (be honest)
- Where Scoop clearly wins
- Neutral territories
- How to flip their strengths

**Counter-Positioning:**
- If they claim X, we show Y
- Their complexity vs our simplicity
- Their IT project vs our instant value
- Their dashboard prison vs our conversations

## Evidence Collection Standards

### Screenshot Requirements

**Must Capture:**
1. Homepage hero/claims
2. Pricing page (FULL page, all tiers)
3. Product interface (actual, not marketing)
4. Setup/configuration screens
5. Documentation showing complexity
6. User reviews (especially negative)
7. Forum posts about problems
8. Comparison charts they publish

**Naming Convention:**
```
[competitor]-[content]-[date].png
tableau-pulse-pricing-2025-01-28.png
tableau-pulse-setup-complexity-2025-01-28.png
```

### Source Documentation Standards

**For EVERY source you analyze, create an individual document that:**

1. **Captures ALL Key Content**
   - Every significant claim, feature, limitation
   - Specific numbers, pricing, requirements
   - Technical details AND business implications
   - Both positive and negative findings
   - Direct quotes for controversial/important claims

2. **Provides Analytical Synthesis**
   - What does this mean for business users?
   - What are the hidden implications?
   - How does this compare to their marketing?
   - What patterns are emerging?
   - What's missing or suspicious?

3. **Enables Verification**
   - Include enough specific quotes/details to verify
   - Note page sections or timestamps for video
   - Flag anything that needs screenshot evidence
   - Make it easy to fact-check your analysis

4. **Quality Standard**
   - Someone reading your source doc should learn everything important from that source
   - If they check the original, they should find NO significant missed insights
   - Short is fine if complete; long is fine if needed
   - Thoroughness trumps everything

**Example Source Document Structure:**
```markdown
# [Source Title] - [Company] Analysis
**URL**: [full URL]
**Type**: [Official Docs/Review/Forum/Video/etc]
**Date Accessed**: YYYY-MM-DD

## Key Findings Summary
[2-3 sentence overview of most important discoveries]

## Detailed Analysis

### Technical Capabilities (or relevant section)
- [Specific capability claims with quotes]
- [What's actually delivered vs marketed]
- [Hidden limitations discovered]

### Business User Experience (or relevant section)
- [Specific barriers or enablers]
- [Time to value realities]
- [Skill requirements]

### Pricing/Costs (if mentioned)
- [All specific numbers]
- [Hidden costs revealed]
- [Licensing complexities]

### Red Flags/Concerns
- [What they're not saying]
- [Contradictions found]
- [Warning signs]

### Notable Quotes
> "[Exact quote that proves key point]" - Context

### Evidence Needed
- [ ] Screenshot of [specific thing]
- [ ] Video timestamp of [claim]

### Cross-Reference Notes
- Contradicts [other source] which claims...
- Confirms pattern seen in [other source]
```

**Remember**: The goal is analytical completeness. Every source document should be thorough enough that you never need to revisit the original source, but concise enough to be useful. Focus on insights that matter for competitive positioning.

## Tier-Specific Research Focus

### Tier 1: "AI Pretenders"
**Goal**: Expose the fake AI

**Focus Areas:**
- Prove no real ML/AI capabilities
- Show it's just NL-to-SQL or alerts
- Document IT complexity
- Highlight missing capabilities
- Show dashboard dependence

**Key Evidence:**
- No mention of algorithms
- No prediction capabilities
- No pattern discovery
- Requires existing reports
- Can't answer "why"

### Tier 3: "Real Competition"
**Goal**: Find limitations and position to win

**Focus Areas:**
- Understand actual ML capabilities
- Document implementation complexity
- Find scaling limitations
- Identify missing features
- Calculate true TCO

**Key Evidence:**
- Implementation timeline reality
- Technical team requirements
- Where their AI breaks down
- Customer frustrations
- Price points that shock

## Folder Structure for Source Documentation

### Required Organization (CONSISTENT ACROSS ALL COMPETITORS)

**IMPORTANT**: Only create folders when you have content. Never create empty directories.

```
/competitive-intelligence/
└── [tier-folder]/
    └── [competitor-name]/
        ├── README.md                 # Final competitive analysis
        ├── sources/                  # All source documentation
        │   ├── research-summary-YYYY-MM-DD.md  # Overall findings
        │   ├── research-index.md     # Index of all sources analyzed
        │   └── [source-specific-files].md
        └── evidence/                 # Only if screenshots/videos exist
```

**Source File Naming Convention**:
```
[source-type]-[specific-topic]-YYYY-MM-DD.md

Examples:
official-homepage-analysis-2025-01-28.md
official-pricing-analysis-2025-01-28.md
community-reddit-complaints-2025-01-28.md
review-g2-user-feedback-2025-01-28.md
technical-setup-complexity-2025-01-28.md
```

### Source Index File
Each competitor should have a `research-index.md` that tracks:
```markdown
# Tableau Pulse Research Index
**Last Updated**: 2025-01-28
**Total Sources Analyzed**: 24

## Official Sources (6)
- [x] Homepage and marketing materials
- [x] Official documentation (setup, features, API)
- [x] Pricing pages and calculators
- [x] Case studies and customer stories
- [ ] Webinar recordings
- [ ] Conference presentations

## Review Sites (5)
- [x] G2 reviews (47 reviews analyzed)
- [x] Capterra reviews (23 reviews analyzed)
- [ ] Gartner Peer Insights
...

## Community Sources (8)
- [x] Tableau Community Forum (15 relevant threads)
- [x] Reddit discussions (r/tableau, r/analytics)
...

## Technical Analysis (5)
- [x] Video demos and tutorials
- [x] Technical blog posts
...
```

## Output Templates

### Research Summary Format
```markdown
# [Competitor] - The Reality

## What They Say They Are:
"AI-powered analytics platform that [claim]"

## What They Actually Are:
[Reality based on research]

## Where Scoop Wins:
1. [Advantage 1] - They need X, we need zero
2. [Advantage 2] - They take weeks, we take minutes
3. [Advantage 3] - They cost $$$, we cost $$

## Evidence:
- [Screenshot 1]: Shows complexity
- [Screenshot 2]: Proves no real AI
- [Review Quote]: "It took 6 months to implement"
```

### Sales Battle Card Format
```markdown
# Quick Win: Scoop vs [Competitor]

## Discovery Questions:
1. "How long did implementation take?"
2. "Do you need IT support for queries?"
3. "Can it discover insights you didn't ask for?"

## Red Flags They'll Mention:
- "We need dashboards first"
- "IT handles the setup"
- "We're still in implementation"

## Transition to Scoop:
"What if you could just ask questions in Slack and get answers immediately?"

## Proof Points:
- No dashboards needed
- 30-second setup
- Real AI that discovers
```

## Quality Checklist

**Before Marking Complete:**
- [ ] 15+ screenshots collected
- [ ] 20+ sources documented
- [ ] Pricing fully understood (including hidden)
- [ ] Setup complexity documented
- [ ] User frustrations captured
- [ ] Missing capabilities listed
- [ ] Win scenarios clear
- [ ] Counter-positioning ready
- [ ] Evidence organized and backed up

## Research Hacks

### Quick Wins:
1. **Pricing = "Contact Us"** = Expensive enterprise
2. **No algorithm mentions** = No real AI
3. **"Prerequisites" section** = Complex setup
4. **Certification program** = Not self-service
5. **Partner requirements** = Hidden costs

### Time Savers:
- Start with user complaints (reveals truth faster)
- Video demos show reality better than docs
- Job postings reveal technical requirements
- Support forums expose common issues
- Recent reviews more accurate than old ones

### Evidence Goldmines:
- Reddit: Unfiltered user reality
- YouTube comments: Real user experiences
- LinkedIn: Professional complaints
- G2 compare pages: Side-by-side features
- Conference talks: Live Q&A reveals limits

## The End Game

**We're Building:**
1. Proof that most "AI BI" is fake
2. Evidence of complexity others hide
3. Clear paths to win each deal
4. Credible content ammunition
5. Strategic competitive advantage

**Success Looks Like:**
- Sales says "This is exactly what I needed"
- Marketing can make bold, backed claims
- Customers say "Now I see the difference"
- Competitors can't respond effectively
- Scoop wins more deals

---

**Remember**: We're not just researching competitors. We're building Scoop's competitive moat.