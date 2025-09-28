package com.scoop.competitive.model;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Represents a complete 3-way comparison page (A vs B vs Scoop).
 * Contains all 15 sections from the template.
 */
public class ThreeWayComparison {
    // Meta information
    private String title;
    private String slug; // URL slug
    private String seoTitle;
    private String metaDescription;
    private String primaryKeyword;
    private List<String> questionCluster;
    private Map<String, List<String>> keywordClusters;

    // Competitors
    private Competitor competitorA;
    private Competitor competitorB;
    private ScoopCapabilities scoop;

    // Section content (15 sections)
    private ExecutiveSummary executiveSummary;
    private ComparisonMatrix atAGlanceMatrix;
    private String comparisonContext;
    private BUADeepDive buaDeepDive;
    private CapabilityDeepDive capabilityDeepDive;
    private String competitiveBattlefield;
    private AsymmetricAdvantages asymmetricAdvantages;
    private String sharedBlindSpot;
    private CostAnalysis costAnalysis;
    private UseCaseMatrix useCaseMatrix;
    private MigrationGuide migrationGuide;
    private List<FAQQuestion> faqSection;
    private EvidenceIndex evidenceIndex;
    private String bottomLine;

    // Schema markup
    private String faqPageSchema;
    private String productSchema;
    private String organizationSchema;

    // Metadata
    private LocalDate lastUpdated;
    private int wordCount;
    private int citationCount;
    private double fleschScore;
    private int aeoScore; // 0-50 points

    public ThreeWayComparison() {
        this.questionCluster = new ArrayList<>();
        this.faqSection = new ArrayList<>();
    }

    // Nested classes for structured sections

    public static class ExecutiveSummary {
        private String tldrVerdict; // 40-60 words
        private String whatIsScoop; // 40-60 words anchor
        private String chooseScoopIf; // Bullet list
        private String considerAIf;
        private String considerBIf;
        private String bottomLine; // 150 words

        public String getTldrVerdict() { return tldrVerdict; }
        public void setTldrVerdict(String tldrVerdict) { this.tldrVerdict = tldrVerdict; }

        public String getWhatIsScoop() { return whatIsScoop; }
        public void setWhatIsScoop(String whatIsScoop) { this.whatIsScoop = whatIsScoop; }

        public String getChooseScoopIf() { return chooseScoopIf; }
        public void setChooseScoopIf(String chooseScoopIf) { this.chooseScoopIf = chooseScoopIf; }

        public String getConsiderAIf() { return considerAIf; }
        public void setConsiderAIf(String considerAIf) { this.considerAIf = considerAIf; }

        public String getConsiderBIf() { return considerBIf; }
        public void setConsiderBIf(String considerBIf) { this.considerBIf = considerBIf; }

        public String getBottomLine() { return bottomLine; }
        public void setBottomLine(String bottomLine) { this.bottomLine = bottomLine; }
    }

    public static class ComparisonMatrix {
        private List<MatrixRow> rows;

        public ComparisonMatrix() {
            this.rows = new ArrayList<>();
        }

        public List<MatrixRow> getRows() { return rows; }
        public void setRows(List<MatrixRow> rows) { this.rows = rows; }
    }

    public static class MatrixRow {
        private String dimension;
        private String competitorAValue;
        private String competitorBValue;
        private String scoopValue;
        private String keyInsight;

        public MatrixRow() {
            // Default constructor
        }

        public MatrixRow(String dimension, String aValue, String bValue,
                        String scoopValue, String insight) {
            this.dimension = dimension;
            this.competitorAValue = aValue;
            this.competitorBValue = bValue;
            this.scoopValue = scoopValue;
            this.keyInsight = insight;
        }

        // Getters and setters
        public String getDimension() { return dimension; }
        public void setDimension(String dimension) { this.dimension = dimension; }

        public String getCompetitorAValue() { return competitorAValue; }
        public void setCompetitorAValue(String competitorAValue) {
            this.competitorAValue = competitorAValue;
        }

