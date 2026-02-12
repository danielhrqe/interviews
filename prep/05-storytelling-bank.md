# Storytelling Bank - Cross-Company

> Sources: [QA storytelling](../companies/quintoandar/storytelling.md), all [research.md](../companies/) files

---

## 1. Story Inventory

### Story A: A Plataforma (Technical Leadership)
**1-line**: Built a global ML/data platform from scratch, growing from solo IC to leading a 9-person team, serving 150+ models and 70K executions/day.

**STAR Skeleton:**
- **S**: 5 different platforms worldwide, no standardization, orphaned infrastructure
- **T**: Build centralized platform for 600+ engineers/DS globally
- **A**: Designed architecture (Azure, Databricks/Spark, Airflow, K8s, ArgoCD, Terraform), created template system for standardized ML workflows, implemented trunk-based dev with 3-min deploys, grew team from 1→9+manager
- **R**: 70K+ exec/day, 150+ models in production, 5 legacy platforms decommissioned, global standard

**Tags**: `technical` `architecture` `hands-on` `team-building` `scaling` `MLOps`

---

### Story B: Expansão Global (Leadership & Resilience)
**1-line**: Led worldwide adoption of the platform against cultural resistance, hitting all migration targets through stakeholder management and adaptive leadership.

**STAR Skeleton:**
- **S**: Platform built, now needed worldwide adoption. Targets: 60% of 30K datasets (zone A), 50% of 5K datasets (zone B), 50+ ML models
- **T**: Convince resistant regional teams to migrate from their working tools
- **A**: Found early adopters (teams with most pain), delivered quick wins for domino effect, managed team emotion under high pressure, made strategic exceptions when needed, balanced hands-on technical work with stakeholder alignment
- **R**: All migration targets met, 600+ global users, personal growth as a more complete leader

**Tags**: `leadership` `stakeholder-mgmt` `conflict` `resilience` `cross-cultural` `change-mgmt`

---

### Story C: Recomendação (ML Hands-On)
**1-line**: Built a recommendation system at Zé Delivery using collaborative filtering (MBA project → production MVP).

**STAR Skeleton:**
- **S**: MBA project + real implementation at Zé Delivery (2019)
- **T**: Recommend products based on user profile and behavior of similar users
- **A**: Implemented graph-based collaborative + content-based filtering
- **R**: Good initial results, but project didn't continue after departure

**Tags**: `ML` `recommendation` `hands-on` `data-science`

**Note**: Keep this short (1 min). It bridges "I'm infra" → "I understand ML in practice."

---

### Story G1: Underperformer (TO DEVELOP)
**1-line**: [Fill in specific example]

**STAR Skeleton:**
- **S**: [Team member showing declining performance / missed expectations]
- **T**: Address performance while maintaining team morale
- **A**: 1) Identified root cause (skills gap? motivation? personal issue?), 2) Had direct, empathetic conversation, 3) Set clear expectations with timeline, 4) Provided specific support/resources, 5) Followed up regularly
- **R**: [Outcome: improved performance OR managed exit respectfully]

**Tags**: `performance-mgmt` `feedback` `people-leadership`

**Key for DoorDash**: They specifically ask about underperformers. The "ignore them" question tests if you're a people-first leader. Your answer should show: you CAN'T ignore them, you invest in people, AND you know when to make hard calls.

---

### Story G2: Critical Hire (TO DEVELOP)
**1-line**: [Fill in specific hire that transformed the team]

**STAR Skeleton:**
- **S**: [Team gap or scaling need]
- **T**: Find the right person for a critical role
- **A**: 1) Defined what the team actually needed (not just a job description), 2) Partnered with recruiting on sourcing strategy, 3) Designed evaluation criteria, 4) Sold the opportunity to the candidate
- **R**: [Impact after they joined: team velocity, culture, technical capability]

**Tags**: `hiring` `team-building` `recruiting-partnership`

---

### Story G3: Failure/Recovery (TO DEVELOP)
**1-line**: [Fill in project that failed or nearly failed]

**STAR Skeleton:**
- **S**: [Project at risk / thing that went wrong]
- **T**: Recover the situation
- **A**: 1) Acknowledged the problem early, 2) Root-caused it, 3) Took specific corrective actions, 4) Communicated transparently to stakeholders
- **R**: [Recovered or pivoted successfully + specific lessons learned]

