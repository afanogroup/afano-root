import Link from "next/link";
import { PageHero } from "@/components/PageHero";

export const metadata = { title: "Investors" };

export default function Investors() {
  const tiles = [
    { href: "/investors/governance", title: "Governance", body: "Board charter, committee charters, code of conduct." },
    { href: "/investors/esg", title: "ESG & Sustainability", body: "GRI, SASB, TCFD-aligned reporting; net-zero pathway." },
    { href: "/news", title: "News & Press", body: "Press releases and corporate updates." },
    { href: "/contact", title: "IR Contact", body: "Reach the Investor Relations function." },
  ];
  return (
    <>
      <PageHero eyebrow="Investor Relations" title="Capital. Stewardship. Long-term value."
        lead="The IR function is the Group's single voice to the capital markets — covering financial reporting, governance, ESG, and sovereign-investor engagement." />
      <section className="max-w-7xl mx-auto px-6 py-16 grid sm:grid-cols-2 gap-6">
        {tiles.map(t => (
          <Link key={t.href} href={t.href as never} className="block no-underline border border-mist p-8 bg-white hover:shadow-lg transition">
            <h2 className="font-display text-2xl text-navy">{t.title}</h2>
            <p className="mt-3 text-ink/70">{t.body}</p>
          </Link>
        ))}
      </section>
    </>
  );
}
