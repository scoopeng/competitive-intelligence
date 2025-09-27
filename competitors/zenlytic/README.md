# Zenlytic - Competitive Intelligence

## Quick Summary
**Category**: IT Platform (BUA Score: 44/100, 44%, Category C - Weak)  
**Fatal Flaw**: YAML configuration nightmare  
**Key Fact**: Requires SQL/YAML/Git knowledge  
**Reality Check**: Built for developers, not business users  

## The Scoop Advantage
- **Setup**: Natural language vs YAML configuration
- **Users**: Business teams vs technical teams
- **Time to value**: 30 seconds vs weeks of config
- **Schema changes**: Automatic vs YAML updates
- **Skills needed**: None vs SQL/YAML/Git

## Files in This Folder

### Sales Tools
- **[BATTLE_CARD.md](BATTLE_CARD.md)** - Quick reference with YAML complexity

### Research Sources
- **[sources/](sources/)** - 3 research documents:
  - YAML complexity examples
  - Research analysis
  - Source documentation

## Key Differentiators

### 1. The YAML Hell (Fatal Flaw)
**Reality of "self-service"**:
```yaml
# What business users must write:
models:
  - name: revenue_metrics
    sql: |
      SELECT 
        date_trunc('month', order_date) as month,
        SUM(amount) as revenue
      FROM orders
    dimensions:
      - name: month
        type: time
    measures:
      - name: revenue
        type: sum
        sql: amount
```
**Ask yourself**: Can your marketing manager write this?

### 2. The Technical Barrier
| Requirement | Zenlytic | Scoop |
|-------------|----------|-------|
| YAML knowledge | Required | None |
| SQL expertise | Required | None |
| Git for changes | Required | None |
| Semantic layer | Weeks to build | Automatic |
| Developer dependency | Always | Never |

### 3. Configuration Timeline
**Before first insight**:
1. Week 1-2: Design semantic model
2. Week 3-4: Write YAML configurations
3. Week 5-6: Test and debug
4. Week 7-8: Train users on constraints
5. Ongoing: YAML updates for any change

**vs Scoop**: 30 seconds to first insight

### 4. The Schema Change Nightmare
**When you add a column**:
- Update YAML definitions
- Test configurations
- Deploy changes
- Notify users
- Debug breaks

**Scoop**: Automatically adapts

## Discovery Questions
1. "Who on your team knows YAML?"
2. "Can your business users write SQL?"
3. "Who maintains configuration when schema changes?"
4. "How long before business users get value?"
5. "What happens when you need a new metric?"

## Objection Handlers

**"Zenlytic has natural language"**
→ "After weeks of YAML configuration. Your business users can't configure it, only use what developers set up. That's not self-service."

**"It's powerful once configured"**
→ "Weeks of YAML configuration, then locked into that structure. Every change needs more YAML. Business users are always dependent on developers."

**"We have technical resources"**
→ "Then you're buying a tool for developers, not business users. Scoop empowers everyone immediately, no YAML required."

## The YAML Reality Check
**Show them actual YAML requirements**:
- Semantic model definitions
- Metric configurations
- Dimension mappings
- Join definitions
- Access controls

**Ask**: "Which business users will maintain this?"

## Why YAML Fails for Business
1. **Learning curve**: Steeper than SQL
2. **Syntax errors**: One space breaks everything
3. **Version control**: Git required
4. **Testing burden**: Each change needs validation
5. **Documentation**: Constant updates needed

## Competitive Landmines
- Don't mock YAML (some love it)
- Focus on business user impact
- Show time-to-value difference
- Emphasize ongoing maintenance

## The Business User Test
**Demo scenario**:
1. "Marketing wants to analyze campaign ROI"
2. "Show me how they'd do it in Zenlytic"
3. Watch them realize YAML is required
4. "Now watch Scoop" → Natural language

## Real Configuration Example
**What Zenlytic requires for a simple metric**:
```yaml
measures:
  - name: customer_ltv
    type: number
    sql: |
      SUM(order_amount) / 
      COUNT(DISTINCT customer_id)
    format: currency
    description: Lifetime value per customer
    drill_fields: [customer_id, order_date]
```

**What Scoop requires**:
"What's the customer lifetime value?"

## The Maintenance Trap
- Every schema change = YAML updates
- Every new metric = YAML writing
- Every user request = Developer time
- Every bug = YAML debugging
- Result: IT bottleneck returns

## The Closing Line
"Zenlytic requires your business users to write YAML configurations and SQL. After weeks of setup, they're still dependent on developers for any change. Scoop works instantly with natural language. Do you want to train everyone on YAML or get answers now?"

---

*Intelligence current as of: January 2025*  
*YAML requirement = developer tool, not business tool*  
*Show actual YAML to make the point*