# Phase 3: Technical Reality & Competitive Context Research Library

**Research Date**: September 26, 2025
**Researcher**: Claude
**Time Spent**: 60 minutes

## Phase 3A: Technical Performance Analysis (10 searches)

### 1. Performance & Response Time Issues
**Search**: "qlik slow performance response time seconds query"
**Critical Evidence Found**:
- "App Response time (App Size: 400MB) is very SLOW, resulting in Escalations from Client"
- "Select query taking too long to load and getting failed after 2 hrs" even with 0.3-0.4 million records
- "Takes almost an hour to add updated data to dashboard"
- "Displaying asset section is very slow (3-4 seconds to display sheet list)"
- **55-second API timeout**: "Blocks will wait for maximum of 55 seconds to receive an API response"
- Average CPU utilization around 70% = system oversubscribed
- 40 columns, 28 million records = 16 minutes to load (just SELECT *)

### 2. Memory Requirements & Crashes
**Search**: "qlik memory requirements GB RAM crashes"
**Critical Evidence**:
- **Daily crashes**: "At least once a day, web servers are crashing due to memory usage spike"
- "Servers with 64 GiB Memory are going down continuously, Qlik Service engine consuming 99% memory"
- "When you reach Max threshold you are in trouble...QIX does not work well with paging, data has to be in RAM"
- **Memory expansion factor**: 2-10x compression ratio - files expand massively in RAM
- 32GB RAM "just is too little RAM for your data"
- **Cloud limits**: Standard peak reload memory 10 GB in app, up to 40 GB hub/scheduled

### 3. Concurrent User Scalability
**Search**: "qlik concurrent users limit scalability testing"
**Key Limits**:
- **6 users/second** boundary for user creation/ramp-up (product limitation)
- Can scale to 4,000 user sessions (Windows architecture)
- 15k concurrent users possible with large clusters
- Maximum 5 parallel connections per professional user
- **Real-world vs test**: "Scalability tools may show better performance than actual user experience"
- Guardrails restrict parallel reloads to prevent overload

### 4. Database Timeout Issues
**Search**: "qlik database timeout connection errors"
**Common Problems**:
- Default timeout: 30-31 seconds for many operations
- "ERROR [HYT00] Timeout expired" after 1-2 minutes
- SQL Server Remote Query timeout: 600 seconds (10 minutes)
- MongoDB Socket Timeout default: -1
- Tables locked by write operations cause read timeouts
- Heavy loading = insufficient available connections

### 5. Uptime & Availability
**Search**: "qlik uptime downtime SLA breach outage"
**Reliability Concerns**:
- StatusGator tracked 107+ outages over 4 years
- Users can monitor at status.qlikcloud.com
- Multiple AWS regions but still has outages
- Fitch downgraded Qlik to 'B' rating (November 2024)
- Documents show as available but fail to load when node unavailable

### 6. API Rate Limiting
**Search**: "qlik API rate limits throttling developers"
**Developer Restrictions**:
- Rate limits enforced since November 1, 2022
- Per tier, per user, per tenant evaluation
- HTTP 429 Too Many Requests errors common
- Tenant rate limit = (user limit) × (users) × 0.5
- POST /api/v1/reloads: 50 requests/minute (was 10)
- Cannot customize per-customer or per-tenant

### 7. SSO/SAML Integration Issues
**Search**: "qlik SSO integration broken SAML authentication"
**Authentication Problems**:
- "Error 400 - Bad request" for SAML responses
- Missing essential parameters: AssertionConsumerServiceURL, NameIDPolicy
- UserID mismatches between IdP and Qlik
- Multi-node SSO failures (works on central, fails on RIM nodes)
- Hub stuck loading after successful authentication
- Qlik Support cannot help with initial SAML setup

### 8. Mobile Performance
**Search**: "qlik mobile app terrible performance user"
**Mobile-Specific Issues**:
- "Terrible performing apps" with section access
- Charts taking over a minute to load on mobile
- "Initializing" messages for long periods
- "Connection timed out because of inactivity"
- 10 GB apps face extreme slowness
- Enabling diagnostics impacts mobile performance
- Apps work with 1-3 users but fail with 10+

