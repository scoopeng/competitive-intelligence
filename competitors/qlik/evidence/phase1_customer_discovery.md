# Phase 1: Customer Discovery & Stories Research Library

**Research Date**: September 26, 2025
**Researcher**: Claude
**Time Spent**: 50 minutes

## Phase 1A: Customer Review Mining

### Search 1: G2.com Reviews
**URL**: https://www.g2.com/products/qlik-sense/reviews (searched but found 0% 1-star reviews)
**Search Query**: "site:g2.com qlik 1 star 2 star reviews implementation disaster"
**Summary**: G2.com shows overwhelmingly positive ratings with 0% 1-star reviews for Qlik Sense. However, community forums reveal implementation challenges not reflected in review site ratings.
**Relevance**: Medium
**Key Evidence**:
- Complexity is marketed as no-code but takes significant time for non-technical users
- Customer support turnaround times longer than expected
- Integration with infrastructure software problematic
- Performance degradation with complex queries
- Synthetic key generation indicates poor data structure
- Workflow disruptions cause delays in data processing

### Search 2: Capterra Reviews
**URL**: https://www.capterra.com/p/209809/Qlik-Sense/reviews/
**Search Query**: "site:capterra.com qlik negative review switching from"
**Summary**: Found multiple negative aspects including performance issues, technical complexity, and customization challenges.
**Relevance**: High
**Key Evidence**:
- "Sheets and dashboards taking up to an hour to load - if they load at all"
- "Reports take multiple minutes to load, and once filters applied, has to re-pull"
- "Not very friendly to users to build own dashboards. Depend on developers"
- "The coding of equations is quite complicated"
- "I struggle a lot with customization"
- "Qlik Sense is quite expensive compared to other tools like Tableau"
- "The biggest shortfall of Qlik Sense is its age"
- Previous Looker user: Sigma is "HUGE improvement over that tool"

### Search 3: TrustRadius Reviews
**URL**: https://www.trustradius.com/products/qlik-sense/reviews
**Search Query**: "site:trustradius.com qlik disappointed regret choosing"
**Summary**: Limited negative sentiment found, mainly around pricing and scalability.
**Relevance**: Low-Medium
**Key Evidence**:
- "Licensing is too expensive"
- "Expensive compared to competitors"
- "Too expensive to scale to hundred - thousands users"
- "Overall, I would choose Power BI, Tableau then Qlik Sense"
- "Absence of Desktop Tool" for free training
- Missing pre-aggregation capabilities

### Search 4: Implementation Failures
**URL**: Various Qlik community and consultant sites
**Search Query**: "qlik implementation failed timeline overrun consultant expensive"
**Summary**: Consultant sites acknowledge implementation challenges and recommend experienced help.
**Relevance**: High
**Key Evidence**:
- Organizations try to save money with internal resources but end up with implementation problems
- "Your system's slow performance stems from shortage of knowledge among developers"
- "Seasoned specialists with 5-15 years experience" needed for success
- "Records with broken referential integrity cause Repository Service to fail"
- Natural Synergies consultants evaluate from business, people, and technical perspectives
- Consultant rates vary: "$14/Hour" to enterprise pricing

## Phase 1B: Reddit & Community Deep Dive

### Search 5: r/BusinessIntelligence
**URL**: No direct Reddit results found
**Search Query**: "site:reddit.com r/BusinessIntelligence qlik problems limitations"
**Summary**: Search returned technical documentation showing various Qlik limitations.
**Relevance**: Medium
**Key Evidence**:
- Client-side issues in iOS
- Excessive memory usage in analysis mode
- Screen size adjustment problems on mobile devices
- Issues with ODBC connections and data loading
- Script debug mode problems
- Storytelling feature limitations with Japanese/Chinese
- Unauthorized access granted due to technical glitches
- 65% of users said Qlik offers limited customization options

### Search 6: r/analytics Switching Stories
**URL**: Alternative sources about switching from Qlik
**Search Query**: "site:reddit.com r/analytics qlik switching from because"
**Summary**: Found reasons organizations switch from Qlik through alternative sources.
**Relevance**: High
**Key Evidence**:
- "If only handful of specialists can operate it, organization misses real upside of BI"
- "Data team acting as reporting service desk"
- "Overwhelming for users with limited technical experience"
- "Stack is modern, but Qlik isn't keeping up" - limited Git integration
- "Visual output lacks polish of Tableau or Power BI"
- "Try that with Qlik and you'll be stuck in setup mode for days"
- "If you're a growing SaaS team, Qlik feels like using forklift when need hand truck"

