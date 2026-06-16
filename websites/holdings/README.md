# afano-holdings-web

Master Next.js 16 App Router site for **afanogroup.com**.

## Stack
- Next.js 16 (App Router, Fluid Compute on Vercel)
- React 19, TypeScript strict
- Tailwind CSS v4 (PostCSS plugin)
- Brand tokens mirrored from `02_Visual-Identity/colors.json`

## Run
```bash
npm install
npm run dev
# http://localhost:3000
```

## Deploy
```bash
npm i -g vercel
vercel link
vercel deploy --prod
```

## Information architecture
- `/` — Hero, 15-division grid, House of Brands note
- `/about`, `/leadership`, `/news`, `/careers`, `/contact`, `/sustainability`, `/legal`
- `/divisions`, `/divisions/[slug]` — one page per SBG (15 routes statically generated)
- `/investors`, `/investors/governance`, `/investors/esg`

## Data
`lib/divisions.ts` mirrors `scripts/afano_data.py`. Keep them in sync — the Python module is the source of truth for the docx generators; this TS file is the source of truth for the site.
