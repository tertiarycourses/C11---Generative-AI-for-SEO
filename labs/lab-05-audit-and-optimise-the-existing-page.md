# Lab 5 — Audit and Optimise the Existing Page

**Course:** Generative AI for SEO  
**Course Code:** C11  
**Version:** v1.0 (28 July 2026)  
**Topic 2:** Creating and Optimising SEO Content with Generative AI  
**Maps to:** LO4: audit and improve content, on-page signals and technical SEO in a controlled sequence  
**Duration:** 50 minutes  
**Tools:** Browser - text editor - spreadsheet - AI assistant - existing-carry-on-page.html

---

## Goal

Diagnose the supplied HTML page, prioritise findings and create a corrected local version.

## What You Will Do

You will inspect a deliberately flawed local HTML page. The audit separates page purpose, on-page signals, crawl/index state and experience. You will record evidence for every finding, correct the authorised local copy, preserve a before/after diff and keep production deployment as a separate human-controlled action.

## What You Will Build

work-c11/05-page-audit.csv, work-c11/05-optimised-page.html and work-c11/05-page-changes.diff with evidence, priorities, authorised corrections and an explicit verification record

## Prerequisites

- Selected title, meta description, opening, outline and checklist from Lab 4 or labs/assets/checkpoint-04-content-package.md.
- Copy labs/assets/existing-carry-on-page.html into work-c11 before editing.
- Use only a local file; do not access or change a live website.

> **Data note.** Use only the supplied synthetic MerlionTrail files or information you are authorised to process. Do not paste credentials, confidential client material or sensitive personal data into an AI assistant.

## Steps

### 1. Open the original HTML in a browser and text editor. Create work-c11/05-page-audit.csv with the header below. Record baseline notes for the visible title, headings, links and page purpose. Add one OBSERVED row for each element you can point to in the HTML.

```text
Layer,Finding,Evidence,Impact,Hypothesis_or_Fact,Priority,Recommended_Change,Owner,Verification,Status
Layers: PURPOSE | ON_PAGE | CRAWL_INDEX | EXPERIENCE
```

### 2. Audit the four layers. Find at least: vague title, missing meta description, two H1 elements, thin opening, generic internal-link text, a JavaScript-only navigation control, noindex directive, conflicting canonical URL, missing image alt text and missing mobile viewport. Ask AI to explain - not automatically fix - each supplied fragment. Mark causal statements HYPOTHESIS unless directly observable.

```text
For each supplied HTML fragment, return:
Observed issue | Why it may matter | Fact or hypothesis | Smallest safe change | Human owner | How to verify.
Do not claim a ranking outcome and do not invent a live crawl result.
```

### 3. Prioritise findings P0, P1, P2 or P3. Use P0 for accidental noindex, P1 for canonical conflict and inaccessible navigation, P2 for title/H1/content/link alignment and P3 for refinements. Assign Content Editor or Web Developer as Owner and specify a direct verification method.

```text
P0 - prevents intended discovery/indexing or creates serious release risk
P1 - materially obstructs the preferred URL or user path
P2 - weakens clarity, relevance or accessibility
P3 - useful refinement after higher-priority work
```

### 4. Save the editable copy as work-c11/05-optimised-page.html. Remove noindex; set canonical to https://www.merliontrail.example/guides/carry-on-packing-list; add a viewport; insert the selected title, description, opening and checklist; keep one H1; and add the repair-or-replace decision box. Use /collections/carry-on-organisers with anchor 'compare carry-on organisers' and /support/repair-reuse-travel-gear with anchor 'repair and reuse support'. Add meaningful alt text.

```text
Verification checklist:
[ ] one descriptive <title> and page-specific meta description
[ ] one visible <h1> and no robots noindex
[ ] exact self-consistent canonical URL
[ ] real <a href> links with the required descriptive anchors
[ ] meaningful image alt text and mobile viewport
[ ] opening and checklist match approved sources
[ ] decision box stays within the written repair instructions
```

### 5. Create work-c11/05-page-changes.diff by comparing the source asset with the corrected HTML. In an editor use Compare Files and save the result, or run the command below from the repository root. Exit status 1 is normal when differences are found. Confirm every changed line maps to an audit row.

```text
git diff --no-index -- labs/assets/existing-carry-on-page.html work-c11/05-optimised-page.html > work-c11/05-page-changes.diff
```

### 6. Open the corrected file in the browser. Press F12, choose Elements, expand <head>, and inspect the title, meta description and canonical. Confirm robots noindex is absent. Inspect the visible H1 and both link destinations. Record exact values and VERIFIED in the matching audit rows; a visual body check alone is insufficient.

```text
Required inspected values:
canonical=https://www.merliontrail.example/guides/carry-on-packing-list
selection link=/collections/carry-on-organisers
support link=/support/repair-reuse-travel-gear
robots noindex=absent
```

## Test It

The audit must contain at least ten evidence-backed findings across all four layers, one priority, owner and verification per row. The corrected HTML must pass every checklist item and open locally. The diff must show only changes represented in the audit, and head values must be verified through source or developer tools. No row may promise ranking or traffic.

## Checkpoint and Rejoin Point

Keep all three Lab 5 files and do not overwrite the original asset. Lab 6 uses the corrected HTML and audit. To rejoin, copy labs/assets/checkpoint-05-optimised-page.html and labs/assets/checkpoint-05-page-audit.csv, then mark both as supplied checkpoints.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The HTML opens as raw text. | Confirm the filename ends in .html and choose a web browser rather than a text editor. |
| The page becomes blank after editing. | Undo the last change and check for a missing angle bracket or accidental deletion of body tags. |
| The assistant rewrites the full page automatically. | Discard the rewrite; request one finding at a time and make only authorised local edits yourself. |

## Challenge

Add a second verification method for the canonical and link targets, and explain which method is less likely to miss a hidden technical defect.

## Reflection

Which issue had the highest priority despite being invisible in the page body, and why?

---

[← Lab 4](lab-04-create-the-seo-brief-outline-metadata-and-first-draft.md) · [Lab 6 →](lab-06-run-the-quality-gate-and-build-the-seo-improvement-plan.md)
