# Competitor Research Template - Complete Protocol

**Time**: 120-150 minutes for comprehensive, evidence-based competitive intelligence
**Quality**: Enterprise-grade with functionality mapping, implementation stories, quantified data, and research library

## 🔴 CRITICAL INSTRUCTIONS

### 1. CHECK EXISTING RESEARCH FIRST
**Before running ANY search, check the Research Library section below to see if it's already been done**
- If a search is already documented with good results, SKIP IT (check the box and move on)
- If a search was done but returned no/poor results, you MAY retry it
- This prevents duplicate work and saves time

### 2. DOCUMENT AS YOU GO
**Document EVERY URL you visit in the appropriate phase research library file AS YOU GO**
- Create `evidence/phase[N]_research_library.md` for each phase
- Add each URL immediately after visiting to the appropriate phase file
- Include searches that return no results
- Update the main checklist summary after completing each phase

### 3. HANDLE EDGE CASES
- **Paywalled content**: Try cache:URL in Google, archive.org, or note as "Paywalled - could not access"
- **No results**: After 3 failed searches in a section, try broader terms or competitor's parent company
- **Time management**: If Phase 1 exceeds 50 minutes, prioritize remaining high-value searches
- **Conflicting evidence**: Document both viewpoints in NOTES section with sources

### 4. RESEARCH LIBRARY ORGANIZATION
**All research is stored in separate files for better organization:**
- **Phase 1**: Create `evidence/phase1_customer_discovery.md`
- **Phase 2**: Create `evidence/phase2_functionality_analysis.md`
- **Phase 3**: Create `evidence/phase3_technical_reality.md`
- **Phase 4**: Create `evidence/phase4_sales_enablement.md`
- **In main checklist**: Reference each file with 5-8 key findings summary
- **Benefit**: Keeps checklist clean and research fully documented

## Research Status Tracker
### Overall Progress
- [ ] Archive recovery completed
- [ ] Customer discovery completed (17 searches)
- [ ] Functionality analysis completed (15 searches)
- [ ] Technical analysis completed (24 searches)
- [ ] BUPAF scoring completed with evidence
- [ ] Battle card updated
- [ ] Sales materials created
- [ ] Research library fully documented

### Phase Status (Mark X to reset phase)
- [ ] Reset Phase 1: Customer Discovery & Stories
- [ ] Reset Phase 2: Functionality Deep Dive
- [ ] Reset Phase 3: Technical Reality & Competitive Context
- [ ] Reset Phase 4: Analysis & Sales Enablement

### Last Research Date
- **Phase 1**: Never / [Date]
- **Phase 2**: Never / [Date]
- **Phase 3**: Never / [Date]
- **Phase 4**: Never / [Date]

---

## PHASE 0: Existing Assets Check (5 minutes)

### Archive & Evidence Recovery
- [ ] Checked `../../archive/` for any tableau-pulse related files
- [ ] Checked `../../evidence/` for existing tableau-pulse content
- [ ] Listed all existing files in `competitors/tableau-pulse/` directory
- [ ] Read existing `README.md` if exists
- [ ] Read existing `BATTLE_CARD.md` if exists
- [ ] Read all files in `research/` subdirectory if exists
- [ ] Read all files in `evidence/` subdirectory if exists
- [ ] **READ THE RESEARCH LIBRARY BELOW** - Check what searches were already done
- [ ] Documented what was recovered in `research/existing_research.md`

### Existing Research Inventory
```
Files Found:
- [ ] README.md exists
- [ ] BATTLE_CARD.md exists
- [ ] research/ folder exists with ___ files
- [ ] evidence/ folder exists with ___ files
- [ ] outputs/ folder exists with ___ files
- [ ] Archive contained: [list any recovered files]
```

---

## PHASE 1: Deep Discovery & Customer Stories (40-50 minutes)

### ⚠️ PRE-PHASE 1 CHECK (2 minutes)
- [ ] **FIRST**: Scroll down and read the entire Phase 1 Research Library section
- [ ] **IDENTIFY**: Which searches have already been completed successfully
- [ ] **MARK**: Check off any searches below that are already well-documented
- [ ] **PROCEED**: Only execute searches that haven't been done or need better results

