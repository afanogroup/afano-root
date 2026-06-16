"""Scaffold 15 Next.js division subdomain sites at websites/divisions/<slug>.

Each scaffold inherits a shared @afano/ui package layout but is self-contained
(small, focused) so each can be promoted to its own Vercel project and pointed
at an independent domain without code changes.
"""
from pathlib import Path
import json
import afano_data as A

ROOT = Path(__file__).parent.parent / "websites" / "divisions"
ROOT.mkdir(parents=True, exist_ok=True)

SLUGS = {
    1: "financial-services", 2: "energy", 3: "technology", 4: "infrastructure",
    5: "agriculture", 6: "healthcare", 7: "mobility", 8: "education",
    9: "media", 10: "trade", 11: "defense", 12: "industrial",
    13: "professional", 14: "impact", 15: "sports",
}


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def package_json(slug):
    return json.dumps({
        "name": f"afano-{slug}-web",
        "version": "1.0.0",
        "private": True,
        "scripts": {
            "dev": "next dev",
            "build": "next build",
            "start": "next start",
        },
        "dependencies": {
            "next": "^16.0.0",
            "react": "^19.0.0",
            "react-dom": "^19.0.0",
        },
        "devDependencies": {
            "typescript": "^5.6.0",
            "@types/node": "^22.0.0",
            "@types/react": "^19.0.0",
            "@types/react-dom": "^19.0.0",
            "tailwindcss": "^4.0.0",
            "@tailwindcss/postcss": "^4.0.0",
            "postcss": "^8.4.0",
        },
    }, indent=2)


TSCONFIG = '''{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [{ "name": "next" }],
    "paths": { "@/*": ["./*"] }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
'''

POSTCSS = '''export default { plugins: { "@tailwindcss/postcss": {} } };
'''

NEXTCONFIG = '''import type { NextConfig } from "next";
const nextConfig: NextConfig = {};
export default nextConfig;
'''

def globals_css(color):
    return f'''@import "tailwindcss";
@theme {{
  --color-brand: {color};
  --color-ivory: #F5F0E3;
  --color-ink: #0A0F1A;
  --color-mist: #D9DEE6;
  --color-afano-navy: #0B1F3A;
  --color-afano-gold: #C8A04A;
  --font-display: Georgia, serif;
  --font-sans: Inter, ui-sans-serif, system-ui, sans-serif;
}}
html {{ font-family: var(--font-sans); color: var(--color-ink); background: var(--color-ivory); }}
body {{ margin: 0; }}
.font-display {{ font-family: var(--font-display); }}
.bg-brand {{ background: var(--color-brand); }}
.text-brand {{ color: var(--color-brand); }}
.border-brand {{ border-color: var(--color-brand); }}
.bg-afano-navy {{ background: var(--color-afano-navy); }}
.text-afano-navy {{ color: var(--color-afano-navy); }}
.text-afano-gold {{ color: var(--color-afano-gold); }}
'''


def layout_tsx(name):
    return f'''import type {{ Metadata }} from "next";
import "./globals.css";

export const metadata: Metadata = {{
  title: {{ default: "{name}", template: "%s · {name}" }},
  description: "An independent operating subsidiary within AFANO Group Holdings.",
}};

export default function RootLayout({{ children }}: {{ children: React.ReactNode }}) {{
  return (
    <html lang="en">
      <body>{{children}}</body>
    </html>
  );
}}
'''


def endorsement_tsx():
    return '''export function EndorsementFooter() {
  return (
    <footer className="bg-afano-navy text-ivory mt-24">
      <div className="max-w-6xl mx-auto px-6 py-10 flex flex-col md:flex-row items-center justify-between gap-4">
        <div className="flex items-center gap-3 text-sm">
          <svg viewBox="0 0 40 40" width="28" height="28" xmlns="http://www.w3.org/2000/svg">
            <polygon points="20,4 35,12 35,28 20,36 5,28 5,12" fill="none" stroke="#C8A04A" strokeWidth="2" />
            <circle cx="20" cy="20" r="6" fill="#C8A04A" />
          </svg>
          <span className="tracking-[0.3em] uppercase text-xs text-afano-gold">An AFANO Group Company</span>
        </div>
        <a href="https://afanogroup.com" className="text-xs text-ivory/70 hover:text-afano-gold no-underline">afanogroup.com</a>
      </div>
    </footer>
  );
}
'''


