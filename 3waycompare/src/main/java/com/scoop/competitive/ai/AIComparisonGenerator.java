package com.scoop.competitive.ai;

import scoop.ai.aiconnector.AIConnector;
import scoop.ai.aiconnector.ModelUseCase;
import com.scoop.competitive.config.AppConfig;
import com.scoop.competitive.model.*;
import scoop.ScoopException;
import scoop.ScoopContext;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.JsonNode;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;
import java.util.stream.Collectors;

/**
 * AI-powered comparison generator using Claude/GPT-4 via AIConnector.
 *
 * This class orchestrates the generation of three-way comparisons by:
 * 1. Loading competitor data and BUA scores
 * 2. Preparing context for prompt templates
 * 3. Making multiple AI calls (typically 11 calls total)
 * 4. Parsing JSON responses and assembling the final document
 *
 * Each comparison takes approximately 5 minutes to generate and includes:
 * - Executive Summary with TL;DR (50-58 words)
 * - BUA Framework Deep Dive (5 dimensions)
 * - Capability Comparisons (4 sections)
 * - FAQ Section (40-60 words per answer for AEO)
 *
 * @author Scoop Competitive Intelligence Team
 * @version 1.0
 */
public class AIComparisonGenerator {
    private static final Logger logger = LoggerFactory.getLogger(AIComparisonGenerator.class);

    private final AIConnector aiConnector;
    private final PromptTemplateLoader templateLoader;
    private final ObjectMapper objectMapper;
    private final String cachedSystemPrompt;

    /**
     * Initialize the AI comparison generator.
     *
     * @param scoopContext The ScoopContext with database and API configuration
     * @throws IOException if prompt templates cannot be loaded
     */
    public AIComparisonGenerator(ScoopContext scoopContext) throws IOException {
        this.aiConnector = AIConnector.getAIConnector(scoopContext, ModelUseCase.General);
        this.templateLoader = new PromptTemplateLoader();
        this.objectMapper = new ObjectMapper();
        
        // Load and cache the system prompt
        this.cachedSystemPrompt = templateLoader.loadTemplate("system_prompt.md");
        logger.info("Initialized AIComparisonGenerator with cached system prompt");
    }
    
    /**
     * Generate complete three-way comparison using AI.
     *
     * Makes approximately 11 AI calls:
     * - 1 for Executive Summary
     * - 5 for BUA dimensions (Autonomy, Flow, Understanding, Presentation, Data)
     * - 4 for Capability sections (Investigation, Spreadsheet, Mobile, Cost)
     * - 1 for FAQ generation
     *
     * @param competitorA First competitor to compare
     * @param competitorB Second competitor to compare
     * @return Complete three-way comparison document
     * @throws IOException if template loading fails
     * @throws ScoopException if AI calls fail
     */
    public ThreeWayComparison generateComparison(Competitor competitorA, Competitor competitorB)
            throws IOException, ScoopException {
        
        logger.info("Generating AI-powered comparison: {} vs {} vs Scoop", 
                   competitorA.getName(), competitorB.getName());
        
        ThreeWayComparison comparison = new ThreeWayComparison();
        
        // Set basic metadata
        comparison.setCompetitorA(competitorA);
        comparison.setCompetitorB(competitorB);
        comparison.setTitle(String.format("%s vs %s vs Scoop: Complete Comparison",
                                         competitorA.getName(), competitorB.getName()));
        comparison.setSlug(String.format("%s-vs-%s-vs-scoop",
                                        competitorA.getSlug(), competitorB.getSlug()));
        
        // Generate each section with AI
        comparison.setExecutiveSummary(generateExecutiveSummary(competitorA, competitorB));
        comparison.setAtAGlanceMatrix(generateAtAGlanceMatrix(competitorA, competitorB));
        comparison.setBuaDeepDive(generateBUADeepDive(competitorA, competitorB));
        comparison.setCapabilityDeepDive(generateCapabilityDeepDive(competitorA, competitorB));
        comparison.setFaqSection(generateFAQs(competitorA, competitorB));
        
        // Generate schemas
        comparison.setFaqPageSchema(generateFAQSchema(comparison.getFaqSection()));
        
        logger.info("Successfully generated AI comparison");
        return comparison;
    }
    
