# AI-Powered Three-Way Comparison Generator

Generates intelligent three-way comparisons (Competitor A vs Competitor B vs Scoop) using Claude AI to create nuanced, evidence-based content that highlights Scoop's business user autonomy advantages.

## Status: ✅ Production Ready v1.1.0
- Successfully calls Claude AI via Scoop's AIConnector
- Generates complete comparisons in ~4-5 minutes
- All sections properly populated (Executive Summary, BUA, Capabilities, FAQ)
- All hard-coded content removed
- Uses production configuration and API keys

### Latest Fixes (v1.1.0)
- ✅ Executive Summary bullet points now populate correctly
- ✅ BUA Framework tables show all component scores
- ✅ Capability Deep Dive sections generate all 5 capabilities
- ✅ Handles both string and array AI responses

## Architecture

```
Competitor Data (BUA scores, evidence)
    ↓
Prompt Templates (structured with variables)
    ↓
AIConnector (Claude/GPT-4 via Scoop integration)
    ↓
Intelligent Content Generation
    ↓
AEO-Optimized Markdown Output
```

## Features

- **AI-Powered Content**: Uses Claude/GPT-4 for intelligent, nuanced generation
- **Prompt Template System**: Structured templates with JSON output contracts
- **BUA Framework Integration**: 100-point scoring across 5 dimensions
- **AEO Optimization**: 40-60 word extractable passages for answer engines
- **Evidence Integration**: Automatically incorporates BUA scores and research
- **Dynamic Emphasis**: Adapts focus based on competitor weaknesses

## Project Structure

```
3waycompare/
├── src/main/
│   ├── java/com/scoop/competitive/
│   │   ├── ai/
│   │   │   ├── AIComparisonGenerator.java  # Main AI orchestrator
│   │   │   └── PromptTemplateLoader.java   # Template handling
│   │   ├── model/                          # Data models
│   │   ├── loader/                         # Competitor data loaders
│   │   ├── writer/                         # Markdown output
│   │   └── AIComparisonApp.java           # Main application
│   └── resources/prompts/
│       ├── system_prompt.md                # Cached system context
│       ├── executive_summary.md            # Executive summary template
│       ├── bua_dimension_analysis.md       # BUA deep dive template
│       ├── faq_generation.md               # FAQ template (40-60 words)
│       └── capability_comparison.md        # Capability analysis template
└── output/                                  # Generated comparisons
```

## Prerequisites

1. **Java 17+** and **Gradle 7+**
2. **Scoop project** built and available at `../scoop`
3. **Competitive intelligence data** at `../competitive-intelligence`
4. **API credentials** configured in Scoop for Claude/GPT-4 access

## Installation

```bash
# Clone if needed
git clone [repository]
cd 3waycompare

# Build the project
./gradlew build

# Ensure scoop project is built
cd ../scoop
./gradlew build
cd ../competitive-intelligence/3waycompare
```

## Usage

### Generate a Comparison

```bash
# Using Gradle
./gradlew run --args="power-bi-copilot snowflake-cortex"

# Or directly with Java (requires classpath setup)
java -cp "build/libs/*:../scoop/build/libs/*" \
     com.scoop.competitive.AIComparisonApp power-bi-copilot snowflake-cortex
```

### Output

Generated comparisons are saved to:
```
output/[competitorA]-vs-[competitorB]-vs-scoop-ai.md
```

## Available Competitors

| Competitor | BUA Score | Category |
|------------|-----------|----------|
| power-bi-copilot | 32/100 | C Weak |
| tableau-pulse | 37/100 | C Weak |
| snowflake-cortex | 26/100 | D Poor |
| domo | 62/100 | B Moderate |
| thoughtspot | 57/100 | B Moderate |
| sisense | 37/100 | C Weak |
| qlik | 47/100 | C Weak |
| tellius | 40/100 | C Weak |
| datagpt | 27/100 | D Poor |
| zenlytic | 42/100 | C Weak |
| datachat | 17/100 | D Poor |

Scoop: **82/100** (A Strong)

## How It Works

1. **Load Competitor Data**: BUA scores, competitive strategy, evidence
2. **Prepare Context**: Fill prompt templates with competitor-specific data
3. **Invoke AI Model**: Send prompts to Claude/GPT-4 via AIConnector
4. **Parse JSON Response**: Extract structured content from AI response
5. **Generate Markdown**: Assemble final comparison document

### Example Prompt Flow

```
System Prompt (cached):
"You are an expert competitive intelligence analyst..."
    +
User Prompt (with variables):
"Generate Executive Summary for {competitorA} vs {competitorB}..."
    ↓
AI Response (JSON):
{
  "markdown": {
    "tldrVerdict": "[50-58 words]",
    "whatIsScoop": "[50-58 words]",
    ...
  }
}
```

## Key Advantages of AI Generation

✅ **Nuanced Understanding**: AI understands subtle relationships between evidence
✅ **Natural Variation**: Each generation is unique, avoiding template fatigue
✅ **Dynamic Emphasis**: Automatically adjusts focus based on competitor weaknesses
✅ **Evidence Weaving**: Naturally incorporates citations into prose
✅ **Scalability**: Easy to add new sections or modify requirements

## Development

### Add New Prompt Templates

1. Create template in `src/main/resources/prompts/`
2. Use `{variable}` syntax for substitution
3. Define JSON output contract
4. Add parsing logic in AIComparisonGenerator

### Modify Generation Logic

Edit `AIComparisonGenerator.java` to:
- Add new sections
- Modify context preparation
- Adjust output parsing

## Troubleshooting

**"AI generator not initialized"**
- Ensure Scoop project is built
- Check API credentials are configured
- Verify ScoopContext initialization

**"Template not found"**
- Check template exists in resources/prompts/
- Verify filename matches exactly

**Word count violations in FAQ**
- AI occasionally misses word count requirements
- Implement retry logic with stricter constraints
- Manual validation recommended

## Future Enhancements

- [ ] Add remaining prompt templates (Cost Analysis, Migration Guide, etc.)
- [ ] Implement retry logic for AEO validation failures
- [ ] Add streaming for real-time progress
- [ ] Create validation suite for output quality
- [ ] Add configuration for model selection (Claude vs GPT-4)
- [ ] Implement prompt caching for efficiency

## License

Proprietary - Scoop Analytics

## Support

For issues or questions, contact the Scoop competitive intelligence team.