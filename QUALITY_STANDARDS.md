# Quality Standards & Assurance

**Purpose**: Comprehensive quality standards for competitive intelligence research and framework verification
**Version**: 2.0 (Consolidated from 3 separate QA files)
**Last Updated**: September 27, 2025

---

## Table of Contents
1. [Framework Verification (100-Point System)](#section-1-framework-verification)
2. [Research Quality Checklist](#section-2-research-quality-checklist)
3. [Research Best Practices](#section-3-research-best-practices)

---

# SECTION 1: Framework Verification (100-Point System)

## Purpose
Verify all competitive intelligence files are correct and consistent with the 100-point BUA framework.

**Context**: Completed major framework redesign from 59-point to 100-point system. All 12 competitors rescored and files updated.

---

## What to Verify

### 1.1 Framework Scoring Files (12 files)
**Location**: `competitors/*/evidence/framework_scoring.md`

**Check Each File For**:
- ✅ **Header** shows: `Total Score: X/100 (Y%, Category Z)`
- ✅ **Dimensions** all show `/20` (not /10, /16, /13, etc.)
- ✅ **Sub-components** match this structure:
  - Autonomy (/20): Setup /8, Questions /6, Speed /6
  - Flow (/20): Native Integration /8, Portal Prison /6, Interface Simplicity /6
  - Understanding (/20): Investigation /8, ML /6, Explanation /6
  - Presentation (/20): Automatic Generation /8, Brand Control /6, Distribution /6
  - Data (/20): Multi-Source /4, Schema Evolution /8, Data Quality /4, Data Prep /4
- ✅ **Math is correct**: Sub-components add to dimension, dimensions add to total
- ✅ **Category matches score**:
  - A+ Elite (85-100)
  - A Strong (70-84)
  - B Good (55-69)
  - C Moderate (40-54)
  - C Weak (25-39)
  - D Poor (0-24)
- ✅ **No old references**: No "/50", "/59", "BUPAF", "Marketing Mirage"
- ✅ **Date**: September 27, 2025 or later

**Expected Scores** (verify these exactly):
```
Scoop: 82/100 (A Strong)
Domo: 62/100 (B Good)
ThoughtSpot: 57/100 (B Good)
Qlik: 47/100 (C Moderate)
Zenlytic: 42/100 (C Moderate)
Tableau Pulse: 37/100 (C Weak)
Power BI Copilot: 32/100 (D Weak)
Sisense: 28/100 (C Weak)
Snowflake Cortex: 26/100 (C Weak)
DataGPT: 22/100 (D Poor)
Tellius: 22/100 (D Poor)
DataChat: 17/100 (D Poor)
```

### 1.2 Battle Cards (11 files)
**Location**: `competitors/*/BATTLE_CARD.md`

**Check Each File For**:
- ✅ **Header** shows: `BUA Score: X/100 (Y%, Category Z)`
- ✅ **Score matches** framework_scoring.md
- ✅ **Category name** is correct (not old names)
- ✅ **No "/50" or "/59"** anywhere

### 1.3 README Files (11 files)
**Location**: `competitors/*/README.md`

**Check Each File For**:
- ✅ **BUA Score** (if mentioned) matches framework_scoring.md
- ✅ **Category** matches framework_scoring.md
- ✅ **No "BUPAF"** (should be "BUA")
- ✅ **No "/50" or "/59"** in scoring references

### 1.4 Web Comparisons (11 files)
**Location**: `competitors/*/outputs/web_comparison.md`

**Check Each File For**:
- ✅ **File exists**
- ✅ **Header** shows competitor score as X/100
- ✅ **Last Updated**: September 27, 2025
- ✅ **Score matches** framework_scoring.md
- ✅ **Word count**: 4,000+ words minimum
- ✅ **No old references**: No /50, /59, BUPAF

### 1.5 Core Framework Document (1 file)
**Location**: `framework/BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md`

**Check**:
- ✅ **Structure**: Shows 5 dimensions × 20 points = 100 total
- ✅ **Categories**: Use 100-point ranges (not 50-point)
- ✅ **Examples**: Use 100-point scores
- ✅ **No old references**: No /50, /59 system

---

## How to Verify Mathematical Accuracy

For each framework_scoring.md file:

1. **Extract dimension scores** from these lines:
   - `## Dimension 1: Autonomy (X/20)`
   - `## Dimension 2: Flow (X/20)`
   - `## Dimension 3: Understanding (X/20)`
   - `## Dimension 4: Presentation (X/20)`
   - `## Dimension 5: Data (X/20)`

2. **Add them up**: Sum of all 5 dimensions

3. **Compare to header**: Does sum match `Total Score: X/100`?

4. **Check sub-components**: Do they add to dimension total?

**Example (Power BI Copilot)**:
- Autonomy: 7/20 (should be 2+3+2 = 7) ✅
- Flow: 6/20 (should be 3+0+3 = 6) ✅
- Understanding: 7/20 (should be 2+0+5 = 7) ✅
- Presentation: 6/20 (should be 3+1+2 = 6) ✅
- Data: 6/20 (should be 1+0+3+2 = 6) ✅
- **Total**: 7+6+7+6+6 = 32/100 ✅

---

## Critical Issues to Flag

**Priority 1 (Blocker)**:
- ❌ Math doesn't add up (dimensions ≠ total)
- ❌ Score mismatch between files (framework_scoring.md vs battle card)
- ❌ Wrong dimension structure (not /20)
- ❌ Category doesn't match score range

**Priority 2 (Important)**:
- ⚠️ Old references still present (/50, /59, BUPAF)
- ⚠️ Missing sub-component scores
- ⚠️ Outdated dates (before Sept 27, 2025)

**Priority 3 (Nice to Fix)**:
- 💡 Web comparison under 4,000 words
- 💡 Missing evidence citations
- 💡 Formatting inconsistencies

---

## Quick Verification Commands

```bash
# Check all framework scoring totals
for comp in scoop power-bi-copilot tableau-pulse thoughtspot snowflake-cortex domo qlik zenlytic sisense datagpt tellius datachat; do
  echo "=== $comp ==="
  grep "Total Score:" competitors/$comp/evidence/framework_scoring.md | head -1
done

# Check for old references in active files
grep -r "/50\|/59\|BUPAF" competitors/*/evidence/framework_scoring.md
grep -r "/50\|/59\|BUPAF" competitors/*/BATTLE_CARD.md
grep -r "/50\|/59\|BUPAF" competitors/*/README.md

# Verify dimension structure
for comp in scoop power-bi-copilot tableau-pulse thoughtspot; do
  echo "=== $comp ==="
  grep "^## Dimension" competitors/$comp/evidence/framework_scoring.md
done

# Check web comparison existence and word count
for comp in power-bi-copilot tableau-pulse thoughtspot snowflake-cortex domo qlik zenlytic sisense datagpt tellius datachat; do
  file="competitors/$comp/outputs/web_comparison.md"
  if [ -f "$file" ]; then
    wc=$(wc -w "$file" | awk '{print $1}')
    echo "✓ $comp: $wc words"
  else
    echo "✗ $comp: MISSING"
  fi
done
```

---

# SECTION 2: Research Quality Checklist

## Purpose
Ensure all competitive research meets factual accuracy and credibility standards.

---

## How to Use This Checklist

1. **Before Publishing**: Run every document through this checklist
2. **During Review**: Check off each item as verified
3. **On Failure**: Fix the issue, document what was wrong
4. **Update Checklist**: Add new checks as we discover new issues

---

## 2.1 SCOOP FACTUAL ACCURACY

### Capabilities - What Scoop HAS ✅
- [ ] **In-Memory Spreadsheet Engine**: 150+ Excel functions for data prep and transformation (NOT a =SCOOP() function)
- [ ] **Google Sheets Plugin**: Utility functions to pull/refresh Scoop data into spreadsheets
- [ ] **Multi-Pass Investigation**: 3-10 queries, stateful conversation, builds on previous context
- [ ] **AI Data Scientist Engine**: Three-layer system (auto data prep + real ML models + AI explanation)
  - Layer 1: Automatic data prep (cleaning, binning, feature engineering)
  - Layer 2: Real ML (J48 trees 800+ nodes, JRip rules, EM clustering)
  - Layer 3: AI explains complex model output in business language
- [ ] **Visual Intelligence**: Generates PowerPoint presentations automatically
- [ ] **30-Second Setup**: No data modeling, no training, no complex configuration
- [ ] **Works in Existing Tools**: Spreadsheet engine, Slack (bot), PowerPoint (generation)

### Capabilities - What Scoop DOES NOT HAVE ❌
- [ ] **NO =SCOOP() Excel Function**: We have a spreadsheet ENGINE, not a spreadsheet function
- [ ] **NO Public Developer API**: Scoop mobile API is internal use only - DO NOT claim SDK/API access
- [ ] **NO HIPAA Certification**: Not certified, not compliant, not "HIPAA ready"
- [ ] **NO FedRAMP Authorization**: Not authorized for government use
- [ ] **NO SOC1 Certification**: Only SOC2 certified
- [ ] **NO Python SDK**: We don't use Python internally, don't mention it
- [ ] **NO JavaScript SDK**: No public SDK exists
- [ ] **NO Mobile Developer API**: Internal only, not for customer developers
- [ ] **NO Statistical Tests**: We use ML models, not p-values or statistical significance tests
- [ ] **NO International Expansion Yet**: US market focus only currently

### Compliance & Certifications - EXACT FACTS
- [ ] **SOC2 Certified**: This is accurate - we have SOC2 Type II
- [ ] **NOT HIPAA**: Never claim HIPAA compliance, certification, or readiness
- [ ] **NOT FedRAMP**: Never claim FedRAMP authorization or government cloud
- [ ] **Check Before Claiming**: If unsure about compliance, DO NOT claim it

### Pricing & Cost - FLEXIBLE NOT FIXED
- [ ] **NO Specific Pricing**: Don't use "$3,588/year" or any specific number
- [ ] **Use Relative Language**: "a small fraction of the cost", "20-30x less expensive"
- [ ] **Use Ranges if Needed**: "Scoop costs thousands annually vs hundreds of thousands"
- [ ] **Let Sales Handle**: Don't lock in specific pricing in content

### Resource Requirements - REALISTIC NOT ZERO
- [ ] **NO Zero FTE Claims**: Don't say "zero maintenance" or "no IT involvement"
- [ ] **Use Reduction Language**: "1/5 the FTE requirement", "reduces by 80%"
- [ ] **Be Honest**: Some setup/maintenance exists, just far less than competitors

### Technical Accuracy - AI DATA SCIENTIST ENGINE
- [ ] **Three-Layer Architecture**: Always describe all three layers (data prep + ML + AI explanation)
- [ ] **Real ML Models**: J48 decision trees (can be 800+ nodes), JRip rules, EM clustering
- [ ] **Automatic Data Prep**: Emphasize cleaning, binning, feature engineering happens automatically
- [ ] **AI Explanation Layer**: Models produce complex output, AI explains in business language
- [ ] **NOT Just Rules**: Don't oversimplify - we run sophisticated ML then explain it
- [ ] **NO P-Values**: We don't provide statistical significance (p < 0.05)
- [ ] **NO Statistical Tests**: We run ML models, not statistical hypothesis tests
- [ ] **NO Tech Stack Details**: Don't mention internal languages (Python, etc.)

---

## 2.2 COMPETITOR FACTUAL ACCURACY

### Cost Claims - CREDIBLE & VERIFIABLE
- [ ] **Source Required**: Every cost claim must have URL + date from competitor documentation
- [ ] **Realistic Ranges**: Use documented pricing, not inflated estimates
- [ ] **Include All Components**: License + implementation + maintenance (document each)
- [ ] **Red Flag Test**: Does this number pass the "would they publish this?" test?
- [ ] **Conservative Bias**: If unsure between two estimates, use the lower one

#### Cost Claim Checklist
- [ ] Base license cost documented with source URL
- [ ] Implementation cost documented (if included)
- [ ] Annual maintenance/support documented (if included)
- [ ] Hidden costs itemized (semantic models, consulting, training)
- [ ] Total cost calculation shows math
- [ ] Does NOT exceed 100x Scoop cost (red flag if it does)

### Capability Claims - EVIDENCE REQUIRED
- [ ] **Official Documentation**: Link to competitor's own docs/website
- [ ] **Customer Reviews**: G2, Reddit, LinkedIn posts with URLs
- [ ] **Test Results**: Our own benchmarking with methodology documented
- [ ] **NO Speculation**: If we didn't test it or find documentation, don't claim it

### Customer Quotes - REAL & SOURCED
- [ ] **Full URL**: Every quote needs source link
- [ ] **Date Captured**: When was this quote published/captured
- [ ] **Context Preserved**: Don't cherry-pick, show enough context
- [ ] **Verbatim**: Use exact quotes, note [...] for omissions

### ROI & Business Impact - CONSERVATIVE
- [ ] **NO Made-Up ROI**: Don't calculate speculative ROI percentages
- [ ] **Use Case Studies**: Only cite competitor's published case studies
- [ ] **Time Savings**: Must be from documented customer stories
- [ ] **Cost Savings**: Must tie to documented costs from competitor
- [ ] **Red Flag**: Any ROI claim over 1000% needs extra scrutiny

---

## 2.3 TONE & MESSAGING

### Professional Language
- [ ] **NO "FATAL"**: Use "Critical" instead of "Fatal" for competitor issues
- [ ] **NO "Disaster"**: Use "Significant Challenge" or "Critical Issue"
- [ ] **NO "Destroys"**: Use "Undermines" or "Significantly Impacts"
- [ ] **Balanced Tone**: State facts, not inflammatory language

### Framing & Positioning
- [ ] **Focus on User Value**: What business users can/can't do, not just features
- [ ] **Skill Requirements**: Emphasize learning curve, not just capability gaps
- [ ] **Business Impact**: Tie technical limitations to business outcomes
- [ ] **Fair Comparison**: Acknowledge competitor strengths where they exist

### Title & Headers
- [ ] **Clear & Direct**: "Excel Skills vs Complex Training" not "Excel Formula Desert"
- [ ] **User-Centric**: Frame from buyer perspective, not inside baseball
- [ ] **Avoid Jargon**: Unless industry-standard term, explain it
- [ ] **Scannable**: Can reader understand section from title alone?

---

## 2.4 EVIDENCE QUALITY

### Source Documentation
- [ ] **Every Claim = Source**: No unsourced assertions
- [ ] **URL + Date**: Full link and capture date for every source
- [ ] **Official > Third-Party**: Prefer competitor's own docs over analyst reports
- [ ] **Recent Sources**: Prefer <6 months, acceptable <12 months
- [ ] **Archive Links**: For critical claims, note archive.org backup

### Test Results & Benchmarks
- [ ] **Methodology Documented**: How was the test conducted?
- [ ] **Reproducible**: Could someone else repeat this test?
- [ ] **Fair Setup**: Did we give competitor best-case scenario?
- [ ] **Quantified Results**: Specific numbers, not "much slower"
- [ ] **Context Provided**: What does this mean for business users?

### Claim Strength Indicators
- [ ] **"Documented"**: Official competitor documentation exists
- [ ] **"Verified"**: We tested this ourselves
- [ ] **"Reported"**: Customer reviews mention this (3+ sources)
- [ ] **"Estimated"**: Our calculation, show math (use sparingly)
- [ ] **"Claimed"**: Competitor says this, we haven't verified (skeptical tone)

---

## 2.5 STRUCTURAL QUALITY

### Organization
- [ ] **Clear Hierarchy**: H2 → H3 → H4, logical structure
- [ ] **Scannable**: Can busy exec understand in 2 minutes?
- [ ] **Progressive Detail**: Summary → Details → Deep dive
- [ ] **Consistent Format**: Same structure across all competitors

### Completeness
- [ ] **Core Capabilities**: Covers key differentiators (Excel, ML, Investigation, Setup)
- [ ] **Cost Reality**: Total cost of ownership documented
- [ ] **Customer Perspective**: Real user stories included
- [ ] **Decision Criteria**: Helps buyer understand when to choose what

### Usability
- [ ] **Sales-Ready**: Can AE use this in customer conversation?
- [ ] **Objection Handlers**: Addresses likely "what about..." questions
- [ ] **Quick Reference**: Key facts easy to find
- [ ] **Action-Oriented**: Clear next steps for prospect

---

## 2.6 RED FLAGS - STOP & FIX

### Automatic Failures (Must Fix Before Publishing)
- [ ] ❌ Any made-up API/SDK code examples
- [ ] ❌ HIPAA or FedRAMP claims for Scoop
- [ ] ❌ Competitor costs >$1M without detailed documentation
- [ ] ❌ Python, JavaScript, or tech stack claims for Scoop
- [ ] ❌ P-values or statistical significance for Scoop
- [ ] ❌ "Zero FTE" or "no maintenance" claims
- [ ] ❌ Specific Scoop pricing ($3,588 or any number)
- [ ] ❌ ROI percentages over 1000% without case study source
- [ ] ❌ Customer quotes without source URL
- [ ] ❌ "FATAL" or inflammatory language

### Warning Signs (Review Carefully)
- [ ] ⚠️ Any cost claim seems unusually high
- [ ] ⚠️ Capability claim we can't demonstrate/prove
- [ ] ⚠️ Aggressive tone or unprofessional language
- [ ] ⚠️ Complex jargon without explanation
- [ ] ⚠️ Speculation presented as fact

---

## 2.7 CROSS-REFERENCE CHECKS

### Against Other Documents
- [ ] **Consistent with BATTLE_CARD.md**: Same facts, no contradictions
- [ ] **Consistent with evidence/*.md**: Claims match research sources
- [ ] **Consistent with other competitors**: Same standards applied
- [ ] **No Orphaned Claims**: Every fact in battle card has evidence file backup

### Against Templates
- [ ] **Follows COMPETITOR_RESEARCH_TEMPLATE.md**: All phases completed
- [ ] **Matches WEB_COMPARISON_TEMPLATE.md**: Structure if applicable
- [ ] **Uses SHARED/ components**: Consistent Scoop capability descriptions

---

## 2.8 FINAL VERIFICATION

### Pre-Publication Checklist
- [ ] **Peer Review**: Has another person reviewed for accuracy?
- [ ] **Legal Review**: Any compliance or regulatory claims verified?
- [ ] **Sales Review**: Will sales team feel confident using this?
- [ ] **Credibility Test**: Would I trust this if I were the buyer?
- [ ] **Source Check**: Spot-check 10 random sources - do they work?

### Post-Publication Monitoring
- [ ] **Update Date**: Document last reviewed date
- [ ] **Dead Link Check**: Quarterly verification of source URLs
- [ ] **Relevance Check**: Are facts still current (pricing, features)?
- [ ] **Feedback Loop**: Sales team reporting issues with claims?

---

## 2.9 QUICK REFERENCE: COMMON FIXES

### When You Find These Issues

**Issue**: "$3,588/year" or specific Scoop pricing
**Fix**: "Scoop costs a fraction of the price" or "20-30x less expensive"

**Issue**: "FATAL" or inflammatory language
**Fix**: "Critical" or "Significant"

**Issue**: "Zero FTE" or "no maintenance"
**Fix**: "1/5 the FTE requirement" or "reduces by 80%"

**Issue**: HIPAA/FedRAMP for Scoop
**Fix**: "SOC2 certified" only

**Issue**: P-values, statistical significance
**Fix**: "ML confidence scores", "decision tree rules"

**Issue**: "=SCOOP()" function or Excel formula
**Fix**: "In-memory spreadsheet engine" or "Google Sheets plugin with utility functions"

**Issue**: Oversimplified ML description ("shows rules", "explainable output")
**Fix**: "Three-layer AI Data Scientist: auto data prep + real ML (J48/JRip/EM) + AI explains complex output"

**Issue**: API/SDK code examples
**Fix**: DELETE entirely - we don't have public API

**Issue**: Competitor cost seems inflated (>$1M)
**Fix**: Find documented pricing, use conservative estimate

**Issue**: Made-up capability for Scoop
**Fix**: DELETE or replace with actual capability

---

# SECTION 3: Research Best Practices

## Purpose
Document learnings from competitor research implementations to improve future work.

---

## 3.1 Research Library Organization

### Problem
Phase 2 research (24 searches) generated extensive documentation that overwhelmed the main checklist file.

### Solution
Always separate research into dedicated phase files:
- `evidence/phase1_research_library.md`
- `evidence/phase2_research_library.md`
- `evidence/phase3_research_library.md`

### Benefits
- Keeps main checklist clean and readable
- Allows for comprehensive documentation without clutter
- Maintains searchability and organization
- Provides clear file references for sales teams

---

## 3.2 Summary Structure in Main Checklist

**Format**: Each phase should have 5-8 key findings summarized in main checklist:
- Customer stories: [Top 2-3 implementation failures/complaints]
- Industry verticals: [Top 2-3 industry-specific issues]
- Performance: [Top 2-3 performance/scalability issues]
- Competition: [Top 2-3 competitive weaknesses]
- Economics: [Top 2-3 cost/ROI concerns]

---

## 3.3 Documentation Process

**Always document as you go**:
1. Create phase research library file when starting each phase
2. Add each URL/search result immediately after visiting
3. Use comprehensive evidence format (not brief summaries)
4. Update main checklist summary after completing each phase

---

## 3.4 Scalability Principles

**Simple and consistent approach**:
- No conditional logic (thresholds, complexity decisions)
- Same structure for all competitors
- Clear file naming conventions
- Predictable organization pattern

---

## 3.5 Template Updates Applied

### Critical Instructions Enhanced
- Added Section 4: Research Library Organization
- Updated Section 2: Document as you go (references phase files)
- Maintains all existing edge case handling

### Research Library Sections Standardized
- All phases now reference separate evidence files
- Consistent summary format across all competitors
- Clear file path references for quick access

---

## 3.6 Impact of Best Practices

- **Scalability**: Same approach works for any competitor research volume
- **Clarity**: Main checklists stay clean and actionable
- **Completeness**: No research is lost or abbreviated
- **Usability**: Sales teams get both summaries and detailed evidence
- **Consistency**: All competitors follow identical organization pattern

---

## SIGN-OFF

Before marking research as "Complete", verify:

- [ ] All Section 1 (Framework Verification) items verified ✅
- [ ] All Section 2 (Research Quality Checklist) items verified ✅
- [ ] All Section 2.6 (Red Flags) cleared ✅
- [ ] Document reviewed by second person
- [ ] Changes documented in git commit

**Reviewed By**: _____________
**Date**: _____________
**Issues Found**: _____________
**Issues Fixed**: _____________

---

**This document is the source of truth for all quality standards. When in doubt, refer to this document.**

---

**Version History**:
- **v2.0** (2025-09-27): Consolidated from 3 separate files (QA_INSTRUCTIONS, RESEARCH_QA_CHECKLIST, RESEARCH_BEST_PRACTICES)
- **v1.0** (2025-09-26): Initial creation based on Power BI audit findings