    /**
     * Generate Executive Summary section using AI.
     */
    private ThreeWayComparison.ExecutiveSummary generateExecutiveSummary(
            Competitor competitorA, Competitor competitorB) throws IOException, ScoopException {
        
        // Prepare context variables
        Map<String, Object> context = new HashMap<>();
        context.put("competitorA", competitorA.getName());
        context.put("competitorB", competitorB.getName());
        context.put("aScore", competitorA.getBuaScore().getTotalScore());
        context.put("bScore", competitorB.getBuaScore().getTotalScore());
        context.put("aCategory", competitorA.getBuaScore().getCategory());
        context.put("bCategory", competitorB.getBuaScore().getCategory());
        context.put("aWeaknesses", extractWeaknesses(competitorA));
        context.put("bWeaknesses", extractWeaknesses(competitorB));
        context.put("aEvidence", gatherEvidence(competitorA));
        context.put("bEvidence", gatherEvidence(competitorB));
        
        // Load and fill template
        String template = templateLoader.loadTemplate("executive_summary.md");
        String prompt = templateLoader.fillTemplate(template, context);
        
        // Invoke AI model
        String response = aiConnector.invokeModel(cachedSystemPrompt, prompt);

        // Parse JSON response using AIConnector's built-in method
        JsonNode json = aiConnector.getJsonFromResult(response);
        JsonNode markdown = json.get("markdown");
        
        // Create ExecutiveSummary object
        ThreeWayComparison.ExecutiveSummary summary = new ThreeWayComparison.ExecutiveSummary();
        summary.setTldrVerdict(markdown.get("tldrVerdict").asText());
        summary.setWhatIsScoop(markdown.get("whatIsScoop").asText());

        // Handle bullet points that might be returned as a string or array
        JsonNode chooseScoopNode = markdown.get("chooseScoopIf");
        if (chooseScoopNode != null && !chooseScoopNode.isNull()) {
            if (chooseScoopNode.isArray()) {
                StringBuilder bullets = new StringBuilder();
                for (JsonNode bullet : chooseScoopNode) {
                    bullets.append("- ").append(bullet.asText()).append("\n");
                }
                summary.setChooseScoopIf(bullets.toString().trim());
            } else {
                summary.setChooseScoopIf(chooseScoopNode.asText());
            }
        }

        JsonNode considerANode = markdown.get("considerAIf");
        if (considerANode != null && !considerANode.isNull()) {
            if (considerANode.isArray()) {
                StringBuilder bullets = new StringBuilder();
                for (JsonNode bullet : considerANode) {
                    bullets.append("- ").append(bullet.asText()).append("\n");
                }
                summary.setConsiderAIf(bullets.toString().trim());
            } else {
                summary.setConsiderAIf(considerANode.asText());
            }
        }

        JsonNode considerBNode = markdown.get("considerBIf");
        if (considerBNode != null && !considerBNode.isNull()) {
            if (considerBNode.isArray()) {
                StringBuilder bullets = new StringBuilder();
                for (JsonNode bullet : considerBNode) {
                    bullets.append("- ").append(bullet.asText()).append("\n");
                }
                summary.setConsiderBIf(bullets.toString().trim());
            } else {
                summary.setConsiderBIf(considerBNode.asText());
            }
        }

        summary.setBottomLine(markdown.get("bottomLine").asText());
        
        return summary;
    }
    
    /**
     * Generate BUA Deep Dive section with all 5 dimensions.
     */
    private ThreeWayComparison.BUADeepDive generateBUADeepDive(
            Competitor competitorA, Competitor competitorB) throws IOException, ScoopException {
        
        ThreeWayComparison.BUADeepDive deepDive = new ThreeWayComparison.BUADeepDive();
        
        // Generate analysis for each dimension
        deepDive.setAutonomy(generateDimensionAnalysis("Autonomy", competitorA, competitorB));
        deepDive.setFlow(generateDimensionAnalysis("Flow", competitorA, competitorB));
        deepDive.setUnderstanding(generateDimensionAnalysis("Understanding", competitorA, competitorB));
        deepDive.setPresentation(generateDimensionAnalysis("Presentation", competitorA, competitorB));
        deepDive.setData(generateDimensionAnalysis("Data", competitorA, competitorB));
        
        return deepDive;
    }
    
