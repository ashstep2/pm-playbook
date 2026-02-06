---
name: customer-discovery
description: "Help users plan and execute customer discovery — producing interview guides, recruitment strategies, synthesis frameworks, and discovery reports with validated/invalidated hypotheses."
---

# Customer Discovery

Produces a structured customer discovery plan and synthesis report: interview guide, recruitment strategy, hypothesis tracker, synthesis framework, and a final discovery report with validated and invalidated hypotheses. Reach for this skill before building anything new, before entering a new market, or when existing assumptions need stress-testing.

## Core Principles

1. **Get out of the building**
   "There are no facts inside the building, so get the heck outside."
   -- *Steve Blank, The Four Steps to the Epiphany* ([source](https://steveblank.com/2010/03/11/teaching-entrepreneurship-%E2%80%93-by-getting-out-of-the-building/))

2. **Talk about their life, not your idea**
   "The measure of usefulness of an early customer conversation is whether it gives us concrete facts about our customers' lives and world views."
   -- *Rob Fitzpatrick, The Mom Test* ([source](https://www.momtestbook.com/))

3. **Discover opportunities, not features**
   "The biggest mistake product teams make is they start with solutions. Instead, start by mapping the opportunity space."
   -- *Teresa Torres, Continuous Discovery Habits* ([source](https://www.producttalk.org/2021/08/opportunity-solution-trees/))

4. **Hypotheses before conversations**
   "Lean Customer Development means formulating falsifiable hypotheses before you talk to a single person, so you can design conversations that actually test those hypotheses."
   -- *Cindy Alvarez, Lean Customer Development* ([source](https://www.oreilly.com/library/view/lean-customer-development/9781449356576/))

5. **Understand the job, not the person**
   "People don't simply buy products or services; they pull them into their lives to make progress. We call this progress the 'job' they are trying to get done."
   -- *Bob Moesta, Demand-Side Sales 101* ([source](https://www.demandsidesales.com/))

6. **Seek disconfirming evidence**
   "The goal of customer development is not to collect opinions that confirm what you already believe. The goal is to find the fastest path to the truth."
   -- *Steve Blank, The Startup Owner's Manual* ([source](https://steveblank.com/books-for-startups/))

7. **Patterns emerge from volume**
   "You need to talk to enough customers that you start hearing the same problems repeated back to you. Five is a starting point, not a finish line."
   -- *Teresa Torres, Continuous Discovery Habits* ([source](https://www.producttalk.org/2022/01/continuous-interviewing/))

8. **Distinguish stated preferences from revealed behavior**
   "Opinions are worthless. You want facts and commitments. Facts are things that happened in the past. Commitments are things they are doing to solve this today."
   -- *Rob Fitzpatrick, The Mom Test* ([source](https://www.momtestbook.com/))

## Instructions

### Step 1: Define the Discovery Scope

- State the product, feature, or market you are investigating.
- Identify whether this is **exploratory** (understanding a problem space), **evaluative** (testing a specific solution concept), or **generative** (discovering unmet needs in a new vertical).
- Write a one-paragraph discovery mission statement: what you need to learn and why it matters now.

**Artifact:** Discovery scope document (mission statement + discovery type + decision this will inform).

### Step 2: Formulate Falsifiable Hypotheses

- List 5-10 hypotheses about your users, their problems, current alternatives, and willingness to adopt.
- Each hypothesis must be written as a falsifiable statement with a clear pass/fail threshold.
- Categorize each: **Problem** (does this pain exist?), **Segment** (who has it worst?), **Behavior** (what do they do today?), or **Value** (would they pay/switch?).
- Reference `context/verticals/` for market-specific assumptions and `context/products/` for existing product assumptions.

**Artifact:** Hypothesis tracker table with columns: ID, Category, Hypothesis, Pass Threshold, Status (untested/validated/invalidated).

### Step 3: Build the Interview Guide

- Create a semi-structured guide with 12-18 questions organized in three sections:
  - **Context & Background** (3-5 questions): Understand who they are, what they do, and how they work today. No leading questions.
  - **Problem Exploration** (5-8 questions): Probe specific pain points, frequency, severity, current workarounds, and cost of the status quo. Use "Tell me about the last time..." framing.
  - **Solution Direction** (3-5 questions): Explore reactions to concepts without pitching. Ask about constraints, trade-offs, and what "good enough" looks like.
- Include 2-3 follow-up probes per section for when responses are vague ("Can you give me a specific example?", "What happened next?", "How did you decide?").
- Add a closing question: "Who else should I talk to who faces this problem?"

**Artifact:** Interview guide document with numbered questions, section headers, and follow-up probes.

### Step 4: Design the Recruitment Strategy

- Define your target participant profile: role, company size, industry, and qualifying behaviors (not demographics alone).
- Specify the number of interviews needed per segment (minimum 5 per segment for pattern detection).
- List 3-5 recruitment channels ranked by signal quality: existing users, community forums, LinkedIn outreach, partner introductions, conference attendees.
- Write a recruitment screener (5-7 qualifying questions) to filter out poor-fit participants.
- Include a brief outreach message template (under 100 words) that explains the purpose without biasing responses.
- Reference `context/verticals/` for segment-specific recruitment channels.

**Artifact:** Recruitment plan with target profiles, channel strategy, screener questions, and outreach template.

### Step 5: Create the Synthesis Framework

- Design a tagging taxonomy for interview notes: **Pain Points**, **Current Workflow**, **Triggers** (what prompts them to look for a solution), **Barriers** (what stops them from switching), **Value Drivers** (what they would pay for).
- Build an affinity mapping template: group raw observations into clusters, then clusters into themes.
- Create a quote bank structure: verbatim quotes indexed by participant ID, theme, and hypothesis.
- Include a Jobs-to-Be-Done capture template: When [situation], I want to [motivation], so I can [expected outcome].

**Artifact:** Synthesis framework with tagging taxonomy, affinity map template, quote bank structure, and JTBD template.

### Step 6: Produce the Discovery Report

- For each hypothesis, state **Validated**, **Invalidated**, or **Inconclusive** with supporting evidence (direct quotes, observation counts, behavioral data).
- Summarize the top 3-5 validated pain points with severity and frequency scores (1-5 scale based on interview data).
- Map validated problems to opportunity areas using an Opportunity-Solution Tree structure.
- Identify the strongest user segment: which segment has the most acute problem, fewest alternatives, and highest willingness to act?
- List 3-5 recommended next steps: build, test further, pivot, or kill.
- Include a confidence assessment: how much weight should stakeholders put on these findings given sample size, participant quality, and potential biases?
- Reference `context/competitive/` to contextualize how current alternatives shape user expectations.

**Artifact:** Discovery report with hypothesis verdicts, evidence summary, opportunity map, segment recommendation, and next steps.

### Step 7: Design the Continuous Discovery Cadence

- Recommend an ongoing interview cadence (e.g., 2-3 interviews per week during active development).
- Define triggers for re-running discovery: new competitor launch, usage data anomalies, expansion into a new vertical.
- Specify how findings should be stored and shared: living document, team wiki, or integrated into the product backlog.
- Connect discovery insights to product decisions: which upcoming roadmap items depend on which validated hypotheses?

**Artifact:** Continuous discovery plan with cadence, triggers, storage format, and roadmap linkage.

## Diagnostic Questions

1. **What decision will this discovery inform?** If you cannot name a specific upcoming decision (build/kill/pivot/sequence), you are not ready for discovery -- you need to align with stakeholders first.

2. **How confident are you in your problem definition?** If you are above 80% confident before talking to anyone, you are likely suffering from confirmation bias. Discovery should feel uncomfortable.

3. **Who are you NOT talking to that you should be?** The most dangerous blind spot is interviewing only your most enthusiastic users. Seek out churned users, non-adopters, and users of competitors.

4. **Can you distinguish between a problem and a feature request?** Feature requests ("I want a dark mode") are not discovery insights. The underlying problem ("I work late at night and the screen hurts my eyes") is.

5. **Are you hearing new information or just confirming what you already know?** If every interview feels like validation, your questions are leading or your sample is biased.

6. **Do you have access to real users or only proxies?** Talking to sales, support, or executives is useful context but is not a substitute for direct user contact. Prioritize end users.

## Common Mistakes

1. **Pitching instead of listening**
   Founders and PMs instinctively pitch their solution during interviews. This poisons the data. If you are talking more than 30% of the time, you are pitching, not discovering. Prepare questions, then let silences do the work.

2. **Asking hypothetical questions**
   "Would you use a product that...?" always gets a yes. Instead, ask about past behavior: "Tell me about the last time you faced this problem. What did you do?" Past behavior predicts future behavior; stated intent does not.

3. **Stopping at 3 interviews**
   Three interviews feel like a pattern but are usually a coincidence. Plan for at least 5 per segment, and keep going until you hear the same problems repeated without new themes emerging (saturation).

4. **Synthesizing too late**
   If you conduct 15 interviews and then sit down to synthesize, you will forget critical nuance. Synthesize after every 2-3 interviews: update your hypothesis tracker, tag new themes, and adjust your guide.

5. **Conflating customer discovery with user research**
   Discovery is about validating whether a problem worth solving exists and for whom. It is not a usability study, an A/B test, or a satisfaction survey. Keep the scope tight: hypotheses in, verdicts out.

6. **Ignoring non-verbal and contextual signals**
   Energy shifts, hesitation, workarounds visible on their screen, and the tools already open on their desktop are all data. Note the context around statements, not just the statements themselves.

## Context Integration

| Context Directory | How It Feeds This Skill |
|---|---|
| `context/products/` | **Step 1-2**: Grounds hypotheses in the actual product capabilities, pricing, and positioning. Helps distinguish what users can already do from what they cannot. |
| `context/verticals/` | **Step 2, 4**: Provides market-specific assumptions for hypothesis formulation and identifies segment-specific recruitment channels and communities. |
| `context/competitive/` | **Step 2, 6**: Informs hypotheses about current alternatives and workarounds. Contextualizes discovery findings against competitive offerings. |
| `context/company/` | **Step 4, 7**: Shapes recruitment strategy based on existing user base and company stage. Informs realistic cadence recommendations given team size. |
| `context/founders/` | **Step 1-2**: Surfaces founder assumptions and domain expertise to formulate stronger initial hypotheses (and flag which ones need the most testing). |
| `context/signals/` | **Step 2, 6**: Supplements interview data with community sentiment, support tickets, and ecosystem signals. Check collection timestamps for freshness. |
