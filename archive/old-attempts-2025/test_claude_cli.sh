#!/bin/bash

# Test Claude CLI with a simple research task

cd competitors/power-bi-copilot/

echo "Testing Claude CLI research capabilities..."

claude --print "Read the TODO.md file in this directory and tell me what the current task is. Just output the task, nothing else." 2>/dev/null

echo ""
echo "Exit code: $?"