### 9. Embedding Security (CSP)
**Search**: "qlik embedding iframe security CSP issues"
**Security Complications**:
- "Refused to frame" errors due to CSP violations
- frame-ancestors directive misconfiguration common
- Localhost embedding often fails
- OAuth limitations for iframe embedding
- HTTPS required for all embedding
- Third-party cookie blocking issues
- Management Console CSP configuration complex

### 10. API Documentation
**Search**: "qlik REST API documentation incomplete missing"
**Documentation Problems**:
- OpenAPI specs missing key elements
- Empty servers.url fields
- Incorrect endpoint paths (/v1/apps instead of /api/v1/apps)
- OAuth schema authentication not supported in REST Connector
- "Please let us know!" requests on multiple doc pages
- Breaking changes to "enhance usability"

## Phase 3B: Competitive Positioning Research (7 searches)

### 11. Qlik vs Tableau
**Search**: "qlik vs Tableau why customers switch"
**Why They Leave Tableau for Qlik**:
- Tableau engine slows dramatically with large volumes
- Performance worsens scaling to thousands of users
- APIs limited - can only embed complete dashboard
- Requires users to be authors to interact with data

**Why They Choose Tableau over Qlik**:
- Simpler learning curve, intuitive drag-drop
- Superior visualization capabilities
- Pre-built dashboards and templates
- Strong mobile compatibility
- Better for simpler datasets

### 12. Qlik vs ThoughtSpot
**Search**: "qlik vs ThoughtSpot RFP evaluation lost deal"
**RFP Decision Factors**:
- ThoughtSpot: 4.6 stars vs Qlik: 4.5 stars (Gartner)
- ThoughtSpot wins on ease of use (8.8 vs 8.4)
- ThoughtSpot better support (8.7 vs 8.0)
- Qlik wins on visualization (9.4 vs 8.6)
- Qlik better data blending (8.9 vs 8.3)
- ThoughtSpot: "No technical expertise required"
- Qlik: "Steep learning curve" for non-technical users

### 13. Qlik vs Power BI
**Search**: "qlik vs Power BI comparison customers choose alternative"
**Market Reality**:
- Power BI: 13.84% market share (53,901 users)
- Qlik Sense: 2.36% market share (9,206 users)
- Power BI Pro: $10/user/month
- Qlik: Must contact sales for pricing

**Why Organizations Choose Power BI**:
- "Much more intuitive for non-technical people"
- Seamless Microsoft integration
- Free desktop version available
- "Qlik looks outdated in terms of UX and visuals"

### 14. Market Share Trends
**Search**: "qlik losing market share declining adoption 2024 2025"
**Current Position**:
- 4.29% market share in data analytics
- 2.35% in data visualization
- Datadog (29.82%), Tableau (26.09%) dominate
- Fitch downgraded to 'B' rating (Nov 2024)
- 15,313 companies using Qlik Sense (2025)
- Leader in Gartner MQ for 15 years (but declining influence)

### 15. Customer Complaints
**Search**: "qlik Gartner customers complain disappointed"
**Key Complaints**:
- "Forced SaaS migration" without fair transition
- "Only one person can edit any dashboard"
- "$100k a year reporting service you get free with SQL"
- "Lost sight of long-term relationships and trust"
- Support tickets closed before resolution
- Account managers "too busy" to speak

### 16. POC Failures
**Search**: "qlik proof of concept POC failure unsuccessful"
**Why POCs Fail**:
- 78% of IT executives: <50% POCs reach production
- Misunderstood requirements common
- Key SMEs unavailable (busiest people)
- "Concept proven but doesn't provide expected value"
- High opportunity cost vs other deals
- Disconnect between business and technology groups

### 17. Customer Migration
**Search**: "qlik customers moving to competitors migration"
**Migration Reality**:
- Search revealed Qlik trying to PREVENT migration
- Free cloud tenant offers for existing customers
- Acquired migration tools to keep customers
- No public evidence of mass exodus
- Focus on QlikView → Qlik Cloud migration
- Trying to retain 40,000+ customers

## Phase 3C: Economic Impact Deep Dive (7 searches)

