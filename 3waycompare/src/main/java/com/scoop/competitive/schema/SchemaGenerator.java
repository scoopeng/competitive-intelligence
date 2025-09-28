package com.scoop.competitive.schema;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import com.scoop.competitive.model.ThreeWayComparison;
import java.util.List;

/**
 * Generates JSON-LD schema markup for SEO enhancement.
 * Creates FAQ, Product, and SoftwareApplication schemas.
 */
public class SchemaGenerator {
    private final ObjectMapper objectMapper;

    public SchemaGenerator() {
        this.objectMapper = new ObjectMapper();
    }

    /**
     * Generate FAQ schema for rich results.
     */
    public String generateFAQSchema(List<ThreeWayComparison.FAQQuestion> faqs) {
        if (faqs == null || faqs.isEmpty()) {
            return "";
        }

        ObjectNode schema = objectMapper.createObjectNode();
        schema.put("@context", "https://schema.org");
        schema.put("@type", "FAQPage");

        ArrayNode mainEntity = objectMapper.createArrayNode();

        for (ThreeWayComparison.FAQQuestion faq : faqs) {
            ObjectNode question = objectMapper.createObjectNode();
            question.put("@type", "Question");
            question.put("name", faq.getQuestion());

            ObjectNode answer = objectMapper.createObjectNode();
            answer.put("@type", "Answer");
            answer.put("text", faq.getAnswer());

            question.set("acceptedAnswer", answer);
            mainEntity.add(question);
        }

        schema.set("mainEntity", mainEntity);

        try {
            return "<!-- FAQ Schema for Rich Results -->\n" +
                   "<script type=\"application/ld+json\">\n" +
                   objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(schema) +
                   "\n</script>";
        } catch (Exception e) {
            return "";
        }
    }

    /**
     * Generate Product comparison schema.
     */
    public String generateProductSchema(String competitorA, String competitorB,
                                       int scoreA, int scoreB) {
        ObjectNode schema = objectMapper.createObjectNode();
        schema.put("@context", "https://schema.org");
        schema.put("@type", "Product");
        schema.put("name", competitorA + " vs " + competitorB + " vs Scoop Analytics");
        schema.put("description", "Comprehensive comparison of business intelligence platforms focusing on business user autonomy");

        // Add aggregate rating for Scoop
        ObjectNode aggregateRating = objectMapper.createObjectNode();
        aggregateRating.put("@type", "AggregateRating");
        aggregateRating.put("ratingValue", "82");
        aggregateRating.put("bestRating", "100");
        aggregateRating.put("worstRating", "0");
        aggregateRating.put("ratingCount", "1");
        aggregateRating.put("reviewCount", "1");

        schema.set("aggregateRating", aggregateRating);

        // Add review
        ObjectNode review = objectMapper.createObjectNode();
        review.put("@type", "Review");
        review.put("reviewRating", objectMapper.createObjectNode()
            .put("@type", "Rating")
            .put("ratingValue", "82")
            .put("bestRating", "100"));
        review.put("author", objectMapper.createObjectNode()
            .put("@type", "Organization")
            .put("name", "Scoop Analytics Competitive Intelligence"));

        schema.set("review", review);

        try {
            return "<!-- Product Schema for Rich Results -->\n" +
                   "<script type=\"application/ld+json\">\n" +
                   objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(schema) +
                   "\n</script>";
        } catch (Exception e) {
            return "";
        }
    }

