# Tableau Pulse Research Summary
**Date**: January 28, 2025
**Time**: 7:02 AM - 7:30 AM

## Official Sources

### 1. Tableau Pulse Product Page
**URL**: https://www.tableau.com/products/tableau-pulse
**Key Claims**:
- "AI-powered analytics"
- "Proactive insights" 
- "Natural language summaries"
- "Understand the why behind data"

**Reality Found**:
- Actually just tracks metrics over time and sends alerts
- "AI" is limited to natural language generation for describing changes
- No real machine learning models
- Cannot discover patterns or do root cause analysis

### 2. Official Documentation 
**URL**: https://help.tableau.com/current/online/en-us/pulse_intro.htm
**Key Findings**:
- Requires existing published data sources
- Needs time dimension for tracking (daily/weekly/monthly)
- Cloud-only, not available for Tableau Server
- Enhanced features require Tableau+ subscription
- Main functionality: trend detection, outlier alerts, threshold tracking

**Setup Requirements**:
- Tableau Cloud subscription
- Published data sources with proper permissions
- Time-series data (no point-in-time analysis)
- Creator or Explorer role to create metrics
- Embedded credentials or SSO for data access

## Pricing Intelligence

### Tableau Cloud Pricing (2025)
**Source**: Multiple pricing sites (Vendr, Explo, Qrvey)
**Key Findings**:

**Per User/Month (Annual Billing)**:
- Tableau Creator: $75 ($900/year)
- Tableau Explorer: $42 ($504/year)  
- Tableau Viewer: $15 ($180/year)
- Enterprise Creator: $115 ($1,380/year)
- Enterprise Explorer: $70 ($840/year)
- Enterprise Viewer: $35 ($420/year)

**Hidden Costs**:
- Minimum 1 Creator license required
- Multi-year contracts needed for discounts (20-30% premium for single year)
- 200-user enterprise = ~$276,000/year
- Tableau+ required for "Enhanced Q&A" features
- Professional services often needed

## Limitations & Problems

### InterWorks Blog - "5 Things to Consider"
**URL**: https://interworks.com/blog/2023/12/14/5-things-to-consider-when-using-tableau-pulse/
**Date**: December 14, 2023

**Major Limitations Found**:
1. **Metric Proliferation** - Each filter/time range creates new metric, becomes "chaotic mess"
2. **No Table Calculations** - Advanced metrics return errors
3. **Limited Scheduling** - Can't set different schedules per metric
4. **Governance Issues** - Limited control over who creates metrics
5. **Customization Restrictions** - Can only toggle existing insight types

### Documentation Limitations
**From Official Docs**:
- No support for calculations within advanced metrics
- Single time granularity per site
- API doesn't support limiting to user groups
- No project hierarchy or content-based permissions
- Pre-aggregated measures cause errors
- Cloud-only (no on-premise option)

## User Experience Issues

### Common Problems Reported:
1. **Setup Complexity** - Requires proper data modeling first
2. **Permission Hell** - Complex permission requirements
3. **Alert Fatigue** - Too many notifications, limited control
4. **No Real Discovery** - Just monitors what you tell it to
5. **Dashboard Dependency** - Still need traditional dashboards for complex analysis

### Missing Capabilities vs Claims:
- No predictive analytics
- No clustering or segmentation
- No root cause analysis
- No pattern discovery
- No multi-hypothesis testing
- Can't answer "why" questions beyond simple correlations

## Competitive Intelligence

### What Tableau Pulse ACTUALLY Is:
- Metric tracking system with alerts
- Natural language descriptions of changes
- Basic outlier detection
- Threshold monitoring
- Email/Slack notifications

### What It's NOT:
- Not a true AI analytics platform
- Not capable of discovery or investigation
- Not self-service (requires IT setup)
- Not able to work without pre-built data sources
- Not capable of complex analysis

### Scoop Advantages:
1. **Real ML** - 4 actual ML models vs zero
2. **True Discovery** - Finds patterns you didn't know to look for
3. **No Prerequisites** - Connect and analyze immediately
4. **Actual Conversations** - Multi-turn with context vs one-way alerts
5. **Total Cost** - $299/month vs $75-115/user + implementation
6. **Time to Value** - 30 seconds vs weeks of setup

## Evidence Needed:
- [ ] Screenshot of Pulse marketing claims
- [ ] Screenshot of actual Pulse interface showing limitations
- [ ] Screenshot of pricing page
- [ ] Screenshot of setup documentation complexity
- [ ] Screenshot of error messages from advanced metrics
- [ ] User forum complaints

## Key Takeaway:
Tableau Pulse is a metric monitoring and alerting system marketed as "AI analytics." It requires significant investment in Tableau infrastructure, offers no real ML capabilities, and essentially sends natural language notifications about changes in pre-defined metrics. Classic "AI washing" of a basic feature.