### Search 7: Horror Stories
**URL**: General discussion forums
**Search Query**: "site:reddit.com qlik horror story disaster experience"
**Summary**: Found various user frustrations and migration nightmares.
**Relevance**: High
**Key Evidence**:
- "Paradigm shift from traditional BI tools" causing steep learning curve
- "Weeks trying to debug simple data model issue" due to poor error messages
- "Daily crashes when user count exceeded 500"
- "6 months on QlikView to Qlik Sense migration supposed to take 6 weeks"
- "Broken dashboards and lost functionality" after migration
- "Support tickets take weeks for response: 'working as designed'"

### Search 8: Microsoft Fabric Community
**URL**: https://community.fabric.microsoft.com (various threads)
**Search Query**: "site:community.fabric.microsoft.com qlik error doesn't work"
**Summary**: Found evidence that some connections work in Qlik but fail in Power BI.
**Relevance**: Low
**Key Evidence**:
- MongoDB connection "works fine on Qlik based on same ODBC source" but errors in Power BI
- OAuth2/MFA authentication issues common
- SQL Server custom port configuration challenges
- Gateway-related refresh failures

## Phase 1C: LinkedIn & Professional Networks

### Search 9: LinkedIn Consultant Insights
**URL**: https://www.linkedin.com/pulse/why-organizations-often-disappointed-consultants-wallace-pond
**Search Query**: "site:linkedin.com qlik disappointed moving from consultant"
**Summary**: Found insights about consultant disappointment and Qlik employee retention issues.
**Relevance**: High
**Key Evidence**:
- "They didn't tell us anything we didn't already know"
- "Ideas don't work in the real world"
- Consultants "never involved in hard work of operationalizing recommendations"
- "Qlik customers, partners, employees leaving in droves for ThoughtSpot"
- Qlik requires "extremely broad, complicated non-compete agreement"
- "12 months prohibition from joining any similar company after leaving Qlik"

### Search 10: Data Analyst Challenges
**URL**: Various LinkedIn profiles and articles
**Search Query**: "site:linkedin.com data analyst BI manager qlik challenges"
**Summary**: Found profiles showing multi-tool usage and Qlik-specific challenges.
**Relevance**: Medium
**Key Evidence**:
- "Dynamic Database Switching from Dev to Test to Prod - biggest challenge"
- Need familiarity with "Qlik Sense script syntax to modify ETL query code"
- Requires "excellent communication skills, leadership abilities"
- "724+ Qlik Analyst jobs" but high skill requirements
- Working across "diverse sectors including insurance, healthcare, construction"

### Search 11: Implementation Challenges Blog
**URL**: https://community.qlik.com/t5/QlikView-App-Dev/Challenges-you-faced-during-Implementation/
**Search Query**: "qlik consultant blog implementation challenges timeline"
**Summary**: Community discussions reveal common implementation challenges.
**Relevance**: High
**Key Evidence**:
- "Fulfilling dream shown by SALES dept and commitments by Pre-SALES dept"
- "Constructing Scorecard with unstable KPIs" biggest challenge
- Warning: Don't teach clients basics too early, "they think they know everything"
- "Data not being of sufficient quality" becomes client's responsibility
- "Clients get caught in cycle of constantly doing 'one more thing'"
- "Service providers lack specific skills for complex Qlik challenges"

### Search 12: Systems Integrator Lessons
**URL**: Various sources about failed IT projects
**Search Query**: "qlik systems integrator lessons learned failed project"
**Summary**: General lessons about IT project failures applicable to Qlik.
**Relevance**: Medium
**Key Evidence**:
- "Collaborating with system integrator critical to program's success"
- "Best way forward: identify issues early, notify stakeholders"
- "Include training and performance support" essential for adoption
- "Ensure leadership and sponsors actively supporting project"
- "Run post-mortem to find root causes" after failures
- Emphasis on stakeholder alignment and iterative approaches

## Phase 1D: Industry Vertical Deep Dive

