# Phase 2: Functionality Deep Dive - Domo vs Scoop
**Date**: September 25, 2025
**Purpose**: Map Domo capabilities against Scoop's core differentiators

## Scoop's Core Differentiators (Reference)
1. **Excel Formula Engine**: 150+ functions on live data
2. **Automatic ML Discovery**: J48, JRip, EM Clustering
3. **Multi-Pass Investigation**: 3-10 automatic queries
4. **Visual Intelligence**: AI-powered presentations
5. **30-Second Workflow Integration**: Excel, Slack, PowerPoint

## Research Library

### Search 1: Domo Platform Overview
**URL**: https://www.domo.com/platform
**Date**: September 25, 2025
**Summary**: Official platform capabilities including AI Chat, 1000+ connectors, drag-and-drop ETL
**Key Evidence**:
- AI Chat for "questions you didn't know to ask" (but single query only)
- AI Agents for automation (not investigation)
- Drag-and-drop ETL pipelines
- Cloud data warehouse integration
- No mention of multi-pass investigation or Excel formulas

### Search 2: Excel Integration Deep Dive
**URL**: https://knowledge.domo.com/Engage/Sharing_Content_in_Domo/Using_the_Domo_Excel_Plugin
**Date**: September 25, 2025
**Summary**: Excel plugin exists but major limitations
**Key Evidence**:
- **Windows-only plugin**: Only works on Windows, Office 2000+
- **No formula support**: "Domo disables any formulas in Excel files before export" for security
- **Static export**: Download dataset, edit, re-upload - not live
- **1M row limit**: Excel supports only 1 million rows when exporting
- **25K limit for Mega Tables**: Only exports 25K rows to Excel
- **Admin can enable formulas**: But "strongly recommended not to" due to security
- **vs Scoop**: No live formulas like =SCOOP(), no 150+ functions on live data

### Search 3: Natural Language & Investigation
**URL**: Multiple sources on Domo NLP
**Date**: September 25, 2025
**Summary**: Has NLP but no multi-pass investigation
**Key Evidence**:
- **SHIFT Technology**: Multiple datasets in single interface for search
- **Pramana Labs NLP**: Natural language queries of large databases
- **Single queries only**: No evidence of multi-hypothesis testing
- **No "why" capability**: Can't investigate root causes automatically
- **vs Scoop**: No 3-10 probe investigations, no hypothesis testing

### Search 4: Machine Learning Capabilities
**URL**: https://www.domo.com/learn/video/automatic-insights-with-automl
**Date**: September 25, 2025
**Summary**: Has AutoML but different from Scoop's approach
**Key Evidence**:
- **AutoML exists**: "Applies hundreds of models automatically"
- **Clustering supported**: K-Means mentioned
- **No J48/JRip**: No evidence of these specific algorithms
- **Black box approach**: Not explainable like Scoop's white-box ML
- **No automatic discovery**: User must initiate ML, not automatic on questions
- **vs Scoop**: No J48 decision trees, no JRip rules, no automatic ML on "why" questions

### Search 5: PowerPoint & Slack Integration
**URL**: https://www.domo.com/business-apps/add-ins
**Date**: September 25, 2025
**Summary**: Limited integration requiring multiple tools
**Key Evidence**:
- **Office Add-in exists**: Single add-in for Word, PPT, Excel, Outlook
- **Manual process**: Insert visuals one at a time, not automatic generation
- **No native Slack**: Requires third-party tools (Workato, n8n)
- **No automatic presentations**: Must manually build each time
- **vs Scoop**: No 30-second PowerPoint generation, no native Slack investigation

### Search 6: Implementation Timeline
**URL**: https://www.domo.com/blog/what-domos-speed-of-deployment-does-for-customers/
**Date**: September 25, 2025
**Summary**: 1-2 months typical, not 30 seconds
**Key Evidence**:
- **Gartner praise**: "Speed of deployment" as strength
- **1-2 months average**: With account exec and customer service rep
- **QuickStarts available**: Pre-built dashboards for common uses
- **Business-in-a-Box**: Role-based dashboards with "little technical assistance"
- **1000+ connectors**: But each needs configuration
- **vs Scoop**: Weeks/months vs 30 seconds, IT involvement vs self-service

### Search 7: Root Cause Analysis Capabilities
**URL**: General RCA research (no Domo-specific features found)
**Date**: September 25, 2025
**Summary**: No evidence of automated root cause analysis
**Key Evidence**:
- **No "5 Whys" automation**: Standard RCA requires manual process
- **No hypothesis testing**: No automatic hypothesis generation/testing
- **Single query limitation**: Can't follow investigative threads
- **vs Scoop**: No multi-pass investigation, no automatic "why" capability

## Capability Comparison Matrix

| Capability | Domo | Scoop | Winner | Evidence |
|------------|------|-------|--------|----------|
| **Excel Formula Support** | ❌ Disabled for security | ✅ 150+ functions live | Scoop | Domo explicitly disables formulas |
| **Live Excel Data** | ❌ Export/import only | ✅ =SCOOP() formulas | Scoop | Domo is download/upload cycle |
| **Multi-Pass Investigation** | ❌ Single queries | ✅ 3-10 automatic | Scoop | No evidence of multi-hypothesis |
| **Automatic ML** | ⚠️ AutoML exists | ✅ Automatic on "why" | Scoop | Domo requires manual ML initiation |
| **Explainable ML** | ❌ Black box | ✅ J48/JRip rules | Scoop | No white-box ML in Domo |
| **PowerPoint Generation** | ❌ Manual inserts | ✅ 30-second auto | Scoop | Domo requires manual building |
| **Native Slack** | ❌ Third-party only | ✅ Full platform | Scoop | Domo needs Workato/n8n |
| **Setup Time** | ❌ 1-2 months | ✅ 30 seconds | Scoop | Domo needs implementation team |
| **CSV Upload** | ❌ Workbench needed | ✅ Drag & drop | Scoop | Domo requires Windows tool |
| **Root Cause Analysis** | ❌ Not found | ✅ Automatic | Scoop | No RCA features found |

## Fatal Gaps vs Scoop

### 1. No Excel Formula Engine
- **Domo Reality**: Formulas disabled, export-only, Windows plugin required
- **Scoop Advantage**: 150+ Excel functions work on live data immediately
- **Business Impact**: Hours of manual work vs instant analysis

### 2. No Investigation Capability
- **Domo Reality**: Single SQL queries, no hypothesis testing, no "why"
- **Scoop Advantage**: 3-10 automatic probes finding root causes
- **Business Impact**: Surface symptoms vs deep insights

### 3. No Automatic ML Discovery
- **Domo Reality**: Manual AutoML initiation, black box results
- **Scoop Advantage**: J48/JRip automatically on questions, explainable rules
- **Business Impact**: Need data scientist vs automatic discovery

### 4. No Native Workflow Integration
- **Domo Reality**: Portal-centric, third-party tools for Slack, manual PowerPoint
- **Scoop Advantage**: Native in Excel/Slack/PowerPoint in 30 seconds
- **Business Impact**: Workflow disruption vs seamless integration

### 5. Complex Implementation
- **Domo Reality**: 1-2 months, Workbench installation, IT involvement
- **Scoop Advantage**: 30 seconds, drag & drop CSV, no IT needed
- **Business Impact**: Months to value vs immediate insights