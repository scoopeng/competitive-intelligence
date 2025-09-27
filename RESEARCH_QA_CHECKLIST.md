# Research Quality Assurance Checklist
**Version**: 1.0
**Last Updated**: 2025-09-26
**Purpose**: Ensure all competitive research meets factual accuracy and credibility standards

---

## How to Use This Checklist

1. **Before Publishing**: Run every document through this checklist
2. **During Review**: Check off each item as verified
3. **On Failure**: Fix the issue, document what was wrong
4. **Update Checklist**: Add new checks as we discover new issues

---

## SECTION 1: SCOOP FACTUAL ACCURACY

### 1.1 Capabilities - What Scoop HAS ✅
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

### 1.2 Capabilities - What Scoop DOES NOT HAVE ❌
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

### 1.3 Compliance & Certifications - EXACT FACTS
- [ ] **SOC2 Certified**: This is accurate - we have SOC2 Type II
- [ ] **NOT HIPAA**: Never claim HIPAA compliance, certification, or readiness
- [ ] **NOT FedRAMP**: Never claim FedRAMP authorization or government cloud
- [ ] **Check Before Claiming**: If unsure about compliance, DO NOT claim it

### 1.4 Pricing & Cost - FLEXIBLE NOT FIXED
- [ ] **NO Specific Pricing**: Don't use "$3,588/year" or any specific number
- [ ] **Use Relative Language**: "a small fraction of the cost", "20-30x less expensive"
- [ ] **Use Ranges if Needed**: "Scoop costs thousands annually vs hundreds of thousands"
- [ ] **Let Sales Handle**: Don't lock in specific pricing in content

### 1.5 Resource Requirements - REALISTIC NOT ZERO
- [ ] **NO Zero FTE Claims**: Don't say "zero maintenance" or "no IT involvement"
- [ ] **Use Reduction Language**: "1/5 the FTE requirement", "reduces by 80%"
- [ ] **Be Honest**: Some setup/maintenance exists, just far less than competitors

### 1.6 Technical Accuracy - AI DATA SCIENTIST ENGINE
- [ ] **Three-Layer Architecture**: Always describe all three layers (data prep + ML + AI explanation)
- [ ] **Real ML Models**: J48 decision trees (can be 800+ nodes), JRip rules, EM clustering
- [ ] **Automatic Data Prep**: Emphasize cleaning, binning, feature engineering happens automatically
- [ ] **AI Explanation Layer**: Models produce complex output, AI explains in business language
- [ ] **NOT Just Rules**: Don't oversimplify - we run sophisticated ML then explain it
- [ ] **NO P-Values**: We don't provide statistical significance (p < 0.05)
- [ ] **NO Statistical Tests**: We run ML models, not statistical hypothesis tests
- [ ] **NO Tech Stack Details**: Don't mention internal languages (Python, etc.)

---

## SECTION 2: COMPETITOR FACTUAL ACCURACY

### 2.1 Cost Claims - CREDIBLE & VERIFIABLE
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

### 2.2 Capability Claims - EVIDENCE REQUIRED
- [ ] **Official Documentation**: Link to competitor's own docs/website
- [ ] **Customer Reviews**: G2, Reddit, LinkedIn posts with URLs
- [ ] **Test Results**: Our own benchmarking with methodology documented
- [ ] **NO Speculation**: If we didn't test it or find documentation, don't claim it

### 2.3 Customer Quotes - REAL & SOURCED
- [ ] **Full URL**: Every quote needs source link
- [ ] **Date Captured**: When was this quote published/captured
- [ ] **Context Preserved**: Don't cherry-pick, show enough context
- [ ] **Verbatim**: Use exact quotes, note [...] for omissions

### 2.4 ROI & Business Impact - CONSERVATIVE
- [ ] **NO Made-Up ROI**: Don't calculate speculative ROI percentages
- [ ] **Use Case Studies**: Only cite competitor's published case studies
- [ ] **Time Savings**: Must be from documented customer stories
- [ ] **Cost Savings**: Must tie to documented costs from competitor
- [ ] **Red Flag**: Any ROI claim over 1000% needs extra scrutiny

---

## SECTION 3: TONE & MESSAGING

