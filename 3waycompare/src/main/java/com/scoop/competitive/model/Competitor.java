package com.scoop.competitive.model;

import java.time.LocalDate;
import java.util.List;
import java.util.Map;

/**
 * Represents a competitor with BUA scoring data.
 * Simplified for AI-powered generation that reads evidence files directly.
 */
public class Competitor {
    private String name;
    private String slug; // URL-friendly name (e.g., "power-bi-copilot")
    private String parent; // Parent company (e.g., "Microsoft")
    private String productType; // e.g., "Text-to-SQL interface", "Dashboard platform"

    // Core scoring data
    private BUAScore buaScore;

    // For AI generation - paths to evidence files
    private String basePath;
    private String category; // A-F based on BUA score

    // Constructors
    public Competitor() {}

    public Competitor(String name, String slug) {
        this.name = name;
        this.slug = slug;
    }

    // Getters and Setters
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getSlug() { return slug; }
    public void setSlug(String slug) { this.slug = slug; }

    public String getParent() { return parent; }
    public void setParent(String parent) { this.parent = parent; }

    public String getProductType() { return productType; }
    public void setProductType(String productType) { this.productType = productType; }


    public BUAScore getBuaScore() { return buaScore; }
    public void setBuaScore(BUAScore buaScore) { this.buaScore = buaScore; }

    public String getCategory() { return category; }
    public void setCategory(String category) { this.category = category; }

    public String getBasePath() { return basePath; }
    public void setBasePath(String basePath) { this.basePath = basePath; }

    @Override
    public String toString() {
        return "Competitor{" +
                "name='" + name + '\'' +
                ", buaScore=" + (buaScore != null ? buaScore.getTotalScore() : "N/A") +
                ", category='" + category + '\'' +
                '}';
    }
}