    /**
     * Generate analysis for a specific BUA dimension.
     */
    private ThreeWayComparison.DimensionComparison generateDimensionAnalysis(
            String dimension, Competitor competitorA, Competitor competitorB) 
            throws IOException, ScoopException {
        
        // Get dimension scores
        BUAScore.Dimension dimA = getDimension(competitorA.getBuaScore(), dimension);
        BUAScore.Dimension dimB = getDimension(competitorB.getBuaScore(), dimension);
        BUAScore.Dimension dimScoop = getScoopDimension(dimension);
        
        // Prepare context
        Map<String, Object> context = new HashMap<>();
        context.put("dimension", dimension);
        context.put("competitorA", competitorA.getName());
        context.put("competitorB", competitorB.getName());
        context.put("aDimensionScore", dimA != null ? dimA.getScore() : 0);
        context.put("bDimensionScore", dimB != null ? dimB.getScore() : 0);
        context.put("scoopDimensionScore", dimScoop.getScore());
        context.put("aDimensionBreakdown", describeDimension(dimA));
        context.put("bDimensionBreakdown", describeDimension(dimB));
        context.put("scoopDimensionBreakdown", describeDimension(dimScoop));
        context.put("componentEvidence", gatherComponentEvidence(dimension, competitorA, competitorB));
        context.put("dimensionGuidance", getDimensionGuidance(dimension));
        
        // Load and fill template
        String template = templateLoader.loadTemplate("bua_dimension_analysis.md");
        String prompt = templateLoader.fillTemplate(template, context);
        
        // Invoke AI
        String response = aiConnector.invokeModel(cachedSystemPrompt, prompt);

        // Parse response using AIConnector's built-in method
        JsonNode json = aiConnector.getJsonFromResult(response);
        JsonNode markdown = json.get("markdown");
        
        // Create DimensionComparison object
        ThreeWayComparison.DimensionComparison comparison = new ThreeWayComparison.DimensionComparison();
        comparison.setDimensionName(dimension);

        // Parse component table if present
        if (markdown.has("componentTable")) {
            List<ThreeWayComparison.ComponentComparison> components = new ArrayList<>();
            for (JsonNode comp : markdown.get("componentTable")) {
                ThreeWayComparison.ComponentComparison component = new ThreeWayComparison.ComponentComparison();
                component.setComponentName(comp.get("component").asText());
                // Parse scores from JSON - might be strings like "7/8"
                String aScore = comp.get("competitorA").asText();
                String bScore = comp.get("competitorB").asText();
                String sScore = comp.get("scoop").asText();

                // Extract numeric part (e.g., "7/8" -> 7)
                component.setCompetitorAScore(extractScore(aScore));
                component.setCompetitorBScore(extractScore(bScore));
                component.setScoopScore(extractScore(sScore));
                components.add(component);
            }
            comparison.setComponents(components);
        }

        return comparison;
    }
    
    /**
     * Generate Capability Deep Dive section.
     */
    private ThreeWayComparison.CapabilityDeepDive generateCapabilityDeepDive(
            Competitor competitorA, Competitor competitorB) throws IOException, ScoopException {
        
        ThreeWayComparison.CapabilityDeepDive capabilities = new ThreeWayComparison.CapabilityDeepDive();
        
        // Generate each capability comparison
        capabilities.setInvestigationAnalysis(
            generateCapabilitySection("Investigation & Root Cause Analysis", competitorA, competitorB));
        capabilities.setSpreadsheetEngine(
            generateCapabilitySection("Excel & Spreadsheet Integration", competitorA, competitorB));
        capabilities.setSideByByScenario(
            generateCapabilitySection("Side-by-Side Scenario Analysis", competitorA, competitorB));
        capabilities.setMlPatternDiscovery(
            generateCapabilitySection("Machine Learning & Pattern Discovery", competitorA, competitorB));
        capabilities.setWorkflowIntegration(
            generateCapabilitySection("Workflow Integration & Mobile", competitorA, competitorB));
        
        return capabilities;
    }
    
