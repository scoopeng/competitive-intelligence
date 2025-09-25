# Phase 2 Research Library - Tableau Pulse Technical Reality
**Phase 2 Executed: 2025-09-25**

## Performance and Scalability (Searches 18-22)

**URL**: Multiple performance documentation sources
**Date**: 2025-09-25
**Search Query**: Search #18: Tableau Pulse performance benchmark response time
**Summary**: Performance heavily dependent on workbook design. Default VizQL session timeout is 30 minutes. Query compilation complexity impacts performance significantly. Real-time capabilities marketed but actual performance varies with dataset size.
**Relevance**: High
**Key Evidence**:
- "Majority of slow dashboards caused by poor design - too many charts or too much data"
- "If slow in data source, will be slow in Tableau Desktop and Server"
- "More views and data sources = slower response time"
- "Long compile query times indicate queries are complex"
- Default 30-minute session timeout still consumes memory/CPU when idle
- Performance recording tool needed to identify bottlenecks
---

**URL**: Hardware requirements documentation
**Date**: 2025-09-25
**Search Query**: Search #19: Memory requirements CPU usage RAM crashes
**Summary**: Production systems require 64GB RAM minimum for 2021.4+. Memory management issues persist with idle sessions consuming resources. Extract memory held indefinitely for performance. Risk of crashes without proper configuration.
**Relevance**: High
**Key Evidence**:
- Minimum testing: 4 cores, 8GB RAM, 15GB disk
- Production recommended: 8 physical cores, 32GB RAM, 50GB disk
- Current standard: 64GB RAM for 2021.4+ versions
- "May not start without at least 20GB memory"
- CPU must support SSE4.2 and POPCNT instructions
- "Even idle VizQL sessions consume memory and CPU cycles"
- 1 CPU to 4GB RAM ratio recommended
---

**URL**: Scalability testing documentation
**Date**: 2025-09-25
**Search Query**: Search #20: Concurrent users scalability limits
**Summary**: Tableau Pulse scaled from 500 to 20,000 daily email digests during pilot. Required significant infrastructure investment. Site capacity limited to 10 concurrent extract refreshes and subscriptions. No published hard limits for concurrent users.
**Relevance**: High
**Key Evidence**:
- Scaled from 500 to 20,000 email digests/day in pilot
- Required "horizontal and vertical scaling techniques"
- Site limit: 10 concurrent extract refreshes
- Site limit: 10 concurrent subscriptions
- Site limit: 10 concurrent metric refreshes
- TabJolt tool required for load testing
- No published maximum concurrent user limits
---

**URL**: Database timeout documentation
**Date**: 2025-09-25
**Search Query**: Search #21: Database timeout connection errors
**Summary**: Multiple timeout types cause failures. Connection and command timeouts both problematic. No specific Pulse timeout documentation found, inherits general Tableau limitations.
**Relevance**: Medium
**Key Evidence**:
- 30-minute default VizQL session timeout
- Connection timeout vs command timeout issues
- "Performance issues with extremely large datasets"
- Timeout configuration requires TSM command-line access
---

**URL**: Uptime and SLA documentation
**Date**: 2025-09-25
**Search Query**: Search #22: Uptime downtime SLA outage
**Summary**: Limited specific Pulse SLA information. Inherits general Tableau Cloud availability. No separate Pulse uptime metrics published.
**Relevance**: Low
**Key Evidence**:
- Tableau Cloud general SLA applies
- No Pulse-specific uptime guarantees
- Service interruptions affect all Tableau services including Pulse
---

## Integration and Developer Experience (Searches 23-27)

**URL**: REST API documentation
**Date**: 2025-09-25
**Search Query**: Search #23: API limitations REST developer integration
**Summary**: Pulse REST API only available on Tableau Cloud (API 3.24, Dec 2024). Not available for Tableau Server at all. Complex authentication with connected apps required. Limited insight types supported. Request frequency limits apply.
**Relevance**: High
**Key Evidence**:
- "Pulse REST API methods only available in API 3.24 and later"
- "Not available for Tableau Server" - Cloud only
- Must use connected apps for authentication
- "Bundles are rich and complex objects" difficult to build manually
- Only supports "ban", "springboard", and "basic" insight types
- Request frequency limits with quotas
- CORS configuration required via TSM
- Most examples in XML, not JSON
---

**URL**: SSO integration documentation
**Date**: 2025-09-25
**Search Query**: Search #24: SSO integration broken SAML authentication
**Summary**: Complex authentication requirements for Pulse. Connected apps mandatory for embedding. Additional configuration burden for enterprises.
**Relevance**: Medium
**Key Evidence**:
- Connected apps required for Pulse embedding
- CORS must be enabled by server admins
- Complex permission model for data source access
- Authentication adds significant integration complexity
---

