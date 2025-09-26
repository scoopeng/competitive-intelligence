# Qlik BUPAF Scoring - Evidence-Based Assessment

## BUPAF Framework Overview
Business User Power Assessment Framework - Evaluating true business user empowerment

## Dimension 1: Independence (Can business users work alone?)
**Score: 2/10**

### Evidence Points:
1. **Customer Quote**: "Not very friendly to our users to build their own dashboards. They really depend on the developers to do the coding" (Phase 1 - Capterra)

2. **Training Requirements**:
   - Certification exam: 2 hours, 50-60 questions, 58% pass rate (Phase 3)
   - Must know SQL, ETL, data modeling (Phase 2)
   - "Significant preparation needed" (Phase 3)

3. **IT Dependency**:
   - "Interact with IT professionals to ensure seamless integration" (Phase 2)
   - Port 443 must be opened by IT (Phase 2)
   - User permissions and entitlements managed by IT (Phase 2)

4. **Consultant Requirements**:
   - "Seasoned specialists with 5-15 years experience needed" (Phase 1)
   - Consultant rates: $50-76/hour (Phase 3)
   - "Organization misses real upside of BI" without specialists (Phase 1)

5. **Setup Timeline**:
   - "Few hours to few months" for implementation (Phase 2)
   - Simple setup: 5 days minimum (Phase 2)
   - Compare to Scoop: 30 seconds (Phase 2)

**Verdict**: Business users cannot work independently. Requires IT support, extensive training, and often consultants.

## Dimension 2: Analytical Depth (Investigation vs single queries)
**Score: 4/10**

### Evidence Points:
1. **Single Query Limitation**:
   - No multi-pass reasoning capability found (Phase 2)
   - Cannot test multiple hypotheses automatically (Phase 2)
   - User must manually explore relationships (Phase 2)

2. **ML/AI Reality**:
   - "No-code but requires understanding of ML concepts" (Phase 2)
   - "Models need manual training and deployment" (Phase 2)
   - "Not automatic - user must initiate and configure" (Phase 2)

3. **Root Cause Analysis**:
   - Associative model allows exploration but "user drives investigation manually" (Phase 2)
   - No automatic investigation features found (Phase 2)
   - Cannot answer "why" questions without manual analysis (Phase 2)

4. **Performance Impact**:
   - "Weeks trying to debug simple data model issue" (Phase 1)
   - Poor error messages hinder investigation (Phase 1)
   - 55-second API timeout limits complex analysis (Phase 3)

5. **Accuracy Issues**:
   - "Synthetic key generation indicates poor data structure" (Phase 1)
   - "Working as designed" responses to errors (Phase 1)

**Verdict**: Limited to single queries and manual exploration. No automatic investigation or hypothesis testing.

## Dimension 3: Workflow Integration (Excel, Slack, PowerPoint)
**Score: 2/10**

### Evidence Points:
1. **Excel Integration Failure**:
   - "QlikView formulas cannot be directly exported as Excel formulas" (Phase 2)
   - Static data export only, no formula conversion (Phase 2)
   - Third-party extensions required for Excel-like features (Phase 2)
   - No live connection to Excel (Phase 2)

2. **Slack Integration Complexity**:
   - Requires automation setup and configuration (Phase 2)
   - "Send chart image to Slack" but no native integration (Phase 2)
   - Multiple steps and configuration needed (Phase 2)

3. **PowerPoint Generation**:
   - No direct PowerPoint generation capability found (Phase 2)
   - Cannot generate presentations, only send images (Phase 2)

4. **Mobile Experience**:
   - "Terrible performing apps" on mobile (Phase 3)
   - "Features malfunctioning in iOS" (Phase 1)
   - Charts taking over a minute to load on mobile (Phase 3)

5. **API/Embedding Issues**:
   - "Refused to frame" CSP violations (Phase 3)
   - OAuth limitations for iframe embedding (Phase 3)
   - API rate limits: 429 Too Many Requests common (Phase 3)

**Verdict**: Completely fails at preserving business user workflows. No Excel engine, complex integrations, poor mobile.

## Dimension 4: Business Communication (Natural language)
**Score: 3/10**

