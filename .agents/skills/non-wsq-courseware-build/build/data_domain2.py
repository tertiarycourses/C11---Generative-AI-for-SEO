"""Topic 2 labs for C11."""

DOMAIN2 = [
    dict(
        num=4,
        topic=2,
        title="Create the SEO Brief, Outline, Metadata and First Draft",
        duration=30,
        objective="LO3: create a grounded content package from the approved intent plan",
        goal="Produce a brief-first draft for the carry-on packing guide with traceable metadata and claims.",
        workflow=["Complete the brief", "Approve the outline", "Draft metadata", "Generate grounded copy"],
        desc=(
            "You will turn the approved Pack a Carry-On plan into a content brief, outline, title preference, meta "
            "description, opening and checklist. The assistant may use only supplied sources, and every factual claim "
            "must carry a source label for later verification."
        ),
        build=(
            "work-c11/04-content-package.md containing the approved brief, outline, three title options, two meta "
            "descriptions, a selected opening and checklist, claim labels and a human edit log"
        ),
        services="Text editor - AI assistant - content-brief-template.md - prior lab checkpoints",
        prerequisites=[
            "The Pack a Carry-On row from Lab 3 or labs/assets/checkpoint-03-intent-content-plan.csv.",
            "Open labs/assets/content-brief-template.md and labs/assets/merliontrail-brand-source-pack.md.",
            "Keep all unverified travel rules and performance claims out of the draft.",
        ],
        steps=[
            (
                "Copy labs/assets/content-brief-template.md to work-c11/04-content-package.md. Complete every brief "
                "field from the Lab 3 row and source pack. Set Primary user job to 'Prepare a practical carry-on packing "
                "plan and choose when an organiser helps', Planned URL to /guides/carry-on-packing-list and Human owner "
                "to Product Editor. Add the unique contribution: a reusable seven-step checklist plus a repair-or-replace "
                "decision box.",
                "Required brief decisions:\n"
                "Page type: Guide\n"
                "Planned URL: /guides/carry-on-packing-list\n"
                "Human owner: Product Editor\n"
                "Primary user job: Prepare a practical carry-on packing plan and choose when an organiser helps\n"
                "Unique contribution: Seven-step checklist + repair-or-replace decision box\n"
                "Primary action: Use the checklist\n"
                "Secondary action: Compare organiser options",
            ),
            (
                "Ask the assistant for an outline of five to seven H2 sections. Each row must contain Heading, Section "
                "job, Approved source and Exclusion. Reject any section whose source is UNKNOWN. Replace both placeholders "
                "between the delimiters with the full text from your completed brief and source pack before submitting.",
                "GOAL: Create a 5-7 section outline for the approved carry-on packing guide.\n"
                "SOURCES: Use only text between BRIEF START/END and SOURCE START/END. If unsupported, write UNKNOWN.\n"
                "OUTPUT: Heading | Section job | Approved source | Exclusion.\n"
                "REVIEW: Flag duplicate coverage, unsupported claims and sections that do not advance the user job.\n"
                "BRIEF START\n<PASTE THE COMPLETED BRIEF>\nBRIEF END\n"
                "SOURCE START\n<PASTE THE MERLIONTRAIL BRAND SOURCE PACK>\nSOURCE END",
            ),
            (
                "Generate three concise, descriptive title preferences and two unique meta descriptions. Require a "
                "claim-to-source note for each. Choose one title and one description only after checking that both "
                "accurately match the outline. Do not use 'best', '#1', 'guaranteed' or repeated keyword variants.",
                "Create 3 title-element preferences and 2 page-specific meta descriptions for this brief. Use natural "
                "language; no keyword stuffing or unsupported superlatives. For each option, state which brief field "
                "and source fact it represents. Search systems may generate a different title link or snippet.",
            ),
            (
                "Draft a 100-150 word opening and the seven-step checklist section in 350-500 words; do not draft the "
                "entire page. Require [SOURCE: section] after every factual claim and [EDITOR INPUT NEEDED] where original "
                "experience is required. Select the final opening, then add a Human Edit Log with at least three edits "
                "for accuracy, usefulness, voice or missing experience.",
                "Draft a 100-150 word opening and a 350-500 word seven-step checklist section. Use only supplied sources. "
                "Add [SOURCE: <section>] after each factual claim and [EDITOR INPUT NEEDED] where first-hand detail is "
                "required. Finish with a claim ledger: Claim | Source | Supported yes/no | Editor action.",
            ),
        ],
        test=(
            "The package must have every brief field, a five-to-seven-section outline with no UNKNOWN source kept, "
            "three title options, two descriptions, one selected title and description, a selected 100-150 word opening, "
            "a 350-500 word checklist, a claim ledger and at least three human edits. Prohibited superlatives and ranking "
            "promises must be absent."
        ),
        checkpoint=(
            "Keep 04-content-package.md. Lab 5 applies its selected metadata, H1, opening and checklist to the sample "
            "HTML page. To rejoin, copy labs/assets/checkpoint-04-content-package.md and record that you used a supplied "
            "checkpoint."
        ),
        troubleshooting=[
            (
                "The outline repeats the same advice under several headings.",
                "Write a one-sentence job for each section and merge rows that answer the same question.",
            ),
            (
                "The meta description contains facts not visible on the page.",
                "Remove them or add supported content to the brief before reconsidering the description.",
            ),
            (
                "The draft sounds polished but lacks a source label.",
                "Mark the claim unsupported and either trace it to the pack, qualify it or remove it.",
            ),
        ],
        challenge=(
            "Write a second opening in the organisation's own voice without changing any fact. Explain which version "
            "better establishes the page job in the first two sentences."
        ),
        reflection="Which brief decision prevented the largest drafting error, and why?",
    ),
    dict(
        num=5,
        topic=2,
        title="Audit and Optimise the Existing Page",
        duration=50,
        objective="LO4: audit and improve content, on-page signals and technical SEO in a controlled sequence",
        goal="Diagnose the supplied HTML page, prioritise findings and create a corrected local version.",
        workflow=["Baseline the page", "Audit four layers", "Prioritise findings", "Correct and verify"],
        desc=(
            "You will inspect a deliberately flawed local HTML page. The audit separates page purpose, on-page signals, "
            "crawl/index state and experience. You will record evidence for every finding, correct the authorised local "
            "copy, preserve a before/after diff and keep production deployment as a separate human-controlled action."
        ),
        build=(
            "work-c11/05-page-audit.csv, work-c11/05-optimised-page.html and work-c11/05-page-changes.diff with "
            "evidence, priorities, authorised corrections and an explicit verification record"
        ),
        services="Browser - text editor - spreadsheet - AI assistant - existing-carry-on-page.html",
        prerequisites=[
            "Selected title, meta description, opening, outline and checklist from Lab 4 or "
            "labs/assets/checkpoint-04-content-package.md.",
            "Copy labs/assets/existing-carry-on-page.html into work-c11 before editing.",
            "Use only a local file; do not access or change a live website.",
        ],
        steps=[
            (
                "Open the original HTML in a browser and text editor. Create work-c11/05-page-audit.csv with the header "
                "below. Record baseline notes for the visible title, headings, links and page purpose. Add one OBSERVED "
                "row for each element you can point to in the HTML.",
                "Layer,Finding,Evidence,Impact,Hypothesis_or_Fact,Priority,Recommended_Change,Owner,Verification,Status\n"
                "Layers: PURPOSE | ON_PAGE | CRAWL_INDEX | EXPERIENCE",
            ),
            (
                "Audit the four layers. Find at least: vague title, missing meta description, two H1 elements, thin "
                "opening, generic internal-link text, a JavaScript-only navigation control, noindex directive, conflicting "
                "canonical URL, missing image alt text and missing mobile viewport. Ask AI to explain - not automatically "
                "fix - each supplied fragment. Mark causal statements HYPOTHESIS unless directly observable.",
                "For each supplied HTML fragment, return:\n"
                "Observed issue | Why it may matter | Fact or hypothesis | Smallest safe change | Human owner | "
                "How to verify.\n"
                "Do not claim a ranking outcome and do not invent a live crawl result.",
            ),
            (
                "Prioritise findings P0, P1, P2 or P3. Use P0 for accidental noindex, P1 for canonical conflict and "
                "inaccessible navigation, P2 for title/H1/content/link alignment and P3 for refinements. Assign Content "
                "Editor or Web Developer as Owner and specify a direct verification method.",
                "P0 - prevents intended discovery/indexing or creates serious release risk\n"
                "P1 - materially obstructs the preferred URL or user path\n"
                "P2 - weakens clarity, relevance or accessibility\n"
                "P3 - useful refinement after higher-priority work",
            ),
            (
                "Save the editable copy as work-c11/05-optimised-page.html. Remove noindex; set canonical to "
                "https://www.merliontrail.example/guides/carry-on-packing-list; add a viewport; insert the selected title, "
                "description, opening and checklist; keep one H1; and add the repair-or-replace decision box. Use "
                "/collections/carry-on-organisers with anchor 'compare carry-on organisers' and "
                "/support/repair-reuse-travel-gear with anchor 'repair and reuse support'. Add meaningful alt text.",
                "Verification checklist:\n"
                "[ ] one descriptive <title> and page-specific meta description\n"
                "[ ] one visible <h1> and no robots noindex\n"
                "[ ] exact self-consistent canonical URL\n"
                "[ ] real <a href> links with the required descriptive anchors\n"
                "[ ] meaningful image alt text and mobile viewport\n"
                "[ ] opening and checklist match approved sources\n"
                "[ ] decision box stays within the written repair instructions",
            ),
            (
                "Create work-c11/05-page-changes.diff by comparing the source asset with the corrected HTML. In an "
                "editor use Compare Files and save the result, or run the command below from the repository root. Exit "
                "status 1 is normal when differences are found. Confirm every changed line maps to an audit row.",
                "git diff --no-index -- labs/assets/existing-carry-on-page.html "
                "work-c11/05-optimised-page.html > work-c11/05-page-changes.diff",
            ),
            (
                "Open the corrected file in the browser. Press F12, choose Elements, expand <head>, and inspect the title, "
                "meta description and canonical. Confirm robots noindex is absent. Inspect the visible H1 and both link "
                "destinations. Record exact values and VERIFIED in the matching audit rows; a visual body check alone is "
                "insufficient.",
                "Required inspected values:\n"
                "canonical=https://www.merliontrail.example/guides/carry-on-packing-list\n"
                "selection link=/collections/carry-on-organisers\n"
                "support link=/support/repair-reuse-travel-gear\n"
                "robots noindex=absent",
            ),
        ],
        test=(
            "The audit must contain at least ten evidence-backed findings across all four layers, one priority, owner "
            "and verification per row. The corrected HTML must pass every checklist item and open locally. The diff must "
            "show only changes represented in the audit, and head values must be verified through source or developer "
            "tools. No row may promise ranking or traffic."
        ),
        checkpoint=(
            "Keep all three Lab 5 files and do not overwrite the original asset. Lab 6 uses the corrected HTML and audit. "
            "To rejoin, copy labs/assets/checkpoint-05-optimised-page.html and "
            "labs/assets/checkpoint-05-page-audit.csv, then mark both as supplied checkpoints."
        ),
        troubleshooting=[
            (
                "The HTML opens as raw text.",
                "Confirm the filename ends in .html and choose a web browser rather than a text editor.",
            ),
            (
                "The page becomes blank after editing.",
                "Undo the last change and check for a missing angle bracket or accidental deletion of body tags.",
            ),
            (
                "The assistant rewrites the full page automatically.",
                "Discard the rewrite; request one finding at a time and make only authorised local edits yourself.",
            ),
        ],
        challenge=(
            "Add a second verification method for the canonical and link targets, and explain which method is less "
            "likely to miss a hidden technical defect."
        ),
        reflection="Which issue had the highest priority despite being invisible in the page body, and why?",
    ),
    dict(
        num=6,
        topic=2,
        title="Run the Quality Gate and Build the SEO Improvement Plan",
        duration=45,
        objective="LO4: fact-check the page, apply Google guidance and define a measurable improvement cycle",
        goal="Make a defensible Publish, Repair or Hold decision and create a prioritised monitoring plan.",
        workflow=["Build the claim ledger", "Apply Who-How-Why", "Review performance evidence", "Decide and monitor"],
        desc=(
            "You will complete the workflow with a claim ledger, people-first content review, synthetic performance "
            "baseline and release decision. The final plan separates observations from hypotheses and states which "
            "owner will verify content and technical changes before any live publication."
        ),
        build=(
            "work-c11/06-quality-gate.md, work-c11/06-performance-baseline.csv and work-c11/06-action-plan.csv with "
            "claim evidence, Who-How-Why review, calculated CTR, three actions, guardrails and a final decision"
        ),
        services="Text editor - spreadsheet - AI assistant - corrected HTML - synthetic-search-console.csv",
        prerequisites=[
            "Corrected HTML and audit from Lab 5, or labs/assets/checkpoint-05-optimised-page.html and "
            "labs/assets/checkpoint-05-page-audit.csv.",
            "Open labs/assets/quality-control-log-template.md and labs/assets/synthetic-search-console.csv.",
            "Open labs/assets/google-search-quality-sources.md and use only the dated official guidance listed there.",
            "Treat the performance export as synthetic training evidence, not a forecast.",
        ],
        steps=[
            (
                "Copy quality-control-log-template.md to work-c11/06-quality-gate.md. Read the corrected HTML and list "
                "every material product, process or comparative claim in the Claim Ledger. Record exact wording, source, "
                "Supported Yes/No, freshness need and Editor action. Remove, qualify or HOLD unsupported claims.",
                "Claim ledger columns:\n"
                "Claim | Page location | Source | Supported Yes/No | Freshness check | Editor action",
            ),
            (
                "Complete the Who-How-Why review. Who names the responsible human editor and relevant experience to add. "
                "How records AI's bounded role, sources and human edits. Why states visitor benefit independent of search "
                "traffic. Review originality, rights, privacy, scaled-content risk and whether an AI-use disclosure would "
                "provide useful context.",
                "WHO: <human owner and relevant contribution>\n"
                "HOW: <AI role, supplied sources, checks and human edits>\n"
                "WHY: <visitor benefit if the person arrived without Search>\n"
                "Decision options: READY | REPAIR | HOLD",
            ),
            (
                "Save synthetic-search-console.csv as work-c11/06-performance-baseline.csv. Add H1=CTR. In H2 enter the "
                "exact formula below, copy through H7 and format numeric results as percentages with two decimal places. "
                "Preserve all source columns and rows. Average position is not a promise or page-quality score.",
                "Formula in H2: =IF(D2=0,\"N/A\",C2/D2)\n"
                "Expected H2:H7: 1.50% | 1.00% | 1.33% | 2.30% | 1.43% | N/A",
            ),
            (
                "Create work-c11/06-action-plan.csv with the exact header below and exactly three page-level rows: verify "
                "indexability/canonical after release; test aligned title/H1; and improve the checklist with original "
                "editor experience. Label report values OBSERVATION and suspected causes HYPOTHESIS. Give each action a "
                "priority, owner, window, success signal and guardrail.",
                "Page,Observation,Hypothesis,Proposed_Action,Priority,Owner,Verification_Window,Success_Signal,Guardrail\n"
                "Required actions: verify indexability/canonical | test aligned title/H1 | add original editor experience",
            ),
            (
                "Finish 06-quality-gate.md with one final decision: Publish, Repair or Hold. Choose Repair until a Web "
                "Developer verifies the live technical state. Cite applicable title, snippet, helpful-content or "
                "generative-AI guidance by page title and access date from google-search-quality-sources.md; do not use a "
                "vague 'Google says' reference.",
                "Final decision: REPAIR\n"
                "Required reason: Local content checks complete; live indexability, canonical and release verification "
                "remain assigned to the Web Developer.\n"
                "Never publish from this lab.",
            ),
        ],
        test=(
            "The quality gate must contain a complete claim ledger, Who-How-Why review, rights/privacy/scaled-content "
            "checks, dated official guidance citations and the required Repair decision. The performance baseline must "
            "preserve six synthetic rows and show CTR values 1.50%, 1.00%, 1.33%, 2.30%, 1.43% and N/A. The separate "
            "action plan must contain exactly three rows with priority, owner, window, success signal and guardrail. "
            "Observations and hypotheses must be visibly separate."
        ),
        checkpoint=(
            "This is the final checkpoint. The complete workflow consists of the AI-ready brief, keyword workbook, "
            "intent plan, content package, page audit, corrected HTML, quality gate, performance baseline and action plan."
        ),
        troubleshooting=[
            (
                "The claim ledger becomes a list of every sentence.",
                "Keep claims that affect product understanding, comparison, action or trust; transitions need no row.",
            ),
            (
                "The plan attributes low CTR to the title as a fact.",
                "Relabel it HYPOTHESIS and define a monitored title-alignment change with other variables held stable.",
            ),
            (
                "The final decision says Publish because the local file looks correct.",
                "Change it to Repair until an authorised owner verifies the deployed URL and technical state.",
            ),
        ],
        challenge=(
            "Add a stop condition for each action, such as pausing if a change harms task completion or introduces "
            "unsupported claims. Explain why guardrails matter alongside traffic metrics."
        ),
        reflection="What evidence would be required to change the final decision from Repair to Publish?",
    ),
]
