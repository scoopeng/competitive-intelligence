# Evidence Requirements for Competitive Analysis

**Purpose**: Define the evidence standards required for BUPAF scoring and competitive claims

## Evidence Hierarchy

### Level 1: Primary Evidence (Highest Value)
- **Official documentation** from vendor
- **Product demos** (recorded/screenshot)
- **Published pricing** sheets
- **Technical specifications**
- **API documentation**
- **Training materials**

### Level 2: User Evidence (High Value)
- **Review platforms** (G2, Capterra, TrustRadius)
- **User testimonials** with attribution
- **Community forums** discussions
- **Conference presentations** by users
- **Social media** mentions
- **Support tickets** (public)

### Level 3: Third-Party Evidence (Medium Value)
- **Analyst reports** (Gartner, Forrester)
- **News articles** and press coverage
- **Comparison sites** reviews
- **Academic papers** or studies
- **Benchmark reports**
- **Industry publications**

### Level 4: Indirect Evidence (Lower Value)
- **Job postings** revealing tech stack
- **Patent filings**
- **GitHub repositories**
- **LinkedIn profiles** of employees
- **Marketing materials** (verify claims)

## Required Evidence by BUPAF Dimension

### 1. Independence Evidence
**Must Document**:
- Setup/implementation timeline
- Required technical skills
- IT dependencies
- Training requirements
- User testimonials on ease of use

**Red Flag Evidence**:
- "Requires data team"
- "IT must configure"
- Long implementation timelines
- Complex training programs
- Low adoption rates

### 2. Analytical Depth Evidence
**Must Document**:
- Specific ML/AI algorithms used
- Investigation capabilities
- Pattern discovery features
- Predictive capabilities
- Statistical methods

**Red Flag Evidence**:
- "Proprietary algorithm" (no details)
- No ML specifics
- Single-query limitations
- Basic statistics only
- No root cause capability

### 3. Workflow Integration Evidence
**Must Document**:
- Integration capabilities
- Excel functionality
- Collaboration features
- Automation options
- Schema handling

**Red Flag Evidence**:
- "Export only"
- Portal-only access
- Manual processes
- Breaks on changes
- No native integration

### 4. Business Communication Evidence
**Must Document**:
- Natural language capabilities
- Explanation features
- Narrative generation
- Visualization options
- Actionability of insights

**Red Flag Evidence**:
- Technical jargon
- No explanations
- Static outputs
- Complex interfaces
- No recommendations

## Evidence Collection Template

```markdown
## [Competitor Name] - Evidence Collection

### Claim: [Specific capability claimed]
**Evidence Type**: [Primary/User/Third-Party/Indirect]
**Source**: [URL or document name]
**Date Collected**: [YYYY-MM-DD]
**Direct Quote/Screenshot**: 
> "[Exact quote or description]"

**Verification Status**: 
- [ ] Verified by multiple sources
- [ ] Contradicting evidence found
- [ ] Needs further validation

**Impact on BUPAF Score**: 
- Dimension affected: [Independence/Depth/Workflow/Communication]
- Points impact: [+X or -X]
- Reasoning: [Why this evidence matters]
```

## Special Evidence Categories

### The Absence Evidence
**Powerful when missing**:
- No user reviews after 2+ years
- No community forum
- No case studies
- No conference presentations
- No pricing transparency

**How to document**:
```markdown
**Missing Evidence**: [What's absent]
**Searched Locations**: [Where you looked]
**Date Searched**: [YYYY-MM-DD]
**Implication**: [What absence suggests]
```

### The Contradiction Evidence
**When marketing conflicts with reality**:
- Claims vs user reviews
- Features vs documentation
- Pricing claims vs actual costs
- Ease claims vs implementation time

**How to document**:
```markdown
**Marketing Claim**: "[What they say]"
**Reality Evidence**: "[What users/docs say]"
**Source**: [URL/document]
**Impact**: [How this affects scoring]
```

### The Warning Evidence
**Vendor's own admissions**:
- "Nondeterministic behavior" (Power BI)
- "Not using LLMs" (Tableau)
- "Requires technical expertise"
- "May produce incorrect results"

**These are gold** - always screenshot and preserve

## Evidence Verification Standards

### Must Verify
1. **Pricing claims** - Get actual quotes when possible
2. **User counts** - Cross-reference multiple sources
3. **AI/ML capabilities** - Demand specifics
4. **Implementation time** - Check user testimonials
5. **Adoption rates** - Verify with reviews

### Verification Methods
- **Triangulation**: 3+ sources confirming
- **Direct testing**: Free trials/demos
- **User validation**: Reviews matching claims
- **Technical proof**: Documentation/code
- **Time validation**: Historical consistency

## Evidence Storage Requirements

### File Naming Convention
```
[Competitor]_[EvidenceType]_[Date].md
Example: Tableau_UserReview_20250129.md
```

### Required Metadata
- Collection date
- Source URL
- Evidence type
- Confidence level
- Expiration (when to recheck)

### Screenshot Requirements
- Include URL bar
- Show date/timestamp
- Capture full context
- Save as PNG
- Name descriptively

## Red Flag Evidence Triggers

### Immediate Investigation Required
- Zero reviews after 1+ years
- Sudden pricing model changes
- Acquisition announcements
- Mass layoffs
- Security breaches
- Feature deprecations

### Credibility Destroyers
- Fake testimonials discovered
- Misleading benchmark claims
- Hidden costs exposed
- Feature doesn't exist
- Vaporware indicators

## Evidence Quality Scoring

### High Quality (3 points)
- Recent (< 6 months)
- Multiple sources confirm
- Technical documentation
- Named customer testimonial
- Recorded demo

### Medium Quality (2 points)
- Older (6-12 months)
- Single source
- Anonymous review
- Marketing material (verified)
- Third-party analysis

### Low Quality (1 point)
- Old (> 12 months)
- Unverified claim
- Indirect evidence
- Competitor comparison
- Speculative

## Evidence Refresh Requirements

### Must Refresh Quarterly
- Pricing
- Feature availability
- User reviews
- Market position
- Company status

### Must Refresh Annually
- Architecture
- Integration capabilities
- Market share
- Customer base
- Competitive landscape

## Legal Considerations

### Always Allowed
- Public documentation
- Published reviews
- Marketing materials
- Conference presentations
- Social media posts

### Never Allowed
- Private communications
- Internal documents
- Hacked/leaked data
- Impersonation to gather info
- Violating terms of service

### Gray Areas (Get Approval)
- Competitive intelligence services
- Paid research reports
- Customer interviews
- Partner information
- Reseller intelligence

---

*Evidence is the foundation of credible competitive intelligence. No claim without proof, no score without evidence.*