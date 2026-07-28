# Lab 3 — Map Search Intent and Create the Content Plan

**Course:** Generative AI for SEO  
**Course Code:** C11  
**Version:** v1.0 (28 July 2026)  
**Topic 1:** Getting Started with Generative AI for SEO  
**Maps to:** LO2: translate keyword clusters into an intent-led, evidence-ready content plan  
**Duration:** 35 minutes  
**Tools:** Spreadsheet · AI assistant · cluster decisions · synthetic-serp-observations.csv

---

## Goal

Create a three-page content plan that matches user jobs and prevents page overlap.

## What You Will Do

You will convert the three reviewed clusters into a content plan. The plan distinguishes dominant and secondary intent, records dated result-page observations from a supplied snapshot and assigns each page a unique job, evidence plan, internal links and success signal.

## What You Will Build

work-c11/03-intent-content-plan.csv with one approved row per cluster plus a short cannibalisation boundary and human decision for each planned page

## Prerequisites

- Three final clusters from Lab 2.
- Open labs/assets/synthetic-serp-observations.csv.
- Use the observation date shown in the file; do not present it as a live search result.

> **Data note.** Use only the supplied synthetic MerlionTrail files or information you are authorised to process. Do not paste credentials, confidential client material or sensitive personal data into an AI assistant.

## Steps

### 1. Create work-c11/03-intent-content-plan.csv with the exact header below. Add one row for each of the three final clusters. Use these primary queries: packing cubes singapore; carry on packing list; repair packing cube zipper. For each row, combine all three matching Synthetic_Result_Page_Clues values in source-file order, separated by ' | ', and copy the common observation date. Do not add a page type yet.

```text
Cluster,Planned_URL,Human_Owner,Primary_Query,Primary_User_Job,Secondary_Intent,SERP_Observation_Date,SERP_Clues,Intent_Review,Human_Resolution,Planned_Page_Type,Page_Job,Unique_Contribution,Required_Evidence,Inbound_Link_Source,Inbound_Anchor_Text,Outbound_Link_Target,Outbound_Anchor_Text,Success_Signal,Overlap_Boundary,Human_Decision
```

### 2. For each cluster, write Primary_User_Job as a verb-led sentence. Use Learn, Compare, Act or Navigate only as Secondary_Intent labels. Ask the assistant to critique mismatches between the user job and the supplied result-page clues; it must not predict what Google will rank. Save the assistant's critique in Intent_Review and your own Keep, Repair or Reject response in Human_Resolution.

```text
Review these three cluster rows. For each, identify a mismatch between the stated user job and the supplied SERP clues, or write 'No material mismatch observed'. Use only supplied observations. Do not predict rankings or claim that the snapshot is permanent.
OUTPUT: Cluster | Intent_Review | Suggested_Repair
```

### 3. Choose one page type per row: guide for Pack a Carry-On, category/selection page for Choose Carry-On Organisers, and support guide for Repair or Reuse Travel Gear. Complete Page_Job, Unique_Contribution and Required_Evidence. Set Planned_URL to /guides/carry-on-packing-list, /collections/carry-on-organisers or /support/repair-reuse-travel-gear respectively, and set Human_Owner to Product Editor. Every unique contribution must come from the brand source pack or be marked HOLD.

```text
Required page choices:
Pack a Carry-On → /guides/carry-on-packing-list → guide
Choose Carry-On Organisers → /collections/carry-on-organisers → category/selection page
Repair or Reuse Travel Gear → /support/repair-reuse-travel-gear → support guide
```

### 4. For each row, fill Inbound_Link_Source and Inbound_Anchor_Text with the page that should link into it, then fill Outbound_Link_Target and Outbound_Anchor_Text with the page it should link to. The packing guide must link to the selection page using 'compare carry-on organisers'; the selection page must link to the guide using 'carry-on packing checklist'; both may link to the support guide using 'repair and reuse support'. Add a measurable Success_Signal such as qualified clicks or checklist completion—not a ranking guarantee. Write an Overlap_Boundary and Human_Decision for every row.

```text
Boundary pattern:
This page answers <user job>. It links to <other page> for <different job> and does not duplicate <excluded coverage>.
```

## Test It

The CSV must contain exactly three planned pages, the three specified primary queries, all three aggregated SERP clues per cluster, the supplied observation date, Intent_Review and Human_Resolution, a verb-led page job, planned URL, Product Editor owner, traceable unique contribution, descriptive anchor text in both directions, success signal, overlap boundary and human decision. No cell may promise a position, traffic amount or guaranteed result.

## Checkpoint and Rejoin Point

Keep 03-intent-content-plan.csv. Lab 4 uses the Pack a Carry-On guide row. To rejoin, select that row and use the supplied source pack plus content-brief template.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The page job merely repeats the keyword. | Rewrite it as what the visitor will be able to decide, learn or do after using the page. |
| Unique contribution is generic. | Tie it to an approved repairability, material or local-use fact from the source pack. |
| Two pages have the same success signal and coverage. | Clarify their different jobs and write distinct next actions before keeping both pages. |

## Challenge

Create a separate work-c11/03-hold-page-challenge.md for one AI-suggested page. State which evidence is missing and what must be observed before planning it; do not add a fourth row to the three-page plan.

## Reflection

How did the page job change when you considered result-page clues and overlap together?

---

[← Lab 2](lab-02-build-the-keyword-universe-and-topic-clusters.md) · [Lab 4 →](lab-04-create-the-seo-brief-outline-metadata-and-first-draft.md)
