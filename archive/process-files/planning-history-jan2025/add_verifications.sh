#!/bin/bash

# Add verification sections to remaining battle cards

# DOMO
cat >> battle-cards/DOMO_BATTLE_CARD.md << 'EOF'

## Verify This Yourself

### Portal Prison Architecture
1. Visit: https://www.g2.com/products/domo/reviews
2. Search: "dashboard-first" complaints
3. Reality: AI Chat only works within dashboards

### Average Enterprise Cost
1. Research: Domo customer case studies
2. Find: "$134K average annual cost"
3. Problem: Consumption pricing unpredictability

### Renewal Shock Stories
1. Search: "Domo renewal increase" online
2. Find: Customer complaints about pricing
3. Reality: Consumption model drives costs up

---

*Use when: Dashboard-heavy org, Cost concerns, Need investigation not views*
EOF

# THOUGHTSPOT
cat >> battle-cards/THOUGHTSPOT_BATTLE_CARD.md << 'EOF'

## Verify This Yourself

### Accuracy Issues
1. Review: Independent benchmarks
2. Find: "33.3% accuracy" in query tests
3. Reality: 2 out of 3 queries fail

### Enterprise Pricing
1. Contact: ThoughtSpot sales
2. Quote: "$140K+ annual" typical
3. Implementation: "2-3 months" standard

### Search Limitations
1. Test: Complex business questions
2. Result: Only works for simple metrics
3. Problem: Can't investigate causality

---

*Use when: Accuracy matters, Budget conscious, Need investigation*
EOF

# TELLIUS
cat >> battle-cards/TELLIUS_BATTLE_CARD.md << 'EOF'

## Verify This Yourself

### Data Science Requirements
1. Review: Tellius documentation
2. Find: "ML model configuration" required
3. Reality: Need data scientists to operate

### Black Box Predictions
1. Test: Ask for explanation of predictions
2. Result: Statistical outputs without context
3. Problem: Business users can't interpret

### Enterprise Cost
1. Quote: Tellius pricing
2. Reality: "$100K+" annual typical
3. Plus: Data science team costs

---

*Use when: Business users primary, Need explainable AI, Budget matters*
EOF

# DATAGPT
cat >> battle-cards/DATAGPT_BATTLE_CARD.md << 'EOF'

## Verify This Yourself

### Schema Rigidity
1. Test: Add new data column
2. Result: Requires complete reconfiguration
3. Problem: Can't handle evolving data

### Single Source Limitation
1. Review: DataGPT architecture
2. Find: "Single data source" only
3. Reality: No cross-source investigation

### Portal-Only Access
1. Check: Integration options
2. Find: Web portal only
3. Missing: Excel, PowerPoint, Slack

---

*Use when: Multi-source needs, Schema changes often, Tool integration matters*
EOF

# ZENLYTIC
cat >> battle-cards/ZENLYTIC_BATTLE_CARD.md << 'EOF'

## Verify This Yourself

### YAML Configuration Hell
1. Visit: https://docs.zenlytic.com
2. Find: "YAML configuration files" required
3. Reality: Git-based metric management

### Technical Users Only
1. Review: Setup requirements
2. Find: "SQL and YAML expertise" needed
3. Problem: Business users can't use it

### Weeks to Configure
1. Check: Implementation timeline
2. Reality: "Weeks to configure" metrics
3. Then: Ongoing YAML maintenance

---

*Use when: Business user focus, Quick implementation needed, Non-technical team*
EOF

# DATACHAT
cat >> battle-cards/DATACHAT_BATTLE_CARD.md << 'EOF'

## Verify This Yourself

### Legitimate Company (Not Vaporware)
1. Visit: https://www.businesswire.com/news/home/20250219735773/en/
2. Find: "$25M Series A funding"
3. Reality: Founded 2018, real product

### Limited Market Presence
1. Search: Customer reviews
2. Find: Very few public references
3. Question: Why so little adoption?

### Recognition but No Traction
1. Note: Gartner mention in 2024
2. But: No significant customer base
3. Reality: Technology without adoption

---

*Use when: Proven solutions needed, Customer references matter, Risk-averse*
EOF

echo "Verification sections added to all battle cards"