package com.scoop.competitive.writer;

import com.scoop.competitive.model.ThreeWayComparison;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.List;

public class MarkdownWriter {

    public void writeComparison(ThreeWayComparison comparison, Path outputPath) throws IOException {
        StringBuilder markdown = new StringBuilder();

        writeMeta(markdown, comparison);
        writeExecutiveSummary(markdown, comparison);
        writeAtAGlanceMatrix(markdown, comparison);
        writeBUADeepDive(markdown, comparison);
        writeCapabilityDeepDive(markdown, comparison);
        writeFAQ(markdown, comparison);
        writeSchemas(markdown, comparison);

        Files.createDirectories(outputPath.getParent());
        Files.writeString(outputPath, markdown.toString(),
            StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING);
    }

    private void writeMeta(StringBuilder md, ThreeWayComparison comparison) {
        md.append("---\n");
        md.append("title: ").append(comparison.getSeoTitle()).append("\n");
        md.append("description: ").append(comparison.getMetaDescription()).append("\n");
        md.append("slug: ").append(comparison.getSlug()).append("\n");
        md.append("lastUpdated: ").append(java.time.LocalDate.now()).append("\n");
        md.append("---\n\n");

        md.append("# ").append(comparison.getTitle()).append("\n\n");

        if (comparison.getQuestionCluster() != null && !comparison.getQuestionCluster().isEmpty()) {
            md.append("<!-- Question Cluster for AEO:\n");
            for (String question : comparison.getQuestionCluster()) {
                md.append("  - ").append(question).append("\n");
            }
            md.append("-->\n\n");
        }
    }

    private void writeExecutiveSummary(StringBuilder md, ThreeWayComparison comparison) {
        if (comparison.getExecutiveSummary() == null) return;

        md.append("## Executive Summary\n\n");

        ThreeWayComparison.ExecutiveSummary summary = comparison.getExecutiveSummary();

        md.append("### TL;DR Verdict\n\n");
        md.append(summary.getTldrVerdict()).append("\n\n");

        md.append("### What is Scoop?\n\n");
        md.append(summary.getWhatIsScoop()).append("\n\n");

        md.append("### Choose Scoop If\n\n");
        md.append(summary.getChooseScoopIf()).append("\n\n");

        md.append("### Consider ").append(comparison.getCompetitorA().getName()).append(" If\n\n");
        md.append(summary.getConsiderAIf()).append("\n\n");

        md.append("### Consider ").append(comparison.getCompetitorB().getName()).append(" If\n\n");
        md.append(summary.getConsiderBIf()).append("\n\n");

        md.append("### Bottom Line\n\n");
        md.append(summary.getBottomLine()).append("\n\n");
    }

    private void writeAtAGlanceMatrix(StringBuilder md, ThreeWayComparison comparison) {
        if (comparison.getAtAGlanceMatrix() == null) return;

        md.append("## At-a-Glance Comparison\n\n");

        md.append("| Dimension | ").append(comparison.getCompetitorA().getName());
        md.append(" | ").append(comparison.getCompetitorB().getName());
        md.append(" | Scoop |\n");
        md.append("|-----------|");
        md.append("----------|----------|-------|\n");

        List<ThreeWayComparison.MatrixRow> rows = comparison.getAtAGlanceMatrix().getRows();
        if (rows != null) {
            for (ThreeWayComparison.MatrixRow row : rows) {
                md.append("| **").append(row.getDimension()).append("** | ");
                md.append(row.getCompetitorAValue()).append(" | ");
                md.append(row.getCompetitorBValue()).append(" | ");
                md.append(row.getScoopValue());

                if (row.getKeyInsight() != null && row.getKeyInsight().contains("Scoop")) {
                    md.append(" ✓");
                }

                md.append(" |\n");
            }
        }

        md.append("\n");
    }

