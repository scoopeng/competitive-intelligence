# Mathematical Errors to Fix

Based on QA report, these files have dimension sums that don't match totals:

1. **Tableau Pulse**: 7+4+10+8+8 = 37, but shows 36/100 → Change to 37/100
2. **ThoughtSpot**: 11+6+20+6+14 = 57, but shows 56/100 → Change to 57/100  
3. **Snowflake Cortex**: Dimensions sum to 26, but shows 34/100 → Need to check dimensions
4. **Qlik**: Dimensions sum to 47, but shows 46/100 → Change to 47/100
5. **Zenlytic**: Dimensions sum to 42, but shows 44/100 → Change to 42/100
6. **Sisense**: Dimensions sum to 28, but shows 38/100 → Need to check dimensions
7. **DataGPT**: Dimensions sum to 22, but shows 30/100 → Need to check dimensions
8. **Tellius**: Dimensions sum to 22, but shows 30/100 → Need to check dimensions
9. **DataChat**: Dimensions sum to 17, but shows 28/100 → Need to check dimensions

**Action**: Fix totals to match dimension sums OR fix dimensions to match totals.
