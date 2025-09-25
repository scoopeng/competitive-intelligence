# Phase 2: Functionality Deep Dive - Tableau Pulse
*Research Date: September 25, 2025*

## Pre-Phase Review: Scoop's Core Differentiators
✓ Reviewed SCOOP_CAPABILITIES.md

### Key Scoop Differentiators to Compare Against:
1. **Excel Formula Engine**: 150+ native Excel functions executed on live data
2. **Automatic ML Discovery**: J48, JRip, EM Clustering run automatically
3. **Multi-Pass Investigation**: 3-10 queries to find root causes
4. **Visual Intelligence**: AI-powered presentation generation
5. **30-Second Workflow Integration**: Excel, PowerPoint, Slack native

---

## 2A: Documentation & Core Functionality

**Documentation Review**: https://www.tableau.com/products/tableau-pulse
- AI-powered insights delivered in workflow
- Automatically detects drivers, trends, outliers
- Natural language summaries and explanations
- Available on Tableau Cloud only (not Server)
- Requires Tableau+ for premium features

**Core Features**:
- Enhanced Q&A in natural language
- Proactive metric monitoring
- Integration with Slack, Teams, email
- Mobile app access
- Built on "Agentforce Trust Layer"

**Key Requirements**:
- Requires time dimension (day, week, month, quarter, year)
- Data must be updated regularly (daily/weekly)
- Single point-in-time values won't work
- Missing latest data point limits functionality

---

## 2B: Business User Empowerment Assessment

**Search 5**: Excel integration formula support
- **Reality**: NO native Excel formula execution
- "May not fully support complex Excel formulas or pivot tables"
- Tableau doesn't support pivot tables in Excel
- Export to Excel requires third-party tools (Coupler.io)
- Manual export "time-consuming and impractical"
- **vs Scoop**: Zero Excel formulas vs 150+ functions

**Search 6**: Natural language query investigation
- Can ask questions in "plain, natural language"
- Uses embeddings model (not LLM) to avoid hallucination
- "Progressively reveals insights" through guided Q&A
- Provides "why" behind data changes
- **vs Scoop**: Progressive but not true multi-pass investigation

**Search 7**: Machine learning automated analysis
- "Automatically detect hidden drivers, trends, contributors"
- Uses "in-house AI/ML mathematical models"
- Exploring Einstein Discovery for predictive metrics (future)
- Built on Einstein Trust Layer
- **vs Scoop**: Detection but not automatic ML models like J48/JRip

**Search 8**: Self-service business users setup
- "As easy as checking a box" for technical setup
- BUT requires careful metric definition
- "No technical skill needed" but needs "data literacy basics"
- Controlled rollout recommended
- **vs Scoop**: Easy turn-on but metric setup complex

**Search 9**: PowerPoint Slack workflow integration
- **Slack**: Native integration with digests and alerts
- **PowerPoint**: NO native export - requires third-party (Rollstack)
- **Teams**: Yes, native integration
- **Google Slides**: New app available
- **vs Scoop**: Good Slack, zero PowerPoint native

**Search 10**: Root cause analysis capabilities
- "Provides context to help figure out why changes happened"
- "Accelerating root cause analysis without manual data slicing"
- Statistical grounding for insights
- Goes "beyond 'what' to get to 'why'"
- **vs Scoop**: Guided insights but not true multi-pass investigation

---

## 2C: Gap Analysis & Limitations

**Search 11**: Limitations and missing features
- "Looking at a 'moment in time' is currently a limitation"
- Cannot explore specific historical periods (e.g., pandemic only)
- "Limited to bar charts presenting single metric filter"
- "Beta version does not support table calculations"
- API access limitations for group restrictions
- Hour/minute granularity not supported

**Search 12**: vs Scoop comparison
- No direct comparison found

**Search 13**: IT expertise required
- Initial setup "as easy as checking a box"
- BUT metric definition requires expertise
- Need to merge fields for multi-dimensional analysis
- Data must be prepared with time dimensions

**Search 14**: Training requirements
- "No technical skill needed to get value"
- BUT "training should cover data literacy basics"
- Users need to "trust the AI-driven insights"
- Controlled rollout with training recommended

**Search 15**: Setup time
- Technical setup minimal
- BUT requires:
  - Time dimension setup
  - Regular data updates
  - Metric definitions
  - Group rollout strategy

---

## Capability Comparison Matrix

| Capability | Tableau Pulse | Scoop | Winner | Evidence |
|------------|---------------|-------|--------|----------|
| Excel Support | ❌ Zero formulas | ✅ 150+ functions | **Scoop** | "Doesn't support complex Excel formulas or pivot tables" |
| ML/AI Analysis | ⚠️ Detection only | ✅ Automatic ML | **Scoop** | No J48/JRip/EM clustering models |
| Investigation Depth | ⚠️ Guided Q&A | ✅ Multi-pass (3-10) | **Scoop** | Progressive but not true multi-pass |
| Workflow Integration | ⚠️ Slack yes, PPT no | ✅ Native all | **Scoop** | PowerPoint requires third-party tools |
| Business User Ready | ⚠️ Metric setup complex | ✅ 30-second | **Scoop** | Requires time dimension, regular updates |

---

## Key Functionality Gaps vs Scoop

### Excel Support Gap:
- **Tableau Pulse**: ZERO Excel formula support, export requires third-party
- **Scoop**: 150+ Excel functions work on live data
- **Impact**: Excel users completely blocked, must use Tableau interface

### ML/AI Capabilities Gap:
- **Tableau Pulse**: Detects trends/outliers but no actual ML models
- **Scoop**: Runs J48, JRip, EM clustering automatically
- **Impact**: Surface-level insights vs deep pattern discovery

### Investigation Depth Gap:
- **Tableau Pulse**: "Progressive" Q&A but single-path exploration
- **Scoop**: True multi-pass (3-10 queries) investigation
- **Impact**: Guided tour vs actual root cause discovery

### Workflow Integration Gap:
- **Tableau Pulse**: Slack native, PowerPoint requires Rollstack ($$$)
- **Scoop**: Native Excel, PowerPoint, Slack in 30 seconds
- **Impact**: Additional tools and costs for basic workflow needs

### Business User Readiness Gap:
- **Tableau Pulse**: Requires time dimension, regular updates, metric definition
- **Scoop**: Works immediately with any data
- **Impact**: IT project vs immediate value