    /**
     * Generate a specific capability comparison section.
     */
    private String generateCapabilitySection(String capabilityType, 
                                            Competitor competitorA, 
                                            Competitor competitorB) 
            throws IOException, ScoopException {
        
        // Prepare context
        Map<String, Object> context = new HashMap<>();
        context.put("capabilityType", capabilityType);
        context.put("competitorA", competitorA.getName());
        context.put("competitorB", competitorB.getName());
        context.put("capabilityContext", getCapabilityContext(capabilityType));
        context.put("aCapabilityEvidence", gatherCapabilityEvidence(capabilityType, competitorA));
        context.put("bCapabilityEvidence", gatherCapabilityEvidence(capabilityType, competitorB));
        context.put("scoopCapabilityEvidence", getScoopCapabilityEvidence(capabilityType));
        context.put("additionalGuidance", "");
        
        // Load and fill template
        String template = templateLoader.loadTemplate("capability_comparison.md");
        String prompt = templateLoader.fillTemplate(template, context);
        
        // Invoke AI
        String response = aiConnector.invokeModel(cachedSystemPrompt, prompt);
        
        // Parse and format as markdown using AIConnector's built-in method
        JsonNode json = aiConnector.getJsonFromResult(response);
        JsonNode markdown = json.get("markdown");
        
        StringBuilder section = new StringBuilder();
        section.append("### ").append(markdown.get("sectionTitle").asText()).append("\n\n");
        section.append(markdown.get("openingNarrative").asText()).append("\n\n");
        section.append(markdown.get("deepDiveAnalysis").asText()).append("\n\n");
        section.append("**Example**: ").append(markdown.get("exampleScenario").asText()).append("\n\n");
        section.append("**Bottom Line**: ").append(markdown.get("bottomLine").asText()).append("\n\n");
        
        return section.toString();
    }
    
    /**
     * Generate FAQ section.
     */
    private List<ThreeWayComparison.FAQQuestion> generateFAQs(
            Competitor competitorA, Competitor competitorB) throws IOException, ScoopException {
        
        // Define standard FAQ questions
        List<String> questions = Arrays.asList(
            "What is Scoop?",
            "Can Scoop handle complex multi-table queries?",
            "How much training do users need?",
            "What does " + competitorA.getName() + " really cost including hidden fees?",
            "What does " + competitorB.getName() + " really cost including hidden fees?",
            "Can Scoop handle real-time data?",
            "Which platform is best for non-technical users?",
            "How does Scoop's investigation capability work?",
            "What's the difference between Scoop and dashboard tools?",
            "Can Scoop integrate with Excel?",
            "How long does implementation take?",
            "What about data security and governance?",
            "Which platform has the best AI capabilities?",
            "Can Scoop replace my existing BI tool?"
        );
        
        // Prepare context
        Map<String, Object> context = new HashMap<>();
        context.put("competitorA", competitorA.getName());
        context.put("competitorB", competitorB.getName());
        context.put("aScore", competitorA.getBuaScore().getTotalScore());
        context.put("bScore", competitorB.getBuaScore().getTotalScore());
        context.put("aStrengths", extractStrengths(competitorA));
        context.put("bStrengths", extractStrengths(competitorB));
        context.put("aWeaknesses", extractWeaknesses(competitorA));
        context.put("bWeaknesses", extractWeaknesses(competitorB));
        context.put("faqQuestions", String.join("\n- ", questions));
        context.put("questionGuidance", "");
        
        // Load and fill template
        String template = templateLoader.loadTemplate("faq_generation.md");
        String prompt = templateLoader.fillTemplate(template, context);
        
        // Invoke AI
        String response = aiConnector.invokeModel(cachedSystemPrompt, prompt);

        // Parse response using AIConnector's built-in method
        JsonNode json = aiConnector.getJsonFromResult(response);
        JsonNode faqs = json.get("markdown").get("faqs");
        
        List<ThreeWayComparison.FAQQuestion> faqList = new ArrayList<>();
        for (JsonNode faq : faqs) {
            ThreeWayComparison.FAQQuestion question = new ThreeWayComparison.FAQQuestion();
            question.setQuestion(faq.get("question").asText());
            question.setAnswer(faq.get("answer").asText());
            
            // Add citation if present
            if (faq.has("evidence")) {
                question.setCitations(Arrays.asList(faq.get("evidence").asText()));
            }
            
            faqList.add(question);
        }
        
        return faqList;
    }
    
    // Helper methods
    
    private String extractWeaknesses(Competitor competitor) {
        // Identify weaknesses from low BUA scores
        return identifyWeaknessesFromBUA(competitor.getBuaScore());
    }
    
    private String extractStrengths(Competitor competitor) {
        // Identify from high BUA scores
        return identifyStrengthsFromBUA(competitor.getBuaScore());
    }
    
    private String identifyWeaknessesFromBUA(BUAScore score) {
        List<String> weaknesses = new ArrayList<>();
        if (score.getAutonomy() != null && score.getAutonomy().getScore() < 10) {
            weaknesses.add("Low autonomy (" + score.getAutonomy().getScore() + "/20)");
        }
        if (score.getFlow() != null && score.getFlow().getScore() < 10) {
            weaknesses.add("Poor workflow (" + score.getFlow().getScore() + "/20)");
        }
        if (score.getUnderstanding() != null && score.getUnderstanding().getScore() < 10) {
            weaknesses.add("Limited understanding (" + score.getUnderstanding().getScore() + "/20)");
        }
        return String.join(", ", weaknesses);
    }
    
