# C11---Generative-AI-for-SEO

Complete aligned courseware for **Generative AI for SEO (C11)**.

## Course package

- Trainer slide deck and learner-slide PDF: `courseware/`
- Learner Guide in DOCX, PDF and Markdown: `courseware/` and repository root
- Lesson Plan in DOCX and PDF: `courseware/`
- Six connected hands-on labs and synthetic support files: `labs/`
- Single-source content modules and build engine: `.agents/skills/non-wsq-courseware-build/`

The two-topic content spine follows the approved course page:

1. Getting Started with Generative AI for SEO
2. Creating and Optimising SEO Content with Generative AI

Every artifact is generated from the same `course_data.py`, `data_domain1.py` and
`data_domain2.py` modules. Lab numbers, titles, objectives, sequence and verification
criteria therefore remain synchronised across the slide deck, Learner Guide, Lesson
Plan and lab files.

## Build

Run from Git Bash on Windows:

```bash
COURSE_REPO="$(pwd)" bash ".agents/skills/non-wsq-courseware-build/build/build_courseware.sh"
```

## Source standard

Concept teaching is based on the official C11 outline and authoritative primary
documentation from Google Search Central, Google Ads Help, OpenAI, Anthropic and
Google AI for Developers. Links are embedded in the single-source content module and
rendered into the Learner Guide.

All MerlionTrail business information, keyword values, result-page observations and
Search Console values are clearly labelled synthetic training data.