        public String getCompetitorBValue() { return competitorBValue; }
        public void setCompetitorBValue(String competitorBValue) {
            this.competitorBValue = competitorBValue;
        }

        public String getScoopValue() { return scoopValue; }
        public void setScoopValue(String scoopValue) { this.scoopValue = scoopValue; }

        public String getKeyInsight() { return keyInsight; }
        public void setKeyInsight(String keyInsight) { this.keyInsight = keyInsight; }
    }

    public static class BUADeepDive {
        private String introduction;
        private DimensionComparison autonomy;
        private DimensionComparison flow;
        private DimensionComparison understanding;
        private DimensionComparison presentation;
        private DimensionComparison data;
        private String scoreSummary;

        public String getIntroduction() { return introduction; }
        public void setIntroduction(String introduction) { this.introduction = introduction; }

        public DimensionComparison getAutonomy() { return autonomy; }
        public void setAutonomy(DimensionComparison autonomy) { this.autonomy = autonomy; }

        public DimensionComparison getFlow() { return flow; }
        public void setFlow(DimensionComparison flow) { this.flow = flow; }

        public DimensionComparison getUnderstanding() { return understanding; }
        public void setUnderstanding(DimensionComparison understanding) {
            this.understanding = understanding;
        }

        public DimensionComparison getPresentation() { return presentation; }
        public void setPresentation(DimensionComparison presentation) {
            this.presentation = presentation;
        }

        public DimensionComparison getData() { return data; }
        public void setData(DimensionComparison data) { this.data = data; }

        public String getScoreSummary() { return scoreSummary; }
        public void setScoreSummary(String scoreSummary) { this.scoreSummary = scoreSummary; }
    }

    public static class DimensionComparison {
        private String dimensionName;
        private List<ComponentComparison> components;
        private String extractableSummary; // 40-60 word summary for AEO

        public DimensionComparison() {
            this.components = new ArrayList<>();
        }

        public String getDimensionName() { return dimensionName; }
        public void setDimensionName(String dimensionName) { this.dimensionName = dimensionName; }

        public List<ComponentComparison> getComponents() { return components; }
        public void setComponents(List<ComponentComparison> components) {
            this.components = components;
        }

        public String getExtractableSummary() { return extractableSummary; }
        public void setExtractableSummary(String extractableSummary) {
            this.extractableSummary = extractableSummary;
        }
    }

    public static class ComponentComparison {
        private String componentName;
        private int competitorAScore;
        private int competitorBScore;
        private int scoopScore;
        private int maxScore;
        private String aReasoning;
        private String bReasoning;
        private String scoopReasoning;
        private String advantageExplanation;

        public String getComponentName() { return componentName; }
        public void setComponentName(String componentName) { this.componentName = componentName; }

        public int getCompetitorAScore() { return competitorAScore; }
        public void setCompetitorAScore(int competitorAScore) {
            this.competitorAScore = competitorAScore;
        }

        public int getCompetitorBScore() { return competitorBScore; }
        public void setCompetitorBScore(int competitorBScore) {
            this.competitorBScore = competitorBScore;
        }

        public int getScoopScore() { return scoopScore; }
        public void setScoopScore(int scoopScore) { this.scoopScore = scoopScore; }

        public int getMaxScore() { return maxScore; }
        public void setMaxScore(int maxScore) { this.maxScore = maxScore; }

        public String getaReasoning() { return aReasoning; }
        public void setaReasoning(String aReasoning) { this.aReasoning = aReasoning; }

        public String getbReasoning() { return bReasoning; }
        public void setbReasoning(String bReasoning) { this.bReasoning = bReasoning; }

        public String getScoopReasoning() { return scoopReasoning; }
        public void setScoopReasoning(String scoopReasoning) {
            this.scoopReasoning = scoopReasoning;
        }

        public String getAdvantageExplanation() { return advantageExplanation; }
        public void setAdvantageExplanation(String advantageExplanation) {
            this.advantageExplanation = advantageExplanation;
        }
    }

