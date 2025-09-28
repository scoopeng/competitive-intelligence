# Changelog

All notable changes to the 3waycompare project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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