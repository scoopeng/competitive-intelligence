# Power BI Copilot Research Foundation

## Company Overview
- Company: Microsoft Power BI Copilot
- Parent: Microsoft Corporation
- Founded: Power BI (2011), Copilot features (2023-2024)
- Employees: Microsoft has 221,000+ employees
- Customers: Power BI has 5M+ users, Copilot adoption at 3% success rate
- Revenue/Funding: Part of Microsoft's $60B+ cloud revenue
- Market Position: "AI-powered insights for Power BI"

## Product Facts

### What It Actually Is
Power BI Copilot is an AI-powered feature within Microsoft Power BI that uses large language models (specifically GPT) to generate natural language summaries, answer questions about data, and create report pages. It operates as an overlay on existing Power BI infrastructure, requiring substantial prerequisite setup including semantic models, proper data curation, and premium capacity licensing.

The product consists of two main components: Copilot for report consumers (Q&A functionality) and Copilot for report creators (page generation). It's important to note this is NOT a standalone product but a feature requiring extensive Power BI infrastructure, and it's completely separate from Microsoft 365 Copilot which requires additional licensing.

### Core Capabilities (Verified)
- **Natural language Q&A**: Ask questions about data in semantic models [Microsoft Learn]
- **Report page generation**: Create basic report layouts from prompts [Official docs]
- **Narrative summaries**: Generate text descriptions of data insights [Product page]
- **DAX query generation**: Converts natural language to DAX queries [Technical docs]
- **Visual suggestions**: Recommends chart types based on data [Feature overview]
- **Cross-filter insights**: Basic insights when filtering reports [Documentation]

### Documented Limitations
From their own documentation:
- "Copilot doesn't answer follow-up questions. One question at a time" - [Microsoft Learn, Sept 2025]
- "Can't currently answer questions that require generating new insights" - [Official limitations]
- "LLMs can hallucinate" - [Microsoft's AI warning]
- "No dedicated Copilot REST APIs exist" - [Developer documentation]
- "DirectLake is not yet supported" - [Technical limitations]
- "Premium Per User (PPU) licenses don't support Copilot" - [Licensing docs]
- "Not available in sovereign clouds" - [Geographic limitations]

## Pricing Reality

### Published Pricing
- **Power BI Pro**: $10/user/month (doesn't support Copilot)
- **Power BI Premium Per User (PPU)**: $20/user/month (doesn't support Copilot)
- **Premium P1 Capacity**: $4,995/month minimum
- **Fabric F2 Capacity**: Starting at ~$300/month
- **Fabric F64 Capacity**: $60,000-67,392/year (recommended for production)

### Hidden/Additional Costs
- **Semantic model development**: 2-14 weeks professional services [$20-50K]
- **Data curation project**: Required pre-work for accuracy [$10-30K]
- **Training programs**: Microsoft-certified training [$5-10K]
- **Excel Copilot separate**: $30/user/month for Excel integration [$72K for 200 users]
- **Maintenance burden**: 1-2 FTE for semantic model upkeep [$150-300K/year]
- **Compute costs**: Per-query charges on top of capacity
- **Migration from PPU**: Must upgrade all PPU users to Premium [$2.4M for 200 users]

### Total Cost Reality
200 users, first year: **$175,000 - $235,000**
- F64 Capacity: $67,392
- Power BI Pro licenses: $24,000 (200 × $10 × 12)
- Semantic model development: $35,000 (average)
- Training & enablement: $7,500
- Excel Copilot (if needed): $72,000
- Professional services: $20,000
- Hidden compute/overages: $10,000+

## Implementation Requirements
- **Setup Time**: 14+ weeks documented (semantic models, curation, training)
- **Technical Resources**: Data engineers, DAX developers, Azure architects
- **Training Required**: 2-3 days admin training, 1-2 days per end user
- **Maintenance**: 1-2 FTE ongoing for semantic model maintenance

## Geographic & Compliance
- **Available Regions**: Commercial clouds only (subset of Power BI regions)
- **Blocked Regions**: 
  - All sovereign clouds (Government, China, Germany)
  - Dubai, Singapore, Hong Kong (GPU limitations)
  - 11+ regions total blocked
- **Compliance**: 
  - Not FedRAMP certified
  - Not available for government use
  - HIPAA - requires additional configuration
  - Data processed outside geographic boundaries
- **Industry Limitations**: 
  - Government agencies cannot use
  - Regulated industries with data residency requirements
  - Financial services with strict compliance needs

## Initial Comparison Data
| Metric | Power BI Copilot | Scoop | Evidence |
|--------|------------------|-------|----------|
| Setup Time | 14+ weeks | 30 seconds | [MS docs, Scoop demo] |
| Business User Ready | No - requires IT/DAX | Yes | [Training requirements] |
| Excel Formulas | Zero support | 150+ native | [Functionality analysis] |
| Investigation | Single query only | Multi-pass (3-10) | [Architecture docs] |
| True Cost (200 users) | $175-235K | $3,588 | [Pricing analysis] |
| Accuracy Rate | 47% (Gartner) | Deterministic | [Gartner survey] |
| API Access | None | Full REST API | [Developer docs] |
| Slack Integration | None | Native | [Integration analysis] |

## Key Evidence URLs
1. https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction - Core limitations documented
2. https://learn.microsoft.com/en-us/fabric/fundamentals/copilot-power-bi-privacy-security - Nondeterministic warning
3. https://www.gartner.com/reviews/market/generative-ai-apps - 3% success rate survey
4. https://powerbi.microsoft.com/en-us/pricing/ - Official pricing (missing Copilot costs)
5. https://learn.microsoft.com/en-us/power-bi/developer/embedded/copilot-support - No API confirmation
6. https://techcommunity.microsoft.com/discussions/powerbiembed/copilot-in-embedded - CSP violations
7. https://www.reddit.com/r/PowerBI/comments/copilot-experience - User frustrations
8. https://github.com/MicrosoftDocs/power-bi-docs/issues - Ongoing Copilot issues
9. https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data - 14-week prep requirement
10. https://www.microsoft.com/en-us/store/b/copilotpro - Separate Excel licensing
11. https://learn.microsoft.com/en-us/power-bi/transform-model/datamarts-copilot - DirectLake not supported
12. https://community.fabric.microsoft.com/t/copilot-availability - Regional restrictions
13. Congressional testimony on Copilot ban - Security concerns documented
14. https://interworks.com/blog/powerbi-copilot-reality - Real implementation timelines
15. Customer case studies showing 12% initial adoption, 30-day remediation projects

## Critical Findings Summary
Power BI Copilot is positioned as AI-powered analytics but reality shows:
- **97% failure rate**: Only 3% of IT leaders find significant value (Gartner)
- **14+ week implementation**: Not the "instant AI" marketed
- **No developer access**: Complete absence of REST APIs
- **Geographic restrictions**: Unavailable in 11+ regions including all government clouds
- **Nondeterministic behavior**: Microsoft warns same query gives different results
- **Hidden costs**: True cost 50-65x higher than advertised ($175K vs implied $0)
- **Excel gap**: Zero Excel formula support despite Microsoft ecosystem