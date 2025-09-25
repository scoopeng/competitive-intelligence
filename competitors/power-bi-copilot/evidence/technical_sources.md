# Power BI Copilot - Technical Sources & Evidence

**Last Updated**: September 24, 2025
**Research Method**: WebSearch and WebFetch

## Architecture & Infrastructure Sources

### GPU Requirements and Regional Availability
- **Microsoft Learn - Copilot Introduction**: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction
  - Confirms GPU dependency and sovereign cloud limitations
- **Microsoft Learn - Copilot Requirements Q&A**: https://learn.microsoft.com/en-us/answers/questions/2127068/copilot-requirements-for-power-bi
  - Details F64/P1 minimum requirements
- **Power BI September 2025 Feature Summary**: https://powerbi.microsoft.com/en-us/blog/power-bi-september-2025-feature-summary/
  - Lists unsupported regions including India, Indonesia, Korea, Qatar, UAE

### Capacity Requirements
- **Microsoft Learn - Enable Fabric Copilot**: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-enable-power-bi
  - States F64 or P1 minimum for Copilot
- **GigXP Fabric Licensing Guide 2025**: https://www.gigxp.com/fabric-licensing-guide/
  - Confirms PPU does not support Copilot
- **Microsoft Fabric Community - F64 vs P1**: https://community.fabric.microsoft.com/t5/Fabric-platform/Fabric-F64-capacity-vs-Power-BI-Premium-P1-capacity/m-p/3708411
  - Comparison of F64 and P1 capabilities

## Data & Integration Sources

### DirectLake and Composite Model Limitations
- **Power BI May 2025 Feature Summary**: https://powerbi.microsoft.com/en-us/blog/power-bi-may-2025-feature-summary/
  - "DirectLake is not yet supported" for Copilot
- **Microsoft Learn - Direct Lake Overview**: https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview
  - Technical limitations of Direct Lake mode
- **SQLBI - Direct Lake Analysis May 2025**: https://www.sqlbi.com/blog/marco/2025/05/13/direct-lake-vs-import-vs-direct-lakeimport-fabric-semantic-models-may-2025/
  - Performance comparison and limitations

### Data Preparation Requirements
- **Microsoft Learn - Prepare Data for AI**: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai
  - Extensive requirements for model preparation
- **Microsoft Learn - Optimize Semantic Model**: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-evaluate-data
  - Model optimization requirements
- **Bismart Blog - AI-Ready Semantic Model**: https://blog.bismart.com/en/ai-ready-semantic-model-copilot-power-bi
  - Industry perspective on preparation effort

## Performance & Reliability Sources

### Throttling and Performance Issues
- **CrossJoin Blog - Query Timeout**: https://blog.crossjoin.co.uk/2025/02/02/limit-the-impact-of-expensive-power-bi-queries-on-your-capacity-by-reducing-the-query-timeout/
  - Query timeout and capacity issues
- **CrossJoin Blog - Finding Throttled Queries**: https://blog.crossjoin.co.uk/2025/09/21/finding-power-bi-queries-and-refreshes-that-have-been-throttled-with-workspace-monitoring/
  - Evidence of throttling issues
- **Fynd Academy - Power BI Disadvantages 2025**: https://www.fynd.academy/blog/disadvantages-of-power-bi
  - Performance limitations with large datasets

### Accuracy and Non-Deterministic Results
- **Data Goblins - Myths and Magic**: https://data-goblins.com/power-bi/copilot-in-power-bi
  - Analysis of non-deterministic behavior
- **Holistics - AI BI Tools Comparison 2025**: https://www.holistics.io/bi-tools/ai-powered/
  - Comparative accuracy analysis

## Pricing Sources

### Official Microsoft Pricing
- **Microsoft Power Platform Pricing**: https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing
  - Official pricing page
- **Power BI Blog - Important Pricing Update**: https://powerbi.microsoft.com/en-us/blog/important-update-to-microsoft-power-bi-pricing/
  - April 2025 price increase announcement
- **Power BI Blog - Premium Licensing Update**: https://powerbi.microsoft.com/en-us/blog/important-update-coming-to-power-bi-premium-licensing/
  - P-SKU retirement announcement

### Fabric Capacity Pricing
- **Microsoft Azure - Fabric Pricing**: https://azure.microsoft.com/en-us/pricing/details/microsoft-fabric/
  - Fabric capacity pricing details
- **Synapx - Fabric Pricing Guide 2025**: https://www.synapx.com/microsoft-fabric-pricing-guide-2025/
  - F64 costs breakdown
- **That Fabric Guy - Costs Explained**: https://thatfabricguy.com/microsoft-fabric-costs-explained/
  - Hidden costs analysis

### Hidden Costs and Billing Issues
- **Reporting Hub Blog - Hidden Costs**: https://blog.thereportinghub.com/the-hidden-costs-of-power-bi-embedded-licensing-scaling-and-optimization/
  - Analysis of unexpected charges
- **Webdashboard - Price Increases**: https://webdashboard.com/power-bi-price-increases/
  - Customer impact analysis
- **The Register - 40% Price Hike**: https://www.theregister.com/2025/04/02/microsoft_power_bi_hikes/
  - Industry reaction to price increases

## Competitor Pricing Sources

### Scoop Analytics
- **Scoop Analytics Pricing Page**: https://www.scoopanalytics.com/pricing
  - Official pricing information
- **Software Advice - Scoop Review 2025**: https://www.softwareadvice.com/product/522641-Scoop-Analytics/
  - Independent pricing verification

## Capacity Monitoring Sources

### CU Consumption and Metrics
- **Microsoft Learn - Fabric Capacity Metrics App**: https://learn.microsoft.com/en-us/fabric/enterprise/metrics-app
  - Official monitoring documentation
- **Webdashboard - CU Performance Issues**: https://webdashboard.com/capacity-units-cu-and-performance-issues-explained/
  - CU consumption analysis
- **GigXP - Power BI Embedded SKU Estimation**: https://www.gigxp.com/power-bi-embedded-sku-estimation/
  - Capacity planning guide

## Customer Feedback Sources

### Price Shock and Complaints
- **CIO Magazine - Buyer Impact Analysis**: https://www.cio.com/article/3845524/microsoft-is-set-to-hike-its-power-bi-prices-will-buyers-jump-ship-or-just-take-the-hit.html
  - Analyst perspective on customer reaction
- **ERP Today - License Price Raises**: https://erp.today/microsoft-to-raise-prices-of-power-bi-licenses-in-2025/
  - Industry news coverage
- **Bismart - Price Increase Impact**: https://blog.bismart.com/en/power-bi-price-increase-2025
  - Customer guidance on managing increases

## Technical Documentation

### Integration and API
- **Microsoft Learn - Power BI REST APIs**: https://learn.microsoft.com/en-us/rest/api/power-bi/
  - API limitations and throttling
- **Microsoft Learn - Copilot Integration**: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-integration
  - Integration architecture details

All sources verified and accessible as of September 24, 2025.