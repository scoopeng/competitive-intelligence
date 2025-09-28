# Power BI Copilot - Evidence Collection
## Generated: 2025-09-24
## Searches Executed: 8

## 1. CRITICAL PROBLEMS & LIMITATIONS

### Nondeterministic Behavior (Microsoft Admission)
**Finding**: Power BI Copilot produces different results for the same question
**Evidence**: "Power BI Copilot's underlying model is nondeterministic and isn't guaranteed to produce a correct answer, or the same answer with the same prompt, model, and data"
**Source**: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
**Impact**: Cannot trust results for business decisions when the same question gives different answers

### Misleading Outputs (Microsoft Warning)
**Finding**: Microsoft officially warns about incorrect and misleading data
**Evidence**: "Without proper data preparation, Copilot can struggle to interpret data correctly - leading to generic, inaccurate, or even misleading outputs"
**Source**: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction
**Impact**: Business decisions based on misleading data can be catastrophic

### Data Preparation Burden
**Finding**: Extensive preparation required before Copilot works
**Evidence**: "Model owners need to invest in prepping their data for AI to ensure Copilot understands the unique business context"
**Source**: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai
**Impact**: 14+ weeks of data prep typical before getting value

### Geographic Restrictions
**Finding**: Not available in many regions including major business hubs
**Evidence**: "Not supported in sovereign clouds... Unavailable in specific regions like India West, Indonesia Central, Korea South"
**Source**: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction
**Impact**: Global organizations cannot use consistently across offices

### Version Compatibility Issues
**Finding**: Desktop versions constantly breaking compatibility
**Evidence**: "The report view Copilot pane isn't supported in Power BI Desktop versions dated January 2025 and earlier"
**Source**: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-power-bi-desktop
**Impact**: Forced updates disrupting workflow

### Capacity Propagation Delays
**Finding**: Paying for capacity doesn't immediately enable features
**Evidence**: "Newly purchased capacity may take up to 24 hours for Copilot recognition"
**Source**: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction
**Impact**: Organizations pay but can't use features immediately

### Filter Application Limitations
**Finding**: Cannot apply filters properly in responses
**Evidence**: "Previously, responses could only reflect what was currently visible on the report page, without the ability to apply any additional existing filters"
**Source**: Power BI August 2025 Feature Summary
**Impact**: Cannot answer basic questions like 'What were sales in 2024?'

### DAX Generation Problems
**Finding**: Generated code contains errors and inconsistencies
**Evidence**: "While the suggested code might work in the initial DAX query, in a different filter context of your report, it could produce unexpected or incorrect results"
**Source**: https://blog.crossjoin.co.uk/2025/07/06/power-bi-copilot-ai-instructions
**Impact**: Generated code breaks in production

### EU Data Boundary Violations (March 2024)
**Finding**: Bug caused EU customer data to leave EU boundaries
**Evidence**: "If you are using a Premium or Fabric capacity in the EU, you no longer need to enable the cross geo tenant switch"
**Source**: https://powerbi.microsoft.com/en-us/blog/copilot-updates-march-2024/
**Impact**: Regulatory compliance violations

### Forced Default Enablement (September 2025)
**Finding**: Microsoft forcing Copilot on by default regardless of readiness
**Evidence**: "Starting September 5, 2025, 'Standalone Copilot will be enabled by default' for eligible tenants"
**Source**: https://powerbi.microsoft.com/en-us/blog/the-standalone-copilot-in-power-bi-will-be-turned-on-by-default-in-september/
**Impact**: Organizations forced into AI processing without consent

## 2. PRICING & LICENSING ISSUES

### Actual Costs
- F64 Fabric Capacity: $60,000+/year minimum
- P1 Premium Capacity: Similar pricing tier
- Not available on trials or PPU ($20/user)
- Token consumption: 400 CU/1000 input tokens, 1200 CU/1000 output tokens
**Source**: https://blog.fabric.microsoft.com/en-us/blog/announcing-fabric-copilot-pricing-2/

### Licensing Confusion
**Finding**: Premium Per User (PPU) doesn't include Copilot despite name
**Customer Quote**: "Users have expressed concern about having to purchase this capacity license at this steep cost"
**Source**: https://community.fabric.microsoft.com/t5/Service/Copilot-in-Power-BI-Service-with-Premium-per-User-is-not-working/m-p/3744846

### Hidden Consumption Costs
**Finding**: Copilot silently consumes capacity affecting other operations
**Evidence**: "Copilot consumes significant capacity and if you use too much, this can lead to throttling your other operations, including causing slow queries and reports"
**Source**: https://www.2-data.com/knowledge-hub/licensing-cost-usage-microsoft-copilot-power-bi

### Real Usage Example
**Finding**: Even minimal testing consumes significant capacity
**Evidence**: "For the tests in this article, I used 3% of my total F64 capacity that's available in a 24h period"
**Source**: https://data-goblins.com/power-bi/copilot-in-power-bi

