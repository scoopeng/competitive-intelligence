# Migration Plan: Tier Structure to Category Structure

## Migration Mapping

### From tier1-ai-pretenders → category-d-mirages
- tableau-pulse/ → Already has COMPREHENSIVE_BUPAF_ANALYSIS.md
- powerbi-copilot/ → Already has COMPREHENSIVE_BUPAF_ANALYSIS.md
- sisense/ → Already has COMPREHENSIVE_BUPAF_ANALYSIS.md
- qlik-insight-advisor/ → Already has COMPREHENSIVE_BUPAF_ANALYSIS.md
- datachat/ → Already has COMPREHENSIVE_BUPAF_ANALYSIS.md
- microstrategy/ → Not analyzed yet (skip for now)

### From tier2-accessible-ai → category-c-analyst
- domo/ → Already has COMPREHENSIVE_BUPAF_ANALYSIS.md
- datagpt/ → Already has COMPREHENSIVE_BUPAF_ANALYSIS.md
- snowflake/ → Move to category-d-mirages (scored 12/40)

### From tier3-real-ai → category-c-analyst
- thoughtspot/ → Already has COMPREHENSIVE_BUPAF_ANALYSIS.md
- tellius/ → Already has COMPREHENSIVE_BUPAF_ANALYSIS.md
- zenlytic/ → Already has COMPREHENSIVE_BUPAF_ANALYSIS.md

## Content to Preserve

### Valuable Source Documentation
1. **Research summaries** (research-summary-*.md)
2. **Pricing analyses** (pricing-*.md)
3. **User feedback** (review-*.md)
4. **Technical deep dives** (AI_CAPABILITIES_*.md)
5. **Implementation guides** (IMPLEMENTATION_*.md)

### Content to Archive
- Old README.md files (replaced by COMPREHENSIVE_BUPAF_ANALYSIS.md)
- Duplicate analyses
- Outdated research

## Migration Steps

1. Copy source documentation to new category folders
2. Create archive folder for old structure
3. Update any cross-references
4. Remove old tier folders
5. Create README for each category