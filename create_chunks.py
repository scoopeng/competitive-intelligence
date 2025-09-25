#!/usr/bin/env python3

import os

# Competitors that need CHUNK files
competitors = [
    "snowflake-cortex",
    "sisense",
    "qlik",
    "tellius",
    "zenlytic",
    "datagpt",
    "datachat"
]

# Proper case names for each competitor
proper_names = {
    "snowflake-cortex": "Snowflake Cortex",
    "sisense": "Sisense",
    "qlik": "Qlik",
    "tellius": "Tellius",
    "zenlytic": "Zenlytic",
    "datagpt": "DataGPT",
    "datachat": "DataChat"
}

# Read the template
with open("CHUNK_TEMPLATE.md", "r") as f:
    template = f.read()

# Create CHUNK files for each competitor
for competitor in competitors:
    proper_name = proper_names[competitor]
    competitor_dir = f"competitors/{competitor}"

    # Ensure directory exists
    if not os.path.exists(competitor_dir):
        os.makedirs(competitor_dir)

    # Replace {COMPETITOR} with proper name
    content = template.replace("{COMPETITOR}", proper_name)

    # Split into chunks based on the "---" separator
    chunks = content.split("\n---\n")

    # Extract CHUNK 1 (index 1)
    chunk1 = chunks[1].strip()
    with open(f"{competitor_dir}/CHUNK_1.md", "w") as f:
        f.write(chunk1)

    # Extract CHUNK 2 (index 2)
    chunk2 = chunks[2].strip()
    with open(f"{competitor_dir}/CHUNK_2.md", "w") as f:
        f.write(chunk2)

    # Extract CHUNK 3 (index 3)
    chunk3 = chunks[3].strip()
    with open(f"{competitor_dir}/CHUNK_3.md", "w") as f:
        f.write(chunk3)

    print(f"Created CHUNK files for {proper_name}")

print("\nAll CHUNK files created successfully!")