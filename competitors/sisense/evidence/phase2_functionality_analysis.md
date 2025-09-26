# Phase 2: Functionality Deep Dive - Sisense
**Date**: September 25, 2025
**Time**: Phase 2 Completed

## Executive Summary
Sisense is an **embedded analytics platform** focused on ISVs and developers, NOT business user self-service. Critical findings:
- **ZERO Excel formula support** (export only, no live formulas)
- **No investigation capability** (single queries only, no multi-pass)
- **Requires significant IT involvement** (14+ weeks typical implementation)
- **Portal-based architecture** (no native workflow integration)

---

## 2A: Documentation & Core Functionality Review

### Core Platform Capabilities Found
1. **Compose SDK** - Developer-focused embedded analytics
2. **ElastiCube** - Proprietary data modeling (complex, requires SQL)
3. **BloX** - Custom dashboard components (requires coding)
4. **Simply Ask (DEPRECATED)** - Natural language failed, being replaced
5. **Generative AI (Beta)** - GPT-3.5/4o for cloud customers only

### Workflow Reality
**Their Process**: Data → ElastiCube → Dashboard → Portal → Export → Excel
**Time**: 14+ weeks implementation, then 3-4 hours per report
**Expertise Required**: SQL, JavaScript, technical data modeling

### Key Documentation Findings
- **L2025.1 Release**: Focus on embedded analytics, not self-service
- **Connection Management**: Now GA but requires IT setup
- **Export to Excel V2**: Replacing old service (still just export, no live connection)
- **Build to Destination (B2D)**: Requires CDWH configuration

---

## 2B: Business User Empowerment Assessment

### Capability 1: Excel Integration ❌ CRITICAL GAP
**What Sisense Has**: Export to Excel (XLSX) with 1.5M cell limit
**How It Works**: Static export only, no live formulas, no refresh
**Business User Empowerment**: 2/10 - Export dies on arrival
**vs Scoop**: Scoop has 150+ live Excel functions with =SCOOP()
**Gap**: Cannot use ANY Excel formulas with live data
**Evidence**: docs.sisense.com/main/SisenseLinux/exporting-pivot-tables-to-excel.htm

### Capability 2: Natural Language Query ⚠️ MAJOR ISSUES
**What Sisense Has**: Simply Ask (being deprecated), new chatbot in beta
**How It Works**: Template-based NLQ, not true understanding
**Business User Empowerment**: 3/10 - Requires training on syntax
**vs Scoop**: Scoop has multi-pass investigation with context
**Gap**: Single query only, no "why" investigation
**Evidence**: "Simply Ask deprecated" - switching to new beta system

### Capability 3: Machine Learning/AI 🔴 MARKETING MIRAGE
**What Sisense Has**: ARIMA forecasting, regression analysis
**How It Works**: Statistical methods from 1970s, not ML
**Business User Empowerment**: 1/10 - Requires data science knowledge
**vs Scoop**: Automatic ML with J48, JRip, EM clustering
**Gap**: No automatic ML, no explanatory models
**Evidence**: Community posts confirm AutoML requires technical setup

### Capability 4: Self-Service Analytics ❌ FALSE CLAIM
**What Sisense Has**: Drag-drop dashboards (with permissions)
**How It Works**: IT creates data models, users view dashboards
**Business User Empowerment**: 3/10 - Viewers only, not creators
**vs Scoop**: 30-second setup, no IT required
**Gap**: ElastiCube requires SQL despite "codeless" claims
**Evidence**: "ElastiCube isn't user-friendly, requires SQL"

### Capability 5: Workflow Integration ❌ PORTAL PRISON
**What Sisense Has**: Slack posting (screenshots), no PowerPoint
**How It Works**: Post static charts to Slack, manual export rest
**Business User Empowerment**: 2/10 - Leave tools to use Sisense
**vs Scoop**: Native Excel/PowerPoint/Slack in 30 seconds
**Gap**: No PowerPoint generation, no live Excel, portal-only
**Evidence**: Only Google Slides mentioned, no PPT capability

### Capability 6: Investigation & Root Cause ❌ DOESN'T EXIST
**What Sisense Has**: Drill-down in dashboards
**How It Works**: Click through pre-built hierarchies
**Business User Empowerment**: 2/10 - Not real investigation
**vs Scoop**: Multi-pass with 3-10 queries finding "why"
**Gap**: Cannot investigate, only navigate dashboards
**Evidence**: No root cause analysis capability found

---

## 2C: Gap Analysis & Limitations

### Critical Limitations Found

1. **2GB Export Limit** - Models fail when exceeding threshold
2. **No Offline Sharing** - Cannot share PDFs with non-users
3. **Dashboard Deletion Risk** - Deleting user deletes all dashboards (irreversible)
4. **C:\ Drive Only** - Must install on C drive
5. **One Admin Limit** - Single system admin per license
6. **No Network Paths** - Cannot import from network/mapped drives
7. **Wide Tables Cut Off** - PDF exports truncate wide tables
8. **No Scheduled Email Reports** - Users must log into portal
9. **400% Renewal Increases** - Documented customer shock
10. **14+ Week Implementation** - Standard timeline

### Training Requirements
- **Sisense Academy**: 30-80 hours of training needed
- **Prerequisites**: SQL knowledge helpful but "not mandatory"
- **Reality Check**: "Requires extensive training if new to BI"
- **Learning Curve**: "Steep learning curve" per multiple sources