    /**
     * Generate SoftwareApplication schema.
     */
    public String generateSoftwareApplicationSchema() {
        ObjectNode schema = objectMapper.createObjectNode();
        schema.put("@context", "https://schema.org");
        schema.put("@type", "SoftwareApplication");
        schema.put("name", "Scoop Analytics");
        schema.put("applicationCategory", "BusinessApplication");
        schema.put("applicationSubCategory", "Business Intelligence");
        schema.put("operatingSystem", "Web, Windows, macOS");

        // Add offers
        ObjectNode offers = objectMapper.createObjectNode();
        offers.put("@type", "Offer");
        offers.put("price", "0");
        offers.put("priceCurrency", "USD");
        offers.put("description", "Free trial available");

        schema.set("offers", offers);

        // Add aggregate rating
        ObjectNode aggregateRating = objectMapper.createObjectNode();
        aggregateRating.put("@type", "AggregateRating");
        aggregateRating.put("ratingValue", "4.8");
        aggregateRating.put("ratingCount", "150");

        schema.set("aggregateRating", aggregateRating);

        // Add feature list
        ArrayNode featureList = objectMapper.createArrayNode();
        featureList.add("Natural Language Analytics");
        featureList.add("Multi-pass Investigation");
        featureList.add("Excel Native Integration");
        featureList.add("Slack Integration");
        featureList.add("No Training Required");

        schema.set("featureList", featureList);

        try {
            return "<!-- SoftwareApplication Schema -->\n" +
                   "<script type=\"application/ld+json\">\n" +
                   objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(schema) +
                   "\n</script>";
        } catch (Exception e) {
            return "";
        }
    }

    /**
     * Generate BreadcrumbList schema for navigation.
     */
    public String generateBreadcrumbSchema(String competitorA, String competitorB) {
        ObjectNode schema = objectMapper.createObjectNode();
        schema.put("@context", "https://schema.org");
        schema.put("@type", "BreadcrumbList");

        ArrayNode itemList = objectMapper.createArrayNode();

        // Home
        ObjectNode item1 = objectMapper.createObjectNode();
        item1.put("@type", "ListItem");
        item1.put("position", 1);
        item1.put("name", "Home");
        item1.put("item", "https://scoop-analytics.com");
        itemList.add(item1);

        // Comparisons
        ObjectNode item2 = objectMapper.createObjectNode();
        item2.put("@type", "ListItem");
        item2.put("position", 2);
        item2.put("name", "Comparisons");
        item2.put("item", "https://scoop-analytics.com/comparisons");
        itemList.add(item2);

        // This comparison
        ObjectNode item3 = objectMapper.createObjectNode();
        item3.put("@type", "ListItem");
        item3.put("position", 3);
        item3.put("name", competitorA + " vs " + competitorB + " vs Scoop");
        itemList.add(item3);

        schema.set("itemListElement", itemList);

        try {
            return "<!-- Breadcrumb Schema -->\n" +
                   "<script type=\"application/ld+json\">\n" +
                   objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(schema) +
                   "\n</script>";
        } catch (Exception e) {
            return "";
        }
    }

    /**
     * Generate complete schema markup for a comparison.
     */
    public String generateCompleteSchema(ThreeWayComparison comparison) {
        StringBuilder schemas = new StringBuilder();

        // Add FAQ schema
        if (comparison.getFaqSection() != null && !comparison.getFaqSection().isEmpty()) {
            schemas.append(generateFAQSchema(comparison.getFaqSection())).append("\n\n");
        }

        // Add Product schema
        if (comparison.getCompetitorA() != null && comparison.getCompetitorB() != null) {
            schemas.append(generateProductSchema(
                comparison.getCompetitorA().getName(),
                comparison.getCompetitorB().getName(),
                comparison.getCompetitorA().getBuaScore().getTotalScore(),
                comparison.getCompetitorB().getBuaScore().getTotalScore()
            )).append("\n\n");
        }

        // Add SoftwareApplication schema
        schemas.append(generateSoftwareApplicationSchema()).append("\n\n");

        // Add Breadcrumb schema
        if (comparison.getCompetitorA() != null && comparison.getCompetitorB() != null) {
            schemas.append(generateBreadcrumbSchema(
                comparison.getCompetitorA().getName(),
                comparison.getCompetitorB().getName()
            ));
        }

        return schemas.toString();
    }
}