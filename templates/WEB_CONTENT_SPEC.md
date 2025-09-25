# Web Content Specification for Competitive Pages

**Purpose**: Define structure and content requirements for competitor comparison web pages
**Integration**: Designed for webflow API automation
**Last Updated**: January 2025

---

## Content Architecture

### Page URL Structure
```
/compare/scoop-vs-{competitor}/
/why-scoop/switch-from-{competitor}/
/alternative-to-{competitor}/
```

### Meta Requirements
```yaml
title: "Scoop vs {Competitor}: Why Business Users Choose Scoop"
description: "Compare Scoop Analytics to {Competitor}. See why businesses save 457x on costs while getting deeper insights in 30 seconds vs 3 weeks."
keywords:
  - "{competitor} alternative"
  - "scoop vs {competitor}"
  - "{competitor} comparison"
  - "better than {competitor}"
og_image: "/images/comparisons/scoop-vs-{competitor}-og.png"
```

---

## Page Sections Template

### 1. Hero Section
```markdown
# The Clear Choice for Business User Liberation

## Scoop vs {Competitor}: {Primary Differentiator}

**Hero Statement**: While {Competitor} {their_limitation}, Scoop {our_advantage}.

[CTA: See Scoop in Action] [CTA: Book a Demo]

**Trust Indicators**:
- ✅ 30-second setup vs {their_time}
- ✅ ${our_price}/month vs ${their_price}/month
- ✅ {our_capability} vs {their_limitation}
```

### 2. Problem Agitation Section
```markdown
## The Hidden Truth About {Competitor}

### What They Don't Tell You:
- **{Pain Point 1}**: {Evidence with source link}
- **{Pain Point 2}**: {Customer quote or statistic}
- **{Pain Point 3}**: {Technical limitation}

### Real Customer Experience:
> "{Negative customer quote about competitor}"
> - {Customer Title}, {Industry}

[Source: {Review Site} - Verified Purchase]
```

### 3. Comparison Table Section
```markdown
## Head-to-Head Comparison

| Capability | Scoop | {Competitor} |
|------------|-------|--------------|
| **Business User Independence** | ✅ No IT required | ❌ {Their limitation} |
| **Time to First Insight** | 30 seconds | {Their time} |
| **Annual Cost (200 users)** | $3,588 | ${Their cost} |
| **Investigation Depth** | 3-10 query analysis | {Their capability} |
| **Excel Integration** | Native formulas | {Their approach} |
| **ML/AI Capabilities** | Explainable ML | {Their ML} |
| **Setup Requirements** | Email only | {Their requirements} |
| **Schema Flexibility** | Auto-evolution | {Their approach} |

[See Full Feature Comparison →]
```

### 4. Key Differentiators Section
```markdown
## Why Businesses Choose Scoop Over {Competitor}

### 1. {Primary Differentiator Title}
**The Problem with {Competitor}**: {Their limitation explained}
**The Scoop Advantage**: {Our solution explained}
**Business Impact**: {ROI or time saved}

### 2. {Secondary Differentiator Title}
**The Problem with {Competitor}**: {Their limitation explained}
**The Scoop Advantage**: {Our solution explained}
**Business Impact**: {ROI or time saved}

### 3. {Tertiary Differentiator Title}
**The Problem with {Competitor}**: {Their limitation explained}
**The Scoop Advantage**: {Our solution explained}
**Business Impact**: {ROI or time saved}
```

### 5. Use Case Demonstrations
```markdown
## See the Difference in Action

### Scenario: "{Common Business Question}"

#### {Competitor} Approach:
1. {Step 1 - typically complex}
2. {Step 2 - requiring technical knowledge}
3. {Step 3 - time consuming}
**Time**: {Their time}
**Result**: {Limited outcome}

#### Scoop Approach:
1. Type question in Slack/Excel
2. Get complete analysis with recommendations
**Time**: 30 seconds
**Result**: {Superior outcome with actions}

[Watch 2-Minute Demo →]
```

### 6. Migration Section
```markdown
## Switching from {Competitor} is Simple

### What You Keep:
- ✅ All your data sources
- ✅ Your existing workflows
- ✅ Historical analyses

### What You Gain:
- ✅ 95% cost reduction
- ✅ True business user independence
- ✅ Investigation not just visualization
- ✅ Excel, PowerPoint, Slack native

### Migration Timeline:
- **Day 1**: Connect data sources (30 minutes)
- **Day 2**: Team onboarded and productive
- **Week 1**: First insights delivered
- **Month 1**: ROI achieved

[Get Migration Guide →]
```

### 7. Proof Section
```markdown
## Don't Take Our Word For It

### Customer Success Story:
> "We switched from {Competitor} to Scoop and saved $127,000 annually while actually getting MORE insights. The investigation capabilities are game-changing."
> - {Name}, {Title} at {Company}

### Verified Performance Metrics:
- **Setup Time**: 30 seconds (vs {competitor_time})
- **Time to Insight**: 30 seconds (vs {competitor_time})
- **User Adoption**: 94% (vs industry avg 22%)
- **Cost Savings**: {percentage}% reduction

[Read Case Studies →]
```

