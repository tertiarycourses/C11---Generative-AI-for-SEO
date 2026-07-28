"""Topic 1 labs for C11."""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Build the AI-Ready SEO Brief and Prompt Guardrails",
        duration=35,
        objective="LO1: set safe AI working boundaries and apply the G-C-C-S-O-R prompt method",
        goal="Create a grounded project brief and reusable prompt that prevent unsupported SEO claims.",
        workflow=["Prepare the workspace", "Extract approved facts", "Build G-C-C-S-O-R", "Run the evidence check"],
        desc=(
            "You will set up one AI assistant for the synthetic MerlionTrail scenario, distinguish approved facts "
            "from unknowns and create a reusable SEO prompt. The prompt will force the assistant to use supplied "
            "sources, label missing information and return a claim-to-source review."
        ),
        build=(
            "work-c11/01-ai-ready-seo-brief.md containing the audience, offer, page goal, data boundary, "
            "G-C-C-S-O-R prompt, first output and human review decision"
        ),
        services="Text editor · ChatGPT, Claude or Gemini · merliontrail-brand-source-pack.md",
        prerequisites=[
            "Download the C11 repository and keep labs/assets in the same folder.",
            "Create an empty work-c11 folder beside labs.",
            "Confirm internet access and sign in to one approved AI assistant before class; then open a fresh conversation.",
        ],
        steps=[
            (
                "Open labs/assets/merliontrail-brand-source-pack.md. Create work-c11/01-ai-ready-seo-brief.md "
                "with headings Audience, Offer, Page Goal, Approved Facts, Unknowns, Data Boundary, Prompt, "
                "First Output and Human Review. Copy only the six facts explicitly marked APPROVED into Approved "
                "Facts. Copy every item marked UNKNOWN into Unknowns.",
                "File: work-c11/01-ai-ready-seo-brief.md\n"
                "Required headings: Audience | Offer | Page Goal | Approved Facts | Unknowns | Data Boundary | "
                "Prompt | First Output | Human Review",
            ),
            (
                "Complete the brief for an audience of Singapore-based leisure travellers and a page goal of helping "
                "them choose carry-on organisers. In Data Boundary, write the exact rule below. Do not add live "
                "customer, account, search-volume or competitor data.",
                "Use only the delimited MerlionTrail source text. Treat APPROVED statements as facts. Mark anything "
                "else UNKNOWN. Do not invent search volume, rankings, reviews, certifications, product performance or "
                "customer results.",
            ),
            (
                "Build the reusable prompt using G-C-C-S-O-R. Paste the approved facts between SOURCE START and "
                "SOURCE END. Ask for a five-row table with columns Candidate idea, Audience need, Supporting source "
                "section, Unknown or assumption, and Human check. Ask for ideas only—not final copy.",
                "GOAL: Propose five useful page ideas for a Singapore-based traveller choosing carry-on organisers.\n"
                "CONTEXT: Synthetic brand MerlionTrail; audience and page goal are in my brief.\n"
                "CONSTRAINTS: No ranking promise, invented metric, testimonial, comparison or unsupported product claim.\n"
                "SOURCES: Use only text between SOURCE START and SOURCE END. Write UNKNOWN when evidence is missing.\n"
                "OUTPUT: Markdown table with exactly five rows and these columns: Candidate idea | Audience need | "
                "Supporting source section | Unknown or assumption | Human check.\n"
                "REVIEW: After the table, list every proposed statement that is not directly supported by the source.\n"
                "SOURCE START\n<PASTE APPROVED SOURCE TEXT>\nSOURCE END",
            ),
            (
                "Run the prompt in your chosen assistant. Paste the response under First Output. Under Human Review, "
                "record which one page idea you would Keep, which one you would Repair and which one you would Hold. "
                "For each decision, cite the source section or the missing evidence. Save the file.",
                "Decision format:\n"
                "KEEP — <idea> — source: <section>\n"
                "REPAIR — <idea> — change: <specific repair>\n"
                "HOLD — <idea> — missing evidence: <unknown>",
            ),
        ],
        test=(
            "The file must contain the stated audience and page goal, exactly six approved facts, all listed unknowns, "
            "the full G-C-C-S-O-R prompt, a five-row AI output, and one evidence-based Keep, Repair and Hold decision. "
            "Search the file for '%' and 'guarantee'; neither may appear unless quoted in a rejection note."
        ),
        checkpoint=(
            "Keep work-c11/01-ai-ready-seo-brief.md. Lab 2 reuses its audience, page goal, approved facts and source "
            "boundary. To rejoin, use the completed sample in labs/assets/rejoin-checkpoints.md."
        ),
        troubleshooting=[
            (
                "The assistant adds search volume or ranking claims.",
                "Delete those rows and repeat the prompt with: 'Numeric market metrics are unavailable; write UNKNOWN.'",
            ),
            (
                "The assistant cites a source that is not in the pack.",
                "Mark the row Hold and require the exact source-section heading from the delimited text.",
            ),
            (
                "The output columns differ from the requested schema.",
                "Paste the required header again and ask the assistant to reformat without changing content.",
            ),
        ],
        challenge=(
            "Run the same prompt in a second assistant. Compare only source discipline, usefulness and schema "
            "compliance; do not choose a winner based on fluency alone."
        ),
        reflection="Which instruction did the most work to keep the AI output evidence-led, and how could you tell?",
    ),
    dict(
        num=2,
        topic=1,
        title="Build the Keyword Universe and Topic Clusters",
        duration=45,
        objective="LO2: build evidence-led keyword candidates and non-overlapping topic clusters",
        goal="Turn supplied query evidence into a reviewed keyword universe and three coherent topic clusters.",
        workflow=["Inspect evidence", "Label suggestions", "Cluster by user need", "Resolve overlap"],
        desc=(
            "You will work from a synthetic keyword evidence export, preserving source and metric labels while an AI "
            "assistant proposes additional wording and preliminary groups. You will reject invented measurements, "
            "remove irrelevant terms and make the final clustering decisions yourself."
        ),
        build=(
            "work-c11/02-keyword-cluster-workbook.csv and work-c11/02-cluster-decisions.md with source-labelled "
            "keywords, AI suggestions, three final clusters, exclusions and overlap decisions"
        ),
        services="Spreadsheet · text editor · AI assistant · synthetic-keyword-evidence.csv",
        prerequisites=[
            "Completed Lab 1 brief or the Lab 1 rejoin checkpoint.",
            "Open labs/assets/synthetic-keyword-evidence.csv in a spreadsheet.",
            "Remember that every metric in this file is synthetic training data.",
        ],
        steps=[
            (
                "Save a copy of labs/assets/synthetic-keyword-evidence.csv as "
                "work-c11/02-keyword-cluster-workbook.csv. Add six columns: Candidate_Type, Proposed_Cluster, "
                "User_Job, Evidence_Status, Human_Decision and Decision_Reason. For all supplied rows, set "
                "Candidate_Type to OBSERVED and Evidence_Status to SYNTHETIC_TRAINING_EVIDENCE.",
                "New columns:\nCandidate_Type | Proposed_Cluster | User_Job | Evidence_Status | Human_Decision | Decision_Reason",
            ),
            (
                "Paste only the Query and Evidence_Note columns into the prompt below. Ask for no more than eight "
                "additional query phrasings. Append those rows to the CSV with Location, Observation_Date and both "
                "numeric fields blank; Source=AI_ASSISTANT_OUTPUT; Evidence_Note set to the generated rationale; "
                "Candidate_Type=AI_SUGGESTION; and Evidence_Status=UNVALIDATED. Never let the assistant fill volume "
                "or competition.",
                "GOAL: Suggest up to eight additional query phrasings related to the supplied evidence.\n"
                "CONSTRAINTS: Do not invent volume, trend, competition or ranking difficulty. Do not repeat supplied "
                "queries. Keep suggestions relevant to MerlionTrail's approved offer.\n"
                "OUTPUT: Query | Evidence_Note | Proposed user job. Label every row AI_SUGGESTION.\n"
                "SOURCE START\n<PASTE QUERY AND EVIDENCE_NOTE COLUMNS>\nSOURCE END",
            ),
            (
                "Run the copy-ready clustering prompt below using the Query, Candidate_Type and Evidence_Status columns. "
                "Review every row and choose exactly three final cluster names: Choose Carry-On Organisers, Pack a "
                "Carry-On, and Repair or Reuse Travel Gear. Set User_Job to Learn, Compare, Act or Navigate. Mark every "
                "row KEEP, EXCLUDE or HOLD with a reason. For EXCLUDE rows set Proposed_Cluster=EXCLUDED; for unresolved "
                "HOLD rows set Proposed_Cluster=UNASSIGNED.",
                "GOAL: Propose a preliminary cluster and user job for every supplied row.\n"
                "ALLOWED CLUSTERS: Choose Carry-On Organisers | Pack a Carry-On | Repair or Reuse Travel Gear.\n"
                "RULES: Use semantic user need, not wording alone. Preserve Candidate_Type and Evidence_Status. "
                "Do not invent or use numeric metrics. AI_SUGGESTION rows remain UNVALIDATED.\n"
                "OUTPUT: Query | Proposed_Cluster | User_Job | Recommended_Decision | Decision_Reason.\n"
                "SOURCE START\n<PASTE QUERY, CANDIDATE_TYPE AND EVIDENCE_STATUS>\nSOURCE END",
            ),
            (
                "Create work-c11/02-cluster-decisions.md. For each final cluster record Primary user job, Example "
                "observed queries, Possible page type, Unique contribution, Overlap risk and Human decision. Add an "
                "Exclusions section naming at least three removed queries or suggestions and the reason. Save both files.",
                "Per cluster:\n"
                "Primary user job: <verb phrase>\n"
                "Observed queries: <at least two>\n"
                "Possible page type: <guide/category/support page>\n"
                "Unique contribution: <specific MerlionTrail value>\n"
                "Overlap risk: <other cluster + boundary>\n"
                "Human decision: KEEP | REPAIR | HOLD",
            ),
        ],
        test=(
            "The CSV must preserve every supplied source and synthetic metric, contain no numeric value on an "
            "AI_SUGGESTION row, use exactly three final cluster names and give every row a human decision and reason. "
            "The decisions file must contain at least two observed queries per cluster and at least three exclusions."
        ),
        checkpoint=(
            "Keep both Lab 2 files. Lab 3 uses the three final clusters. To rejoin, use the three named clusters and "
            "the supplied observed rows; leave unvalidated AI suggestions on Hold."
        ),
        troubleshooting=[
            (
                "CSV values shift into the wrong columns.",
                "Undo the paste, import the file as comma-delimited UTF-8 and append AI rows one at a time.",
            ),
            (
                "The assistant assigns volume to its suggestions.",
                "Clear the cells, set Evidence_Status=UNVALIDATED and record the defect in Decision_Reason.",
            ),
            (
                "Two clusters appear to target the same page.",
                "Rewrite each user job. Merge the groups if the visitor would expect one page to satisfy both.",
            ),
        ],
        challenge=(
            "Create a simple pivot table counting rows by Proposed_Cluster and Candidate_Type. Explain why a large "
            "cluster or many AI suggestions do not prove demand."
        ),
        reflection="Which cluster boundary required the most human judgment, and what evidence resolved it?",
    ),
    dict(
        num=3,
        topic=1,
        title="Map Search Intent and Create the Content Plan",
        duration=35,
        objective="LO2: translate keyword clusters into an intent-led, evidence-ready content plan",
        goal="Create a three-page content plan that matches user jobs and prevents page overlap.",
        workflow=["State the user job", "Record SERP clues", "Choose page type", "Plan links and evidence"],
        desc=(
            "You will convert the three reviewed clusters into a content plan. The plan distinguishes dominant and "
            "secondary intent, records dated result-page observations from a supplied snapshot and assigns each page "
            "a unique job, evidence plan, internal links and success signal."
        ),
        build=(
            "work-c11/03-intent-content-plan.csv with one approved row per cluster plus a short cannibalisation "
            "boundary and human decision for each planned page"
        ),
        services="Spreadsheet · AI assistant · cluster decisions · synthetic-serp-observations.csv",
        prerequisites=[
            "Three final clusters from Lab 2.",
            "Open labs/assets/synthetic-serp-observations.csv.",
            "Use the observation date shown in the file; do not present it as a live search result.",
        ],
        steps=[
            (
                "Create work-c11/03-intent-content-plan.csv with the exact header below. Add one row for each of the "
                "three final clusters. Use these primary queries: packing cubes singapore; carry on packing list; "
                "repair packing cube zipper. For each row, combine all three matching Synthetic_Result_Page_Clues "
                "values in source-file order, separated by ' | ', and copy the common observation date. Do not add a "
                "page type yet.",
                "Cluster,Planned_URL,Human_Owner,Primary_Query,Primary_User_Job,Secondary_Intent,"
                "SERP_Observation_Date,SERP_Clues,Intent_Review,Human_Resolution,Planned_Page_Type,Page_Job,"
                "Unique_Contribution,Required_Evidence,Inbound_Link_Source,Inbound_Anchor_Text,"
                "Outbound_Link_Target,Outbound_Anchor_Text,Success_Signal,Overlap_Boundary,Human_Decision",
            ),
            (
                "For each cluster, write Primary_User_Job as a verb-led sentence. Use Learn, Compare, Act or Navigate "
                "only as Secondary_Intent labels. Ask the assistant to critique mismatches between the user job and "
                "the supplied result-page clues; it must not predict what Google will rank. Save the assistant's "
                "critique in Intent_Review and your own Keep, Repair or Reject response in Human_Resolution.",
                "Review these three cluster rows. For each, identify a mismatch between the stated user job and the "
                "supplied SERP clues, or write 'No material mismatch observed'. Use only supplied observations. "
                "Do not predict rankings or claim that the snapshot is permanent.\n"
                "OUTPUT: Cluster | Intent_Review | Suggested_Repair",
            ),
            (
                "Choose one page type per row: guide for Pack a Carry-On, category/selection page for Choose Carry-On "
                "Organisers, and support guide for Repair or Reuse Travel Gear. Complete Page_Job, Unique_Contribution "
                "and Required_Evidence. Set Planned_URL to /guides/carry-on-packing-list, "
                "/collections/carry-on-organisers or /support/repair-reuse-travel-gear respectively, and set Human_Owner "
                "to Product Editor. Every unique contribution must come from the brand source pack or be marked HOLD.",
                "Required page choices:\n"
                "Pack a Carry-On → /guides/carry-on-packing-list → guide\n"
                "Choose Carry-On Organisers → /collections/carry-on-organisers → category/selection page\n"
                "Repair or Reuse Travel Gear → /support/repair-reuse-travel-gear → support guide",
            ),
            (
                "For each row, fill Inbound_Link_Source and Inbound_Anchor_Text with the page that should link into it, "
                "then fill Outbound_Link_Target and Outbound_Anchor_Text with the page it should link to. The packing "
                "guide must link to the selection page using 'compare carry-on organisers'; the selection page must "
                "link to the guide using 'carry-on packing checklist'; both may link to the support guide using "
                "'repair and reuse support'. Add a measurable Success_Signal such as qualified clicks or checklist "
                "completion—not a ranking guarantee. Write an Overlap_Boundary and Human_Decision for every row.",
                "Boundary pattern:\n"
                "This page answers <user job>. It links to <other page> for <different job> and does not duplicate "
                "<excluded coverage>.",
            ),
        ],
        test=(
            "The CSV must contain exactly three planned pages, the three specified primary queries, all three aggregated "
            "SERP clues per cluster, the supplied observation date, Intent_Review and Human_Resolution, a verb-led page "
            "job, planned URL, Product Editor owner, traceable unique contribution, descriptive anchor text in both "
            "directions, success signal, overlap boundary and human decision. No cell may promise a position, traffic "
            "amount or guaranteed result."
        ),
        checkpoint=(
            "Keep 03-intent-content-plan.csv. Lab 4 uses the Pack a Carry-On guide row. To rejoin, select that row and "
            "use the supplied source pack plus content-brief template."
        ),
        troubleshooting=[
            (
                "The page job merely repeats the keyword.",
                "Rewrite it as what the visitor will be able to decide, learn or do after using the page.",
            ),
            (
                "Unique contribution is generic.",
                "Tie it to an approved repairability, material or local-use fact from the source pack.",
            ),
            (
                "Two pages have the same success signal and coverage.",
                "Clarify their different jobs and write distinct next actions before keeping both pages.",
            ),
        ],
        challenge=(
            "Create a separate work-c11/03-hold-page-challenge.md for one AI-suggested page. State which evidence is "
            "missing and what must be observed before planning it; do not add a fourth row to the three-page plan."
        ),
        reflection="How did the page job change when you considered result-page clues and overlap together?",
    ),
]
