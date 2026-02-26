# DoorDash - STAR Stories para Team Building & Hiring

## Como usar
- Pratique em voz alta, não apenas leia
- Cada história deve durar 2-3 minutos no máximo
- O entrevistador vai fazer follow-ups - as "perguntas esperadas" te preparam
- Foque no "EU fiz", não "NÓS fizemos"

---

## H1: Montei time de Data & ML do zero (0 → 21 pessoas)

**Use para:** Team building, hiring strategy, scaling, vision

### STAR

**Situation:**
When I joined, the company had no centralized data or ML platform. Every team was building their own pipelines — choosing their own languages, architectures, and tools independently. This created massive problems: security gaps, no governance, spiraling cloud costs, no clear ownership, and a growing pile of legacy systems that business teams depended on daily with zero reliability guarantees.

**Task:**
I was brought in to build this capability from scratch — not just the platform, but the entire team. I needed to define the vision, hire the right people, and deliver a platform that would become the company standard globally.

**Action:**
- **Hiring strategy:** I started by defining the profile I needed — not just coders, but people with strong system design thinking and solid fundamentals. I wanted engineers who could reason about architecture, not just write features.
- **Process design:** I partnered with our internal recruiting team. I wrote all job descriptions myself and designed the entire technical interview process: 5 structured questions covering REST API design, logic, data concepts, and a straightforward data structures problem. I intentionally kept the coding question simple because I was hiring for judgment and architectural thinking, not LeetCode skills.
- **Scaling approach:** I hired in waves aligned with platform milestones. First wave: senior engineers who could help define architecture. Second wave: mid-level engineers to build out the platform. Third wave: specialists (ML engineers, data engineers) as the platform matured.
- **Over 3 years**, I grew the team from 0 to 8-11 direct reports, and eventually to 21 people including indirect reports across multiple squads.

**Result:**
- **Regional platform (South America):** 300+ users, 100K+ datasets, 1,000 daily business users running queries, 1M API requests/day, 2M low-latency queries/day on our Kubernetes/Trino stack. Hundreds of dashboards used by directors and VPs for daily strategic decisions — mission-critical, if it went down, operations stopped.
- **Global platform (worldwide):** 600+ users, 100K+ datasets globally, 80K daily workload executions, 130 ML models in production, 4K Airflow DAGs, deployed across 8 availability zones worldwide.
- **Cost savings:** $2M reduction through code and infrastructure optimization.
- **Time-to-market:** Reduced pipeline deployment from days/weeks to 1-2 hours for senior users.
- **Adoption:** Achieved company-wide adoption — the platform became THE standard.

### Perguntas esperadas de follow-up:
- "How did you decide who to hire first?" → Senior architects first, build the foundation, then scale
- "What was the hardest hire?" → Finding people with both data AND platform engineering skills
- "How did you ensure quality as the team grew?" → ADRs/RFCs for technical decisions, structured onboarding, pair programming culture
- "What would you do differently?" → Invest earlier in developer experience and documentation

---

## H2: Migração da plataforma global (descomissionar plataforma de US/EU)

**Use para:** Cross-functional leadership, influence without authority, stakeholder management, conflict resolution, delivery

### STAR

**Situation:**
The company had multiple regional data platforms — my team had built the one for South America, and teams in the US and Europe had their own. Leadership decided to consolidate into a single global platform. The challenge: the US and European teams were attached to their own solutions and didn't want to migrate to ours.

**Task:**
I was tasked with leading the global platform consolidation. This meant not just technical migration, but convincing teams across different regions, cultures, and time zones to adopt our platform and decommission theirs.

**Action:**
- **Built the case with data:** I didn't go in saying "mine is better." Instead, I quantified the cost of fragmentation — duplicate infrastructure costs, inconsistent governance, duplicated engineering effort. I presented a clear TCO comparison.
- **Stakeholder mapping:** I identified the key decision-makers and influencers in each region. I had separate conversations with each, understanding their specific concerns and requirements.
- **Incorporated their needs:** Rather than forcing a one-size-fits-all approach, I adapted our platform to address legitimate gaps they identified. This gave them ownership in the solution.
- **Structured migration plan:** I created a phased migration plan with clear milestones, rollback procedures, and support commitments. No team would be left without support during transition.
- **Tough conversations about budget and goals:** There were hard discussions about budget reallocation, team restructuring, and changing reporting lines. I had to navigate political dynamics while keeping the technical migration on track.

