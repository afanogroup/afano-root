# AFANO GitHub Setup

## Current state

- `github.com/afanogroup` exists as a **personal User account** (0 repos, public).
- Local `gh` CLI is authenticated as **`officialprofab`** with scopes `repo, workflow, gist, read:org`.
- Because `afanogroup` is a User (not Org), `officialprofab` cannot create repos under it. There are three resolution paths — your call.

## Resolution Path 1 (Recommended for a multinational): Convert `afanogroup` into an Organization

1. Sign in as `afanogroup` at https://github.com/settings/organizations
2. Click **New organization** — choose the Free plan for now (upgrade to Team/Enterprise later).
3. Important: GitHub does NOT let you rename a User to an Org *directly*. The supported approach is:
   - Rename the existing `afanogroup` User to something else (e.g. `afanogroup-personal`).
   - Create a new Organization named `afanogroup` (now free).
   - Invite `officialprofab` as Owner of the new Org.
4. After acceptance, run: `gh org list` to confirm `afanogroup` shows up.
5. Then run the repo-creation block at the bottom of this file.

This is the right answer for the long term: orgs give you teams (one per SBG), fine-grained roles, SAML SSO, audit logs, and protected branches across many repos.

## Resolution Path 2: Re-authenticate `gh` as `afanogroup`

1. `gh auth logout --hostname github.com`
2. `gh auth login` — choose GitHub.com, HTTPS, paste-token or browser flow as `afanogroup`.
3. Confirm: `gh auth status` shows `Logged in to github.com account afanogroup`.
4. Then run the repo-creation block at the bottom of this file.

Simpler short-term, but you lose multi-admin governance and team-based permissions. Not recommended if you want a real multinational footprint.

## Resolution Path 3: Create under `officialprofab` and transfer

1. Run the repo-creation block below using your current auth.
2. After Path 1 is done, transfer each repo: `gh repo transfer officialprofab/<repo> afanogroup`

Useful if you want to push code today and resolve the org question this week.

---

## Repo plan (run AFTER one of the paths above is complete)

```bash
# Adjust OWNER to either afanogroup (after Path 1 or 2) or officialprofab (Path 3).
OWNER=afanogroup

# Repositories to create:
gh repo create $OWNER/afano-meta --public  --description "AFANO Group Holdings — public org profile, security policy, conglomerate diagram"
gh repo create $OWNER/afano-strategy-docs --private --description "Strategy, governance, brand, and phased deliverables (DOCX/XLSX)"
gh repo create $OWNER/afano-brand --public --description "Brand identity — Grand Seal, Network Emblem, Network Node, divisional sigils (SVG masters)"
gh repo create $OWNER/afano-ui --public --description "Shared @afano/ui React component library and design tokens"
gh repo create $OWNER/afano-holdings-web --public --description "afanogroup.com — Next.js 16 master holdings site"

# Per-division web repos (one per SBG):
gh repo create $OWNER/afano-financial-web    --public --description "Financial Services Group — independent operating brand site"
gh repo create $OWNER/afano-energy-web       --public --description "Energy & Natural Resources Group site"
gh repo create $OWNER/afano-technology-web   --public --description "Technology & Digital Innovation Group site"
gh repo create $OWNER/afano-infrastructure-web --public --description "Infrastructure, Real Estate & Development Group site"
gh repo create $OWNER/afano-agriculture-web  --public --description "Agriculture & Agribusiness Group site"
gh repo create $OWNER/afano-healthcare-web   --public --description "Healthcare & Life Sciences Group site"
gh repo create $OWNER/afano-mobility-web     --public --description "Tourism, Hospitality & Mobility Group site"
gh repo create $OWNER/afano-education-web    --public --description "Education, Training & Workforce Development Group site"
gh repo create $OWNER/afano-media-web        --public --description "Media, Communications & Entertainment Group site"
gh repo create $OWNER/afano-trade-web        --public --description "Trade, Commerce & Consumer Services Group site"
gh repo create $OWNER/afano-defense-web      --public --description "Government, Defense & National Security Group site"
gh repo create $OWNER/afano-industrial-web   --public --description "Industrial Manufacturing & Supply Chain Group site"
gh repo create $OWNER/afano-professional-web --public --description "Professional & Business Services Group site"
gh repo create $OWNER/afano-impact-web       --public --description "Social Impact & International Development Group site"
gh repo create $OWNER/afano-sports-web       --public --description "Sports, Recreation & Youth Development Group site"
```

## Pushing local content

The local working tree at `C:\Users\adupe\Desktop\AFANO\` maps to repos as follows:

| Local folder | Repo |
|---|---|
| `00_Strategy/`, `01_Branding-Domains/`, `03_-06_*` | `afano-strategy-docs` (private) |
| `02_Visual-Identity/` | `afano-brand` |
| `websites/holdings/` | `afano-holdings-web` |
| `websites/divisions/<slug>/` | `afano-<slug>-web` |

To push the holdings site after repo creation:
```bash
cd websites/holdings
git init -b main
git add .
git commit -m "Initial commit — afanogroup.com master holdings site"
git remote add origin git@github.com:$OWNER/afano-holdings-web.git
git push -u origin main
```

Repeat per division scaffold.
