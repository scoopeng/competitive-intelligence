# Web Comparison Phased Execution Framework

**Purpose**: Step-by-step generation process that builds comprehensive competitor comparisons through distinct phases, then consolidates into final web-ready output
**Target**: 150,000 characters of credible, balanced, capability-focused content

---

## EXECUTION OVERVIEW

```
Phase 1: Foundation & Evidence Gathering (Research-Heavy)
    ↓
Phase 2: Capability Analysis & Testing (Functionality-Focused)
    ↓
Phase 3: Business Impact & Use Cases (Application-Oriented)
    ↓
Phase 4: Consolidation & Web Optimization (AEO/SEO Polish)
    ↓
Final Output: competitors/{name}/outputs/web_comparison.md
```

---

## PHASE 1: FOUNDATION & EVIDENCE GATHERING
*Time: 30-40 minutes | Output: 30-35K chars*

### Objective
Establish factual foundation with verified evidence and documented capabilities.

### 1.1 METADATA COLLECTION
```yaml
Complete all metadata fields:
- competitor_name
- parent_company
- market_position
- bupaf_score (with justification)
- employee_count
- customer_count (if available)
- last_funding/revenue
- geographic_availability
- compliance_certifications
```

### 1.2 EVIDENCE GATHERING CHECKLIST
- [ ] Review existing BATTLE_CARD.md
- [ ] Extract from research/ folder
- [ ] Compile evidence/ URLs
- [ ] Document official vendor claims
- [ ] Collect documentation quotes
- [ ] Find customer testimonials (balanced)
- [ ] Identify third-party analysis

### 1.3 CORE FACTS DOCUMENTATION
Write factual descriptions for:
- **What It Actually Is**: Product category and architecture
- **Verified Capabilities**: What it can do (with evidence)
- **Documented Limitations**: From their own docs
- **Pricing Structure**: All components, hidden costs
- **Implementation Requirements**: Time, resources, expertise
- **Geographic/Compliance Gaps**: Where it can't be used

### 1.4 INITIAL COMPARISON FRAMEWORK
Create basic comparison structure:
```markdown
| Dimension | {Competitor} | Scoop | Evidence |
|-----------|-------------|-------|----------|
| Setup Time | {Actual} | 30 seconds | [Sources] |
| Excel Support | {Level} | 150+ formulas | [Demo link] |
| Investigation | {Capability} | Multi-pass | [Test results] |
```

### Phase 1 Output
File: `competitors/{name}/research_foundation.md`
- Clean, factual foundation
- All claims evidenced
- Balanced perspective established

---

## PHASE 2: CAPABILITY ANALYSIS & FUNCTIONAL TESTING
*Time: 40-50 minutes | Output: 40-45K chars*

### Objective
Deep-dive into functional capabilities with specific focus on what Scoop can do that competitor cannot.

### 2.1 FUNCTIONAL CAPABILITY MATRIX
Complete detailed capability assessment:

```markdown
Essential Business User Capabilities:
□ Multi-pass investigation → {Competitor: No | Scoop: Yes, 3-10 passes}
□ Excel formula execution → {Competitor: Limited | Scoop: 150+ native}
□ Schema adaptation → {Competitor: Manual | Scoop: Automatic}
□ Natural language → {Competitor: Quality | Scoop: Conversational}
□ Workflow integration → {Competitor: Exports | Scoop: Native Office}
□ ML/Statistics → {Competitor: Basic | Scoop: J48, JRip, EM}
□ Presentation generation → {Competitor: No | Scoop: Direct to PPT}
```

### 2.2 UNIQUE SCOOP ADVANTAGES
Document capabilities ONLY Scoop has:
- **Investigation Engine**: Multi-hypothesis parallel testing
- **Smart Scanner**: Handles embedded subtotals, complex formats
- **Dual-Time Intelligence**: Transaction vs knowledge time
- **Slack-Native Platform**: Full analytics in Slack
- **=SCOOP() Function**: Live Excel integration
- **Dynamic Schema Evolution**: Zero-downtime adaptation

### 2.3 TECHNICAL ARCHITECTURE COMPARISON
```markdown
Architecture Analysis:
- Query Execution Model: {Single vs Multi-pass}
- Data Model Requirements: {Semantic layer vs Direct}
- Integration Architecture: {APIs vs Native}
- Scaling Model: {Vertical vs Horizontal}
- Maintenance Burden: {FTEs required vs Zero}
```

### 2.4 TESTING & REPRODUCIBILITY
If applicable, document:
- Query comparison results
- Performance benchmarks
- Accuracy testing
- Non-deterministic behavior (for AI products)

### Phase 2 Output
File: `competitors/{name}/capability_analysis.md`
- Detailed functional comparison
- Clear Scoop advantages
- Technical differentiation

---

## PHASE 3: BUSINESS IMPACT & APPLICATION
*Time: 30-40 minutes | Output: 35-40K chars*

### Objective
Translate capabilities into business value through use cases and scenarios.

### 3.1 USE CASE DEMONSTRATIONS
Create 3-5 detailed scenarios showing capability differences:

```markdown
Scenario: Quarterly Business Review Preparation

With {Competitor}:
1. Monday: Request IT for dashboard updates (ticket created)
2. Wednesday: IT delivers updated dashboard
3. Thursday: Export charts, paste to PowerPoint
4. Friday morning: Manual formatting
5. Friday afternoon: Discover missing analysis, too late
Time: 5 days, 2-3 people

With Scoop:
1. Friday 3pm: "Quarterly review deck with YoY comparison"
2. Friday 3:30pm: Complete PowerPoint ready
Time: 30 minutes, 1 person
```

