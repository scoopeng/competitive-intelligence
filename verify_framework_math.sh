#!/bin/bash

echo "=== BUA Framework Mathematical Verification ==="
echo ""
echo "Checking all 12 framework_scoring.md files for mathematical accuracy..."
echo ""

total_files=0
pass_files=0
fail_files=0

for comp in scoop power-bi-copilot tableau-pulse thoughtspot snowflake-cortex domo qlik zenlytic sisense datagpt tellius datachat; do
    file="/home/ubuntu/dev/competitive-intelligence/competitors/$comp/evidence/framework_scoring.md"
    
    if [ -f "$file" ]; then
        total_files=$((total_files + 1))
        
        # Extract total score
        total=$(grep "Total Score:" "$file" | head -1 | grep -oP '\d+/100' | cut -d'/' -f1)
        
        # Extract dimension scores
        autonomy=$(grep "^## Dimension 1: Autonomy" "$file" | grep -oP '\d+/20' | cut -d'/' -f1)
        flow=$(grep "^## Dimension 2: Flow" "$file" | grep -oP '\d+/20' | cut -d'/' -f1)
        understanding=$(grep "^## Dimension 3: Understanding" "$file" | grep -oP '\d+/20' | cut -d'/' -f1)
        presentation=$(grep "^## Dimension 4: Presentation" "$file" | grep -oP '\d+/20' | cut -d'/' -f1)
        data=$(grep "^## Dimension 5: Data" "$file" | grep -oP '\d+/20' | cut -d'/' -f1)
        
        if [ -n "$autonomy" ] && [ -n "$flow" ] && [ -n "$understanding" ] && [ -n "$presentation" ] && [ -n "$data" ]; then
            sum=$((autonomy + flow + understanding + presentation + data))
            
            if [ "$sum" -eq "$total" ]; then
                echo "✅ $comp: $total/100 = $autonomy+$flow+$understanding+$presentation+$data"
                pass_files=$((pass_files + 1))
            else
                echo "❌ $comp: Claims $total/100 but sums to $sum ($autonomy+$flow+$understanding+$presentation+$data)"
                fail_files=$((fail_files + 1))
            fi
        else
            echo "⚠️  $comp: Missing dimension scores (cannot verify)"
            fail_files=$((fail_files + 1))
        fi
    fi
done

echo ""
echo "=== Summary ==="
echo "Total files: $total_files"
echo "Passed: $pass_files"
echo "Failed: $fail_files"
echo ""

if [ "$fail_files" -eq 0 ]; then
    echo "✅ All framework scoring files are mathematically correct!"
    exit 0
else
    echo "❌ $fail_files files have mathematical errors that need fixing"
    exit 1
fi