def page_tsx(division):
    num, name, color, sub, glyph, summary, bus = division
    bu_blocks = "\n".join([
        f'''        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">{bu_name}</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
{chr(10).join([f'            <li>· {s}</li>' for s in services])}
          </ul>
        </div>'''
        for bu_name, services in bus
    ])
    return f'''import {{ EndorsementFooter }} from "@/components/EndorsementFooter";

export default function Home() {{
  return (
    <>
      <header className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-6 flex items-center justify-between">
          <div className="font-display text-2xl tracking-wide">{name}</div>
          <nav className="hidden md:flex gap-6 text-sm">
            <a href="#about" className="text-white/85 hover:text-white">About</a>
            <a href="#units" className="text-white/85 hover:text-white">Business Units</a>
            <a href="#contact" className="text-white/85 hover:text-white">Contact</a>
          </nav>
        </div>
      </header>

      <section id="hero" className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-24">
          <div className="text-xs tracking-[0.4em] uppercase opacity-80">AFANO SBG {num}</div>
          <h1 className="font-display text-5xl md:text-6xl mt-4 max-w-3xl leading-[1.05]">{name}</h1>
          <p className="mt-6 max-w-2xl text-white/90 text-lg leading-relaxed">{summary}</p>
        </div>
      </section>

      <section id="units" className="max-w-6xl mx-auto px-6 py-20">
        <div className="text-xs text-brand tracking-[0.4em] uppercase">Operating Subsidiaries</div>
        <h2 className="font-display text-3xl text-afano-navy mt-3">Business Units</h2>
        <div className="mt-10 grid md:grid-cols-2 gap-6">
{bu_blocks}
        </div>
      </section>

      <section id="about" className="border-t border-mist bg-ivory">
        <div className="max-w-3xl mx-auto px-6 py-16">
          <h2 className="font-display text-3xl text-afano-navy">About this Division</h2>
          <p className="mt-4 text-ink/75 leading-relaxed">{name} is a Strategic Business Group of AFANO Group Holdings — operated as a wholly-owned intermediate holding entity. Each Business Unit is separately incorporated and trades under its own independent brand and domain.</p>
        </div>
      </section>

      <section id="contact" className="max-w-3xl mx-auto px-6 py-16">
        <h2 className="font-display text-3xl text-afano-navy">Contact</h2>
        <p className="mt-4 text-ink/75">Reach this division at <a className="text-brand underline" href="mailto:hello@{sub}.afanogroup.com">hello@{sub}.afanogroup.com</a>. For Group-level inquiries, visit <a className="text-brand underline" href="https://afanogroup.com">afanogroup.com</a>.</p>
      </section>

      <EndorsementFooter />
    </>
  );
}}
'''


README = '''# afano-{slug}-web

Independent Next.js site for **{name}** (AFANO SBG {num}).

- Brand color: `{color}`
- Subdomain (working): `{sub}.afanogroup.com`
- Future independent domain: see `01_Branding-Domains/Domain-Architecture.xlsx`

## Run
```bash
npm install
npm run dev
```

## Independence
This scaffold can be promoted to its own Vercel project and pointed at an
independent domain without code change. The only AFANO-branded element is the
mandatory endorsement footer (`An AFANO Group Company`) which links back to
afanogroup.com — per Brand Guidelines section 6.
'''


def scaffold(division):
    num, name, color, sub, glyph, summary, bus = division
    slug = SLUGS[num]
    base = ROOT / slug
    write(base / "package.json", package_json(slug))
    write(base / "tsconfig.json", TSCONFIG)
    write(base / "postcss.config.mjs", POSTCSS)
    write(base / "next.config.ts", NEXTCONFIG)
    write(base / "app" / "globals.css", globals_css(color))
    write(base / "app" / "layout.tsx", layout_tsx(name))
    write(base / "app" / "page.tsx", page_tsx(division))
    write(base / "components" / "EndorsementFooter.tsx", endorsement_tsx())
    write(base / "README.md", README.format(slug=slug, name=name, num=num, color=color, sub=sub))
    print(f"SCAFFOLD  {base}  ({name})")


def main():
    for d in A.DIVISIONS:
        scaffold(d)
    # Root README for the divisions folder
    idx = "\n".join([f"- [{name}](./{SLUGS[num]}/) — SBG {num}  ·  {color}"
                     for num, name, color, *_ in A.DIVISIONS])
    (ROOT / "README.md").write_text(
        "# AFANO Division Subdomain Scaffolds\n\n"
        "15 independent Next.js scaffolds, one per SBG. Each is small, focused, and "
        "carries the mandatory 'An AFANO Group Company' endorsement footer per "
        "Brand Guidelines.\n\n" + idx + "\n",
        encoding="utf-8")
    print(f"WROTE {ROOT}/README.md")


if __name__ == "__main__":
    main()