**Result:**
- Successfully consolidated into a single global platform across 8 availability zones
- 600+ users worldwide, 70K+ daily executions, 98% SLO, 99% uptime
- Eliminated millions in duplicate infrastructure costs
- Established a single global framework for data, ML, and AI workloads

### Perguntas esperadas de follow-up:
- "How did you handle resistance?" → Listened first, incorporated feedback, gave ownership
- "What was the biggest risk?" → Migration failures disrupting business operations — mitigated with phased approach
- "How did you handle the cultural differences?" → Adapted communication style, respected time zones, built personal relationships

---

## H3: Primeiro desligamento

**Use para:** Performance management, difficult decisions, coaching, process improvement

### STAR

**Situation:**
I had a senior engineer on my team who was underperforming significantly. Within the first few weeks, I noticed warning signs during a pair programming session — they were coding directly in the GitHub UI, which was unusual for someone at a senior level who should at minimum have an IDE setup. I gathered additional feedback from Product Owners and peers, which confirmed both performance and behavioral issues: missing dailies, missing plannings, being unreachable during the day.

**Task:**
As their manager, I needed to either help them succeed or make a tough call. This was my first termination, so I was also navigating this process for the first time.

**Action:**
- **First conversation (empathetic):** I called them in for a 1:1. I asked if there were any personal or family issues affecting their work. They said no. I gave them a chance — I had them redo our full onboarding to understand the architecture deeply before taking on tasks.
- **Second conversation (direct):** After a week, the same patterns continued — missing standups, leaving the PO without updates. I was direct: I told them this couldn't continue and that the next conversation would involve a harder decision. I created a formal development plan, assigned them a medium-complexity task, and asked them to focus solely on that.
- **Third conversation (termination):** The same issues persisted. I made the decision to terminate. The conversation was short and direct — I outlined the specific issues, the steps we'd taken, and the decision. They weren't surprised, which told me the communication had been clear throughout.

**Result:**
- The termination was handled respectfully and cleanly
- **Process change:** I fundamentally changed my hiring and onboarding approach. I added culture-fit evaluation to my interview process. Even if someone was technically strong, I now explicitly assessed willingness to learn, proactiveness, and collaboration style. I also enhanced my onboarding to set clearer expectations from day one.
- The team's morale actually improved — they had noticed the issues too, and seeing them addressed built trust in my leadership.

### Perguntas esperadas de follow-up:
- "Would you do anything differently?" → I'd set more explicit, measurable expectations from week 1. And I'd start the formal process earlier rather than hoping things improve informally.
- "How did the team react?" → Positively — addressing underperformance builds trust
- "What if your manager told you to ignore the underperformer?" → (DOORDASH QUESTION!) I wouldn't ignore it. Underperformance affects the whole team — morale, workload distribution, and standards. My job is to address it, not avoid it.

---

## H4: Promoções — desenvolvendo 7+ pessoas

**Use para:** Coaching, mentoring, career development, growing engineers

### STAR

**Situation:**
As I built the team from scratch over 3 years, I had engineers at various levels — from junior to senior. Many of them had the potential to grow, but needed structured guidance and opportunities.

**Task:**
I wanted to create a culture where growth wasn't accidental — it was intentional and systematic. I needed to develop a framework that would help me identify readiness, create opportunities, and build the case for promotions.

**Action:**
- **Individual development plans:** In 1:1s, I worked with each engineer to define their career goals and the specific gaps between their current level and the next. We turned these into concrete, measurable objectives.
- **Stretch assignments:** I intentionally assigned projects slightly above each person's current level. For example, having a mid-level engineer lead an ADR/RFC process, or having a senior engineer present architecture decisions to stakeholders.
- **Visibility:** I made sure their work was visible to leadership. I brought them into meetings with directors and VPs, let them present their own work, and advocated for them in calibration sessions.
- **Continuous feedback:** Not just in review cycles — weekly in 1:1s. Small course corrections, not big annual surprises.

