#!/usr/bin/env python3

import os
import re

# Competitors to update
competitors_to_update = [
    "tableau-pulse",
    "power-bi-copilot",
    "thoughtspot",
    "domo"
]

# Updates to make
updates = {
    "chunk1_search": {
        "old": "**For each search**: Read full reviews, extract specific quotes with company size/industry context",
        "new": """**For each search**:
1. Document URL, date accessed, and key findings in research library
2. Extract specific quotes with company size/industry context
3. Rate source credibility (High/Medium/Low)"""
    },
    "chunk1_output": {
        "old": """## OUTPUT FILES
- `research/customer_stories.md` - Implementation experiences
- `research/industry_analysis.md` - Vertical-specific limitations
- `evidence/customer_quotes.md` - Direct quotes with context
- `evidence/community_sources.md` - Forum/Reddit findings""",
        "new": """## OUTPUT FILES
- `research/customer_stories.md` - Implementation experiences
- `research/industry_analysis.md` - Vertical-specific limitations
- `evidence/customer_quotes.md` - Direct quotes with context
- `evidence/community_sources.md` - Forum/Reddit findings
- `evidence/research_library_chunk1.md` - Complete library of all URLs investigated with summaries"""
    },
    "chunk2_output": {
        "old": """## OUTPUT FILES
- `research/performance_analysis.md` - Quantified limitations
- `research/competitive_positioning.md` - Market context
- `research/integration_reality.md` - Technical limitations
- `research/economic_impact.md` - True TCO analysis""",
        "new": """## OUTPUT FILES
- `research/performance_analysis.md` - Quantified limitations
- `research/competitive_positioning.md` - Market context
- `research/integration_reality.md` - Technical limitations
- `research/economic_impact.md` - True TCO analysis
- `evidence/research_library_chunk2.md` - Complete library of all URLs investigated with summaries"""
    }
}

# Process each competitor
for competitor in competitors_to_update:

    # Update CHUNK_1.md
    chunk1_path = f"competitors/{competitor}/CHUNK_1.md"
    if os.path.exists(chunk1_path):
        with open(chunk1_path, "r") as f:
            content = f.read()

        # Apply updates
        if updates["chunk1_search"]["old"] in content:
            content = content.replace(updates["chunk1_search"]["old"], updates["chunk1_search"]["new"])

        if updates["chunk1_output"]["old"] in content:
            content = content.replace(updates["chunk1_output"]["old"], updates["chunk1_output"]["new"])

        with open(chunk1_path, "w") as f:
            f.write(content)
        print(f"Updated {chunk1_path}")

    # Update CHUNK_2.md
    chunk2_path = f"competitors/{competitor}/CHUNK_2.md"
    if os.path.exists(chunk2_path):
        with open(chunk2_path, "r") as f:
            content = f.read()

        # Apply updates
        if updates["chunk2_output"]["old"] in content:
            content = content.replace(updates["chunk2_output"]["old"], updates["chunk2_output"]["new"])

        with open(chunk2_path, "w") as f:
            f.write(content)
        print(f"Updated {chunk2_path}")

print("\nAll existing CHUNK files updated with research library tracking!")