# Research Execution Guide

## Current Setup

### What We Have
1. **2 competitors with chunks ready**: tableau-pulse, power-bi-copilot
2. **9 competitors need chunks**: All others
3. **Two execution options**: Manual or semi-automated

## Execution Options

### Option 1: Direct Claude Execution (Recommended)
```bash
# In Claude, for each competitor:
cd competitors/tableau-pulse
# Read and execute CHUNK_1.md
# Read and execute CHUNK_2.md
# Read and execute CHUNK_3.md
```

**Pros**: Full visibility, adaptive, can fix issues in real-time
**Cons**: Requires human to continue between chunks

### Option 2: Python Runner (Semi-Automated)
```bash
python3 run_research.py tableau-pulse
```

**What it does**:
- Executes existing chunks via Claude CLI
- Waits between chunks
- Logs progress

**What it DOESN'T do**:
- Create missing chunks
- Continue to next competitor automatically
- Resume from failures

### Option 3: Autonomous Script (Aspirational)
```bash
python3 autonomous_research.py --all
```

**Would do (if Claude CLI worked reliably)**:
- Generate chunks from template
- Run all competitors in sequence
- Track progress in JSON
- Resume from failures

**Reality**: Claude CLI integration is fragile, may not work as expected

## Recommended Approach

### For Immediate Execution (Tableau Pulse)

**Step 1: Start with Tableau manually in Claude**
```
1. Read competitors/tableau-pulse/CHUNK_1.md
2. Execute all 17 searches systematically
3. Save results to specified files
4. Continue with CHUNK_2.md
5. Continue with CHUNK_3.md
```

**Step 2: Verify outputs**
- Check research/ folder has customer stories
- Check evidence/ folder has quotes
- Verify BUPAF scoring is updated

**Step 3: Commit progress**
```bash
git add competitors/tableau-pulse/
git commit -m "Complete Tableau Pulse research"
```

### For Remaining Competitors

**Create chunks first**:
```bash
# For each competitor without chunks:
1. Copy CHUNK_TEMPLATE.md content
2. Replace {COMPETITOR} with actual name
3. Split into 3 separate CHUNK_*.md files
4. Save in competitors/[name]/
```

**Then execute**:
- Either manually in Claude (reliable)
- Or via run_research.py (if Claude CLI works)

## Key Points

1. **No truly autonomous solution exists** - Claude can't restart itself
2. **Manual execution in Claude is most reliable** - You see what's happening
3. **Python runners add complexity** - Only useful if Claude CLI works well
4. **Chunks must exist first** - Scripts won't generate them automatically

## Current Priority

1. ✅ Complete Tableau Pulse (has chunks, ready to go)
2. ⏸️ Re-run Power BI (has chunks, needs better execution)
3. ⏸️ Create chunks for remaining 9 competitors
4. ⏸️ Execute systematically by priority

The simplest path: Execute Tableau Pulse chunks directly in Claude now.