# Tableau Pulse - Competitive Intelligence

## Quick Summary
**Parent**: Salesforce  
**Category**: Dashboard Tool (BUA Score: 11/50)  
**Fatal Flaw**: Schema changes break everything  
**Key Fact**: NOT using LLMs (their admission) - just embedding models  

## The Scoop Advantage
- **Schema Evolution**: We adapt automatically, they break and require IT rebuild
- **True Investigation**: We discover WHY (3-10 queries), they just alert WHAT changed
- **Cost**: $3,588/year vs $165,000+/year for 200 users (46x more expensive)
- **Setup**: 30 seconds vs weeks/months

## Files in This Folder

### Sales Tools
- **[BATTLE_CARD.md](BATTLE_CARD.md)** - Quick reference for sales calls
- **[DEEP_ANALYSIS.md](DEEP_ANALYSIS.md)** - Enhanced battle card with BUA scores and detailed talk tracks

### Evidence & Proof Points
| Claim | Proof |
|-------|-------|
| "NOT using LLMs" | Salesforce documentation admits embedding models only |
| Schema breaks | "Pulse metrics can break" - their docs |
| Weeks to implement | 47-step setup guide |
| No investigation | Single metric alerts only |

## Key Differentiators

### 1. Schema Evolution (Their Achilles Heel)
- Add a column → Tableau Pulse breaks
- Change a type → Metrics fail
- Rename a field → Everything needs rebuilding
- **Demo this live** - it's undeniable

### 2. Alert vs Investigation
- **Tableau**: "Sales dropped 15%" (that's it)
- **Scoop**: "Sales dropped 15% because Northeast enterprise deals are stalling at contract review due to new procurement policies"

### 3. Business User Independence
- **Tableau**: Need Tableau license first, then IT setup
- **Scoop**: Upload spreadsheet, get answers immediately

## Discovery Questions
1. "What happens when you add a new column to your data?"
2. "Can Pulse investigate WHY metrics changed?"
3. "How long did your Pulse implementation take?"
4. "Can business users upload their own data?"

## Objection Handlers

**"We already have Tableau"**
→ "Perfect - Scoop complements Tableau beautifully. Your analysts keep building dashboards while business users get immediate answers."

**"Tableau is industry standard"**
→ "For dashboards, absolutely. But Pulse proves they know that's not enough. We built for investigation from day one, they're trying to bolt it on."

## Competitive Landmines
- Don't criticize Salesforce's size (they'll use it as stability)
- Don't call Pulse "useless" (it does basic alerts well)
- Emphasize schema evolution (they literally cannot do this)

## The Closing Line
"Would you rather have a system that tells you what happened, or one that figures out why and what to do about it?"

---

*Intelligence current as of: January 2025*  
*Tableau Pulse is just alerts. Scoop is investigation.*