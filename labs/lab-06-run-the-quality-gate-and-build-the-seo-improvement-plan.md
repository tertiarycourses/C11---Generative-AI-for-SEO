# Lab 6 — Run the Quality Gate and Build the SEO Improvement Plan

**Course:** Generative AI for SEO  
**Course Code:** C11  
**Version:** v1.0 (28 July 2026)  
**Topic 2:** Creating and Optimising SEO Content with Generative AI  
**Maps to:** LO4: fact-check the page, apply Google guidance and define a measurable improvement cycle  
**Duration:** 45 minutes  
**Tools:** Text editor - spreadsheet - AI assistant - corrected HTML - synthetic-search-console.csv

---

## Goal

Make a defensible Publish, Repair or Hold decision and create a prioritised monitoring plan.

## What You Will Do

You will complete the workflow with a claim ledger, people-first content review, synthetic performance baseline and release decision. The final plan separates observations from hypotheses and states which owner will verify content and technical changes before any live publication.

## What You Will Build

work-c11/06-quality-gate.md, work-c11/06-performance-baseline.csv and work-c11/06-action-plan.csv with claim evidence, Who-How-Why review, calculated CTR, three actions, guardrails and a final decision

## Prerequisites

- Corrected HTML and audit from Lab 5, or labs/assets/checkpoint-05-optimised-page.html and labs/assets/checkpoint-05-page-audit.csv.
- Open labs/assets/quality-control-log-template.md and labs/assets/synthetic-search-console.csv.
- Open labs/assets/google-search-quality-sources.md and use only the dated official guidance listed there.
- Treat the performance export as synthetic training evidence, not a forecast.

> **Data note.** Use only the supplied synthetic MerlionTrail files or information you are authorised to process. Do not paste credentials, confidential client material or sensitive personal data into an AI assistant.

## Steps

### 1. Copy quality-control-log-template.md to work-c11/06-quality-gate.md. Read the corrected HTML and list every material product, process or comparative claim in the Claim Ledger. Record exact wording, source, Supported Yes/No, freshness need and Editor action. Remove, qualify or HOLD unsupported claims.

```text
Claim ledger columns:
Claim | Page location | Source | Supported Yes/No | Freshness check | Editor action
```

### 2. Complete the Who-How-Why review. Who names the responsible human editor and relevant experience to add. How records AI's bounded role, sources and human edits. Why states visitor benefit independent of search traffic. Review originality, rights, privacy, scaled-content risk and whether an AI-use disclosure would provide useful context.

```text
WHO: <human owner and relevant contribution>
HOW: <AI role, supplied sources, checks and human edits>
WHY: <visitor benefit if the person arrived without Search>
Decision options: READY | REPAIR | HOLD
```

### 3. Save synthetic-search-console.csv as work-c11/06-performance-baseline.csv. Add H1=CTR. In H2 enter the exact formula below, copy through H7 and format numeric results as percentages with two decimal places. Preserve all source columns and rows. Average position is not a promise or page-quality score.

```text
Formula in H2: =IF(D2=0,"N/A",C2/D2)
Expected H2:H7: 1.50% | 1.00% | 1.33% | 2.30% | 1.43% | N/A
```

### 4. Create work-c11/06-action-plan.csv with the exact header below and exactly three page-level rows: verify indexability/canonical after release; test aligned title/H1; and improve the checklist with original editor experience. Label report values OBSERVATION and suspected causes HYPOTHESIS. Give each action a priority, owner, window, success signal and guardrail.

```text
Page,Observation,Hypothesis,Proposed_Action,Priority,Owner,Verification_Window,Success_Signal,Guardrail
Required actions: verify indexability/canonical | test aligned title/H1 | add original editor experience
```

### 5. Finish 06-quality-gate.md with one final decision: Publish, Repair or Hold. Choose Repair until a Web Developer verifies the live technical state. Cite applicable title, snippet, helpful-content or generative-AI guidance by page title and access date from google-search-quality-sources.md; do not use a vague 'Google says' reference.

```text
Final decision: REPAIR
Required reason: Local content checks complete; live indexability, canonical and release verification remain assigned to the Web Developer.
Never publish from this lab.
```

## Test It

The quality gate must contain a complete claim ledger, Who-How-Why review, rights/privacy/scaled-content checks, dated official guidance citations and the required Repair decision. The performance baseline must preserve six synthetic rows and show CTR values 1.50%, 1.00%, 1.33%, 2.30%, 1.43% and N/A. The separate action plan must contain exactly three rows with priority, owner, window, success signal and guardrail. Observations and hypotheses must be visibly separate.

## Checkpoint and Rejoin Point

This is the final checkpoint. The complete workflow consists of the AI-ready brief, keyword workbook, intent plan, content package, page audit, corrected HTML, quality gate, performance baseline and action plan.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The claim ledger becomes a list of every sentence. | Keep claims that affect product understanding, comparison, action or trust; transitions need no row. |
| The plan attributes low CTR to the title as a fact. | Relabel it HYPOTHESIS and define a monitored title-alignment change with other variables held stable. |
| The final decision says Publish because the local file looks correct. | Change it to Repair until an authorised owner verifies the deployed URL and technical state. |

## Challenge

Add a stop condition for each action, such as pausing if a change harms task completion or introduces unsupported claims. Explain why guardrails matter alongside traffic metrics.

## Reflection

What evidence would be required to change the final decision from Repair to Publish?

---

[← Lab 5](lab-05-audit-and-optimise-the-existing-page.md) · [Labs index →](README.md)