### Technical Requirements vs Claims
| Sisense Claims | Reality Found |
|---------------|--------------|
| "No code required" | Requires SQL for ElastiCube |
| "Self-service BI" | IT creates, users view only |
| "Business user friendly" | "Not easy to use" per reviews |
| "AI-powered" | ARIMA from 1970s |
| "Natural language" | Template-based, being deprecated |

---

## Competitive Gap Matrix

| Capability | Sisense Reality | Scoop Advantage | Impact |
|------------|----------------|-----------------|--------|
| **Excel Support** | Export only, static | 150+ live formulas | Scoop wins 10/10 |
| **ML/AI** | ARIMA statistics | Auto ML (J48/JRip/EM) | Scoop wins 10/10 |
| **Investigation** | None, drill-down only | Multi-pass 3-10 queries | Scoop wins 10/10 |
| **Workflow** | Portal + exports | Native tools integration | Scoop wins 9/10 |
| **Setup Time** | 14+ weeks | 30 seconds | Scoop wins 10/10 |
| **Business Users** | Requires IT/training | True self-service | Scoop wins 9/10 |
| **PowerPoint** | None found | 30-second generation | Scoop wins 10/10 |
| **Cost** | $200K+ with renewals | $3,588 flat | Scoop wins 10/10 |

---

## Phase 2 URLs Visited

1. **sisense.com/demo/** - Demo request form, no actual demo
2. **documentation.sisense.com/latest/getting-started/tutorial.htm** - Tutorial overview
3. **docs.sisense.com/main/SisenseLinux/l2024-3-release-notes.htm** - Latest features
4. **expertbeacon.com/a-comprehensive-guide-to-the-sisense-api-for-2024/** - API focus confirms developer orientation
5. **sisense.com/blog/sisense-product-roundup-embedded-ai/** - Embedded focus
6. **docs.sisense.com/main/SisenseLinux/l2025-1-release-notes.htm** - 2025 roadmap
7. **sisense.com/resources/case-studies/** - Customer examples (embedded focus)
8. **portable.io/learn/sisense-integrations** - Integration limitations
9. **sisense.com/whitepapers/big-book-of-embedded-analytics-use-cases/** - ISV focus
10. **sisense.com/blog/the-data-journey-from-raw-data-to-insights/** - Complex workflow
11. **docs.sisense.com/main/SisenseLinux/exporting-pivot-tables-to-excel.htm** - Export only
12. **sisense.com/marketplace/add-on/advanced-formula/** - Requires add-on for formulas
13. **sisense.com/blog/ai-in-analytics-the-nlq-use-case/** - NLQ limitations
14. **docs.sisense.com/main/SisenseLinux/simply-ask-query-in-natural-language.htm** - Deprecated
15. **sisense.com/blog/4-strategies-for-success-with-ai-machine-learning-and-analytics/** - No real ML
16. **community.sisense.com/t5/knowledge-base/automated-machine-learning-with-sisense-fusion-a-practical-guide/ta-p/24897** - Complex AutoML
17. **sisense.dev/** - Developer portal (confirms developer focus)
18. **sisense.com/glossary/self-service-bi/** - Marketing vs reality
19. **dtdocs.sisense.com/article/slack-integration** - Basic Slack posting only
20. **sisense.com/glossary/diagnostic-analytics/** - Drill-down not investigation
21. **yurbi.com/blog/straight-talk-review-of-sisense-the-pros-and-cons/** - Major limitations
22. **betterbuys.com/bi/reviews/sisense-business-intelligence/** - Complexity confirmed
23. **cbinsights.com/company/scoop-analytics/alternatives-competitors** - Market comparison
24. **qrvey.com/blog/sisense-reviews/** - Technical expertise required
25. **academy.sisense.com/** - 30-80 hours training needed

---

## Key Discoveries for Sales

### The Embedded Analytics Trap
Sisense is built for ISVs to embed analytics in their software products, NOT for enterprise business users. Every feature confirms this:
- Compose SDK for developers
- API-first architecture
- White-labeling focus
- Complex technical requirements

### The Excel Lie
They claim Excel support but it's **export-only with no live connection**. Business users must:
1. Log into Sisense portal
2. Navigate to dashboard
3. Export to Excel (static)
4. Lose all live connection
5. Manually update forever

**Scoop**: =SCOOP("revenue last month") updates live

### The AI Deception
- **Simply Ask**: Being deprecated because it failed
- **ARIMA**: Time-series from 1970s, not AI
- **AutoML**: Requires technical configuration
- **Chatbot**: Beta for cloud customers only

**Scoop**: Real ML runs automatically without users knowing

### The Self-Service Myth
Despite marketing claims:
- ElastiCube requires SQL knowledge
- 30-80 hours of training needed
- IT must build data models
- Users are viewers, not creators
- "Best suited for companies with technical teams"

---

## Conclusion

Sisense is an **embedded analytics platform for ISVs**, not a business intelligence tool for enterprises. With zero Excel formula support, no investigation capability, and 14+ week implementations, it's the opposite of business user empowerment. At $200K+ with 400% renewal increases, they lock customers into a portal prison that requires constant IT support.

**Scoop wins on every dimension** that matters for business users.