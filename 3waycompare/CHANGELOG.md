# Changelog

All notable changes to the 3waycompare project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2025-01-28 - AEO/SEO Complete Implementation

### 🎉 Major Achievement
**Grade: A (from C+)** - Complete AEO/SEO stack implemented for featured snippet capture

### Added
- **Evidence Database** (evidence_database.json) with real sources for 12 competitors
- **Schema Markup Generator** (SchemaGenerator.java) - FAQ, Product, Software, Breadcrumb
- **Evidence Loader** (EvidenceLoader.java) - Replaces placeholder citations
- **Question Clusters Database** with 100+ real user queries (5 categories)
- **Extractable Summaries** - 40-60 word blocks after each dimension
- **AEO Validation Script** (scripts/validate_aeo.py) - Comprehensive compliance checking
- **TCO Framework** - Cost category elimination messaging (replaces pricing claims)

### Changed
- **CRITICAL**: Switched from ModelUseCase.General to ModelUseCase.Reasoning (Claude Opus 4.1)
- **TL;DR Structure**: 3-sentence format achieving consistent 50-52 words
- **FAQ Generation**: Real questions replacing generic (100% improvement)
- **Java Model**: Added extractableSummary field to DimensionComparison
- **All Prompt Templates**: Enhanced for AEO compliance and word targets

### Fixed
- TL;DR word count: 38-42 → **50-52 words** (perfect target achievement)
- Readability: ~25 → **18-19 words/sentence** (exceeds <20 target)
- Question relevance: 0% → **100% real queries**
- Extractable summaries: 0 → **5 per document** (all 40-60 words)
- Evidence citations: placeholders → **real sources with dates**

### Performance Metrics
| Metric | Before | After | Target | Status |
|--------|--------|-------|--------|--------|
| TL;DR Words | 38-42 | 50-52 | 50-58 | ✅ |
| Readability | ~25 w/s | 18-19 w/s | <20 | ✅ |
| Summaries | 0 | 5 | 5 | ✅ |
| Real Questions | 0% | 100% | 100% | ✅ |
| Schema Types | 0 | 4 | 4+ | ✅ |

### Documentation
- Created AEO_SEO_ASSESSMENT.md (1,025 lines comprehensive analysis)
- Created AEO_SEO_IMPLEMENTATION_PLAN.md v2.0 (4-week roadmap)
- Created AEO_IMPLEMENTATION_COMPLETE.md (final achievement summary)
- Added WEEK_1_COMPLETION_REPORT.md (TL;DR + questions)
- Added WEEK_2_COMPLETION_REPORT.md (summaries + evidence + schema)
- Updated README to v1.2.0 with complete feature list

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