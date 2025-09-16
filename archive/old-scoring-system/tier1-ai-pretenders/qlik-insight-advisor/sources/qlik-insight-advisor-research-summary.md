# Qlik Insight Advisor Research Summary

## Executive Summary

Qlik Insight Advisor is marketed as an AI-powered natural language analytics tool that enables business users to self-serve insights. However, research reveals significant gaps between marketing claims and reality, with numerous technical barriers preventing true business user self-service.

## Key Findings

### 1. Real ML/AI Capabilities vs Marketing Claims

**Marketing Claims:**
- "AI-powered natural language processing"
- "Machine learning that improves over time"
- "Generative AI integration (2024-2025)"
- "Automated insight generation"

**Reality:**
- **Limited ML Implementation**: The "machine learning" primarily learns user preferences for chart types on a per-user basis
- **Rule-Based System**: Heavily relies on predefined business logic and data model structures rather than true AI understanding
- **No Mathematical Operations**: Cannot perform basic calculations like adding two fields together
- **Poor Language Understanding**: Cannot recognize:
  - Misspellings ("its user intent understanding is not quite good")
  - Plurals (must ask "how many country" instead of "countries")
  - Contractions (won't recognize "isn't" or "haven't")
  - Common abbreviations (YOY, MOM not supported)

### 2. Business User Accessibility: The Reality

**Critical Blockers for Business Users:**

1. **Complex Setup Requirements**
   - Requires IT to configure "business logic" - a complex logical model
   - Needs specific data structures (modern calendars using DECLARE)
   - Master items must be pre-configured by technical users
   - "Business logic is too complex and a Qlik application evolves very quickly, no one wants to waste time on it"

2. **Technical Prerequisites**
   - Star schema data model required
   - Specific field naming conventions
   - Proper calendar configuration or basic questions like "sales for Jun 2023" fail
   - Business logic must be reset after any data model changes

3. **Query Formulation Challenges**
   - Must reference fields and values precisely
   - Requires understanding of dimensions, measures, and filters
   - Questions must be technically structured despite "natural language" claims
   - "If your question is not formulated well, it will lead to misleading results"

### 3. Setup Complexity and Time

**Initial Setup:**
- **Minimal Setup**: Can start immediately but with poor results
- **Proper Setup**: Requires significant IT involvement:
  - Configure business logic and logical models
  - Define fields, groups, packages, and hierarchies
  - Set up behaviors and calendar periods
  - Create master items and synonyms
  - Test and refine based on user feedback

**Common Setup Issues:**
- "Invalid Business Logic" errors after any data model change
- Performance degradation: "server uses more resources, especially RAM"
- "Objects take much longer to show information" (30-second reports now take 9 minutes)

### 4. Pricing and Total Cost of Ownership

**Licensing Costs:**
- Qlik Sense Business: $30/user/month (minimum)
- Enterprise SaaS: $40-70/user/month depending on role
- Premium tier: $2,700/month for 50GB data
- Insight Advisor included in base licensing (not separate)

**Hidden TCO Factors:**
- Significant IT resources for setup and maintenance
- Ongoing business logic configuration
- Performance impact requiring infrastructure upgrades
- Training costs due to poor natural language understanding
- Lost productivity from failed queries and workarounds

### 5. Output Format and Usability

**What Users Actually Get:**
- Technical visualizations requiring interpretation
- Error messages like "Invalid Business Logic" or "Unable to generate insights"
- Responses that require precise technical query formulation
- No actionable business insights in plain language
- "Often when you check the result manually, sometimes it throws you wrong answers"

**Real User Experience:**
- "I've never seen Insight Advisor being used in professional environment"
- "I tried to use it a few times and they were not very satisfactory"
- Users report waiting 45+ minutes with no insights generated
- Consultants report: "couldn't find a single company using this in day-to-day operations"

### 6. Integration Limitations

**Slack/Teams Integration:**
- **Major Limitation**: Doesn't work with SSO authentication (most enterprises use SSO)
- Requires forms or SAML authentication only
- Users report "cannot access this app" errors even after successful authentication
- Some evidence suggests Slack/Teams integration may have been discontinued
- Qlik documentation now emphasizes in-app experience over external channels

**Portal Dependency:**
- Most functionality requires using Qlik portal directly
- External integrations have persistent authentication issues
- No true mobile or embedded analytics for business users

## Why Business Users Can't Actually Self-Serve

### 1. **Technical Barriers**
- Requires understanding of data model concepts
- Must know exact field names and structures
- Need to formulate queries with technical precision
- Business logic configuration is IT-dependent

### 2. **Poor Natural Language Processing**
- Cannot handle common language variations
- Requires memorization of specific query patterns
- No forgiveness for typos or natural phrasing
- Limited to predefined question structures

### 3. **Dependency on IT**
- Any data model change requires IT intervention
- Business logic must be constantly maintained
- Performance issues require technical investigation
- Master items and synonyms need technical setup

### 4. **Unreliable Results**
- Frequent errors with no clear resolution
- Inconsistent or incorrect answers
- Performance degradation over time
- "Misleading results" per user reports

### 5. **Limited Real-World Adoption**
- Professional users avoid it after initial attempts
- No evidence of successful business user self-service
- Consultants can't find companies using it daily
- Community forums filled with unresolved issues

## Sources

1. Official Qlik Documentation (help.qlik.com)
2. Qlik Community Forums (community.qlik.com)
3. Qlik Product Pages (qlik.com/us/products)
4. ITQlick Pricing Guide (July 2025)
5. BetterBuys BI Reviews
6. BARC Analytics Reviews (2025)
7. TechBuilders Pricing Analysis
8. Forrester TEI Study (209% ROI claim)

## Conclusion

Despite marketing claims of AI-powered self-service analytics, Qlik Insight Advisor remains a technically complex tool that requires significant IT involvement and delivers unreliable results. The gap between "business user self-service" marketing and the reality of technical prerequisites, poor language understanding, and limited adoption makes it unsuitable for true business user self-service analytics.

The tool's inability to work with SSO authentication (standard in enterprises), requirement for precise technical query formulation, and frequent "Invalid Business Logic" errors create insurmountable barriers for sales, marketing, and customer success teams seeking independent analytics capabilities.