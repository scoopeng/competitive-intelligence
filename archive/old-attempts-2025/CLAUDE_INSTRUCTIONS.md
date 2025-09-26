# CLAUDE: Execute Competitor Research

## YOUR MISSION
Research competitors systematically. Each time you open this file, continue where the previous Claude left off.

## IMMEDIATE ACTION
1. Check `CURRENT_RESEARCH.md` to see which competitor and step you're on
2. Go to that competitor's folder
3. Read their `TODO.md`
4. Execute that ONE task
5. Update files
6. Move to next task
7. Stop after completing ONE task

## STEP-BY-STEP PROCESS

### Step 1: Check Current State
```bash
cat CURRENT_RESEARCH.md
```
This tells you: competitor name, current step number

### Step 2: Read Current Task
```bash
cat competitors/[name]/TODO.md
```
This tells you: exactly what to research

### Step 3: Execute Research
- Use WebSearch for finding information
- Use WebFetch for getting documentation
- Gather REAL evidence with URLs
- Be thorough

### Step 4: Save Findings
```bash
# Append to findings file
cat >> competitors/[name]/research/findings.md
```
Include:
- Date/time
- What you searched
- What you found
- Source URLs
- Key quotes

### Step 5: Update TODO
Edit `competitors/[name]/TODO.md`:
- Mark current task DONE
- Add next task from RESEARCH_PLAN.md
- Include context for next Claude

### Step 6: Update Current State
Edit `CURRENT_RESEARCH.md`:
- Update step number
- Add timestamp
- Note what was completed

### Step 7: STOP
- Do NOT continue to next task
- Leave clear state for next Claude
- Exit

## EXAMPLE EXECUTION

If CURRENT_RESEARCH.md says:
```
Competitor: power-bi-copilot
Step: 3
```

Then you:
1. Read `competitors/power-bi-copilot/TODO.md`
2. See task is "Search G2 for negative reviews"
3. Use WebSearch("Power BI site:g2.com negative reviews")
4. Save findings to research/findings.md
5. Update TODO.md with step 4 task
6. Update CURRENT_RESEARCH.md to step 4
7. STOP

## CRITICAL RULES
- ONE task per Claude session
- ALWAYS save real findings, not placeholders
- ALWAYS update state files
- NEVER skip steps
- NEVER do multiple tasks
- STOP means STOP

## FILE STRUCTURE
```
CURRENT_RESEARCH.md         <- Start here
competitors/
  [name]/
    TODO.md                 <- Current task
    RESEARCH_PLAN.md        <- All 50 tasks
    research/
      findings.md           <- Accumulating research
    evidence/
      sources.md            <- All URLs
```

## BEGIN
Read CURRENT_RESEARCH.md and execute your ONE task.