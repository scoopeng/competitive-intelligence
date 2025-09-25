# Competitor Research Template V2 - Complete Protocol with Functionality Analysis

**Time**: 120-150 minutes for comprehensive, evidence-based competitive intelligence
**Quality**: Enterprise-grade with functionality mapping, implementation stories, quantified data, and research library
**Version**: 2.0 - Added Phase 2 Functionality Deep Dive

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
- **Time management**: If any phase exceeds time limit, prioritize high-value searches
- **Conflicting evidence**: Document both viewpoints in NOTES section with sources

### 4. RESEARCH LIBRARY ORGANIZATION
**All research is stored in separate files for better organization:**
- **Phase 1**: Create `evidence/phase1_research_library.md` (Customer Discovery)
- **Phase 2**: Create `evidence/phase2_functionality_analysis.md` (What It Actually Does)
- **Phase 3**: Create `evidence/phase3_technical_reality.md` (Technical Deep Dive)
- **Phase 4**: Create `evidence/phase4_sales_enablement.md` (BUPAF & Materials)
- **In main checklist**: Reference each file with 5-8 key findings summary
- **Benefit**: Keeps checklist clean and research fully documented

## Research Status Tracker
### Overall Progress
- [ ] Archive recovery completed
- [ ] Customer discovery completed (17 searches)
- [ ] Functionality analysis completed (NEW - 15 searches)
- [ ] Technical analysis completed (24 searches)
- [ ] BUPAF scoring completed with evidence
- [ ] Battle card updated
- [ ] Sales materials created
- [ ] Research library fully documented

### Phase Status (Mark X to reset phase)
- [ ] Reset Phase 1: Customer Discovery & Stories
- [ ] Reset Phase 2: Functionality Deep Dive (NEW)
- [ ] Reset Phase 3: Technical Reality & Competitive Context
- [ ] Reset Phase 4: Analysis & Sales Enablement

### Last Research Date
- **Phase 0**: Never / [Date]
- **Phase 1**: Never / [Date]
- **Phase 2**: Never / [Date]
- **Phase 3**: Never / [Date]
- **Phase 4**: Never / [Date]

---

## PHASE 0: Existing Assets Check (5 minutes)

### Archive & Evidence Recovery
- [ ] Checked `../../archive/` for any {COMPETITOR} related files
- [ ] Checked `../../evidence/` for existing {COMPETITOR} content
- [ ] Listed all existing files in `competitors/{competitor}/` directory
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

## PHASE 1: Deep Discovery & Customer Stories (30-40 minutes)

### ⚠️ PRE-PHASE 1 CHECK (2 minutes)
- [ ] **FIRST**: Check if phase1_research_library.md already exists
- [ ] **IDENTIFY**: Which searches have already been completed successfully
- [ ] **MARK**: Check off any searches below that are already well-documented
- [ ] **PROCEED**: Only execute searches that haven't been done or need better results

### 1A: Customer Review Mining (10 minutes)
Execute these WebSearch queries:

- [ ] **Search 1**: "site:g2.com {COMPETITOR} 1 star 2 star reviews implementation disaster"
- [ ] **Search 2**: "site:capterra.com {COMPETITOR} negative review switching from"
- [ ] **Search 3**: "site:trustradius.com {COMPETITOR} disappointed regret choosing"
- [ ] **Search 4**: "{COMPETITOR} implementation failed timeline overrun consultant expensive"

### 1B: Reddit & Community Sentiment (5 minutes)
- [ ] **Search 5**: "site:reddit.com r/BusinessIntelligence {COMPETITOR} problems limitations"
- [ ] **Search 6**: "site:reddit.com r/analytics {COMPETITOR} switching from because"
- [ ] **Search 7**: "site:reddit.com {COMPETITOR} horror story disaster experience"
- [ ] **Search 8**: "site:community.{competitor}.com error doesn't work broken"

### 1C: Professional Network Analysis (5 minutes)
- [ ] **Search 9**: "site:linkedin.com {COMPETITOR} disappointed moving from consultant"
- [ ] **Search 10**: "site:linkedin.com data analyst BI manager {COMPETITOR} challenges"

### 1D: Industry-Specific Horror Stories (10 minutes)
- [ ] **Search 11**: "{COMPETITOR} healthcare HIPAA compliance failed implementation"
- [ ] **Search 12**: "{COMPETITOR} financial services bank switching accuracy issues"
- [ ] **Search 13**: "{COMPETITOR} retail manufacturing implementation disaster"