### 1A: Customer Review Mining (10 minutes)
Execute these WebSearch queries:

- [ ] **Search 1**: "site:g2.com tableau-pulse 1 star 2 star reviews implementation disaster"
- [ ] **Search 2**: "site:capterra.com tableau-pulse negative review switching from"
- [ ] **Search 3**: "site:trustradius.com tableau-pulse disappointed regret choosing"
- [ ] **Search 4**: "tableau-pulse implementation failed timeline overrun consultant expensive"

**📝 IMPORTANT - For EVERY search and EVERY URL visited**:
1. **IMMEDIATELY** document in the Research Library section at the bottom of this file
2. **BE COMPREHENSIVE** - Don't over-summarize! Capture:
   - Multiple full quotes (not fragments)
   - All specific numbers, costs, percentages, timelines
   - Company details (size, industry, name if mentioned)
   - Technical details (licensing requirements, error messages)
   - Implementation challenges and failure scenarios
3. Do this AS YOU GO - don't wait until the end
4. Include even "no results found" searches for completeness
5. If a source is rich, use WebFetch to extract MORE detail
6. Rate source credibility (High/Medium/Low)

### 1B: Reddit & Community Deep Dive (10 minutes)

- [ ] **Search 5**: "site:reddit.com r/BusinessIntelligence tableau-pulse problems limitations"
- [ ] **Search 6**: "site:reddit.com r/analytics tableau-pulse switching from because"
- [ ] **Search 7**: "site:reddit.com tableau-pulse horror story disaster experience"
- [ ] **Search 8**: "site:community.fabric.microsoft.com tableau-pulse error doesn't work"

**Goal**: Find real user frustrations, specific error messages, switching decisions

### 1C: LinkedIn & Professional Networks (8-10 minutes)

- [ ] **Search 9**: "site:linkedin.com tableau-pulse disappointed moving from consultant"
- [ ] **Search 10**: "site:linkedin.com data analyst BI manager tableau-pulse challenges"
- [ ] **Search 11**: "tableau-pulse consultant blog implementation challenges timeline"
- [ ] **Search 12**: "tableau-pulse systems integrator lessons learned failed project"

**Focus**: Professional insights, consultant perspectives, enterprise challenges

### 1D: Industry Vertical Deep Dive (8-10 minutes)

- [ ] **Search 13**: "tableau-pulse healthcare HIPAA compliance audit failed"
- [ ] **Search 14**: "tableau-pulse financial services SOX regulatory problems"
- [ ] **Search 15**: "tableau-pulse retail real-time inventory scalability issues"
- [ ] **Search 16**: "tableau-pulse manufacturing plant floor data integration"
- [ ] **Search 17**: "tableau-pulse government security clearance restrictions"

**Goal**: Find industry-specific deal-breakers, compliance failures, regulatory issues

### Phase 1 Success Criteria
- [ ] Found 10+ specific customer complaints with context
- [ ] Identified 5+ implementation horror stories
- [ ] Documented 3+ industry-specific limitations
- [ ] Captured 15+ direct customer quotes
- [ ] All findings include company size, industry, specific use case

### Phase 1 Output Files
- [ ] Created/Updated `research/customer_stories.md` - Implementation experiences
- [ ] Created/Updated `research/industry_analysis.md` - Vertical-specific limitations
- [ ] Created/Updated `evidence/customer_quotes.md` - Direct quotes with context
- [ ] Created/Updated `evidence/community_sources.md` - Forum/Reddit findings

---

## PHASE 2: Functionality Deep Dive (35-40 minutes)

### ⚠️ CRITICAL: STRATEGIC CAPABILITY ASSESSMENT
**This phase maps competitor capabilities against Scoop's core differentiators**

### Pre-Phase 2: Review Scoop's Core Differentiators (3 minutes)
- [ ] **READ**: Review SCOOP_CAPABILITIES.md for key differentiators
- [ ] **FOCUS**: Keep these in mind during all searches:
  - Excel Formula Engine (150+ functions)
  - Automatic ML Discovery (J48, JRip, EM Clustering)
  - Multi-Pass Investigation (3-10 queries)
  - Visual Intelligence (AI presentations)
  - 30-Second Workflow Integration

