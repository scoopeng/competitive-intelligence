#!/usr/bin/env python3
"""
Simple research runner - executes chunks in Claude CLI
Minimal orchestration, Claude does the real work
"""

import subprocess
import sys
import time
from pathlib import Path

def run_chunk(competitor, chunk_num):
    """Execute a single chunk via Claude CLI"""
    chunk_file = f"competitors/{competitor}/CHUNK_{chunk_num}.md"

    if not Path(chunk_file).exists():
        print(f"❌ {chunk_file} not found")
        return False

    print(f"\n{'='*60}")
    print(f"Executing {competitor} - Chunk {chunk_num}")
    print(f"{'='*60}")

    # Simple prompt that tells Claude to execute the chunk
    prompt = f"""
    Read the file CHUNK_{chunk_num}.md in this directory.
    Execute ALL the searches and tasks listed.
    Save all outputs to the specified files.
    Follow the success criteria exactly.
    When complete, write 'CHUNK_{chunk_num}_COMPLETE' to progress.md
    """

    cmd = ['claude', '--print', prompt.strip()]

    try:
        result = subprocess.run(
            cmd,
            cwd=f"competitors/{competitor}",
            capture_output=True,
            text=True,
            timeout=2400  # 40 minutes per chunk
        )

        if result.returncode == 0:
            print(f"✅ Chunk {chunk_num} executed")
            # Small pause between chunks
            if chunk_num < 3:
                print("Pausing 30 seconds before next chunk...")
                time.sleep(30)
            return True
        else:
            print(f"❌ Chunk {chunk_num} failed")
            if result.stderr:
                print(f"Error: {result.stderr[:500]}")
            return False

    except subprocess.TimeoutExpired:
        print(f"⏱️ Chunk {chunk_num} timed out after 40 minutes")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def run_competitor(competitor):
    """Run all 3 chunks for a competitor"""
    print(f"\n{'='*70}")
    print(f"RESEARCHING: {competitor}")
    print(f"{'='*70}")

    success_count = 0
    for chunk_num in [1, 2, 3]:
        if run_chunk(competitor, chunk_num):
            success_count += 1
        else:
            print(f"⚠️ Stopping {competitor} due to chunk failure")
            break

    print(f"\n📊 Completed {success_count}/3 chunks for {competitor}")
    return success_count == 3

def main():
    """Main execution"""
    if len(sys.argv) > 1:
        competitor = sys.argv[1]
        success = run_competitor(competitor)
        return 0 if success else 1
    else:
        print("Usage: python3 run_research.py <competitor-name>")
        print("\nAvailable competitors with chunks:")
        print("  - tableau-pulse")
        print("  - power-bi-copilot")
        return 1

if __name__ == "__main__":
    sys.exit(main())