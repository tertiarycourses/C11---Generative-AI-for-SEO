# Lab 2 — Build the Keyword Universe and Topic Clusters

**Course:** Generative AI for SEO  
**Course Code:** C11  
**Version:** v1.0 (28 July 2026)  
**Topic 1:** Getting Started with Generative AI for SEO  
**Maps to:** LO2: build evidence-led keyword candidates and non-overlapping topic clusters  
**Duration:** 45 minutes  
**Tools:** Spreadsheet · text editor · AI assistant · synthetic-keyword-evidence.csv

---

## Goal

Turn supplied query evidence into a reviewed keyword universe and three coherent topic clusters.

## What You Will Do

You will work from a synthetic keyword evidence export, preserving source and metric labels while an AI assistant proposes additional wording and preliminary groups. You will reject invented measurements, remove irrelevant terms and make the final clustering decisions yourself.

## What You Will Build

work-c11/02-keyword-cluster-workbook.csv and work-c11/02-cluster-decisions.md with source-labelled keywords, AI suggestions, three final clusters, exclusions and overlap decisions

## Prerequisites

- Completed Lab 1 brief or the Lab 1 rejoin checkpoint.
- Open labs/assets/synthetic-keyword-evidence.csv in a spreadsheet.
- Remember that every metric in this file is synthetic training data.

> **Data note.** Use only the supplied synthetic MerlionTrail files or information you are authorised to process. Do not paste credentials, confidential client material or sensitive personal data into an AI assistant.

## Steps

### 1. Save a copy of labs/assets/synthetic-keyword-evidence.csv as work-c11/02-keyword-cluster-workbook.csv. Add six columns: Candidate_Type, Proposed_Cluster, User_Job, Evidence_Status, Human_Decision and Decision_Reason. For all supplied rows, set Candidate_Type to OBSERVED and Evidence_Status to SYNTHETIC_TRAINING_EVIDENCE.

```text
New columns:
Candidate_Type | Proposed_Cluster | User_Job | Evidence_Status | Human_Decision | Decision_Reason
```

### 2. Paste only the Query and Evidence_Note columns into the prompt below. Ask for no more than eight additional query phrasings. Append those rows to the CSV with Location, Observation_Date and both numeric fields blank; Source=AI_ASSISTANT_OUTPUT; Evidence_Note set to the generated rationale; Candidate_Type=AI_SUGGESTION; and Evidence_Status=UNVALIDATED. Never let the assistant fill volume or competition.

```text
GOAL: Suggest up to eight additional query phrasings related to the supplied evidence.
CONSTRAINTS: Do not invent volume, trend, competition or ranking difficulty. Do not repeat supplied queries. Keep suggestions relevant to MerlionTrail's approved offer.
OUTPUT: Query | Evidence_Note | Proposed user job. Label every row AI_SUGGESTION.
SOURCE START
<PASTE QUERY AND EVIDENCE_NOTE COLUMNS>
SOURCE END
```

### 3. Run the copy-ready clustering prompt below using the Query, Candidate_Type and Evidence_Status columns. Review every row and choose exactly three final cluster names: Choose Carry-On Organisers, Pack a Carry-On, and Repair or Reuse Travel Gear. Set User_Job to Learn, Compare, Act or Navigate. Mark every row KEEP, EXCLUDE or HOLD with a reason. For EXCLUDE rows set Proposed_Cluster=EXCLUDED; for unresolved HOLD rows set Proposed_Cluster=UNASSIGNED.

```text
GOAL: Propose a preliminary cluster and user job for every supplied row.
ALLOWED CLUSTERS: Choose Carry-On Organisers | Pack a Carry-On | Repair or Reuse Travel Gear.
RULES: Use semantic user need, not wording alone. Preserve Candidate_Type and Evidence_Status. Do not invent or use numeric metrics. AI_SUGGESTION rows remain UNVALIDATED.
OUTPUT: Query | Proposed_Cluster | User_Job | Recommended_Decision | Decision_Reason.
SOURCE START
<PASTE QUERY, CANDIDATE_TYPE AND EVIDENCE_STATUS>
SOURCE END
```

### 4. Create work-c11/02-cluster-decisions.md. For each final cluster record Primary user job, Example observed queries, Possible page type, Unique contribution, Overlap risk and Human decision. Add an Exclusions section naming at least three removed queries or suggestions and the reason. Save both files.

```text
Per cluster:
Primary user job: <verb phrase>
Observed queries: <at least two>
Possible page type: <guide/category/support page>
Unique contribution: <specific MerlionTrail value>
Overlap risk: <other cluster + boundary>
Human decision: KEEP | REPAIR | HOLD
```

## Test It

The CSV must preserve every supplied source and synthetic metric, contain no numeric value on an AI_SUGGESTION row, use exactly three final cluster names and give every row a human decision and reason. The decisions file must contain at least two observed queries per cluster and at least three exclusions.

## Checkpoint and Rejoin Point

Keep both Lab 2 files. Lab 3 uses the three final clusters. To rejoin, use the three named clusters and the supplied observed rows; leave unvalidated AI suggestions on Hold.

## Troubleshooting

| If this happens | Fix |
|---|---|
| CSV values shift into the wrong columns. | Undo the paste, import the file as comma-delimited UTF-8 and append AI rows one at a time. |
| The assistant assigns volume to its suggestions. | Clear the cells, set Evidence_Status=UNVALIDATED and record the defect in Decision_Reason. |
| Two clusters appear to target the same page. | Rewrite each user job. Merge the groups if the visitor would expect one page to satisfy both. |

## Challenge

Create a simple pivot table counting rows by Proposed_Cluster and Candidate_Type. Explain why a large cluster or many AI suggestions do not prove demand.

## Reflection

Which cluster boundary required the most human judgment, and what evidence resolved it?

---

[← Lab 1](lab-01-build-the-ai-ready-seo-brief-and-prompt-guardrails.md) · [Lab 3 →](lab-03-map-search-intent-and-create-the-content-plan.md)
