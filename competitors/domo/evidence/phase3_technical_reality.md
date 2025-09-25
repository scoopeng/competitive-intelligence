# Phase 3: Technical Reality & Competitive Context - Domo
**Date**: September 25, 2025
**Purpose**: Validate technical claims, performance issues, and competitive positioning

## Research Library

### Search 18: Performance & Response Time Issues
**URL**: https://community-forums.domo.com/main/discussion/50763/domo-slow-to-pull-in-data
**Date**: September 25, 2025
**Search Query**: "Domo slow performance response time seconds query lag dashboard"
**Summary**: Widespread performance issues documented in community forums
**Relevance**: Very High
**Key Evidence**:
- **Load Times**: "30 seconds to 1 minute just to open analyzer"
- **Dashboard Rendering**: "5-10 seconds to eventually render" for embedded dashboards
- **Extreme Cases**: "Almost 5 minutes to login and run a card"
- **Query Timeouts**: "Queries will time out if they exceed 1 minute"
- **Data Lag**: "Lagging few hours behind compared to SQL console"
- **Card Limits**: Performance degrades with 30-40 cards, recommended under 15
- **Large Datasets**: Problems reported with datasets over 20 million rows
- **Browser Issues**: "Performance due to browser/machine capability"
---

### Search 19: Memory & Resource Requirements
**URL**: Various Domo documentation and forums
**Date**: September 25, 2025
**Search Query**: "Domo memory requirements GB RAM crashes out of memory errors"
**Summary**: Memory-intensive operations cause crashes, especially in Workbench
**Relevance**: High
**Key Evidence**:
- **Workbench Requirements**: 250MB minimum, 2GB recommended hard drive
- **Memory Issues**: "Windows uses disk space as memory, slowing performance"
- **CPU Usage**: "14% CPU and 37% memory when Workbench appears slow"
- **Service Crashes**: "Workbench service crashing and not restarting"
- **Preview Crashes**: "Crashes commonly occur when hitting preview button"
- **Concurrent Jobs**: Need to limit jobs to prevent resource exhaustion
- **MySQL Driver**: Memory issues with MySQL requiring parameter tuning
---

### Search 23: API Rate Limits & Developer Issues
**URL**: https://community-forums.domo.com/main/discussion/56897/
**Date**: September 25, 2025
**Search Query**: "Domo API rate limits throttling developers frustrated"
**Summary**: Undocumented API limits frustrating developers
**Relevance**: High
**Key Evidence**:
- **No Documentation**: "Couldn't find allowed limits/quota in documentation"
- **Hidden Thresholds**: "Errors when request body exceeds magical threshold"
- **Query Cap**: "1 million rows cap" on API queries
- **Webform Limits**: No documentation on rate limits for automation
- **Developer Frustration**: "Struggling with undocumented or poorly communicated limits"
- **Trial and Error**: Need workarounds through experimentation
---

### Search 28: Competitive Positioning vs Tableau
**URL**: https://www.domo.com/competitors/domo-vs-tableau
**Date**: September 25, 2025
**Search Query**: "Domo vs Tableau why customers switch comparison choose"
**Summary**: Clear patterns in switching decisions between platforms
**Relevance**: Very High
**Key Evidence**:

**Switch TO Domo from Tableau**:
- Ease of use for non-technical users
- 1000+ pre-built connectors vs manual setup
- Cloud-native architecture advantage
- Better collaboration features

**Switch FROM Domo to Tableau**:
- **Cost**: "Tableau is cheaper and more flexible"
- **Analytics Depth**: "Tableau wins in depth of analysis"
- **Visualizations**: "Tableau is one of the best in the game"
- **Market Share**: Tableau 2.25% vs Domo 0.59%
- **Performance Issues**: "Major complaints about Domo dashboard performance"
---

### Search 35: Hidden Costs & Professional Services
**URL**: https://www.clarista.io/blog/the-hidden-cost-of-domos-data-vault
**Date**: September 25, 2025
**Search Query**: "Domo hidden costs professional services implementation consultant fees"
**Summary**: Significant hidden costs beyond advertised pricing
**Relevance**: Very High
**Key Evidence**:
- **Professional Services**: "Additional one-time fee for setup hours"
- **Base Reality**: "At least $10K/year but actual much higher"
- **100 Users**: "$95,800 actual cost"
- **Enterprise Range**: "$50,000 to $100,000+ depending on usage"
- **Add-ons Separate**: "Support, training, custom engineering priced separately"
- **Consumption Penalty**: "Penalized for running frequent dataset updates"
- **Storage Redundancy**: "Source storage + Vault fees + ETL overhead"
- **User Licensing**: "$750 per user whether viewer or developer"
- **Shocking Quote**: "Cost of Domo is roughly 1% of company's entire revenue"

## Technical Reality Summary

### Performance Issues (Quantified)
1. **30-60 seconds** to open analyzer
2. **5-10 seconds** dashboard rendering
3. **1 minute timeout** for queries
4. **20M row** dataset problems
5. **15 card limit** for acceptable performance

### Resource & Stability Issues
1. Workbench crashes on preview
2. Service won't stay running
3. Memory exhaustion with concurrent jobs
4. Browser-dependent performance

### API & Integration Problems
1. No documented rate limits
2. Hidden query caps (1M rows)
3. "Magical thresholds" causing errors
4. Developer frustration widespread

### Competitive Losses to Tableau
1. Cost (Domo much more expensive)
2. Analytics depth
3. Visualization quality
4. Performance complaints

### True Cost Reality
1. **$95,800** for 100 users (not advertised)
2. **1% of company revenue** in one case
3. Professional services required
4. Hidden consumption penalties
5. Storage redundancy costs