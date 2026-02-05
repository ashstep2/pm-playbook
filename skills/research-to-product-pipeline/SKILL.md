---
name: research-to-product-pipeline
description: "Help users translate research breakthroughs into shipped products by evaluating readiness, designing productization paths, and managing the research-to-product handoff."
---

# Research-to-Product Pipeline

Produces a research readiness scorecard and a productization plan that guides teams from breakthrough paper to shipped product, managing the tensions between research velocity and product reliability at every stage.

## Core Principles

1. **Spatial intelligence completes the AI picture**
   "Our dreams of truly intelligent machines will not be complete without spatial intelligence."
   — *Fei-Fei Li, CEO & Co-founder of World Labs* ([source](https://drfeifei.substack.com/p/from-words-to-worlds-spatial-intelligence))

   Research-to-product PMs must understand when a research direction represents a missing capability layer rather than an incremental improvement. Spatial intelligence is not a feature; it is a foundational capability that unlocks entire verticals (gaming, robotics, architecture). The productization strategy should reflect this: build infrastructure, not point solutions.

2. **The demo-to-product gap is measured in nines, not months**
   "There's a very large demo-to-product gap where the demo is very easy, but the product is very hard. It's especially the case in cases like self-driving where the cost of failure is too high."
   — *Andrej Karpathy, former Director of AI at Tesla* ([source](https://navaneethsen.medium.com/the-andrej-karpathy-interview-with-dwarkesh-patel-c10659db456c))

   Karpathy's "march of nines" framework applies directly to research productization: the first 90% of capability is the paper; the next 9% is the demo; the final 0.9% (and beyond) is the product. Each nine requires exponentially more engineering effort. Assess where your research sits on this curve before committing to a launch timeline.

3. **New categories require new patience**
   "This is a brand new category of model that's generating 3D worlds, and this is something that's going to get better over time."
   — *Justin Johnson, Co-founder of World Labs* ([source](https://techcrunch.com/2025/11/12/fei-fei-lis-world-labs-speeds-up-the-world-model-race-with-marble-its-first-commercial-product/))

   When research creates an entirely new product category rather than improving an existing one, the PM must set expectations that quality will improve iteratively. Ship the category-defining version, not the perfect version. Creative control and iteration speed matter more than initial fidelity.

4. **Tackle technology risk before you scale**
   "One of the most common, yet largely avoidable, problems is when a product manager judges technical feasibility risk without consulting the engineers."
   — *Marty Cagan, Partner at Silicon Valley Product Group* ([source](https://www.svpg.com/four-big-risks/))

   In research-driven companies, technology risk is the dominant risk. PMs must work with research engineers during discovery to identify which capabilities are production-ready, which need hardening, and which are still too fragile. Never treat a research prototype's performance as the product baseline.

5. **Turning models into products requires closing the integration gap**
   "While it's become easier to train ML models, it's still way too hard to turn them into products that work, with real data on real users."
   — *Peter Welinder, VP of Product at OpenAI* ([source](https://www.linkedin.com/posts/welinder_come-build-the-gpt3-and-codex-api-with-us-activity-6826654613530406912-NTF1))

   The gap between "model works in evaluation" and "product works for users" is where most research-to-product efforts die. The PM's job is to define the integration layer: API contracts, latency budgets, failure modes, and graceful degradation. This is not engineering overhead; it is the product.

6. **Solve intelligence, then apply it everywhere**
   "Solve intelligence, and then use that to solve everything else."
   — *Demis Hassabis, CEO of Google DeepMind* ([source](https://www.technologyreview.com/2016/03/31/161234/how-google-plans-to-solve-artificial-intelligence/))

   Research labs must decide when to stop researching and start applying. The productization trigger is not perfection; it is when the research is sufficient to unlock value in a specific domain. DeepMind's AlphaFold shipped when it was useful to biologists, not when it solved protein folding completely. Identify your "useful to whom" moment.

7. **Creative control must survive productization**
   "You don't want the machine to just take the wheel and pull all that creativity away from you."
   — *Justin Johnson, Co-founder of World Labs* ([source](https://techcrunch.com/2025/11/12/fei-fei-lis-world-labs-speeds-up-the-world-model-race-with-marble-its-first-commercial-product/))

   When research becomes a creative tool, the product must preserve user agency. The PM's job is to design the "control surface" between AI capability and human intent. This means offering quick generation paths alongside deep customization. Do not automate away the user; augment them.

8. **The age of scaling is ending; the age of ideas is beginning**
   "The bigger problem is ideas, not compute."
   — *Ilya Sutskever, Co-founder of Safe Superintelligence* ([source](https://www.calcalistech.com/ctechnews/article/h1fudk7z11x))

   Research readiness is not just about whether the model is big enough. It is about whether the core insight is sound. A product built on a scaling hack will be disrupted; a product built on a fundamental idea will compound. Evaluate whether the research represents a genuine conceptual advance, not just a resource advantage.

9. **Feedback loops between research and product are the real moat**
   "The team is united by a shared curiosity, passion, and deep backgrounds in technology — from AI research to systems engineering to product design — creating a tight feedback loop between their cutting-edge research and products."
   — *World Labs, company description* ([source](https://www.worldlabs.ai/about))

   The most successful research-to-product organizations are not pipelines; they are loops. Product usage data improves research direction. Research breakthroughs unlock new product capabilities. The PM's role is to design and protect this feedback loop, ensuring product constraints inform research priorities and research insights shape the product roadmap.

## Instructions

### Step 1: Map the Research Landscape

Produce a **Research Landscape Map** documenting the breakthrough being evaluated.

- Identify the core research paper(s) or technical capability under consideration
- Read `context/founders/` to understand the founding team's research vision and what they believe the breakthrough enables
- Read `context/company/` for funding stage, team composition, and organizational capacity
- Document: What is the fundamental insight? What does it make possible that was not possible before?
- Classify the breakthrough: incremental improvement, new capability layer, or new product category
- List the key researchers involved and their track record of shipping vs. publishing

**Output:** A 1-page Research Landscape Map with the breakthrough classified and its implications summarized.

### Step 2: Score Research Readiness

Produce a **Research Readiness Scorecard** by evaluating the research across seven dimensions on a 1-5 scale.

| Dimension | 1 (Not Ready) | 3 (Emerging) | 5 (Ready) |
|---|---|---|---|
| **Reproducibility** | Works only in authors' setup | Works with careful replication | Independently reproduced by others |
| **Robustness** | Fails on edge cases | Handles common variations | Gracefully degrades under stress |
| **Latency** | Minutes per inference | Seconds per inference | Real-time or near-real-time |
| **Cost Efficiency** | Prohibitively expensive | Viable for high-value use cases | Viable at consumer scale |
| **Input Flexibility** | Single narrow input type | Multiple constrained inputs | Diverse real-world inputs |
| **Output Quality** | Impressive but inconsistent | Consistently good | Consistently good with controllability |
| **Integration Surface** | No API, manual pipeline | Basic scripting interface | Clean API with error handling |

- Score each dimension based on the current state of the research
- For each dimension scoring below 3, document what would be required to reach 3
- Calculate a composite score (sum / 35 as a percentage)
- Readiness thresholds: below 40% = too early; 40-60% = needs targeted hardening; 60-80% = ready for beta; above 80% = ready for GA

**Output:** A filled Research Readiness Scorecard with composite score and gap analysis.

### Step 3: Identify the Productization Wedge

Produce a **Wedge Analysis** identifying the narrowest, highest-value use case to ship first.

- Read `context/products/` to understand the current product surface and what already exists
- Read `context/verticals/` to understand target markets and their specific needs
- For each potential use case, evaluate:
  - Does the research's current quality level meet this use case's bar? (Reference scorecard from Step 2)
  - What is the cost of failure for this use case? (Low = creative tools; High = safety-critical)
  - How many users can this unlock in the first 90 days?
  - Does this use case generate feedback data that improves the research?
- Rank use cases by: (value to users) x (research readiness) x (feedback loop strength) / (cost of failure)
- Select the top wedge and document why it is the right starting point

**Output:** A ranked wedge analysis with the selected first use case and rationale.

### Step 4: Design the Integration Architecture

Produce an **Integration Architecture Document** specifying how research becomes a callable service.

- Define the API contract: inputs, outputs, error states, latency budget, cost per call
- Specify the failure mode hierarchy: What happens when the model fails? What does graceful degradation look like?
- Define quality tiers if applicable (e.g., draft quality at 30 seconds vs. production quality at 5 minutes)
- Document the human-in-the-loop touchpoints: Where does the user steer, approve, or override?
- Specify the telemetry plan: What data flows back to improve the research?
- Address security model: API key management, input validation, rate limiting

**Output:** An Integration Architecture Document with API contract, failure modes, and telemetry plan.

### Step 5: Define the Hardening Roadmap

Produce a **Hardening Roadmap** that sequences the work to close gaps identified in the scorecard.

- For each scorecard dimension below target, define a concrete workstream
- Sequence workstreams by: (impact on wedge use case) x (effort feasibility) / (research disruption)
- For each workstream, specify:
  - Owner: Research team, product engineering, or joint
  - Success metric: How do we know this dimension moved from X to Y?
  - Timeline: Weeks, not months. If a workstream takes months, break it into milestones.
  - Research velocity impact: Does this slow down research? If so, by how much, and is the trade-off worth it?
- Flag any workstreams that require research breakthroughs (not just engineering) and mark them as risks

**Output:** A sequenced Hardening Roadmap with owners, metrics, timelines, and research velocity impact assessment.

### Step 6: Build the Launch Criteria and Feedback Plan

Produce a **Launch Gate Checklist** and **Feedback Loop Design** for the first productized release.

- Define launch gates across four categories:
  - **Technical:** Minimum scorecard thresholds, latency p95, error rate ceiling
  - **User experience:** Minimum controllability, onboarding time to first value, recovery from bad output
  - **Business:** Pricing model, credit/cost structure, support capacity
  - **Research:** Telemetry pipeline active, feedback data flowing, no research regressions
- Design the post-launch feedback loop:
  - What user actions become training signal?
  - What product metrics indicate the research needs to improve?
  - How frequently does product data reach the research team?
  - What is the process for research improvements to reach production?
- Define the criteria for moving from beta to GA

**Output:** A Launch Gate Checklist with pass/fail criteria and a Feedback Loop Design document.

### Step 7: Write the Stakeholder Alignment Brief

Produce a **Stakeholder Alignment Brief** that communicates the plan to research leads, engineering leads, and executives.

- Read `context/competitive/` to frame urgency and positioning
- Summarize: What we are shipping, why now, what we are NOT shipping yet, and what the research team should expect
- Address the research team's concerns explicitly:
  - "Will productization slow our research?" (Answer with the velocity impact from Step 5)
  - "Will our reputation suffer if quality is not perfect?" (Answer with the wedge selection rationale from Step 3)
  - "How will product feedback improve our research?" (Answer with the feedback loop from Step 6)
- Include a one-page timeline from current state to first external user
- Include a risk register with the top 5 risks and mitigations

**Output:** A 2-3 page Stakeholder Alignment Brief ready for distribution.

## Diagnostic Questions

1. **Can someone outside the research team reproduce the core result?** If reproducibility requires the original authors' specific setup, environment, or tacit knowledge, the research is not ready for product engineering to take over.

2. **What happens when the model receives unexpected input?** Research evaluations use curated inputs. Products receive adversarial, malformed, and bizarre inputs. If nobody has tested failure modes, you are not ready.

3. **Is the research team excited or threatened by productization?** If researchers see the product as a distraction from their real work, the handoff will fail. Alignment on how product data improves research is a prerequisite, not a nice-to-have.

4. **Does the use case tolerate imperfection?** Creative tools can ship with inconsistent output because users iterate. Safety-critical systems cannot. Match your first wedge to your quality level.

5. **Is there a natural feedback loop between usage and improvement?** The best research-to-product pipelines create a flywheel where more users generate more data that makes the research better. If your product does not create this loop, you are building a dead end.

6. **Can you articulate the "useful to whom" moment?** Researchers optimize for benchmarks. Products need a specific user who will pay or engage. If you cannot name the user persona and their immediate use case, the research is not ready for productization.

7. **Does the founding team have a shared definition of "good enough"?** Research teams and product teams often have fundamentally different quality bars. Align on the definition before you start building.

## Common Mistakes

1. **Waiting for research perfection before shipping**
   Research will never be "done." The question is not "is this perfect?" but "is this useful enough for a specific user?" Waiting for perfection means competitors ship the imperfect-but-useful version first. Use the Research Readiness Scorecard to set objective thresholds and ship when they are met.

2. **Treating the research prototype as the product architecture**
   Research code is optimized for experimentation speed. Product code is optimized for reliability, latency, and maintainability. Plan for a rewrite or at minimum a hardening phase. Never ship the Jupyter notebook.

3. **Ignoring the researcher's incentives**
   Researchers are motivated by publications, citations, and intellectual credit. If productization is framed as "turning their research into boring engineering," they will disengage or actively resist. Frame it as "putting their research in front of millions of users and generating data that enables the next paper."

4. **Skipping the wedge and launching broadly**
   Launching across all possible use cases simultaneously dilutes focus, stretches quality thin, and makes it impossible to tell which feedback matters. Pick one wedge, dominate it, learn from it, and expand.

5. **Building the API without the feedback loop**
   Many teams ship an API and declare victory. But an API without telemetry, usage analytics, and a data pipeline back to the research team is a one-way street. The feedback loop is not a phase 2 feature; it is a launch requirement.

6. **Conflating research milestones with product milestones**
   A new SOTA result on a benchmark is a research milestone. A user successfully completing their task with your product is a product milestone. These are different events. Track them separately. Celebrate both, but do not confuse them in your roadmap.

## Context Integration

This skill draws from multiple context directories to produce its artifacts:

| Context Directory | Used In | Purpose |
|---|---|---|
| `context/founders/` | Step 1 (Research Landscape Map), Step 7 (Stakeholder Brief) | Founder quotes reveal the research vision and what the team believes the breakthrough enables. Key themes from founders inform whether the research is positioned as incremental or category-defining. |
| `context/products/` | Step 3 (Wedge Analysis), Step 4 (Integration Architecture) | Current product surface shows what already exists and where the new research capability fits. Existing API patterns and architecture inform integration design. |
| `context/company/` | Step 1 (Research Landscape Map), Step 5 (Hardening Roadmap) | Funding stage, team size, and org structure determine how much hardening capacity exists and whether the team can support parallel research and product workstreams. |
| `context/competitive/` | Step 3 (Wedge Analysis), Step 7 (Stakeholder Brief) | Competitor capabilities determine urgency. If a competitor is 6 months behind on similar research, the wedge selection should favor speed over polish. |
| `context/verticals/` | Step 3 (Wedge Analysis) | Vertical-specific requirements (e.g., gaming vs. robotics vs. architecture) determine quality bars, latency requirements, and cost sensitivity for the wedge selection. |

When `context/` directories are not populated, the skill prompts the user for the equivalent information before proceeding with each step.