    public static class CapabilityDeepDive {
        private String investigationAnalysis;
        private String sideByByScenario;
        private String spreadsheetEngine;
        private String mlPatternDiscovery;
        private String workflowIntegration;

        public String getInvestigationAnalysis() { return investigationAnalysis; }
        public void setInvestigationAnalysis(String investigationAnalysis) {
            this.investigationAnalysis = investigationAnalysis;
        }

        public String getSideByByScenario() { return sideByByScenario; }
        public void setSideByByScenario(String sideByByScenario) {
            this.sideByByScenario = sideByByScenario;
        }

        public String getSpreadsheetEngine() { return spreadsheetEngine; }
        public void setSpreadsheetEngine(String spreadsheetEngine) {
            this.spreadsheetEngine = spreadsheetEngine;
        }

        public String getMlPatternDiscovery() { return mlPatternDiscovery; }
        public void setMlPatternDiscovery(String mlPatternDiscovery) {
            this.mlPatternDiscovery = mlPatternDiscovery;
        }

        public String getWorkflowIntegration() { return workflowIntegration; }
        public void setWorkflowIntegration(String workflowIntegration) {
            this.workflowIntegration = workflowIntegration;
        }
    }

    public static class AsymmetricAdvantages {
        private List<String> whereABeatsB;
        private List<String> whereBBeatsA;
        private List<String> whereScoopBeatsBoth;

        public AsymmetricAdvantages() {
            this.whereABeatsB = new ArrayList<>();
            this.whereBBeatsA = new ArrayList<>();
            this.whereScoopBeatsBoth = new ArrayList<>();
        }

        public List<String> getWhereABeatsB() { return whereABeatsB; }
        public void setWhereABeatsB(List<String> whereABeatsB) {
            this.whereABeatsB = whereABeatsB;
        }

        public List<String> getWhereBBeatsA() { return whereBBeatsA; }
        public void setWhereBBeatsA(List<String> whereBBeatsA) {
            this.whereBBeatsA = whereBBeatsA;
        }

        public List<String> getWhereScoopBeatsBoth() { return whereScoopBeatsBoth; }
        public void setWhereScoopBeatsBoth(List<String> whereScoopBeatsBoth) {
            this.whereScoopBeatsBoth = whereScoopBeatsBoth;
        }
    }

    public static class CostAnalysis {
        private TCOBreakdown competitorA;
        private TCOBreakdown competitorB;
        private TCOBreakdown scoop;
        private String interpretation;

        public TCOBreakdown getCompetitorA() { return competitorA; }
        public void setCompetitorA(TCOBreakdown competitorA) {
            this.competitorA = competitorA;
        }

        public TCOBreakdown getCompetitorB() { return competitorB; }
        public void setCompetitorB(TCOBreakdown competitorB) {
            this.competitorB = competitorB;
        }

        public TCOBreakdown getScoop() { return scoop; }
        public void setScoop(TCOBreakdown scoop) { this.scoop = scoop; }

        public String getInterpretation() { return interpretation; }
        public void setInterpretation(String interpretation) {
            this.interpretation = interpretation;
        }
    }

    public static class TCOBreakdown {
        private String licenses;
        private String implementation;
        private String training;
        private String maintenance;
        private String consultants;
        private String productivityLoss;
        private String total;

        public String getLicenses() { return licenses; }
        public void setLicenses(String licenses) { this.licenses = licenses; }

        public String getImplementation() { return implementation; }
        public void setImplementation(String implementation) {
            this.implementation = implementation;
        }

        public String getTraining() { return training; }
        public void setTraining(String training) { this.training = training; }

        public String getMaintenance() { return maintenance; }
        public void setMaintenance(String maintenance) { this.maintenance = maintenance; }

        public String getConsultants() { return consultants; }
        public void setConsultants(String consultants) { this.consultants = consultants; }

