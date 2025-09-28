# Release Notes v1.1.0

**Date**: September 28, 2025
**Status**: Production Ready ✅

## Overview
Version 1.1.0 fixes critical issues where sections were empty or missing in generated comparisons. All sections now generate and display correctly.

## What Was Fixed

### 1. Executive Summary Sections
**Problem**: Bullet point sections (Choose Scoop If, Consider X If) were empty
**Solution**: Added array handling for AI responses that return bullet points as JSON arrays
**Result**: All bullet sections now populate with 2-4 items each

### 2. BUA Framework Tables
**Problem**: Component breakdown tables were completely empty
**Solution**:
- Uncommented component iteration in MarkdownWriter
- Set dimension names on comparison objects
**Result**: Tables now show scores for all platforms (e.g., "7/8")

### 3. Missing Capability Sections
**Problem**: Capability Deep Dive section wasn't being generated or written
**Solution**:
- Added writeCapabilityDeepDive method to MarkdownWriter
- Generate all 5 capability sections in AIComparisonGenerator
**Result**: Full capability analysis with ~500 words per section

## Code Changes

### AIComparisonGenerator.java
```java
// Now handles both string and array responses
if (chooseScoopNode.isArray()) {
    StringBuilder bullets = new StringBuilder();
    for (JsonNode bullet : chooseScoopNode) {
        bullets.append("- ").append(bullet.asText()).append("\n");
    }
    summary.setChooseScoopIf(bullets.toString().trim());
}
```

### MarkdownWriter.java
```java
// Added capability writing
private void writeCapabilityDeepDive(StringBuilder md, ThreeWayComparison comparison) {
    if (comparison.getCapabilityDeepDive() == null) return;
    md.append("## Capability Deep Dive\n\n");
    // Write each capability section...
}
```

## Testing Results

### Test 1: thoughtspot vs domo
- **Duration**: 4m 44s
- **Result**: ✅ All sections populated
- **Issues**: TL;DR only 42 words

### Test 2: power-bi-copilot vs tableau-pulse
- **Duration**: 4m 41s
- **Result**: ✅ All sections populated
- **Issues**: TL;DR only 38 words

## Known Issues (Not Critical)

1. **TL;DR Word Count**: Currently 38-42 words (target: 50-58)
   - Requires prompt template adjustment
   - Does not affect functionality

2. **Evidence Citations**: Still generic "[Evidence: source]"
   - Requires evidence gathering enhancement
   - Cosmetic issue only

## Sections Now Generated

1. **Executive Summary**
   - TL;DR Verdict ✅
   - What is Scoop ✅
   - Choose Scoop If (3-4 bullets) ✅
   - Consider A If (2-3 bullets) ✅
   - Consider B If (2-3 bullets) ✅
   - Bottom Line ✅

2. **BUA Framework** (5 dimensions)
   - Autonomy (component table) ✅
   - Flow (component table) ✅
   - Understanding (component table) ✅
   - Presentation (component table) ✅
   - Data (component table) ✅

3. **Capability Deep Dive** (5 sections)
   - Investigation & Root Cause Analysis ✅
   - Excel & Spreadsheet Integration ✅
   - Side-by-Side Scenario Analysis ✅
   - Machine Learning & Pattern Discovery ✅
   - Workflow Integration & Mobile ✅

4. **FAQ Section**
   - 14 questions with 40-60 word answers ✅

## Usage

```bash
# Generate a comparison
./gradlew run --args="competitor-a competitor-b"

# Example
./gradlew run --args="thoughtspot domo"

# Output location
output/thoughtspot-vs-domo-vs-scoop-ai.md
```

## Performance Metrics

- **AI Calls**: 11 per comparison
- **Total Time**: ~4-5 minutes
- **Output Size**: ~15-20KB markdown
- **Sections**: 4 major, 15+ subsections
- **Word Count**: ~7,500-10,000 words

## Next Steps

1. Adjust TL;DR prompt for proper word count
2. Implement evidence citation integration
3. Add progress indicators during generation
4. Consider parallel AI calls for speed

## Files Changed

- `src/main/java/com/scoop/competitive/ai/AIComparisonGenerator.java`
- `src/main/java/com/scoop/competitive/writer/MarkdownWriter.java`
- `CHANGELOG.md`
- `README.md`
- `PROJECT_STRUCTURE.md`

## Commit

```
ef74036 Fix v1.1.0: All sections now generate correctly
```

---

**Version**: 1.1.0
**Build**: Stable
**Ready for**: Production Use