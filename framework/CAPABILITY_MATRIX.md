# Platform Capability Matrix
*Last Updated: September 30, 2025*

This file defines the detailed capability assessment for each platform.
Used by: webflow-competitive-platform/src/lib/framework/bua-framework-research.js

## Capability Categories

### Investigation
- multiHypothesis: Can test multiple hypotheses automatically
- autoDrill: Automatic drill-down capabilities
- patternDiscovery: Discovers patterns without user guidance
- whyAnalysis: Can answer "why" questions (not just "what")

### Integration
- slackNative: Native Slack integration
- slackActions: Number of Slack actions supported
- fileUpload: Direct file upload capability
- privacy: Privacy-aware processing

### Productivity
- powerpoint: PowerPoint generation
- queryDecks: Query deck creation
- nlSaving: Natural language query saving
- excelFormulas: Excel formula execution

### ML/AI
- builtInML: Built-in ML algorithms
- comparisons: Period-over-period comparisons
- segments: Segment analysis
- clustering: Clustering capabilities

---

## Platform Capabilities

### Scoop Analytics
```yaml
investigation:
  multiHypothesis: true
  autoDrill: true
  patternDiscovery: true
  whyAnalysis: true
integration:
  slackNative: true
  slackActions: 12
  fileUpload: true
  privacy: true
productivity:
  powerpoint: true
  queryDecks: true
  nlSaving: true
  excelFormulas: true
ml:
  builtInML: true
  comparisons: true
  segments: true
  clustering: true
```

### Power BI Copilot
```yaml
investigation:
  multiHypothesis: false
  autoDrill: false
  patternDiscovery: false
  whyAnalysis: false  # "doesn't answer follow-up questions"
integration:
  slackNative: false
  slackActions: 0
  fileUpload: false
  privacy: false
productivity:
  powerpoint: false  # Requires separate add-in
  queryDecks: false
  nlSaving: false  # Cannot save prompts
  excelFormulas: false  # ZERO Excel formula support
ml:
  builtInML: false
  comparisons: false
  segments: false
  clustering: false
```

### Tableau Pulse
```yaml
investigation:
  multiHypothesis: false
  autoDrill: false
  patternDiscovery: false
  whyAnalysis: false  # Notifications only
integration:
  slackNative: true  # Has Slack notifications
  slackActions: 1
  fileUpload: false
  privacy: false
productivity:
  powerpoint: false
  queryDecks: false
  nlSaving: false
  excelFormulas: false
ml:
  builtInML: false
  comparisons: true  # Can track changes
  segments: false
  clustering: false
```

### Domo
```yaml
investigation:
  multiHypothesis: false
  autoDrill: false
  patternDiscovery: true  # Has AutoML
  whyAnalysis: false
integration:
  slackNative: false
  slackActions: 0
  fileUpload: true
  privacy: false
productivity:
  powerpoint: false
  queryDecks: true  # Card system
  nlSaving: false
  excelFormulas: false
ml:
  builtInML: true  # AutoML features
  comparisons: true
  segments: true
  clustering: false
```

### ThoughtSpot
```yaml
investigation:
  multiHypothesis: false
  autoDrill: true  # SpotIQ
  patternDiscovery: true  # SpotIQ insights
  whyAnalysis: false
integration:
  slackNative: false
  slackActions: 0
  fileUpload: false
  privacy: false
productivity:
  powerpoint: false
  queryDecks: false
  nlSaving: true  # Saved searches
  excelFormulas: false
ml:
  builtInML: true  # SpotIQ ML
  comparisons: true
  segments: true
  clustering: false
```

### Qlik
```yaml
investigation:
  multiHypothesis: false
  autoDrill: false
  patternDiscovery: false
  whyAnalysis: false
integration:
  slackNative: false
  slackActions: 0
  fileUpload: true
  privacy: false
productivity:
  powerpoint: false
  queryDecks: false
  nlSaving: false
  excelFormulas: false
ml:
  builtInML: false
  comparisons: true
  segments: true
  clustering: false
```

### Zenlytic
```yaml
investigation:
  multiHypothesis: false
  autoDrill: false
  patternDiscovery: false
  whyAnalysis: false
integration:
  slackNative: false
  slackActions: 0
  fileUpload: true
  privacy: false
productivity:
  powerpoint: false
  queryDecks: false
  nlSaving: true
  excelFormulas: true  # Excel-like interface
ml:
  builtInML: false
  comparisons: true
  segments: false
  clustering: false
```

### Sisense
```yaml
investigation:
  multiHypothesis: false
  autoDrill: false
  patternDiscovery: false
  whyAnalysis: false
integration:
  slackNative: false
  slackActions: 0
  fileUpload: false
  privacy: false
productivity:
  powerpoint: false
  queryDecks: false
  nlSaving: false
  excelFormulas: false
ml:
  builtInML: false
  comparisons: true
  segments: false
  clustering: false
```

### Snowflake Cortex
```yaml
investigation:
  multiHypothesis: false
  autoDrill: false
  patternDiscovery: false
  whyAnalysis: false
integration:
  slackNative: false
  slackActions: 0
  fileUpload: false
  privacy: false
productivity:
  powerpoint: false
  queryDecks: false
  nlSaving: false
  excelFormulas: false
ml:
  builtInML: true  # Has ML functions
  comparisons: false
  segments: false
  clustering: true  # ML clustering
```

### DataGPT
```yaml
investigation:
  multiHypothesis: false
  autoDrill: false
  patternDiscovery: false
  whyAnalysis: false
integration:
  slackNative: false
  slackActions: 0
  fileUpload: false
  privacy: false
productivity:
  powerpoint: false
  queryDecks: false
  nlSaving: false
  excelFormulas: false
ml:
  builtInML: false
  comparisons: true
  segments: false
  clustering: false
```

### Tellius
```yaml
investigation:
  multiHypothesis: true  # Genius Mode
  autoDrill: true
  patternDiscovery: true  # 25+ ML algorithms
  whyAnalysis: false
integration:
  slackNative: false
  slackActions: 0
  fileUpload: false
  privacy: false
productivity:
  powerpoint: false
  queryDecks: false
  nlSaving: true
  excelFormulas: false
ml:
  builtInML: true  # Extensive ML
  comparisons: true
  segments: true
  clustering: true
```

### DataChat
```yaml
investigation:
  multiHypothesis: false
  autoDrill: false
  patternDiscovery: false
  whyAnalysis: false
integration:
  slackNative: false
  slackActions: 0
  fileUpload: true
  privacy: false
productivity:
  powerpoint: false
  queryDecks: false
  nlSaving: true  # Conversation history
  excelFormulas: false
ml:
  builtInML: false
  comparisons: false
  segments: false
  clustering: false
```

---

## Sources

- Power BI Copilot: phase2_functionality_analysis.md, Microsoft documentation
- Tableau Pulse: Notification-only system per vendor documentation
- Domo: AutoML and card system per platform research
- ThoughtSpot: SpotIQ capabilities per vendor documentation
- Others: Framework scoring and competitive research files