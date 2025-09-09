# Domo - Competitive Analysis

**Company**: Domo  
**Category**: Tier 2 - Accessible AI (Dashboard-Centric)  
**Founded**: 2010  
**Key Insight**: Conversational AI layered on traditional dashboards  
**Completion**: 90% (updated with AI Chat analysis)

## Executive Summary

Domo has legitimate conversational AI capabilities through their AI Chat feature (launched 2024), allowing natural language queries with transparency features like SQL inspection. However, it remains fundamentally a dashboard-first platform where conversations happen within the context of existing visualizations. The platform requires significant data integration, dashboard creation, and ongoing maintenance before conversational features become useful.

## What They Say They Are
"AI-powered platform with conversational analytics that enables natural language conversations with data, delivering personalized insights through AI Chat"

## What They Actually Are
A dashboard platform with conversational AI that:
- Requires dashboards/apps to exist first
- Needs 1,000+ connector integrations
- Operates within dashboard context only
- Shows SQL steps (not true investigation)
- Requires extensive data prep
- Uses consumption-based pricing

## Product Capabilities

### Conversational AI - Real but Limited

**AI Chat (2024)**:
- Natural language queries about data
- Contextual to current dashboard/app
- Shows SQL generation steps
- Suggests follow-up questions
- Visual and narrative responses

**Mr. Roboto Suite**:
- Trend detection and correlations
- Outlier detection
- Market basket analysis
- Basic statistical features

### Key Product Limitations

**1. Dashboard-First Architecture**
- Must build dashboards BEFORE conversing
- AI Chat works within dashboard context
- Can't explore beyond pre-built views
- Business users depend on dashboard builders

**2. Integration Complexity**
- 1,000+ connectors to configure
- Extensive data modeling required
- Performance degrades with large datasets
- "Platform becomes disorganized" per users

**3. No Investigation Engine**
- Shows SQL steps, not reasoning
- Can't answer multi-step "why" questions
- No hypothesis testing
- Limited to dashboard-scoped data

**4. Technical Dependency**
- "Business users find it complicated"
- Requires data engineers
- 1-2+ month implementations
- Not true self-service

## Where Scoop Wins (Product Focus)

### 1. Investigation vs Conversation
- **Domo**: Chat within dashboard limits
- **Scoop**: Investigate across all data
- **Example**: "Why did sales drop?" 
  - Domo: Shows SQL for current dashboard
  - Scoop: Tests 5-10 hypotheses across sources

### 2. Zero Prerequisites
- **Domo**: Build dashboards first, then chat
- **Scoop**: Start asking questions immediately
- **Impact**: Months vs 30 seconds to insights

### 3. True Multi-Source Analysis
- **Domo**: 1,000 connectors to configure
- **Scoop**: Native multi-source without setup
- **Impact**: Integration project vs instant analysis

### 4. ML Capabilities
- **Domo**: Basic statistics (Mr. Roboto)
- **Scoop**: ML clustering, predictions, relationships
- **Impact**: Descriptive vs prescriptive analytics

### 5. Business User Experience
- **Domo**: "Complicated" per user reviews
- **Scoop**: Native Slack, zero training
- **Impact**: IT dependency vs self-service

## Technical Architecture Comparison

### Conversational Scope
| Aspect | Domo | Scoop |
|--------|------|--------|
| Query Scope | Current dashboard | All connected data |
| Context | Visual-first | Conversation-first |
| Investigation | Shows SQL steps | Multi-hypothesis testing |
| Depth | Single queries | 3-10 probe investigations |

### AI Capabilities
| Feature | Domo | Scoop |
|---------|------|--------|
| Natural Language | ✓ | ✓ |
| SQL Transparency | ✓ | ✓ |
| Investigation Engine | ✗ | ✓ |
| ML Analysis | Basic stats | Full ML suite |
| Pattern Discovery | ✗ | ✓ |
| Cross-source reasoning | ✗ | ✓ |

## Customer Decision Factors

### When They Choose Domo
- Heavy investment in dashboards already
- Want chat within visual context
- Have data engineering teams
- Prefer seeing SQL steps
- Dashboard culture dominant

### When They Choose Scoop
- Need insights before dashboards
- Want true investigation capabilities
- Business users need autonomy
- Multi-source analysis critical
- Speed to insight matters

## Real Implementation Reality

**User Reviews Confirm**:
> "To get the AI workflows to produce the output you need, there needs to be significant data modeling and preparation done beforehand"

