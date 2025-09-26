# Web Comparison Phased Execution Framework

**Purpose**: Step-by-step generation process that builds comprehensive competitor comparisons through distinct phases, then consolidates into final web-ready output
**Target**: 150,000 characters of credible, balanced, capability-focused content

---

## 🎯 WHAT THIS FRAMEWORK PROVIDES

### Templates (What to Write)
1. **WEB_COMPARISON_TEMPLATE.md** - Final output template (150K chars)
2. **Phase Output Templates** - Structure for each phase (below)
3. **Content Guidelines** - What goes in each section

### Process (How to Execute)
1. **Phased Execution Plan** - 4 distinct phases with clear objectives
2. **Checklists** - Step-by-step tasks for each phase
3. **Quality Gates** - Review points between phases

### The System
```
Research Inputs → Phase 1 → Phase 2 → Phase 3 → Phase 4 → Final Output
                    ↓         ↓         ↓         ↓
                Templates  Templates  Templates  Polish &
                    +          +          +      Consolidate
                Checklists  Checklists Checklists    ↓
                                                 web_comparison.md
                                                    (150K chars)
```

---

## EXECUTION OVERVIEW

```
Phase 1: Foundation & Evidence Gathering (Research-Heavy)
    ├── Output: research_foundation.md (30-35K chars)
    └── Focus: Facts, evidence, documentation
    
Phase 2: Capability Analysis & Testing (Functionality-Focused)
    ├── Output: capability_analysis.md (40-45K chars)
    └── Focus: Features, architecture, what Scoop can do
    
Phase 3: Business Impact & Use Cases (Application-Oriented)
    ├── Output: business_impact.md (35-40K chars)
    └── Focus: Scenarios, ROI, workflow reality
    
Phase 4: Consolidation & Web Optimization (Integration & Polish)
    ├── Output: web_comparison.md (150K chars)
    └── Focus: Merge, enhance, optimize for AEO/SEO
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

### PHASE 1 OUTPUT TEMPLATE
File: `competitors/{name}/research_foundation.md`

```markdown
# {COMPETITOR} Research Foundation

## Company Overview
- Company: {Full name}
- Parent: {If applicable}
- Founded: {Year}
- Employees: {Count}
- Customers: {Count if available}
- Revenue/Funding: {Latest}
- Market Position: {Their claim}

## Product Facts
### What It Actually Is
{2-3 paragraph factual description}

### Core Capabilities (Verified)
- {Capability 1}: {Description} [Source]
- {Capability 2}: {Description} [Source]
- {Continue for all major capabilities}

### Documented Limitations
From their own documentation:
- "{Quote about limitation}" - [URL, Date]
- "{Quote about requirement}" - [URL, Date]

## Pricing Reality
### Published Pricing
- {Component}: ${Amount}
- {Component}: ${Amount}

### Hidden/Additional Costs
- {Hidden cost}: ${Amount} [Evidence]
- {Hidden cost}: ${Amount} [Evidence]

### Total Cost Reality
200 users, first year: ${Total}

