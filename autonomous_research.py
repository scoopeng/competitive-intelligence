#!/usr/bin/env python3
"""
Autonomous research executor
- Creates chunks for competitors that don't have them
- Executes all competitors in priority order
- Tracks progress and can resume
"""

import subprocess
import json
import time
from pathlib import Path
from datetime import datetime
import shutil

class AutonomousResearcher:
    def __init__(self):
        self.base_dir = Path.cwd()
        self.template_path = self.base_dir / "CHUNK_TEMPLATE.md"
        self.tracker_path = self.base_dir / "RESEARCH_TRACKER.json"
        self.priority_order = [
            "tableau-pulse",
            "power-bi-copilot",
            "thoughtspot",
            "domo",
            "snowflake-cortex",
            "sisense",
            "qlik",
            "tellius",
            "zenlytic",
            "datagpt",
            "datachat"
        ]
        self.load_progress()

    def load_progress(self):
        """Load or initialize progress tracking"""
        if self.tracker_path.exists():
            with open(self.tracker_path, 'r') as f:
                self.progress = json.load(f)
        else:
            self.progress = {comp: {"chunks_created": False, "completed": []}
                           for comp in self.priority_order}
            self.save_progress()

    def save_progress(self):
        """Save progress to file"""
        with open(self.tracker_path, 'w') as f:
            json.dump(self.progress, f, indent=2)

    def create_chunks_for_competitor(self, competitor):
        """Generate chunk files from template"""
        comp_dir = self.base_dir / "competitors" / competitor

        # Check if chunks already exist
        if (comp_dir / "CHUNK_1.md").exists():
            print(f"✅ {competitor} already has chunks")
            self.progress[competitor]["chunks_created"] = True
            return True

        print(f"📝 Creating chunks for {competitor}")

        # Read template
        with open(self.template_path, 'r') as f:
            template = f.read()

        # Split template into 3 chunks (it has all 3 in one file)
        chunks = template.split("---\n\n# CHUNK")

        # Process and save each chunk
        for i, chunk_content in enumerate(chunks):
            if i == 0:
                # First chunk doesn't have "CHUNK" prefix
                chunk_text = chunk_content.split("# CHUNK 1:")[1]
                chunk_text = "# CHUNK 1:" + chunk_text.split("---")[0]
            else:
                chunk_num = i + 1
                chunk_text = f"# CHUNK {chunk_num}:" + chunk_content.split(f"# CHUNK {chunk_num + 1}:")[0] if f"# CHUNK {chunk_num + 1}:" in chunk_content else f"# CHUNK {chunk_num}:" + chunk_content

            # Replace {COMPETITOR} placeholder with actual name
            chunk_text = chunk_text.replace("{COMPETITOR}", competitor.replace("-", " ").title())

            # Write chunk file
            chunk_path = comp_dir / f"CHUNK_{i + 1}.md"
            with open(chunk_path, 'w') as f:
                f.write(chunk_text.strip())

            print(f"  Created CHUNK_{i + 1}.md")

        self.progress[competitor]["chunks_created"] = True
        self.save_progress()
        return True

    def execute_chunk(self, competitor, chunk_num):
        """Execute a single chunk via Claude CLI"""
        comp_dir = self.base_dir / "competitors" / competitor
        chunk_file = comp_dir / f"CHUNK_{chunk_num}.md"

        if not chunk_file.exists():
            print(f"❌ {chunk_file} not found")
            return False

        # Check if already completed
        if f"chunk_{chunk_num}" in self.progress[competitor]["completed"]:
            print(f"✓ Chunk {chunk_num} already completed")
            return True

        print(f"\n  Executing Chunk {chunk_num}...")

        prompt = f"""
        Read CHUNK_{chunk_num}.md in this directory.
        Execute ALL searches and tasks listed.
        Save outputs to specified files.
        Follow success criteria exactly.
        Mark completion in progress.md
        """

        cmd = ['claude', '--print', prompt.strip()]

        try:
            result = subprocess.run(
                cmd,
                cwd=comp_dir,
                capture_output=True,
                text=True,
                timeout=2400  # 40 minutes
            )

            if result.returncode == 0:
                print(f"  ✅ Chunk {chunk_num} completed")
                self.progress[competitor]["completed"].append(f"chunk_{chunk_num}")
                self.save_progress()
                time.sleep(30)  # Pause between chunks
                return True
            else:
                print(f"  ❌ Chunk {chunk_num} failed")
                return False

        except subprocess.TimeoutExpired:
            print(f"  ⏱️ Chunk {chunk_num} timed out")
            return False
        except FileNotFoundError:
            print(f"  ❌ Claude CLI not found - falling back to manual execution")
            print(f"  Please manually execute: {chunk_file}")
            return False

    def research_competitor(self, competitor):
        """Full research flow for one competitor"""
        print(f"\n{'='*60}")
        print(f"RESEARCHING: {competitor}")
        print(f"{'='*60}")

        # Create chunks if needed
        if not self.progress[competitor]["chunks_created"]:
            if not self.create_chunks_for_competitor(competitor):
                return False

        # Execute all 3 chunks
        success = True
        for chunk_num in [1, 2, 3]:
            if not self.execute_chunk(competitor, chunk_num):
                print(f"⚠️ Stopping {competitor} at chunk {chunk_num}")
                success = False
                break

        if success:
            print(f"🎉 Completed all chunks for {competitor}")
            self.progress[competitor]["completed"].append("all_chunks")
            self.save_progress()

        return success

    def run_all(self, start_from=None):
        """Run research for all competitors"""
        print("="*70)
        print("AUTONOMOUS RESEARCH EXECUTOR")
        print("="*70)
        print(f"Starting at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        start_index = 0
        if start_from:
            try:
                start_index = self.priority_order.index(start_from)
            except ValueError:
                print(f"Warning: {start_from} not found, starting from beginning")

        completed_count = 0
        failed_competitors = []

        for competitor in self.priority_order[start_index:]:
            # Skip if already completed
            if "all_chunks" in self.progress.get(competitor, {}).get("completed", []):
                print(f"\n✓ Skipping {competitor} (already complete)")
                completed_count += 1
                continue

            # Research this competitor
            if self.research_competitor(competitor):
                completed_count += 1
            else:
                failed_competitors.append(competitor)
                # Continue with next competitor even if this one failed

        # Final report
        print("\n" + "="*70)
        print("RESEARCH COMPLETE")
        print(f"Completed: {completed_count}/{len(self.priority_order)}")
        if failed_competitors:
            print(f"Failed: {', '.join(failed_competitors)}")
        print(f"Ended at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*70)

def main():
    import sys

    researcher = AutonomousResearcher()

    if len(sys.argv) > 1:
        if sys.argv[1] == "--all":
            researcher.run_all()
        elif sys.argv[1] == "--resume":
            # Find first incomplete and start from there
            for comp in researcher.priority_order:
                if "all_chunks" not in researcher.progress[comp]["completed"]:
                    print(f"Resuming from: {comp}")
                    researcher.run_all(start_from=comp)
                    break
        else:
            # Run specific competitor
            researcher.research_competitor(sys.argv[1])
    else:
        print("Autonomous Research Executor")
        print("\nUsage:")
        print("  python3 autonomous_research.py --all        # Run all competitors")
        print("  python3 autonomous_research.py --resume     # Resume from last failure")
        print("  python3 autonomous_research.py <name>       # Run specific competitor")
        print("\nWill create chunks automatically for competitors that lack them.")

if __name__ == "__main__":
    main()