### 2A: Documentation & Core Functionality (10 minutes)
- [ ] **Documentation Review**: Visit tableau-pulse.com/docs or help.tableau-pulse.com
  - [ ] Read getting started guide
  - [ ] Review feature overview/capabilities page
  - [ ] Check API documentation overview
  - [ ] Note any "What's New" or recent releases
- [ ] **Search 1**: "tableau-pulse demo walkthrough tutorial" official capabilities
- [ ] **Search 2**: "tableau-pulse documentation" feature list complete overview
- [ ] **Search 3**: "tableau-pulse use cases" real world applications
- [ ] **Search 4**: "tableau-pulse workflow" end-to-end process

### 2B: Business User Empowerment Assessment (12 minutes)
**Compare each capability to Scoop's differentiators**

- [ ] **Search 5**: "tableau-pulse Excel integration" formula support export
  - Compare to Scoop's 150+ native Excel functions
- [ ] **Search 6**: "tableau-pulse natural language" query capabilities NLP
  - Compare to Scoop's multi-pass investigation
- [ ] **Search 7**: "tableau-pulse machine learning" AI automated analysis
  - Compare to Scoop's automatic ML (J48, JRip, EM)
- [ ] **Search 8**: "tableau-pulse self-service" business users no code
  - Compare to Scoop's 30-second setup
- [ ] **Search 9**: "tableau-pulse PowerPoint Slack integration" workflow
  - Compare to Scoop's native workflow integration
- [ ] **Search 10**: "tableau-pulse root cause analysis" investigation why
  - Compare to Scoop's multi-hypothesis testing

### 2C: Gap Analysis & Limitations (8 minutes)
- [ ] **Search 11**: "tableau-pulse limitations" cannot do missing features
- [ ] **Search 12**: "tableau-pulse vs Scoop" comparison (if exists)
- [ ] **Search 13**: "tableau-pulse requires IT" technical expertise needed
- [ ] **Search 14**: "tableau-pulse training certification" learning curve
- [ ] **Search 15**: "tableau-pulse setup time" implementation duration

### 📝 STRATEGIC FUNCTIONALITY DOCUMENTATION FORMAT
For each capability found, document with BUPAF lens:
```markdown
**Capability**: [Name of feature/function]
**What It Does**: [Clear description of functionality]
**How It Works**: [Technical mechanism if known]
**Business User Empowerment**: [Can business users use this alone? Scale 1-10]
**vs Scoop Equivalent**: [How does this compare to Scoop's approach?]
**Gaps/Limitations**: [What it can't do that Scoop can]
**Evidence**: [URL/source - especially documentation]
```

#### Key Questions for Each Capability:
1. Can a business user do this WITHOUT IT help?
2. Does it require training/certification?
3. How long from question to answer?
4. Does it work in user's existing tools (Excel/Slack/PPT)?
5. Can it investigate WHY, not just WHAT?

### Phase 2 Output Files
- [ ] Created `evidence/phase2_functionality_analysis.md`
- [ ] Documented 10+ capabilities WITH Scoop comparisons
- [ ] Identified gaps in Excel support (vs 150+ functions)
- [ ] Identified gaps in ML capabilities (vs automatic ML)
- [ ] Identified gaps in investigation (vs multi-pass)
- [ ] Identified gaps in workflow (vs 30-second integration)
- [ ] Created competitive gap matrix for sales team

---

## PHASE 3: Technical Reality & Competitive Context (30-35 minutes)

### ⚠️ PRE-PHASE 3 CHECK (2 minutes)
- [ ] **FIRST**: Review Phase 2 functionality findings
- [ ] **IDENTIFY**: Technical claims to verify from Phase 2
- [ ] **MARK**: Check off any searches that are already well-documented
- [ ] **PROCEED**: Focus on validating/invalidating functionality claims

### 3A: Technical Performance Analysis (12-15 minutes)

