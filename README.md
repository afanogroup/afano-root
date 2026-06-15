# AFANO Group Holdings

A multinational, founder-led conglomerate. This repository is the **single source of truth** for strategy, governance, brand, and engineering across the Group.

## Architecture

Four-tier hierarchy modeled on Berkshire Hathaway, Mitsubishi Corporation, Samsung Group, and Dangote Group:

1. **AFANO Group Holdings, Inc.** — Delaware C-Corp parent.
2. **15 Strategic Business Groups (SBGs)** — each a wholly-owned intermediate holding entity.
3. **Business Units** — separately incorporated operating subsidiaries; independent brands and domains.
4. **Services & Sub-Services** — delivered by each Business Unit.

## Folder layout

| Folder | Contents |
|---|---|
| `00_Strategy/` | Revised holdings strategy DOCX |
| `01_Branding-Domains/` | Domain architecture (XLSX + DOCX), live RDAP results |
| `02_Visual-Identity/` | Grand Seal, Network Emblem, Network Node, 15 divisional sigils (SVG), brand guidelines |
| `03_Governance-Foundation/` | Operating Agreement, Shareholders, Buy-Sell, Board & Committee Charters, Corp Sec Playbook, Capital Budget, Multi-Jurisdiction Registration, Code of Conduct, Related-Party Policy |
| `04_Operations-Launch/` | 15 SBG Capability Statements, Marketing & Brand Standards, Shared-Services SOPs, IR Playbook, ESG Framework, Cybersecurity Policy |
| `05_Growth-Expansion/` | M&A Playbook, International Market Entry, PPP Playbook, Government Contracting, FDI Strategy |
| `06_Scale-IPO/` | IPO Readiness, Subsidiary Spinoff, Sukuk & Green Bond, Carve-Out & Divestiture |
| `websites/holdings/` | afanogroup.com — Next.js 16 App Router master site |
| `websites/divisions/<slug>/` | 15 independent Next.js scaffolds, one per SBG |
| `scripts/` | Regeneration scripts (Python) — `python-docx`, `openpyxl`, RDAP, SVG, Next.js scaffolders |

## Regenerating deliverables

```powershell
# from C:\Users\adupe\Desktop\AFANO\
.\.venv\Scripts\python.exe scripts\create_strategy_doc.py
.\.venv\Scripts\python.exe scripts\create_visual_identity.py
.\.venv\Scripts\python.exe scripts\create_brand_guidelines.py
.\.venv\Scripts\python.exe scripts\check_domains.py            # live RDAP, takes 4-5 minutes
.\.venv\Scripts\python.exe scripts\create_branding_architecture.py
.\.venv\Scripts\python.exe scripts\create_phase03_governance.py
.\.venv\Scripts\python.exe scripts\create_phase04_operations.py
.\.venv\Scripts\python.exe scripts\create_phase05_growth.py
.\.venv\Scripts\python.exe scripts\create_phase06_ipo.py
.\.venv\Scripts\python.exe scripts\scaffold_division_sites.py
```

`scripts/afano_data.py` is the canonical data module. Edit it once, regenerate everything.

## Running the holdings site

```bash
cd websites/holdings
npm install
npm run dev
# http://localhost:3000
```

## GitHub

See `GITHUB-SETUP.md`. The `github.com/afanogroup` account is currently a personal User; before pushing it needs to be either (a) converted to an Organization (recommended), (b) re-authenticated locally, or (c) repos created elsewhere and transferred.

## Currently live operating subsidiaries

| Property | Business Unit | SBG |
|---|---|---|
| https://cybitsolutions.net | Cybersecurity | SBG 3 — Technology & Digital |
| https://cybit360.com | Academy | SBG 8 — Education & Workforce |
| https://srv1736078.hstgr.cloud | Financial Services & FinTech | SBG 1 — Financial Services |

These properties keep their existing brands per the Brand Independence Policy. The hostinger temp URL should migrate to its independent brand domain pre-launch (see `01_Branding-Domains/`).
