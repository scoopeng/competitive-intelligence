#!/bin/bash

# Generate all three-way comparisons
# Each comparison takes ~6 minutes, 55 total = ~5.5 hours

echo "=================================================="
echo "Starting batch generation of all 3-way comparisons"
echo "Start time: $(date)"
echo "=================================================="

# List of all competitors (excluding scoop)
competitors=(
    "datachat"
    "datagpt"
    "domo"
    "power-bi-copilot"
    "qlik"
    "sisense"
    "snowflake-cortex"
    "tableau-pulse"
    "tellius"
    "thoughtspot"
    "zenlytic"
)

# Counter for progress
count=0
total=55
successful=0
failed=0

# Create output directory if it doesn't exist
mkdir -p output
mkdir -p logs

# Generate all combinations
for ((i=0; i<${#competitors[@]}; i++)); do
    for ((j=i+1; j<${#competitors[@]}; j++)); do
        comp1=${competitors[$i]}
        comp2=${competitors[$j]}
        count=$((count + 1))

        echo ""
        echo "[$count/$total] Generating: $comp1 vs $comp2 vs scoop"
        echo "Progress: $(( count * 100 / total ))%"
        echo "Time: $(date '+%H:%M:%S')"

        # Run generation with timeout (10 minutes max per comparison)
        timeout 600 ./gradlew run --args="$comp1 $comp2" > "logs/${comp1}-vs-${comp2}.log" 2>&1

        if [ $? -eq 0 ]; then
            echo "✅ SUCCESS: $comp1 vs $comp2"
            successful=$((successful + 1))

            # Quick validation
            if [ -f "output/${comp1}-vs-${comp2}-vs-scoop-ai.md" ]; then
                echo "  Output file created successfully"
                # Run validation
                python3 scripts/validate_aeo.py "output/${comp1}-vs-${comp2}-vs-scoop-ai.md" 2>/dev/null | grep -E "✅|❌|⚠️" | head -5
            fi
        else
            echo "❌ FAILED: $comp1 vs $comp2"
            failed=$((failed + 1))
            # Log error
            echo "Failed: $comp1 vs $comp2 at $(date)" >> logs/failures.txt
        fi

        echo "Status: $successful successful, $failed failed, $((total - count)) remaining"
        echo "--------------------------------------------------"
    done
done

echo ""
echo "=================================================="
echo "BATCH GENERATION COMPLETE"
echo "End time: $(date)"
echo "=================================================="
echo "Total attempted: $count"
echo "Successful: $successful"
echo "Failed: $failed"
echo ""

# Generate summary report
echo "Creating summary report..."
cat > generation_report.md << EOF
# Three-Way Comparison Generation Report

## Summary
- **Date**: $(date)
- **Total Comparisons**: $total
- **Successfully Generated**: $successful
- **Failed**: $failed
- **Success Rate**: $(( successful * 100 / total ))%

## Generated Files
EOF

# List all generated files
ls -la output/*.md | awk '{print "- " $9 " (" $5 " bytes)"}' >> generation_report.md

# Add validation summary
echo "" >> generation_report.md
echo "## Validation Summary" >> generation_report.md
for file in output/*-vs-*-vs-scoop-ai.md; do
    if [ -f "$file" ]; then
        echo "" >> generation_report.md
        echo "### $(basename $file)" >> generation_report.md
        python3 scripts/validate_aeo.py "$file" 2>/dev/null | grep -E "✅|❌|⚠️" >> generation_report.md || echo "Validation failed" >> generation_report.md
    fi
done

echo ""
echo "Report saved to generation_report.md"
echo "Logs saved in logs/ directory"
echo ""
echo "All comparisons complete! Enjoy your dinner! 🍽️"