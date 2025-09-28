# 3waycompare Project Structure

## Clean Project Layout (Post-Cleanup)

```
3waycompare/
├── src/                            # Source code
│   └── main/
│       ├── java/com/scoop/competitive/
│       │   ├── AIComparisonApp.java         # Main entry point
│       │   ├── ai/                          # AI generation logic
│       │   │   ├── AIComparisonGenerator.java
│       │   │   └── PromptTemplateLoader.java
│       │   ├── config/
│       │   │   └── AppConfig.java           # Configuration management
│       │   ├── loader/
│       │   │   └── CompetitorLoader.java    # Load competitor data
│       │   ├── model/                       # Data models
│       │   │   ├── BUAScore.java
│       │   │   ├── Competitor.java
│       │   │   └── ThreeWayComparison.java
│       │   └── writer/
│       │       └── MarkdownWriter.java      # Output generation
│       └── resources/prompts/               # AI prompt templates
│           ├── system_prompt.md             # Cached system context
│           ├── executive_summary.md         # Executive summary
│           ├── bua_dimension_analysis.md    # BUA deep dive
│           ├── capability_comparison.md     # Feature comparison
│           └── faq_generation.md            # FAQ generation
│
├── archive/                        # Archived planning docs
│   ├── AI_POWERED_GENERATION_PLAN.md
│   ├── SETUP_STATUS.md
│   ├── AEO_QUALITY_CHECKLIST.md
│   ├── AEO_SEO_OPTIMIZATION_FRAMEWORK.md
│   ├── THREE_WAY_COMPARISON_TEMPLATE.md
│   ├── THREE_WAY_COMPARISON_FEASIBILITY_ANALYSIS.md
│   └── THREE_WAY_COMPARISON_PROJECT.md
│
├── output/                         # Generated comparisons (empty, cleaned)
├── build.gradle.kts               # Build configuration
├── settings.gradle.kts            # Gradle settings
├── README.md                      # Project documentation
└── PROJECT_STRUCTURE.md          # This file

## File Count Summary
- Java files: 9
- Prompt templates: 5
- Configuration files: 2
- Documentation: 2
- Total active files: 18 (excluding gradle wrapper)

## Key Components

### 1. AIComparisonApp.java (Main Entry)
- Loads competitor data
- Creates ScoopContext with prod config
- Orchestrates AI generation
- Handles fallback to mock generation

### 2. AIComparisonGenerator.java (AI Logic)
- Makes ~11 AI calls per comparison
- Parses JSON responses
- Assembles final document
- Methods for each section type

### 3. PromptTemplateLoader.java (Template Engine)
- Loads prompt templates
- Variable substitution with {variable} syntax
- Caches system prompt

### 4. CompetitorLoader.java (Data Loading)
- Reads BUA scores from ../competitive-intelligence
- Parses framework_scoring.md files
- Loads competitor metadata

### 5. Prompt Templates (AI Instructions)
- Define JSON output contracts
- Include word count requirements
- Provide context and examples
- Guide AI generation

## Dependencies
- Scoop app.jar (AIConnector integration)
- AWS SDK v1 & v2 (for ScoopMetadata)
- MariaDB driver (database access)
- Jackson (JSON parsing)
- Flexmark (Markdown processing)
- SLF4J/Logback (logging)

## Configuration Sources
- Scoop prod config: ../../scoop/app/src/dist/prod/application.properties
- API keys: Embedded in Scoop's ClaudeConnector.java
- Workspace ID: W517 (hardcoded for testing)
- User ID: test-user-3way (hardcoded for testing)

## Generation Process
1. Load competitor BUA scores
2. Initialize ScoopContext with prod config
3. Create AIComparisonGenerator with cached system prompt
4. Generate each section with AI calls:
   - Executive Summary (1 call)
   - BUA Dimensions (5 calls)
   - Capabilities (4 calls)
   - FAQ Section (1 call)
5. Write to output/[name]-ai.md

## Testing Commands
```bash
# Build
./gradlew build

# Run comparison
./gradlew run --args="power-bi-copilot snowflake-cortex"

# Clean
./gradlew clean
```

## Quality Metrics
- Generation time: ~5 minutes
- AI calls: ~11 per comparison
- Output size: ~15-20KB markdown
- Word count compliance: FAQ (40-60), TL;DR (50-58)

## Known Working State (v1.1.0)
- ✅ Connects to Scoop production database
- ✅ Creates valid ScoopContext
- ✅ Successfully calls Claude AI (11 calls per comparison)
- ✅ Parses JSON responses with markdown wrapper handling
- ✅ Handles both string and array responses for bullet points
- ✅ Generates complete comparisons with all sections
- ✅ Writes valid markdown output with populated tables

### Fixed Issues (Sept 28, 2025)
- Executive Summary bullet points (was empty, now populated)
- BUA Framework component tables (was empty, now shows scores)
- Capability sections (was missing, now generates all 5)
- Array response handling (was failing on arrays, now handles both)

## For QA Testing
Focus on:
1. Prompt template quality and instructions
2. JSON parsing reliability
3. Word count compliance in generated content
4. Evidence integration accuracy
5. Competitor data loading correctness
6. Output markdown formatting