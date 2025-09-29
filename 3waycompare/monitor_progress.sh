#!/bin/bash

echo "=========================================="
echo "3-Way Comparison Generation Monitor"
echo "=========================================="

while true; do
    clear
    echo "=========================================="
    echo "3-Way Comparison Generation Monitor"
    echo "Current Time: $(date)"
    echo "=========================================="
    echo ""

    # Check if process is still running
    if ps -p 994139 > /dev/null; then
        echo "✅ Generation process is RUNNING (PID: 994139)"
    else
        echo "❌ Generation process has STOPPED"
        echo "Check generation_master.log for details"
        break
    fi

    echo ""
    echo "Latest Progress:"
    echo "----------------"
    tail -15 generation_master.log | grep -E "Generating:|SUCCESS:|FAILED:|Status:"

    echo ""
    echo "Files Generated So Far:"
    echo "------------------------"
    generated_count=$(ls -1 output/*-vs-*-vs-scoop-ai.md 2>/dev/null | wc -l)
    echo "✓ Completed: $generated_count / 55 comparisons"
    echo "✓ Progress: $(( generated_count * 100 / 55 ))%"

    if [ $generated_count -gt 0 ]; then
        echo ""
        echo "Latest files:"
        ls -lt output/*-vs-*-vs-scoop-ai.md 2>/dev/null | head -5 | awk '{print "  - " $9}'
    fi

    echo ""
    echo "Resource Usage:"
    echo "---------------"
    ps aux | grep -E "java|gradle" | head -2 | awk '{print "CPU: " $3 "%, MEM: " $4 "%"}'

    echo ""
    echo "Press Ctrl+C to stop monitoring (generation will continue)"
    echo "Refreshing in 30 seconds..."
    sleep 30
done