**Result:**
- Promoted 7+ engineers (seniority level + salary increases)
- Several engineers who joined as junior/mid grew to senior level
- High retention rate on the team — people stayed because they saw a growth path
- Built a reputation as a manager who develops talent, which helped with future recruiting

### Perguntas esperadas de follow-up:
- "Give me a specific example of someone you developed" → Pick your best story
- "How do you handle someone who wants a promotion but isn't ready?" → Honest, specific feedback with a concrete plan
- "How do you balance developing people vs. delivering results?" → They're not in conflict — developing people IS how you deliver results at scale

---

## H5: Diversidade no hiring (RESPOSTA MELHORADA)

**Use para:** Hiring practices, diversity & inclusion, partnership with recruiting

### RESPOSTA SENIOR (substitui a anterior):

"Diversity was a deliberate part of my hiring strategy, not just a checkbox. Here's what I actually did:

**Pipeline:** I worked with recruiting to ensure we had affirmative action positions specifically for women and Black candidates. But I went beyond just opening these positions — I reviewed where we were sourcing candidates and pushed to expand to communities and networks that were underrepresented in our pipeline.

**Process:** I structured our interviews to reduce bias. Five standardized technical questions with clear evaluation criteria, so every candidate was assessed on the same rubric regardless of background. I trained my interviewers to evaluate on demonstrated skills and potential, not pedigree.

**Beyond hiring:** Diversity doesn't end at the offer letter. I focused on creating an inclusive environment through structured onboarding, pair programming culture, and ensuring diverse voices were heard in technical discussions like ADRs and RFCs. I also monitored retention — there's no point in diverse hiring if people leave.

**Result:** My team had meaningful diversity, and more importantly, people from underrepresented groups were being promoted and growing, not just filling seats."

---

## H6: Conflitos com stakeholders e reestruturação

**Use para:** Conflict resolution, influence, cross-functional partnership

### STAR

**Situation:**
During the global platform consolidation, I faced constant tension with teams from other regions — particularly US and European teams who had their own platforms being decommissioned. There were hard conversations around budget allocation, goals, and the classic "my solution is better than yours" dynamic. Business teams also pushed back when migration timelines threatened their operations.

**Task:**
I needed to resolve these conflicts without authority over these teams, while keeping the consolidation on track.

**Action:**
- **Technical alignment through ADRs/RFCs:** I moved debates from opinions to structured proposals. Every major decision went through a documented RFC process where all teams could comment, challenge, and propose alternatives. This depersonalized the conflict.
- **1:1 relationship building:** I invested time in building personal relationships with key counterparts in each region, despite time zone challenges. Understanding their pressures and constraints helped me find compromises.
- **Data-driven decisions:** When it was "my approach vs. theirs," I pushed for proof-of-concepts and benchmarks rather than debates. Let the data decide.
- **Business team communication:** For business stakeholders, I created clear migration timelines with guaranteed support windows and rollback plans, reducing their anxiety about disruption.

**Result:**
- Successfully navigated the consolidation without any major stakeholder escalations
- Built lasting cross-regional relationships that improved collaboration beyond just this project
- The RFC process I established became a company-wide standard for technical decision-making

---

## Respostas rápidas para perguntas diretas

### "What's your management philosophy?"
"I believe in building high-trust environments through transparency, clear expectations, and continuous feedback. I hire for judgment and growth mindset, give people ownership and stretch opportunities, and remove blockers so they can do their best work. My job shifts based on what the team needs — sometimes I'm a technical architect, sometimes a coach, sometimes a shield from organizational noise."

### "How do you handle competing priorities?"
"I align everything to business impact. I work with product and business stakeholders to understand what moves the needle most, then I'm transparent with my team about what we're prioritizing and why. I protect the team from context-switching by batching work and pushing back on requests that aren't aligned with our goals."

### "What's your approach to technical decisions as a manager?"
"I stay deeply involved in architecture and system design, but I don't dictate. I created an ADR/RFC culture where the team proposes, debates, and decides together. I set the bar for quality and scalability, and I step in when decisions have long-term architectural implications. But for day-to-day technical choices, I trust my engineers."

### "Why DoorDash?"
Personalize com: marketplace de 3 lados, problemas de escala real, data/ML central ao negócio, cultura de ownership