**URL**: Mobile app performance
**Date**: 2025-09-25
**Search Query**: Search #25: Mobile app performance issues
**Summary**: Mobile experience acknowledged as inferior to desktop. Limited mobile-specific documentation for Pulse.
**Relevance**: Medium
**Key Evidence**:
- Mobile apps "less robust than desktop version"
- Performance degradation on mobile platforms
- Limited mobile optimization for Pulse features
---

**URL**: Embedding and iframe security
**Date**: 2025-09-25
**Search Query**: Search #26: Embedding iframe security CSP issues
**Summary**: Embedding requires Tableau Cloud 2024.1+ and Embedding API 3.8+. CORS configuration mandatory. Limited backward compatibility.
**Relevance**: High
**Key Evidence**:
- Available only on Tableau Cloud 2024.1+
- Requires Embedding API library version 3.8+
- CORS configuration via TSM required
- Connected apps authentication mandatory
- No backward compatibility
---

**URL**: REST API documentation gaps
**Date**: 2025-09-25
**Search Query**: Search #27: REST API documentation incomplete missing
**Summary**: Documentation primarily in XML format. JSON examples require manual conversion. Complex data structures poorly documented.
**Relevance**: High
**Key Evidence**:
- "REST API documentation provides most syntax examples in XML"
- Developers must convert to JSON using Jackson Parser
- Complex bundle structures challenging to understand
- Recommendation to use UI first then inspect JSON
---

## Competitive Positioning (Searches 28-34)

**URL**: Power BI comparison analysis
**Date**: 2025-09-25
**Search Query**: Search #28: Tableau Pulse vs Power BI Copilot comparison
**Summary**: Power BI Copilot more integrated with Microsoft ecosystem. Tableau Pulse higher cost but claims better data storytelling. Both have AI limitations. Power BI requires Premium for Copilot, Tableau requires Tableau+ for Pulse.
**Relevance**: High
**Key Evidence**:
- Power BI: $14/user/month Pro, $24 Premium Per User
- Tableau: $75 Creator, $42 Explorer, $15 Viewer
- Power BI Copilot "limited to Premium license holders"
- Tableau Pulse "requires Tableau+ premium license"
- Power BI better for Microsoft shops
- Tableau "on the expensive side" - Creator ~$6,000/user/month in some regions
- Job market: 7,638 Power BI jobs vs 4,632 Tableau jobs in India
---

**URL**: ThoughtSpot comparison
**Date**: 2025-09-25
**Search Query**: Search #29: vs ThoughtSpot comparison
**Summary**: Limited direct Pulse vs ThoughtSpot comparisons found. ThoughtSpot positioned as more search-focused analytics.
**Relevance**: Low
**Key Evidence**:
- ThoughtSpot focuses on search-driven analytics
- Limited head-to-head Pulse comparisons available
---

**URL**: Qlik comparison
**Date**: 2025-09-25
**Search Query**: Search #30: vs Qlik comparison
**Summary**: Limited direct Pulse vs Qlik comparisons. Qlik has smaller market share but specific strengths in associative model.
**Relevance**: Low
**Key Evidence**:
- Limited Pulse-specific comparisons with Qlik
- Market share differences significant
---

**URL**: Market share trends
**Date**: 2025-09-25
**Search Query**: Search #31: Market share declining adoption 2024 2025
**Summary**: Power BI gaining market share over Tableau. More competitors entering leaders quadrant. Tableau facing increased competition.
**Relevance**: High
**Key Evidence**:
- "Power BI ahead of Tableau in 2024 report"
- "More tools entering leaders' quadrant" - increased competition
- Open-source alternatives gaining traction
- Sigma Computing winning Excel users
---

**URL**: Gartner analysis (not found)
**Date**: 2025-09-25
**Search Query**: Search #32-33: Gartner/Forrester analysis
**Summary**: No specific Gartner or Forrester analysis of Tableau Pulse found. Lack of analyst coverage notable for new feature.
**Relevance**: Low
**Key Evidence**:
- No Gartner Magic Quadrant placement for Pulse specifically
- No Forrester Wave analysis found
- Limited analyst attention to Pulse as standalone feature
---

**URL**: Analyst feedback
**Date**: 2025-09-25
**Search Query**: Search #34: Analyst report customer feedback
**Summary**: Limited formal analyst coverage of Pulse. Most feedback comes from user forums rather than analyst reports.
**Relevance**: Low
**Key Evidence**:
- Sparse analyst coverage of Pulse specifically
- Feedback primarily from community forums
---

## Economic Impact and TCO (Searches 35-41)