### 18. Pricing & Licensing
**Search**: "qlik pricing license cost per user enterprise"
**Pricing Structure**:
- **Cloud**: $825-$2,700/month for 20 users
- **Legacy QlikView**: $1,395 per named user
- **Concurrent**: $15,495 per concurrent user
- **Server**: $36,150 per server
- No public enterprise pricing (must contact sales)
- Capacity-based model replaced per-user
- "Hard to know what you'll pay"

### 19. Hidden Implementation Costs
**Search**: "qlik hidden costs consultant implementation total"
**Total Cost Reality (50 users)**:
- License fees: $50,000-$150,000+
- Implementation: $50,000-$200,000
- Training: $15,000-$30,000
- **First-year total**: $115,000-$380,000+
- Consultant rates: $12-$76/hour
- Infrastructure costs additional
- Ongoing maintenance extra
- "Deciphering pricing model is a headache"

### 20. ROI Studies
**Search**: "qlik ROI return on investment business value case study"
**Positive ROI Claims**:
- Forrester study: 209% ROI, $6.4M benefits over 3 years
- Everwell: 645% ROI, 1.9 months payback
- 400-450 hours/month saved (40-50% reduction)
- Kenway client: $18,000/week recovered
- Ewals: 400% improvement, 1.7 year payback

**Note**: These are Qlik-commissioned or featured studies

### 21. TCO Comparisons
**Search**: "qlik TCO study comparison total cost ownership"
**TCO Analysis**:
- Power BI appears cheaper initially
- Power BI Pro: €8.40/user/month
- Qlik Analyzer: €36.25/user/month
- Power BI 1GB limit forces Premium ($4,212/month)
- Azure infrastructure adds to Power BI TCO
- Qlik scores well in low-margin businesses
- Legacy system savings: $2.1M over 3 years (claimed)

### 22. Training & Certification Costs
**Search**: "qlik training costs certification budget time"
**Training Investment**:
- **Certification exam**: $250 USD each
- **Exam duration**: 2 hours, 50-60 questions
- **Pass rate**: 58% required
- Public ILT Passport: 1-year access
- Private training available (custom pricing)
- "Significant preparation needed"
- Must know SQL, ETL, data modeling

### 23. Productivity Loss
**Search**: "qlik productivity lost downtime users waiting"
**Productivity Impact**:
- **50% of time lost** to unplanned work in reactive environments
- **43 hours/year** lost per employee (5 working days)
- 3,000 hours annually reclaimed by reducing downtime
- 74% of employees "overwhelmed or unhappy" with data
- 31% took sick leave due to data-related stress
- 12-hour dashboards lost when not saved
- Session timeout: 30 minutes default

### 24. Professional Services Rates
**Search**: "qlik professional services charge hourly cost estimate"
**Consulting Costs**:
- Global average: $76/hour for Qlik consultants
- US average: $50-54/hour
- Day rate: $460 average worldwide
- Official Qlik services: Must contact for quote
- Implementation often requires consultants
- "Seasoned specialists with 5-15 years" needed

## Summary of Phase 3 Findings

### Technical Reality
- **Performance**: Hour-long loads, 55-second timeouts, daily crashes
- **Scalability**: 6 users/second limit, crashes at 500+ users
- **Memory**: 99% consumption, requires all data in RAM
- **Mobile**: "Terrible performance", minute+ load times
- **Integration**: SAML failures, CSP violations, API rate limits

### Competitive Position
- **Market Share**: 2.36% and declining (vs Power BI 13.84%)
- **Customer Sentiment**: "Lost sight of relationships and trust"
- **vs Competitors**: Loses on ease of use, wins on visualization
- **POC Success**: <50% reach production
- **Migration**: Trying to prevent exodus with free offers

### Economic Impact
- **Total Cost**: $115,000-$380,000+ first year for 50 users
- **Hidden Costs**: Implementation, training, consultants, infrastructure
- **Productivity**: 50% time lost to unplanned work
- **Training**: $250/exam, 58% pass rate, weeks of preparation
- **Consultants**: $50-76/hour, often required
- **ROI Claims**: 209% (but Qlik-commissioned studies)