> "As a small business it is clear we are not a target customer group"

> "Platform becomes very disorganized"

**Translation**: AI Chat doesn't eliminate complexity

## Sales Positioning

### Discovery Questions
1. "Do you want to chat with dashboards or investigate across all data?"
2. "How many dashboards exist before users can start?"
3. "Can your AI tell you WHY metrics changed?"
4. "Do business users build their own views?"
5. "How long before new users get value?"

### Objection Handling

**"Domo has conversational AI"**
- "Yes, for chatting with existing dashboards. But can it investigate WHY sales dropped by testing multiple hypotheses across all your data sources? That's the difference between conversation and investigation."

**"We like the SQL transparency"**
- "Transparency is great! Scoop shows reasoning steps too. But showing SQL isn't the same as reasoning. Can Domo break down complex questions into investigation plans?"

**"Domo has 1,000+ connectors"**
- "Having connectors and using them are different. How long does it take to integrate and model all that data? With Scoop, you're analyzing in 30 seconds, not configuring for months."

## Competitive Reality

**Domo AI Chat is good for**:
- Organizations with mature dashboards
- Users who think visually first
- Teams wanting SQL transparency
- Dashboard-centric workflows

**But fundamentally limited by**:
- Dashboard-first architecture
- No investigation capabilities
- Complex setup requirements
- Technical team dependency

**Scoop's Advantage**: We don't just converse with data - we investigate it. While Domo shows you the SQL for your dashboard, Scoop creates investigation plans, tests hypotheses, and discovers insights across all your data.

## Post-Setup Reality: Why Users Choose Scoop Daily

### When Both Domo and Scoop Are Connected

Even large enterprises with Domo already deployed choose Scoop for daily analytics because:

**Morning Routine Comparison**:
- **Domo**: Open portal → Navigate dashboards → Check each KPI → Screenshot for meeting
- **Scoop**: "run my morning deck" in Slack → Complete PowerPoint ready → Email to team

**Ad-Hoc Investigation**:
- **Domo AI Chat**: Limited to existing dashboard context and cards
- **Scoop**: Full investigation across ALL data, not just what's pre-built

**Business User Independence**:
- **Domo**: "Can you add this to a dashboard?" → Wait for BI team
- **Scoop**: Ask any question immediately → Get answer → Save for reuse

### Daily Feature Comparison

| What Users Need | Domo Reality | Scoop Reality |
|-----------------|--------------|---------------|
| Quick morning check | Navigate multiple dashboards | "run morning deck" |
| Why did X happen? | Limited to dashboard data | Full investigation engine |
| Share insights | Screenshot dashboard | Export PowerPoint/Excel |
| New analysis | Request dashboard changes | Ask naturally |
| Work location | Domo portal | Native Slack |
| Save analysis | Create new cards/dashboards | "save as [name]" |
| Bulk reporting | Manual dashboard tour | Single deck execution |

### Real User Feedback on Daily Use

**From a Domo customer who added Scoop**:
"We spent $400K on Domo and have beautiful dashboards. But when the CEO asks 'why?' in a meeting, I open Scoop in Slack because Domo can't investigate - it just shows what we already built."

**Why enterprises keep both**:
- Domo: Executive dashboards (pretty but static)
- Scoop: Daily investigation and analysis (dynamic and intelligent)

### The Investigation Gap

**Scenario**: "Revenue dropped 15% last week - why?"

**Domo Process**:
1. Check revenue dashboard (see the drop)
2. Check customer dashboard (looks normal)
3. Check product dashboard (also normal)
4. Ask BI team to investigate
5. Wait 2-3 days for new dashboard
6. Still just seeing symptoms, not causes

**Scoop Process**:
1. Ask the question in Slack
2. Scoop investigates automatically:
   - Tests day-of-week patterns
   - Analyzes customer segments
   - Checks product mix shifts
   - Identifies geographic changes
   - Correlates with marketing events
   - Finds root cause: "New customer cohort has 40% lower AOV"
3. Total time: 45 seconds

## Bottom Line for Positioning

Domo has added legitimate conversational AI, but it's constrained by their dashboard-first architecture. It's like having a brilliant assistant who can only discuss what's on the PowerPoint slides in front of them. Scoop is the analyst who can investigate your entire business, test theories, and explain what's really happening - not just chat about pre-built views.

**Post-Setup Truth**: Even when enterprises have invested heavily in Domo, business users choose Scoop daily because dashboards show what happened, but Scoop explains why it happened and what to do about it.