### Evidence Points:
1. **NLP Limitations**:
   - Cannot handle typos - "one typo = query fails" (Phase 2)
   - Requires exact field names (Phase 2)
   - Cannot understand synonyms or variations (Phase 2)
   - "Requires Business Logic customization" (Phase 2)

2. **Language Support Issues**:
   - "Storytelling feature has limitations with Japanese/Chinese" (Phase 1)
   - Server fails to handle these characters properly (Phase 1)

3. **Training Burden**:
   - "Paradigm shift from traditional BI tools" (Phase 1)
   - "Coding of equations is quite complicated" (Phase 1)
   - "Struggle a lot with customization" (Phase 1)

4. **Communication Barriers**:
   - 74% of employees "overwhelmed or unhappy" with data (Phase 3)
   - 31% took sick leave due to data-related stress (Phase 3)
   - "Data team acting as reporting service desk" (Phase 1)

5. **Query Complexity**:
   - Set analysis and AGGR functions required (Phase 3)
   - Must understand data models and relationships (Phase 2)
   - "Proficient in SQL and relational databases" required (Phase 2)

**Verdict**: Not actually natural language. Requires technical syntax, breaks on typos, overwhelming for business users.

## Dimension 5: Visual Intelligence (Presentation-ready)
**Score: 5/10**

### Evidence Points:
1. **Visualization Strengths**:
   - Score of 9.4 for data visualization vs competitors (Phase 3)
   - GeoAnalytics for spatial data (Phase 2)
   - Dashboard and analytics visualization capabilities (Phase 2)

2. **Export Limitations**:
   - Formatting and conditional logic lost in export (Phase 2)
   - Static exports lose all interactivity (Phase 2)
   - Maximum 500 unique reports per task (Phase 3)

3. **Performance Issues**:
   - "Sheets and dashboards taking up to an hour to load" (Phase 1)
   - "3-4 seconds to display sheet list" (Phase 3)
   - 4-hour maximum execution time for reports (Phase 3)

4. **Presentation Gaps**:
   - No PowerPoint generation capability (Phase 2)
   - Cannot create narratives automatically (Phase 2)
   - Manual formatting required for presentations

5. **Visual Quality Concerns**:
   - "Qlik looks outdated in terms of UX and visuals" (Phase 3)
   - "Visual output lacks polish of Tableau or Power BI" (Phase 1)

**Verdict**: Good visualization capabilities undermined by performance issues and lack of presentation features.

## TOTAL BUPAF SCORE: 16/50

### Category: C (15-24) - Enterprise Platform
Qlik is an enterprise platform requiring significant IT support, not a business user empowerment tool.

## Competitive Comparison

| Dimension | Qlik | Scoop | Evidence |
|-----------|------|-------|----------|
| Independence | 2/10 | 9/10 | "Depend on developers" vs 30-second setup |
| Analytical Depth | 4/10 | 9/10 | Single queries vs multi-pass investigation |
| Workflow Integration | 2/10 | 10/10 | No Excel engine vs 150+ functions |
| Business Communication | 3/10 | 9/10 | Typo-intolerant vs true NLP |
| Visual Intelligence | 5/10 | 8/10 | Hour-long loads vs instant presentations |
| **TOTAL** | **16/50** | **45/50** | Enterprise Platform vs Business Empowerment |

## Key Takeaways

### Fatal Flaws for Business Users:
1. **Training Wall**: Weeks of training, 58% certification pass rate
2. **IT Dependency**: Cannot work without IT support
3. **Workflow Disruption**: No Excel support, complex integrations
4. **Language Barrier**: Not actually natural language
5. **Performance Block**: Hour-long waits kill productivity

### Why This Matters:
Organizations buying Qlik for "self-service analytics" are being misled. The platform requires extensive IT support, weeks of training, and ongoing consultant help. Business users cannot and will not adopt it independently. The 16/50 BUPAF score reveals Qlik as an IT-centric enterprise platform, not a business user empowerment tool.

### Sales Positioning:
"Qlik scores 16/50 on business user empowerment - that's an 'F' grade. Your business users will never adopt it without extensive IT support. Scoop scores 45/50 because business users can actually use it alone, in their existing workflows, without any training."