# Tableau Pulse Technical Requirements - Tableau Analysis
**URL**: https://help.tableau.com/current/online/en-us/pulse_intro.htm & pulse_create_metrics.htm
**Type**: Official Technical Documentation
**Date Accessed**: 2025-01-28

## Key Findings Summary
Technical documentation reveals Tableau Pulse is far from the "easy, self-service" tool marketed. It requires extensive technical knowledge, specific data structures, complex permissions, and is limited to Tableau Cloud only. The "simplified" metric creation still demands understanding of data aggregation, time dimensions, and business logic that typical business users don't possess.

## Detailed Analysis

### What They Claim vs Reality

**Marketing Claims:**
- "Simplified way to create metric definitions"
- "Guided data exploration" for business users  
- "With only a few selections" you can create metrics

**Reality from Technical Docs:**
- Requires understanding of measures vs dimensions
- Must know appropriate aggregation methods
- Need to configure time dimensions correctly
- "Advanced definitions need more technical skills"
- Recommends using desktop/laptop, not mobile for creation

### Core Technical Requirements

**Data Source Requirements:**
1. **Must be published to Tableau Cloud** - no local or Server sources
2. **Time dimension mandatory** with specific granularities:
   - Supported: day, week, month, quarter, year
   - NOT supported: hour, minute, second
   - "Data that requires a lower level of granularity (hour or minute) isn't a good fit"
3. **At least one dimension for filtering**
4. **Proper data structure** - single point-in-time values won't work
5. **Authentication pre-configured** - no user prompts allowed

**Metric Creation Requirements:**
- Understanding of measure fields vs dimensions
- Knowledge of aggregation types
- Ability to define time series parameters
- Understanding of data granularity
- Technical skill to create "advanced definitions"

### Licensing & Permission Complexity

**Who Can Create Metrics:**
- Creator license ($42-98/month)
- Site Administrator Explorer
- Explorer (can publish) - mid-tier license

**Who CANNOT Create Metrics:**
- Viewer license users (lowest tier)
- Standard Explorer users
- Anyone without specific data source permissions

**Permission Requirements:**
- "Create Metric Definitions" permission capability
- Connect permission on data source
- View permission on data source
- Write and publish access for updates

### The "Simplified" Creation Process

**Actual Steps (not so simple):**
1. Select appropriate data source (must meet all requirements)
2. Name the metric definition 
3. Select measure field (or dimension with proper aggregation)
4. Choose correct aggregation method
5. Configure time dimension settings
6. Set up adjustable filters (require dimension selection)
7. Configure number formatting
8. Set up insights platform settings
9. Optional: Configure goals and thresholds
10. Optional: Set up custom calendar (complex)

**"Advanced" Requirements:**
- Custom calculations
- Complex aggregations
- Programmatic creation via API
- JSON bundle manipulation

### Platform Limitations

**Critical Restrictions:**
- **Tableau Cloud ONLY** - no Tableau Server support
- Cannot handle real-time or near-real-time data
- Limited to predefined time granularities
- No support for complex time-series analysis
- Single data source per metric limitation

**Hidden Complexities:**
- Custom calendars require complete field validation
- All calendar fields mandatory
- Must ensure calendar is "complete, consistent, and doesn't skip any dates"
- Programmatic creation requires JSON template manipulation

### Business User Reality Check

**What Business Users Actually Need:**
- Technical understanding of data structures
- Knowledge of aggregation methods
- Ability to identify appropriate time dimensions
- Understanding of filtering requirements
- Desktop/laptop access (mobile not recommended)

**What They Can't Do:**
- Create metrics from unpublished data
- Work with hourly or real-time data
- Create metrics without proper permissions
- Build complex calculations without technical help
- Use natural language to define metrics

### API Complexity Revealed

**Documentation Quote:**
> "Bundles are rich and complex objects that can be challenging to build manually. One approach to efficiently create the JSON for a bundle is to use the Tableau user interface to create the form of metric definition and metrics you want to produce programmatically. Then you can navigate to a metric and use your browsers' inspector to view and copy the JSON response for the insight bundle."

This reveals the true technical complexity hidden behind the "simplified" interface.

### Missing Capabilities

**What Pulse CANNOT Do:**
- Handle streaming or real-time data
- Support sub-daily granularity
- Work with Tableau Server (on-premise)
- Allow true ad-hoc metric creation
- Enable natural language metric definition
- Support complex multi-source metrics

### Red Flags

**Technical Debt Indicators:**
- Legacy metrics don't transfer
- Complex permission inheritance
- Manual JSON manipulation for automation
- Browser developer tools needed for API work

**Complexity Warnings:**
> "For more complex setups...Tableau Pulse validates the fields for the custom calendar. All of the fields are required."

> "Recommended to use desktop/laptop, not mobile"

**Licensing Trap:**
> "All user licenses on a deployment must be on the same edition"

### Key Quotes

Reality admission:
> "Advanced definitions need more technical skills"

Granularity limitation:
> "Data that requires a lower level of granularity (hour or minute) isn't a good fit for Tableau Pulse"

Complexity revealed:
> "Bundles are rich and complex objects that can be challenging to build manually"

Platform restriction:
> "Only available on Tableau Cloud"

### Evidence Needed
- Screenshots showing the actual complexity of metric creation
- Examples of "simple" vs "advanced" definitions
- Time studies on metric creation by real business users
- Documentation of permission setup complexity
- Examples of failures with hourly/real-time data
- Proof of how much IT support is actually required