        public String getProductivityLoss() { return productivityLoss; }
        public void setProductivityLoss(String productivityLoss) {
            this.productivityLoss = productivityLoss;
        }

        public String getTotal() { return total; }
        public void setTotal(String total) { this.total = total; }
    }

    public static class UseCaseMatrix {
        private List<UseCaseRow> rows;

        public UseCaseMatrix() {
            this.rows = new ArrayList<>();
        }

        public List<UseCaseRow> getRows() { return rows; }
        public void setRows(List<UseCaseRow> rows) { this.rows = rows; }
    }

    public static class UseCaseRow {
        private String scenario;
        private String recommendation;
        private String rationale;
        private String tradeoff;

        public String getScenario() { return scenario; }
        public void setScenario(String scenario) { this.scenario = scenario; }

        public String getRecommendation() { return recommendation; }
        public void setRecommendation(String recommendation) {
            this.recommendation = recommendation;
        }

        public String getRationale() { return rationale; }
        public void setRationale(String rationale) { this.rationale = rationale; }

        public String getTradeoff() { return tradeoff; }
        public void setTradeoff(String tradeoff) { this.tradeoff = tradeoff; }
    }

    public static class MigrationGuide {
        private MigrationPath fromA;
        private MigrationPath fromB;
        private String whyMigrate;

        public MigrationPath getFromA() { return fromA; }
        public void setFromA(MigrationPath fromA) { this.fromA = fromA; }

        public MigrationPath getFromB() { return fromB; }
        public void setFromB(MigrationPath fromB) { this.fromB = fromB; }

        public String getWhyMigrate() { return whyMigrate; }
        public void setWhyMigrate(String whyMigrate) { this.whyMigrate = whyMigrate; }
    }

    public static class MigrationPath {
        private String whatTransfers;
        private String whatAbandoned;
        private String timeline;
        private String biggestRelief;
        private String biggestChallenge;

        public String getWhatTransfers() { return whatTransfers; }
        public void setWhatTransfers(String whatTransfers) { this.whatTransfers = whatTransfers; }

        public String getWhatAbandoned() { return whatAbandoned; }
        public void setWhatAbandoned(String whatAbandoned) {
            this.whatAbandoned = whatAbandoned;
        }

        public String getTimeline() { return timeline; }
        public void setTimeline(String timeline) { this.timeline = timeline; }

        public String getBiggestRelief() { return biggestRelief; }
        public void setBiggestRelief(String biggestRelief) {
            this.biggestRelief = biggestRelief;
        }

        public String getBiggestChallenge() { return biggestChallenge; }
        public void setBiggestChallenge(String biggestChallenge) {
            this.biggestChallenge = biggestChallenge;
        }
    }

    public static class FAQQuestion {
        private String question;
        private String answer; // 40-60 words
        private List<String> citations;

        public FAQQuestion() {
            this.citations = new ArrayList<>();
        }

        public FAQQuestion(String question, String answer) {
            this.question = question;
            this.answer = answer;
            this.citations = new ArrayList<>();
        }

        public String getQuestion() { return question; }
        public void setQuestion(String question) { this.question = question; }

        public String getAnswer() { return answer; }
        public void setAnswer(String answer) { this.answer = answer; }

        public List<String> getCitations() { return citations; }
        public void setCitations(List<String> citations) { this.citations = citations; }
    }

    public static class EvidenceIndex {
        private int totalCitations;
        private List<Citation> competitorACitations;
        private List<Citation> competitorBCitations;
        private List<Citation> scoopCitations;

        public EvidenceIndex() {
            this.competitorACitations = new ArrayList<>();
            this.competitorBCitations = new ArrayList<>();
            this.scoopCitations = new ArrayList<>();
        }

        public int getTotalCitations() { return totalCitations; }
        public void setTotalCitations(int totalCitations) {
            this.totalCitations = totalCitations;
        }

        public List<Citation> getCompetitorACitations() { return competitorACitations; }
        public void setCompetitorACitations(List<Citation> competitorACitations) {
            this.competitorACitations = competitorACitations;
        }

