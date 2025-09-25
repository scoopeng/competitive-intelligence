# Master Plan: Automated Competitor Research

**Status**: ENHANCED PROCESS DEPLOYED
**Power BI**: COMPLETED with deep research (85% complete)
**Next Target**: Tableau Pulse (Priority #2) - Enhanced 3-chunk process
**Remaining**: 9 competitors to complete with customer-story-driven intelligence

## The Strategy
Use Claude CLI to execute deep 3-chunk research that produces customer-story-driven intelligence with quantified evidence.

## The Architecture
```
Python Orchestrator → Claude CLI (with WebSearch/WebFetch) → Markdown Files → Next Chunk
```

## The 3 Chunks (Aligned to 6 Phases)

### Chunk 1: Discovery & Evidence (Phases 1-3)
- Check archives and existing research
- Verify URLs and documentation
- Mine customer reviews and forums
- **Output**: `research/evidence.md`

### Chunk 2: Technical & Pricing (Phases 4-5)
- Deep technical architecture analysis
- Find all pricing and hidden costs
- **Output**: `research/technical.md`, `research/pricing.md`

### Chunk 3: Analysis & Sales (Phase 6)
- BUPAF scoring with evidence
- Update battle card
- Create sales materials
- **Output**: Updated `BATTLE_CARD.md`, `outputs/`

## File Structure Per Competitor
```
competitors/[name]/
  CHUNK_1.md        # Detailed instructions for evidence gathering
  CHUNK_2.md        # Detailed instructions for technical/pricing
  CHUNK_3.md        # Detailed instructions for analysis
  research/         # Where findings are saved
  evidence/         # Sources and quotes
  outputs/          # Sales materials
  BATTLE_CARD.md    # Final output
```

## The Orchestrator
`claude_research_orchestrator.py`:
- Runs each chunk with 30-minute timeout
- Passes chunks to Claude CLI
- Claude reads instructions and executes
- Saves state between chunks
- Moves to next competitor

## Execution
```bash
python3 claude_research_orchestrator.py --competitor power-bi-copilot
```

## Why This Works
1. Claude CLI has WebSearch/WebFetch tools
2. Each chunk is self-contained with clear instructions
3. State preserved in markdown files between chunks
4. Python just orchestrates, Claude does the work