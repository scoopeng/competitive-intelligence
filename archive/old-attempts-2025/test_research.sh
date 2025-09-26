#!/bin/bash

# Test if Claude CLI can do actual research and save results

cd competitors/power-bi-copilot/

echo "Testing Claude CLI research and file writing..."

claude --print --allowedTools "Write" "
Read TODO.md in this directory.
The task asks to search for Power BI Copilot problems.
Create a file called test_output.md with at least 3 problems you know about Power BI Copilot.
Just say 'Done' when complete.
" 2>/dev/null

if [ -f "test_output.md" ]; then
    echo "Success! File created:"
    cat test_output.md
else
    echo "File not created"
fi