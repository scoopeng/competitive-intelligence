# Visual Strategy Guide for Competitor Comparisons

**Purpose**: Guide content generation to suggest strategic visual placements
**Audience**: AI agents generating web_comparison.md files
**Status**: Active - to be referenced in generation prompts

---

## Philosophy

Content should **suggest** where visuals enhance understanding, not hardcode specific images. The deployment platform (webflow-competitive-platform) will select appropriate screenshots from the shared visual registry.

---

## Available Visual Categories

All screenshots are available in both repositories via CDN URLs in `../promptcontent/screenshots.md`:

### Investigation & Analysis
- **Multi-pass investigation** (bubble chart drill-down with segmentation)
- **Chat-generated visualizations** (column charts, time series)
- **Decision tree analysis** (ML segmentation with nodes)
- **Pipeline exploration** (stage-by-month tracking)

### Setup & Integration
- **Data source connection** (30-second setup screen)
- **CRM writeback** (closing the loop from insight to action)

### Output & Presentation
- **Auto-generated presentations** (dark theme, light theme)
- **PowerPoint export from Slack**

### Workflow Integration
- **Slack full interface** (analytics where teams work)
- **Slack visualizations** (dark mode charts)
- **Slack dataset questions** (natural language interface)

---

## Suggested Visual Hints in Markdown

When generating `web_comparison.md` files, include visual suggestions as HTML comments:

### Syntax
```markdown
<!-- VISUAL: [use-case] -->
<!-- CAPTION: [what this proves about competitive advantage] -->
```

### Example Placements

#### 1. Hero Section (Always)
```markdown
## 1. EXECUTIVE COMPARISON

<!-- VISUAL: hero -->
<!-- CAPTION: Scoop's core competitive advantage for this matchup -->

### TL;DR Verdict
...
```

**Deployment platform decides**:
- Portal-heavy competitors (Domo, Sisense) → Investigation depth screenshot
- Excel/BI competitors (Power BI, Tableau) → Setup simplicity screenshot
- Platform plays (Snowflake) → Data source integration

#### 2. Architecture Comparison Section
```markdown
## 3. THE FUNDAMENTAL ARCHITECTURE DIFFERENCE

<!-- VISUAL: architecture-comparison -->
<!-- CAPTION: Workflow difference - [Competitor] vs Scoop approach -->

### [Competitor]: [Their Approach]
...

### Scoop: Investigation-First
...
```

**Deployment platform can**:
- Generate Mermaid.js diagram from workflow descriptions
- Show side-by-side screenshots (if available)
- Or skip if content is too long (50K limit)

#### 3. Investigation Depth Section
```markdown
## 4. INVESTIGATION CAPABILITIES

<!-- VISUAL: investigation-depth -->
<!-- CAPTION: Multi-pass investigation - follow your curiosity 3-10 queries deep -->

**[Competitor] Limitation**: Single-query responses, dashboard narration
**Scoop Advantage**: True investigation with follow-up questions
...
```

**Proves**: Our core "investigation vs query" positioning

#### 4. Native Workflow Section
```markdown
## 5. WORKFLOW & USER EXPERIENCE

<!-- VISUAL: native-workflow -->
<!-- CAPTION: Analytics in Excel/Slack - no portal required -->

**[Competitor]**: Portal-centric access
**Scoop**: Native Excel formulas, Slack integration
...
```

**Proves**: "Portal prison" vs native workflow claim

#### 5. Setup Time Section
```markdown
## 6. IMPLEMENTATION & SETUP

<!-- VISUAL: setup-simplicity -->
<!-- CAPTION: 30-second setup - connect and start investigating immediately -->

**[Competitor]**: 1-2 month implementation, semantic model required
**Scoop**: 30 seconds from signup to first insight
...
```

**Proves**: Time-to-value advantage

