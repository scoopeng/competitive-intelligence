# Qlik Insight Advisor User Experiences: Community Research Report

## Executive Summary

Based on extensive research across community forums, Reddit, review sites, and technical discussions, Qlik Insight Advisor faces significant adoption challenges despite being launched in 2019 - well before the current AI/NLP analytics boom. The most telling finding: experienced consultants and experts report they "couldn't find a single company that was using this resource in their day-to-day operations."

## Key Findings

### 1. Near-Zero Professional Adoption (2019-2025)

**Community Quote:**
> "I've asked a lot of consultants and Qlik experts, but I couldn't find a single company that was using this resource in their day-to-day operations to solve problems." - User asking why Insight Advisor isn't popular despite 5+ years in market

**Expert Experience:**
> "I've never seen Insight Advisor being used in professional environment. I've only seen some uses in academic videos or demonstrations." - Cezário Abrantes, experienced Qlik developer

### 2. Critical Technical Failures

#### Infinite Loading/Complete System Failure
**URL:** https://community.qlik.com/t5/Insight-Advisor/Insight-Advisor-regularly-goes-into-infinite-load-impacting/td-p/2074414  
**Date:** 2023
**User Complaint:**
- "Insight Advisor regularly goes into an endless cycle of thinking, even for really simple actions like selecting one measure and one dimension"
- "Almost always does this when I ask a natural-language question, including fairly simple ones like 'Show me revenue by product and country'"
- "When this happens, it is usually not possible to stop the current process - hitting 'Cancel' works but no further actions seem to work"
- **Impact:** Must close and reopen entire application

#### Performance Degradation
**Multiple Reports:**
- Users leaving system running for 45+ minutes with no results
- "Just says analysing data" indefinitely
- No timeout or error handling

### 3. Business Logic Configuration Nightmare

**Community Consensus:**
> "Business logic is too complex and a Qlik application evolves very quickly, no one want to waste time on it"

**Technical Requirements:**
- Requires specific modern calendar (DECLARE) implementation
- Most migrated apps lack proper calendar setup
- Even experienced developers' custom calendar implementations break Insight Advisor
- Result: "The most basic NL question 'what are my sales for Jun 2023' will fail"

### 4. Natural Language Understanding Failures

**User Experience Reports:**
- "You need to take time to understand how it works and its user intent understanding is not quite good"
- "Many limitations where you need to mention the measure, filter, and dimension"
- "If your question is not formulated well, it will lead to misleading results"
- "Often when you check the result manually, sometimes it throws you wrong answers"
- "Not quite good at understanding grammar issues where it is difficult to depend on it"

### 5. Common Error Messages

#### "Invalid Business Logic"
- Occurs after any data model modification
- Triggered by dropping fields or removing master items
- Requires complete business logic reset to fix

#### "Unable to Get Data"
- Common in Insight Advisor Chat
- No clear error messaging or troubleshooting guidance

#### "Unable to Generate Insights"
- Specific to certain apps
- Persists even with proper configuration

### 6. IT Dependency and Complexity

**Configuration Requirements:**
- Complex service configuration files
- Multiple Windows processes must be running (nl-app-search, nlparser_r.exe)
- Requires enabling debug logs across multiple services for troubleshooting
- License verification issues

### 7. Comparison to Modern AI Tools

**Community Discussion (2023-2024):**
> "With Bard and ChatGPT, the 'NL generated visualization and insights' has become a really hot topic these days, but Qlik has had this functionality since 2019 with the Insight Advisor"

**Why It Failed Where Others Succeeded:**
- "The list of 'IA can not do...' is too long"
- "Not good enough, or easy to configure, beyond basic use cases"
- Requires extensive data preparation vs. modern tools that "just work"

### 8. Developer Sentiment

**From Active Qlik Developers:**
- Prefer traditional analysis methods
- View it as "gimmicky" or demonstration feature
- Low perceived value compared to effort required
- Many actively avoid using it in professional projects

### 9. Failed Integration Attempts

**Stack Overflow/Developer Forums:**
- CORS errors when accessing API
- OAuth2 authentication complexity
- API endpoints returning 403 errors even with proper tokens
- Version compatibility issues

### 10. Time Investment Before Abandonment

**Typical User Journey:**
1. Initial excitement about NL analytics
2. Hours spent on business logic configuration
3. Days trying to get basic queries working
4. Weeks of intermittent failures and support tickets
5. Eventual abandonment in favor of traditional BI methods

### 11. Qlik's Own Recognition of Failure