        public List<Citation> getCompetitorBCitations() { return competitorBCitations; }
        public void setCompetitorBCitations(List<Citation> competitorBCitations) {
            this.competitorBCitations = competitorBCitations;
        }

        public List<Citation> getScoopCitations() { return scoopCitations; }
        public void setScoopCitations(List<Citation> scoopCitations) {
            this.scoopCitations = scoopCitations;
        }
    }

    public static class Citation {
        private String claim;
        private String source;
        private String location;
        private String type; // BUA score, Customer quote, Official docs, Pricing, Technical

        public String getClaim() { return claim; }
        public void setClaim(String claim) { this.claim = claim; }

        public String getSource() { return source; }
        public void setSource(String source) { this.source = source; }

        public String getLocation() { return location; }
        public void setLocation(String location) { this.location = location; }

        public String getType() { return type; }
        public void setType(String type) { this.type = type; }
    }

    public static class ScoopCapabilities {
        private String spreadsheetEngine;
        private String aiDataScientist;
        private String multiPassInvestigation;
        private String visualIntelligence;
        private String nativeWorkflowIntegration;
        private int buaScore = 82; // Fixed for Scoop

        public String getSpreadsheetEngine() { return spreadsheetEngine; }
        public void setSpreadsheetEngine(String spreadsheetEngine) {
            this.spreadsheetEngine = spreadsheetEngine;
        }

        public String getAiDataScientist() { return aiDataScientist; }
        public void setAiDataScientist(String aiDataScientist) {
            this.aiDataScientist = aiDataScientist;
        }

        public String getMultiPassInvestigation() { return multiPassInvestigation; }
        public void setMultiPassInvestigation(String multiPassInvestigation) {
            this.multiPassInvestigation = multiPassInvestigation;
        }

        public String getVisualIntelligence() { return visualIntelligence; }
        public void setVisualIntelligence(String visualIntelligence) {
            this.visualIntelligence = visualIntelligence;
        }

        public String getNativeWorkflowIntegration() { return nativeWorkflowIntegration; }
        public void setNativeWorkflowIntegration(String nativeWorkflowIntegration) {
            this.nativeWorkflowIntegration = nativeWorkflowIntegration;
        }

        public int getBuaScore() { return buaScore; }
        public void setBuaScore(int buaScore) { this.buaScore = buaScore; }
    }

    // Main class getters and setters
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public String getSlug() { return slug; }
    public void setSlug(String slug) { this.slug = slug; }

    public String getSeoTitle() { return seoTitle; }
    public void setSeoTitle(String seoTitle) { this.seoTitle = seoTitle; }

    public String getMetaDescription() { return metaDescription; }
    public void setMetaDescription(String metaDescription) {
        this.metaDescription = metaDescription;
    }

    public String getPrimaryKeyword() { return primaryKeyword; }
    public void setPrimaryKeyword(String primaryKeyword) {
        this.primaryKeyword = primaryKeyword;
    }

    public List<String> getQuestionCluster() { return questionCluster; }
    public void setQuestionCluster(List<String> questionCluster) {
        this.questionCluster = questionCluster;
    }

    public Map<String, List<String>> getKeywordClusters() { return keywordClusters; }
    public void setKeywordClusters(Map<String, List<String>> keywordClusters) {
        this.keywordClusters = keywordClusters;
    }

    public Competitor getCompetitorA() { return competitorA; }
    public void setCompetitorA(Competitor competitorA) { this.competitorA = competitorA; }

    public Competitor getCompetitorB() { return competitorB; }
    public void setCompetitorB(Competitor competitorB) { this.competitorB = competitorB; }

    public ScoopCapabilities getScoop() { return scoop; }
    public void setScoop(ScoopCapabilities scoop) { this.scoop = scoop; }

    public ExecutiveSummary getExecutiveSummary() { return executiveSummary; }
    public void setExecutiveSummary(ExecutiveSummary executiveSummary) {
        this.executiveSummary = executiveSummary;
    }

