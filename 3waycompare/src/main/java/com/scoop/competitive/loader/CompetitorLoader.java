package com.scoop.competitive.loader;

import com.scoop.competitive.config.AppConfig;
import com.scoop.competitive.model.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

/**
 * Loads competitor data from the competitive-intelligence directory structure.
 *
 * Expected structure:
 * /competitors/[slug]/
 *   - COMPETITIVE_STRATEGY.md
 *   - BATTLE_CARD.md
 *   - evidence/framework_scoring.md
 *   - evidence/phase1_customer_discovery.md
 *   - evidence/phase2_functionality_analysis.md
 *   - evidence/phase3_technical_reality.md
 *   - evidence/phase4_sales_enablement.md
 *   - outputs/web_comparison.md
 */
public class CompetitorLoader {
    private static final Logger logger = LoggerFactory.getLogger(CompetitorLoader.class);
    private final AppConfig config;

    public CompetitorLoader(AppConfig config) {
        this.config = config;
    }

    /**
     * Load complete competitor data from filesystem
     */
    public Competitor loadCompetitor(String slug) throws IOException {
        logger.info("Loading competitor: {}", slug);

        Path competitorPath = config.getCompetitorPath(slug);
        logger.debug("Competitor path: {}", competitorPath);
        logger.debug("Path exists: {}", Files.exists(competitorPath));

        if (!Files.exists(competitorPath)) {
            logger.error("Looking for competitor at: {}", competitorPath);
            logger.error("Absolute path: {}", competitorPath.toAbsolutePath());
            throw new IOException("Competitor directory not found: " + competitorPath);
        }

        Competitor competitor = new Competitor();
        competitor.setSlug(slug);
        competitor.setBasePath(competitorPath.toString());

        // Derive name from slug
        competitor.setName(deriveNameFromSlug(slug));

        // Load BUA scores
        loadBUAScores(competitor, competitorPath);

        // Note: CompetitiveStrategy and BattleCard loading removed
        // AI generation uses BUA scores and evidence files directly

        logger.info("Loaded competitor: {} - {} (BUA: {})",
                slug,
                competitor.getName(),
                competitor.getBuaScore() != null ?
                        competitor.getBuaScore().getTotalScore() : "N/A");

        return competitor;
    }

    /**
     * Load BUA scores from framework_scoring.md
     */
    private void loadBUAScores(Competitor competitor, Path competitorPath) throws IOException {
        Path scoringPath = competitorPath.resolve("evidence/framework_scoring.md");
        if (!Files.exists(scoringPath)) {
            logger.warn("BUA scoring file not found: {}", scoringPath);
            return;
        }

        // Read file content
        List<String> lines = Files.readAllLines(scoringPath);

        BUAScore score = new BUAScore();

        // Parse markdown to extract scores
        // This is a simple parser - could be enhanced with proper markdown library
        for (int i = 0; i < lines.size(); i++) {
            String line = lines.get(i).trim();

            // Look for total score line
            if (line.contains("**Total Score**:") || line.startsWith("**Scored By**")) {
                // Try next few lines for score
                for (int j = i; j < Math.min(i + 10, lines.size()); j++) {
                    String scoreLine = lines.get(j);
                    if (scoreLine.matches(".*\\d+/100.*")) {
                        String[] parts = scoreLine.split("/100");
                        if (parts.length > 0) {
                            String scoreStr = parts[0].replaceAll("[^0-9]", "");
                            if (!scoreStr.isEmpty()) {
                                int totalScore = Integer.parseInt(scoreStr);
                                score.setTotalScore(totalScore);
                                score.calculateCategory();
                                logger.debug("Found total score: {}", totalScore);
                                break;
                            }
                        }
                    }
                }
            }

            // Parse dimension scores
            if (line.startsWith("### Dimension 1: Autonomy")) {
                parseDimensionScore(lines, i, score, "autonomy");
            } else if (line.startsWith("### Dimension 2: Flow")) {
                parseDimensionScore(lines, i, score, "flow");
            } else if (line.startsWith("### Dimension 3: Understanding")) {
                parseDimensionScore(lines, i, score, "understanding");
            } else if (line.startsWith("### Dimension 4: Presentation")) {
                parseDimensionScore(lines, i, score, "presentation");
            } else if (line.startsWith("### Dimension 5: Data")) {
                parseDimensionScore(lines, i, score, "data");
            }
        }

        competitor.setBuaScore(score);
    }

    /**
     * Parse dimension score from markdown
     */
    private void parseDimensionScore(List<String> lines, int startIndex,
                                     BUAScore score, String dimensionName) {
        // Look for "**Total [Dimension]**: X/20" pattern
        for (int i = startIndex; i < Math.min(startIndex + 50, lines.size()); i++) {
            String line = lines.get(i).trim();
            if (line.startsWith("**Total") && line.contains("/20")) {
                String[] parts = line.split("/20");
                if (parts.length > 0) {
                    String scoreStr = parts[0].replaceAll("[^0-9]", "");
                    if (!scoreStr.isEmpty()) {
                        int dimScore = Integer.parseInt(scoreStr);
                        BUAScore.Dimension dimension = new BUAScore.Dimension(
                                dimensionName, dimScore, 20);

                        // Set the dimension
                        switch (dimensionName.toLowerCase()) {
                            case "autonomy":
                                score.setAutonomy(dimension);
                                break;
                            case "flow":
                                score.setFlow(dimension);
                                break;
                            case "understanding":
                                score.setUnderstanding(dimension);
                                break;
                            case "presentation":
                                score.setPresentation(dimension);
                                break;
                            case "data":
                                score.setData(dimension);
                                break;
                        }
                        logger.debug("Found {} dimension score: {}/20", dimensionName, dimScore);
                        break;
                    }
                }
            }
        }
    }

    private String deriveNameFromSlug(String slug) {
        switch (slug) {
            case "power-bi-copilot": return "Power BI Copilot";
            case "tableau-pulse": return "Tableau Pulse";
            case "snowflake-cortex": return "Snowflake Cortex";
            case "domo": return "Domo";
            case "thoughtspot": return "ThoughtSpot";
            case "sisense": return "Sisense";
            case "qlik": return "Qlik Sense";
            case "tellius": return "Tellius";
            case "datagpt": return "DataGPT";
            case "zenlytic": return "Zenlytic";
            case "datachat": return "DataChat";
            default:
                String[] parts = slug.split("-");
                StringBuilder name = new StringBuilder();
                for (String part : parts) {
                    name.append(Character.toUpperCase(part.charAt(0)));
                    name.append(part.substring(1));
                    name.append(" ");
                }
                return name.toString().trim();
        }
    }

}