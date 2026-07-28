# Lab 1 — Build the AI-Ready SEO Brief and Prompt Guardrails

**Course:** Generative AI for SEO  
**Course Code:** C11  
**Version:** v1.0 (28 July 2026)  
**Topic 1:** Getting Started with Generative AI for SEO  
**Maps to:** LO1: set safe AI working boundaries and apply the G-C-C-S-O-R prompt method  
**Duration:** 35 minutes  
**Tools:** Text editor · ChatGPT, Claude or Gemini · merliontrail-brand-source-pack.md

---

## Goal

Create a grounded project brief and reusable prompt that prevent unsupported SEO claims.

## What You Will Do

You will set up one AI assistant for the synthetic MerlionTrail scenario, distinguish approved facts from unknowns and create a reusable SEO prompt. The prompt will force the assistant to use supplied sources, label missing information and return a claim-to-source review.

## What You Will Build

work-c11/01-ai-ready-seo-brief.md containing the audience, offer, page goal, data boundary, G-C-C-S-O-R prompt, first output and human review decision

## Prerequisites

- Download the C11 repository and keep labs/assets in the same folder.
- Create an empty work-c11 folder beside labs.
- Confirm internet access and sign in to one approved AI assistant before class; then open a fresh conversation.

> **Data note.** Use only the supplied synthetic MerlionTrail files or information you are authorised to process. Do not paste credentials, confidential client material or sensitive personal data into an AI assistant.

## Steps

### 1. Open labs/assets/merliontrail-brand-source-pack.md. Create work-c11/01-ai-ready-seo-brief.md with headings Audience, Offer, Page Goal, Approved Facts, Unknowns, Data Boundary, Prompt, First Output and Human Review. Copy only the six facts explicitly marked APPROVED into Approved Facts. Copy every item marked UNKNOWN into Unknowns.

```text
File: work-c11/01-ai-ready-seo-brief.md
Required headings: Audience | Offer | Page Goal | Approved Facts | Unknowns | Data Boundary | Prompt | First Output | Human Review
```

### 2. Complete the brief for an audience of Singapore-based leisure travellers and a page goal of helping them choose carry-on organisers. In Data Boundary, write the exact rule below. Do not add live customer, account, search-volume or competitor data.

```text
Use only the delimited MerlionTrail source text. Treat APPROVED statements as facts. Mark anything else UNKNOWN. Do not invent search volume, rankings, reviews, certifications, product performance or customer results.
```

### 3. Build the reusable prompt using G-C-C-S-O-R. Paste the approved facts between SOURCE START and SOURCE END. Ask for a five-row table with columns Candidate idea, Audience need, Supporting source section, Unknown or assumption, and Human check. Ask for ideas only—not final copy.

```text
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

### 4. Run the prompt in your chosen assistant. Paste the response under First Output. Under Human Review, record which one page idea you would Keep, which one you would Repair and which one you would Hold. For each decision, cite the source section or the missing evidence. Save the file.

```text
Decision format:
KEEP — <idea> — source: <section>
REPAIR — <idea> — change: <specific repair>
HOLD — <idea> — missing evidence: <unknown>
```

## Test It

The file must contain the stated audience and page goal, exactly six approved facts, all listed unknowns, the full G-C-C-S-O-R prompt, a five-row AI output, and one evidence-based Keep, Repair and Hold decision. Search the file for '%' and 'guarantee'; neither may appear unless quoted in a rejection note.

## Checkpoint and Rejoin Point

Keep work-c11/01-ai-ready-seo-brief.md. Lab 2 reuses its audience, page goal, approved facts and source boundary. To rejoin, use the completed sample in labs/assets/rejoin-checkpoints.md.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The assistant adds search volume or ranking claims. | Delete those rows and repeat the prompt with: 'Numeric market metrics are unavailable; write UNKNOWN.' |
| The assistant cites a source that is not in the pack. | Mark the row Hold and require the exact source-section heading from the delimited text. |
| The output columns differ from the requested schema. | Paste the required header again and ask the assistant to reformat without changing content. |

## Challenge

Run the same prompt in a second assistant. Compare only source discipline, usefulness and schema compliance; do not choose a winner based on fluency alone.

## Reflection

Which instruction did the most work to keep the AI output evidence-led, and how could you tell?

---

[← Labs index](README.md) · [Lab 2 →](lab-02-build-the-keyword-universe-and-topic-clusters.md)