**Tags**: `failure` `recovery` `accountability` `learning`

**Key**: Every company wants to hear about failure. Show self-awareness, accountability, and growth.

---

### Story G4: Cross-Functional Unblock (TO DEVELOP)
**1-line**: [Fill in example of removing a cross-team blocker]

**STAR Skeleton:**
- **S**: [Your team blocked by dependency on another team/org]
- **T**: Unblock without authority over the other team
- **A**: 1) Understood the other team's priorities, 2) Found win-win framing, 3) Escalated appropriately when needed, 4) Built the relationship for future collaboration
- **R**: [Unblocked, project delivered, lasting relationship built]

**Tags**: `cross-functional` `influence` `politics` `delivery`

---

## 2. Company Mapping Matrix

| Question Theme | Best Story | Backup | DD | Nubank | Wise | QA |
|---------------|------------|--------|-----|--------|------|-----|
| Technical leadership | **A: Plataforma** | C: Recomendação | ✓ | ✓ | ✓ | ✓ |
| Building a team | **A: Plataforma** | G2: Critical Hire | ✓ | ✓ | | |
| Stakeholder management | **B: Expansão** | G4: Cross-Func | ✓ | ✓ | ✓ | ✓ |
| Conflict / resistance | **B: Expansão** | G1: Underperformer | ✓ | ✓ | ✓ | |
| Underperformance | **G1: Underperformer** | B: Expansão (team emotion) | ✓ | | | |
| Critical hire | **G2: Critical Hire** | A: Plataforma (first hires) | ✓ | ✓ | | |
| Failure / recovery | **G3: Failure** | B: Expansão (challenges) | ✓ | ✓ | ✓ | |
| Cross-functional | **G4: Cross-Func** | B: Expansão (regions) | ✓ | ✓ | ✓ | |
| ML / data experience | **A: Plataforma** | C: Recomendação | | | | ✓ |
| Product thinking | **A: Plataforma** (template decisions) | B: Expansão (adoption) | | | ✓ | |
| IC → Manager transition | **A: Plataforma** | B: Expansão | ✓ | | | ✓ |

---

## 3. "Why Company?" Answers

### DoorDash
> Scale and complexity of three-sided marketplace. Culture of ownership and "1% better every day." The EM role combines platform-building (my strength) with DoorDash's engineering challenges at scale.

### Nubank
> Technical ambition (billions of events, immutable architecture). Data infrastructure challenges at scale match my experience. Engineering culture (functional programming as a principle, simplicity, self-service platforms).

### Wise
> Mission-driven ("Money without borders" is a real problem). Financial systems at scale (consistency, idempotency, multi-currency). Staff role expectations (own technical AND product roadmaps) match how I work.

### QuintoAndar (already detailed in [storytelling.md](../companies/quintoandar/storytelling.md))
> Customer-oriented culture. Innovation and collaborative environment. MLOps challenge is very similar to what I built. Stack alignment (ML Pipeline, Kafka monitoring, feature store).

---

## 4. Adaptation Notes

### Same story, different emphasis

**Story A: Plataforma**
- **For DoorDash**: Emphasize team building (1→9), engineering excellence (templates, CI/CD), results (70K/day)
- **For Nubank**: Emphasize data infrastructure parallels, Spark/K8s, functional approach to templates
- **For Wise**: Emphasize ownership (ideation → production), product decisions (template design), simplicity
- **For QA**: Emphasize MLOps, model serving, experiment tracking, similarity to their stack

**Story B: Expansão**
- **For DoorDash**: Emphasize stakeholder management, hitting targets, team leadership under pressure
- **For Nubank**: Emphasize cross-team collaboration, cultural adaptation, data-driven decisions
- **For Wise**: Emphasize product adoption (users choosing to use your platform), pragmatic exceptions
- **For QA**: Emphasize global scale, managing change, connecting tech to business value

### Universal tweaks
- **DoorDash**: Lead with NUMBERS and IMPACT. They care about business outcomes.
- **Nubank**: Lead with LEARNING and COLLABORATION. They care about culture fit.
- **Wise**: Lead with SIMPLICITY and PRODUCT JUDGMENT. They care about pragmatism.
- **QA**: Lead with TECH STACK CONNECTION. They care about relevance to their problems.
