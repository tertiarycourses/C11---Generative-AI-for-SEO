# Generative AI for SEO — Learner Guide

**Course Code:** C11  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 28 July 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Getting Started with Generative AI for SEO  (First half · 3 labs)](#topic-01--getting-started-with-generative-ai-for-seo--first-half--3-labs)
  - [Introduction to SEO and Generative AI](#introduction-to-seo-and-generative-ai)
  - [Setting Up ChatGPT, Claude and Gemini for SEO](#setting-up-chatgpt-claude-and-gemini-for-seo)
  - [AI-Powered Keyword Research and Topic Clusters](#ai-powered-keyword-research-and-topic-clusters)
  - [Understanding Search Intent and Content Planning with AI](#understanding-search-intent-and-content-planning-with-ai)
  - [Effective Prompting for SEO Tasks](#effective-prompting-for-seo-tasks)
  - [Lab 1 — Build the AI-Ready SEO Brief and Prompt Guardrails](#lab-1--build-the-ai-ready-seo-brief-and-prompt-guardrails)
  - [Lab 2 — Build the Keyword Universe and Topic Clusters](#lab-2--build-the-keyword-universe-and-topic-clusters)
  - [Lab 3 — Map Search Intent and Create the Content Plan](#lab-3--map-search-intent-and-create-the-content-plan)
  - [Topic 01 Recap - Mapped to Learning Outcomes](#topic-01-recap---mapped-to-learning-outcomes)
- [Topic 02 — Creating and Optimising SEO Content with Generative AI  (Second half · 3 labs)](#topic-02--creating-and-optimising-seo-content-with-generative-ai--second-half--3-labs)
  - [Generating Titles, Meta Descriptions and On-Page Content](#generating-titles-meta-descriptions-and-on-page-content)
  - [Writing Briefs, Outlines and Long-Form Content with AI](#writing-briefs-outlines-and-long-form-content-with-ai)
  - [On-Page and Technical SEO Optimisation with AI](#on-page-and-technical-seo-optimisation-with-ai)
  - [Auditing and Improving Existing Pages](#auditing-and-improving-existing-pages)
  - [Fact-Checking, Quality Control and Google Guidance](#fact-checking-quality-control-and-google-guidance)
  - [Lab 4 — Create the SEO Brief, Outline, Metadata and First Draft](#lab-4--create-the-seo-brief-outline-metadata-and-first-draft)
  - [Lab 5 — Audit and Optimise the Existing Page](#lab-5--audit-and-optimise-the-existing-page)
  - [Lab 6 — Run the Quality Gate and Build the SEO Improvement Plan](#lab-6--run-the-quality-gate-and-build-the-seo-improvement-plan)
  - [Topic 02 Recap - Mapped to Learning Outcomes](#topic-02-recap---mapped-to-learning-outcomes)
- [Wrap-Up — The Complete C11 Workflow](#wrap-up--the-complete-c11-workflow)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies Generative AI for SEO (C11). It follows the same two-topic sequence, six connected labs and learning outcomes as the slide deck, Lesson Plan and lab files. The course uses a synthetic travel-gear business so every learner can practise without exposing client data or making changes to a live website.

Use the guide as a study text before, during and after class. Each concept explains what it is, why it matters, how it works, a worked example and a decision guide. The labs then apply those concepts to one evidence-led workflow. AI output is always a draft or suggestion until a human checks its sources, usefulness, rights, privacy and technical implications.


## Course Learning Outcomes

- LO1: Explain how SEO and generative AI work together, set safe working boundaries and use a structured prompt-and-review method.
- LO2: Build an evidence-led keyword universe, topic clusters and a search-intent content plan with AI assistance.
- LO3: Create an SEO content brief, outline, title, meta description and on-page draft that remain grounded in approved sources.
- LO4: Audit and improve an existing page for content, on-page and technical SEO, then verify quality against Google guidance.


## Before You Start — Preparation

**What you need**

- A Windows or Mac laptop with a modern browser, spreadsheet application and plain-text editor.
- Access to at least one approved assistant: ChatGPT, Claude or Gemini; a free account is sufficient.
- A downloaded copy of this repository with the labs/assets folder intact.
- No API key, paid SEO platform, website login or live publishing access is required.

**Verify your setup**

Open labs/assets/merliontrail-brand-source-pack.md and labs/assets/synthetic-keyword-evidence.csv. Create a local folder named work-c11 for your outputs. Confirm that your chosen AI assistant can accept pasted text and return a Markdown table.

```bash
Expected local structure:
C11---Generative-AI-for-SEO/
  labs/assets/
  work-c11/
```

**Conventions used in every lab**

- All MerlionTrail facts and metrics are synthetic training material, not current market claims.
- Text between <ANGLE_BRACKETS> is a placeholder that you replace; never paste a real secret.
- OBSERVED means supported by a supplied source; HYPOTHESIS means a testable interpretation; UNKNOWN means unresolved.
- Save the prompt, first output, human edits and final decision so another person can review the trail.


## Topic 01 — Getting Started with Generative AI for SEO  (First half · 3 labs)

SEO and generative AI · ChatGPT, Claude and Gemini · keyword research and topic clusters · search intent · content planning · effective prompting

**Key concepts**

- SEO fundamentals — Help search engines understand a page and help people decide whether it answers their need.
- AI assistants — Use ChatGPT, Claude or Gemini to transform supplied evidence, not to invent market facts.
- Keyword evidence — Separate observed query data from AI suggestions and label assumptions explicitly.
- Topic clusters — Group related queries around one audience problem while preventing overlapping pages.
- Search intent — Infer the job behind a query, then confirm it against current result-page evidence.
- Structured prompting — Use Goal, Context, Constraints, Sources, Output and Review to make quality observable.


### Introduction to SEO and Generative AI

Search engine optimisation helps search systems understand web content and helps people decide whether a result is useful. Search discovery is not a single ranking trick: a page must be discoverable, crawlable, indexable, relevant to a need and useful after the click. Generative AI can accelerate research organisation, comparison, drafting and critique, but it does not create search demand or guarantee visibility.

A fluent AI draft can hide weak evidence. Keeping the search process and the AI workflow separate prevents common errors such as treating invented search volume as data, assuming a keyword alone determines ranking or publishing generic pages at scale. The practitioner remains responsible for the purpose, evidence, editorial quality and technical state of the page.

**How it works**

- Define the audience, business purpose and page job before opening an AI assistant.
- Collect approved business facts, query evidence and current result-page observations.
- Use AI to organise or transform the evidence, then verify the page and monitor real outcomes.

**Worked example**

- MerlionTrail sells repairable travel organisers. The team wants a useful guide for carry-on packing.
- Keyword evidence and current result pages suggest several related questions, but no ranking promise.
- AI organises the evidence into a plan; the human owner supplies product facts and approves the result.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The task has a defined user need and sources that can be supplied to the assistant. | The goal is to mass-produce pages primarily to manipulate search visibility. |
| A human can review both the output and the live page before publication. | The only evidence is an AI answer with no traceable source or current query data. |

**Practitioner quality lens**

- Purpose: State the audience need and the useful outcome before choosing keywords.
- Evidence: Label business facts, observed data, hypotheses and unknowns separately.
- Ownership: Assign a human editor to approve claims, page quality and technical changes.

**Authoritative references**

- https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- https://developers.google.com/search/docs/essentials
- https://developers.google.com/search/docs/fundamentals/using-gen-ai-content

---


### Setting Up ChatGPT, Claude and Gemini for SEO

ChatGPT, Claude and Gemini are general-purpose AI assistants with changing models and interfaces. For this course, the tool is a workspace for grounded transformation: learners provide a source pack, ask for a defined output and review it against a checklist. The course does not depend on a paid tier, API key, browser extension or automatic publishing connection.

Good setup is mostly governance. Confidential strategy, personal information, credentials and unreleased client material should not be pasted into an unapproved service. A reusable project brief, source boundary and output convention make results more consistent across tools without assuming that any vendor has unique access to Google ranking data.

**How it works**

- Choose one approved assistant and create a fresh conversation for the C11 synthetic scenario.
- Paste only the supplied source pack and state that missing information must be marked Unknown.
- Save the prompt, output and human edits in local files so the reasoning trail is reviewable.

**Worked example**

- A learner opens one assistant and adds the MerlionTrail source pack as delimited context.
- The assistant must cite the supplied section behind each proposed claim and label any assumption.
- The learner compares one small task in a second tool only if time allows; no account is mandatory.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The organisation permits the selected tool and the source material is appropriate to share. | A prompt would contain passwords, unpublished client data or sensitive personal information. |
| The output can be stored and reviewed before it affects a live page. | A browser add-on or automation would publish or change a website without approval. |

**Practitioner quality lens**

- Minimum data: Share only the context needed for the specific SEO task.
- Clear boundary: Tell the assistant which sources it may use and how to show unknowns.
- Review trail: Keep the input, first output, edits and final decision together.

**Authoritative references**

- https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- https://ai.google.dev/gemini-api/docs/prompting-intro

---


### AI-Powered Keyword Research and Topic Clusters

Keyword research discovers the language people use around a need. A useful keyword record includes the query, source, date, location, evidence notes and an intended page job. A topic cluster groups closely related queries under a coherent primary page and supporting pages; it is an information-architecture decision, not a licence to create one near-duplicate page per phrase.

AI is good at expanding seeds, normalising wording and proposing groups, but it can fabricate volume, competition and trends. Evidence from Keyword Planner, Search Console, customer language or a current result-page review must remain distinguishable from an AI suggestion. Human review removes irrelevant phrases and resolves clusters that would compete with each other.

**How it works**

- Start with approved products, customer questions and a small set of evidence-backed seed queries.
- Ask AI for labelled expansions and preliminary semantic groups without inventing numeric metrics.
- Validate relevance, combine overlapping clusters and assign one clear page job to each retained group.

**Worked example**

- Seeds include 'packing cubes singapore', 'carry on packing list' and 'repair travel organiser'.
- AI proposes variants, but synthetic training metrics remain in the evidence CSV—not in the model output.
- The editor keeps three clusters: choose organisers, pack a carry-on and repair/reuse travel gear.

**Decision guide**

| Use when | Avoid when |
|---|---|
| There is a real offer or audience problem and at least one traceable source of query evidence. | Numeric demand or competition comes only from an AI response. |
| Clusters can be mapped to distinct page purposes rather than wording variations alone. | The plan creates many thin pages whose purpose and content substantially overlap. |

**Practitioner quality lens**

- Source every row: Record where the query came from and when the evidence was observed.
- Separate facts: Keep measured values, AI suggestions and human decisions in different columns.
- Prevent overlap: Give each retained cluster one primary need and one primary destination page.

**Authoritative references**

- https://support.google.com/google-ads/answer/7337243
- https://support.google.com/google-ads/answer/9247190
- https://developers.google.com/search/docs/fundamentals/seo-starter-guide

---


### Understanding Search Intent and Content Planning with AI

Search intent is the job a person is trying to complete. A practical planning heuristic labels a query as learn, compare, act or navigate, then records the required evidence and suitable format. Intent is inferred—not read directly from a keyword—and mixed intents are common. Current result-page features and leading page types provide observations that a human must interpret.

A page can mention a relevant phrase yet fail the user if its format and depth do not match the job. A content plan joins cluster, audience, intent, page type, unique value, evidence, internal links and success signal. AI can make this matrix faster to assemble, but it cannot safely decide business priority or claim that a result-page pattern will remain unchanged.

**How it works**

- Review each cluster and state the user job in one sentence using an action verb.
- Record current result-page observations and distinguish dominant, secondary and uncertain intent.
- Choose a page type, unique contribution, evidence plan, internal links and measurable next action.

**Worked example**

- 'Carry on packing list' is mainly a learn job; a checklist guide fits better than a category page.
- 'Packing cubes singapore' mixes compare and act; a category page needs selection guidance and real facts.
- Both pages can link naturally without repeating the same primary purpose.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The team can review current search results and articulate what a satisfied visitor would accomplish. | Intent is assigned from an AI label without checking the query context or result page. |
| The plan includes unique experience or approved evidence beyond a generic AI summary. | A sales page is forced onto a query whose dominant job is to learn or solve a problem. |

**Practitioner quality lens**

- User job: Write the desired visitor outcome before selecting the page format.
- SERP evidence: Date observations and treat them as a snapshot, not a permanent rule.
- Unique value: Name the experience, example or data the page contributes.

**Authoritative references**

- https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide

---


### Effective Prompting for SEO Tasks

A prompt is a working brief. C11 uses G-C-C-S-O-R: Goal, Context, Constraints, Sources, Output and Review. The structure tells the assistant what successful work looks like, confines it to approved evidence and requests a self-check that a human can inspect. Prompting is iterative: the user reviews a first output, identifies a specific defect and changes one instruction or source at a time.

Vague prompts produce generic copy and hide assumptions. A structured prompt reduces ambiguity, makes outputs comparable and allows a claim-to-source check. It does not remove hallucination risk, replace keyword evidence or transfer editorial accountability to the model.

**How it works**

- State one goal and the exact audience, page job and business context.
- Add constraints, delimit approved sources and specify the output schema or example.
- Require a review table for unsupported claims, missing evidence and guideline risks before accepting.

**Worked example**

- Goal: create a cluster table from the supplied CSV; Context: MerlionTrail Singapore travel gear.
- Constraints: do not invent volume; Sources: only delimited rows; Output: fixed six-column table.
- Review: list excluded terms, overlapping clusters and every statement not supported by a source row.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The task can be evaluated against observable criteria such as fields, sources and page purpose. | The prompt asks the model to guarantee ranking, predict proprietary metrics or conceal AI use. |
| The user is prepared to inspect and refine the output rather than accept the first response. | The source boundary is empty while the task requires factual claims. |

**Practitioner quality lens**

- Specific: Define audience, task, scope, format and the decision the output supports.
- Grounded: Delimit sources and instruct the model to show Unknown instead of inventing.
- Testable: Request a self-check, then perform an independent human review.

**Authoritative references**

- https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices
- https://help.openai.com/en/articles/6654000-best-practices-for-prompting-chatgpt
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- https://ai.google.dev/gemini-api/docs/prompting-intro

---


### Lab 1 — Build the AI-Ready SEO Brief and Prompt Guardrails

Learning outcome: LO1: set safe AI working boundaries and apply the G-C-C-S-O-R prompt method.

Goal: Create a grounded project brief and reusable prompt that prevent unsupported SEO claims.

You will set up one AI assistant for the synthetic MerlionTrail scenario, distinguish approved facts from unknowns and create a reusable SEO prompt. The prompt will force the assistant to use supplied sources, label missing information and return a claim-to-source review.

**What you'll build**

work-c11/01-ai-ready-seo-brief.md containing the audience, offer, page goal, data boundary, G-C-C-S-O-R prompt, first output and human review decision   (Tools: Text editor · ChatGPT, Claude or Gemini · merliontrail-brand-source-pack.md.)

**Prerequisites**

- Download the C11 repository and keep labs/assets in the same folder.
- Create an empty work-c11 folder beside labs.
- Confirm internet access and sign in to one approved AI assistant before class; then open a fresh conversation.

**Step-by-step**

1. Open labs/assets/merliontrail-brand-source-pack.md. Create work-c11/01-ai-ready-seo-brief.md with headings Audience, Offer, Page Goal, Approved Facts, Unknowns, Data Boundary, Prompt, First Output and Human Review. Copy only the six facts explicitly marked APPROVED into Approved Facts. Copy every item marked UNKNOWN into Unknowns.

   ```bash
   File: work-c11/01-ai-ready-seo-brief.md
Required headings: Audience | Offer | Page Goal | Approved Facts | Unknowns | Data Boundary | Prompt | First Output | Human Review
   ```

2. Complete the brief for an audience of Singapore-based leisure travellers and a page goal of helping them choose carry-on organisers. In Data Boundary, write the exact rule below. Do not add live customer, account, search-volume or competitor data.

   ```bash
   Use only the delimited MerlionTrail source text. Treat APPROVED statements as facts. Mark anything else UNKNOWN. Do not invent search volume, rankings, reviews, certifications, product performance or customer results.
   ```

3. Build the reusable prompt using G-C-C-S-O-R. Paste the approved facts between SOURCE START and SOURCE END. Ask for a five-row table with columns Candidate idea, Audience need, Supporting source section, Unknown or assumption, and Human check. Ask for ideas only—not final copy.

   ```bash
   GOAL: Propose five useful page ideas for a Singapore-based traveller choosing carry-on organisers.
CONTEXT: Synthetic brand MerlionTrail; audience and page goal are in my brief.
CONSTRAINTS: No ranking promise, invented metric, testimonial, comparison or unsupported product claim.
SOURCES: Use only text between SOURCE START and SOURCE END. Write UNKNOWN when evidence is missing.
OUTPUT: Markdown table with exactly five rows and these columns: Candidate idea | Audience need | Supporting source section | Unknown or assumption | Human check.
REVIEW: After the table, list every proposed statement that is not directly supported by the source.
SOURCE START
<PASTE APPROVED SOURCE TEXT>
SOURCE END
   ```

4. Run the prompt in your chosen assistant. Paste the response under First Output. Under Human Review, record which one page idea you would Keep, which one you would Repair and which one you would Hold. For each decision, cite the source section or the missing evidence. Save the file.

   ```bash
   Decision format:
KEEP — <idea> — source: <section>
REPAIR — <idea> — change: <specific repair>
HOLD — <idea> — missing evidence: <unknown>
   ```


**Test it**

The file must contain the stated audience and page goal, exactly six approved facts, all listed unknowns, the full G-C-C-S-O-R prompt, a five-row AI output, and one evidence-based Keep, Repair and Hold decision. Search the file for '%' and 'guarantee'; neither may appear unless quoted in a rejection note.

**Checkpoint and rejoin point**

Keep work-c11/01-ai-ready-seo-brief.md. Lab 2 reuses its audience, page goal, approved facts and source boundary. To rejoin, use the completed sample in labs/assets/rejoin-checkpoints.md.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The assistant adds search volume or ranking claims. | Delete those rows and repeat the prompt with: 'Numeric market metrics are unavailable; write UNKNOWN.' |
| The assistant cites a source that is not in the pack. | Mark the row Hold and require the exact source-section heading from the delimited text. |
| The output columns differ from the requested schema. | Paste the required header again and ask the assistant to reformat without changing content. |

**Challenge**

Run the same prompt in a second assistant. Compare only source discipline, usefulness and schema compliance; do not choose a winner based on fluency alone.

**Reflection**

Which instruction did the most work to keep the AI output evidence-led, and how could you tell?

> **Note:** The complete lab and its support-file references are in labs/lab-01-*.md. Use only the supplied synthetic MerlionTrail files or information you are authorised to process. Do not paste credentials, confidential client material or sensitive personal data into an AI assistant.

---


### Lab 2 — Build the Keyword Universe and Topic Clusters

Learning outcome: LO2: build evidence-led keyword candidates and non-overlapping topic clusters.

Goal: Turn supplied query evidence into a reviewed keyword universe and three coherent topic clusters.

You will work from a synthetic keyword evidence export, preserving source and metric labels while an AI assistant proposes additional wording and preliminary groups. You will reject invented measurements, remove irrelevant terms and make the final clustering decisions yourself.

**What you'll build**

work-c11/02-keyword-cluster-workbook.csv and work-c11/02-cluster-decisions.md with source-labelled keywords, AI suggestions, three final clusters, exclusions and overlap decisions   (Tools: Spreadsheet · text editor · AI assistant · synthetic-keyword-evidence.csv.)

**Prerequisites**

- Completed Lab 1 brief or the Lab 1 rejoin checkpoint.
- Open labs/assets/synthetic-keyword-evidence.csv in a spreadsheet.
- Remember that every metric in this file is synthetic training data.

**Step-by-step**

1. Save a copy of labs/assets/synthetic-keyword-evidence.csv as work-c11/02-keyword-cluster-workbook.csv. Add six columns: Candidate_Type, Proposed_Cluster, User_Job, Evidence_Status, Human_Decision and Decision_Reason. For all supplied rows, set Candidate_Type to OBSERVED and Evidence_Status to SYNTHETIC_TRAINING_EVIDENCE.

   ```bash
   New columns:
Candidate_Type | Proposed_Cluster | User_Job | Evidence_Status | Human_Decision | Decision_Reason
   ```

2. Paste only the Query and Evidence_Note columns into the prompt below. Ask for no more than eight additional query phrasings. Append those rows to the CSV with Location, Observation_Date and both numeric fields blank; Source=AI_ASSISTANT_OUTPUT; Evidence_Note set to the generated rationale; Candidate_Type=AI_SUGGESTION; and Evidence_Status=UNVALIDATED. Never let the assistant fill volume or competition.

   ```bash
   GOAL: Suggest up to eight additional query phrasings related to the supplied evidence.
CONSTRAINTS: Do not invent volume, trend, competition or ranking difficulty. Do not repeat supplied queries. Keep suggestions relevant to MerlionTrail's approved offer.
OUTPUT: Query | Evidence_Note | Proposed user job. Label every row AI_SUGGESTION.
SOURCE START
<PASTE QUERY AND EVIDENCE_NOTE COLUMNS>
SOURCE END
   ```

3. Run the copy-ready clustering prompt below using the Query, Candidate_Type and Evidence_Status columns. Review every row and choose exactly three final cluster names: Choose Carry-On Organisers, Pack a Carry-On, and Repair or Reuse Travel Gear. Set User_Job to Learn, Compare, Act or Navigate. Mark every row KEEP, EXCLUDE or HOLD with a reason. For EXCLUDE rows set Proposed_Cluster=EXCLUDED; for unresolved HOLD rows set Proposed_Cluster=UNASSIGNED.

   ```bash
   GOAL: Propose a preliminary cluster and user job for every supplied row.
ALLOWED CLUSTERS: Choose Carry-On Organisers | Pack a Carry-On | Repair or Reuse Travel Gear.
RULES: Use semantic user need, not wording alone. Preserve Candidate_Type and Evidence_Status. Do not invent or use numeric metrics. AI_SUGGESTION rows remain UNVALIDATED.
OUTPUT: Query | Proposed_Cluster | User_Job | Recommended_Decision | Decision_Reason.
SOURCE START
<PASTE QUERY, CANDIDATE_TYPE AND EVIDENCE_STATUS>
SOURCE END
   ```

4. Create work-c11/02-cluster-decisions.md. For each final cluster record Primary user job, Example observed queries, Possible page type, Unique contribution, Overlap risk and Human decision. Add an Exclusions section naming at least three removed queries or suggestions and the reason. Save both files.

   ```bash
   Per cluster:
Primary user job: <verb phrase>
Observed queries: <at least two>
Possible page type: <guide/category/support page>
Unique contribution: <specific MerlionTrail value>
Overlap risk: <other cluster + boundary>
Human decision: KEEP | REPAIR | HOLD
   ```


**Test it**

The CSV must preserve every supplied source and synthetic metric, contain no numeric value on an AI_SUGGESTION row, use exactly three final cluster names and give every row a human decision and reason. The decisions file must contain at least two observed queries per cluster and at least three exclusions.

**Checkpoint and rejoin point**

Keep both Lab 2 files. Lab 3 uses the three final clusters. To rejoin, use the three named clusters and the supplied observed rows; leave unvalidated AI suggestions on Hold.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| CSV values shift into the wrong columns. | Undo the paste, import the file as comma-delimited UTF-8 and append AI rows one at a time. |
| The assistant assigns volume to its suggestions. | Clear the cells, set Evidence_Status=UNVALIDATED and record the defect in Decision_Reason. |
| Two clusters appear to target the same page. | Rewrite each user job. Merge the groups if the visitor would expect one page to satisfy both. |

**Challenge**

Create a simple pivot table counting rows by Proposed_Cluster and Candidate_Type. Explain why a large cluster or many AI suggestions do not prove demand.

**Reflection**

Which cluster boundary required the most human judgment, and what evidence resolved it?

> **Note:** The complete lab and its support-file references are in labs/lab-02-*.md. Use only the supplied synthetic MerlionTrail files or information you are authorised to process. Do not paste credentials, confidential client material or sensitive personal data into an AI assistant.

---


### Lab 3 — Map Search Intent and Create the Content Plan

Learning outcome: LO2: translate keyword clusters into an intent-led, evidence-ready content plan.

Goal: Create a three-page content plan that matches user jobs and prevents page overlap.

You will convert the three reviewed clusters into a content plan. The plan distinguishes dominant and secondary intent, records dated result-page observations from a supplied snapshot and assigns each page a unique job, evidence plan, internal links and success signal.

**What you'll build**

work-c11/03-intent-content-plan.csv with one approved row per cluster plus a short cannibalisation boundary and human decision for each planned page   (Tools: Spreadsheet · AI assistant · cluster decisions · synthetic-serp-observations.csv.)

**Prerequisites**

- Three final clusters from Lab 2.
- Open labs/assets/synthetic-serp-observations.csv.
- Use the observation date shown in the file; do not present it as a live search result.

**Step-by-step**

1. Create work-c11/03-intent-content-plan.csv with the exact header below. Add one row for each of the three final clusters. Use these primary queries: packing cubes singapore; carry on packing list; repair packing cube zipper. For each row, combine all three matching Synthetic_Result_Page_Clues values in source-file order, separated by ' | ', and copy the common observation date. Do not add a page type yet.

   ```bash
   Cluster,Planned_URL,Human_Owner,Primary_Query,Primary_User_Job,Secondary_Intent,SERP_Observation_Date,SERP_Clues,Intent_Review,Human_Resolution,Planned_Page_Type,Page_Job,Unique_Contribution,Required_Evidence,Inbound_Link_Source,Inbound_Anchor_Text,Outbound_Link_Target,Outbound_Anchor_Text,Success_Signal,Overlap_Boundary,Human_Decision
   ```

2. For each cluster, write Primary_User_Job as a verb-led sentence. Use Learn, Compare, Act or Navigate only as Secondary_Intent labels. Ask the assistant to critique mismatches between the user job and the supplied result-page clues; it must not predict what Google will rank. Save the assistant's critique in Intent_Review and your own Keep, Repair or Reject response in Human_Resolution.

   ```bash
   Review these three cluster rows. For each, identify a mismatch between the stated user job and the supplied SERP clues, or write 'No material mismatch observed'. Use only supplied observations. Do not predict rankings or claim that the snapshot is permanent.
OUTPUT: Cluster | Intent_Review | Suggested_Repair
   ```

3. Choose one page type per row: guide for Pack a Carry-On, category/selection page for Choose Carry-On Organisers, and support guide for Repair or Reuse Travel Gear. Complete Page_Job, Unique_Contribution and Required_Evidence. Set Planned_URL to /guides/carry-on-packing-list, /collections/carry-on-organisers or /support/repair-reuse-travel-gear respectively, and set Human_Owner to Product Editor. Every unique contribution must come from the brand source pack or be marked HOLD.

   ```bash
   Required page choices:
Pack a Carry-On → /guides/carry-on-packing-list → guide
Choose Carry-On Organisers → /collections/carry-on-organisers → category/selection page
Repair or Reuse Travel Gear → /support/repair-reuse-travel-gear → support guide
   ```

4. For each row, fill Inbound_Link_Source and Inbound_Anchor_Text with the page that should link into it, then fill Outbound_Link_Target and Outbound_Anchor_Text with the page it should link to. The packing guide must link to the selection page using 'compare carry-on organisers'; the selection page must link to the guide using 'carry-on packing checklist'; both may link to the support guide using 'repair and reuse support'. Add a measurable Success_Signal such as qualified clicks or checklist completion—not a ranking guarantee. Write an Overlap_Boundary and Human_Decision for every row.

   ```bash
   Boundary pattern:
This page answers <user job>. It links to <other page> for <different job> and does not duplicate <excluded coverage>.
   ```


**Test it**

The CSV must contain exactly three planned pages, the three specified primary queries, all three aggregated SERP clues per cluster, the supplied observation date, Intent_Review and Human_Resolution, a verb-led page job, planned URL, Product Editor owner, traceable unique contribution, descriptive anchor text in both directions, success signal, overlap boundary and human decision. No cell may promise a position, traffic amount or guaranteed result.

**Checkpoint and rejoin point**

Keep 03-intent-content-plan.csv. Lab 4 uses the Pack a Carry-On guide row. To rejoin, select that row and use the supplied source pack plus content-brief template.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The page job merely repeats the keyword. | Rewrite it as what the visitor will be able to decide, learn or do after using the page. |
| Unique contribution is generic. | Tie it to an approved repairability, material or local-use fact from the source pack. |
| Two pages have the same success signal and coverage. | Clarify their different jobs and write distinct next actions before keeping both pages. |

**Challenge**

Create a separate work-c11/03-hold-page-challenge.md for one AI-suggested page. State which evidence is missing and what must be observed before planning it; do not add a fourth row to the three-page plan.

**Reflection**

How did the page job change when you considered result-page clues and overlap together?

> **Note:** The complete lab and its support-file references are in labs/lab-03-*.md. Use only the supplied synthetic MerlionTrail files or information you are authorised to process. Do not paste credentials, confidential client material or sensitive personal data into an AI assistant.

---


### Topic 01 Recap - Mapped to Learning Outcomes

Use this checkpoint to explain what you can now do and identify any lab evidence you still need to repair.

| Learning outcome | Evidence from this topic |
|---|---|
| LO1 - Set Up and Prompt | Explain the SEO and generative-AI relationship, keep evidence separate from suggestions, and use G-C-C-S-O-R with a human review gate. |
| LO2 - Research and Plan | Build labelled keyword evidence, resolve three topic clusters, and map each cluster to a distinct intent-led page with dated clues and descriptive internal links. |

---


## Topic 02 — Creating and Optimising SEO Content with Generative AI  (Second half · 3 labs)

Titles and meta descriptions · briefs, outlines and long-form content · on-page and technical SEO · page audits · fact-checking · Google guidance

**Key concepts**

- Search appearance — Write descriptive title and meta preferences while recognising that Google may generate alternatives.
- Content brief — Join audience, intent, evidence, unique value, structure, links and acceptance criteria.
- People-first drafting — Use AI for structure and options; add original experience, accurate facts and editorial judgment.
- On-page signals — Align visible title, headings, body, images and internal links around one clear page job.
- Technical triage — Check indexability, canonical choice, crawlable links, mobile usability and page experience.
- Quality control — Verify every material claim, disclose automation where useful and avoid scaled low-value production.


### Generating Titles, Meta Descriptions and On-Page Content

A page title is a preference used among several signals when Google creates a title link. A meta description is a page-specific summary that Google may use when it better describes the page than on-page text. Neither is a fixed-length ranking formula. On-page content should clearly answer the visitor's job with a distinct main heading, useful sections and natural language.

AI can create alternatives quickly, but generic formulas often cause boilerplate titles, repeated descriptions and keyword stuffing. The editor should choose wording that accurately represents the page, differentiates it from other site pages and sets the right expectation before the click.

**How it works**

- Write the page job and primary topic, then draft several descriptive and concise title options.
- Create a unique meta summary using only facts actually present on that page.
- Check title, visible H1, opening, sections and call to action for one coherent promise.

**Worked example**

- Weak title: 'Packing Cubes, Packing Cube, Best Packing Cubes | MerlionTrail'.
- Improved preference: 'How to Choose Packing Cubes for Carry-On Travel | MerlionTrail'.
- The description summarises the selection guide and repairable construction without a ranking claim.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The page has a distinct purpose and approved facts that can support a useful summary. | Titles repeat phrases, add unsupported superlatives or differ materially from the page. |
| Alternative wording will be reviewed against the actual visible content. | One generic description is copied across every page. |

**Practitioner quality lens**

- Accurate: The title, H1, snippet preference and page content describe the same primary job.
- Distinct: Wording differentiates this URL from other site pages.
- Natural: Use human-readable language and avoid repeated keyword variants.

**Authoritative references**

- https://developers.google.com/search/docs/appearance/title-link
- https://developers.google.com/search/docs/appearance/snippet
- https://developers.google.com/search/docs/fundamentals/seo-starter-guide

---


### Writing Briefs, Outlines and Long-Form Content with AI

A content brief translates research into an editorial contract: audience, user job, primary topic, unique value, approved sources, coverage, exclusions, internal links, conversion path and review criteria. An outline sequences the answer. A draft turns that plan into readable content while retaining source boundaries and the organisation's genuine experience.

Starting with 'write an SEO article' encourages generic prose and invented facts. Brief-first generation lets the human settle strategy before wording. It also creates checkpoints: an outline can be rejected cheaply, claims can be traced and the draft can be evaluated for completeness without using word count as a proxy for usefulness.

**How it works**

- Complete the brief from the approved cluster, intent plan, source pack and unique contribution.
- Generate an outline with a one-sentence purpose for every section and remove duplicated coverage.
- Draft section by section, preserving citations and adding human examples, edits and a final read-through.

**Worked example**

- The carry-on guide promises a printable seven-step checklist and a repair/reuse decision table.
- The outline moves from bag constraints to categories, packing order, organiser choice and a final check.
- The draft uses only supplied product facts; general travel rules stay out unless independently sourced.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The team can state what is uniquely useful and which sources support the page. | The only brief is a target word count and a keyword-density request. |
| A human editor will review outline, claims, voice and final flow. | The model is asked to imitate a competitor or rewrite copyrighted text closely. |

**Practitioner quality lens**

- Brief before prose: Approve the user job, evidence and unique value before drafting.
- One section, one job: Give each heading a clear question or decision to resolve.
- Human contribution: Add first-hand detail, examples or judgment that the model cannot supply.

**Authoritative references**

- https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide

---


### On-Page and Technical SEO Optimisation with AI

On-page SEO covers the visible and embedded signals that explain one page: title, main heading, sections, media text and internal links. Technical SEO ensures search systems can access and process the intended version: crawlable links, an indexable response, a sensible canonical, mobile usability and acceptable page experience. AI can explain code and propose a checklist, but the site owner must inspect the real page and approve changes.

A strong article can remain hard to discover if it is blocked, orphaned or duplicated; technical perfection cannot rescue unhelpful content. A layered check—purpose, on-page, crawl/index and experience—keeps the audit proportional and prevents automated tools from producing an unprioritised list of warnings.

**How it works**

- Confirm the preferred URL loads, returns indexable content and has a consistent title and main heading.
- Review descriptive crawlable internal links, image text, canonical choice and accidental robots directives.
- Record page-experience observations, assign an owner and verify changes with the appropriate live tool.

**Worked example**

- The sample page has a vague title, two H1 elements, a noindex directive and a JavaScript-only link.
- Content edits alone will not solve the noindex issue; the release owner must remove it deliberately.
- The corrected internal link uses a real anchor element and descriptive text to a related packing guide.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The practitioner has authority to inspect the page and can involve a developer for release changes. | AI-generated code is pasted into production without review, backup and testing. |
| Each finding is tied to impact, evidence, owner and a verification method. | Tool scores are treated as ranking guarantees or every warning receives equal priority. |

**Practitioner quality lens**

- Layered audit: Check page purpose, on-page signals, crawl/index state and experience separately.
- Evidence: Record the element, URL or tool observation behind each finding.
- Release control: Assign technical changes to an authorised owner and verify after deployment.

**Authoritative references**

- https://developers.google.com/search/docs/essentials
- https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- https://developers.google.com/search/docs/appearance/core-web-vitals

---


### Auditing and Improving Existing Pages

A page audit compares the page's intended job, current evidence and observed performance with a clear standard. Useful findings describe the problem, evidence, likely user or search impact, recommended change, owner and verification step. Improvement is a controlled cycle: establish a baseline, diagnose, prioritise, change, verify and monitor.

AI can summarise a page and detect inconsistencies, but it lacks proprietary Search Console data unless supplied and may overstate causes. Search performance changes for many reasons. A disciplined audit separates direct observations from hypotheses and avoids rewriting an entire page before the team knows which problem it is solving.

**How it works**

- Record the intended query cluster, page job and baseline clicks, impressions, CTR and position context.
- Inspect content, search appearance, links and technical state; label facts, hypotheses and unknowns.
- Prioritise by user impact, confidence and effort, implement one coherent change set and monitor.

**Worked example**

- The sample page has impressions but weak clicks for carry-on queries and a title that says only 'Products'.
- The title mismatch is an observation; its contribution to CTR is a hypothesis to test after correction.
- The plan fixes indexability first, then aligns the title/H1 and improves the guide with approved evidence.

**Decision guide**

| Use when | Avoid when |
|---|---|
| There is a defined page purpose and baseline evidence can be preserved. | A single metric movement is attributed to one cause without sufficient evidence. |
| The team can observe the page after changes and avoid changing unrelated variables at the same time. | An AI audit is used as a direct production-change list without human triage. |

**Practitioner quality lens**

- Observation: Capture what the page, source code or report actually shows.
- Hypothesis: State the suspected effect and confidence without presenting it as fact.
- Verification: Define what will be checked, by whom and over what observation window.

**Authoritative references**

- https://support.google.com/webmasters/answer/7576553
- https://support.google.com/webmasters/answer/9012289
- https://developers.google.com/search/docs/appearance/title-link

---


### Fact-Checking, Quality Control and Google Guidance

Quality control verifies claims, sources, originality, usefulness, language, rights, privacy and technical readiness. Google's guidance focuses on helpful, reliable, people-first content and asks creators to consider who made it, how it was made and why it exists. Appropriate AI assistance is not automatically prohibited; using automation primarily to manipulate rankings or create scaled low-value content can violate spam policies.

Generative systems can produce confident errors, outdated statements and unsupported comparisons. An editorial gate makes every material claim traceable and gives the editor a deliberate Publish, Repair or Hold decision. Disclosing automation may give readers useful context when they would reasonably expect to know how the material was created.

**How it works**

- Build a claim ledger and verify each material statement against an authoritative or approved source.
- Review originality, audience value, Who-How-Why context, rights, privacy and search-policy risks.
- Run the on-page and technical checks, record the human owner and choose Publish, Repair or Hold.

**Worked example**

- The AI draft says MerlionTrail products 'cut packing time by 40%' although no source supports it.
- The editor removes the claim, retains the approved repairable-material facts and records the source.
- The page is held until its noindex directive is removed and the final HTML is checked.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Every important claim can be traced, corrected or explicitly marked as unknown. | Unsupported claims are kept because they sound plausible or include a desirable keyword. |
| A named human owner can explain the page's purpose and approve publication. | Large batches of near-duplicate pages are generated without original value or editorial review. |

**Practitioner quality lens**

- Truth: Trace claims to sources and remove or qualify anything unsupported.
- Value: Confirm the page adds useful, original contribution for its intended audience.
- Readiness: Approve content, rights, privacy, search-policy and technical checks together.

**Authoritative references**

- https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
- https://developers.google.com/search/docs/essentials/spam-policies
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide

---


### Lab 4 — Create the SEO Brief, Outline, Metadata and First Draft

Learning outcome: LO3: create a grounded content package from the approved intent plan.

Goal: Produce a brief-first draft for the carry-on packing guide with traceable metadata and claims.

You will turn the approved Pack a Carry-On plan into a content brief, outline, title preference, meta description, opening and checklist. The assistant may use only supplied sources, and every factual claim must carry a source label for later verification.

**What you'll build**

work-c11/04-content-package.md containing the approved brief, outline, three title options, two meta descriptions, a selected opening and checklist, claim labels and a human edit log   (Tools: Text editor - AI assistant - content-brief-template.md - prior lab checkpoints.)

**Prerequisites**

- The Pack a Carry-On row from Lab 3 or labs/assets/checkpoint-03-intent-content-plan.csv.
- Open labs/assets/content-brief-template.md and labs/assets/merliontrail-brand-source-pack.md.
- Keep all unverified travel rules and performance claims out of the draft.

**Step-by-step**

1. Copy labs/assets/content-brief-template.md to work-c11/04-content-package.md. Complete every brief field from the Lab 3 row and source pack. Set Primary user job to 'Prepare a practical carry-on packing plan and choose when an organiser helps', Planned URL to /guides/carry-on-packing-list and Human owner to Product Editor. Add the unique contribution: a reusable seven-step checklist plus a repair-or-replace decision box.

   ```bash
   Required brief decisions:
Page type: Guide
Planned URL: /guides/carry-on-packing-list
Human owner: Product Editor
Primary user job: Prepare a practical carry-on packing plan and choose when an organiser helps
Unique contribution: Seven-step checklist + repair-or-replace decision box
Primary action: Use the checklist
Secondary action: Compare organiser options
   ```

2. Ask the assistant for an outline of five to seven H2 sections. Each row must contain Heading, Section job, Approved source and Exclusion. Reject any section whose source is UNKNOWN. Replace both placeholders between the delimiters with the full text from your completed brief and source pack before submitting.

   ```bash
   GOAL: Create a 5-7 section outline for the approved carry-on packing guide.
SOURCES: Use only text between BRIEF START/END and SOURCE START/END. If unsupported, write UNKNOWN.
OUTPUT: Heading | Section job | Approved source | Exclusion.
REVIEW: Flag duplicate coverage, unsupported claims and sections that do not advance the user job.
BRIEF START
<PASTE THE COMPLETED BRIEF>
BRIEF END
SOURCE START
<PASTE THE MERLIONTRAIL BRAND SOURCE PACK>
SOURCE END
   ```

3. Generate three concise, descriptive title preferences and two unique meta descriptions. Require a claim-to-source note for each. Choose one title and one description only after checking that both accurately match the outline. Do not use 'best', '#1', 'guaranteed' or repeated keyword variants.

   ```bash
   Create 3 title-element preferences and 2 page-specific meta descriptions for this brief. Use natural language; no keyword stuffing or unsupported superlatives. For each option, state which brief field and source fact it represents. Search systems may generate a different title link or snippet.
   ```

4. Draft a 100-150 word opening and the seven-step checklist section in 350-500 words; do not draft the entire page. Require [SOURCE: section] after every factual claim and [EDITOR INPUT NEEDED] where original experience is required. Select the final opening, then add a Human Edit Log with at least three edits for accuracy, usefulness, voice or missing experience.

   ```bash
   Draft a 100-150 word opening and a 350-500 word seven-step checklist section. Use only supplied sources. Add [SOURCE: <section>] after each factual claim and [EDITOR INPUT NEEDED] where first-hand detail is required. Finish with a claim ledger: Claim | Source | Supported yes/no | Editor action.
   ```


**Test it**

The package must have every brief field, a five-to-seven-section outline with no UNKNOWN source kept, three title options, two descriptions, one selected title and description, a selected 100-150 word opening, a 350-500 word checklist, a claim ledger and at least three human edits. Prohibited superlatives and ranking promises must be absent.

**Checkpoint and rejoin point**

Keep 04-content-package.md. Lab 5 applies its selected metadata, H1, opening and checklist to the sample HTML page. To rejoin, copy labs/assets/checkpoint-04-content-package.md and record that you used a supplied checkpoint.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The outline repeats the same advice under several headings. | Write a one-sentence job for each section and merge rows that answer the same question. |
| The meta description contains facts not visible on the page. | Remove them or add supported content to the brief before reconsidering the description. |
| The draft sounds polished but lacks a source label. | Mark the claim unsupported and either trace it to the pack, qualify it or remove it. |

**Challenge**

Write a second opening in the organisation's own voice without changing any fact. Explain which version better establishes the page job in the first two sentences.

**Reflection**

Which brief decision prevented the largest drafting error, and why?

> **Note:** The complete lab and its support-file references are in labs/lab-04-*.md. Use only the supplied synthetic MerlionTrail files or information you are authorised to process. Do not paste credentials, confidential client material or sensitive personal data into an AI assistant.

---


### Lab 5 — Audit and Optimise the Existing Page

Learning outcome: LO4: audit and improve content, on-page signals and technical SEO in a controlled sequence.

Goal: Diagnose the supplied HTML page, prioritise findings and create a corrected local version.

You will inspect a deliberately flawed local HTML page. The audit separates page purpose, on-page signals, crawl/index state and experience. You will record evidence for every finding, correct the authorised local copy, preserve a before/after diff and keep production deployment as a separate human-controlled action.

**What you'll build**

work-c11/05-page-audit.csv, work-c11/05-optimised-page.html and work-c11/05-page-changes.diff with evidence, priorities, authorised corrections and an explicit verification record   (Tools: Browser - text editor - spreadsheet - AI assistant - existing-carry-on-page.html.)

**Prerequisites**

- Selected title, meta description, opening, outline and checklist from Lab 4 or labs/assets/checkpoint-04-content-package.md.
- Copy labs/assets/existing-carry-on-page.html into work-c11 before editing.
- Use only a local file; do not access or change a live website.

**Step-by-step**

1. Open the original HTML in a browser and text editor. Create work-c11/05-page-audit.csv with the header below. Record baseline notes for the visible title, headings, links and page purpose. Add one OBSERVED row for each element you can point to in the HTML.

   ```bash
   Layer,Finding,Evidence,Impact,Hypothesis_or_Fact,Priority,Recommended_Change,Owner,Verification,Status
Layers: PURPOSE | ON_PAGE | CRAWL_INDEX | EXPERIENCE
   ```

2. Audit the four layers. Find at least: vague title, missing meta description, two H1 elements, thin opening, generic internal-link text, a JavaScript-only navigation control, noindex directive, conflicting canonical URL, missing image alt text and missing mobile viewport. Ask AI to explain - not automatically fix - each supplied fragment. Mark causal statements HYPOTHESIS unless directly observable.

   ```bash
   For each supplied HTML fragment, return:
Observed issue | Why it may matter | Fact or hypothesis | Smallest safe change | Human owner | How to verify.
Do not claim a ranking outcome and do not invent a live crawl result.
   ```

3. Prioritise findings P0, P1, P2 or P3. Use P0 for accidental noindex, P1 for canonical conflict and inaccessible navigation, P2 for title/H1/content/link alignment and P3 for refinements. Assign Content Editor or Web Developer as Owner and specify a direct verification method.

   ```bash
   P0 - prevents intended discovery/indexing or creates serious release risk
P1 - materially obstructs the preferred URL or user path
P2 - weakens clarity, relevance or accessibility
P3 - useful refinement after higher-priority work
   ```

4. Save the editable copy as work-c11/05-optimised-page.html. Remove noindex; set canonical to https://www.merliontrail.example/guides/carry-on-packing-list; add a viewport; insert the selected title, description, opening and checklist; keep one H1; and add the repair-or-replace decision box. Use /collections/carry-on-organisers with anchor 'compare carry-on organisers' and /support/repair-reuse-travel-gear with anchor 'repair and reuse support'. Add meaningful alt text.

   ```bash
   Verification checklist:
[ ] one descriptive <title> and page-specific meta description
[ ] one visible <h1> and no robots noindex
[ ] exact self-consistent canonical URL
[ ] real <a href> links with the required descriptive anchors
[ ] meaningful image alt text and mobile viewport
[ ] opening and checklist match approved sources
[ ] decision box stays within the written repair instructions
   ```

5. Create work-c11/05-page-changes.diff by comparing the source asset with the corrected HTML. In an editor use Compare Files and save the result, or run the command below from the repository root. Exit status 1 is normal when differences are found. Confirm every changed line maps to an audit row.

   ```bash
   git diff --no-index -- labs/assets/existing-carry-on-page.html work-c11/05-optimised-page.html > work-c11/05-page-changes.diff
   ```

6. Open the corrected file in the browser. Press F12, choose Elements, expand <head>, and inspect the title, meta description and canonical. Confirm robots noindex is absent. Inspect the visible H1 and both link destinations. Record exact values and VERIFIED in the matching audit rows; a visual body check alone is insufficient.

   ```bash
   Required inspected values:
canonical=https://www.merliontrail.example/guides/carry-on-packing-list
selection link=/collections/carry-on-organisers
support link=/support/repair-reuse-travel-gear
robots noindex=absent
   ```


**Test it**

The audit must contain at least ten evidence-backed findings across all four layers, one priority, owner and verification per row. The corrected HTML must pass every checklist item and open locally. The diff must show only changes represented in the audit, and head values must be verified through source or developer tools. No row may promise ranking or traffic.

**Checkpoint and rejoin point**

Keep all three Lab 5 files and do not overwrite the original asset. Lab 6 uses the corrected HTML and audit. To rejoin, copy labs/assets/checkpoint-05-optimised-page.html and labs/assets/checkpoint-05-page-audit.csv, then mark both as supplied checkpoints.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The HTML opens as raw text. | Confirm the filename ends in .html and choose a web browser rather than a text editor. |
| The page becomes blank after editing. | Undo the last change and check for a missing angle bracket or accidental deletion of body tags. |
| The assistant rewrites the full page automatically. | Discard the rewrite; request one finding at a time and make only authorised local edits yourself. |

**Challenge**

Add a second verification method for the canonical and link targets, and explain which method is less likely to miss a hidden technical defect.

**Reflection**

Which issue had the highest priority despite being invisible in the page body, and why?

> **Note:** The complete lab and its support-file references are in labs/lab-05-*.md. Use only the supplied synthetic MerlionTrail files or information you are authorised to process. Do not paste credentials, confidential client material or sensitive personal data into an AI assistant.

---


### Lab 6 — Run the Quality Gate and Build the SEO Improvement Plan

Learning outcome: LO4: fact-check the page, apply Google guidance and define a measurable improvement cycle.

Goal: Make a defensible Publish, Repair or Hold decision and create a prioritised monitoring plan.

You will complete the workflow with a claim ledger, people-first content review, synthetic performance baseline and release decision. The final plan separates observations from hypotheses and states which owner will verify content and technical changes before any live publication.

**What you'll build**

work-c11/06-quality-gate.md, work-c11/06-performance-baseline.csv and work-c11/06-action-plan.csv with claim evidence, Who-How-Why review, calculated CTR, three actions, guardrails and a final decision   (Tools: Text editor - spreadsheet - AI assistant - corrected HTML - synthetic-search-console.csv.)

**Prerequisites**

- Corrected HTML and audit from Lab 5, or labs/assets/checkpoint-05-optimised-page.html and labs/assets/checkpoint-05-page-audit.csv.
- Open labs/assets/quality-control-log-template.md and labs/assets/synthetic-search-console.csv.
- Open labs/assets/google-search-quality-sources.md and use only the dated official guidance listed there.
- Treat the performance export as synthetic training evidence, not a forecast.

**Step-by-step**

1. Copy quality-control-log-template.md to work-c11/06-quality-gate.md. Read the corrected HTML and list every material product, process or comparative claim in the Claim Ledger. Record exact wording, source, Supported Yes/No, freshness need and Editor action. Remove, qualify or HOLD unsupported claims.

   ```bash
   Claim ledger columns:
Claim | Page location | Source | Supported Yes/No | Freshness check | Editor action
   ```

2. Complete the Who-How-Why review. Who names the responsible human editor and relevant experience to add. How records AI's bounded role, sources and human edits. Why states visitor benefit independent of search traffic. Review originality, rights, privacy, scaled-content risk and whether an AI-use disclosure would provide useful context.

   ```bash
   WHO: <human owner and relevant contribution>
HOW: <AI role, supplied sources, checks and human edits>
WHY: <visitor benefit if the person arrived without Search>
Decision options: READY | REPAIR | HOLD
   ```

3. Save synthetic-search-console.csv as work-c11/06-performance-baseline.csv. Add H1=CTR. In H2 enter the exact formula below, copy through H7 and format numeric results as percentages with two decimal places. Preserve all source columns and rows. Average position is not a promise or page-quality score.

   ```bash
   Formula in H2: =IF(D2=0,"N/A",C2/D2)
Expected H2:H7: 1.50% | 1.00% | 1.33% | 2.30% | 1.43% | N/A
   ```

4. Create work-c11/06-action-plan.csv with the exact header below and exactly three page-level rows: verify indexability/canonical after release; test aligned title/H1; and improve the checklist with original editor experience. Label report values OBSERVATION and suspected causes HYPOTHESIS. Give each action a priority, owner, window, success signal and guardrail.

   ```bash
   Page,Observation,Hypothesis,Proposed_Action,Priority,Owner,Verification_Window,Success_Signal,Guardrail
Required actions: verify indexability/canonical | test aligned title/H1 | add original editor experience
   ```

5. Finish 06-quality-gate.md with one final decision: Publish, Repair or Hold. Choose Repair until a Web Developer verifies the live technical state. Cite applicable title, snippet, helpful-content or generative-AI guidance by page title and access date from google-search-quality-sources.md; do not use a vague 'Google says' reference.

   ```bash
   Final decision: REPAIR
Required reason: Local content checks complete; live indexability, canonical and release verification remain assigned to the Web Developer.
Never publish from this lab.
   ```


**Test it**

The quality gate must contain a complete claim ledger, Who-How-Why review, rights/privacy/scaled-content checks, dated official guidance citations and the required Repair decision. The performance baseline must preserve six synthetic rows and show CTR values 1.50%, 1.00%, 1.33%, 2.30%, 1.43% and N/A. The separate action plan must contain exactly three rows with priority, owner, window, success signal and guardrail. Observations and hypotheses must be visibly separate.

**Checkpoint and rejoin point**

This is the final checkpoint. The complete workflow consists of the AI-ready brief, keyword workbook, intent plan, content package, page audit, corrected HTML, quality gate, performance baseline and action plan.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The claim ledger becomes a list of every sentence. | Keep claims that affect product understanding, comparison, action or trust; transitions need no row. |
| The plan attributes low CTR to the title as a fact. | Relabel it HYPOTHESIS and define a monitored title-alignment change with other variables held stable. |
| The final decision says Publish because the local file looks correct. | Change it to Repair until an authorised owner verifies the deployed URL and technical state. |

**Challenge**

Add a stop condition for each action, such as pausing if a change harms task completion or introduces unsupported claims. Explain why guardrails matter alongside traffic metrics.

**Reflection**

What evidence would be required to change the final decision from Repair to Publish?

> **Note:** The complete lab and its support-file references are in labs/lab-06-*.md. Use only the supplied synthetic MerlionTrail files or information you are authorised to process. Do not paste credentials, confidential client material or sensitive personal data into an AI assistant.

---


### Topic 02 Recap - Mapped to Learning Outcomes

Use this checkpoint to explain what you can now do and identify any lab evidence you still need to repair.

| Learning outcome | Evidence from this topic |
|---|---|
| LO3 - Create and Optimise | Turn the approved intent plan into a source-grounded brief, outline, metadata, opening and checklist with a claim ledger and human edits. |
| LO4 - Audit and Verify | Audit purpose, on-page, crawl/index and experience layers; correct the local page; and make a source-backed Repair decision with owners, metrics and guardrails. |

---


## Wrap-Up — The Complete C11 Workflow

The final output is not merely an AI-written article. It is a traceable SEO workflow in which research evidence, model suggestions, human decisions and unknowns remain visible.

**Research**

- Start from a real audience, offer and user need.
- Record the source and date behind query evidence.
- Use AI to expand and organise; validate relevance and remove overlap.

**Create**

- Approve the brief and outline before requesting long-form prose.
- Ground titles, descriptions and content in approved sources.
- Add original experience, examples and editorial judgment.

**Optimise and verify**

- Audit purpose, on-page signals, crawl/index state and experience in layers.
- Separate observations from hypotheses and define a verification window.
- Choose Publish, Repair or Hold with a named human owner.

---


## Next Steps

- Re-run the six labs with a different synthetic page while keeping the same evidence and review gates.
- Adapt the templates to one authorised page in your organisation; replace all synthetic inputs with traceable sources.
- Use Google Search Console exports and current result-page observations to refresh decisions over time.
- Review Google Search Central guidance when platform features or policies change.


## Glossary

- **Canonical URL** — The representative URL selected from duplicate or very similar pages.
- **Crawl** — A search engine's process of discovering and fetching web resources.
- **Index** — The search engine's stored understanding of eligible content that may be served in results.
- **Internal link** — A link from one page on a site to another page on the same site.
- **Keyword evidence** — A traceable observation about query language or demand; not an unsourced AI suggestion.
- **Meta description** — A page-specific description that a search engine may use when generating a result snippet.
- **Noindex** — A directive asking compliant search engines not to include a page in their index.
- **Search intent** — The job a person is trying to complete with a query; inferred and validated, not directly observed.
- **SERP** — Search engine results page.
- **Title link** — The linked title shown for a search result; generated automatically from several sources.
- **Topic cluster** — A group of related queries and content organised around a coherent user problem.
- **G-C-C-S-O-R** — Goal, Context, Constraints, Sources, Output and Review—the C11 prompt framework.
