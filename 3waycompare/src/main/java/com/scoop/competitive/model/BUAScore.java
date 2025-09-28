package com.scoop.competitive.model;

import java.util.HashMap;
import java.util.Map;

/**
 * Business User Autonomy (BUA) Framework Score (100-point system).
 * 5 dimensions, each with multiple components.
 */
public class BUAScore {
    // Total score (out of 100)
    private int totalScore;
    private String category; // A, B, C, D, E, F
    private String categoryDescription;

    // Dimension scores (out of 20 each)
    private Dimension autonomy;  // /20
    private Dimension flow;      // /20
    private Dimension understanding; // /20
    private Dimension presentation;  // /20
    private Dimension data;      // /20

    // Component scores with justifications
    private Map<String, ComponentScore> componentScores;

    public BUAScore() {
        this.componentScores = new HashMap<>();
    }

    // Nested class for dimension scores
    public static class Dimension {
        private String name;
        private int score;
        private int maxScore;
        private String reasoning;
        private Map<String, ComponentScore> components;

        public Dimension() {
            this.components = new HashMap<>();
        }

        public Dimension(String name, int score, int maxScore) {
            this.name = name;
            this.score = score;
            this.maxScore = maxScore;
            this.components = new HashMap<>();
        }

        // Getters and Setters
        public String getName() { return name; }
        public void setName(String name) { this.name = name; }

        public int getScore() { return score; }
        public void setScore(int score) { this.score = score; }

        public int getMaxScore() { return maxScore; }
        public void setMaxScore(int maxScore) { this.maxScore = maxScore; }

        public String getReasoning() { return reasoning; }
        public void setReasoning(String reasoning) { this.reasoning = reasoning; }

        public Map<String, ComponentScore> getComponents() { return components; }
        public void setComponents(Map<String, ComponentScore> components) {
            this.components = components;
        }

        public void addComponent(String name, ComponentScore score) {
            this.components.put(name, score);
        }
    }

    // Nested class for individual component scores
    public static class ComponentScore {
        private String name;
        private int score;
        private int maxScore;
        private String evidence;
        private String source;
        private String reasoning;

        public ComponentScore() {}

        public ComponentScore(String name, int score, int maxScore,
                            String evidence, String reasoning) {
            this.name = name;
            this.score = score;
            this.maxScore = maxScore;
            this.evidence = evidence;
            this.reasoning = reasoning;
        }

        // Getters and Setters
        public String getName() { return name; }
        public void setName(String name) { this.name = name; }

        public int getScore() { return score; }
        public void setScore(int score) { this.score = score; }

        public int getMaxScore() { return maxScore; }
        public void setMaxScore(int maxScore) { this.maxScore = maxScore; }

        public String getEvidence() { return evidence; }
        public void setEvidence(String evidence) { this.evidence = evidence; }

        public String getSource() { return source; }
        public void setSource(String source) { this.source = source; }

        public String getReasoning() { return reasoning; }
        public void setReasoning(String reasoning) { this.reasoning = reasoning; }
    }

    // Getters and Setters
    public int getTotalScore() { return totalScore; }
    public void setTotalScore(int totalScore) { this.totalScore = totalScore; }

    public String getCategory() { return category; }
    public void setCategory(String category) { this.category = category; }

    public String getCategoryDescription() { return categoryDescription; }
    public void setCategoryDescription(String categoryDescription) {
        this.categoryDescription = categoryDescription;
    }

    public Dimension getAutonomy() { return autonomy; }
    public void setAutonomy(Dimension autonomy) { this.autonomy = autonomy; }

    public Dimension getFlow() { return flow; }
    public void setFlow(Dimension flow) { this.flow = flow; }

    public Dimension getUnderstanding() { return understanding; }
    public void setUnderstanding(Dimension understanding) { this.understanding = understanding; }

    public Dimension getPresentation() { return presentation; }
    public void setPresentation(Dimension presentation) { this.presentation = presentation; }

    public Dimension getData() { return data; }
    public void setData(Dimension data) { this.data = data; }

    public Map<String, ComponentScore> getComponentScores() { return componentScores; }
    public void setComponentScores(Map<String, ComponentScore> componentScores) {
        this.componentScores = componentScores;
    }

    /**
     * Calculate category based on total score
     */
    public void calculateCategory() {
        if (totalScore >= 70) {
            this.category = "A";
            this.categoryDescription = "Strong - Business Empowerment";
        } else if (totalScore >= 55) {
            this.category = "B";
            this.categoryDescription = "Good - Analyst Workbench";
        } else if (totalScore >= 40) {
            this.category = "C";
            this.categoryDescription = "Adequate - Enterprise Platform";
        } else if (totalScore >= 25) {
            this.category = "D";
            this.categoryDescription = "Weak - IT-Dependent";
        } else if (totalScore >= 10) {
            this.category = "E";
            this.categoryDescription = "Poor - Limited Capabilities";
        } else {
            this.category = "F";
            this.categoryDescription = "Minimal - Marketing Claims";
        }
    }

    @Override
    public String toString() {
        return "BUAScore{" +
                "totalScore=" + totalScore + "/100" +
                ", category='" + category + '\'' +
                ", autonomy=" + (autonomy != null ? autonomy.getScore() : "N/A") + "/20" +
                ", flow=" + (flow != null ? flow.getScore() : "N/A") + "/20" +
                ", understanding=" + (understanding != null ? understanding.getScore() : "N/A") + "/20" +
                ", presentation=" + (presentation != null ? presentation.getScore() : "N/A") + "/20" +
                ", data=" + (data != null ? data.getScore() : "N/A") + "/20" +
                '}';
    }
}