    private void writeBUADeepDive(StringBuilder md, ThreeWayComparison comparison) {
        if (comparison.getBuaDeepDive() == null) return;

        md.append("## BUA Framework Deep Dive\n\n");
        md.append("The Business User Autonomy (BUA) Framework measures what users can do alone across 5 dimensions (20 points each).\n\n");

        ThreeWayComparison.BUADeepDive deepDive = comparison.getBuaDeepDive();

        writeDimension(md, "Autonomy", deepDive.getAutonomy(), comparison);
        writeDimension(md, "Flow", deepDive.getFlow(), comparison);
        writeDimension(md, "Understanding", deepDive.getUnderstanding(), comparison);
        writeDimension(md, "Presentation", deepDive.getPresentation(), comparison);
        writeDimension(md, "Data", deepDive.getData(), comparison);
    }

    private void writeDimension(StringBuilder md, String dimensionName,
                                 ThreeWayComparison.DimensionComparison analysis,
                                 ThreeWayComparison comparison) {
        if (analysis == null) return;

        md.append("### ").append(dimensionName).append(" (20 points)\n\n");

        // Dimension comparison scoring not directly available in model
        md.append("**Dimension**: ").append(dimensionName).append("\n\n");

        // Write component comparisons if available
        if (analysis.getComponents() != null && !analysis.getComponents().isEmpty()) {
            md.append("#### Component Breakdown\n\n");
            md.append("| Component | ").append(comparison.getCompetitorA().getName());
            md.append(" | ").append(comparison.getCompetitorB().getName());
            md.append(" | Scoop |\n");
            md.append("|-----------|----------|----------|-------|\n");

            // Write component rows
            for (ThreeWayComparison.ComponentComparison comp : analysis.getComponents()) {
                md.append("| ").append(comp.getComponentName());
                md.append(" | ").append(comp.getCompetitorAScore()).append("/8");
                md.append(" | ").append(comp.getCompetitorBScore()).append("/8");
                md.append(" | ").append(comp.getScoopScore()).append("/8 |\n");
            }

            md.append("\n");
        }
    }

    private void writeCapabilityDeepDive(StringBuilder md, ThreeWayComparison comparison) {
        if (comparison.getCapabilityDeepDive() == null) return;

        md.append("## Capability Deep Dive\n\n");

        ThreeWayComparison.CapabilityDeepDive capabilities = comparison.getCapabilityDeepDive();

        // Write each capability section if it exists
        if (capabilities.getInvestigationAnalysis() != null) {
            md.append(capabilities.getInvestigationAnalysis()).append("\n\n");
        }
        if (capabilities.getSpreadsheetEngine() != null) {
            md.append(capabilities.getSpreadsheetEngine()).append("\n\n");
        }
        if (capabilities.getSideByByScenario() != null) {
            md.append(capabilities.getSideByByScenario()).append("\n\n");
        }
        if (capabilities.getMlPatternDiscovery() != null) {
            md.append(capabilities.getMlPatternDiscovery()).append("\n\n");
        }
        if (capabilities.getWorkflowIntegration() != null) {
            md.append(capabilities.getWorkflowIntegration()).append("\n\n");
        }
    }

    private void writeFAQ(StringBuilder md, ThreeWayComparison comparison) {
        if (comparison.getFaqSection() == null || comparison.getFaqSection().isEmpty()) return;

        md.append("## Frequently Asked Questions\n\n");

        for (ThreeWayComparison.FAQQuestion faq : comparison.getFaqSection()) {
            md.append("### ").append(faq.getQuestion()).append("\n\n");
            md.append(faq.getAnswer());

            if (faq.getCitations() != null && !faq.getCitations().isEmpty()) {
                md.append(" [Evidence: ");
                md.append(String.join(", ", faq.getCitations()));
                md.append("]");
            }

            md.append("\n\n");
        }
    }

    private void writeSchemas(StringBuilder md, ThreeWayComparison comparison) {
        md.append("## Schema Markup\n\n");

        if (comparison.getFaqPageSchema() != null) {
            md.append("### FAQPage Schema\n\n");
            md.append("```json\n");
            md.append(comparison.getFaqPageSchema());
            md.append("```\n\n");
        }

        if (comparison.getProductSchema() != null) {
            md.append("### Product Schema\n\n");
            md.append("```json\n");
            md.append(comparison.getProductSchema());
            md.append("```\n\n");
        }

        if (comparison.getOrganizationSchema() != null) {
            md.append("### Organization Schema\n\n");
            md.append("```json\n");
            md.append(comparison.getOrganizationSchema());
            md.append("```\n\n");
        }
    }
}