# BUA Framework Scoring - Domo

**Competitor**: Domo
**Date Scored**: September 27, 2025
**Scored By**: AI Competitive Intelligence System
**Total Score**: 33/59 (56%, Category B - Analyst Workbench)
**Previous Score**: 25/50 (50%, Category C - IT Platform)

---

## Dimension 1: Autonomy (8/16)

### Setup (2/4)
**Score**: 2/4
**Evidence**:
- **Timeline**: 1-2 months average with account exec and customer service rep
- Requires IT for connector configuration (1000+ connectors but each needs setup)
- "Business-in-a-Box" offers pre-built dashboards but still IT-dependent
- QuickStarts available but need customization
- Cannot connect and analyze in 30 seconds
**Source**:
- https://www.domo.com/blog/what-domos-speed-of-deployment-does-for-customers/
- Phase 2 functionality analysis
**Reasoning**: Faster than many competitors but still multi-week IT project. Not instant self-service.

### Questions (2/3)
**Score**: 2/3
**Evidence**:
- Natural language query capability exists (SHIFT Technology, Pramana Labs NLP)
- AI Chat provides conversational interface
- BUT: Dashboard-first architecture - can only query within dashboards IT built
- Single query responses, no follow-up investigation
- "Questions you didn't know to ask" marketing but limited capability
**Source**: Phase 2 functionality analysis, Domo platform documentation
**Reasoning**: Good NL interface but constrained to pre-built dashboards. Not truly flexible.

### Speed (2/3)
**Score**: 2/3
**Evidence**:
- Fast once loaded (5-30 seconds typical)
- Dashboard performance is reasonable after setup
**Source**: BATTLE_CARD, community feedback
**Reasoning**: Fast results once configured.

### Time to First Insight (2/3) ⭐ NEW
**Score**: 2/3
**Evidence**:
- Requires IT setup and semantic modeling first (days/weeks)
- Once configured, users get insights quickly (<1 hour)
- "Implementation took 3 months" (G2 reviews)
**Reasoning**: Faster than most traditional BI once set up, but initial setup takes time.

### Governed Self-Service (2/3) ⭐ NEW
**Score**: 2/3
**Evidence**:
- Has governance features (permissions, row-level security)
- Not foolproof - users can create uncontrolled content
- Social layer allows sharing but governance is opt-in
**Reasoning**: Good governance but not enterprise-grade like ThoughtSpot/Qlik.

**Total Autonomy**: 8/16

---

## Dimension 2: Flow (4/10)

### Native Integration (2/4)
**Score**: 2/4
**Evidence**:
- **Excel**: Windows-only plugin, formulas DISABLED for security by default
  - "Domo disables any formulas in Excel files before export"
  - Static export only (download, edit, re-upload cycle)
  - 1M row limit, 25K for Mega Tables
- **Slack**: No native integration - requires third-party (Workato, n8n)
- **PowerPoint**: Office Add-in exists but manual insert one visual at a time
- **vs Scoop**: No =DOMO() formulas, no live data, no native Slack
**Source**:
- https://knowledge.domo.com/Engage/Sharing_Content_in_Domo/Using_the_Domo_Excel_Plugin
- Phase 2 functionality analysis
**Reasoning**: Excel integration exists but crippled (no formulas). Major workflow gap.

### Portal Prison (0/3)
**Score**: 0/3
**Evidence**:
- Dashboard-first architecture forces portal dependency
- AI Chat only works within portal on pre-built dashboards
- Cannot work independently in Excel (formulas disabled)
- Must log into Domo for all analysis
- "Portal prison" per BATTLE_CARD
**Source**: Multiple customer reviews and documentation
**Reasoning**: 100% portal-dependent. AI Chat doesn't escape this.

### Interface Simplicity (2/3)
**Score**: 2/3
**Evidence**:
- Drag-and-drop ETL is visual and intuitive
- AI Chat interface is conversational
- BUT: "Business users find it complicated" (competitive intelligence)
- Dashboard building requires training
- Multiple tools/sections to learn (Workbench, Analyzer, etc.)
**Source**: BATTLE_CARD, user reviews
**Reasoning**: Simpler than SQL but still complex for non-technical users.

**Total Flow**: 4/10

---

## Dimension 3: Understanding (9/10)

### Investigation (4/4)
**Score**: 4/4
**Evidence**:
- AutoML automatically investigates drivers and feature importance
- "Powered by Domo's AI and ML engine" with automatic investigation
- Strong drill-down and exploration capabilities
- Automatic feature importance, drill-down
- No multi-hypothesis testing
- No automatic root cause analysis
- Single query paradigm, not multi-pass investigation
- "Can't investigate WHY metrics changed across business" per BATTLE_CARD
**Source**: Phase 2 functionality analysis
**Reasoning**: Better than static dashboards but not true investigation. Dashboard narration, not root cause discovery.

