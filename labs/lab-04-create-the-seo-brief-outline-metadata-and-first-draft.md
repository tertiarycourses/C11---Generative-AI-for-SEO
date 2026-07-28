# Lab 4 — Create the SEO Brief, Outline, Metadata and First Draft

**Course:** Generative AI for SEO  
**Course Code:** C11  
**Version:** v1.0 (28 July 2026)  
**Topic 2:** Creating and Optimising SEO Content with Generative AI  
**Maps to:** LO3: create a grounded content package from the approved intent plan  
**Duration:** 30 minutes  
**Tools:** Text editor - AI assistant - content-brief-template.md - prior lab checkpoints

---

## Goal

Produce a brief-first draft for the carry-on packing guide with traceable metadata and claims.

## What You Will Do

You will turn the approved Pack a Carry-On plan into a content brief, outline, title preference, meta description, opening and checklist. The assistant may use only supplied sources, and every factual claim must carry a source label for later verification.

## What You Will Build

work-c11/04-content-package.md containing the approved brief, outline, three title options, two meta descriptions, a selected opening and checklist, claim labels and a human edit log

## Prerequisites

- The Pack a Carry-On row from Lab 3 or labs/assets/checkpoint-03-intent-content-plan.csv.
- Open labs/assets/content-brief-template.md and labs/assets/merliontrail-brand-source-pack.md.
- Keep all unverified travel rules and performance claims out of the draft.

> **Data note.** Use only the supplied synthetic MerlionTrail files or information you are authorised to process. Do not paste credentials, confidential client material or sensitive personal data into an AI assistant.

## Steps

### 1. Copy labs/assets/content-brief-template.md to work-c11/04-content-package.md. Complete every brief field from the Lab 3 row and source pack. Set Primary user job to 'Prepare a practical carry-on packing plan and choose when an organiser helps', Planned URL to /guides/carry-on-packing-list and Human owner to Product Editor. Add the unique contribution: a reusable seven-step checklist plus a repair-or-replace decision box.

```text
Required brief decisions:
Page type: Guide
Planned URL: /guides/carry-on-packing-list
Human owner: Product Editor
Primary user job: Prepare a practical carry-on packing plan and choose when an organiser helps
Unique contribution: Seven-step checklist + repair-or-replace decision box
Primary action: Use the checklist
Secondary action: Compare organiser options
```

### 2. Ask the assistant for an outline of five to seven H2 sections. Each row must contain Heading, Section job, Approved source and Exclusion. Reject any section whose source is UNKNOWN. Replace both placeholders between the delimiters with the full text from your completed brief and source pack before submitting.

```text
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

### 3. Generate three concise, descriptive title preferences and two unique meta descriptions. Require a claim-to-source note for each. Choose one title and one description only after checking that both accurately match the outline. Do not use 'best', '#1', 'guaranteed' or repeated keyword variants.

```text
Create 3 title-element preferences and 2 page-specific meta descriptions for this brief. Use natural language; no keyword stuffing or unsupported superlatives. For each option, state which brief field and source fact it represents. Search systems may generate a different title link or snippet.
```

### 4. Draft a 100-150 word opening and the seven-step checklist section in 350-500 words; do not draft the entire page. Require [SOURCE: section] after every factual claim and [EDITOR INPUT NEEDED] where original experience is required. Select the final opening, then add a Human Edit Log with at least three edits for accuracy, usefulness, voice or missing experience.

```text
Draft a 100-150 word opening and a 350-500 word seven-step checklist section. Use only supplied sources. Add [SOURCE: <section>] after each factual claim and [EDITOR INPUT NEEDED] where first-hand detail is required. Finish with a claim ledger: Claim | Source | Supported yes/no | Editor action.
```

## Test It

The package must have every brief field, a five-to-seven-section outline with no UNKNOWN source kept, three title options, two descriptions, one selected title and description, a selected 100-150 word opening, a 350-500 word checklist, a claim ledger and at least three human edits. Prohibited superlatives and ranking promises must be absent.

## Checkpoint and Rejoin Point

Keep 04-content-package.md. Lab 5 applies its selected metadata, H1, opening and checklist to the sample HTML page. To rejoin, copy labs/assets/checkpoint-04-content-package.md and record that you used a supplied checkpoint.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The outline repeats the same advice under several headings. | Write a one-sentence job for each section and merge rows that answer the same question. |
| The meta description contains facts not visible on the page. | Remove them or add supported content to the brief before reconsidering the description. |
| The draft sounds polished but lacks a source label. | Mark the claim unsupported and either trace it to the pack, qualify it or remove it. |

## Challenge

Write a second opening in the organisation's own voice without changing any fact. Explain which version better establishes the page job in the first two sentences.

## Reflection

Which brief decision prevented the largest drafting error, and why?

---

[← Lab 3](lab-03-map-search-intent-and-create-the-content-plan.md) · [Lab 5 →](lab-05-audit-and-optimise-the-existing-page.md)
