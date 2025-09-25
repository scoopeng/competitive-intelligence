# Research Guide - How to Build Competitor Intelligence

**Purpose**: Guide for researching competitors and organizing findings
**Result**: Comprehensive intelligence that feeds battle cards and content

---

## Research Phases

### Phase 1: Initial Discovery (2-4 hours)

#### Start with Official Sources
1. **Company Website**
   - Product pages
   - Pricing page (screenshot everything)
   - Documentation
   - Case studies
   - Blog posts

2. **Product Documentation**
   - Setup requirements
   - Technical architecture
   - Integration guides
   - API documentation
   - Limitations sections

3. **Free Trial/Demo**
   - Sign up if available
   - Record demo if offered
   - Test key claims
   - Document actual experience

#### Create Initial Research Document
```markdown
# [Competitor] Initial Research

## Company Overview
- Founded:
- Funding:
- Size:
- Market position:

## Product Basics
- What it does:
- Target users:
- Key features:
- Architecture:

## Pricing Discovered
- Published pricing:
- Hidden costs found:
- Trial limitations:

## Initial Impressions
- Strengths observed:
- Weaknesses noticed:
- Questions to investigate:
```

---

### Phase 2: Deep Dive Research (4-8 hours)

#### Customer Feedback Mining
1. **Review Sites**
   - G2.com → Filter by "Cons"
   - Capterra → Sort by lowest ratings
   - TrustRadius → Read "Room for Improvement"
   - Gartner Peer Insights → Check critical reviews

2. **Forums & Communities**
   - Reddit: r/businessintelligence, r/analytics
   - Stack Overflow: Search "[competitor] problem"
   - Hacker News: Search company name
   - Their own community forums

3. **Social Media**
   - Twitter: "[competitor] sucks" OR "frustrated"
   - LinkedIn: Employee posts about challenges
   - YouTube: Critical reviews or comparisons

#### Technical Investigation
1. **Architecture Analysis**
   - Data flow diagrams
   - Security model
   - Scalability limits
   - Performance benchmarks

2. **Integration Testing**
   - Excel export/import
   - API capabilities
   - Workflow integration
   - Schema change handling

3. **ML/AI Validation**
   - What they claim vs reality
   - Actual algorithms used
   - Explainability
   - Accuracy/performance

#### Document Everything
```markdown
# [Competitor] Deep Dive

## Customer Pain Points
### Pain Point 1: [Title]
- Source: [URL]
- Quote: "[Exact quote]"
- Impact: [Business impact]
- Our advantage: [How we solve this]

## Technical Limitations
### Limitation 1: [Title]
- Evidence: [URL or screenshot]
- Technical reason: [Why it exists]
- Can they fix it?: [Architectural barrier?]
- Our approach: [How we handle this]

## Pricing Reality
### Hidden Cost 1: [Title]
- What: [Description]
- Amount: $[X]
- Evidence: [Source]
- Common surprise?: [Yes/No]
```

---

### Phase 3: Competitive Testing (Optional but Powerful)

#### If You Can Access the Product
1. **Test Their Claims**
   - Response time
   - Accuracy
   - Ease of use
   - Feature completeness

2. **Break Things**
   - Add columns to data
   - Try complex queries
   - Test edge cases
   - Upload messy data

3. **Document Failures**
   - Screenshot errors
   - Record videos
   - Save error messages
   - Note workarounds needed

#### Create Test Report
```markdown
# [Competitor] Testing Results

## Test 1: [Name]
- Goal: [What we're testing]
- Method: [How we tested]
- Result: [What happened]
- Screenshot: [Link]
- Implication: [What this means for users]

## Comparison to Scoop
- Their approach: [Steps and time]
- Our approach: [Steps and time]
- Winner: [Who and why]
```

---

### Phase 4: Evidence Collection (Ongoing)

#### What to Collect
1. **Quotes**
   - Customer complaints
   - Employee admissions
   - Analyst assessments
   - Media coverage

2. **Screenshots**
   - Pricing pages
   - Error messages
   - Complex workflows
   - Setup requirements

3. **Documents**
   - PDF downloads
   - Whitepapers
   - Case studies
   - Technical specs

#### How to Organize
```
competitors/[name]/evidence/
├── links.md          # All URLs with dates
├── quotes.md         # Customer quotes organized by topic
├── screenshots/      # Named clearly
│   ├── pricing-enterprise-[date].png
│   ├── error-schema-change-[date].png
│   └── setup-complexity-[date].png
└── documents/        # PDFs and downloads
```

---

## Research Best Practices

### Always Document Sources
```markdown
**Claim**: They require 3 months implementation
**Evidence**: https://example.com/case-study
**Date Accessed**: 2024-01-15
**Quote**: "Our implementation took 14 weeks..."
```

### Be Specific About Limitations
❌ "It's slow"
✅ "Queries take 45-60 seconds for datasets over 1M rows (tested 2024-01-15)"

### Verify Before Claiming
1. Find the claim
2. Verify with second source
3. Test if possible
4. Document evidence

### Look for Patterns
- Multiple customers mentioning same issue
- Repeated problems in different contexts
- Consistent limitations across versions

---

## What Makes Great Intelligence

### The Killer Find
- Official admission of limitation
- Customer quote about switching to competitor
- Benchmark showing poor performance
- Pricing surprise documentation

### The Technical Proof
- Architecture diagram showing bottleneck
- Documentation noting "not supported"
- Error message revealing design flaw
- Performance metrics from testing

### The Business Impact
- Time wasted by users
- Cost overruns
- Failed implementations
- Adoption struggles

---

## Research Output Structure

### Organize Findings Into
1. **Technical Limitations** - What they can't do
2. **Pricing Reality** - True costs
3. **Customer Pain** - Real frustrations
4. **Competitive Advantages** - How we win
5. **Evidence Vault** - All proof

### Feed Into
- BATTLE_CARD.md (sales)
- outputs/web-content.md (marketing)
- outputs/comparison.md (product)
- synthesis/master-comparison.md (strategy)

---

## Red Flags to Look For

### Technical Red Flags
- "Coming soon" for core features
- "Contact sales" for basic capabilities
- "Professional services recommended"
- "Semantic model required"
- "Schema must be stable"

### Business Red Flags
- Pricing not published
- "Custom pricing only"
- Consumption-based without caps
- Long implementation times
- High services attachment

### Adoption Red Flags
- Low review counts
- Employees as reviewers
- No community activity
- Few job postings
- No recent updates

---

## Synthesis Questions

After research, answer these:

1. **What's their fatal flaw?** (The one thing they can't fix)
2. **Who is their ideal customer?** (And why that's not our customer)
3. **What's the hidden cost?** (The surprise customers face)
4. **Why do customers leave?** (The breaking point)
5. **How do we win?** (The demo moment)

---

## Quality Checklist

Before considering research complete:

- [ ] Pricing fully documented with evidence
- [ ] 3+ customer pain points with quotes
- [ ] 3+ technical limitations with proof
- [ ] Setup/implementation time verified
- [ ] Hidden costs identified
- [ ] Comparison table completed
- [ ] Evidence URLs all working
- [ ] Screenshots captured
- [ ] Battle card can be generated
- [ ] Key differentiators clear

---

*Good research is patient, thorough, and evidence-based. One killer finding is worth 10 assumptions.*