#### Performance Quantification
- [ ] **Search 18**: "tableau-pulse slow performance response time seconds query"
- [ ] **Search 19**: "tableau-pulse memory requirements GB RAM crashes"
- [ ] **Search 20**: "tableau-pulse concurrent users limit scalability testing"
- [ ] **Search 21**: "tableau-pulse database timeout connection errors"
- [ ] **Search 22**: "tableau-pulse uptime downtime SLA breach outage"

**📝 REMEMBER**: Document EVERY URL visited in the Research Library section (bottom of file) AS YOU GO
**Goal**: Get specific numbers - response times, memory needs, user limits, uptime stats

#### Integration Reality Check
- [ ] **Search 23**: "tableau-pulse API rate limits throttling developers"
- [ ] **Search 24**: "tableau-pulse SSO integration broken SAML authentication"
- [ ] **Search 25**: "tableau-pulse mobile app terrible performance user"
- [ ] **Search 26**: "tableau-pulse embedding iframe security CSP issues"
- [ ] **Search 27**: "tableau-pulse REST API documentation incomplete missing"

**Focus**: Real developer pain points, integration failures, technical debt

### 3B: Competitive Positioning Research (10-12 minutes)

#### Direct Competitive Intelligence
- [ ] **Search 28**: "tableau-pulse vs Tableau why customers switch"
- [ ] **Search 29**: "tableau-pulse vs ThoughtSpot RFP evaluation lost deal"
- [ ] **Search 30**: "tableau-pulse vs Qlik comparison customers choose alternative"
- [ ] **Search 31**: "tableau-pulse losing market share declining adoption 2024 2025"

#### Analyst & Market Intelligence
- [ ] **Search 32**: "tableau-pulse Gartner customers complain disappointed"
- [ ] **Search 33**: "tableau-pulse Forrester critical assessment limitations"
- [ ] **Search 34**: "tableau-pulse analyst report customer feedback negative"

**Goal**: Position in market context, understand competitive losses

### 3C: Economic Impact Deep Dive (8-10 minutes)

#### Total Cost of Ownership Reality
- [ ] **Search 35**: "tableau-pulse hidden costs professional services implementation"
- [ ] **Search 36**: "tableau-pulse training required weeks months learning curve"
- [ ] **Search 37**: "tableau-pulse consultant fees implementation partner expensive"
- [ ] **Search 38**: "tableau-pulse maintenance overhead admin full-time required"

#### ROI and Value Realization
- [ ] **Search 39**: "tableau-pulse time to value months delayed insights"
- [ ] **Search 40**: "tableau-pulse ROI negative failed to deliver business value"
- [ ] **Search 41**: "tableau-pulse opportunity cost manual reporting workarounds"

**Focus**: True costs beyond licenses, delayed value realization

### Phase 2 Success Criteria
- [ ] Documented 5+ quantified performance limitations
- [ ] Found 3+ competitive win/loss scenarios
- [ ] Calculated true TCO including hidden costs
- [ ] Identified 5+ technical integration problems
- [ ] Positioned against 3+ direct competitors

### Phase 2 Output Files
- [ ] Created/Updated `research/performance_analysis.md` - Quantified limitations
- [ ] Created/Updated `research/competitive_positioning.md` - Market context
- [ ] Created/Updated `research/integration_reality.md` - Technical limitations
- [ ] Created/Updated `research/economic_impact.md` - True TCO analysis

---

## PHASE 4: Analysis & Rich Sales Enablement (20-25 minutes)

### 4A: Evidence-Based BUPAF Scoring (8-10 minutes)

**IMPORTANT**: Use Phase 2 functionality findings as primary evidence

Score each dimension with specific evidence:

#### Independence (Can business users work alone?)
- [ ] Referenced Phase 2: Documentation requirements, training needs
- [ ] Used customer quotes about IT dependency (Phase 1)
- [ ] Cited specific setup requirements (Phase 2 & 3)
- [ ] Referenced consultant requirements (Phase 1 & 3)
- [ ] **Score: ___/10** with 3+ evidence points

#### Analytical Depth (Investigation vs single queries)
- [ ] Referenced Phase 2: ML/AI capabilities vs Scoop's automatic ML
- [ ] Compared investigation depth from Phase 2 (single vs multi-pass)
- [ ] Used performance data (response times, errors) from Phase 3
- [ ] Cited accuracy issues, inconsistent results
- [ ] **Score: ___/10** with quantified limitations

