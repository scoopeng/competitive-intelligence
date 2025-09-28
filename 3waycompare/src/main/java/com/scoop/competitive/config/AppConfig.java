package com.scoop.competitive.config;

import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Application configuration - paths to data sources and outputs.
 */
public class AppConfig {
    private static AppConfig instance;

    private final Path competitiveIntelligencePath;
    private final Path webflowOutputPath;
    private final Path scoopPath;
    private final Path outputPath; // For generated comparisons

    private AppConfig() {
        // Use absolute paths directly
        String ciPath = "/home/ubuntu/dev/competitive-intelligence";
        String webflowPath = "/home/ubuntu/dev/webflow-competitive-intelligence";
        String scopePath = "/home/ubuntu/dev/scoop";

        System.out.println("DEBUG: ciPath = " + ciPath);
        this.competitiveIntelligencePath = Paths.get(ciPath);
        this.webflowOutputPath = Paths.get(webflowPath);
        this.scoopPath = Paths.get(scopePath);
        System.out.println("DEBUG: competitiveIntelligencePath = " + this.competitiveIntelligencePath);
        this.outputPath = this.competitiveIntelligencePath.resolve("3waycompare/output");
    }

    public static synchronized AppConfig getInstance() {
        if (instance == null) {
            instance = new AppConfig();
        }
        return instance;
    }

    public Path getCompetitiveIntelligencePath() {
        return competitiveIntelligencePath;
    }

    public Path getWebflowOutputPath() {
        return webflowOutputPath;
    }

    public Path getScoopPath() {
        return scoopPath;
    }

    public Path getOutputPath() {
        return outputPath;
    }

    /**
     * Get path to specific competitor directory
     */
    public Path getCompetitorPath(String competitorSlug) {
        return competitiveIntelligencePath.resolve("competitors").resolve(competitorSlug);
    }

    /**
     * Get path to SCOOP_CAPABILITIES.md
     */
    public Path getScoopCapabilitiesPath() {
        return competitiveIntelligencePath.resolve("SCOOP_CAPABILITIES.md");
    }

    /**
     * Get path to THREE_WAY_COMPARISON_TEMPLATE.md
     */
    public Path getTemplatePath() {
        return competitiveIntelligencePath.resolve("3waycompare")
                .resolve("THREE_WAY_COMPARISON_TEMPLATE.md");
    }

    /**
     * Get list of all competitor slugs
     */
    public String[] getAllCompetitorSlugs() {
        return new String[]{
                "power-bi-copilot",
                "tableau-pulse",
                "snowflake-cortex",
                "domo",
                "thoughtspot",
                "sisense",
                "qlik",
                "tellius",
                "datagpt",
                "zenlytic",
                "datachat"
        };
    }

    public void printConfig() {
        System.out.println("=== App Configuration ===");
        System.out.println("Current Dir: " + System.getProperty("user.dir"));
        System.out.println("Competitive Intelligence: " + competitiveIntelligencePath);
        System.out.println("Webflow Output: " + webflowOutputPath);
        System.out.println("Scoop Path: " + scoopPath);
        System.out.println("Output Path: " + outputPath);
        System.out.println("========================");
    }
}