#### 6. Presentation Output Section
```markdown
## 7. PRESENTATION & SHARING

<!-- VISUAL: presentation-automation -->
<!-- CAPTION: Auto-generated presentations in 30 seconds - no manual assembly -->

**[Competitor]**: Manual dashboard export, requires assembly
**Scoop**: Automatic presentation generation with AI layouts
...
```

**Proves**: Presentation automation advantage

---

## Visual Hint Guidelines

### When to Suggest Visuals

✅ **DO suggest visuals when**:
- Making a major competitive claim that benefits from visual proof
- Describing a workflow difference (architecture comparison)
- Highlighting a unique capability (investigation depth, spreadsheet engine)
- Proving a quantified advantage (30-second setup, 97% cost savings)

❌ **DON'T suggest visuals for**:
- Pricing tables (already well-formatted)
- Feature comparison matrices (tables work better)
- Bullet lists of capabilities (text is clearer)
- Bottom-line summaries (keep concise)

### How Many Visuals to Suggest

**Conservative approach** (recommended):
- 1 hero visual (always)
- 2-3 section visuals (for major claims only)
- Total: 3-4 visual hints per page

**Why conservative?**:
- Webflow 50K character limit per field
- Visual HTML adds ~400 chars per screenshot
- Some competitors have 100K+ content already
- Deployment platform may skip visuals on content-heavy pages

### Caption Writing Guidelines

Captions should:
1. **Connect to competitive advantage**: Not just "Scoop interface" but "Multi-pass investigation proves we go 3-10 queries deep vs single-query responses"
2. **Be specific**: "30-second setup" not "fast setup"
3. **Stay business-focused**: Emphasize user benefit, not technical feature
4. **Be concise**: 10-15 words max

**Good captions**:
- "Scoop's multi-pass investigation: Start with segmentation, drill into any bubble, explore root causes"
- "30-second setup: Connect to any data source and start investigating immediately"
- "Auto-generated presentations with live data - no manual assembly required"

**Bad captions**:
- "Screenshot of Scoop" (too generic)
- "Our sophisticated AI-powered multi-modal investigation engine" (too technical)
- "This shows how users can analyze data using natural language" (too vague)

---

## Use Case to Visual Mapping

The deployment platform uses this mapping:

| Use Case Hint | Resolves To | When Most Effective |
|--------------|-------------|---------------------|
| `hero` | Auto-selected by competitor type | Every page |
| `investigation-depth` | Bubble chart drill-down | Portal competitors (Domo, ThoughtSpot, Sisense) |
| `setup-simplicity` | Data source connection screen | Complex setup competitors (Snowflake, Tableau, Power BI) |
| `native-workflow` | Excel/Slack in action | Portal-centric competitors |
| `presentation-automation` | Auto-generated decks | Manual export competitors (most) |
| `architecture-comparison` | Mermaid.js diagram | Fundamental workflow differences |
| `advanced-analytics` | Decision tree ML output | Competitors claiming "AI" without ML |
| `slack-integration` | Slack interface | When Slack is key differentiator |

---

## Example: Full Visual Strategy for Domo

```markdown
# Scoop vs Domo: Complete Comparison

## 1. EXECUTIVE COMPARISON

<!-- VISUAL: hero -->
<!-- CAPTION: Scoop's multi-pass investigation vs Domo's single-query dashboard narration -->

### TL;DR Verdict
...

## 2. CAPABILITY COMPARISON MATRIX
[No visual - table format works best]

## 3. THE FUNDAMENTAL ARCHITECTURE DIFFERENCE

<!-- VISUAL: architecture-comparison -->
<!-- CAPTION: Investigation-first vs Dashboard-first - fundamentally different approaches to analytics -->

### Domo: Dashboard-First, Insight-Second
...

### Scoop: Investigation-First, Dashboard-Optional
...

## 4. INVESTIGATION DEPTH: THE DECISIVE DIFFERENCE

<!-- VISUAL: investigation-depth -->
<!-- CAPTION: Multi-pass investigation - follow curiosity 3-10 queries deep, not single-query responses -->

**The Core Difference**: Domo's AI Chat narrates existing dashboards (single query). Scoop investigates with follow-up questions (multi-pass exploration).
...

## 5. NATIVE WORKFLOW VS PORTAL PRISON

<!-- VISUAL: native-workflow -->
<!-- CAPTION: Excel formulas executing with 150+ functions - no portal required -->

**Domo**: Disables Excel formulas "for security", requires portal for all analysis
**Scoop**: 150+ Excel functions execute natively, Slack integration, no portal dependency
...

## 6. SETUP TIME: 30 SECONDS VS 1-2 MONTHS
[No visual - the numbers speak for themselves]

## 7. PRICING: FLAT VS CONSUMPTION

<!-- VISUAL: setup-simplicity -->
<!-- CAPTION: 30-second setup: Connect any data source, start investigating immediately - no semantic model required -->

[Content about pricing and setup...]

## 8. NEXT STEPS
[No visual - CTA section]
```

