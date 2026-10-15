# AFANO Group Holdings — Claude Code Context

## Project
AFANO Group Holdings is a multinational conglomerate (Berkshire Hathaway / Mitsubishi / Dangote style) with 15 Strategic Business Groups (SBGs). This repo is the root monorepo.

GitHub org: `github.com/afanogroup` | Remote: `afanogroup/afano-root` | Branch: `main`

## Single Source of Truth
`scripts/afano_data.py` — all BU and service data. **Never hand-edit generated output files.** Edit `afano_data.py`, then re-run the relevant generator.

## Generator Scripts (run from repo root with `.venv\Scripts\python.exe`)
| Script | Output |
|--------|--------|
| `scripts/scaffold_division_sites.py` | `websites/divisions/*/app/page.tsx` |
| `scripts/create_phase04_operations.py` | `04_Operations-Launch/` DOCX |
| `scripts/check_domains.py` | `01_Branding-Domains/Domain-Architecture.xlsx/.json` |
| `scripts/create_strategy_doc.py` | `00_Strategy/` DOCX |
| `scripts/create_phase03_governance.py` | `03_Governance-Foundation/` DOCX |
| `scripts/create_phase05_growth.py` | `05_Growth-Expansion/` DOCX |
| `scripts/create_phase06_ipo.py` | `06_Scale-IPO/` DOCX |

## Brand Tokens
- NAVY `#0B1F3A` · GOLD `#C8A04A` · IVORY `#F5F0E3` · DARK `#0A0F1A`
- Brand model: **House of Brands** — each BU has its own independent brand
- Endorsement only: "An AFANO Group Company" footer mark

## Domain Strategy
- Niche TLDs preferred: `.africa`, `.finance`, `.health`, `.green`, `.build`, `.farm`, `.gg`, `.sport`, `.travel`, `.energy`, `.consulting`
- Compound neologisms only — no `.com` for primary division-level picks
- RDAP check: `ERROR` = unknown/re-check; `REGISTERED` = taken, replace

## Known REGISTERED domains (replace in `domain_candidates.py`)
`clarivex.com`, `zenithskills.com`, `nexustradegroup.com`, `aetherguard.com`, `korvexsecurity.com`, `vulcantex.com`, `zenithstride.com`, `sahelresources.com`, `granitebuilds.com`, `veltralogistics.com`

## Git Notes
- Commit attribution: `Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>`
- If `git add` warns about embedded repos: `git rm --cached -f <dir>` + delete nested `.git` dirs, then re-stage
- Never commit `.pyc` files

## Pending Work
1. Complete RDAP second pass (`check_domains.py` stopped at 139/296)
2. Replace confirmed REGISTERED candidates in `domain_candidates.py`
3. Push updated division sites to per-division GitHub repos
4. Configure Vercel deployments

## Tech Stack
- Websites: Next.js 16 App Router · React 19 · TypeScript strict · Tailwind CSS v4
- Python: 3.13 · python-docx · openpyxl · venv at `.venv/`
- Node: 24