## Implementation Requirements
- Setup Time: {Documented timeline}
- Technical Resources: {What's needed}
- Training Required: {Hours/days}
- Maintenance: {FTE requirement}

## Geographic & Compliance
- Available Regions: {List}
- Blocked Regions: {List}
- Compliance: {HIPAA, SOX, etc.}
- Industry Limitations: {Any sectors excluded}

## Initial Comparison Data
| Metric | {Competitor} | Scoop | Evidence |
|--------|-------------|-------|----------|
| Setup Time | {X} | 30 seconds | [Links] |
| Business User Ready | {Y/N} | Yes | [Links] |
| Excel Formulas | {Level} | 150+ | [Links] |
| Investigation | {Type} | Multi-pass | [Links] |
| True Cost (200 users) | ${Amount} | $3,588 | [Links] |

## Key Evidence URLs
1. {URL} - {What it proves}
2. {URL} - {What it proves}
{Continue for top 10-15 sources}
```

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

### PHASE 2 OUTPUT TEMPLATE
File: `competitors/{name}/capability_analysis.md`

```markdown
# {COMPETITOR} Capability Analysis

## Functional Capability Assessment

### Core Business User Capabilities
| Capability | {Competitor} | Scoop | Advantage |
|------------|-------------|-------|-----------|
| Multi-pass Investigation | ❌ No | ✅ Yes (3-10 passes) | Scoop finds root causes |
| Excel Formula Execution | {Details} | ✅ 150+ native | Scoop: No translation needed |
| Schema Adaptation | ❌ Manual updates | ✅ Automatic | Scoop: Zero downtime |
| Natural Language Quality | {Quality} | ✅ Conversational | Scoop: Actually works |
| Workflow Integration | {Level} | ✅ Native Office/Slack | Scoop: Work where you are |
| ML/Statistical Analysis | {Types} | ✅ J48, JRip, EM, etc. | Scoop: Auto-discovery |
| Presentation Generation | ❌ No | ✅ Direct to PPT | Scoop: 30-second decks |
| Data Quality Handling | {Approach} | ✅ Smart Scanner | Scoop: Handles messy data |

## Scoop's Unique Capabilities (NO competitor has these)

### 1. Investigation Engine
**What It Does**: Multi-hypothesis parallel testing
**How It Works**: 
{Technical explanation}
**Business Value**: Find root causes, not just symptoms
**Proof**: [Demo link or test result]

### 2. Dynamic Schema Evolution
**What It Does**: Automatic adaptation to data changes
**How It Works**:
{Technical explanation}
**Business Value**: No breaking dashboards/queries
**Proof**: [Evidence]

### 3. Native Excel Engine
**What It Does**: Executes actual Excel formulas
**Supported Functions**: VLOOKUP, SUMIFS, INDEX/MATCH, etc.
**Business Value**: No retraining for Excel users
**Proof**: [List of 150+ supported functions]

### 4. Smart Scanner Technology
**What It Does**: Handles complex, messy data
**Capabilities**:
- Embedded subtotals detection
- Multi-format recognition
- Automatic normalization
**Business Value**: Works with real-world data
**Proof**: [Examples]

### 5. Slack-Native Analytics
**What It Does**: Full analytics platform in Slack
**Not Just Notifications**: Complete analysis, visualization, sharing
**Business Value**: Analytics where work happens
**Proof**: [Screenshots/demo]

## Technical Architecture Comparison

### Query Execution Model
| Aspect | {Competitor} | Scoop |
|--------|-------------|-------|
| Query Strategy | Single SQL | Multi-pass reasoning |
| Execution | Sequential | Parallel with dependencies |
| Context | Stateless | Full conversation memory |
| Output | Raw data | Synthesized insights |

### Data Model Requirements
| Aspect | {Competitor} | Scoop |
|--------|-------------|-------|
| Semantic Layer | Required (weeks to build) | None needed |
| Schema Changes | Manual updates | Auto-evolution |
| Maintenance | 1-2 FTE | Zero |

### Infrastructure & Performance
| Metric | {Competitor} | Scoop |
|--------|-------------|-------|
| Setup Time | {Actual} | 30 seconds |
| Query Speed | {Range} | {Scoop speed} |
| Concurrent Users | {Limits} | {Scoop scale} |
| Data Volume | {Limits} | {Scoop capacity} |

## Testing Results (If Applicable)

### Query Comparison Test
Query: "Why did revenue drop in Q3?"

**{Competitor} Result**:
{What they return - usually single query}

**Scoop Result**:
{Multi-pass investigation with findings}

### Excel Formula Test
Test: VLOOKUP between two datasets

**{Competitor}**: {Result - usually fails or requires translation}
**Scoop**: Direct execution, immediate results

## Capability Gaps That Matter

### What {Competitor} CANNOT Do
1. **Investigation**: Cannot explore "why" questions
2. **Excel Integration**: No native formula support
3. **Schema Evolution**: Breaks on data changes
4. **Workflow**: Requires portal access
5. **ML Discovery**: No automatic pattern finding

### Business Impact of These Gaps
- Investigation gap = 2-4 hours manual analysis
- Excel gap = Retraining entire teams
- Schema gap = 2-4 weeks for updates
- Workflow gap = 3+ hours per report
- ML gap = Missing critical insights
```

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

### PHASE 3 OUTPUT TEMPLATE
File: `competitors/{name}/business_impact.md`

```markdown
# {COMPETITOR} Business Impact Analysis

## Real-World Scenario Comparisons

### Scenario 1: Quarterly Business Review Prep
**The Task**: Prepare QBR deck with YoY analysis and insights

**With {Competitor}**:
- Monday AM: Submit IT ticket for dashboard updates
- Tuesday: IT acknowledges request
- Wednesday: Dashboard updated
- Thursday AM: Export charts to images
- Thursday PM: Build PowerPoint manually
- Friday AM: Format and polish slides
- Friday PM: Realize missing analysis, too late

**Time**: 5 days, 2-3 people
**Result**: Static slides, limited insights

**With Scoop**:
- Friday 2:00 PM: "Create QBR deck with YoY analysis"
- Friday 2:30 PM: Complete PowerPoint ready
- Friday 2:45 PM: Add custom insights via chat
- Friday 3:00 PM: Final deck delivered

**Time**: 1 hour, 1 person
**Result**: Dynamic insights, complete analysis

**Impact**: 40 hours saved, deeper insights delivered

### Scenario 2: Investigating Revenue Anomaly
**The Task**: CEO asks "Why did revenue spike last Tuesday?"

**With {Competitor}**:
{Step-by-step process showing manual investigation}
**Time**: 3-4 hours
**Result**: Basic answer, no root cause

**With Scoop**:
{Shows Investigation Engine process}
**Time**: 2 minutes
**Result**: Complete root cause with recommendations

### Scenario 3: New Marketing Campaign Analysis
{Similar detailed comparison}

### Scenario 4: Sales Pipeline Investigation
{Similar detailed comparison}

### Scenario 5: Customer Churn Analysis
{Similar detailed comparison}

## Workflow Integration Impact

### Daily Analytics Tasks
| Task | {Competitor} Time | Scoop Time | Weekly Savings |
|------|-------------------|------------|----------------|
| Morning dashboards | 45 min | 5 min | 3.3 hours |
| Ad-hoc questions | 2 hours | 5 min | 9.6 hours |
| Report generation | 3 hours | 30 min | 12.5 hours |
| Data exploration | Not possible | 15 min | New capability |
| **Total per analyst** | **5.75 hours/day** | **55 min/day** | **24.8 hours** |

### Excel User Reality
**{Competitor} Approach**:
- Export data to CSV
- Rebuild formulas from scratch
- No connection to source
- Manual refresh process
- Days to recreate complex models

**Scoop Approach**:
- =SCOOP() function in Excel
- Existing formulas work immediately
- Live data connection
- Automatic refresh
- Zero migration effort

## ROI Analysis

### Cost Comparison (200 users, Year 1)

#### {Competitor} Total Investment
**Software Costs**:
- Licenses: ${amount}
- Infrastructure: ${amount}
- Add-ons: ${amount}

**Implementation Costs**:
- Professional services: ${amount}
- Training: ${amount}
- Semantic layer development: ${amount}

**Ongoing Costs**:
- Maintenance (1.5 FTE): ${amount}
- Support: ${amount}

**Hidden Costs**:
- Lost productivity during ramp: ${amount}
- Delayed insights: ${amount}

**Total Year 1**: ${total}
**Cost per user**: ${amount}

#### Scoop Investment
**Software**: $3,588/year flat
**Implementation**: $0
**Training**: $0
**Maintenance**: $0
**Total Year 1**: $3,588
**Cost per user**: $17.94

#### ROI Calculation
- Direct savings: ${competitor_cost - 3588}
- Productivity gain (24.8 hrs/week × 50 analysts × $75/hr): ${amount}
- Faster decisions value: ${estimated}
- **Total ROI**: {X}% in Year 1
- **Payback period**: {X} days

## Decision Framework

### Scoop is Ideal When You Have:
✅ Business users who need quick answers
✅ Excel-heavy workflows
✅ Changing data structures
✅ Limited IT resources
✅ Need for investigation, not just reporting
✅ Distributed teams using Slack/Teams
✅ Rapid implementation requirements
✅ Budget constraints

### Consider {Competitor} When You:
⚠️ Need pixel-perfect dashboard layouts
⚠️ Have dedicated BI team with time
⚠️ Require {specific competitor strength}
⚠️ Already heavily invested in {ecosystem}
⚠️ Don't mind manual investigation
⚠️ Have static data structures
⚠️ Can afford long implementation

### Migration Path from {Competitor}

#### Week 1-2: Parallel Running
- Keep {Competitor} active
- Upload key datasets to Scoop
- Validate core metrics match
- Identify quick wins

#### Week 3-4: Pilot Team
- Select 5-10 power users
- Document their success stories
- Show capabilities {Competitor} lacks
- Calculate time savings

#### Week 5-6: Broader Rollout
- Expand to department
- Migrate key reports
- Train in 30-minute sessions
- Share wins broadly

#### Week 7-8: Full Migration
- All users on Scoop
- Decommission {Competitor}
- Document savings
- Celebrate success

### Risk Mitigation
| Concern | Mitigation |
|---------|------------|
| "Our dashboards" | Recreate key views quickly |
| "User training" | 30-min sessions, Excel familiar |
| "Data security" | SOC2, HIPAA compliant |
| "Vendor risk" | Month-to-month, no lock-in |
```

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

### 4.2 AEO OPTIMIZATION (CRITICAL - DO NOT SKIP)
This is where we add the AI-engine optimization layer:

```markdown
Step 1: Question Cluster Development
- Generate 8-10 primary questions users ask
- Create direct, extractable answers
- Add schema.org markup for FAQPage
- Format for featured snippets

Step 2: Long-tail Keyword Integration
Natural insertion of high-intent searches:
- "{competitor} alternative for business users"
- "migrate from {competitor} to scoop"
- "{competitor} vs scoop for {industry}"
- "why {competitor} fails for excel users"
- "{competitor} implementation time and cost"

Step 3: Direct Answer Boxes
For each major question, create:
<div class="aeo-answer" itemscope itemtype="schema.org/Answer">
**Q**: {Question}
**A**: {2-3 sentence direct answer with key facts}
</div>

Step 4: Voice Search Optimization
Add conversational responses:
- "Hey Google, what's better than {competitor}?"
- "Alexa, how much does {competitor} cost?"

Step 5: Position Zero Tables
Create comparison tables optimized for featured snippets:
| Question | {Competitor} | Scoop |
|----------|-------------|-------|
| Setup time | {X weeks} | 30 seconds |
| Cost | ${amount} | $3,588 |
| Excel support | No | Yes |

Step 6: Semantic Enrichment
- Add related terms and synonyms
- Include industry-specific terminology
- Build topical authority signals
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

## 📋 MASTER EXECUTION CHECKLIST

### Pre-Flight Check
- [ ] Reviewed existing BATTLE_CARD.md
- [ ] Checked research/ folder for evidence
- [ ] Reviewed evidence/ folder for URLs
- [ ] Have access to WEB_COMPARISON_TEMPLATE.md
- [ ] Understand competitor type (Major/AI/Cloud/Smaller)

### PHASE 1 EXECUTION (30-40 min)
**Command**: "Generate Phase 1 foundation for {competitor}"

**Checklist**:
- [ ] Company overview complete
- [ ] Product facts documented
- [ ] Capabilities verified with sources
- [ ] Limitations quoted from docs
- [ ] Pricing breakdown complete
- [ ] Hidden costs identified
- [ ] Implementation requirements clear
- [ ] Geographic/compliance gaps noted
- [ ] Initial comparison table done
- [ ] 10-15 evidence URLs listed
- [ ] Output: research_foundation.md (30-35K chars)

**Quality Gate**: Stop and review. All facts accurate? Evidence solid?

### PHASE 2 EXECUTION (40-50 min)
**Command**: "Generate Phase 2 capability analysis for {competitor}"

**Checklist**:
- [ ] Capability matrix complete (8+ capabilities)
- [ ] All 5 unique Scoop capabilities explained
- [ ] Technical architecture compared
- [ ] Query execution model detailed
- [ ] Data model requirements clear
- [ ] Infrastructure comparison done
- [ ] Testing results documented (if applicable)
- [ ] Excel formula matrix complete
- [ ] Capability gaps identified
- [ ] Business impact of gaps calculated
- [ ] Output: capability_analysis.md (40-45K chars)

**Quality Gate**: Are Scoop's advantages crystal clear?

### PHASE 3 EXECUTION (30-40 min)
**Command**: "Generate Phase 3 business impact for {competitor}"

**Checklist**:
- [ ] 5 scenario comparisons complete
- [ ] Workflow integration analyzed
- [ ] Daily task time savings calculated
- [ ] Excel user reality documented
- [ ] Full ROI model built
- [ ] Cost breakdown detailed
- [ ] Decision framework clear
- [ ] Migration path outlined (8 weeks)
- [ ] Risk mitigation addressed
- [ ] Best-fit analysis balanced
- [ ] Output: business_impact.md (35-40K chars)

**Quality Gate**: Is the business case compelling yet credible?

### PHASE 4 EXECUTION (60-90 min)
**Command**: "Consolidate all phases into final web comparison"

**Pre-consolidation Checklist**:
- [ ] All 3 phase files ready
- [ ] WEB_COMPARISON_TEMPLATE.md available
- [ ] Target competitor type identified

**Consolidation Steps**:
- [ ] Merge Phase 1 content into template sections
- [ ] Integrate Phase 2 capabilities throughout
- [ ] Weave in Phase 3 scenarios and ROI
- [ ] Add narrative connections between sections
- [ ] Ensure flow and readability

**AEO Enhancement Checklist**:
- [ ] 8-10 question cluster created
- [ ] Direct answer boxes added
- [ ] Long-tail keywords integrated naturally
- [ ] Voice search responses included
- [ ] Position Zero tables formatted
- [ ] Schema markup added
- [ ] Semantic enrichment complete

**Credibility Polish**:
- [ ] Competitor strengths acknowledged
- [ ] Professional language throughout
- [ ] All claims have evidence
- [ ] Balanced tone maintained

**Final Structure Check**:
- [ ] Field 1 (Hero, Evidence): ~50K chars
- [ ] Field 2 (Technical): ~50K chars
- [ ] Field 3 (Business, CTAs): ~50K chars
- [ ] Total: 140-160K chars

**Output**: `competitors/{name}/outputs/web_comparison.md`

### POST-GENERATION VALIDATION
- [ ] Fact-check 10 random claims
- [ ] Verify all URLs still work
- [ ] Read for tone and balance
- [ ] Check character counts
- [ ] Validate AEO elements
- [ ] Review CTAs and migration path

## EXECUTION COMMANDS

### Full Generation Sequence:
```bash
# Phase 1: Foundation
"Generate Phase 1 foundation for {competitor} using research from competitors/{name}/"

# Review Phase 1 output, then:

# Phase 2: Capabilities  
"Generate Phase 2 capability analysis for {competitor} building on Phase 1"

# Review Phase 2 output, then:

# Phase 3: Business Impact
"Generate Phase 3 business impact for {competitor} using Phases 1-2"

# Review Phase 3 output, then:

# Phase 4: Consolidation
"Consolidate all phases into final web comparison for {competitor}"
```

### Quick Command (if confident):
```bash
"Generate complete web comparison for {competitor} using phased execution framework"
# This runs all 4 phases with automatic progression
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