#### Workflow Integration (Excel, Slack, PowerPoint)
- [ ] Referenced Phase 2: Excel support vs Scoop's 150+ functions
- [ ] Documented workflow gaps from Phase 2
- [ ] Used developer complaints about APIs (Phase 3)
- [ ] Cited mobile/embedding limitations
- [ ] **Score: ___/10** with technical evidence

#### Business Communication (Natural language)
- [ ] Used examples of misunderstood queries
- [ ] Cited data preparation requirements
- [ ] Documented training curve evidence
- [ ] **Score: ___/10** with customer stories

#### Visual Intelligence (Presentation-ready)
- [ ] Used examples of poor visualizations
- [ ] Cited manual formatting requirements
- [ ] Documented export/sharing limitations
- [ ] **Score: ___/10** with specific examples

**TOTAL BUPAF SCORE: ___/50**
**Category**: A (35-50) / B (25-34) / C (15-24) / D (0-14)

### 4B: Competitive Capability Matrix (5 minutes)

Create comparison table based on Phase 2 functionality findings:

| Capability | tableau-pulse | Scoop | Winner | Why |
|------------|--------------|-------|--------|-----|
| Excel Support | ❌/✅ [Phase 2 finding] | ✅ 150+ functions | Scoop/Them | [Evidence] |
| ML/AI Analysis | ❌/✅ [Phase 2 finding] | ✅ Automatic ML | Scoop/Them | [Evidence] |
| Investigation Depth | ❌/✅ [Phase 2 finding] | ✅ Multi-pass | Scoop/Them | [Evidence] |
| Workflow Integration | ❌/✅ [Phase 2 finding] | ✅ 30-second | Scoop/Them | [Evidence] |
| Business User Ready | ❌/✅ [Phase 2 finding] | ✅ No training | Scoop/Them | [Evidence] |

### 4C: Rich Sales Materials Creation (5 minutes)

#### Battle Card Update
- [ ] **Top 5 Fatal Flaws** with functionality gaps from Phase 2
- [ ] **Pricing Reality** includes capability limitations
- [ ] **Customer Horror Stories** - linked to missing features
- [ ] **Competitive Matrix** - completed above

#### Customer-Facing Materials
- [ ] **Gap Analysis** - "They claim X but can't do Y" (Phase 2)
- [ ] **ROI Calculator** - Factor in missing functionality costs
- [ ] **Migration Guide** - From their limitations to our capabilities

### 4D: Quality Assurance (4-5 minutes)

#### Evidence Verification
- [ ] Every claim has customer quote or quantified data
- [ ] All pricing includes hidden/professional services costs
- [ ] Technical limitations include specific examples/metrics
- [ ] Industry issues include compliance/regulatory specifics
- [ ] Competitive positioning includes win/loss stories

### Phase 3 Success Criteria
- [ ] BUPAF scored with 15+ evidence points
- [ ] Battle card includes 5 customer stories
- [ ] Created industry-specific objection handlers
- [ ] Documented 3+ competitive loss scenarios
- [ ] Every sales claim has customer proof point

### Phase 3 Output Files
- [ ] Updated `BATTLE_CARD.md` - Customer story-driven
- [ ] Created/Updated `outputs/industry_briefings.md` - Vertical-specific
- [ ] Created/Updated `outputs/customer_case_comparisons.md` - Implementation stories
- [ ] Created/Updated `outputs/roi_risk_calculator.md` - Economic analysis
- [ ] Created/Updated `research/bupaf_evidence.md` - Detailed scoring rationale

---

## 📚 RESEARCH LIBRARY (ADD TO THIS AS YOU GO - DON'T WAIT!)

### Required Format for EVERY Entry
```
**URL**: [full URL or "No results found"]
**Date**: [today's date]
**Search Query**: [Search #X: exact query used]
**Summary**: [3-5 sentences with specific details. Include company sizes, timelines, percentages, costs mentioned]
**Relevance**: High/Medium/Low/None
**Key Evidence**: [COMPREHENSIVE - Include ALL important quotes, numbers, examples. Use bullets for multiple points:
- Full quotes with context (not fragments)
- Specific metrics (percentages, dollar amounts, timelines)
- Company details (size, industry) when mentioned
- Technical requirements or limitations
- Error messages or failure descriptions
- Multiple evidence points, not just 1-2]
---
```