### 8. FAQ Section
```markdown
## Common Questions from {Competitor} Users

**Q: How hard is it to migrate from {Competitor}?**
A: {Migration ease answer with timeline}

**Q: What about our existing {Competitor} dashboards?**
A: {How we handle their assets}

**Q: Can Scoop handle our data volume?**
A: {Scale and performance answer}

**Q: What's the real total cost?**
A: {Transparent pricing explanation}
```

### 9. Bottom CTA Section
```markdown
## Ready to Liberate Your Business Users?

### See Scoop vs {Competitor} Live
Watch how Scoop delivers insights in 30 seconds while {Competitor} is still loading.

[Schedule Personal Demo] [Start Free Trial]

### Or Try It Right Now:
- 📧 Email: hello@scoopanalytics.com
- 💬 Slack: Join our workspace
- 📊 Excel: Download add-in

**No credit card. No IT required. No SQL needed.**
```

---

## Content Variables for Each Competitor

### Required Variables
```yaml
competitor_name: "Power BI Copilot"
competitor_slug: "power-bi-copilot"
primary_weakness: "Nondeterministic outputs"
primary_differentiator: "Reliable investigation vs random results"
their_price: "60,000"
their_setup_time: "3-4 months"
their_insight_time: "hours"
killer_question: "What does Microsoft mean by nondeterministic?"
customer_pain_quote: "Copilot gives different answers to the same question"
migration_ease: "1 day"
cost_savings_percent: "95"
```

### Optional Enhancements
```yaml
video_demo_url: "https://..."
case_study_pdf: "https://..."
migration_guide_url: "https://..."
g2_review_link: "https://..."
reddit_thread: "https://..."
```

---

## SEO Content Requirements

### Primary Keywords (use 3-5 times)
- `{competitor} alternative`
- `scoop vs {competitor}`
- `better than {competitor}`
- `{competitor} comparison`

### Secondary Keywords (use 1-2 times)
- `switch from {competitor}`
- `{competitor} replacement`
- `{competitor} vs scoop analytics`
- `{competitor} limitations`

### Long-tail Keywords (use naturally)
- `why scoop is better than {competitor}`
- `{competitor} pricing vs scoop`
- `migrate from {competitor} to scoop`
- `{competitor} problems and issues`

---

## Dynamic Content Components

### Competitor-Specific Modules

#### For Text-to-SQL Competitors (Snowflake, Zenlytic, DataGPT)
- Emphasis on WHY vs WHAT
- Multi-pass investigation examples
- Query complexity comparisons

#### For BI Platform Competitors (Power BI, Tableau, Domo)
- Portal prison vs workflow integration
- Dashboard limitations
- Time to create presentations

#### For Self-Service Competitors (ThoughtSpot, Sisense, Qlik)
- True independence examples
- Hidden complexity reveal
- Adoption failure statistics

### Industry-Specific Variations
```yaml
retail:
  use_case: "Why are sales declining in Northeast stores?"
  metric_focus: "Customer behavior analysis"

saas:
  use_case: "What's driving churn in enterprise accounts?"
  metric_focus: "Subscription analytics"

financial:
  use_case: "Which products have margin compression?"
  metric_focus: "Profitability analysis"
```

---

## Visual Content Requirements

### Images Needed
1. **Hero Image**: Scoop vs {Competitor} split screen
2. **Comparison Chart**: Visual feature comparison
3. **Workflow Diagram**: Their process vs ours
4. **Time Savings Graphic**: Clock showing difference
5. **Cost Comparison**: Bar chart of pricing
6. **Customer Logos**: Who switched from them to us

### Video Content
1. **2-Minute Demo**: Core differentiator demonstration
2. **Customer Testimonial**: Switching success story
3. **Feature Comparison**: Side-by-side usage

---

## A/B Testing Variables

### Headlines to Test
- "The {Competitor} Alternative That Actually Works"
- "Why Companies Switch from {Competitor} to Scoop"
- "Scoop vs {Competitor}: {Percentage}% Cost Savings, 100x Faster"

### CTAs to Test
- "See Scoop Beat {Competitor}"
- "Get Better Than {Competitor}"
- "Switch from {Competitor} Today"

### Social Proof to Test
- Customer quotes
- Savings statistics
- Time comparisons
- Feature advantages

---

## Content Governance

### Update Frequency
- **Monthly**: Pricing verification
- **Quarterly**: Feature comparison updates
- **Annually**: Complete content refresh

### Approval Required For
- Customer quotes
- Specific pricing claims
- Performance comparisons
- Migration timelines

### Legal Considerations
- No false claims
- Source all statistics
- Verify customer permissions
- Respect trademarks

---

## Implementation Checklist

### Per Competitor Page
- [ ] All content variables defined
- [ ] 3+ customer pain points with evidence
- [ ] 5+ differentiators documented
- [ ] Comparison table complete
- [ ] Migration path clear
- [ ] Pricing accurate and current
- [ ] SEO keywords integrated
- [ ] Visual assets created
- [ ] Legal review completed
- [ ] A/B tests configured

---

*This spec enables consistent, effective competitor comparison pages that convert.*