**Result**: 1 hero + 4 section visuals = 5 total (on high end, but Domo is highest-scoring competitor so deserves rich visual treatment)

---

## Integration with Generation Workflow

### In Generation Prompts

Add this instruction:
```
When generating web_comparison.md:
1. Reference VISUAL_STRATEGY_GUIDE.md for visual placement guidelines
2. Add visual hints using <!-- VISUAL: [use-case] --> comments
3. Add captions using <!-- CAPTION: [specific advantage] --> comments
4. Suggest 3-4 visuals per page (1 hero + 2-3 sections)
5. Focus visuals on proof points for major competitive claims
```

### In Deployment Platform

The webflow-competitive-platform:
1. Parses `<!-- VISUAL: [use-case] -->` hints
2. Looks up appropriate screenshot from visual registry
3. Inserts if page size allows (under 135K chars estimated)
4. Uses suggested caption or generates from competitive context
5. Skips visual if content is too long (graceful degradation)

---

## Maintenance

### When New Screenshots Are Added

1. Add to `../promptcontent/screenshots.md` with description
2. Add to `webflow-competitive-platform/src/lib/visual-registry.js` with metadata
3. Update this guide's "Available Visual Categories" if new category
4. Optionally: Regenerate competitor pages to suggest new visual use cases

### When Visual Strategy Changes

**No regeneration needed** - just update:
- `visual-registry.js` mappings (which screenshot for which use case)
- Redeploy affected pages

**Regeneration beneficial** - if you want to:
- Change visual placement strategy (hero vs sections)
- Add/remove visual hints for specific competitive claims
- Update captions to emphasize different advantages

---

## Success Metrics

Track these to measure visual enhancement effectiveness:

1. **Engagement**: Time on page, scroll depth (via Webflow analytics)
2. **Conversion**: "Try Scoop Free" click-through rate
3. **Qualitative**: Sales team feedback - are visuals persuasive?
4. **Technical**: Field sizes - are we staying under 50K limit?

**Target**: 20%+ increase in CTA clicks on pages with hero screenshots vs text-only

---

## Questions for Content Strategist

When generating a new comparison, ask:

1. **What's the #1 competitive advantage** for this matchup? (Informs hero visual)
2. **What claim most needs visual proof?** (Investigation depth? Setup time? Output quality?)
3. **What workflow difference is hardest to explain in text?** (May need architecture diagram)
4. **Is this a top-tier competitor** (Domo, ThoughtSpot) or lower-priority (DataChat)? (Affects visual budget: 4-5 vs 2-3 visuals)

---

## Conclusion

Visual strategy should enhance, not clutter. Every visual must:
- **Prove a specific competitive claim**
- **Be referenced in surrounding text**
- **Enhance understanding**, not just decorate

Content suggests WHERE and WHY to show visuals. Deployment platform decides WHICH screenshot and WHETHER to include (based on size constraints).

This separation allows:
- Content strategists to focus on competitive positioning
- Presentation layer to optimize visual delivery
- Quick iteration without full content regeneration