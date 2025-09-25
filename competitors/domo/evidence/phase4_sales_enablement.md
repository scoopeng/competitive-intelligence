# Phase 4: BUPAF Scoring & Sales Enablement - Domo
**Date**: September 25, 2025
**Purpose**: Evidence-based BUPAF scoring and competitive positioning

## BUPAF Scoring with Evidence

### 1. Independence (Can business users work alone?)
**Score: 3/10**

**Evidence from Phase 1**:
- "Teams spend more time training than analyzing" (Reddit)
- "Even seasoned BI veterans find getting started frustrating" (LinkedIn)
- 30% of companies <100 employees cite setup complexity

**Evidence from Phase 2**:
- Workbench installation required (Windows-only) for CSV upload
- 1-2 month implementation with account exec and customer service
- "Little technical assistance" still needed for Business-in-a-Box

**Evidence from Phase 3**:
- Professional services "one-time fee for setup hours"
- Add-ons for training priced separately

**Conclusion**: Business users cannot work independently. IT required for setup, Workbench for data upload, extensive training needed.

### 2. Analytical Depth (Investigation vs single queries)
**Score: 4/10**

**Evidence from Phase 2**:
- Single SQL queries only - no multi-pass investigation
- No "why" capability found in documentation
- No automatic hypothesis testing
- AutoML exists but requires manual initiation

**Evidence from Phase 1**:
- "Doesn't have native NLP and ML capabilities" (Reddit)
- "Relies on Amazon Sagemaker and OpenAI" for ML

**Conclusion**: Can answer WHAT but not WHY. No investigation capability, no automatic ML discovery on questions.

### 3. Workflow Integration (Excel, Slack, PowerPoint)
**Score: 2/10**

**Evidence from Phase 2**:
- Excel formulas "disabled for security"
- Windows-only plugin, export/import cycle only
- No native Slack - requires Workato/n8n third-party
- PowerPoint requires manual insertion one at a time
- 25K row limit when exporting Mega Tables to Excel

**Evidence from Phase 1**:
- "Portal prison" concept well-established
- Everything requires logging into Domo portal

**Conclusion**: Completely portal-centric. No native workflow integration, everything requires leaving current tools.

### 4. Business Communication (Natural language & presentation)
**Score: 5/10**

**Evidence from Phase 2**:
- AI Chat exists with natural language queries
- Pramana Labs NLP integration
- But single queries only, no investigation

**Evidence from Phase 3**:
- Can generate single visualizations per query
- No PowerPoint generation capability
- No query persistence or reuse

**Conclusion**: Has basic NLP but limited to single questions. No presentation generation, no query decks.

### 5. Visual Intelligence (Presentation-ready outputs)
**Score: 4/10**

**Evidence from Phase 3**:
- "Tableau is one of the best" for visualizations (vs Domo)
- Dashboard-centric, not presentation-centric
- Manual export and formatting required

**Evidence from Phase 1**:
- "Most people deploy, find it ugly, and exit" (LinkedIn)
- Limited customization cited by 24 users

**Conclusion**: Decent dashboards but not presentation-ready. No automatic PowerPoint generation.

## TOTAL BUPAF SCORE: 18/50
**Category**: C - Enterprise Platform (15-24)
**Previous Score**: 29/50 (needs adjustment based on new evidence)

## Fatal Flaws for Sales Positioning

### 1. Excel Formula Disability
- **Evidence**: "Domo disables any formulas in Excel files" (official docs)
- **Impact**: Hours of manual work for business users
- **vs Scoop**: 150+ functions work immediately

### 2. No Investigation Capability
- **Evidence**: No multi-pass, no hypothesis testing, single queries only
- **Impact**: Can't find root causes
- **vs Scoop**: 3-10 automatic probes

### 3. Portal Prison Architecture
- **Evidence**: No native Slack/Excel/PowerPoint integration
- **Impact**: Workflow disruption
- **vs Scoop**: Native in all tools

### 4. Cost Explosion
- **Evidence**: "1% of company revenue", $95,800 for 100 users
- **Impact**: Budget destruction
- **vs Scoop**: $3,588 flat rate

### 5. Performance Issues
- **Evidence**: 30-60 seconds to open, 1-minute timeouts
- **Impact**: Productivity loss
- **vs Scoop**: Instant response

## Updated Battle Card Positioning

### Quick Win Questions
1. "Can you use Excel formulas with Domo data?" (No - disabled)
2. "How many queries to find root cause?" (One - no investigation)
3. "What's the real cost for 100 users?" ($95,800+)

### Killer Demo
1. Show Domo's Excel export with formulas disabled
2. Show single query limitation
3. Show Scoop's =SCOOP() formula working live
4. Show multi-pass investigation finding root cause

### Objection Handlers

**"Domo has AI Chat"**
"Yes, for single queries. Ask 'why did sales drop?' - Domo shows the number. Scoop runs 10 investigations and finds it was payment gateway failures in Northeast affecting enterprise accounts."

**"Domo has 1000+ connectors"**
"Each needs configuration and Workbench installation. Scoop: drag CSV into Slack, done in 30 seconds."

**"Domo is enterprise-grade"**
"Enterprise complexity, not enterprise empowerment. 1-2 months to setup, $95,800/year, formulas disabled. That's IT-grade, not business-grade."

## Competitive Capability Matrix (Updated)

| What Matters | Domo Reality | Scoop Advantage |
|--------------|--------------|-----------------|
| Excel Formulas | ❌ Disabled for security | ✅ 150+ functions live |
| Investigation | ❌ Single SQL query | ✅ 3-10 automatic probes |
| ML Discovery | ❌ Manual AutoML | ✅ Automatic J48/JRip |
| Slack Native | ❌ Third-party only | ✅ Full platform |
| Setup Time | ❌ 1-2 months | ✅ 30 seconds |
| CSV Upload | ❌ Workbench required | ✅ Drag & drop |
| True Cost/100 users | ❌ $95,800+ | ✅ $3,588 |
| Performance | ❌ 30-60 second loads | ✅ Instant |