### 3.1 Professional Language
- [ ] **NO "FATAL"**: Use "Critical" instead of "Fatal" for competitor issues
- [ ] **NO "Disaster"**: Use "Significant Challenge" or "Critical Issue"
- [ ] **NO "Destroys"**: Use "Undermines" or "Significantly Impacts"
- [ ] **Balanced Tone**: State facts, not inflammatory language

### 3.2 Framing & Positioning
- [ ] **Focus on User Value**: What business users can/can't do, not just features
- [ ] **Skill Requirements**: Emphasize learning curve, not just capability gaps
- [ ] **Business Impact**: Tie technical limitations to business outcomes
- [ ] **Fair Comparison**: Acknowledge competitor strengths where they exist

### 3.3 Title & Headers
- [ ] **Clear & Direct**: "Excel Skills vs Complex Training" not "Excel Formula Desert"
- [ ] **User-Centric**: Frame from buyer perspective, not inside baseball
- [ ] **Avoid Jargon**: Unless industry-standard term, explain it
- [ ] **Scannable**: Can reader understand section from title alone?

---

## SECTION 4: EVIDENCE QUALITY

### 4.1 Source Documentation
- [ ] **Every Claim = Source**: No unsourced assertions
- [ ] **URL + Date**: Full link and capture date for every source
- [ ] **Official > Third-Party**: Prefer competitor's own docs over analyst reports
- [ ] **Recent Sources**: Prefer <6 months, acceptable <12 months
- [ ] **Archive Links**: For critical claims, note archive.org backup

### 4.2 Test Results & Benchmarks
- [ ] **Methodology Documented**: How was the test conducted?
- [ ] **Reproducible**: Could someone else repeat this test?
- [ ] **Fair Setup**: Did we give competitor best-case scenario?
- [ ] **Quantified Results**: Specific numbers, not "much slower"
- [ ] **Context Provided**: What does this mean for business users?

### 4.3 Claim Strength Indicators
- [ ] **"Documented"**: Official competitor documentation exists
- [ ] **"Verified"**: We tested this ourselves
- [ ] **"Reported"**: Customer reviews mention this (3+ sources)
- [ ] **"Estimated"**: Our calculation, show math (use sparingly)
- [ ] **"Claimed"**: Competitor says this, we haven't verified (skeptical tone)

---

## SECTION 5: STRUCTURAL QUALITY

### 5.1 Organization
- [ ] **Clear Hierarchy**: H2 → H3 → H4, logical structure
- [ ] **Scannable**: Can busy exec understand in 2 minutes?
- [ ] **Progressive Detail**: Summary → Details → Deep dive
- [ ] **Consistent Format**: Same structure across all competitors

### 5.2 Completeness
- [ ] **Core Capabilities**: Covers key differentiators (Excel, ML, Investigation, Setup)
- [ ] **Cost Reality**: Total cost of ownership documented
- [ ] **Customer Perspective**: Real user stories included
- [ ] **Decision Criteria**: Helps buyer understand when to choose what

### 5.3 Usability
- [ ] **Sales-Ready**: Can AE use this in customer conversation?
- [ ] **Objection Handlers**: Addresses likely "what about..." questions
- [ ] **Quick Reference**: Key facts easy to find
- [ ] **Action-Oriented**: Clear next steps for prospect

---

## SECTION 6: RED FLAGS - STOP & FIX

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

## SECTION 7: CROSS-REFERENCE CHECKS

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

## SECTION 8: FINAL VERIFICATION

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

## QUICK REFERENCE: COMMON FIXES

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

## CHECKLIST MAINTENANCE

### When to Update This Checklist
- [ ] New factual error discovered in any competitor research
- [ ] New Scoop capability launched (verify and add)
- [ ] Compliance certification obtained (SOC2, HIPAA, etc.)
- [ ] Pricing model changes
- [ ] Common research pattern identified (good or bad)

### Version History
- **v1.0** (2025-09-26): Initial creation based on Power BI audit findings

---

## SIGN-OFF

Before marking research as "Complete", verify:

- [ ] All SECTION 1 (Scoop Facts) items verified ✅
- [ ] All SECTION 2 (Competitor Facts) items verified ✅
- [ ] All SECTION 6 (Red Flags) cleared ✅
- [ ] Document reviewed by second person
- [ ] Changes documented in git commit

**Reviewed By**: _____________
**Date**: _____________
**Issues Found**: _____________
**Issues Fixed**: _____________

---

**This checklist is the source of truth for research quality standards. When in doubt, refer to this document.**