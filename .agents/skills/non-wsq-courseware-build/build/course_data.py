"""Single source of truth for C11 courseware."""

TITLE = "Generative AI for SEO"
SHORT_TITLE = "Generative AI for SEO"
COURSE_CODE = "C11"
COURSE_PAGE = "tertiarycourses.com.sg/generative-ai-for-seo.html"
VERSION = "v1.0"
VERSION_DATE = "28 July 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Assigned Tertiary Infotech Academy Trainer"
DAYS = 1
DAY_MINUTES = 480
INSTRUCTIONAL_MINUTES = 450
MODE = "Instructor-led, hands-on practical labs"
DAILY_TIMING = (
    "9:30 am – 6:30 pm (1-hour lunch; two 15-minute tea breaks; "
    "7.5 instructional hours)"
)
DARK_THEME = False

TRAINER_TEAM = [
    ("Ray Teoh Tham Kim", "Digital marketing leader with regional business-growth and training experience."),
    ("Patrick Foo", "SEO practitioner and adult educator specialising in practical website optimisation."),
    ("Janice Ong", "Business, e-commerce and digital marketing leader with extensive training experience."),
]

ICE_BREAKER = [
    "Your name, organisation and role.",
    "A page, product or service you would like more people to find.",
    "One SEO task you currently do manually.",
    "Which assistant you can access today: ChatGPT, Claude or Gemini.",
]

LEARNING_OUTCOMES = [
    "LO1: Explain how SEO and generative AI work together, set safe working boundaries and use a structured prompt-and-review method.",
    "LO2: Build an evidence-led keyword universe, topic clusters and a search-intent content plan with AI assistance.",
    "LO3: Create an SEO content brief, outline, title, meta description and on-page draft that remain grounded in approved sources.",
    "LO4: Audit and improve an existing page for content, on-page and technical SEO, then verify quality against Google guidance.",
]

TOPIC_RECAPS = {
    1: [
        (
            "LO1 - Set Up and Prompt",
            "Explain the SEO and generative-AI relationship, keep evidence separate from suggestions, and use "
            "G-C-C-S-O-R with a human review gate.",
        ),
        (
            "LO2 - Research and Plan",
            "Build labelled keyword evidence, resolve three topic clusters, and map each cluster to a distinct "
            "intent-led page with dated clues and descriptive internal links.",
        ),
    ],
    2: [
        (
            "LO3 - Create and Optimise",
            "Turn the approved intent plan into a source-grounded brief, outline, metadata, opening and checklist "
            "with a claim ledger and human edits.",
        ),
        (
            "LO4 - Audit and Verify",
            "Audit purpose, on-page, crawl/index and experience layers; correct the local page; and make a "
            "source-backed Repair decision with owners, metrics and guardrails.",
        ),
    ],
}

LO_TITLES = [
    "Set Up & Prompt",
    "Research & Plan",
    "Create & Optimise",
    "Audit & Verify",
]

