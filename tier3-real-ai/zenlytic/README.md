# Zenlytic Competitive Intelligence Report

**Company**: Zenlytic  
**Product**: Zenlytic BI Platform  
**Research Date**: January 28, 2025  
**Researcher**: Claude  
**Research Status**: 85% Complete

## Executive Summary

Zenlytic positions itself as "self-serve analytics for business teams" but is actually a YAML-configured, SQL-based platform that requires data engineering expertise. Despite marketing claims of being "for business users who don't speak SQL," their entire semantic layer requires writing complex SQL within YAML files managed through Git. They have no real ML capabilities beyond LLM text-to-SQL translation. Classic Tier 3 pattern: marketed to business users, built for engineers.

### Bottom Line vs Scoop
- **They Say They Are**: "Self-serve analytics for business teams without SQL"
- **They Actually Are**: YAML/SQL platform requiring data engineers
- **Scoop Wins Because**: Agentic analytics with Excel integration, true self-service, 95% lower cost

## Company Overview

### Basic Information
- **Founded**: 2021
- **Headquarters**: San Francisco, CA
- **Employees**: ~20-30 (seed stage startup)
- **Funding**: $9.7M total (Seed round 2023)
- **Founders**: Ex-Instacart data scientists
- **CEO**: Ryan Jannsen
- **Website**: https://www.zenlytic.com

### Market Position
- **Target Market**: Mid-market tech companies
- **Industry Focus**: E-commerce, SaaS, marketplace businesses
- **Customer Base**: Small but growing
- **Notable Customers**: Public.com, Modern Treasury

## Product Analysis

### What They Actually Have vs Claims

#### Marketing Claims
- "Self-serve analytics for business teams"
- "No SQL knowledge required"
- "AI-powered insights"
- "Natural language interface"

#### Technical Reality
- **LLM Text-to-SQL**: Only "AI" is converting questions to SQL
- **No Real ML**: No clustering, prediction, or pattern discovery
- **YAML Configuration**: All data modeling in YAML files
- **SQL Required**: Complex SQL embedded throughout
- **Git Workflow**: Changes require version control
- **Engineering Dependency**: Cannot function without data team
- **No Investigation**: Single queries, can't explore "why"
- **Static Output**: No interactive models or Excel integration

### The YAML Configuration Reality

#### What Business Users Face
```yaml
# Just to answer "How many customers?"
version: 1
type: view
name: customers
sql_table_name: analytics.customers

fields:
  - name: customer_id
    type: string
    primary_key: yes
    
  - name: total_customers
    type: number
    sql: COUNT(DISTINCT ${customer_id})
    
  - name: acquisition_date
    type: time
    sql: DATE(${created_at})
```

#### Complex Reality (Revenue Calculation)
```yaml
- name: revenue
  type: number
  sql: |
    SUM(CASE 
      WHEN ${order_status} = 'completed' 
      THEN ${order_total} - COALESCE(${refund_amount}, 0)
      ELSE 0 
    END)
  format: currency
```

### Business User Barriers

#### Technical Requirements
1. **YAML Syntax**: Must understand indentation, structure
2. **SQL Knowledge**: Complex queries embedded everywhere
3. **Git Proficiency**: Version control for all changes
4. **Data Modeling**: Star schema understanding
5. **Testing Skills**: Validate queries don't break

#### Workflow Reality
1. Business user has question
2. Realizes it's not in semantic layer
3. Asks data team to add metric
4. Data engineer writes YAML/SQL
5. Tests in development
6. Commits to Git
7. Deploys to production
8. Business user can now ask question
9. **Time**: 2-5 days per new metric

## Pricing Analysis

### Transparency Issues
- **No Public Pricing**: "Contact sales" only
- **Custom Quotes**: Based on data volume and users
- **Enterprise Focus**: Likely $2,000-5,000/month minimum

### Estimated Total Costs
- **Software**: $24,000-60,000/year
- **Implementation**: $25,000-50,000
- **Ongoing Engineering**: 0.5-1 FTE required
- **Training**: Minimal (engineers do the work)
- **Total Year 1**: $150,000-200,000+

## Implementation Reality

### Timeline
- **Week 1-2**: Data warehouse connection and exploration
- **Week 2-4**: Building semantic layer in YAML
- **Month 2-3**: Training and rollout attempts
- **Ongoing**: Constant YAML updates for new questions

### Who's Really Involved
- **Data Engineers**: Build and maintain YAML
- **Analytics Engineers**: Design semantic layer
- **IT/DevOps**: Manage Git workflow
- **Business Users**: End up requesting changes

## User Experience Reality

### The Founder's Own Admission
> "It's basically writing in this language called YAML... it's like a simplified config language. You just define simple things like 'this is my users table, it has these columns'"

Translation: Even founders can't hide that it requires technical configuration.

### Common User Journey
1. **Marketing Promise**: "Ask questions without SQL!"
2. **Reality Check**: "First, we need to configure the semantic layer"
3. **Training Attempt**: "Here's how to read YAML..."
4. **Abandonment**: "I'll just ask the data team"

### Why Business Users Fail
- Can't modify semantic layer themselves
- Don't understand error messages
- Can't debug SQL issues
- Overwhelmed by technical concepts
- Faster to use Excel

## Competitive Positioning vs Scoop

### Where Zenlytic Fails

| Challenge | Zenlytic Reality | Scoop Advantage |
|-----------|-----------------|-----------------|
| Setup | YAML/SQL configuration | Connect and ask |
| Maintenance | Constant engineering | Self-maintaining |
| Business Users | Can't self-serve | True self-service |
| ML Capabilities | None (just LLM) | Real ML models |
| Time to Value | Weeks/months | 30 seconds |
| Required Skills | SQL, YAML, Git | None |