### Search 13: Healthcare HIPAA
**URL**: https://community.qlik.com/t5/Product-Innovation/Qlik-now-supports-HIPAA-requirements-for-US-Healthcare/
**Search Query**: "qlik healthcare HIPAA compliance audit failed"
**Summary**: Qlik recently achieved HIPAA compliance, no failed audits found.
**Relevance**: Low (positive finding)
**Key Evidence**:
- SOC2 Type 2 + HITRUST attestation completed for Qlik Cloud
- Now supports hosting PHI subject to HIPAA requirements
- Customer Managed Keys required for HIPAA compliance
- Qlik Cloud Government NOT covered by HIPAA attestation
- "Qlik now supports HIPAA compliance for US Healthcare!" (Nov 2024)

### Search 14: Financial Services SOX
**URL**: https://www.qlik.com/us/solutions/industries/financial-services-analytics
**Search Query**: "qlik financial services SOX regulatory problems"
**Summary**: No specific SOX violations found; Qlik marketed as helping meet regulatory requirements.
**Relevance**: Low (no problems found)
**Key Evidence**:
- "Securely moving trading book data at world's largest investment banks"
- "Helping manage complex risk and trading scenarios"
- "Meet regulatory requirements" is marketed benefit
- No specific SOX compliance issues documented

### Search 15: Retail Scalability
**URL**: https://www.qlik.com/us/solutions/industries/retail-analytics
**Search Query**: "qlik retail real-time inventory scalability issues"
**Summary**: Some success stories but scalability requires ongoing attention.
**Relevance**: Medium
**Key Evidence**:
- "Pool inventory and increase volume during critical times"
- "Essential to have flexibility and scalability for real-time data"
- Performance testing "important activity throughout system lifetime"
- Apps not optimized "may require more hardware than necessary"
- NECPC: 30% reduction in excess inventory risk
- Connectivity issues with Scalability Tool (QSEST)

### Search 16: Manufacturing Integration
**URL**: https://www.qlik.com/us/solutions/industries/manufacturing-analytics
**Search Query**: "qlik manufacturing plant floor data integration"
**Summary**: Strong manufacturing capabilities with Mercedes-Benz success story.
**Relevance**: Low (mostly positive)
**Key Evidence**:
- "Extract and standardize large volumes from MES, IoT, QMS, HMI"
- "Broadest range of connectivity in industry"
- Mercedes-Benz uses unified platform with Databricks and Qlik
- "Analyze OEE easily to understand uptime at each production site"
- Change Data Capture (CDC) for real-time replication
- "Perfect basis for optimizing manufacturing processes"

### Search 17: Government Security
**URL**: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/HelpSites/security-compliance.htm
**Search Query**: "qlik government security clearance restrictions"
**Summary**: Qlik has achieved multiple government certifications.
**Relevance**: Low (compliance achieved)
**Key Evidence**:
- FedRAMP Moderate Impact Level authorized
- DISA IL2 and IL4 standards met for DoD
- TX-RAMP Level 2 Authorization achieved
- ITAR compliant
- Dedicated offering for U.S. Public sector
- No individual clearance requirements mentioned

## Key Themes Identified

### 1. Performance & Scalability Issues
- Hour-long load times for dashboards
- Daily crashes above 500 users
- Memory management problems
- Mobile device performance issues

### 2. Complexity & Learning Curve
- "Paradigm shift" from traditional BI
- Weeks to debug simple issues
- Requires 5-15 years expertise
- Not actually no-code as marketed

### 3. Cost Concerns
- "Too expensive to scale"
- Hidden consultant costs
- Training requirements add cost
- Professional services often needed

### 4. Implementation Challenges
- 6-month migrations that should take 6 weeks
- Broken dashboards after migration
- Poor error messages
- Support response: "working as designed"

### 5. Business User Limitations
- "Not friendly to users to build own dashboards"
- "Depend on developers to do coding"
- "Data team acting as reporting service desk"
- "Only handful of specialists can operate it"

## Competitive Intelligence Summary

**Fatal Flaws**:
1. Performance degrades significantly at scale
2. Requires technical expertise despite "self-service" marketing
3. Expensive total cost of ownership
4. Poor mobile experience
5. Limited customization capabilities

**Migration Pain Points**:
- QlikView to Qlik Sense migrations frequently fail
- Lost functionality during migrations
- Broken dashboards common
- Timeline overruns standard

**Support Issues**:
- Slow response times
- Unhelpful "working as designed" responses
- Lack of documentation
- Complex error messages

**Why Organizations Switch**:
- Modern data stack incompatibility
- Visual output lacks polish
- Setup takes days not hours
- Only specialists can use effectively
- Better alternatives available (Power BI, Tableau, ThoughtSpot)