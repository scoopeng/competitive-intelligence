# Changelog

All notable changes to the 3waycompare project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2025-01-28

### Added
- AEO/SEO optimization framework with comprehensive assessment
- Question clusters database with 100+ real user queries
- Extractable summary fields (40-60 words) for featured snippets
- AEO validation script (scripts/validate_aeo.py)
- Comprehensive implementation plan aligned with Webflow's AEO Maturity Model

### Changed
- **CRITICAL**: Switched from General to Reasoning model (Claude Opus 4.1) for superior content quality
- Enhanced TL;DR generation with 3-sentence structure
- FAQ generation now uses real user questions instead of generic
- Improved readability targets (<20 words per sentence)
- Updated all prompt templates for AEO compliance

### Improved
- TL;DR word count: 38-42 → 46-51 (targeting 50-58)
- Readability: ~25 → 19 words per sentence
- Question relevance: 0% → 100% real queries
- Content depth with Reasoning model

### Documentation
- Created AEO_SEO_ASSESSMENT.md (1,025 lines)
- Created AEO_SEO_IMPLEMENTATION_PLAN.md v2.0
- Added WEEK_1_COMPLETION_REPORT.md
- Added EXECUTION_SUMMARY.md
- Updated README with v1.2.0 features

## [1.1.0] - 2025-09-28

### Fixed
- Executive Summary sections now properly populated with bullet points
- BUA Framework tables now display component scores correctly
- Capability Deep Dive sections now generate and display all 5 capabilities
- Array handling for AI responses that return bullet points as arrays
- MarkdownWriter now writes all sections including capabilities

### Changed
- AIComparisonGenerator handles both string and array responses for bullet points
- Added dimension names to BUA comparison objects
- Added all capability section generation (Investigation, Excel, Side-by-Side, ML, Workflow)
- MarkdownWriter includes component iteration and capability writing

### Known Issues
- TL;DR word count below target (38 vs 50-58 words)
- Evidence citations remain generic placeholders

### Testing
- Successfully tested with thoughtspot vs domo comparison
- Successfully tested with power-bi-copilot vs tableau-pulse comparison
- Generation time: ~4-5 minutes per comparison

## [1.0.0] - 2025-09-28

### Added
- Initial production-ready release
- AI-powered generation using Claude via Scoop's AIConnector
- Complete integration with Scoop production configuration
- Support for all 11 competitors with BUA scores
- Five prompt templates for different sections
- JSON response parsing with markdown wrapper handling
- Comprehensive documentation and README

### Changed
- Completely removed hard-coded generators (7 files deleted)
- Removed unused models (BattleCard, Evidence, CompetitiveStrategy)
- Migrated from template-based to AI-powered generation
- Updated to use both AWS SDK v1 and v2 for compatibility

### Fixed
- JSON parsing to handle markdown-wrapped responses from Claude
- AWS SDK dependencies for ScoopMetadata initialization
- Production configuration loading from Scoop

### Technical Details
- Generation time: ~5 minutes per comparison
- AI calls: 11 per comparison
- Dependencies: Scoop app.jar, AWS SDK, MariaDB, Jackson
- Java version: 17+
- Gradle version: 8.13

### Architecture
- Main class: AIComparisonApp.java
- AI orchestration: AIComparisonGenerator.java
- Template engine: PromptTemplateLoader.java
- Data loading: CompetitorLoader.java
- Output: MarkdownWriter.java

### Testing
Successfully tested with:
- power-bi-copilot vs snowflake-cortex
- All database connections working
- Claude AI responding correctly
- Complete markdown generation

### Cleanup
- Archived 7 obsolete planning documents
- Removed all build artifacts
- Cleaned output directory
- Total active files: 18 (9 Java, 5 templates, 4 config/docs)