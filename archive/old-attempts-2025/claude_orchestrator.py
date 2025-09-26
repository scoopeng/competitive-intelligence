#!/usr/bin/env python3
"""
Claude Orchestrator - Directs Claude Code to do actual research
Each step calls Claude as if it's a new chat, but state is preserved via files
"""

import subprocess
import json
import time
import logging
from pathlib import Path
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('claude_orchestrator.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).parent
COMPETITORS_DIR = BASE_DIR / "competitors"

class ClaudeOrchestrator:
    """Orchestrates Claude Code to do real research"""

    def __init__(self):
        self.current_competitor = None
        self.current_step = 0
        self.session_count = 0

    def get_competitors_with_plans(self):
        """Find competitors that have RESEARCH_PLAN.md"""
        competitors = []
        for comp_dir in COMPETITORS_DIR.iterdir():
            if comp_dir.is_dir():
                plan_file = comp_dir / "RESEARCH_PLAN.md"
                if plan_file.exists():
                    competitors.append(comp_dir.name)
        return sorted(competitors)

    def read_current_state(self, competitor):
        """Read the current state from competitor's files"""
        comp_dir = COMPETITORS_DIR / competitor

        # Read TODO to get current task
        todo_file = comp_dir / "TODO.md"
        if todo_file.exists():
            with open(todo_file) as f:
                todo_content = f.read()
        else:
            todo_content = "No TODO found"

        # Read plan to get progress
        plan_file = comp_dir / "RESEARCH_PLAN.md"
        if plan_file.exists():
            with open(plan_file) as f:
                plan_content = f.read()
                # Extract current step number
                for line in plan_content.split('\n'):
                    if 'Current Step:' in line:
                        try:
                            self.current_step = int(line.split(':')[1].strip())
                        except:
                            self.current_step = 0

        return {
            "competitor": competitor,
            "current_step": self.current_step,
            "todo": todo_content,
            "plan_exists": plan_file.exists()
        }

    def create_claude_prompt(self, state):
        """Create prompt for Claude to execute current task"""
        prompt = f"""You are doing competitive intelligence research.

CURRENT COMPETITOR: {state['competitor']}
CURRENT STEP: {state['current_step']}

YOUR TASK (from TODO.md):
{state['todo']}

INSTRUCTIONS:
1. Read the files in competitors/{state['competitor']}/ to understand context
2. Execute the research task described in TODO.md using WebSearch/WebFetch
3. Save your findings in the appropriate files
4. Update RESEARCH_PLAN.md to mark the task complete
5. Update TODO.md with the next task
6. Be thorough - gather REAL evidence with sources

Start by reading RESEARCH_PLAN.md to understand the full context, then execute your current task."""

        return prompt

    def call_claude(self, prompt, competitor):
        """
        This is where we'd call Claude Code API
        For now, this is a placeholder showing what would happen
        """
        logger.info(f"[{competitor}] Calling Claude with task...")
        logger.info(f"Prompt preview: {prompt[:200]}...")

        # In production, this would:
        # 1. Call Claude Code API with the prompt
        # 2. Claude would read files, do research, save results
        # 3. Return success/failure status

        # For now, create a marker file to show we tried
        marker_file = COMPETITORS_DIR / competitor / f"claude_session_{self.session_count}.txt"
        with open(marker_file, 'w') as f:
            f.write(f"Session {self.session_count}\n")
            f.write(f"Time: {datetime.now().isoformat()}\n")
            f.write(f"Task: Step {self.current_step}\n")
            f.write(f"Prompt:\n{prompt}\n")

        self.session_count += 1

        # Simulate processing time
        time.sleep(2)

        return True

    def check_completion(self, competitor):
        """Check if all tasks are complete for this competitor"""
        plan_file = COMPETITORS_DIR / competitor / "RESEARCH_PLAN.md"
        if plan_file.exists():
            with open(plan_file) as f:
                content = f.read()
                # Simple check - if we've done 50 steps, we're done
                return "Current Step: 50" in content or "Completion: 100%" in content
        return False

    def process_competitor(self, competitor, max_steps=5):
        """Process research for one competitor"""
        logger.info(f"\n{'='*60}")
        logger.info(f"Processing: {competitor}")
        logger.info(f"{'='*60}")

        steps_completed = 0

        while steps_completed < max_steps:
            # Read current state
            state = self.read_current_state(competitor)

            if not state['plan_exists']:
                logger.warning(f"No RESEARCH_PLAN.md found for {competitor}")
                break

            # Check if done
            if self.check_completion(competitor):
                logger.info(f"✅ {competitor} research complete!")
                break

            # Create prompt for Claude
            prompt = self.create_claude_prompt(state)

            # Call Claude to do the work
            logger.info(f"Step {state['current_step'] + 1}: Calling Claude...")
            success = self.call_claude(prompt, competitor)

            if not success:
                logger.error(f"Claude execution failed for {competitor}")
                break

            steps_completed += 1
            logger.info(f"Completed step {state['current_step'] + 1}")

            # Small delay between steps
            time.sleep(1)

        logger.info(f"Completed {steps_completed} steps for {competitor}")
        return steps_completed

    def run(self, specific_competitor=None, max_steps_per_competitor=5):
        """Main orchestration loop"""
        logger.info("="*60)
        logger.info("CLAUDE ORCHESTRATOR - Real Research Automation")
        logger.info("="*60)

        if specific_competitor:
            competitors = [specific_competitor]
        else:
            competitors = self.get_competitors_with_plans()

        if not competitors:
            logger.error("No competitors found with RESEARCH_PLAN.md")
            return

        logger.info(f"Found {len(competitors)} competitors to research")
        logger.info(f"Will execute up to {max_steps_per_competitor} steps per competitor")

        total_steps = 0

        for competitor in competitors:
            steps = self.process_competitor(competitor, max_steps_per_competitor)
            total_steps += steps

            # Delay between competitors
            if competitors.index(competitor) < len(competitors) - 1:
                logger.info("Pausing before next competitor...")
                time.sleep(2)

        logger.info(f"\n{'='*60}")
        logger.info(f"COMPLETE: Executed {total_steps} total research steps")
        logger.info(f"Check each competitor's folder for results")
        logger.info(f"Log saved to: claude_orchestrator.log")
        logger.info(f"{'='*60}")

def main():
    """Run the orchestrator"""
    import argparse

    parser = argparse.ArgumentParser(description='Orchestrate Claude for competitor research')
    parser.add_argument('--competitor', help='Specific competitor to research')
    parser.add_argument('--steps', type=int, default=5, help='Max steps per competitor')

    args = parser.parse_args()

    orchestrator = ClaudeOrchestrator()
    orchestrator.run(
        specific_competitor=args.competitor,
        max_steps_per_competitor=args.steps
    )

if __name__ == "__main__":
    main()