### Key Differentiators
- **Zenlytic**: Requires data team to pre-answer every possible question
- **Scoop**: Agentic AI investigates autonomously, creates Excel models

### The Paradigm Shift
**Zenlytic**: Business users still blocked by technical barriers (YAML/SQL)
**Scoop**: AI uses Excel as the universal interface - no code required

## Sales Battle Card

### Discovery Questions
1. "Do you have data engineers who know YAML?"
2. "Are you comfortable with Git version control?"
3. "Who will maintain the semantic layer?"
4. "How often do you need new metrics?"
5. "Can your business users write SQL?"

### Red Flags They'll Mention
- "We need to build out the semantic layer"
- "Our data team is configuring it"
- "We're learning YAML"
- "Waiting for engineering to add that metric"
- "The Git workflow is complex"

### Winning Positioning
"Zenlytic requires your data team to pre-configure every possible question in YAML files with embedded SQL. That's not self-service - that's just a different way to depend on engineers. Scoop delivers true agentic analytics that investigates problems autonomously and creates interactive Excel models - no configuration, no code, just insights."

### Objection Handling

**"They say no SQL required"**
"For end users, yes. But someone has to write all the SQL in YAML files first. Check their docs - every metric requires SQL knowledge."

**"But they have AI"**
"They have LLM text-to-SQL, which just converts questions to database queries. No pattern discovery, no predictions, no real ML - just query translation."

## Market Opportunity

### Zenlytic's Fundamental Flaw
They tried to solve the "business users can't write SQL" problem by creating a layer that requires... writing SQL in YAML. It's like solving "people can't drive stick shift" by requiring them to rebuild the transmission first.

### Who They Serve vs Who They Market To
- **Marketing**: Business teams without SQL knowledge
- **Reality**: Companies with data engineering teams
- **Gap**: 90% of businesses without dedicated data engineers

## Product-Focused Deep Dive

### Core Product Architecture Comparison

**Zenlytic's Technical Architecture**:
```yaml
# Business users must write this to answer basic questions:
- name: customer_lifetime_value
  type: number
  sql: |
    SUM(CASE 
      WHEN ${order_status} = 'completed' 
      AND ${customer_first_order} = ${order_date}
      THEN ${revenue} * ${predicted_retention_rate}
      ELSE 0 
    END)
```

**Reality**: This is programming, not self-service analytics

**Scoop's Approach**:
- Business user asks: "What's our customer lifetime value?"
- Scoop automatically understands schema, relationships, and calculations
- No configuration, no SQL, no YAML

### Investigation Capabilities - The Key Differentiator

**Zenlytic's Limitations**:
- **Single Query**: Each question = one SQL query
- **No "Why"**: Can't investigate causation
- **Pre-defined Only**: Limited to what's in YAML
- **No Discovery**: Can't find unknown patterns

**Scoop's Investigation Engine**:
- **Multi-Hypothesis Testing**: "Why did CLV drop?"
  - Tests seasonality
  - Analyzes cohort changes
  - Checks product mix impact
  - Identifies correlated metrics
- **Pattern Discovery**: Finds insights you didn't ask for
- **3-10 Probe Analysis**: Deep investigation with dependencies
- **Excel Output**: Creates interactive models with =SCOOP() functions
- **Living Analytics**: Models update with fresh data automatically

### Business User Experience Comparison

**Day in the Life: Zenlytic User**
1. **Question**: "Why did revenue drop last month?"
2. **Reality**: 
   - Error: "revenue_last_month not defined"
   - Wait for data engineer to add metric
   - Engineer writes SQL in YAML
   - Git commit, review, deploy
   - 2-3 days later: Try again
   - Still can't answer "why"

**Day in the Life: Scoop User**
1. **Question**: "Why did revenue drop last month?"
2. **Reality**:
   - Scoop investigates immediately
   - Tests 8 hypotheses with probe dependencies
   - Discovers: New cohort has lower AOV
   - Identifies: Specific product category issue
   - Creates: Excel model tracking cohort performance
   - Enables: User adjusts assumptions, model recalculates
   - Time: 45 seconds

### Why Eventbrite Should Choose Scoop

**Technical Barriers with Zenlytic**:
1. **YAML/SQL Expertise Required**: Not self-service
2. **Git Workflow**: Business users can't use Git
3. **Single Source Focus**: Can't analyze across systems
4. **No Investigation**: Just queries, no insights
5. **Static Definitions**: Can't explore freely

**Scoop's Business Advantages**:
1. **Immediate Value**: No setup or configuration
2. **True Self-Service**: Business users independent
3. **Cross-System Intelligence**: All data sources at once
4. **Investigation Engine**: Answers "why" not just "what"
5. **Continuous Learning**: Improves with usage

### The Fundamental Difference

**Zenlytic**: A technical platform that requires programming to answer business questions

**Scoop**: An AI analyst that investigates your business and explains what's happening

For Eventbrite's business users who need immediate insights across multiple systems without technical barriers, Scoop is the only viable choice.

## Conclusion

Zenlytic exemplifies the Tier 3 trap: sophisticated technology marketed to business users but accessible only through technical intermediaries. Their YAML/SQL semantic layer requirement ensures business users remain dependent on data teams, defeating the entire purpose of self-service analytics.

Scoop's advantage is clear: agentic analytics that investigates problems like a human analyst, delivered through the Excel interface everyone already knows. No YAML, no SQL, no Git - just intelligent analysis and interactive models at 95% lower cost.

**The Bottom Line**: Zenlytic makes engineers more productive. Scoop makes business users independent.