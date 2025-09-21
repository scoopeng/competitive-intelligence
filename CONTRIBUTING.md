# Contributing to Competitive Intelligence Repository
## How to Maintain, Update, and Expand This Knowledge Base

---

## Quick Start for New Sessions/Contributors

### Understanding This Repository
1. **Purpose**: Evidence-based competitive intelligence for Scoop Analytics sales enablement
2. **Framework**: BUPAF (Business User Power Assessment Framework) scoring system
3. **Audience**: Sales teams, marketing, product, and executives
4. **Core Principle**: Every claim must have verifiable evidence

### Repository Navigation
```
/competitive-intelligence/
├── README.md                    # Start here - main overview
├── CONTRIBUTING.md              # This file - how to maintain
├── competitors/                 # All competitor intelligence
│   └── [competitor-name]/       # Individual competitor folders
│       ├── README.md           # Quick navigation & summary
│       └── BATTLE_CARD.md      # Sales quick reference
├── framework/                   # BUPAF methodology & templates
├── evidence/                    # Screenshots & proof
└── archive/                     # Historical content
```

---

## Adding a New Competitor

### Step 1: Create Folder Structure
```bash
mkdir competitors/[competitor-name]
cd competitors/[competitor-name]
```

### Step 2: Start with the Template
Copy `framework/COMPETITOR_ANALYSIS_TEMPLATE.md` and rename to `DEEP_ANALYSIS.md`

### Step 3: Create Required Files

#### README.md (Navigation & Summary)
```markdown
# [Competitor Name] - Competitive Intelligence

## Quick Summary
**Category**: [Marketing Mirage/Analyst Workbench/etc]  
**Fatal Flaw**: [One key weakness]  
**Key Fact**: [Most damaging evidence]  
**Reality Check**: [What they really are]  

## The Scoop Advantage
- **[Key Diff 1]**: Our approach vs theirs
- **[Key Diff 2]**: Our approach vs theirs
- **Cost**: Our price vs their price

## Files in This Folder
- **[BATTLE_CARD.md](BATTLE_CARD.md)** - Quick reference
- **[DEEP_ANALYSIS.md](DEEP_ANALYSIS.md)** - Detailed analysis

---
*Last Updated: [DATE]*
*Next Review: [DATE + 3 months]*
```

#### BATTLE_CARD.md (Sales Tool)
```markdown
# Battle Card: [Competitor]

**BUPAF Score**: X/50 (Category)  
**Fatal Flaw**: [Key weakness]  
**Key Fact**: [Damaging evidence]  

## Discovery Questions
1. [Question to expose weakness]
2. [Question to highlight our strength]

## Objection Handlers
**"[Common objection]"**
→ "[Response with evidence]"

## Evidence URLs
- [Claim]: [URL]
- [Claim]: [URL]
```

### Step 4: Research Requirements
- [ ] Official documentation review
- [ ] Pricing investigation (get actual numbers)
- [ ] Customer reviews (G2, Capterra, Reddit)
- [ ] Technical limitations
- [ ] Failed implementations/complaints
- [ ] Market positioning claims vs reality

### Step 5: Document Evidence
Every claim needs:
1. **Source**: URL, document, or customer report
2. **Date**: When evidence was gathered
3. **Quote**: Exact wording when possible

---

## Updating Existing Competitors

### Quarterly Review Checklist
- [ ] Verify all evidence URLs still work
- [ ] Check for product updates/changes
- [ ] Update pricing if changed
- [ ] Look for new customer complaints
- [ ] Add new evidence found
- [ ] Update "Last Updated" date in README

### When You Find New Evidence
1. Add to appropriate file (BATTLE_CARD, README, or create EVIDENCE.md)
2. Include source URL and date
3. Update competitor README's "Last Updated" field
4. Add entry to CHANGELOG.md (if exists)

### Price Changes
Critical to track! When you find pricing changes:
1. Document old vs new pricing
2. Note date of change
3. Update BATTLE_CARD.md
4. Calculate new cost comparison vs Scoop

---

## Testing Competitors (Snowflake Model)

### When to Create Test Suite
- Competitor claims specific capabilities
- We need to prove/disprove claims
- Customer asks for head-to-head comparison

### Testing Structure
```
competitors/[name]/
├── test_scripts/
│   ├── test_setup.py
│   ├── test_queries.py
│   └── test_results.json
├── TEST_SUMMARY.md
└── TESTING_JOURNEY.md
```

### Document Everything
- Setup time and complexity
- Dependencies required
- Errors encountered
- Success/failure rates
- Screenshots of failures

---

## Research Standards