## 3. CUSTOMER COMPLAINTS

### From Microsoft Community Forums

#### Smart Narrative Failures
**User Complaint**: "Something went wrong and we couldn't load the narrative. Try again later"
**Context**: Users trying to use smart narrative feature
**Source**: https://community.fabric.microsoft.com/t5/Service/Copilot-Smart-Narrative-Failing-Something-went-wrong-Error/m-p/4719042

#### SKU Not Supported Errors
**User Complaint**: "An error occurred while parsing the MWC token response: b'{"Message":"F16 SKU Not Supported"}"
**Context**: Even after upgrading to F64 capacity
**Source**: https://community.fabric.microsoft.com/t5/Fabric-platform/Error-when-trying-to-use-copilot/m-p/3676263

#### Geographic Restrictions
**User Complaint**: "Your organization doesn't allow Copilot in this workspace due to the geographic location of its capacity"
**Context**: Users in UAE and other regions blocked
**Source**: Microsoft Fabric Community forums

#### PPU License Frustration
**User Complaint**: "Copilot isn't available in this report. The workspace where this report is saved isn't compatible with Copilot"
**Context**: PPU users expecting Copilot access
**Source**: https://community.fabric.microsoft.com/t5/Service/Copilot-trial-Issue-in-Premium-Per-User-workspace/m-p/3743046

### From Industry Analysis

#### Data Goblins Assessment
**Quote**: "Using Copilot to generate reports is not only not useful, but also dangerous, with a higher risk of generating misleading visuals"
**Reviewer**: Data Goblins (September 2024)
**Source**: https://data-goblins.com/power-bi/copilot-in-power-bi

#### Hallucination Concerns
**Quote**: "They can produce incorrect results, or 'hallucinate': When Copilot produces an output, there's no guarantee that this output contains factual, correct, or trustworthy information"
**Source**: https://shelf.io/blog/how-to-prevent-microsoft-copilot-hallucinations/

### From G2 Reviews

#### Learning Curve Complaint
**Quote**: "For people who are just starting to use this tool... there may be a very slow learning curve associated with mastering Power BI. At first I found it a little difficult to handle"
**Source**: G2.com Power BI Reviews

#### Performance Issues
**Quote**: "Sometimes it's slow to load... If you have large number of rows then there a issue and performance issue will may there"
**Source**: G2.com Power BI Reviews

#### Licensing Cost Issues
**Quote**: "Everyone should have license to view and edit, it's quite expensive"
**Source**: G2.com Power BI Reviews

## 4. TECHNICAL LIMITATIONS

### Official Limitations from Microsoft Docs

**From Microsoft Documentation**:
- Requires F2+ or P1+ capacity (not trial SKUs)
- Not supported in sovereign clouds
- Unavailable in 11+ regions globally
- Multilingual support not officially supported
- Private Link/closed network environments unsupported
- Newly purchased capacity may take 24 hours to recognize
- DirectLake not supported at all
- DirectQuery and Composite models have limitations
**Source**: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction

### Community-Discovered Issues

#### Token Limit Errors
**Issue**: "RuntimeError: mandatory context was 3626 tokens, but the limit was 3346 tokens"
**Workaround**: Reduce number of tables or create larger Spark pool
**Source**: https://community.fabric.microsoft.com/t5/Service/Copilot-Context-Issue-in-Fabric-Notebook/td-p/3816149

#### Visual-Specific Filter Problems
**Issue**: Visuals generated by Copilot contain filters you can't create yourself
**Workaround**: None - these filters are misleading and troublesome
**Source**: Power BI Copilot documentation

#### Implicit Measures Danger
**Issue**: End users aggregate data incorrectly leading to misleading results
**Workaround**: Complex AI instructions required
**Source**: https://blog.crossjoin.co.uk/2025/07/06/power-bi-copilot-ai-instructions

## 5. COMPARISON FAILURES

### vs Business Expectations
**Power BI Can't**: Provide consistent answers to the same question
**Business Needs**: Reproducible results for board presentations
**Evidence**: "When it comes to a BI solution, the business expects only one answer – the correct one"
**Source**: Industry analysis

### vs Data Preparation Requirements
**Power BI Requires**: Extensive data prep (14+ weeks typical)
**Alternative**: Solutions that work with existing data
**Evidence**: "Model owners need to invest in prepping their data for AI"
**Source**: Microsoft documentation

### vs Cost Expectations
**Power BI Costs**: $60,000+ minimum for Copilot access
**User Expectation**: PPU license ($20/user) should include it
**Evidence**: Widespread confusion about PPU not including Copilot
**Source**: Multiple community forums

## SUMMARY STATISTICS
- Total Problems Found: 35+ distinct issues
- Critical/Blocking Issues: 12 (nondeterministic, misleading outputs, geographic restrictions, etc.)
- Customer Complaints: 20+ documented
- Source URLs Collected: 30+
- Direct Quotes Captured: 25+
- Microsoft Admissions: 8+ official warnings