    public ComparisonMatrix getAtAGlanceMatrix() { return atAGlanceMatrix; }
    public void setAtAGlanceMatrix(ComparisonMatrix atAGlanceMatrix) {
        this.atAGlanceMatrix = atAGlanceMatrix;
    }

    public String getComparisonContext() { return comparisonContext; }
    public void setComparisonContext(String comparisonContext) {
        this.comparisonContext = comparisonContext;
    }

    public BUADeepDive getBuaDeepDive() { return buaDeepDive; }
    public void setBuaDeepDive(BUADeepDive buaDeepDive) { this.buaDeepDive = buaDeepDive; }

    public CapabilityDeepDive getCapabilityDeepDive() { return capabilityDeepDive; }
    public void setCapabilityDeepDive(CapabilityDeepDive capabilityDeepDive) {
        this.capabilityDeepDive = capabilityDeepDive;
    }

    public String getCompetitiveBattlefield() { return competitiveBattlefield; }
    public void setCompetitiveBattlefield(String competitiveBattlefield) {
        this.competitiveBattlefield = competitiveBattlefield;
    }

    public AsymmetricAdvantages getAsymmetricAdvantages() { return asymmetricAdvantages; }
    public void setAsymmetricAdvantages(AsymmetricAdvantages asymmetricAdvantages) {
        this.asymmetricAdvantages = asymmetricAdvantages;
    }

    public String getSharedBlindSpot() { return sharedBlindSpot; }
    public void setSharedBlindSpot(String sharedBlindSpot) {
        this.sharedBlindSpot = sharedBlindSpot;
    }

    public CostAnalysis getCostAnalysis() { return costAnalysis; }
    public void setCostAnalysis(CostAnalysis costAnalysis) { this.costAnalysis = costAnalysis; }

    public UseCaseMatrix getUseCaseMatrix() { return useCaseMatrix; }
    public void setUseCaseMatrix(UseCaseMatrix useCaseMatrix) {
        this.useCaseMatrix = useCaseMatrix;
    }

    public MigrationGuide getMigrationGuide() { return migrationGuide; }
    public void setMigrationGuide(MigrationGuide migrationGuide) {
        this.migrationGuide = migrationGuide;
    }

    public List<FAQQuestion> getFaqSection() { return faqSection; }
    public void setFaqSection(List<FAQQuestion> faqSection) { this.faqSection = faqSection; }

    public EvidenceIndex getEvidenceIndex() { return evidenceIndex; }
    public void setEvidenceIndex(EvidenceIndex evidenceIndex) {
        this.evidenceIndex = evidenceIndex;
    }

    public String getBottomLine() { return bottomLine; }
    public void setBottomLine(String bottomLine) { this.bottomLine = bottomLine; }

    public String getFaqPageSchema() { return faqPageSchema; }
    public void setFaqPageSchema(String faqPageSchema) { this.faqPageSchema = faqPageSchema; }

    public String getProductSchema() { return productSchema; }
    public void setProductSchema(String productSchema) { this.productSchema = productSchema; }

    public String getOrganizationSchema() { return organizationSchema; }
    public void setOrganizationSchema(String organizationSchema) {
        this.organizationSchema = organizationSchema;
    }

    public LocalDate getLastUpdated() { return lastUpdated; }
    public void setLastUpdated(LocalDate lastUpdated) { this.lastUpdated = lastUpdated; }

    public int getWordCount() { return wordCount; }
    public void setWordCount(int wordCount) { this.wordCount = wordCount; }

    public int getCitationCount() { return citationCount; }
    public void setCitationCount(int citationCount) { this.citationCount = citationCount; }

    public double getFleschScore() { return fleschScore; }
    public void setFleschScore(double fleschScore) { this.fleschScore = fleschScore; }

    public int getAeoScore() { return aeoScore; }
    public void setAeoScore(int aeoScore) { this.aeoScore = aeoScore; }
}