**Official Statement (2024):**
> "We are focusing on addressing many of the pain points mentioned in this thread, such as improved user intent understanding, better handling of business logic and making apps working with Insight Advisor without using Business Logic"

**Translation:** After 5 years, they're trying to fix fundamental issues that prevented adoption

### 12. The Kyndi Acquisition Hope

**Community Speculation:**
- Qlik acquired Kyndi (NLP company) to address these issues
- "QLIK is being very quiet about what is doing with Kyndi's IP"
- Promises of "LLM integration" at Qlik Connect 2025
- Skepticism remains high given track record

## Success vs Failure Ratio

**Success Stories:** 
- Limited to vendor demonstrations
- Academic/training environments
- Simple proof-of-concepts

**Failure Stories:**
- Every production implementation attempt
- Real-world business scenarios
- Complex data models
- Time-sensitive analytics needs

## Business User Experiences

**Typical Business User Feedback:**
- "It never understands what I'm asking"
- "I get different results each time"
- "IT says it needs more configuration"
- "We went back to regular reports"

## Cost of Failed Adoption

**Time Investment:**
- Weeks of configuration attempts
- Months of user training
- Ongoing troubleshooting
- Lost productivity from system hangs

**Business Impact:**
- Delayed insights
- User frustration and resistance
- Credibility loss for BI teams
- Return to manual analysis methods

## Competitive Analysis Impact

While competitors launched working NL analytics (Tableau Ask Data, Power BI Q&A, ThoughtSpot), Qlik's 5-year head start resulted in:
- Market perception as "legacy BI"
- Loss of innovation leadership position
- Users seeking alternatives for modern analytics

## Specific Technical Issues Documented

### Server Resource Problems
**Case:** App with 10-15 million row fact table  
**Issue:** Stuck on "analyzing data" for 45+ minutes  
**Root Cause:** "Server load" and "server memory usage"  
**Resolution:** None provided - left unresolved

### Multi-Node Environment Failures
**Case:** Migration from single-node DEV to multi-node PROD  
**Issue:** "Invalid Business Logic" error appears only in production  
**Pattern:** Works in simple environments, fails in enterprise setups

### Data Model Sensitivity
**Common Triggers for Failure:**
- Dropping any field from data model
- Modifying master items
- Adding new dimensions
- Changing calculated expressions
- Any data model evolution

### Missing Process Dependencies
**Required Windows Processes:**
- nl-app-search
- nlparser_r.exe
**If Missing:** Complete feature failure with no clear error message

## Implementation Failure Patterns

### Why Pilot Projects Fail
Based on industry analysis of AI/BI failures (80%+ failure rate for AI projects):

1. **Technology-First Mindset**
   - Organizations implement because "AI is hot"
   - No clear business problem identified
   - Feature becomes "checkbox for RFPs"

2. **Data Quality Requirements**
   - Requires perfect data structure
   - Synthetic keys cause failures
   - Legacy data models incompatible

3. **Training Investment vs. ROI**
   - "Hours and hours of training" required
   - Users must balance normal jobs with complex learning
   - Low adoption due to complexity

4. **Unrealistic Expectations**
   - Marketed as "natural language"
   - Reality: Must specify exact measure, filter, dimension
   - Grammar issues lead to wrong results

## The Documentation Trap

**Qlik's Own "Best Practices" Admission:**
- Released extensive best practices documentation in 2024
- 5 years after initial release
- Acknowledges "consolidation and centralization of these best practices... will make it easier"
- Translation: Even Qlik admits it's too complex

## Recent Updates (2024-2025)

**LLM Integration Announcement:**
- "Generative-AI driven language generation as a private preview"
- Promises of "more 'chat GPT like' answers"
- Still in preview after competitors have production features
- Community skepticism high given 5-year track record

**The Kyndi Acquisition:**
- Acquired NLP company to address fundamental issues
- "Being very quiet about what is doing with Kyndi's IP"
- Suggests recognition that original approach failed

## Conclusion

Qlik Insight Advisor represents a cautionary tale of being first-to-market with poorly executed technology. Despite a 5-year head start on the NL analytics trend, fundamental technical issues, overwhelming complexity, and poor user experience resulted in near-zero adoption. The feature exists primarily as a checkbox for RFPs rather than a working solution for business users.

The community consensus is clear: Insight Advisor is "not something that should ever happen" in enterprise software, yet it has persisted for years as a broken feature that damages Qlik's reputation in the modern AI-driven analytics space.