**URL**: Pricing analysis from multiple sources
**Date**: 2025-09-25
**Search Query**: Search #35: Hidden costs total cost ownership TCO
**Summary**: Tableau Pulse requires Tableau+ premium license on top of base costs. Infrastructure, training, and scaling costs add significantly to TCO. Multi-year contracts virtually mandatory for discounts. Viewer licenses still cost $15/month unlike competitors.
**Relevance**: High
**Key Evidence**:
- "AI features like Tableau Pulse restricted to higher-tier plans"
- Tableau+ premium required for Pulse (additional cost)
- Infrastructure costs for Server deployments
- "50-person team scaling to 500 users = $50,000+ monthly"
- Charges $15/month even for view-only users
- "Multi-year contracts virtually mandatory" for discounts
- 20-30% premium for single-year deals
- Training costs significant due to complexity
---

**URL**: Professional services costs
**Date**: 2025-09-25
**Search Query**: Search #36-37: Training requirements consultant fees
**Summary**: 2-6 months typical Tableau learning curve. Formal training often required. Consulting costs add to implementation expense. Pulse designed to be simpler but still requires Tableau foundation.
**Relevance**: High
**Key Evidence**:
- "2-6 months to learn Tableau" average
- "Few weeks for basic proficiency"
- "Several months for advanced techniques"
- 3 months minimum for Desktop Specialist certification
- Pulse "simpler by design" but requires Tableau knowledge
- Formal training programs recommended
- Consulting hours needed for implementation
---

**URL**: Maintenance overhead
**Date**: 2025-09-25
**Search Query**: Search #38: Maintenance overhead admin requirements
**Summary**: No automatic report updates requiring manual effort. Site admins must manage digest preferences via API. Ongoing maintenance burden significant.
**Relevance**: High
**Key Evidence**:
- "No feature for scheduling provided"
- "Significant manual effort required to update data"
- Site admins manage preferences via API
- Continuous maintenance required
- IT staff needed for Server deployments
---

**URL**: Time to value analysis
**Date**: 2025-09-25
**Search Query**: Search #39: Time to value delayed insights
**Summary**: 2-6 months typical implementation time. Pulse positioned as faster but still requires setup. Data quality critical for accurate insights.
**Relevance**: Medium
**Key Evidence**:
- Standard Tableau: 2-6 months to proficiency
- Pulse "plug-and-play" but needs proper data foundation
- Data quality testing required before insights trusted
---

**URL**: ROI analysis
**Date**: 2025-09-25
**Search Query**: Search #40: ROI business value failure
**Summary**: High costs make ROI challenging for small/medium businesses. Startup companies particularly affected. Value depends heavily on data quality and user adoption.
**Relevance**: High
**Key Evidence**:
- "Licenses so expensive, startup company can't afford"
- "Cost can be prohibitive" for small organizations
- Team of 5: ~$1,560/year vs Power BI $600
- "No startup-friendly pricing tier"
- Hidden costs impact budget significantly
---

**URL**: Accuracy and hallucination issues
**Date**: 2025-09-25
**Search Query**: Search #41: Accuracy problems hallucination errors
**Summary**: Tableau officially acknowledges hallucination risks in Pulse. LLMs can generate plausible but incorrect information. Language processing issues documented, especially with Chinese. Data quality dependencies critical.
**Relevance**: High
**Key Evidence**:
- "Occasional hallucinations may occur" - official Tableau warning
- "LLMs can hallucinate... creating output that sounds plausible but contains incorrect information"
- Language blending issues with Chinese languages
- "Reliability hinges on accuracy of underlying data"
- Automated testing recommended to ensure quality
- "Risks of hallucination" acknowledged in design docs
---

## Phase 2 Summary

### Critical Technical Limitations:
1. **Cloud-Only API**: Pulse REST API not available for Tableau Server
2. **Memory Intensive**: 64GB RAM required for production
3. **No Scheduling**: Manual updates required, no automation
4. **Hallucination Risk**: Officially acknowledged AI accuracy issues
5. **Complex Integration**: Connected apps, CORS, limited APIs
6. **Premium Lock**: Requires Tableau+ on top of base licenses

### Cost Reality:
- Base: $75/month Creator minimum
- Plus Tableau+ premium for Pulse
- $15/month even for viewers
- Multi-year contracts mandatory for discounts
- Training: 2-6 months typical
- Hidden infrastructure costs

### Competitive Position:
- Power BI gaining market share
- More expensive than all major competitors
- Limited analyst coverage of Pulse
- Job market favoring Power BI skills

### Adoption Barriers:
- Server customers completely excluded
- 2-6 month learning curve
- Manual maintenance overhead
- Data quality dependencies
- Hallucination risks acknowledged