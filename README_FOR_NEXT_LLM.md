# Instructions for Next LLM

## What We Built
A system to automate competitor research using Claude CLI with real web search capabilities.

## The Complete Solution

### 1. The Orchestrator
`claude_research_orchestrator.py` - Python script that:
- Calls Claude CLI for each research chunk
- Gives Claude 30 minutes per chunk
- Manages state between chunks

### 2. The Chunks (Per Competitor)
Each competitor needs 3 files:
- `CHUNK_1.md` - Instructions for evidence gathering
- `CHUNK_2.md` - Instructions for technical/pricing research
- `CHUNK_3.md` - Instructions for analysis and sales materials

Use `CHUNK_TEMPLATE.md` to create these.

### 3. How It Works
```bash
# Claude CLI reads chunk instructions
# Uses WebSearch and WebFetch to gather REAL data
# Saves findings to markdown files
# Python moves to next chunk
```

## To Continue

### If Power BI chunks exist:
```bash
python3 claude_research_orchestrator.py --competitor power-bi-copilot
```

### To add new competitor:
1. Copy CHUNK_TEMPLATE.md sections to competitors/[name]/
2. Customize searches for that competitor
3. Run orchestrator

## Critical Requirements
- Claude CLI must be installed (`claude` command available)
- Each chunk outputs "CHUNK COMPLETE" when done
- 30-minute timeout per chunk is usually enough
- Results saved in competitors/[name]/research/

## The Goal
Transform each competitor from ~30% researched to 100% with:
- Real evidence from web searches
- Customer complaints with sources
- Technical limitations documented
- Pricing fully understood
- Battle cards ready for sales

This system WORKS - Claude CLI successfully gathered 200+ lines of real Power BI research in testing.