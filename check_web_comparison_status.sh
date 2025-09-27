#!/bin/bash
# Check web comparison generation status for all competitors

echo "=== Web Comparison Status Report ==="
echo "Generated: $(date)"
echo ""

echo "Competitor                 | Score      | Category | Web Comparison | Status"
echo "--------------------------|------------|----------|----------------|--------"

cd /home/ubuntu/dev/competitive-intelligence/competitors

for dir in */; do
    comp=$(basename "$dir")

    # Skip special directories
    if [ "$comp" = "SHARED" ] || [ "$comp" = "README.md" ]; then
        continue
    fi

    # Get score from framework_scoring.md
    if [ -f "$dir/evidence/framework_scoring.md" ]; then
        score=$(grep "Total Score.*59" "$dir/evidence/framework_scoring.md" | head -1 | sed 's/.*: //' | sed 's/ (.*//')
        category=$(grep "Total Score.*59" "$dir/evidence/framework_scoring.md" | head -1 | sed 's/.*Category //' | sed 's/ -.*//')
    else
        score="No score"
        category="?"
    fi

    # Check for web comparison
    if [ -f "$dir/outputs/web_comparison.md" ]; then
        web="✓"
        status="Complete"
    else
        web="✗"
        status="Missing"
    fi

    # Format output
    printf "%-25s | %-10s | %-8s | %-14s | %s\n" "$comp" "$score" "$category" "$web" "$status"
done

echo ""
echo "=== Summary ==="
complete=$(find . -name "web_comparison.md" -path "*/outputs/*" | wc -l)
total=$(find . -maxdepth 1 -type d | grep -v "^\.$" | grep -v "SHARED" | wc -l)
echo "Complete: $complete / $total"
echo ""
echo "Priority Order (from WEB_COMPARISON_UPDATE_PLAN.md):"
echo "  Tier 1: Tableau Pulse, ThoughtSpot, Snowflake Cortex"
echo "  Tier 2: Domo, Qlik, Zenlytic"
echo "  Tier 3: Sisense, DataGPT, Tellius, DataChat"