    private String identifyStrengthsFromBUA(BUAScore score) {
        List<String> strengths = new ArrayList<>();
        if (score.getAutonomy() != null && score.getAutonomy().getScore() >= 15) {
            strengths.add("High autonomy (" + score.getAutonomy().getScore() + "/20)");
        }
        if (score.getData() != null && score.getData().getScore() >= 15) {
            strengths.add("Strong data connectivity (" + score.getData().getScore() + "/20)");
        }
        return String.join(", ", strengths);
    }
    
    private String gatherEvidence(Competitor competitor) {
        // Would read from evidence files
        return "BUA Score: " + competitor.getBuaScore().getTotalScore() + "/100";
    }
    
    private String gatherComponentEvidence(String dimension, Competitor a, Competitor b) {
        // Would gather specific component evidence
        return "Component evidence for " + dimension;
    }
    
    private String gatherCapabilityEvidence(String capability, Competitor competitor) {
        // Would gather capability-specific evidence
        return "Evidence for " + capability + " from " + competitor.getName();
    }
    
    private String getCapabilityContext(String capabilityType) {
        // Return context for specific capability
        return "Context for " + capabilityType;
    }
    
    private String getScoopCapabilityEvidence(String capability) {
        // Return Scoop's evidence for capability
        return "Scoop evidence for " + capability;
    }
    
    private BUAScore.Dimension getDimension(BUAScore score, String dimension) {
        if (score == null) return null;
        switch (dimension.toLowerCase()) {
            case "autonomy": return score.getAutonomy();
            case "flow": return score.getFlow();
            case "understanding": return score.getUnderstanding();
            case "presentation": return score.getPresentation();
            case "data": return score.getData();
            default: return null;
        }
    }
    
    private BUAScore.Dimension getScoopDimension(String dimension) {
        // Scoop's scores: 82/100 total
        switch (dimension.toLowerCase()) {
            case "autonomy": return new BUAScore.Dimension("Autonomy", 18, 20);
            case "flow": return new BUAScore.Dimension("Flow", 17, 20);
            case "understanding": return new BUAScore.Dimension("Understanding", 16, 20);
            case "presentation": return new BUAScore.Dimension("Presentation", 15, 20);
            case "data": return new BUAScore.Dimension("Data", 16, 20);
            default: return new BUAScore.Dimension(dimension, 15, 20);
        }
    }
    
    private String describeDimension(BUAScore.Dimension dim) {
        if (dim == null) return "Not scored";
        return String.format("%d/20 components", dim.getScore());
    }
    
    private String getDimensionGuidance(String dimension) {
        // Return specific guidance for dimension
        return "Focus on " + dimension.toLowerCase() + " capabilities";
    }
    
    private ThreeWayComparison.ComparisonMatrix generateAtAGlanceMatrix(
            Competitor competitorA, Competitor competitorB) {
        // Would generate with AI, but for now return basic matrix
        ThreeWayComparison.ComparisonMatrix matrix = new ThreeWayComparison.ComparisonMatrix();
        List<ThreeWayComparison.MatrixRow> rows = new ArrayList<>();
        
        // Add standard comparison rows
        rows.add(new ThreeWayComparison.MatrixRow(
            "BUA Score",
            competitorA.getBuaScore().getTotalScore() + "/100",
            competitorB.getBuaScore().getTotalScore() + "/100",
            "82/100",
            "Scoop highest autonomy"
        ));
        
        matrix.setRows(rows);
        return matrix;
    }
    
    private String generateFAQSchema(List<ThreeWayComparison.FAQQuestion> faqs) {
        // Generate schema.org FAQPage markup
        return "{\"@type\": \"FAQPage\"}";
    }

    /**
     * Extract numeric score from strings like "7/8" or "7"
     */
    private int extractScore(String scoreStr) {
        if (scoreStr == null || scoreStr.isEmpty()) return 0;

        // Handle "X/Y" format
        if (scoreStr.contains("/")) {
            String[] parts = scoreStr.split("/");
            try {
                return Integer.parseInt(parts[0].trim());
            } catch (NumberFormatException e) {
                return 0;
            }
        }

        // Try to parse as simple number
        try {
            return Integer.parseInt(scoreStr.replaceAll("[^0-9]", ""));
        } catch (NumberFormatException e) {
            return 0;
        }
    }
}