### 1E: Switching & Migration Stories (5 minutes)
- [ ] **Search 14**: "switched from {COMPETITOR} to" migration story
- [ ] **Search 15**: "migrating off {COMPETITOR}" problems issues
- [ ] **Search 16**: "{COMPETITOR} vs competitor" why we chose
- [ ] **Search 17**: "{COMPETITOR} abandoned project failed rollback"

---

## 🆕 PHASE 2: Functionality Deep Dive (30 minutes)

### ⚠️ CRITICAL: UNDERSTAND WHAT IT ACTUALLY DOES
**This phase focuses on understanding the actual capabilities, not just problems**

### 2A: Core Functionality Research (10 minutes)
- [ ] **Search 1**: "{COMPETITOR} demo walkthrough tutorial" official capabilities
- [ ] **Search 2**: "{COMPETITOR} features list" complete functionality overview
- [ ] **Search 3**: "{COMPETITOR} use cases" real world applications examples
- [ ] **Search 4**: "{COMPETITOR} workflow" end-to-end process demonstration
- [ ] **Search 5**: "{COMPETITOR} getting started guide" basic operations

### 2B: Specific Capabilities Analysis (10 minutes)
- [ ] **Search 6**: "{COMPETITOR} data sources" supported connections integrations
- [ ] **Search 7**: "{COMPETITOR} visualization types" charts graphs outputs
- [ ] **Search 8**: "{COMPETITOR} analysis capabilities" statistical ML AI features
- [ ] **Search 9**: "{COMPETITOR} collaboration features" sharing permissions workflow
- [ ] **Search 10**: "{COMPETITOR} automation scheduling" alerts notifications

### 2C: Differentiation Research (10 minutes)
- [ ] **Search 11**: "{COMPETITOR} unique features" competitive advantages
- [ ] **Search 12**: "{COMPETITOR} vs alternatives" feature comparison matrix
- [ ] **Search 13**: "{COMPETITOR} limitations" cannot do missing features
- [ ] **Search 14**: "{COMPETITOR} roadmap" upcoming planned features
- [ ] **Search 15**: "{COMPETITOR} customer success stories" best implementations

### 📝 FUNCTIONALITY DOCUMENTATION FORMAT
For each capability found, document:
```markdown
**Capability**: [Name of feature/function]
**What It Does**: [Clear description of functionality]
**How It Works**: [Technical mechanism if known]
**User Benefit**: [What problem it solves]
**Limitations**: [What it can't do]
**Evidence**: [URL/source]
```

---

## PHASE 3: Technical Reality & Competitive Context (40-50 minutes)

### ⚠️ PRE-PHASE 3 CHECK (2 minutes)
- [ ] **FIRST**: Review Phase 2 functionality findings
- [ ] **IDENTIFY**: Technical claims to verify
- [ ] **FOCUS**: Target searches on validating/invalidating functionality claims

### 3A: Performance & Scalability (10 minutes)
- [ ] **Search 18**: "{COMPETITOR} performance benchmark response time slow"
- [ ] **Search 19**: "{COMPETITOR} memory requirements CPU crashes"
- [ ] **Search 20**: "{COMPETITOR} concurrent users limits scalability"
- [ ] **Search 21**: "{COMPETITOR} database timeout connection errors"
- [ ] **Search 22**: "{COMPETITOR} uptime SLA outage downtime"

### 3B: Integration & Developer Experience (10 minutes)
- [ ] **Search 23**: "{COMPETITOR} API limitations rate limits developers"
- [ ] **Search 24**: "{COMPETITOR} SSO integration broken SAML"
- [ ] **Search 25**: "{COMPETITOR} mobile app terrible performance"
- [ ] **Search 26**: "{COMPETITOR} embedding iframe security issues"
- [ ] **Search 27**: "{COMPETITOR} REST API documentation incomplete"

### 3C: Competitive Positioning (15 minutes)
- [ ] **Search 28**: "{COMPETITOR} vs Power BI" comparison advantages
- [ ] **Search 29**: "{COMPETITOR} vs ThoughtSpot" evaluation lost deal
- [ ] **Search 30**: "{COMPETITOR} vs Qlik" customers choose alternative
- [ ] **Search 31**: "{COMPETITOR} losing market share" declining adoption
- [ ] **Search 32**: "{COMPETITOR} Gartner" critical assessment limitations
- [ ] **Search 33**: "{COMPETITOR} Forrester" wave quadrant position
- [ ] **Search 34**: "{COMPETITOR} analyst report" customer feedback