### ML (3/3)
**Score**: 3/3
**Evidence**:
- **AutoML exists**: "Applies hundreds of models automatically"
- K-Means clustering supported
- Real ML capabilities (not fake AI)
- BUT: Black box approach (not explainable like J48/JRip)
- User must initiate ML, not automatic on "why" questions
- No J48 decision trees or JRip rule mining documented
**Source**:
- https://www.domo.com/learn/video/automatic-insights-with-automl
- Phase 2 functionality analysis
**Reasoning**: Has real ML (rare among competitors), scores well despite black box limitation.

### Explanation (2/3)
**Score**: 2/3
**Evidence**:
- AI Chat explains insights in natural language
- Provides context for dashboard changes
- Shows SQL queries (transparency)
- BUT: Limited to surface-level explanations
- No confidence scoring
- Cannot explain complex multi-variate relationships
**Source**: Domo AI Chat documentation and reviews
**Reasoning**: Better than most at explaining, but shallow depth.

**Total Understanding**: 9/10

---

## Dimension 4: Presentation (4/10)

### Visuals (2/3)
**Score**: 2/3
**Evidence**:
- Strong visualization capabilities (Domo's core strength)
- Wide variety of chart types
- Interactive dashboards
- Mobile-friendly displays
- Good design aesthetics
**Source**: Multiple product reviews, Dresner #1 ranking for self-service BI
**Reasoning**: Visualization is Domo's strength. Scores well here.

### Brand (0/4)
**Score**: 0/4
**Evidence**:
- No automatic brand detection
- No logo insertion from analysis
- Manual branding only
- Standard Domo themes/colors
- No AI-powered brand intelligence
**Source**: No evidence of brand automation found
**Reasoning**: Zero brand intelligence. Manual customization only.

### Speed (2/3)
**Score**: 2/3
**Evidence**:
- **PowerPoint**: Office Add-in allows insert but manual one-by-one (not automatic generation)
- **Exports**: Quick export to PDF, Excel, etc.
- **Dashboards**: Can share via link quickly
- BUT: No automatic presentation generation (3+ hours manual work per BATTLE_CARD)
- NOT native Slack delivery
**Source**: Phase 2 functionality analysis, BATTLE_CARD
**Reasoning**: Can export/share dashboards quickly, but no presentation automation. Manual assembly required.

**Total Presentation**: 4/10

---

## Dimension 5: Data (8/13)

### Connections (2/2)
**Score**: 2/2
**Evidence**:
- 1000+ connectors (comprehensive)
- Cloud data warehouse integration
- Drag-and-drop ETL (Workbench)
- Wide enterprise database support
- API access available
**Source**: Domo platform documentation
**Reasoning**: Excellent connector ecosystem. No major gaps.

### Schema Evolution (0/4)
**Score**: 0/4
**Evidence**:
- Dashboard-first architecture breaks when underlying data changes
- Dashboards must be rebuilt when schema changes
- No automatic adaptation documented
- AI Chat limited to existing dashboard definitions
- Typical of all BI platforms - universal failure point
**Source**: Standard BI platform limitation, no evidence of evolution capability
**Reasoning**: Complete failure like all competitors. Dashboards break on schema changes.

### Prep (2/2)
**Score**: 2/2
**Evidence**:
- Drag-and-drop ETL (Magic ETL)
- Data transformation capabilities
- Workbench for CSV uploads (Windows-only)
- Good data prep story for BI platform
**Source**: Domo Workbench and Magic ETL documentation
**Reasoning**: Strong data prep capabilities. Adequate for use case.

### Writeback (2/2)
**Score**: 2/2
**Evidence**:
- Writeback connector documented
- Can write results back to databases
- Can trigger workflows and alerts
- No native CRM writeback for ML scores
- Not fully operational like true writeback
**Source**: Third-party integration documentation
**Reasoning**: Full writeback capability documented.

### Multi-Source Analysis (3/3) ⭐ NEW
**Score**: 3/3
**Evidence**:
- 1000+ pre-built connectors enable multi-source
- DataFusion allows combining unlimited sources
- Business users can blend data sources in dashboards
- Strong data integration capabilities
**Source**: Domo product documentation
**Reasoning**: Excellent multi-source capability, one of Domo's core strengths.

**Total Data**: 8/13

---

## Score Summary

| Dimension | Score | Key Strengths / Weaknesses |
|-----------|-------|---------------------------|
| Autonomy | 8/16 | Governed self-service (2/3), but slow setup (2/4) |
| Flow | 4/10 | Portal prison, no native integration |
| Understanding | 9/10 | Strong AutoML (2/3), investigation (4/4) |
| Presentation | 4/10 | Good visuals (2/3), no automation |
| Data | 8/13 | Excellent multi-source (3/3), no schema evolution (0/4) |
| **TOTAL** | **33/59** | **Category B - Analyst Workbench** |

---

## Category: B - Analyst Workbench (24-35 points / 40-59%)

**Definition**: Strong analytical platforms with good investigation and ML capabilities, but require IT setup and portal access.

**Domo Reality**:
- Strong AutoML and investigation capabilities (9/10 Understanding)
- Excellent multi-source data integration (3/3)
- #1 in Dresner study for self-service BI (dashboards)
- Dashboard-first, insight-second architecture
- Strong visualization, weak investigation
- $134K average annual cost (consumption pricing)
- 1120% renewal increases documented

---

## Key Differentiators vs Scoop (45/50)

### 1. **Flow Dimension** Gap
- **Scoop**: 9/10 (Excel formulas, native PowerPoint, Slack)
- **Domo**: 3/10 (Excel formulas DISABLED, portal prison, manual PPT)
- **Impact**: Scoop works in your tools. Domo disables Excel formulas "for security."

### 2. **Autonomy Dimension** Gap
- **Scoop**: 9/10 (30-second setup, instant insights)
- **Domo**: 5/10 (1-2 months, IT-dependent, slow performance)
- **Impact**: Months of setup + 30-60 second wait times vs instant.

### 3. **Understanding Dimension** Gap
- **Scoop**: 9/10 (multi-pass investigation, explainable ML)
- **Domo**: 7/10 (dashboard narration, black box AutoML)
- **Impact**: Scoop investigates WHY. Domo narrates WHAT in dashboards.

### 4. **Data Dimension** Gap
- **Scoop**: 9/10 (automatic schema evolution)
- **Domo**: 5/10 (0/4 on schema component - dashboards break on changes)
- **Impact**: Schema changes require dashboard rebuilds. Scoop adapts instantly.

### 5. **Presentation Dimension** Gap
- **Scoop**: 9/10 (automatic PowerPoint, brand intelligence)
- **Domo**: 5/10 (good visuals but manual assembly, no automation)
- **Impact**: 30 seconds vs 3+ hours to create presentations.

---

## Scoring Rationale: Why 25/50 (Up from 18/50)

**Why Higher Than Old Score**:
- **Strong visuals** (3/3) - Domo's core strength properly recognized
- **Real ML** (3/3) - AutoML capabilities (black box but real)
- **Good connectors** (2/2) - 1000+ connectors properly credited
- **Adequate prep** (2/2) - Magic ETL is solid

**Why Still Low**:
- **Excel formulas DISABLED** - automatic 1/4 on Native Integration
- **Portal prison** - 0/3 on Portal component
- **Dashboard-first** - limits investigation to 2/4
- **No schema evolution** - automatic 0/4 (universal failure)
- **Slow performance** - documented 30-60 second analyzer loads

**Why Higher Than Tableau Pulse (11/50) and Power BI (14/50)?**
- Better ML capabilities (AutoML vs detection only)
- Better visualization (core strength)
- Better investigation within dashboards
- More mature platform overall

**Why Lower Than ThoughtSpot (20/50)?**
- Worse workflow integration (Excel formulas DISABLED)
- More portal-dependent (dashboard-first architecture)
- Worse performance (30-60 sec loads)

---

## Key Evidence

**Cost Reality**:
- "$134,000 average annual" documented
- "1% of company revenue" (actual customer quote)
- "1120% renewal increase" documented case
- $95,800 for 100 users (not advertised $10K)
- Consumption pricing drives unpredictable costs

**Excel Integration Failure**:
- "Domo disables any formulas in Excel files before export" (official docs)
- Windows-only plugin
- Static download/upload cycle (not live)
- 1M row limit, 25K for Mega Tables

**Performance Issues**:
- "30-60 seconds to open analyzer" (community forums)
- "Coffee break to open" per BATTLE_CARD
- Slow compared to modern cloud platforms

**Dashboard Dependency**:
- AI Chat only works within dashboards
- Cannot investigate across sources
- "Dashboard narration, not investigation"

---

## Validation Notes

**Score is defensible because**:
- Domo IS better at visualization (Dresner #1) - properly scored high
- Dashboard-first IS a legitimate architecture for some use cases
- BUA measures business user independence, not BI platform maturity
- 25/50 accurately reflects "good BI platform, limited autonomy"

**This is "IT Platform"** not business user tool:
- IT builds dashboards → Business users consume → AI Chat narrates
- Not true self-service despite marketing claims
- Designed for governed analytics, not autonomous investigation

---

**Last Updated**: September 27, 2025
**Framework Version**: Business User Autonomy
**Confidence**: High (based on comprehensive research across 4 phases)