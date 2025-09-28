package com.scoop.competitive;

import com.scoop.competitive.config.AppConfig;
import com.scoop.competitive.ai.AIComparisonGenerator;
import com.scoop.competitive.loader.CompetitorLoader;
import com.scoop.competitive.model.Competitor;
import com.scoop.competitive.model.ThreeWayComparison;
import com.scoop.competitive.writer.MarkdownWriter;
import org.cfg4j.provider.ConfigurationProvider;
import org.cfg4j.provider.ConfigurationProviderBuilder;
import org.cfg4j.source.context.environment.Environment;
import org.cfg4j.source.context.environment.ImmutableEnvironment;
import org.cfg4j.source.context.filesprovider.ConfigFilesProvider;
import org.cfg4j.source.files.FilesConfigurationSource;
import scoop.ScoopContext;
import scoop.metadata.ScoopMetadata;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


/**
 * Main application for AI-powered three-way comparison generation.
 * <p>
 * Uses Claude/GPT-4 via AIConnector to generate intelligent, nuanced comparisons
 * based on prompt templates rather than hard-coded content.
 */
public class AIComparisonApp {
    private static final Logger logger = LoggerFactory.getLogger(AIComparisonApp.class);

    public static void main(String[] args) {
        System.out.println("=== AI-Powered Three-Way Comparison Generator ===");
        System.out.println("Using Claude/GPT-4 for intelligent content generation");
        System.out.println();

        // Determine which competitors to compare
        String competitorA = "power-bi-copilot";
        String competitorB = "snowflake-cortex";

        if (args.length >= 2) {
            competitorA = args[0];
            competitorB = args[1];
        }

        System.out.println("Comparing: " + competitorA + " vs " + competitorB + " vs Scoop");
        System.out.println();

        try {
            // Initialize configuration
            AppConfig config = AppConfig.getInstance();
            config.printConfig();

            // Load competitors
            CompetitorLoader loader = new CompetitorLoader(config);
            System.out.println("\nLoading competitor data...");
            Competitor compA = loader.loadCompetitor(competitorA);
            Competitor compB = loader.loadCompetitor(competitorB);

            System.out.println("Loaded: " + compA.getName() + " (BUA: " + compA.getBuaScore().getTotalScore() + "/100)");
            System.out.println("Loaded: " + compB.getName() + " (BUA: " + compB.getBuaScore().getTotalScore() + "/100)");

            // Initialize AI-powered generator
            System.out.println("\nInitializing AI generator...");
            System.out.println("\nNOTE: This will attempt to create ScoopContext.");
            System.out.println("It may fail if Scoop is not properly configured.\n");

            try {
                // Create ScoopMetadata with prod configuration
                System.out.println("Setting up ScoopMetadata with prod configuration...");

                String configDir = "../../scoop/app/src/dist/prod";
                ConfigFilesProvider configFilesProvider = () -> List.of(
                    Paths.get("application.properties")
                );
                FilesConfigurationSource source = new FilesConfigurationSource(configFilesProvider);
                Environment environment = new ImmutableEnvironment(configDir);
                ConfigurationProvider cfg = new ConfigurationProviderBuilder()
                    .withConfigurationSource(source)
                    .withEnvironment(environment)
                    .build();

                System.out.println("Creating ScoopMetadata...");
                ScoopMetadata metadata = new ScoopMetadata(cfg, false, "3WayComparison");

                // Create ScoopContext with test workspace and user
                String workspaceId = "W517"; // Using the sample workspace from config
                String userId = "test-user-3way";

                System.out.println("Creating ScoopContext...");
                ScoopContext scoopContext = new ScoopContext(metadata, workspaceId, userId);

                System.out.println("\n🎆 Attempting REAL AI generation with Claude/GPT-4...");

                // Create the AI comparison generator
                AIComparisonGenerator aiGenerator = new AIComparisonGenerator(scoopContext);

                // Generate comparison using AI
                System.out.println("\nGenerating AI-powered comparison...");
                System.out.println("This will make multiple calls to Claude/GPT-4 and may take 30-60 seconds.");

                ThreeWayComparison comparison = aiGenerator.generateComparison(compA, compB);

                // Write output
                String filename = String.format("%s-vs-%s-vs-scoop-ai.md", competitorA, competitorB);
                Path outputPath = config.getOutputPath().resolve(filename);

                System.out.println("\nWriting AI-generated comparison to: " + outputPath);
                MarkdownWriter writer = new MarkdownWriter();
                writer.writeComparison(comparison, outputPath);

                System.out.println("\n✅ AI-powered comparison generated successfully!");
                System.out.println("Output: " + outputPath.toAbsolutePath());

                // Print statistics
                printStatistics(comparison);

            } catch (Exception aiException) {
                System.err.println("\n❌ Failed to generate with AI: " + aiException.getMessage());
                aiException.printStackTrace();

                System.out.println("\nFalling back to mock generation...");

                // Fall back to mock comparison
                ThreeWayComparison mockComparison = createMockComparison(compA, compB);
                String filename = String.format("%s-vs-%s-vs-scoop-mock.md", competitorA, competitorB);
                Path outputPath = config.getOutputPath().resolve(filename);

                MarkdownWriter writer = new MarkdownWriter();
                writer.writeComparison(mockComparison, outputPath);

                System.out.println("\n✅ Mock comparison saved to: " + outputPath.toAbsolutePath());
            }

        } catch (Exception e) {
            System.err.println("\n❌ Generation failed: " + e.getMessage());
            e.printStackTrace();
            System.exit(1);
        }
    }

