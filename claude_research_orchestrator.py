#!/usr/bin/env python3
"""
Claude Research Orchestrator - Final Version
Executes 3-chunk research plan per competitor using Claude CLI
"""

import subprocess
import time
import logging
from pathlib import Path
from datetime import datetime
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('research_execution.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).parent
COMPETITORS_DIR = BASE_DIR / "competitors"

class CompetitorResearcher:
    """Orchestrates Claude CLI to execute 3-chunk research plan"""

    def __init__(self):
        self.chunks = ["CHUNK_1.md", "CHUNK_2.md", "CHUNK_3.md"]

    def execute_chunk(self, competitor: str, chunk_file: str) -> bool:
        """Execute one research chunk using Claude CLI"""

        comp_dir = COMPETITORS_DIR / competitor
        chunk_path = comp_dir / chunk_file

        if not chunk_path.exists():
            logger.error(f"Chunk file not found: {chunk_path}")
            return False

        # Build the prompt for Claude
        prompt = f"""Read {chunk_file} in the current directory.
Execute ALL instructions in that file.
Use WebSearch and WebFetch as instructed.
Save all outputs as specified.
When complete, output only: 'CHUNK COMPLETE'"""

        logger.info(f"[{competitor}] Executing {chunk_file}")

        try:
            # Execute via Claude CLI with long timeout
            cmd = f'echo "{prompt}" | claude --print --allowedTools "Read,Write,WebSearch,WebFetch,Edit"'

            result = subprocess.run(
                cmd,
                shell=True,
                cwd=comp_dir,
                capture_output=True,
                text=True,
                timeout=1800  # 30 minutes per chunk
            )

            if result.returncode == 0 and "CHUNK COMPLETE" in result.stdout:
                logger.info(f"[{competitor}] {chunk_file} completed successfully")
                return True
            else:
                logger.error(f"[{competitor}] {chunk_file} failed")
                if result.stderr:
                    logger.error(f"Error: {result.stderr[:500]}")
                return False

        except subprocess.TimeoutExpired:
            logger.error(f"[{competitor}] {chunk_file} timed out after 30 minutes")
            return False
        except Exception as e:
            logger.error(f"[{competitor}] Error: {str(e)}")
            return False

    def research_competitor(self, competitor: str) -> bool:
        """Execute all 3 chunks for a competitor"""

        logger.info(f"\n{'='*60}")
        logger.info(f"Researching: {competitor}")
        logger.info(f"{'='*60}")

        comp_dir = COMPETITORS_DIR / competitor
        if not comp_dir.exists():
            logger.error(f"Competitor directory not found: {comp_dir}")
            return False

        # Check that all chunk files exist
        for chunk in self.chunks:
            if not (comp_dir / chunk).exists():
                logger.error(f"Missing chunk file: {chunk}")
                return False

        # Execute each chunk
        for i, chunk in enumerate(self.chunks, 1):
            logger.info(f"Starting Chunk {i}/3: {chunk}")

            success = self.execute_chunk(competitor, chunk)

            if not success:
                logger.error(f"Chunk {i} failed. Stopping research for {competitor}")
                return False

            # Pause between chunks
            if i < len(self.chunks):
                logger.info("Pausing 30 seconds before next chunk...")
                time.sleep(30)

        logger.info(f"✅ Completed research for {competitor}")
        return True

    def run(self, competitor: str = None):
        """Main execution"""

        logger.info("="*60)
        logger.info("CLAUDE RESEARCH ORCHESTRATOR")
        logger.info("="*60)

        if competitor:
            competitors = [competitor]
        else:
            # Find all competitors with chunk files
            competitors = []
            for comp_dir in COMPETITORS_DIR.iterdir():
                if comp_dir.is_dir() and (comp_dir / "CHUNK_1.md").exists():
                    competitors.append(comp_dir.name)

        if not competitors:
            logger.error("No competitors found with CHUNK files")
            return 1

        logger.info(f"Found {len(competitors)} competitor(s) to research")

        for comp in competitors:
            success = self.research_competitor(comp)

            if not success:
                logger.warning(f"Research failed for {comp}")

        logger.info("\n" + "="*60)
        logger.info("RESEARCH COMPLETE")
        logger.info("Check competitors/[name]/research/ for findings")
        logger.info("="*60)

        return 0

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Orchestrate Claude CLI research')
    parser.add_argument('--competitor', '-c', help='Specific competitor to research')

    args = parser.parse_args()

    researcher = CompetitorResearcher()
    return researcher.run(competitor=args.competitor)

if __name__ == "__main__":
    sys.exit(main())