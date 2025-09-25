# Prompt for Creating Chunks and Running Research

Copy and paste this entire prompt into a new Claude session:

---

## Your Mission

You need to create chunk files for competitors that don't have them, then execute systematic research starting with Tableau Pulse.

## Context
- Working directory: `/home/ubuntu/dev/competitive-intelligence/`
- 2 competitors have chunks: `tableau-pulse`, `power-bi-copilot`
- 9 competitors need chunks: `thoughtspot`, `domo`, `snowflake-cortex`, `sisense`, `qlik`, `tellius`, `zenlytic`, `datagpt`, `datachat`

## Step 1: Create Missing Chunks

For each competitor WITHOUT chunks, create 3 files using the template below.

Read `CHUNK_TEMPLATE.md` to get the full template, then for each competitor:

1. Create `competitors/[name]/CHUNK_1.md` with Phase 1 content
2. Create `competitors/[name]/CHUNK_2.md` with Phase 2 content
3. Create `competitors/[name]/CHUNK_3.md` with Phase 3 content

Replace `{COMPETITOR}` with the actual competitor name in proper case (e.g., "ThoughtSpot", "Domo", "Snowflake Cortex").

Priority order for chunk creation:
1. thoughtspot
2. domo
3. snowflake-cortex
4. sisense
5. qlik
6. tellius
7. zenlytic
8. datagpt
9. datachat

## Step 2: Execute Tableau Pulse Research

After creating chunks, execute the complete research for Tableau Pulse:

### CHUNK 1 Execution:
1. Read `competitors/tableau-pulse/CHUNK_1.md`
2. Execute all 17 searches listed
3. Save outputs to:
   - `research/customer_stories.md`
   - `research/industry_analysis.md`
   - `evidence/customer_quotes.md`
   - `evidence/community_sources.md`

### CHUNK 2 Execution:
1. Read `competitors/tableau-pulse/CHUNK_2.md`
2. Execute all 24 searches listed
3. Save outputs to:
   - `research/performance_analysis.md`
   - `research/competitive_positioning.md`
   - `research/integration_reality.md`
   - `research/economic_impact.md`

### CHUNK 3 Execution:
1. Read `competitors/tableau-pulse/CHUNK_3.md`
2. Calculate BUPAF scores with evidence
3. Update `BATTLE_CARD.md`
4. Create sales materials in `outputs/`

## Success Criteria
- [ ] All 9 competitors have CHUNK_1.md, CHUNK_2.md, CHUNK_3.md files
- [ ] Tableau Pulse research is complete with:
  - 10+ customer complaints
  - 5+ implementation horror stories
  - 15+ direct quotes
  - Quantified performance metrics
  - Updated BATTLE_CARD.md

## Important Notes
- Use WebSearch tool for all searches
- Extract specific quotes with context (company size, industry)
- Save incrementally - don't wait until the end
- Focus on evidence, not speculation
- Include dates and sources for all findings

Begin by checking which competitors already have chunks, then create the missing ones, then execute Tableau Pulse research completely.

---

## Alternate Shorter Version

If the above is too long, use this simpler prompt:

---

Working in `/home/ubuntu/dev/competitive-intelligence/`:

1. Check which competitors in `competitors/` folder have CHUNK_1.md, CHUNK_2.md, CHUNK_3.md files

2. For those that don't, create the 3 chunk files using the `CHUNK_TEMPLATE.md` template. Replace {COMPETITOR} with the actual name. Priority: thoughtspot, domo, snowflake-cortex, sisense, qlik, tellius, zenlytic, datagpt, datachat

3. Once chunks exist, execute complete research for `tableau-pulse`:
   - Read and execute CHUNK_1.md (17 searches about customer stories)
   - Read and execute CHUNK_2.md (24 searches about technical/competitive)
   - Read and execute CHUNK_3.md (BUPAF scoring and battle card update)
   - Save all outputs to the specified files

Focus on getting real customer evidence, quotes, and quantified limitations. Begin now.