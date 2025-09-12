# Qlik Insight Advisor Research Summary
**Date**: January 28, 2025
**Time**: 9:00 AM - 10:00 AM
**Focus**: END USER (Business User) Perspective - Sales/Marketing/CS Teams

## Critical Question: Can Business Users Actually Get Insights Without IT?

### Executive Reality Check
Qlik Insight Advisor is fundamentally broken for business users. Despite heavy "AI" marketing, it's a rule-based system that requires IT to configure complex "business logic," fails on basic typos or plurals, and generates so many errors that consultants report finding zero companies using it in daily operations.

## Key Research Findings

### 1. The "AI" Reality
**Marketing**: "AI-powered natural language analytics with machine learning"
**Reality**: Rule-based system that only "learns" your chart preferences

**What They Call "Machine Learning"**:
- Tracks which chart types you prefer (that's it)
- No pattern discovery
- No clustering or segmentation
- No predictive analytics
- No root cause analysis
- Can't even add two fields together

**Language Understanding Failures**:
- Can't handle typos: "slaes" won't find "sales"
- Plurals break it: Must ask "how many country" not "countries"
- No contractions: "isn't" or "haven't" fail
- No abbreviations: YOY, MOM not recognized
- Direct quote: "its user intent understanding is not quite good"

### 2. Business User Experience: A Disaster

**Day 1 Reality for Sales Person**:
1. Opens Qlik portal (no Slack access)
2. Types: "Show me sales for last month"
3. Error: "Invalid Business Logic"
4. IT: "We need to configure the calendar model"
5. Week later: "Show me top customers"
6. Error: Field not recognized
7. IT: "You need to type 'Customer Name' exactly"
8. Gives up, emails data team

### 3. Setup Complexity Hidden Behind Marketing

**They Say**: "Get started in minutes"
**Reality**: Proper setup requires:

**IT Must Configure**:
- Business logic (complex logical models)
- Star schema data models
- Calendar configurations with DECLARE statements
- Master items and field groups
- Synonym definitions
- Behaviors and packages

**User Quote**: "Business logic is too complex and a Qlik application evolves very quickly, no one wants to waste time on it"

### 4. The Portal Prison

**Slack Integration Broken**:
- Doesn't work with SSO (enterprise standard)
- "Cannot access this app" errors
- Forms/SAML auth only (security risk)
- Evidence suggests it may be discontinued

**Must Use Qlik Portal**:
- Leave workflow to analyze
- Learn Qlik terminology
- Navigate complex UI
- Deal with performance issues

### 5. Performance & Reliability Nightmare

**Community Reports**:
- "30 second reports now take 9 minutes"
- "Server uses more resources, especially RAM"
- "Waited 45+ minutes, no insights generated"
- "Often throws you wrong answers"
- "Objects take much longer to show information"

**Consultant Reality Check**:
> "I've never seen Insight Advisor being used in professional environment"

> "Couldn't find a single company using this in day-to-day operations"

### 6. Error Messages Instead of Insights

**Common Business User Experiences**:
- "Invalid Business Logic" (after any data change)
- "Unable to generate insights"
- "Field not found" (typed plural)
- "No insights available"
- Silent failures with wrong data

**Must Reset Everything**: Any data model change requires IT to reconfigure all business logic

### 7. True Cost for 200 Users

**Published Pricing**:
- Qlik Sense Business: $30/user/month minimum
- Enterprise: $40-70/user/month
- 200 users: $96,000-168,000/year

**Hidden Costs**:
- IT team to maintain business logic
- Infrastructure upgrades for RAM
- Lost productivity from errors
- Training that doesn't help
- Workarounds and manual processes

**Real TCO**: $200,000+ annually

### 8. What Business Users Actually Need vs Get

**They Need**:
- Ask in Slack: "Why are sales down?"
- Get insight: "Sales down 15% due to..."
- Discover patterns they didn't know
- Zero training required

**They Get**:
- Portal login required
- Type precisely: "Sum of Sales Revenue by Customer Name"
- Error or wrong visualization
- Call IT for help

## Evidence From the Field

### Community Forums
- "I tried to use it a few times and they were not very satisfactory"
- "If your question is not formulated well, it will lead to misleading results"
- "Business logic needs to be reset" (constant theme)
- Multiple threads on SSO authentication failures

### Professional Consultants
- Can't find companies actually using it
- Never seen in professional environments
- Clients abandon after initial attempts
- Used as checkbox feature, not daily tool

### Documentation Admissions
- Requires "proper data model structure"
- "Business logic configuration" essential
- Master items must be predefined
- Specific calendar requirements

## Competitive Positioning

### Why Qlik Insight Advisor Fails Business Users:

1. **No Real AI**: Just rules and chart preferences
2. **Language Failures**: Can't understand natural questions
3. **IT Dependency**: Constant business logic maintenance
4. **Portal Required**: No Slack/Teams integration
5. **Unreliable**: Wrong answers, constant errors
6. **Abandoned**: No real-world adoption

### Scoop's Advantages:

1. **Real ML Models**: Discover patterns, predict, classify
2. **Natural Language**: Handles how people actually talk
3. **True Self-Service**: No IT configuration needed
4. **Slack Native**: Work where users work
5. **Reliable Insights**: Accurate, explainable results
6. **Proven Adoption**: Users love it, use it daily

## Key Takeaway

Qlik Insight Advisor represents everything wrong with enterprise BI's approach to "self-service." It's a technically complex, rule-based system marketed as AI that requires constant IT support and delivers such poor results that professional consultants can't find a single company successfully using it for business user self-service. The fact that it can't handle basic typos or plurals while claiming "natural language" capabilities is emblematic of the broader deception in the "AI BI" market.