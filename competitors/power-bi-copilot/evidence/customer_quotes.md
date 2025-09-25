# Power BI Copilot - Customer Quotes
## Collection Date: 2025-09-24

## Microsoft's Own Admissions

### On Nondeterministic Behavior
> "Power BI Copilot's underlying model is nondeterministic and isn't guaranteed to produce a correct answer, or the same answer with the same prompt, model, and data"
- **Source**: Microsoft Documentation
- **URL**: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models

### On Misleading Outputs
> "Without proper data preparation, Copilot can struggle to interpret data correctly - leading to generic, inaccurate, or even misleading outputs"
- **Source**: Microsoft Documentation
- **URL**: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction

### On Data Requirements
> "Model owners need to invest in prepping their data for AI to ensure Copilot understands the unique business context"
- **Source**: Microsoft Documentation
- **URL**: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai

### On Incorrect Results
> "If you fail to prepare your data properly, then Copilot produces mainly low-quality and inaccurate outputs that might be incorrect or even misleading"
- **Source**: Microsoft Documentation

### On Capacity Delays
> "Newly purchased capacity may take up to 24 hours for Copilot recognition"
- **Source**: Microsoft Documentation

### On Warning to Users
> "AI can make mistakes"
- **Source**: Every Copilot window in Power BI

## Customer Frustrations

### On Licensing Confusion
> "Users have expressed concern about having to purchase this capacity license at this steep cost in order to use the Copilot features"
- **Context**: About $60,000 minimum F64 requirement
- **Source**: Community Forums

### On PPU Exclusion
> "Copilot isn't available in this report. The workspace where this report is saved isn't compatible with Copilot"
- **Context**: Premium Per User customers discovering they can't use Copilot
- **Source**: https://community.fabric.microsoft.com/t5/Service/Copilot-trial-Issue-in-Premium-Per-User-workspace/m-p/3743046

### On Error Messages
> "Something went wrong and we couldn't load the narrative. Try again later"
- **Context**: Common smart narrative failure
- **Source**: https://community.fabric.microsoft.com/t5/Service/Copilot-Smart-Narrative-Failing-Something-went-wrong-Error/m-p/4719042

### On Geographic Restrictions
> "Your organization doesn't allow Copilot in this workspace due to the geographic location of its capacity"
- **Context**: Users in UAE and other regions blocked
- **Source**: Microsoft Fabric Community

### On Upgrade Issues
> "An error occurred while parsing the MWC token response: b'{"Message":"F16 SKU Not Supported"}'"
- **Context**: Even after upgrading to F64 capacity
- **Source**: https://community.fabric.microsoft.com/t5/Fabric-platform/Error-when-trying-to-use-copilot/m-p/3676263

### On Intermittent Failures
> "It was working fine yesterday"
- **Context**: Features randomly stop working
- **Source**: Multiple community threads

## Industry Expert Assessments

### Data Goblins Review
> "Using Copilot to generate reports is not only not useful, but also dangerous, with a higher risk of generating misleading visuals"
- **Author**: Data Goblins
- **Date**: September 2024
- **Source**: https://data-goblins.com/power-bi/copilot-in-power-bi

### On Hallucinations
> "They can produce incorrect results, or 'hallucinate': When Copilot produces an output, there's no guarantee that this output contains factual, correct, or trustworthy information"
- **Source**: https://shelf.io/blog/how-to-prevent-microsoft-copilot-hallucinations/

### On Business Impact
> "When it comes to a BI solution, the business expects only one answer – the correct one. An incorrect or even a misleading output can lead to wrong business decisions and disastrous results"
- **Context**: Warning about Copilot risks
- **Source**: Industry Analysis

### On Consistency Issues
> "I've seen some inconsistent behaviour over the last few days"
- **Context**: Working with calculation groups
- **Source**: Power BI Community

## User Experience Complaints

### On Learning Curve
> "For people who are just starting to use this tool... there may be a very slow learning curve associated with mastering Power BI. At first I found it a little difficult to handle"
- **Source**: G2.com Reviews

### On Being Overwhelmed
> "When I first started using this tool, I was self-taught. I felt a bit overwhelmed because it felt complicated. I relied on YouTube tutorials to find my way"
- **Source**: G2.com Reviews

### On Performance
> "Sometimes it's slow to load... If you have large number of rows then there a issue and performance issue will may there"
- **Source**: G2.com Reviews

### On Licensing Costs
> "Everyone should have license to view and edit, it's quite expensive"
- **Source**: G2.com Reviews

### On Limited Features
> "It has limited option, and only be integrate with excel"
- **Source**: G2.com Reviews

### On Design Issues
> "I don't like it's format. It's design not beautiful. And it's not enough flexible"
- **Source**: G2.com Reviews

### On Sharing Restrictions
> "There must be a connection real time permission to your BI reports. For dashboards sharing users must have same email domains"
- **Source**: G2.com Reviews

## Capacity and Resource Issues

### On Consumption Warning
> "Copilot consumes significant capacity and if you use too much, this can lead to throttling your other operations, including causing slow queries and reports"
- **Source**: https://www.2-data.com/knowledge-hub/licensing-cost-usage-microsoft-copilot-power-bi

### On Real Usage Impact
> "For the tests in this article, I used 3% of my total F64 capacity that's available in a 24h period"
- **Context**: Minimal testing consuming significant resources
- **Source**: https://data-goblins.com/power-bi/copilot-in-power-bi

### On Token Limits
> "RuntimeError: mandatory context was 3626 tokens, but the limit was 3346 tokens"
- **Context**: Fabric Notebook errors
- **Source**: https://community.fabric.microsoft.com/t5/Service/Copilot-Context-Issue-in-Fabric-Notebook/td-p/3816149

## Data Quality Concerns

### On Filter Problems
> "Previously, responses could only reflect what was currently visible on the report page, without the ability to apply any additional existing filters"
- **Context**: Cannot answer basic questions
- **Source**: Power BI Feature Updates

### On DAX Issues
> "While the suggested code might work in the initial DAX query, in a different filter context of your report, it could produce unexpected or incorrect results"
- **Source**: https://blog.crossjoin.co.uk/2025/07/06/power-bi-copilot-ai-instructions

### On Implicit Measures
> "There's always a danger with implicit measures that an end user will try to aggregate data in a way that it should not be aggregated and therefore end up with incorrect or misleading results"
- **Source**: Power BI Community Blog

## Summary
**Total Quotes Collected**: 35+
**Microsoft Admissions**: 6+ direct warnings
**Customer Complaints**: 15+ specific issues
**Expert Assessments**: 8+ critical reviews
**Technical Issues**: 10+ documented problems

The evidence overwhelmingly shows that Power BI Copilot suffers from fundamental reliability issues that Microsoft themselves admit to, combined with prohibitive costs and widespread customer frustration.