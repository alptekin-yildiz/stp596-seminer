# stp596-seminer

[🇹🇷 Türkçe](README.md) · 🇬🇧 English

![Beta](https://img.shields.io/badge/version-v0.2.1--beta-orange) ![License: MIT](https://img.shields.io/badge/license-MIT-blue)

An **agent skill** for preparing the seminar **information form** and the **40-minute seminar presentation** of the course **STP 596 Scientific Research, Ethics and Seminar** at the ITU Aviation Institute with an AI agent. The agent first interviews you, then builds the form and the slides from the course templates. The content is yours; the agent edits, formats and checks the rules.

> ⚠️ **Please read first.** This skill is a **beta** release, it is not official course material and its use is **optional**. You verify every sentence, every source and every figure the agent writes before you submit; the responsibility is yours. Details: [Disclaimer and terms of use](#disclaimer-and-terms-of-use).

## What it produces

| Output | Format | Rule |
|---|---|---|
| Information form | A4, IEEE conference layout, two columns, Word (`stp596_bilgilendirme_form.docx` template) | Uploaded as an assignment by the Friday evening before the seminar; 2–3 pages |
| Seminar presentation | 16:9 PowerPoint (`sunum_format_16x9.pptx` template) | 40 min (~30 + 10 Q&A); 15–20 content slides; ten headings; Acknowledgements and References mandatory |

Both declare the use of AI; the agent writes the declaration from your answers.

## Installation

Required: Python 3.9+ and `pip install python-docx python-pptx` (the agent runs the scripts; in a chat-only environment it works without them, see below). Optional: [pandoc](https://pandoc.org) (macOS: `brew install pandoc`); if present, equations are written into the form and slides as editable Word/PowerPoint equations, otherwise a placeholder is left and you type the equation yourself.

**Claude Code (terminal, desktop app or VS Code extension)**
1. Use **Code → Download ZIP** at the top right and extract the folder as `~/.claude/skills/stp596-seminer/` (or `.claude/skills/stp596-seminer/` inside a project). Alternative: `git clone https://github.com/alptekin-yildiz/stp596-seminer ~/.claude/skills/stp596-seminer`
2. In a new session write "Let's prepare my STP 596 seminar presentation" or use the `/stp596-seminer` command.

**claude.ai (web)**
- If your plan supports custom skills: upload `stp596-seminer.zip` from the [Releases](https://github.com/alptekin-yildiz/stp596-seminer/releases) page under **Settings → Capabilities → Skills**; then just mention "STP 596 seminar" in the chat.
- Otherwise: open a **Project**, paste the content of `SKILL.md` as the project instructions and upload the files under `references/`, `assets/` and `scripts/` to the project.

**Codex CLI and other agents that read SKILL.md**
Put the same folder in the agent's skills directory (Codex: `~/.codex/skills/`). The format is the Agent Skills standard.

**ChatGPT (Projects)**
Open a new Project; make the content of `SKILL.md` the project instructions; upload the files under `references/`, `assets/` and `scripts/`. The scripts run in ChatGPT's Python environment; if they do not, the agent gives the form section by section and the slides one by one as text, and you transfer them to the templates.

## How it works

1. **Documents:** the agent first shows a short notice (beta, not official, verification and responsibility are yours, ask your advisor about confidential data), once in every new conversation. Then you give the agent your thesis proposal, reports, charts and reading list; the agent reads them and does not ask what it already knows.
2. **Interview:** 3 rounds, at most 23 questions; each question comes with the agent's suggested answer, so you can just say "yes". On weak answers ("no limitations", an unmeasured number, an unverified source) the agent insists. The topic is your thesis; if there is no thesis yet, that is questioned first.
3. **Plan:** form sections and a slide-by-slide claim–evidence plan; at most 4 multi-option questions (headings, figures, slide patterns, indefensible points).
4. **Form:** the agent shows the text and produces the `.docx` with your approval. Minimums apply: at least 850 words of text and 5 references.
5. **Presentation:** slide texts, patterns (table, process, comparison, cards, timeline), optional click animation; the `.pptx` is produced with your approval.
6. **Check and hand-over note:** `kontrol.py` checks the course rules automatically (including font-size consistency and maths typed on the keyboard); the agent then makes one more pass over the finished form and slides for font sizes, text inside figures and equation typesetting, and goes through the remaining items with you. Font size is uniform across the deck: one size for titles, one for body text.

The agent does not invent sources or add findings; it marks any standard domain knowledge it adds itself and deletes what you do not own. Gaps remain as `[ÖĞRENCİ TAMAMLAYACAK]` ("to be completed by the student") markers; nothing is submitted while they remain.

## Language

The interview runs in the language you write in. The form and the presentation can be in **Turkish** (default) or **English**; the agent asks in the first round. In English output the fixed texts of the templates (headings, labels, footer, "Acknowledgements") are translated by the scripts. The skill files themselves (`SKILL.md`, `references/`) are written in Turkish; the agents read them without difficulty, and the questions reach you in your language.

## Manual use (without an agent)

```bash
python3 scripts/form_doldur.py form.md --sablon assets/stp596_bilgilendirme_form.docx \
        --cikti 514xxxxxx_Surname_stp596_bilgilendirme_form.docx --tarih 02.12.2026 --dil en
python3 scripts/deste_kur.py sunum.md --sablon assets/sunum_format_16x9.pptx \
        --cikti 514xxxxxx_Surname_stp596_sunum.pptx            # front matter: dil: en
python3 scripts/anim.py 514xxxxxx_Surname_stp596_sunum.pptx anim.json      # optional click animation
python3 scripts/kontrol.py 514xxxxxx_Surname_stp596_bilgilendirme_form.docx 514xxxxxx_Surname_stp596_sunum.pptx
```

The `form.md` and `sunum.md` formats are at the end of `references/form.md` and `references/sunum.md`; working examples, including English ones, are under `ornek/`.

## Course rules (short)

| Topic | Rule |
|---|---|
| Subject | The thesis; if not mature yet, the thesis topic plus literature; as a last resort a graduation project or another project |
| Form | Uploaded by the Friday evening before the seminar; without it the seminar cannot be given |
| Duration | 40 min: ~30 min talk + 10 min Q&A; 1.5–2 min per slide |
| Headings | Title · Contents · Introduction · Literature Review · Research Method · Findings · Discussion · Conclusions · Acknowledgements · References |
| Declaration | AI use is declared in the form and in the presentation |

This table summarises the course guidelines; in case of conflict the course guidelines and the instructor's statements prevail.

## Repository layout

```
stp596-seminer/
├── SKILL.md              main instructions read by the agent (Agent Skills format)
├── references/           interview tree, form and slide rules, final review pass, animation, AI declaration, feedback report
├── assets/               stp596_bilgilendirme_form.docx, sunum_format_16x9.pptx
├── scripts/              form_doldur.py, deste_kur.py, anim.py, kontrol.py (Python only)
└── ornek/                anonymised example inputs (Turkish and English)
```

## Feedback and contributions

At the end of each use the agent writes a `geri_bildirim.md` report addressed to the author: environment, numbers, script errors, gaps in the instructions, the step that was hardest for you. The report contains no thesis content, no name and no documents; read and check it. If you wish, send it to **alptekin.yildiz@itu.edu.tr** with the subject line **"stp596-seminer geri bildirim"**. Sending it is not required and has no effect on the course; the skill is improved through these reports.

Bugs and suggestions are also welcome as [Issues](https://github.com/alptekin-yildiz/stp596-seminer/issues). Small fixes can come directly as pull requests; please open an Issue first for larger changes.

## Disclaimer and terms of use

This repository is a personal project; it is not official material of the ITU Aviation Institute or of the STP 596 course and does not bind the institution. The skill is a **beta** release; it may behave incorrectly or incompletely and may change without notice.

Its use is **not mandatory**; it is a suggestion intended to make preparing the course's form and presentation templates easier. All obligations of the course (content, submission deadline, format, duration, academic integrity) belong to the student. If the instructions in this repository conflict with the course guidelines or the instructor's statements, the course guidelines prevail.

Every text, source and figure produced by AI tools must be verified by the student before submission. Fabricated sources, unverified data or text belonging to others are the responsibility of the student, not of the tool (Council of Higher Education of Türkiye, Directive on Scientific Research and Publication Ethics). The skill promises no grade, acceptance or success.

Third-party AI services operate under their own terms of use, privacy policies and fees; which service to use and which data to upload is the student's decision. Consult your advisor before uploading confidential, contractual or unpublished thesis data to such services.

The software and documentation are provided under the MIT License "as is", without warranty of any kind, express or implied; the author cannot be held liable for any damage arising from their use (see [LICENSE](LICENSE)). The templates under `assets/` and the ITU logo are excluded from the MIT License; they may be used only within the STP 596 course and may not be used or distributed for any other purpose.

This English text is a translation provided for convenience; in case of discrepancy the Turkish text in [README.md](README.md) prevails.

## Licence, author, AI declaration

- Licence: [MIT](LICENSE); the exception for the templates and the logo is at the end of the LICENSE file.
- Author: Assoc. Prof. Dr. Alptekin Yıldız, ITU Aviation Institute.
- Claude Code (Anthropic) was used as an assisting tool in preparing this skill. The instructions and scripts were written, reviewed and tested by the author, who is responsible for them.
