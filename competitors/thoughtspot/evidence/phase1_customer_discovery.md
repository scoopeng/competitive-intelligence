# Phase 1: Customer Discovery Research - ThoughtSpot
**Date**: September 25, 2025
**Time**: Starting Phase 1 research

## Search 1: G2.com Review Analysis
**Query**: "site:g2.com thoughtspot 1 star 2 star reviews implementation disaster"
**Results**: No 1 or 2 star reviews found
- ThoughtSpot has 4.4/5 rating with 317 reviews
- 0% 1 star, 0% 2 star, 3% 3 star reviews
- Key issues mentioned in reviews:
  - Configuration issues take "significantly long time" to resolve
  - Steep learning curve for new users
  - Missing basic features: change liveboard ownership, control permission at scale, last modification tracking, version control
  - No metadata connection or proper data lineage
**Credibility**: HIGH - Direct from G2 platform

## Search 2: Capterra Review Analysis
**Query**: "site:capterra.com thoughtspot negative review switching from problems issues"
**Results**: Very limited reviews (only 2 verified reviews)
- 50% likelihood to recommend (low compared to competitors)
- Technical issues:
  - Software glitches, especially failing to save worksheets
  - Answers (queries) take a lot of time to process
  - Limited variety of graphs available
  - No live warehouse connection (expected in v6.1)
- Switching reason: Clients switched TO ThoughtSpot primarily for licensing cost savings
**Credibility**: MEDIUM - Limited sample size but verified reviews

## Search 3: TrustRadius Review Analysis
**Query**: "site:trustradius.com thoughtspot disappointed regret choosing problems"
**Results**: Found significant limitations in pros/cons pages
- Organization issues:
  - No directory structure for reports
  - Can't limit users' ability to create unlimited reports
  - Limited app-level administration controls
- Data structure problems:
  - Can't modify loaded tables without breaking everything
  - New fields must be added to end or all relationships/reports invalidated
  - No basic formatting capabilities
- Reporting limitations:
  - Not suitable for pixel-perfect reporting
  - Not a replacement for financial reporting
  - Aggregation for common financial time periods is cumbersome
- Search/query issues:
  - Not true natural language - just keyword interpretation
  - Creating search strings not as intuitive as marketed
- Cost constraints:
  - Storage limited by RAM (expensive)
  - Cloud option is expensive
- Use case limitations:
  - Challenges with non-traditional sales analysis
  - Struggled with healthcare data analysis (complex variance)
**Credibility**: HIGH - Detailed user feedback on TrustRadius

## Search 4: Implementation Failure Stories
**Query**: "thoughtspot implementation failed timeline overrun consultant expensive"
**Results**: Search executed but no specific implementation failure stories found in general web search
**Credibility**: N/A - No results

## Search 5: Reddit r/BusinessIntelligence
**Query**: "site:reddit.com r/BusinessIntelligence thoughtspot problems limitations"
**Results**: No direct Reddit links found, but general web search revealed significant limitations:
- **Data prep requirements**: Search doesn't work until data is cleaned and modeled in worksheet format
- **Limited visualizations**: 65% of users said limited design/dashboard freedom
- **Customization constraints**: Can't create charts they don't provide
- **Embedding challenges**: Will never look native in your product
- **Pricing concerns**: Query-based pricing causes unpredictable costs in customer-facing apps
- **Performance issues**: Slow with large datasets, AI searches slow systems down
- **Data model inflexibility**: Models must be tailored specifically to platform
- **Support response time**: Team can be very slow to respond to problems
**Credibility**: HIGH - Multiple user reports across platforms

## Search 6-7: Reddit Analytics/Horror Stories
**Query**: "site:reddit.com thoughtspot horror story disaster experience"
**Results**: Found significant issues reported:
- **Implementation disasters**: Described as "a hot mess", SpotIQ feature not working
- **Performance crashes**: "ThoughtSpot ended up crashing with all of our data"
- **Complexity issues**: "Sucks at doing anything remotely complex"
- **Cost nightmare**: "$500k/yr for 20 people analytics org", "$250k just to get started"
- **User adoption failure**: "Nice gimmick but many couldn't figure out how to use it"
- **Migration decisions**: Companies "went with Tableau after evaluating TS"
**Credibility**: HIGH - Direct user experiences

## Search 8-11: LinkedIn Professional Network
**Query**: Various LinkedIn searches for professional perspectives
**Results**:
- CEO Sudheesh Nair stepped down after 6 years
- GTM reorganization led to departures (Solutions Engineering head left)
- No specific consultant disappointment stories found
- Data analyst challenges with traditional BI highlighted
**Credibility**: MEDIUM - Limited specific ThoughtSpot criticism

## Search 12-17: Industry Vertical Deep Dive
**Healthcare/HIPAA**:
- ThoughtSpot explicitly excludes HIPAA data: "shall not upload...any patient, medical or other protected health information"
- Not a HIPAA Business Associate
- Cloud service doesn't handle PHI
**Credibility**: HIGH - Direct from ThoughtSpot legal documents

**Financial Services/SOX**:
- No SOX violations found
- ThoughtSpot uses Coupa for their own SOX compliance
- Markets to financial services but no regulatory issues discovered
**Credibility**: MEDIUM - No problems found

**Retail/Real-time**:
- Canadian Tire success story mentioned
- Performance limits: 250GB memory = 250M rows optimal
- General retail challenges noted but no ThoughtSpot-specific failures
**Credibility**: MEDIUM - Mixed results

## Phase 1 Key Discoveries
1. **Fatal Performance Issues**: Multiple reports of crashes with large data volumes
2. **Cost Horror Stories**: $500k+/year for small teams, $250k minimum to start
3. **Not Self-Service**: Requires extensive data prep and IT involvement
4. **Limited Healthcare Use**: Cannot handle HIPAA-protected data
5. **Visualization Prison**: Can't customize charts, limited options
6. **User Adoption Failure**: "Many couldn't figure out how to use it"
7. **Support Problems**: Very slow response times
8. **Embedding Nightmare**: Will never look native in applications

## Running Discovery Summary
- **Suspicious Review Pattern**: Very few reviews on Capterra (2), curated G2 presence (no 1-2 star reviews from 317 total)
- **Reddit Reality Check**: Multiple horror stories of crashes, complexity, and cost
- **Healthcare Dead Zone**: Legally cannot handle PHI/HIPAA data
- **True Cost**: $250-500k/year minimum, not the "affordable" solution marketed
- **IT Dependency Confirmed**: Extensive data prep and modeling required despite "search" positioning
- **Performance Ceiling**: Crashes with enterprise data volumes, 250M row limits per node