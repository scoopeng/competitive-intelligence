# Capability Experiments - September 2025

**Date**: September 2025
**Status**: Archived - experiments not adopted

## What These Were

During the September 2025 BUA Framework update, we experimented with alternative approaches to capability scoring. These experiments aimed to create more granular, machine-readable capability assessments.

## Files in This Archive

1. **CAPABILITY_MATRIX.md** (332 lines)
   - Defined detailed capability assessment categories
   - Used by: `webflow-competitive-platform/src/lib/framework/bua-framework-research.js`
   - Categories: Investigation, Integration, ML/AI, Data Handling, Visualization
   - Binary and scored capabilities

2. **CAPABILITY_SCORING_RUBRIC.md** (157 lines)
   - Objective rubric for scoring capabilities
   - Binary capabilities (yes/no) with clear criteria
   - Gradient capabilities (0-10 scale) with definitions
   - Alternative to narrative scoring approach

3. **FRAMEWORK_ANALYSIS_2025.md** (96 lines)
   - Analysis of framework inconsistencies across competitors
   - Documented that framework evolved during scoring process
   - Found component name variations across 11 competitors
   - Identified scoring patterns and evolution

## Why Archived

**Decision**: Maintain narrative scoring approach in main framework

**Reasons**:
1. **Narrative approach is more flexible** - Can capture nuances that binary scoring misses
2. **Machine-readable format not needed** - No automated tools consuming this data
3. **Component name variations acceptable** - Consistency improved through documentation
4. **Simplicity preferred** - Single source of truth (BUSINESS_USER_EMPOWERMENT_FRAMEWORK.md)

## What We Kept

- **Core insight from FRAMEWORK_ANALYSIS_2025.md**: Documentation of how framework evolved
- **Lesson**: Need clear rubrics to prevent scoring drift (led to Understanding dimension revision)
- **Approach**: Detailed sub-component rubrics in main framework document

## Lessons Learned

1. **Don't over-engineer** - Machine-readable formats add complexity without clear benefit
2. **Single source of truth** - Multiple scoring approaches create confusion
3. **Narrative + detailed rubrics work** - Best of both worlds (flexibility + consistency)
4. **Evolution is OK** - Framework can improve during use, just document it

---

**Archived**: September 30, 2025
**Reason**: Experiments not adopted - narrative approach preferred
**Status**: Historical reference only