# Phase 2: Functionality Deep Dive - Zenlytic
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

**Documentation Review**: https://docs.zenlytic.com
- AI-powered BI platform with LLM technology
- "Zoë" AI assistant for natural language queries
- Requires "cognitive layer" configuration
- Targets commerce businesses >$10M GMV

**Core Components**:
- Natural language to SQL conversion
- Data Model Editor
- Dashboard creation and scheduling
- Microsoft Teams bot integration
- Embedding options for external apps

**Key Requirements**:
- **YAML configuration for everything**
- GitHub repository for version control
- Database connections setup
- Semantic layer definition

---

## 2B: Business User Empowerment Assessment

**Search 5**: Excel integration and support
- **Reality**: NO Excel integration or export found
- Positions as Excel replacement: "3 hours in spreadsheet vs 3 seconds with Zoë"
- No formula support, no export capabilities
- **vs Scoop**: Zero Excel support vs 150+ functions

**Search 6**: Natural language investigation
- Text-to-SQL conversion via LLM
- Can explain queries in plain language
- Single query responses
- **vs Scoop**: No multi-pass investigation capability

**Search 7**: Machine learning capabilities
- **Reality**: NO actual ML models
- Only LLM for text-to-SQL
- No predictive analytics
- No anomaly detection
- No pattern recognition
- **vs Scoop**: No J48/JRip/EM vs automatic ML

**Search 8**: Self-service setup
- **Claims**: "Anyone can interact without knowing structure"
- **Reality**: Requires YAML configuration
- Needs GitHub repository
- "Maintainers maintain metric definitions in YAML"
- **vs Scoop**: YAML engineering vs 30-second setup

**Search 9**: Workflow integration
- Microsoft Teams bot (limited)
- Slack mentioned but not detailed
- No PowerPoint integration
- No Excel integration
- **vs Scoop**: Limited Teams vs native all workflows

**Search 10**: Root cause analysis
- Can identify "what is causing changes"
- But no multi-pass investigation
- Single query limitation
- **vs Scoop**: Surface-level vs 3-10 pass investigation

---

## 2C: Gap Analysis & Limitations

**Search 11**: Limitations and issues
- CEO admits 90% accuracy is "absolutely terrible"
- "Self-service analytics is not there yet"
- No independent reviews found
- No community discussion

**Search 13**: Technical expertise required
- **YAML files required** for:
  - Models configuration
  - Views definition
  - Dashboard creation
  - Metric definitions
- GitHub repository required
- Version control system needed
- **"Maintainers maintain definitions in YAML"**

**Search 14**: Training requirements
- Claims "no SQL needed"
- BUT requires understanding:
  - YAML syntax
  - Data modeling concepts
  - GitHub operations
  - Semantic layer design

**Search 15**: Setup complexity
- Add database connections
- Configure YAML models
- Define semantic layer
- Set up GitHub repo
- Create zenlytic_project.yml
- Define views and joins

---

## Capability Comparison Matrix

| Capability | Zenlytic | Scoop | Winner | Evidence |
|------------|----------|-------|--------|----------|
| Excel Support | ❌ Zero | ✅ 150+ functions | **Scoop** | No Excel integration found |
| ML/AI Analysis | ❌ LLM only | ✅ Automatic ML | **Scoop** | No ML models, just text-to-SQL |
| Investigation Depth | ❌ Single query | ✅ Multi-pass (3-10) | **Scoop** | No multi-pass capability |
| Workflow Integration | ⚠️ Teams only | ✅ All native | **Scoop** | No Excel/PPT integration |
| Business User Ready | ❌ YAML required | ✅ 30-second | **Scoop** | GitHub + YAML configuration |

---

## Key Functionality Gaps vs Scoop

### Excel Support Gap:
- **Zenlytic**: ZERO Excel support, positions as replacement
- **Scoop**: 150+ Excel functions on live data
- **Impact**: Business users lose all Excel skills

### ML/AI Capabilities Gap:
- **Zenlytic**: Only LLM for text-to-SQL (90% accuracy)
- **Scoop**: J48, JRip, EM clustering run automatically
- **Impact**: No pattern discovery, just query translation

### Investigation Depth Gap:
- **Zenlytic**: Single query responses only
- **Scoop**: 3-10 pass automatic investigation
- **Impact**: Can't find root causes, only surface answers

### Workflow Integration Gap:
- **Zenlytic**: Teams bot only, no Excel/PowerPoint
- **Scoop**: Native Excel, PowerPoint, Slack integration
- **Impact**: Isolated tool vs integrated workflow

### Business User Readiness Gap:
- **Zenlytic**: YAML configuration + GitHub required
- **Scoop**: 30-second setup, no configuration
- **Impact**: IT project for months vs immediate value