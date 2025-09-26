# Phase 4: Analysis & Sales Enablement - Sisense
**Date**: September 26, 2025
**Time**: Starting Phase 4 - BUPAF Scoring

## 4A: Evidence-Based BUPAF Scoring

### Business User Independence (Can business users work alone?)
**Score: 2/10**

**Evidence from Phase 2**:
- "Requires significant IT involvement (14+ weeks typical implementation)"
- "ElastiCube requires SQL knowledge" despite "codeless" claims
- "30-80 hours of training needed"
- "Users are viewers, not creators"
- "Best suited for companies with technical teams"

**Evidence from Phase 1**:
- "8-14 weeks of development work" typical
- "Long implementation times, back-end requires technical expertise"
- "Steep learning curve, poor documentation"
- "No strong community support"

**Evidence from Phase 3**:
- "Weeks or months" for full workflows
- Self-hosted requires "deep technical expertise"
- "Elasticube not user-friendly, requires SQL despite 'codeless' claims"

**Conclusion**: Business users cannot work independently. Sisense requires extensive IT support, SQL knowledge, and weeks of training. The platform is designed for technical teams, not business users.

### Unified Experience (Workflow Integration)
**Score: 1/10**

**Evidence from Phase 2**:
- "ZERO Excel formula support (export only, no live formulas)"
- "No investigation capability (single queries only)"
- "Portal-based architecture (no native workflow integration)"
- "No PowerPoint generation"
- "No Slack beyond basic notifications"

**Evidence from Phase 1**:
- "Mobile experience isn't really as abundant as I'd like"
- "Embedding visuals difficult, don't always work"

**Evidence from Phase 3**:
- "Mobile was certainly an afterthought"
- "Users must reinstall weekly"
- "Cannot resize meaningfully, pivot tables don't scroll"
- "iFrame loads entire BI app, inherently slower"

**Conclusion**: Sisense is a portal prison. Zero Excel integration, no PowerPoint capability, broken mobile app, and embedding issues make it impossible to work in existing workflows.

### Power & Flexibility (Analytics Depth)
**Score: 4/10**

**Evidence from Phase 2**:
- "Simply Ask (DEPRECATED) - Natural language failed"
- "ARIMA from 1970s" marketed as AI
- "Single queries only, no multi-pass"
- "Template-based NLQ, not true understanding"
- "AutoML requires technical configuration"

**Evidence from Phase 1**:
- "Out of the box is best version, changing requires code"
- "Cannot change font size/color without scripting"

**Evidence from Phase 3**:
- "Query Timeout: Default 300 seconds (5 minutes)"
- "Many-to-many relationships cause 'extreme slowness'"
- "Response sizes over 10KB cause degradation"

**Conclusion**: Limited analytics capabilities with deprecated AI, 1970s statistics marketed as ML, single-query only system that times out. No investigation capability.

### Automation (Self-Service Analytics)
**Score: 3/10**

**Evidence from Phase 2**:
- "14+ weeks implementation, then 3-4 hours per report"
- "Build to Destination requires CDWH configuration"
- "Export to Excel V2 - still just export, no live connection"

**Evidence from Phase 3**:
- "Reporting: Manual, repetitive, hard to scale"
- "Python scripts for PDFs, filters" required as workarounds
- "Report Manager needed for automation" (add-on)
- "Coding each job took a lot of time"

**Conclusion**: Minimal automation capabilities. Requires manual workarounds, Python scripts, and add-ons for basic automation. Even scheduled reports are limited.

### Findability (Discovery & Search)
**Score: 2/10**

**Evidence from Phase 2**:
- "Requires exact terminology for search"
- "Template-based NLQ, not true understanding"
- "Simply Ask being deprecated" (their search failed)

**Evidence from Phase 3**:
- "3 API Versions with incomplete migration"
- "Documentation fragmented across sites"
- "Examples incomplete with ellipsis"

**Conclusion**: Search capabilities have failed (Simply Ask deprecated). Requires exact terminology, no true natural language understanding, and documentation is fragmented.

### **TOTAL BUPAF SCORE: 12/50**
**Category: D - Marketing Mirage**

---

## 4B: Competitive Capability Matrix

| Capability | Sisense | Scoop | Winner | Evidence |
|------------|---------|-------|--------|----------|
| Excel Support | ❌ Zero formulas | ✅ 150+ functions | **Scoop** | "Export only, no live formulas" |
| ML/AI Analysis | ❌ ARIMA from 1970s | ✅ Automatic ML | **Scoop** | "Simply Ask deprecated, ARIMA isn't AI" |
| Investigation Depth | ❌ Single query | ✅ 3-10 queries | **Scoop** | "No multi-pass, no context retention" |
| Workflow Integration | ❌ Portal only | ✅ 30-second | **Scoop** | "Zero Excel, no PPT, mobile broken" |
| Business User Ready | ❌ 14+ weeks | ✅ No training | **Scoop** | "Requires SQL, weeks of training" |
| Setup Time | ❌ 8-14 weeks | ✅ 30 seconds | **Scoop** | "$89k/14 weeks for 'plug-and-play'" |
| True Cost | ❌ $25k-$327k | ✅ $3,588 | **Scoop** | "400% renewal increases" |
| Performance | ❌ 5-min timeout | ✅ Instant | **Scoop** | "RAM crashes, 10KB degradation" |
| Documentation | ❌ Fragmented | ✅ Complete | **Scoop** | "Spread across multiple sites" |
| Market Position | ❌ 0.01% share | ✅ Growing | **Scoop** | "13% layoffs, pivoting away" |