TOPICS = [
    dict(
        num=1,
        code="01",
        title="Getting Started with Generative AI for SEO",
        subtitle=(
            "SEO and generative AI · ChatGPT, Claude and Gemini · keyword research "
            "and topic clusters · search intent · content planning · effective prompting"
        ),
        weighting="First half · 3 labs",
        concepts=[
            ("SEO fundamentals", "Help search engines understand a page and help people decide whether it answers their need."),
            ("AI assistants", "Use ChatGPT, Claude or Gemini to transform supplied evidence, not to invent market facts."),
            ("Keyword evidence", "Separate observed query data from AI suggestions and label assumptions explicitly."),
            ("Topic clusters", "Group related queries around one audience problem while preventing overlapping pages."),
            ("Search intent", "Infer the job behind a query, then confirm it against current result-page evidence."),
            ("Structured prompting", "Use Goal, Context, Constraints, Sources, Output and Review to make quality observable."),
        ],
        sections=[
            dict(
                title="Introduction to SEO and Generative AI",
                definition=(
                    "Search engine optimisation helps search systems understand web content and helps people decide "
                    "whether a result is useful. Search discovery is not a single ranking trick: a page must be "
                    "discoverable, crawlable, indexable, relevant to a need and useful after the click. Generative AI "
                    "can accelerate research organisation, comparison, drafting and critique, but it does not create "
                    "search demand or guarantee visibility."
                ),
                why=(
                    "A fluent AI draft can hide weak evidence. Keeping the search process and the AI workflow separate "
                    "prevents common errors such as treating invented search volume as data, assuming a keyword alone "
                    "determines ranking or publishing generic pages at scale. The practitioner remains responsible for "
                    "the purpose, evidence, editorial quality and technical state of the page."
                ),
                how=[
                    "Define the audience, business purpose and page job before opening an AI assistant.",
                    "Collect approved business facts, query evidence and current result-page observations.",
                    "Use AI to organise or transform the evidence, then verify the page and monitor real outcomes.",
                ],
                example=[
                    "MerlionTrail sells repairable travel organisers. The team wants a useful guide for carry-on packing.",
                    "Keyword evidence and current result pages suggest several related questions, but no ranking promise.",
                    "AI organises the evidence into a plan; the human owner supplies product facts and approves the result.",
                ],
                use_when=[
                    "The task has a defined user need and sources that can be supplied to the assistant.",
                    "A human can review both the output and the live page before publication.",
                ],
                avoid_when=[
                    "The goal is to mass-produce pages primarily to manipulate search visibility.",
                    "The only evidence is an AI answer with no traceable source or current query data.",
                ],
                quality=[
                    ("Purpose", "State the audience need and the useful outcome before choosing keywords."),
                    ("Evidence", "Label business facts, observed data, hypotheses and unknowns separately."),
                    ("Ownership", "Assign a human editor to approve claims, page quality and technical changes."),
                ],
                sources=[
                    "https://developers.google.com/search/docs/fundamentals/seo-starter-guide",
                    "https://developers.google.com/search/docs/essentials",
                    "https://developers.google.com/search/docs/fundamentals/using-gen-ai-content",
                ],
            ),
            dict(
                title="Setting Up ChatGPT, Claude and Gemini for SEO",
                definition=(
                    "ChatGPT, Claude and Gemini are general-purpose AI assistants with changing models and interfaces. "
                    "For this course, the tool is a workspace for grounded transformation: learners provide a source "
                    "pack, ask for a defined output and review it against a checklist. The course does not depend on a "
                    "paid tier, API key, browser extension or automatic publishing connection."
                ),
                why=(
                    "Good setup is mostly governance. Confidential strategy, personal information, credentials and "
                    "unreleased client material should not be pasted into an unapproved service. A reusable project "
                    "brief, source boundary and output convention make results more consistent across tools without "
                    "assuming that any vendor has unique access to Google ranking data."
                ),
                how=[
                    "Choose one approved assistant and create a fresh conversation for the C11 synthetic scenario.",
                    "Paste only the supplied source pack and state that missing information must be marked Unknown.",
                    "Save the prompt, output and human edits in local files so the reasoning trail is reviewable.",
                ],
                example=[
                    "A learner opens one assistant and adds the MerlionTrail source pack as delimited context.",
                    "The assistant must cite the supplied section behind each proposed claim and label any assumption.",
                    "The learner compares one small task in a second tool only if time allows; no account is mandatory.",
                ],
                use_when=[
                    "The organisation permits the selected tool and the source material is appropriate to share.",
                    "The output can be stored and reviewed before it affects a live page.",
                ],
                avoid_when=[
                    "A prompt would contain passwords, unpublished client data or sensitive personal information.",
                    "A browser add-on or automation would publish or change a website without approval.",
                ],
                quality=[
                    ("Minimum data", "Share only the context needed for the specific SEO task."),
                    ("Clear boundary", "Tell the assistant which sources it may use and how to show unknowns."),
                    ("Review trail", "Keep the input, first output, edits and final decision together."),
                ],
                sources=[
                    "https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices",
                    "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview",
                    "https://ai.google.dev/gemini-api/docs/prompting-intro",
                ],
            ),
            dict(
                title="AI-Powered Keyword Research and Topic Clusters",
                definition=(
                    "Keyword research discovers the language people use around a need. A useful keyword record includes "
                    "the query, source, date, location, evidence notes and an intended page job. A topic cluster groups "
                    "closely related queries under a coherent primary page and supporting pages; it is an information-"
                    "architecture decision, not a licence to create one near-duplicate page per phrase."
                ),
                why=(
                    "AI is good at expanding seeds, normalising wording and proposing groups, but it can fabricate "
                    "volume, competition and trends. Evidence from Keyword Planner, Search Console, customer language "
                    "or a current result-page review must remain distinguishable from an AI suggestion. Human review "
                    "removes irrelevant phrases and resolves clusters that would compete with each other."
                ),
                how=[
                    "Start with approved products, customer questions and a small set of evidence-backed seed queries.",
                    "Ask AI for labelled expansions and preliminary semantic groups without inventing numeric metrics.",
                    "Validate relevance, combine overlapping clusters and assign one clear page job to each retained group.",
                ],
                example=[
                    "Seeds include 'packing cubes singapore', 'carry on packing list' and 'repair travel organiser'.",
                    "AI proposes variants, but synthetic training metrics remain in the evidence CSV—not in the model output.",
                    "The editor keeps three clusters: choose organisers, pack a carry-on and repair/reuse travel gear.",
                ],
                use_when=[
                    "There is a real offer or audience problem and at least one traceable source of query evidence.",
                    "Clusters can be mapped to distinct page purposes rather than wording variations alone.",
                ],
                avoid_when=[
                    "Numeric demand or competition comes only from an AI response.",
                    "The plan creates many thin pages whose purpose and content substantially overlap.",
                ],
                quality=[
                    ("Source every row", "Record where the query came from and when the evidence was observed."),
                    ("Separate facts", "Keep measured values, AI suggestions and human decisions in different columns."),
                    ("Prevent overlap", "Give each retained cluster one primary need and one primary destination page."),
                ],
                sources=[
                    "https://support.google.com/google-ads/answer/7337243",
                    "https://support.google.com/google-ads/answer/9247190",
                    "https://developers.google.com/search/docs/fundamentals/seo-starter-guide",
                ],
            ),
            dict(
                title="Understanding Search Intent and Content Planning with AI",
                definition=(
                    "Search intent is the job a person is trying to complete. A practical planning heuristic labels a "
                    "query as learn, compare, act or navigate, then records the required evidence and suitable format. "
                    "Intent is inferred—not read directly from a keyword—and mixed intents are common. Current result-"
                    "page features and leading page types provide observations that a human must interpret."
                ),
                why=(
                    "A page can mention a relevant phrase yet fail the user if its format and depth do not match the "
                    "job. A content plan joins cluster, audience, intent, page type, unique value, evidence, internal "
                    "links and success signal. AI can make this matrix faster to assemble, but it cannot safely decide "
                    "business priority or claim that a result-page pattern will remain unchanged."
                ),
                how=[
                    "Review each cluster and state the user job in one sentence using an action verb.",
                    "Record current result-page observations and distinguish dominant, secondary and uncertain intent.",
                    "Choose a page type, unique contribution, evidence plan, internal links and measurable next action.",
                ],
                example=[
                    "'Carry on packing list' is mainly a learn job; a checklist guide fits better than a category page.",
                    "'Packing cubes singapore' mixes compare and act; a category page needs selection guidance and real facts.",
                    "Both pages can link naturally without repeating the same primary purpose.",
                ],
                use_when=[
                    "The team can review current search results and articulate what a satisfied visitor would accomplish.",
                    "The plan includes unique experience or approved evidence beyond a generic AI summary.",
                ],
                avoid_when=[
                    "Intent is assigned from an AI label without checking the query context or result page.",
                    "A sales page is forced onto a query whose dominant job is to learn or solve a problem.",
                ],
                quality=[
                    ("User job", "Write the desired visitor outcome before selecting the page format."),
                    ("SERP evidence", "Date observations and treat them as a snapshot, not a permanent rule."),
                    ("Unique value", "Name the experience, example or data the page contributes."),
                ],
                sources=[
                    "https://developers.google.com/search/docs/fundamentals/seo-starter-guide",
                    "https://developers.google.com/search/docs/fundamentals/creating-helpful-content",
                    "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide",
                ],
            ),
            dict(
                title="Effective Prompting for SEO Tasks",
                definition=(
                    "A prompt is a working brief. C11 uses G-C-C-S-O-R: Goal, Context, Constraints, Sources, Output and "
                    "Review. The structure tells the assistant what successful work looks like, confines it to approved "
                    "evidence and requests a self-check that a human can inspect. Prompting is iterative: the user reviews "
                    "a first output, identifies a specific defect and changes one instruction or source at a time."
                ),
                why=(
                    "Vague prompts produce generic copy and hide assumptions. A structured prompt reduces ambiguity, "
                    "makes outputs comparable and allows a claim-to-source check. It does not remove hallucination risk, "
                    "replace keyword evidence or transfer editorial accountability to the model."
                ),
                how=[
                    "State one goal and the exact audience, page job and business context.",
                    "Add constraints, delimit approved sources and specify the output schema or example.",
                    "Require a review table for unsupported claims, missing evidence and guideline risks before accepting.",
                ],
                example=[
                    "Goal: create a cluster table from the supplied CSV; Context: MerlionTrail Singapore travel gear.",
                    "Constraints: do not invent volume; Sources: only delimited rows; Output: fixed six-column table.",
                    "Review: list excluded terms, overlapping clusters and every statement not supported by a source row.",
                ],
                use_when=[
                    "The task can be evaluated against observable criteria such as fields, sources and page purpose.",
                    "The user is prepared to inspect and refine the output rather than accept the first response.",
                ],
                avoid_when=[
                    "The prompt asks the model to guarantee ranking, predict proprietary metrics or conceal AI use.",
                    "The source boundary is empty while the task requires factual claims.",
                ],
                quality=[
                    ("Specific", "Define audience, task, scope, format and the decision the output supports."),
                    ("Grounded", "Delimit sources and instruct the model to show Unknown instead of inventing."),
                    ("Testable", "Request a self-check, then perform an independent human review."),
                ],
                sources=[
                    "https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices",
                    "https://help.openai.com/en/articles/6654000-best-practices-for-prompting-chatgpt",
                    "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview",
                    "https://ai.google.dev/gemini-api/docs/prompting-intro",
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="Creating and Optimising SEO Content with Generative AI",
        subtitle=(
            "Titles and meta descriptions · briefs, outlines and long-form content · "
            "on-page and technical SEO · page audits · fact-checking · Google guidance"
        ),
        weighting="Second half · 3 labs",
        concepts=[
            ("Search appearance", "Write descriptive title and meta preferences while recognising that Google may generate alternatives."),
            ("Content brief", "Join audience, intent, evidence, unique value, structure, links and acceptance criteria."),
            ("People-first drafting", "Use AI for structure and options; add original experience, accurate facts and editorial judgment."),
            ("On-page signals", "Align visible title, headings, body, images and internal links around one clear page job."),
            ("Technical triage", "Check indexability, canonical choice, crawlable links, mobile usability and page experience."),
            ("Quality control", "Verify every material claim, disclose automation where useful and avoid scaled low-value production."),
        ],
        sections=[
            dict(
                title="Generating Titles, Meta Descriptions and On-Page Content",
                definition=(
                    "A page title is a preference used among several signals when Google creates a title link. A meta "
                    "description is a page-specific summary that Google may use when it better describes the page than "
                    "on-page text. Neither is a fixed-length ranking formula. On-page content should clearly answer the "
                    "visitor's job with a distinct main heading, useful sections and natural language."
                ),
                why=(
                    "AI can create alternatives quickly, but generic formulas often cause boilerplate titles, repeated "
                    "descriptions and keyword stuffing. The editor should choose wording that accurately represents the "
                    "page, differentiates it from other site pages and sets the right expectation before the click."
                ),
                how=[
                    "Write the page job and primary topic, then draft several descriptive and concise title options.",
                    "Create a unique meta summary using only facts actually present on that page.",
                    "Check title, visible H1, opening, sections and call to action for one coherent promise.",
                ],
                example=[
                    "Weak title: 'Packing Cubes, Packing Cube, Best Packing Cubes | MerlionTrail'.",
                    "Improved preference: 'How to Choose Packing Cubes for Carry-On Travel | MerlionTrail'.",
                    "The description summarises the selection guide and repairable construction without a ranking claim.",
                ],
                use_when=[
                    "The page has a distinct purpose and approved facts that can support a useful summary.",
                    "Alternative wording will be reviewed against the actual visible content.",
                ],
                avoid_when=[
                    "Titles repeat phrases, add unsupported superlatives or differ materially from the page.",
                    "One generic description is copied across every page.",
                ],
                quality=[
                    ("Accurate", "The title, H1, snippet preference and page content describe the same primary job."),
                    ("Distinct", "Wording differentiates this URL from other site pages."),
                    ("Natural", "Use human-readable language and avoid repeated keyword variants."),
                ],
                sources=[
                    "https://developers.google.com/search/docs/appearance/title-link",
                    "https://developers.google.com/search/docs/appearance/snippet",
                    "https://developers.google.com/search/docs/fundamentals/seo-starter-guide",
                ],
            ),
            dict(
                title="Writing Briefs, Outlines and Long-Form Content with AI",
                definition=(
                    "A content brief translates research into an editorial contract: audience, user job, primary topic, "
                    "unique value, approved sources, coverage, exclusions, internal links, conversion path and review "
                    "criteria. An outline sequences the answer. A draft turns that plan into readable content while "
                    "retaining source boundaries and the organisation's genuine experience."
                ),
                why=(
                    "Starting with 'write an SEO article' encourages generic prose and invented facts. Brief-first "
                    "generation lets the human settle strategy before wording. It also creates checkpoints: an outline "
                    "can be rejected cheaply, claims can be traced and the draft can be evaluated for completeness "
                    "without using word count as a proxy for usefulness."
                ),
                how=[
                    "Complete the brief from the approved cluster, intent plan, source pack and unique contribution.",
                    "Generate an outline with a one-sentence purpose for every section and remove duplicated coverage.",
                    "Draft section by section, preserving citations and adding human examples, edits and a final read-through.",
                ],
                example=[
                    "The carry-on guide promises a printable seven-step checklist and a repair/reuse decision table.",
                    "The outline moves from bag constraints to categories, packing order, organiser choice and a final check.",
                    "The draft uses only supplied product facts; general travel rules stay out unless independently sourced.",
                ],
                use_when=[
                    "The team can state what is uniquely useful and which sources support the page.",
                    "A human editor will review outline, claims, voice and final flow.",
                ],
                avoid_when=[
                    "The only brief is a target word count and a keyword-density request.",
                    "The model is asked to imitate a competitor or rewrite copyrighted text closely.",
                ],
                quality=[
                    ("Brief before prose", "Approve the user job, evidence and unique value before drafting."),
                    ("One section, one job", "Give each heading a clear question or decision to resolve."),
                    ("Human contribution", "Add first-hand detail, examples or judgment that the model cannot supply."),
                ],
                sources=[
                    "https://developers.google.com/search/docs/fundamentals/creating-helpful-content",
                    "https://developers.google.com/search/docs/fundamentals/using-gen-ai-content",
                    "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide",
                ],
            ),
            dict(
                title="On-Page and Technical SEO Optimisation with AI",
                definition=(
                    "On-page SEO covers the visible and embedded signals that explain one page: title, main heading, "
                    "sections, media text and internal links. Technical SEO ensures search systems can access and process "
                    "the intended version: crawlable links, an indexable response, a sensible canonical, mobile usability "
                    "and acceptable page experience. AI can explain code and propose a checklist, but the site owner must "
                    "inspect the real page and approve changes."
                ),
                why=(
                    "A strong article can remain hard to discover if it is blocked, orphaned or duplicated; technical "
                    "perfection cannot rescue unhelpful content. A layered check—purpose, on-page, crawl/index and "
                    "experience—keeps the audit proportional and prevents automated tools from producing an unprioritised "
                    "list of warnings."
                ),
                how=[
                    "Confirm the preferred URL loads, returns indexable content and has a consistent title and main heading.",
                    "Review descriptive crawlable internal links, image text, canonical choice and accidental robots directives.",
                    "Record page-experience observations, assign an owner and verify changes with the appropriate live tool.",
                ],
                example=[
                    "The sample page has a vague title, two H1 elements, a noindex directive and a JavaScript-only link.",
                    "Content edits alone will not solve the noindex issue; the release owner must remove it deliberately.",
                    "The corrected internal link uses a real anchor element and descriptive text to a related packing guide.",
                ],
                use_when=[
                    "The practitioner has authority to inspect the page and can involve a developer for release changes.",
                    "Each finding is tied to impact, evidence, owner and a verification method.",
                ],
                avoid_when=[
                    "AI-generated code is pasted into production without review, backup and testing.",
                    "Tool scores are treated as ranking guarantees or every warning receives equal priority.",
                ],
                quality=[
                    ("Layered audit", "Check page purpose, on-page signals, crawl/index state and experience separately."),
                    ("Evidence", "Record the element, URL or tool observation behind each finding."),
                    ("Release control", "Assign technical changes to an authorised owner and verify after deployment."),
                ],
                sources=[
                    "https://developers.google.com/search/docs/essentials",
                    "https://developers.google.com/search/docs/crawling-indexing/links-crawlable",
                    "https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls",
                    "https://developers.google.com/search/docs/appearance/core-web-vitals",
                ],
            ),
            dict(
                title="Auditing and Improving Existing Pages",
                definition=(
                    "A page audit compares the page's intended job, current evidence and observed performance with a "
                    "clear standard. Useful findings describe the problem, evidence, likely user or search impact, "
                    "recommended change, owner and verification step. Improvement is a controlled cycle: establish a "
                    "baseline, diagnose, prioritise, change, verify and monitor."
                ),
                why=(
                    "AI can summarise a page and detect inconsistencies, but it lacks proprietary Search Console data "
                    "unless supplied and may overstate causes. Search performance changes for many reasons. A disciplined "
                    "audit separates direct observations from hypotheses and avoids rewriting an entire page before the "
                    "team knows which problem it is solving."
                ),
                how=[
                    "Record the intended query cluster, page job and baseline clicks, impressions, CTR and position context.",
                    "Inspect content, search appearance, links and technical state; label facts, hypotheses and unknowns.",
                    "Prioritise by user impact, confidence and effort, implement one coherent change set and monitor.",
                ],
                example=[
                    "The sample page has impressions but weak clicks for carry-on queries and a title that says only 'Products'.",
                    "The title mismatch is an observation; its contribution to CTR is a hypothesis to test after correction.",
                    "The plan fixes indexability first, then aligns the title/H1 and improves the guide with approved evidence.",
                ],
                use_when=[
                    "There is a defined page purpose and baseline evidence can be preserved.",
                    "The team can observe the page after changes and avoid changing unrelated variables at the same time.",
                ],
                avoid_when=[
                    "A single metric movement is attributed to one cause without sufficient evidence.",
                    "An AI audit is used as a direct production-change list without human triage.",
                ],
                quality=[
                    ("Observation", "Capture what the page, source code or report actually shows."),
                    ("Hypothesis", "State the suspected effect and confidence without presenting it as fact."),
                    ("Verification", "Define what will be checked, by whom and over what observation window."),
                ],
                sources=[
                    "https://support.google.com/webmasters/answer/7576553",
                    "https://support.google.com/webmasters/answer/9012289",
                    "https://developers.google.com/search/docs/appearance/title-link",
                ],
            ),
            dict(
                title="Fact-Checking, Quality Control and Google Guidance",
                definition=(
                    "Quality control verifies claims, sources, originality, usefulness, language, rights, privacy and "
                    "technical readiness. Google's guidance focuses on helpful, reliable, people-first content and asks "
                    "creators to consider who made it, how it was made and why it exists. Appropriate AI assistance is "
                    "not automatically prohibited; using automation primarily to manipulate rankings or create scaled "
                    "low-value content can violate spam policies."
                ),
                why=(
                    "Generative systems can produce confident errors, outdated statements and unsupported comparisons. "
                    "An editorial gate makes every material claim traceable and gives the editor a deliberate Publish, "
                    "Repair or Hold decision. Disclosing automation may give readers useful context when they would "
                    "reasonably expect to know how the material was created."
                ),
                how=[
                    "Build a claim ledger and verify each material statement against an authoritative or approved source.",
                    "Review originality, audience value, Who-How-Why context, rights, privacy and search-policy risks.",
                    "Run the on-page and technical checks, record the human owner and choose Publish, Repair or Hold.",
                ],
                example=[
                    "The AI draft says MerlionTrail products 'cut packing time by 40%' although no source supports it.",
                    "The editor removes the claim, retains the approved repairable-material facts and records the source.",
                    "The page is held until its noindex directive is removed and the final HTML is checked.",
                ],
                use_when=[
                    "Every important claim can be traced, corrected or explicitly marked as unknown.",
                    "A named human owner can explain the page's purpose and approve publication.",
                ],
                avoid_when=[
                    "Unsupported claims are kept because they sound plausible or include a desirable keyword.",
                    "Large batches of near-duplicate pages are generated without original value or editorial review.",
                ],
                quality=[
                    ("Truth", "Trace claims to sources and remove or qualify anything unsupported."),
                    ("Value", "Confirm the page adds useful, original contribution for its intended audience."),
                    ("Readiness", "Approve content, rights, privacy, search-policy and technical checks together."),
                ],
                sources=[
                    "https://developers.google.com/search/docs/fundamentals/creating-helpful-content",
                    "https://developers.google.com/search/docs/fundamentals/using-gen-ai-content",
                    "https://developers.google.com/search/docs/essentials/spam-policies",
                    "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide",
                ],
            ),
        ],
    ),
]

DAY_THEMES = {
    1: "Research, create, optimise and verify one evidence-led SEO workflow",
}


def SCHEDULE(lab_titles):
    return {
        1: (DAY_THEMES[1], [
            ("9:30", "9:50", 20, "admin", "Welcome, course introduction, learning outcomes and safe AI working rules"),
            ("9:50", "10:35", 45, "topic", "Topic 1 - SEO, generative AI, tool setup and structured prompting"),
            ("10:35", "11:10", 35, "lab", "Hands-on: " + lab_titles([1])),
            ("11:10", "11:25", 15, "break", "Tea break"),
            ("11:25", "12:05", 40, "topic", "Topic 1 - Keyword research, topic clusters, search intent and content planning"),
            ("12:05", "12:50", 45, "lab", "Hands-on: " + lab_titles([2])),
            ("12:50", "13:00", 10, "admin", "Lab 2 verification and morning questions"),
            ("13:00", "14:00", 60, "lunch", "Lunch break"),
            ("14:00", "14:35", 35, "lab", "Hands-on: " + lab_titles([3])),
            ("14:35", "14:45", 10, "recap", "Topic 1 recap mapped to LO1 and LO2; questions and rejoin point"),
            ("14:45", "15:25", 40, "topic", "Topic 2 - Titles, snippets, briefs, outlines and people-first content"),
            ("15:25", "15:55", 30, "lab", "Hands-on: " + lab_titles([4])),
            ("15:55", "16:10", 15, "break", "Tea break"),
            ("16:10", "16:40", 30, "topic", "Topic 2 - On-page and technical SEO, auditing, quality control and Google guidance"),
            ("16:40", "17:30", 50, "lab", "Hands-on: " + lab_titles([5])),
            ("17:30", "18:15", 45, "lab", "Hands-on: " + lab_titles([6])),
            ("18:15", "18:30", 15, "recap", "Topic 2 recap mapped to LO3 and LO4; course next steps and questions"),
        ]),
    }


COURSE_OVERVIEW = dict(
    section_title="The AI-Assisted SEO Operating System",
    concepts_title="Keep Four Kinds of Information Separate",
    concepts=[
        ("Observed evidence", "Source-linked business facts, query data, page code and performance exports."),
        ("AI suggestions", "Proposals to compare or refine; never treated as measurements or guarantees."),
        ("Human decisions", "Approved audience, priority, page purpose, wording, release and stop decisions."),
        ("Unknowns", "Missing or uncertain information that stays visible until it can be resolved."),
    ],
    framework_title="G-C-C-S-O-R Prompt Framework",
    framework=[
        ("Goal", "One task and the decision the output must support."),
        ("Context", "Audience, offer, page job and business situation."),
        ("Constraints", "Scope, exclusions, tone, privacy and policy boundaries."),
        ("Sources", "Delimited evidence the assistant may use."),
        ("Output", "A precise schema, length or example."),
        ("Review", "Claim checks, missing evidence and human acceptance criteria."),
    ],
    statement=dict(
        headline="AI accelerates the workflow; evidence and judgment determine the quality.",
        body="Never ask a model to invent demand, guarantee rankings or replace the human editor.",
        kicker="C11 OPERATING PRINCIPLE",
    ),
    pillars_title="What You Will Build",
    pillars=[
        ("Research system", ["AI-ready brief", "keyword evidence", "topic clusters"]),
        ("Content system", ["intent plan", "brief and outline", "metadata and page draft"]),
        ("Quality system", ["page audit", "claim ledger", "prioritised improvement plan"]),
    ],
    arc_title="The Learning Arc in Every Lab",
    arc=[
        "Open the checkpoint and approved source files.",
        "Use a bounded prompt to transform—not invent—evidence.",
        "Make a human decision and save it in the working artifact.",
        "Run the Test It check and keep the checkpoint for the next lab.",
    ],
    deep_dives=[
        dict(
            title="The Human Review Gate",
            kicker="BEFORE ANY PAGE CHANGE",
            items=[
                ("Evidence", "Can every material claim and metric be traced?"),
                ("Intent", "Does the page help the visitor complete the intended job?"),
                ("Quality", "Is the contribution accurate, useful, original and readable?"),
                ("Technical", "Can the preferred page be crawled, indexed, linked and used?"),
                ("Rights & privacy", "Are data, quotations, media and tool use authorised?"),
                ("Decision", "Publish, Repair or Hold—with an owner and reason."),
            ],
        ),
    ],
)

LAB_SHOTS = {}

LG_INTRO = (
    "This Learner Guide accompanies Generative AI for SEO (C11). It follows the same two-topic "
    "sequence, six connected labs and learning outcomes as the slide deck, Lesson Plan and lab files. "
    "The course uses a synthetic travel-gear business so every learner can practise without exposing "
    "client data or making changes to a live website."
)
LG_INTRO2 = (
    "Use the guide as a study text before, during and after class. Each concept explains what it is, "
    "why it matters, how it works, a worked example and a decision guide. The labs then apply those "
    "concepts to one evidence-led workflow. AI output is always a draft or suggestion until a human "
    "checks its sources, usefulness, rights, privacy and technical implications."
)
LG_SETUP = dict(
    needs=[
        "A Windows or Mac laptop with a modern browser, spreadsheet application and plain-text editor.",
        "Access to at least one approved assistant: ChatGPT, Claude or Gemini; a free account is sufficient.",
        "A downloaded copy of this repository with the labs/assets folder intact.",
        "No API key, paid SEO platform, website login or live publishing access is required.",
    ],
    verify_text=(
        "Open labs/assets/merliontrail-brand-source-pack.md and labs/assets/synthetic-keyword-evidence.csv. "
        "Create a local folder named work-c11 for your outputs. Confirm that your chosen AI assistant can "
        "accept pasted text and return a Markdown table."
    ),
    verify_code=(
        "Expected local structure:\n"
        "C11---Generative-AI-for-SEO/\n"
        "  labs/assets/\n"
        "  work-c11/"
    ),
    conventions=[
        "All MerlionTrail facts and metrics are synthetic training material, not current market claims.",
        "Text between <ANGLE_BRACKETS> is a placeholder that you replace; never paste a real secret.",
        "OBSERVED means supported by a supplied source; HYPOTHESIS means a testable interpretation; UNKNOWN means unresolved.",
        "Save the prompt, first output, human edits and final decision so another person can review the trail.",
    ],
)

LAB_NOTE = (
    "Use only the supplied synthetic MerlionTrail files or information you are authorised to process. "
    "Do not paste credentials, confidential client material or sensitive personal data into an AI assistant."
)

LG_WRAPUP = dict(
    title="Wrap-Up — The Complete C11 Workflow",
    intro=(
        "The final output is not merely an AI-written article. It is a traceable SEO workflow in which "
        "research evidence, model suggestions, human decisions and unknowns remain visible."
    ),
    sections=[
        dict(
            title="Research",
            bullets=[
                "Start from a real audience, offer and user need.",
                "Record the source and date behind query evidence.",
                "Use AI to expand and organise; validate relevance and remove overlap.",
            ],
        ),
        dict(
            title="Create",
            bullets=[
                "Approve the brief and outline before requesting long-form prose.",
                "Ground titles, descriptions and content in approved sources.",
                "Add original experience, examples and editorial judgment.",
            ],
        ),
        dict(
            title="Optimise and verify",
            bullets=[
                "Audit purpose, on-page signals, crawl/index state and experience in layers.",
                "Separate observations from hypotheses and define a verification window.",
                "Choose Publish, Repair or Hold with a named human owner.",
            ],
        ),
    ],
)

LG_NEXT_STEPS = [
    "Re-run the six labs with a different synthetic page while keeping the same evidence and review gates.",
    "Adapt the templates to one authorised page in your organisation; replace all synthetic inputs with traceable sources.",
    "Use Google Search Console exports and current result-page observations to refresh decisions over time.",
    "Review Google Search Central guidance when platform features or policies change.",
]

LG_GLOSSARY = [
    ("Canonical URL", "The representative URL selected from duplicate or very similar pages."),
    ("Crawl", "A search engine's process of discovering and fetching web resources."),
    ("Index", "The search engine's stored understanding of eligible content that may be served in results."),
    ("Internal link", "A link from one page on a site to another page on the same site."),
    ("Keyword evidence", "A traceable observation about query language or demand; not an unsourced AI suggestion."),
    ("Meta description", "A page-specific description that a search engine may use when generating a result snippet."),
    ("Noindex", "A directive asking compliant search engines not to include a page in their index."),
    ("Search intent", "The job a person is trying to complete with a query; inferred and validated, not directly observed."),
    ("SERP", "Search engine results page."),
    ("Title link", "The linked title shown for a search result; generated automatically from several sources."),
    ("Topic cluster", "A group of related queries and content organised around a coherent user problem."),
    ("G-C-C-S-O-R", "Goal, Context, Constraints, Sources, Output and Review—the C11 prompt framework."),
]

NEXT_STEPS = dict(
    title="Continue the Workflow",
    items=[
        "Reuse the prompt, research and quality-control templates on an authorised page.",
        "Refresh query and result-page evidence before making a new content decision.",
        "Monitor outcomes in Search Console and distinguish observations from hypotheses.",
        "Keep a human owner accountable for every page change and publication decision.",
    ],
)

THANK_YOU = dict(
    body=(
        "You can now research, create, optimise and verify SEO content with generative AI while "
        "keeping evidence, useful purpose and human judgment in control."
    ),
    kicker="GENERATIVE AI FOR SEO · C11",
)

VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial aligned release of PPT, Learner Guide, Lesson Plan and six connected labs.", TRAINER),
]
