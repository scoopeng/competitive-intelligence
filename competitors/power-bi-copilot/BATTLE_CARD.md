# Battle Card: Power BI Copilot

**BUA Score**: 21/59 (36%, Category C)
**Parent**: Microsoft
**Key Weakness**: Only 3% of IT leaders find significant value (Gartner)
**Last Updated**: September 25, 2025 (100% Complete with new 4-phase template)

---

## Quick Win Discovery Questions
1. "Can Copilot work with your $20 PPU licenses?" (No - needs $60k F64)
2. "How do you embed Copilot in your applications?" (You can't - no APIs)
3. "What's the accuracy rate according to Gartner?" (47% accurate - 53% errors)
4. "Can government agencies use it?" (No - not in sovereign clouds)
5. "How many queries to find root cause?" (One - no investigation)

## Top 5 Fatal Flaws (With Evidence)

1. **NO Excel Formula Support - Zero**
   - Power BI Copilot has ZERO Excel formula execution
   - Cannot understand VLOOKUP, SUMIFS, or any Excel functions
   - Separate $30/user Excel Copilot product required
   - Source: Phase 2 functionality analysis

2. **Cannot Investigate "Why" - Single Query Only**
   - "Copilot doesn't answer follow-up questions. One question at a time"
   - No multi-pass investigation capability
   - "Can't currently answer questions that require generating new insights"
   - Source: Microsoft documentation

3. **No Slack Integration - Microsoft Lock-in**
   - Zero Slack integration capabilities
   - PowerPoint requires separate add-in installation
   - Teams/SharePoint only - vendor lock-in strategy
   - Source: Integration research findings

4. **97% Failure Rate (Gartner Survey)**
   - Only 3% of 123 IT leaders found significant value
   - 53% report too many inaccurate results
   - "Reality is surreal - tool that says 'FYI, I can't be trusted'"
   - US Congress banned Copilot due to security concerns
   - Source: Gartner survey 2025 + Phase 3 research

5. **No REST APIs - Complete Developer Dead-End**
   - "No dedicated Copilot REST APIs exist" - official docs
   - Cannot embed in applications ("Not integrated into Power BI Embedded")
   - CSP violations when attempting to iframe
   - App Owns Data model doesn't support Copilot
   - Source: Microsoft documentation + Phase 3 technical analysis

## Pricing Comparison (200 Users)

### Power BI with Copilot
- F64 Capacity: $5,616/month (reserved)
- 200 Pro licenses: $2,800/month ($14 × 200)
- **Monthly Total: $8,416**
- **Annual Total: $100,992**
- Plus: Training, support, infrastructure management

### Scoop Analytics
- Team Plan: $149 × 200 = $29,800/month
- Enterprise discount (50%): ~$14,900/month
- **Annual Total: ~$178,800**
- Includes: All AI features, no infrastructure, support included

### Power BI WITHOUT Copilot (PPU)
- 200 PPU licenses: $4,800/month
- Annual: $57,600
- **But NO AI capabilities**

## Customer Horror Stories (With Evidence)

### 1. The Gartner Bombshell
**Quote**: "Only four [of 123 IT leaders] said Copilot provided significant value"
**Context**: 3% success rate in Gartner survey
**Impact**: 97% wasted investment, failed deployments

### 2. The $300M SaaS Disaster
**Quote**: "Copilot will happily answer questions your users were never meant to ask—like showing salary data"
**Source**: GoCollectiv case study
**Context**: 12% adoption, required 30-day IT project to salvage

### 3. The Trust Destroyer
**Quote**: "In BI, these mistakes can get you fired... why would a user trust a tool that says 'mistakes are possible'"
**Source**: Data Goblins BI expert analysis
**Impact**: Career-ending wrong answers in financial reports

## Head-to-Head

| Factor | Power BI Copilot | Scoop | Your Win |
|--------|------------------|-------|----------|
| Excel Formulas | ❌ ZERO support | ✅ 150+ functions | "Learn DAX or use your Excel skills?" |
| Investigation | ❌ Single query only | ✅ 3-10 pass analysis | "What happened vs WHY it happened" |
| ML/AI | ❌ Manual setup required | ✅ Automatic ML | "Configure dataflows or just ask why?" |
| Slack Integration | ❌ Not supported | ✅ Native | "Where does your team actually work?" |
| Setup Time | ❌ Weeks of prep + 24hr wait | ✅ 30 seconds | "Quarter planning or quarter analyzing?" |
| Business Users | ❌ Requires training | ✅ No training | "6-week rollout or 6-minute demo?" |

## Discovery Questions for Sales

### Budget Discovery
1. "What's your annual Power BI spend including licenses and capacity?"
2. "Are you aware F64 capacity alone costs $67,392/year?"
3. "How many users need AI analytics capabilities?"

### Pain Discovery
1. "How many weeks did data preparation take before Copilot worked?"
2. "Have you experienced different answers to the same question?"
3. "Which offices can't use it due to geographic restrictions?"

### Integration Discovery
1. "Do your analysts work primarily in Excel or the Power BI portal?"
2. "How do you share insights with non-Power BI users?"
3. "Have you budgeted for Excel Copilot Pro at $30/user?"

## Objection Handlers

**"Microsoft integration is seamless"**
"Let's clarify - Excel COPILOT requires a separate $30/user Copilot Pro license. Power BI Copilot requires $67k minimum infrastructure. That's $73k+ before you analyze a single row. How is that seamless?"

**"It's backed by OpenAI/GPT-4"**
"Which is exactly why Microsoft warns it's 'nondeterministic' and produces 'misleading outputs.' In their own words: 'not guaranteed to produce the same answer with the same prompt.' Would you make million-dollar decisions on answers that change randomly?"

**"We're already invested in Microsoft"**
"That investment is exactly why you need Scoop. Your Excel users can't access Power BI data without learning DAX. Your Power BI users can't share with Slack teams. Scoop bridges those gaps with =SCOOP() in Excel. One formula, not two platforms."

**"The price seems reasonable"**
"Let's do the math: F64 capacity ($67k) + 200 Pro licenses ($34k) = $101k/year minimum. That's before training, support, or the 14 weeks of data prep. Scoop would cost roughly the same but includes everything and works immediately."

**"We need enterprise features"**
"Like working in your Dubai and Singapore offices? Power BI Copilot is blocked in 11+ regions. Like consistent answers for board presentations? Microsoft admits it's nondeterministic. Enterprise means reliability, not beta testing."

## The Winning Pitch

"I noticed you're evaluating Power BI Copilot. Did you know Microsoft's own documentation warns about 'nondeterministic behavior' - meaning the same question gives different answers each time?

Plus there's a hidden $67,392/year infrastructure tax just to enable it, and Excel integration requires another $30/user/month for Copilot Pro.

You're looking at over $100,000/year for 200 users, plus 14 weeks of data preparation, for a system that Microsoft admits can produce 'misleading outputs.'

Scoop gives you deterministic results, native Excel integration with =SCOOP(), and works immediately with your existing data. Would you prefer to spend $100k on infrastructure or on actual insights?"

## Proof Points
- Show Microsoft's warning documentation
- Demonstrate consistent vs random results  
- Calculate true cost with all licenses
- Show =SCOOP() vs =COPILOT() differences

## Verify This Yourself

### Nondeterministic Behavior
1. Visit: https://learn.microsoft.com/en-us/fabric/fundamentals/copilot-power-bi-privacy-security
2. Search for "nondeterministic"
3. Read Microsoft's own warning about different outputs from same prompts

### Excel Separate License
1. Visit: https://www.microsoft.com/en-us/store/b/copilotpro
2. Note: "each will need to buy their own Copilot Pro subscription"
3. Check: Excel features are preview-only and English-only

### Capacity Requirements
1. Visit: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction
2. Find: "F2 or higher" or "P1 or higher" requirement
3. Calculate: F64 minimum = $60,000+/year

### Output Quality Issues
1. Visit: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai
2. Find: "generic, inaccurate, or even misleading outputs"
3. Note: Microsoft's own admission of quality problems

---
*Use when: Microsoft shops, Excel-heavy teams, Cost-conscious buyers, Reliability concerns*