### 3.2 WORKFLOW INTEGRATION ANALYSIS
Compare daily workflow impact:
- Morning dashboard routine
- Ad-hoc investigation process
- Report generation workflow
- Cross-team collaboration
- Mobile/remote access

### 3.3 ROI CALCULATION FRAMEWORK
Build credible ROI model:
```markdown
Cost Comparison (200 users):
{Competitor}:
- Licenses: ${amount}
- Infrastructure: ${amount}
- Implementation: ${amount}
- Training: ${amount}
- Maintenance: ${FTE cost}
- Total Year 1: ${total}

Scoop:
- Platform: $3,588/year
- Implementation: $0
- Training: $0
- Maintenance: $0
- Total Year 1: $3,588

Savings: ${difference} (X% reduction)
```

### 3.4 BEST-FIT ANALYSIS
Professional positioning:
- **Ideal for Scoop**: Specific scenarios
- **Consider {Competitor}**: Where they excel
- **Decision Criteria**: Clear framework

### Phase 3 Output
File: `competitors/{name}/business_impact.md`
- Use case comparisons
- ROI modeling
- Balanced recommendations

---

## PHASE 4: CONSOLIDATION & WEB OPTIMIZATION
*Time: 60-90 minutes | Output: 150K chars final*

### Objective
Merge all phases into comprehensive web-ready comparison with AEO/SEO optimization.

### 4.1 CONTENT CONSOLIDATION
Merge three phase outputs following WEB_COMPARISON_TEMPLATE.md structure:
1. Import Phase 1 evidence and facts
2. Integrate Phase 2 capability analysis
3. Incorporate Phase 3 business scenarios
4. Add connecting narrative tissue

### 4.2 AEO OPTIMIZATION
Enhance for Answer Engine Optimization:
```markdown
Add AEO Elements:
- Primary question cluster (8-10 questions)
- Direct answer boxes with schema markup
- Long-tail keyword integration
- Conversational query responses
- Featured snippet optimization
- Voice search answers
```

### 4.3 CREDIBILITY ENHANCEMENTS
- Add balanced acknowledgments of competitor strengths
- Include "where {competitor} excels" section
- Use professional language throughout
- Ensure all claims have evidence links
- Add confidence levels to assertions

### 4.4 WEB STRUCTURE OPTIMIZATION
Organize into 3x50K character fields:
```markdown
Field 1 (50K): Hero, Evidence, Fatal Flaws^H^H Key Considerations
Field 2 (50K): Technical Analysis, Testing, Architecture
Field 3 (50K): Business Impact, ROI, Migration, CTAs
```

### 4.5 QUALITY CHECKLIST
Before finalizing:
- [ ] All facts verified with sources
- [ ] Tone is professional and balanced
- [ ] Scoop advantages clearly articulated
- [ ] AEO optimization complete
- [ ] 150K character target met (±10%)
- [ ] No unsubstantiated claims
- [ ] Competitor strengths acknowledged

### Phase 4 Output
File: `competitors/{name}/outputs/web_comparison.md`
- Complete 150K character comparison
- Web-ready with all formatting
- AEO/SEO optimized
- Credible and balanced

---

## EXECUTION COMMANDS

### To Generate for a Competitor:
```bash
# Phase 1: Foundation
"Generate Phase 1 foundation for {competitor} using research from competitors/{name}/"

# Phase 2: Capabilities  
"Generate Phase 2 capability analysis for {competitor} building on Phase 1"

# Phase 3: Business Impact
"Generate Phase 3 business impact for {competitor} using Phases 1-2"

# Phase 4: Consolidation
"Consolidate all phases into final web comparison for {competitor}"
```

### Quality Gates Between Phases:
- Review each phase output before proceeding
- Identify gaps or additional research needs
- Adjust subsequent phases based on findings
- Maintain consistency across phases

---

## SPECIAL CONSIDERATIONS BY COMPETITOR TYPE

### Major Vendors (Power BI, Tableau, Domo, ThoughtSpot)
- Emphasize ecosystem lock-in
- Document deprecation history
- Include geographic restrictions
- Analyze parent company influence

### AI-Powered Products (Power BI Copilot, Snowflake Cortex)
- Test non-deterministic behavior
- Document hallucination issues
- Include vendor warnings
- Emphasize consistency problems

### Cloud/Consumption-Based (Snowflake, Domo)
- Calculate consumption spirals
- Document renewal shocks
- Show TCO escalation
- Include hidden compute costs

### Smaller Vendors (Tellius, Sisense, Zenlytic, DataChat)
- Focus on capability gaps
- Document customer base size
- Emphasize innovation velocity
- Show product completeness

---

## SUCCESS METRICS

### Phase Completion Criteria
- Phase 1: All evidence documented and verified
- Phase 2: Complete capability matrix with Scoop advantages clear
- Phase 3: 3+ use cases with ROI model complete
- Phase 4: 150K chars, AEO optimized, credible tone

### Quality Indicators
- Evidence density: 1+ citation per major claim
- Balance ratio: Acknowledge 1 strength per 3-4 limitations
- Readability: Flesch score 80-90
- Completeness: All template sections addressed

---

*This framework ensures systematic, high-quality generation of web comparisons that are credible, comprehensive, and optimized for conversion.*