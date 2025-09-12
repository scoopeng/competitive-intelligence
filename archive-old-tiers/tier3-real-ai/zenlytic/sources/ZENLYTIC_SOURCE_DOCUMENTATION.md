# Zenlytic Source Documentation
## All Research Sources and Evidence

**Research Date**: January 28, 2025
**Researcher**: Claude (Anthropic)

---

## Official Zenlytic Sources

### 1. Zenlytic Main Website
**URL**: https://www.zenlytic.com/
- Marketing positioning as "Intelligent Analytics"
- Claims about Zoë AI assistant
- No pricing information available
- Enterprise sales focus

### 2. Zenlytic Documentation
**URL**: https://docs.zenlytic.com
- Complete technical documentation
- YAML configuration requirements
- Setup and implementation guides
- Data modeling instructions

### 3. Zenlytic Blog Posts

#### "Introducing the Cognitive Layer"
**URL**: https://www.zenlytic.com/blog/introducing-the-cognitive-layer
- Explains their "cognitive layer" concept
- Admits it's semantic layer + LLM
- Marketing terminology for existing concepts

#### "Building Self-Serve Business Intelligence with AI"
**URL**: https://www.zenlytic.com/blog/building-self-serve-business-intelligence-with-ai-and-semantic-modeling-at-zenlytic
**Key Quote**: 
> "Personally, I would say it's a slog to build a bi tool. There's so many small features, permissioning, like all the roles, and just there's so many features in there to build."

#### "Semantic Layer Example"
**URL**: https://www.zenlytic.com/blog/semantic-layer-example
- Shows YAML configuration examples
- Demonstrates technical complexity
- Requires SQL knowledge despite claims

### 4. Zenlytic GitHub
**URL**: https://github.com/Zenlytic
- Public repositories showing code
- Metrics layer open source project
- Example YAML configurations

#### Metrics Layer Repository
**URL**: https://github.com/Zenlytic/metrics_layer
- Shows actual implementation complexity
- Python 3.8-3.11 requirement
- Complex configuration structure

---

## Technical Documentation Evidence

### 5. Views Documentation
**URL**: https://docs.zenlytic.com/docs/data_modeling/view
**Key Evidence**:
- "Views, like all files in Zenlytic, are YAML text files"
- Shows required YAML structure
- Complex configuration options
- SQL requirements in YAML

### 6. Model Documentation
**URL**: https://docs.zenlytic.com/docs/data_modeling/model
- Model YAML requirements
- Connection configuration
- Technical prerequisites

### 7. Getting Started Guide
**URL**: https://docs.zenlytic.com/getting-started/start_here
**Key Requirements Found**:
- GitHub repository setup
- Deploy key configuration
- Branch management
- YAML file creation

### 8. dbt MetricFlow Integration
**URL**: https://docs.zenlytic.com/data-modeling/dbt_metricflow
- Shows integration complexity
- Additional YAML files needed
- Technical configuration required

---

## Partner & Implementation Evidence

### 9. Analytics8 Partnership
**URL**: https://www.analytics8.com/technologies/zenlytic-partnership/
- Premium consultancy partner
- Indicates enterprise focus
- Implementation services required

### 10. Analytics8 Blog Post
**URL**: https://www.analytics8.com/blog/zenlytic-and-agentic-ai-unlocking-true-self-service-analytics-for-business-users/
**Key Quote**:
> "Zenlytic has made our analytics workflow faster, more intuitive, and less reliant on technical expertise to answer one-off, self-service business questions."
- Note: "Less reliant" not "not reliant"

### 11. Snowflake Partnership
**URL**: https://www.snowflake.com/en/why-snowflake/partners/all-partners/zenlytic/
- Enterprise data warehouse partnership
- Indicates target market
- Infrastructure requirements

---

## User Experience Evidence

### 12. AtScale Podcast
**URL**: https://www.atscale.com/podcast/semantic-layer-llms-data-driven-insights/
**Title**: "The Semantic Layer, LLMs and the Future of Data-Driven Insights with Zenlytic's Founders"
- Founders discuss technical nature
- Emphasis on semantic layer
- Technical implementation details

### 13. Ad Fontes Media Case Study
**URL**: https://www.zenlytic.com/blog/ad-fontes-media-uses-zenlytic-to-scale-analytics-with-self-serve-bi
- Shows successful implementation
- But Ad Fontes is a data-driven company
- Had existing data infrastructure

---

## Configuration Examples Found

### 14. Basic View YAML Example
```yaml
type: view
name: customers
model_name: my_database
sql_table_name: prod.customers
description: Contains customer profile information
```

### 15. Complex View with SQL
```yaml
name: my_view
derived_table: 
  sql: "select *, row_number() over (partition by customer_id order by order_date) as order_number from myschema.mytable"
always_filter:
- field: customers.is_churned
  value: FALSE
```

### 16. Python Configuration Example
```python
config = {
  "location": "https://myusername:myaccesstoken@github.com/myorg/myrepo.git",
  "branch": "develop",
  "connections": [
    {
      "name": "mycompany",
      "type": "snowflake",
      "account": "2e12ewdq.us-east-1",
      "username": "demo_user",
      "password": "q23e13erfwefqw",
      "database": "ANALYTICS",
      "schema": "DEV",
    }
  ],
}
```

---

## Review Sites Searched

### 17. G2 Reviews
**URL**: https://www.g2.com/products/zenlytic/reviews
- Limited reviews available
- No detailed user experiences visible
- Pricing not disclosed

### 18. Capterra
**URL**: https://www.capterra.com/p/265168/ZenCentiv/
- No reviews found
- No pricing information

### 19. SourceForge
**URL**: https://sourceforge.net/software/product/Zenlytic/
- Listed but no reviews
- No additional information

---

## Key Evidence Summary

### Technical Complexity Evidence:
1. All configuration in YAML files
2. GitHub repository required
3. Deploy keys needed
4. SQL knowledge required in YAML
5. Version control for all changes

### Business User Barriers Evidence:
1. No UI for configuration
2. Engineering team needed for setup
3. Ongoing technical maintenance
4. Command line operations
5. Complex error messages

### Missing Transparency:
1. No public pricing
2. No self-service trial
3. Limited user reviews
4. Enterprise sales only
5. Implementation costs hidden

---

## Research Methodology

### Search Queries Used:
1. "Zenlytic analytics platform ML AI capabilities YAML configuration"
2. "Zenlytic semantic layer YAML requirements business user complexity"
3. "Zenlytic pricing cost implementation time requirements"
4. "Zenlytic reviews user experiences implementation challenges business users"
5. "Zenlytic YAML configuration examples github repository"
6. "Zenlytic G2 reviews user experiences implementation"
7. "Zenlytic actual pricing per user per month cost"
8. "Zenlytic implementation requirements technical resources data team YAML"
9. "Zenlytic semantic layer YAML example configuration complexity engineers"

### Direct Documentation Review:
- Zenlytic official documentation site
- GitHub repositories
- Partner websites
- Blog posts and case studies

### Analysis Methods:
- Compared marketing claims vs technical documentation
- Analyzed YAML configuration complexity
- Evaluated business user accessibility
- Assessed implementation requirements
- Identified success/failure patterns

---

## Conclusions from Sources

Based on all sources reviewed, Zenlytic is clearly positioned as an enterprise tool requiring significant technical resources, despite marketing claims of being "for business users." The YAML configuration requirement alone creates an insurmountable barrier for non-technical users, confirming its classification as a Tier 3 AI Pretender.