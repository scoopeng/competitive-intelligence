#!/bin/bash
# Test script to check if AI is returning extractableSummary

echo "Testing extractableSummary generation..."

# Build the project
./gradlew build

# Run a test generation with debug output
./gradlew run --args="thoughtspot tellius" 2>&1 | tee test_summary.log

# Check for extractableSummary in the response
echo ""
echo "Checking for extractableSummary in AI responses..."
grep -i "extractable" test_summary.log | head -10

echo ""
echo "Done. Check test_summary.log for full output."