---

## 4C: Fatal Flaws for Sales Positioning

### 1. The 400% Renewal Trap
**Evidence**: Multiple sources confirm "400% price increase at renewal time"
- Year 1: Reasonable price to lock you in
- 14 weeks implementation creates switching costs
- Year 2: Price quadrupled when trapped
- One customer switched in 72 hours, saved $94,000

### 2. The Fake AI Deception
**Evidence**: "ARIMA from 1970s marketed as AI"
- Simply Ask deprecated because it failed
- ARIMA is time-series statistics, not AI
- No real ML capabilities
- "Template-based NLQ, not true understanding"

### 3. The Excel Void
**Evidence**: "ZERO Excel formula support"
- Export only, no live formulas
- Cannot do VLOOKUP, SUMIFS, nothing
- Static CSV dumps only
- vs Scoop's 150+ live Excel functions

### 4. The Implementation Nightmare
**Evidence**: "14 weeks/$89k for 'plug-and-play'"
- 8-14 weeks standard implementation
- $10k-$50k implementation costs
- "Weeks or months" for training
- Requires SQL despite "no code" claims

### 5. The Performance Collapse
**Evidence**: Multiple performance failures
- "Main cube crashed week 2, couldn't resurrect"
- "15-minute chart refresh times"
- "RAM crashes with memory not released"
- "Weekly mobile app reinstalls required"

---

## Killer Sales Questions

### Discovery Phase
1. "What's your total Sisense cost including implementation?" (Expect $100k+)
2. "How long was your implementation?" (8-14 weeks typical)
3. "Can you show me Excel formulas working?" (They can't)
4. "What happened at renewal?" (400% increase likely)
5. "How's the mobile app working?" (Weekly reinstalls)

### Demo Comparison Points
1. **Excel Test**: Upload file with formulas
   - Sisense: All formulas break
   - Scoop: 150+ functions work live

2. **AI Test**: "Why did sales drop?"
   - Sisense: Single query, no investigation
   - Scoop: 3-10 query investigation with ML

3. **Setup Test**: Time to first insight
   - Sisense: 8-14 weeks
   - Scoop: 30 seconds

4. **Cost Test**: Total for 100 users
   - Sisense: $200k+ with renewals
   - Scoop: $3,588 flat

---

## Objection Handlers

**"Sisense has embedded analytics"**
"Yes, for ISVs building software products, not enterprises empowering business users. It requires Compose SDK with developers. After 14 weeks and $89k, you get a portal that can't do Excel formulas. That's not business empowerment."

**"They have AI capabilities"**
"They market ARIMA from the 1970s as AI. Their actual AI attempt, Simply Ask, was deprecated because it failed. For $200k+ per year, you get statistics older than most of your employees."

**"It's an established platform"**
"With 0.01% market share, 13% layoffs in 2024, and 400% renewal increases. They're pivoting away from BI because the platform failed. One customer's main cube crashed in week 2 and couldn't be resurrected."

**"We need scalability"**
"Sisense has 5-minute timeouts, RAM crashes that don't release memory, and performance degradation at 10KB responses. Mobile users reinstall weekly. That's not scalability, it's instability."

---

## The Winning Pitch

"Sisense is an embedded analytics platform for ISVs that takes 14 weeks and $89,000 to implement, then quadruples your price at renewal. They market ARIMA from the 1970s as AI while their actual AI attempt failed and was deprecated.

With zero Excel formula support, no investigation capability, and a mobile app that requires weekly reinstalls, it's a portal prison that locks you in with switching costs then hits you with 400% increases.

At 0.01% market share with 13% layoffs, they're pivoting away from BI. One customer's elastic cube crashed in week 2 and couldn't be resurrected. Another pays $100k for 'tables and basic graphs.'

Scoop provides 150+ live Excel functions, automatic ML investigation, and 30-second setup for $3,588 flat. You're paying 56x more for a platform that can't even do VLOOKUP.

Would you like to see real AI find root causes in your actual Excel files?"

---

## Supporting Evidence Summary

### From Phase 1 (Customer Discovery)
- 400% renewal increases (multiple sources)
- 14-week implementations typical
- $100k for "tables and basic graphs"
- "Main cube crashed week 2"
- "Worse than cold spaghetti" architecture

### From Phase 2 (Functionality Analysis)
- ZERO Excel formulas
- Simply Ask deprecated
- ARIMA from 1970s
- No investigation capability
- Portal-only architecture

### From Phase 3 (Technical Reality)
- 0.01% market share
- 13% layoffs in 2024
- 5-minute timeouts
- RAM crashes
- Weekly mobile reinstalls

### From Phase 4 (BUPAF Analysis)
- Score: 12/50 (Marketing Mirage)
- 2/10 Business Independence
- 1/10 Workflow Integration
- Failed on every dimension

---

*Sisense is a cautionary tale of vendor lock-in, fake AI, and pricing shock. Use these evidence-based insights to protect prospects from the 400% renewal trap.*