### 3D: Economic Impact & TCO (15 minutes)
- [ ] **Search 35**: "{COMPETITOR} hidden costs" professional services implementation
- [ ] **Search 36**: "{COMPETITOR} training required" weeks months learning
- [ ] **Search 37**: "{COMPETITOR} consultant fees" implementation partner
- [ ] **Search 38**: "{COMPETITOR} maintenance overhead" admin full-time
- [ ] **Search 39**: "{COMPETITOR} time to value" months delayed insights
- [ ] **Search 40**: "{COMPETITOR} ROI negative" failed business value
- [ ] **Search 41**: "{COMPETITOR} opportunity cost" manual reporting workarounds

---

## PHASE 4: Analysis & Sales Enablement (20-30 minutes)

### 4A: Evidence-Based BUPAF Scoring (10 minutes)

**IMPORTANT**: Reference Phase 2 functionality findings to score accurately

#### Independence (Can business users work alone?)
- [ ] Used customer quotes about IT dependency
- [ ] Cited specific setup requirements (weeks/months)
- [ ] Referenced consultant requirements
- [ ] **Score: ___/10** with 3+ evidence points

#### Analytical Depth (Investigation vs single queries)
- [ ] Used performance data (response times, errors)
- [ ] Cited accuracy issues, inconsistent results
- [ ] Referenced Phase 2 actual capabilities vs claims
- [ ] **Score: ___/10** with quantified limitations

#### Workflow Integration (Excel, Slack, PowerPoint)
- [ ] Documented specific integration failures
- [ ] Used developer complaints about APIs
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

### 4B: Competitive Differentiation Matrix (10 minutes)

Create comparison table based on Phase 2 findings:

| Capability | {COMPETITOR} | Scoop | Winner | Why |
|------------|--------------|-------|--------|-----|
| [Function 1] | ❌/✅ Details | ✅ Details | Scoop/Them | Evidence |
| [Function 2] | ❌/✅ Details | ✅ Details | Scoop/Them | Evidence |
| [Function 3] | ❌/✅ Details | ✅ Details | Scoop/Them | Evidence |

### 4C: Sales Materials Creation (10 minutes)

#### Battle Card Update
- [ ] **Top 5 Fatal Flaws** with functionality gaps identified
- [ ] **Pricing Reality** includes capability limitations
- [ ] **Customer Horror Stories** linked to missing features
- [ ] **Functionality Comparison** from Phase 2
- [ ] **Competitive Context** positioning vs alternatives

#### Customer-Facing Materials
- [ ] **Capability Gap Analysis** - "They claim X but can't do Y"
- [ ] **ROI Calculator** - Factor in missing functionality costs
- [ ] **Migration Guide** - From their limitations to our capabilities

---

## Research Library Sections

### Phase 0 Existing Assets
<!-- Document any recovered files and existing research here -->

### Phase 1 Research Library
**📁 Phase 1 Research documented in: `evidence/phase1_research_library.md`**

### Phase 2 Functionality Analysis
**📁 Phase 2 Functionality documented in: `evidence/phase2_functionality_analysis.md`**

### Phase 3 Technical Reality
**📁 Phase 3 Technical documented in: `evidence/phase3_technical_reality.md`**

### Phase 4 Sales Enablement
**📁 Phase 4 Analysis documented in: `evidence/phase4_sales_enablement.md`**

---

## SUCCESS METRICS SUMMARY

### Customer Evidence Found
- [ ] 5+ implementation failure stories
- [ ] 3+ cost overrun examples
- [ ] 3+ performance complaints
- [ ] 5+ migration stories

### Functionality Mapped
- [ ] Core capabilities documented
- [ ] Limitations identified
- [ ] Gaps vs claims exposed
- [ ] Competitive advantages clear

### Technical Reality
- [ ] Performance limits quantified
- [ ] Integration gaps documented
- [ ] Scalability issues proven
- [ ] True costs calculated

### Sales Enablement
- [ ] BUPAF score evidence-based
- [ ] Battle card updated
- [ ] Functionality gaps weaponized
- [ ] Objection handlers created

---

## NOTES SECTION
<!-- Add any special observations, conflicting evidence, or unique findings here -->

---

*Template Version 2.0 - Added Phase 2 Functionality Deep Dive*
*Estimated Time: 120-150 minutes total*
*Quality Standard: Enterprise-grade competitive intelligence*