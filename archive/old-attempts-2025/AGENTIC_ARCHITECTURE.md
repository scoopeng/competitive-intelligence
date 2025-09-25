# Agentic Research Architecture

## How It Works

### The Architecture
```
Python Orchestrator (Director)
    ↓
Claude Code API (Worker)
    ↓
Real Research Tools (WebSearch, WebFetch)
    ↓
Saved Results (Markdown files)
    ↓
Next Claude Instance (Reads state, continues)
```

### Key Insight
- **Python Script**: Just orchestrates/directs - doesn't do research
- **Claude Code**: Does ALL the actual research using its tools
- **State Management**: Via markdown files that persist between calls
- **Each Step**: Like a new Claude chat that reads previous context

## Implementation

### 1. Research Plans (Per Competitor)
Each competitor has:
- `RESEARCH_PLAN.md` - 50 detailed research tasks
- `TODO.md` - Current task for Claude to execute
- `research/findings.md` - Accumulating research results
- `evidence/sources.md` - All verified URLs

### 2. Python Orchestrator
```python
# For each step:
1. Read current state from files
2. Create prompt for Claude
3. Call Claude Code API
4. Claude executes task with real tools
5. Claude saves results and updates state
6. Move to next step
```

### 3. Claude Execution (Each Step)
When Claude is called, it:
```
1. Reads RESEARCH_PLAN.md to understand context
2. Reads TODO.md for current task
3. Uses WebSearch to find real information
4. Uses WebFetch to get documentation
5. Saves findings in research/findings.md
6. Updates RESEARCH_PLAN.md (marks task complete)
7. Updates TODO.md with next task
8. Creates clear handoff for next execution
```

## Example Flow

### Step 1: Python calls Claude
```
Prompt: "Research Power BI Copilot limitations.
Your current task is in TODO.md"
```

### Step 2: Claude executes
```
- Reads: TODO says "Search for nondeterministic outputs"
- Executes: WebSearch("Power BI Copilot nondeterministic")
- Finds: Microsoft admits outputs are nondeterministic
- Saves: Evidence in research/findings.md
- Updates: Marks step 1 complete in RESEARCH_PLAN.md
- Updates: TODO.md with step 2 task
```

### Step 3: Next Claude call
```
- Reads: TODO says "Find G2 negative reviews"
- Executes: WebSearch("Power BI site:g2.com negative reviews")
- Continues from where previous Claude left off
```

## Why This Works

1. **True Automation**: Claude does real research, not simulation
2. **Stateful**: Each Claude picks up where previous left off
3. **Verifiable**: All findings saved with sources
4. **Scalable**: Can run 50+ steps per competitor
5. **Intelligent**: Claude makes decisions, not just following script

## Running It

### Manual Testing (What we can do now)
```bash
# Test with 2 steps on Power BI
python3 claude_orchestrator.py --competitor power-bi-copilot --steps 2
```

### Production (With Claude API)
```bash
# Run full research on all competitors
python3 claude_orchestrator.py --steps 50

# Run overnight
nohup python3 claude_orchestrator.py --steps 50 > research.log &
```

## Current Status

✅ **Created**:
- Research plans for each competitor (50 tasks each)
- Python orchestrator framework
- State management system via files
- Clear handoff mechanism between Claude calls

⏳ **Needs**:
- Actual Claude Code API integration
- Or manual execution of each step
- Real research to be performed

## The Key Innovation

**This is NOT simulation** - this is real agentic execution where:
- Python = Director (just orchestrates)
- Claude = Actor (does real work with real tools)
- Files = Memory (state between executions)
- Each Step = Focused task with clear handoff

This solves the problem of automated research by having AI do the actual work, not simulate it!