### Evidence Hierarchy (Best to Worst)
1. **Official vendor documentation** (their own admission)
2. **Customer reports** (named companies)
3. **Benchmark studies** (third-party testing)
4. **User reviews** (G2, Capterra)
5. **Community discussions** (Reddit, forums)
6. **Analyst reports** (Gartner, Forrester)

### What NOT to Include
- ❌ Speculation without evidence
- ❌ Outdated information (>1 year old pricing)
- ❌ Unverifiable claims
- ❌ Personal opinions without data
- ❌ Competitive FUD without proof

### Dating Requirements
Always include dates for:
- Pricing information
- Product capabilities
- Customer quotes
- Benchmark results
- Last verification

---

## BUPAF Scoring Guide

### Understanding the Framework
BUPAF = Business User Power Assessment Framework
- Total score: 50 points possible
- 5 dimensions × 10 points each

### Scoring Dimensions
1. **Independence** (0-10): Can business users work alone?
2. **Analytical Depth** (0-10): Quality of insights
3. **Workflow Integration** (0-10): Excel, Slack, email?
4. **Speed to Insight** (0-10): Time to first answer
5. **Business Communication** (0-10): Understandable outputs?

### Categories by Score
- **Category A** (35-50): Business User Empowerment
- **Category B** (25-34): Analyst Workbench  
- **Category C** (15-24): Enterprise Platform
- **Category D** (0-14): Marketing Mirage

---

## Writing Style Guide

### Tone
- **Confident** but not arrogant
- **Evidence-based** not opinion-based
- **Specific** not vague
- **Professional** but memorable

### Effective Patterns
- "Their own documentation admits..."
- "Customers report..."
- "After X weeks and $Y..."
- "Would you rather... or...?"

### Power Phrases That Work
- "Fatal flaw"
- "Marketing mirage"
- "Portal prison"
- "Schema breaks everything"
- "Investigation vs alerts"

---

## Common Competitor Weaknesses to Look For

### Technical Limitations
- Schema rigidity (can't adapt to changes)
- Single source only (can't join data)
- Black box ML (can't explain why)
- No investigation (single queries only)

### Business Model Issues
- Hidden pricing (red flag)
- Renewal price shocks
- Long implementations
- Requires consultants

### Adoption Failures
- No user reviews
- No case studies
- Deprecated features
- Zero community activity

### User Experience Gaps
- Portal prison (trapped in their UI)
- No Excel/Slack integration
- Requires technical skills
- Complex configuration

---

## Maintenance Schedule

### Weekly (Sales-Driven)
- Check for urgent competitive situations
- Update based on sales feedback
- Add new evidence from deals

### Monthly
- Verify top 5 competitors' evidence
- Check for product announcements
- Update pricing if needed

### Quarterly
- Full review of all competitors
- Archive outdated content
- Update BUPAF scores if needed
- Refresh battle cards

---

## For AI/Chat Sessions

### Starting a Session
1. Read main README.md first
2. Check for any CHANGELOG.md
3. Review this CONTRIBUTING.md
4. Check POST-COMPACT files for context

### Key Commands to Remember
```bash
# See all competitors
ls competitors/

# Check evidence
cat EVIDENCE_VAULT.md

# Find specific claims
grep -r "SEARCH_TERM" competitors/

# Check last updates
find competitors -name "*.md" -exec grep -l "Last Updated" {} \;
```

### Maintaining Consistency
- Always create README.md for navigation
- Always include evidence URLs
- Always date your updates
- Always think "will this help sales?"

---

## Emergency Situations

### Competitor Makes Major Announcement
1. Document announcement with source
2. Analyze impact on positioning
3. Update battle card immediately
4. Alert sales team via README update

### Evidence URL Dies
1. Try Wayback Machine
2. Find alternative source
3. Update with new URL
4. Note change in file

### New Competitor Appears
1. Quick assessment (1-2 hours)
2. Create basic battle card
3. Mark as "Preliminary Research"
4. Schedule deep dive

---

## Quality Checklist

Before committing any update, verify:
- [ ] All claims have sources
- [ ] URLs are current and working
- [ ] Dates are included
- [ ] Sales value is clear
- [ ] README has navigation
- [ ] Battle card is concise
- [ ] Evidence is verifiable

---

## Remember the Mission

**We're not here to trash competitors.**
We're here to provide sales with truthful, evidence-based intelligence that helps them win deals by showing Scoop's genuine advantages.

**Every update should answer**: "How does this help sales win?"

---

*Contributing Guide Version: 1.0*
*Created: January 2025*
*The key to winning: Evidence + Clarity + Speed*