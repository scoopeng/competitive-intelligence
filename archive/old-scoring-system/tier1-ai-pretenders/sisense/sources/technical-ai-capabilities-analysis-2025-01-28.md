# Sisense AI Technical Capabilities - Deep Analysis
**URL**: Multiple technical sources (Sisense docs, blog, whitepapers)
**Type**: Technical Documentation Analysis
**Date Accessed**: 2025-01-28

## Key Findings Summary
Sisense has SOME real ML capabilities (ARIMA forecasting, basic clustering) but they're limited, basic, and mostly rely on sending data to Sisense's cloud for processing. The heavy emphasis on "AI-agnostic architecture" and integration with external tools reveals they don't have deep ML capabilities built-in. Classic augmented analytics, not true AI platform.

## Detailed Technical Analysis

### Actual ML Algorithms Found

**Time Series Forecasting**:
- Uses ARIMA/SARIMA algorithms (1970s statistics, not modern ML)
- Grid search for hyperparameters (basic optimization)
- Must send data to Sisense Cloud Service for processing
- Limited to time-series visualizations only

**Clustering**:
- Basic clustering algorithms mentioned (no specifics)
- Described as "particularly valuable for business analysts to quickly visualize patterns"
- No mention of which algorithms (K-means? DBSCAN? Hierarchical?)

**Statistical Analysis**:
- "Exponential smoothing and local estimates" for trend lines
- These are statistical methods, not machine learning
- Pointwise Mutual Information for "associations" (correlation, not causation)

### Architecture Red Flags

**Cloud Dependency**:
> "Historical data selected by a user is sent to the Sisense Cloud Service, where it's processed by machine-learning algorithms"

**Translation**: Your data leaves your environment for basic ML

**"AI-Agnostic" Admission**:
> "Sisense is designed to enable you to effortlessly connect to a spectrum of AI and Data Science/Machine Learning tools, including LLMs, through its powerful, AI-agnostic architecture"

**Translation**: We don't have much ML built-in, so integrate your own

### Limited Scope of "AI"

**What They Actually Offer**:
1. Basic time-series forecasting (ARIMA)
2. Simple clustering for visualization
3. Statistical trend lines
4. Integration points for external ML

**What's Missing** (vs Real ML Platforms):
- No deep learning models
- No classification algorithms
- No anomaly detection
- No root cause analysis
- No multi-hypothesis testing
- No investigation engine
- No predictive modeling beyond time-series

### Generative AI Claims

**Vague LLM Integration**:
> "emergence of Generative AI...has further elevated the potential...by harnessing the power of Large Language Models"

**Reality**: They added ChatGPT-style natural language queries, not analytical ML

### Custom Code Workaround

**DIY ML Option**:
> "Using Custom Code Notebooks, a user can define their input parameters...and train their machine learning model"

**Translation**: If you want real ML, code it yourself in notebooks

### Comparison to Marketing Claims

**They Claim**: "AI-powered analytics platform"
**Reality**: Basic statistical forecasting + chat interface

**They Claim**: "Predictive analytics"
**Reality**: Only time-series forecasting with 50-year-old algorithms

**They Claim**: "Uncover patterns"
**Reality**: Basic clustering and correlation, not causal analysis

### Technical Limitations Exposed
1. Must send data to cloud for "ML" processing
2. Limited to visualization-based analytics
3. No native advanced ML algorithms
4. Relies on external tools for real AI
5. Forecasting only works on time-series data
6. No investigation or reasoning capabilities

### Evidence Summary
- Documentation focuses on integration, not native ML
- Algorithms mentioned are basic statistics
- Heavy reliance on third-party tools
- Cloud processing for simple operations
- No evidence of proprietary ML models
- "AI-agnostic" = "AI-light"

### Cross-Reference Notes
- Confirms Tier 1 classification: Augmented BI, not AI
- Similar to Qlik: Statistical features marketed as "AI"
- Unlike ThoughtSpot/Tellius: Those have real ML engines
- Pattern matches Power BI Copilot: Chat + basic analytics = "AI"