### Phase 1 Research Library - Customer Discovery
**📁 Full research documented in: `evidence/phase1_customer_discovery.md`**

Key findings from Phase 1:
- Customer stories: [Top 2-3 implementation failures/complaints]
- Industry verticals: [Top 2-3 industry-specific issues]
- Community feedback: [Top 2-3 user frustrations]

### Phase 2 Research Library - Functionality Analysis
**📁 Full research documented in: `evidence/phase2_functionality_analysis.md`**

Key findings from Phase 2:
- Core capabilities: [Top 3-4 actual functions]
- Unique features: [Top 2-3 differentiators]
- Limitations: [Top 2-3 things it CANNOT do]
- Gaps vs claims: [Top 2-3 marketing vs reality]

### Phase 3 Research Library - Technical Reality
**📁 Full research documented in: `evidence/phase3_technical_reality.md`**

Key findings from Phase 3:
- Performance: [Top 2-3 performance/scalability issues]
- Integration: [Top 2-3 API/integration limitations]
- Competition: [Top 2-3 competitive weaknesses]
- Economics: [Top 2-3 cost/ROI concerns]

### Phase 4 Research Library - Sales Enablement
**📁 Full research documented in: `evidence/phase4_sales_enablement.md`**

Key findings from Phase 4:
- BUPAF Score: [Total score and category]
- Fatal flaws: [Top 2-3 deal breakers]
- Sales positioning: [Key differentiation points]

---

## SUCCESS METRICS SUMMARY

### Depth Benchmarks Achieved
- [ ] **Customer Stories**: 10+ implementation experiences
- [ ] **Quantified Data**: 15+ specific metrics (response times, costs, limits)
- [ ] **Industry Analysis**: 5+ verticals covered
- [ ] **Competitive Context**: 3+ direct competitor comparisons
- [ ] **Economic Impact**: True TCO with hidden costs
- [ ] **Technical Reality**: Developer/IT perspective included

### Quality Indicators Met
- [ ] **Evidence Strength**: Customer stories > vendor docs > analyst reports > blogs
- [ ] **Specificity**: Numbers/dates/companies > vague claims
- [ ] **Recency**: Sources <6 months preferred, <12 months acceptable
- [ ] **Diversity**: Multiple source types, industries, company sizes
- [ ] **Actionability**: Sales team can use immediately with confidence

---

## FINAL OUTPUT CHECKLIST

### Research Documentation
- [ ] `research/existing_research.md` - What was already known
- [ ] `research/customer_stories.md` - Implementation experiences
- [ ] `research/industry_analysis.md` - Vertical limitations
- [ ] `research/performance_analysis.md` - Quantified limitations
- [ ] `research/competitive_positioning.md` - Market context
- [ ] `research/integration_reality.md` - Technical limitations
- [ ] `research/economic_impact.md` - True TCO analysis
- [ ] `research/bupaf_evidence.md` - Scoring rationale

### Evidence Collection
- [ ] `evidence/phase1_research_library.md` - Phase 1 research with all URLs and findings
- [ ] `evidence/phase2_research_library.md` - Phase 2 technical research documentation
- [ ] `evidence/phase3_research_library.md` - Phase 3 analysis and evidence
- [ ] `evidence/customer_quotes.md` - Consolidated key quotes from all phases
- [ ] `evidence/community_sources.md` - Forum/Reddit findings summary

### Sales Enablement
- [ ] `BATTLE_CARD.md` - Updated with customer stories
- [ ] `outputs/industry_briefings.md` - Vertical-specific content
- [ ] `outputs/customer_case_comparisons.md` - Implementation stories
- [ ] `outputs/roi_risk_calculator.md` - Economic analysis

---

## NOTES & OBSERVATIONS
<!-- Add any additional insights, patterns, or observations discovered during research -->

---

*Template designed for manual execution with comprehensive tracking, partial reset capability, and systematic evidence collection.*