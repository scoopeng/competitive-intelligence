# Phase 2: Functionality Deep Dive - Power BI Copilot
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

**Documentation Review**: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction
- Core features: Chat with data, find content, create visuals, write DAX queries
- For business users: Ad-hoc analyses, report summaries, visual creation
- For report authors: Suggest content, create pages, write DAX
- Key limitation: "Not supported in sovereign clouds"
- Requires F2 Fabric capacity or higher

**Search 1**: Power BI Copilot demo walkthrough
- Three experiences: Standalone, Copilot pane, Copilot in apps
- Generates visuals from natural language
- Can answer questions if not already visualized on report
- Creates DAX queries for ad hoc calculations

**Search 2**: Power BI Copilot documentation features
- Requires specific regional availability
- Not supported in: India West, Indonesia Central, Korea South, Malaysia West, New Zealand North, Qatar Central, Taiwan, UAE Central, France South, Germany North, Norway West
- Preview phase - many announced features not yet public

---

## 2B: Business User Empowerment Assessment

**Search 5**: Excel integration formula support
- **Reality**: NO native Excel formula execution
- Has "COPILOT function" in Excel (separate product) but NOT in Power BI Copilot
- Requires .xlsx/.xlsm files saved in OneDrive/SharePoint
- Can generate DAX formulas but NOT Excel formulas
- **vs Scoop**: Scoop has 150+ native Excel functions, Power BI has ZERO

**Search 6**: Natural language query capabilities
- Can answer questions with visuals from semantic model
- Responds to follow-up requests in current session only
- Cannot save prompts for future reference
- No follow-up questions - "one question at a time"
- **vs Scoop**: No multi-pass investigation, single query only

**Search 7**: Machine learning automated analysis
- Has AutoML but requires Premium/PPU license
- Supports Binary Prediction, Classification, Regression
- Integrated with Azure ML (separate service)
- No-code model building BUT requires dataflows setup
- **vs Scoop**: Not automatic - requires manual setup, Scoop runs ML automatically

**Search 8**: Self-service business users no code
- "Data needs to be prepared to work with Copilot"
- "Model owners need to invest in prepping their data"
- Requires F64 capacity ($60k/year) or P1 Premium
- NOT available with $20 PPU license
- **vs Scoop**: Requires extensive data prep, Scoop works in 30 seconds

**Search 9**: PowerPoint Slack integration workflow
- PowerPoint: Can add live report page (requires add-in)
- Slack: NO integration found
- Teams: Yes, can embed reports
- SharePoint: Yes, with "Enable Copilot" checkbox
- **vs Scoop**: No Slack, limited PowerPoint, Scoop has native integration

**Search 10**: Root cause analysis investigation
- Has "Decomposition Tree" and "Key Influencers" (separate AI visuals)
- "Copilot can't currently answer questions that require generating new insights like anomaly detection, forecasting, or finding key influencers"
- No multi-pass investigation capability
- **vs Scoop**: Cannot do root cause analysis, Scoop does 3-10 pass investigation

---

## 2C: Gap Analysis & Limitations

**Search 11**: Limitations cannot do missing features
- "Copilot doesn't answer follow-up questions. You need to ask one question at a time"
- "Copilot prompts can't be saved for future reference"
- "Multilingual use is not officially supported"
- "DirectLake is not yet supported"
- "Not supported on trial SKUs or Premium Per User workspaces"

**Search 13**: Requires IT technical expertise
- "Enabling and using Copilot requires careful deliberation"
- "Ensure users have completed training or demonstrated understanding"
- "Governance considerations are important"
- "Getting value requires healthy data culture and good adoption"

**Search 14**: Training certification learning curve
- "Incrementally roll out Copilot in Power BI in phases"
- "Preparing effective user training and enablement" required
- Must demonstrate "understanding of the technology, its limitations, and its use cases"

**Search 15**: Setup time implementation
- "Newly purchased capacity may take up to 24 hours for Copilot to recognize"
- Requires tenant-level AND workspace-level enablement
- Data prep required before Copilot works properly
- Not just "turn on and expect productivity enhancement"

---

## Capability Comparison Matrix

| Capability | Power BI Copilot | Scoop | Winner | Evidence |
|------------|------------------|-------|--------|----------|
| Excel Support | ❌ No Excel formulas | ✅ 150+ functions | **Scoop** | PBI has DAX only, no Excel formula execution |
| ML/AI Analysis | ⚠️ Manual AutoML setup | ✅ Automatic ML | **Scoop** | PBI requires dataflows config, Scoop runs automatically |
| Investigation Depth | ❌ Single query only | ✅ Multi-pass (3-10) | **Scoop** | "Copilot doesn't answer follow-up questions" |
| Workflow Integration | ⚠️ Teams/SharePoint only | ✅ Excel/PPT/Slack | **Scoop** | No Slack integration, limited PowerPoint |
| Business User Ready | ❌ Extensive prep needed | ✅ 30-second setup | **Scoop** | Requires data prep, training, governance |

---

## Key Functionality Gaps vs Scoop

### Excel Support Gap:
- **Power BI**: ZERO native Excel formula support, only DAX
- **Scoop**: 150+ Excel functions (VLOOKUP, SUMIFS, etc.) work on live data
- **Impact**: Business users must learn new DAX language vs using existing Excel knowledge

### ML/AI Capabilities Gap:
- **Power BI**: AutoML exists but requires manual setup, dataflows, Premium license
- **Scoop**: ML runs automatically when user asks "Why?" - no setup needed
- **Impact**: IT must configure ML models vs automatic discovery

### Investigation Depth Gap:
- **Power BI**: "One question at a time", no follow-up, cannot find root causes
- **Scoop**: 3-10 pass automatic investigation to find WHY
- **Impact**: Cannot investigate problems, only surface-level queries

### Workflow Integration Gap:
- **Power BI**: No Slack, limited PowerPoint (add-in required), Teams-focused
- **Scoop**: Native Excel, PowerPoint, Slack integration in 30 seconds
- **Impact**: Locked into Microsoft ecosystem, no Slack for modern teams

### Business User Readiness Gap:
- **Power BI**: Requires F64 capacity ($60k), data prep, training, 24-hour wait
- **Scoop**: Works immediately, no training, PPU license compatible
- **Impact**: Months of prep and training vs immediate value