    /**
     * Create a mock comparison for demonstration purposes
     */
    private static ThreeWayComparison createMockComparison(Competitor compA, Competitor compB) {
        ThreeWayComparison comparison = new ThreeWayComparison();

        // Set basic info
        comparison.setTitle(String.format("%s vs %s vs Scoop: Mock Comparison",
                                        compA.getName(), compB.getName()));
        comparison.setSeoTitle(String.format("%s vs %s vs Scoop 2024",
                                           compA.getName(), compB.getName()));
        comparison.setMetaDescription(String.format("Compare %s (%d/100 BUA) vs %s (%d/100) vs Scoop (82/100). " +
                                                   "See which platform delivers true business user autonomy.",
                                                   compA.getName(), compA.getBuaScore().getTotalScore(),
                                                   compB.getName(), compB.getBuaScore().getTotalScore()));
        comparison.setSlug(String.format("%s-vs-%s-vs-scoop",
                                       compA.getSlug(), compB.getSlug()));
        comparison.setCompetitorA(compA);
        comparison.setCompetitorB(compB);

        // Create mock executive summary
        ThreeWayComparison.ExecutiveSummary summary = new ThreeWayComparison.ExecutiveSummary();
        summary.setTldrVerdict(String.format(
            "Scoop (82/100 BUA) delivers true business autonomy through multi-pass investigation, " +
            "while %s (%d/100) and %s (%d/100) remain dashboard-bound tools requiring IT support.",
            compA.getName(), compA.getBuaScore().getTotalScore(),
            compB.getName(), compB.getBuaScore().getTotalScore()
        ));
        summary.setWhatIsScoop(
            "Scoop is an AI data analyst you chat with, not another dashboard tool. " +
            "Ask questions in plain English, get answers with charts. Works natively in Excel and Slack."
        );
        summary.setChooseScoopIf(
            "- You want business users to investigate 'why' questions independently\n" +
            "- Your team works primarily in Excel\n" +
            "- You need answers in minutes, not days\n" +
            "- You're tired of maintaining semantic layers"
        );
        summary.setConsiderAIf(String.format(
            "- You're already invested in the %s ecosystem\n" +
            "- You have dedicated IT resources for maintenance",
            compA.getParent() != null ? compA.getParent() : compA.getName()
        ));
        summary.setConsiderBIf(String.format(
            "- You need %s's specific industry features\n" +
            "- You have SQL-savvy analysts",
            compB.getName()
        ));
        summary.setBottomLine(
            "The fundamental difference: Scoop enables investigation, competitors enable dashboards. " +
            "When business users ask 'why', Scoop automatically runs multiple queries to find root causes. " +
            "Dashboard tools show you what happened but can't investigate why."
        );
        comparison.setExecutiveSummary(summary);

        // Create mock FAQ section
        java.util.List<ThreeWayComparison.FAQQuestion> faqs = new java.util.ArrayList<>();

        ThreeWayComparison.FAQQuestion faq1 = new ThreeWayComparison.FAQQuestion();
        faq1.setQuestion("What is Scoop?");
        faq1.setAnswer(
            "Scoop is an AI data analyst you chat with, not another dashboard. Ask questions in plain English, " +
            "get answers with charts. Unlike " + compA.getName() + " and " + compB.getName() +
            " which require IT setup, Scoop connects directly to your data."
        );
        faqs.add(faq1);

        ThreeWayComparison.FAQQuestion faq2 = new ThreeWayComparison.FAQQuestion();
        faq2.setQuestion("How much training do users need?");
        faq2.setAnswer(
            "Scoop requires zero training—if you can use ChatGPT, you can use Scoop. " +
            compA.getName() + " requires weeks of training, " + compB.getName() +
            " needs SQL knowledge. Business users become productive immediately with Scoop."
        );
        faqs.add(faq2);

        comparison.setFaqSection(faqs);

        System.out.println("\n📊 Mock Comparison Stats:");
        System.out.println("- " + compA.getName() + ": " + compA.getBuaScore().getTotalScore() + "/100 BUA");
        System.out.println("- " + compB.getName() + ": " + compB.getBuaScore().getTotalScore() + "/100 BUA");
        System.out.println("- Scoop: 82/100 BUA");
        System.out.println("- FAQ Questions: " + faqs.size());

        return comparison;
    }

    private static void printStatistics(ThreeWayComparison comparison) {
        System.out.println("\n=== AI Generation Statistics ===");

        if (comparison.getExecutiveSummary() != null) {
            String tldr = comparison.getExecutiveSummary().getTldrVerdict();
            System.out.println("TL;DR word count: " + countWords(tldr) + " (target: 50-58)");
        }

        if (comparison.getFaqSection() != null) {
            System.out.println("FAQ questions generated: " + comparison.getFaqSection().size());

            // Check word counts for AEO compliance
            int compliant = 0;
            for (ThreeWayComparison.FAQQuestion faq : comparison.getFaqSection()) {
                int words = countWords(faq.getAnswer());
                if (words >= 40 && words <= 60) {
                    compliant++;
                }
            }
            System.out.println("AEO-compliant FAQ answers: " + compliant + "/" + comparison.getFaqSection().size());
        }

        System.out.println("\nKey features of AI generation:");
        System.out.println("- Nuanced understanding of competitor weaknesses");
        System.out.println("- Natural language variation (not template-y)");
        System.out.println("- Evidence integration from BUA scores");
        System.out.println("- AEO optimization built into prompts");
        System.out.println("- Consistent tone and positioning");
    }

    private static int countWords(String text) {
        if (text == null || text.trim().isEmpty()) {
            return 0;
        }
        return text.trim().split("\\s+").length;
    }
}