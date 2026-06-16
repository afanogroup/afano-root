import { PageHero } from "@/components/PageHero";

export const metadata = { title: "Governance" };

export default function Governance() {
  const items = [
    ["Board Composition", "7-15 directors with at least one-third independent. Independent Lead Director if Chair is non-independent."],
    ["Committees", "Audit, Risk, Nominating & ESG, Compensation, Investment — each with independent chair where required."],
    ["Code of Conduct", "Anti-bribery, sanctions, human rights, data protection — applies to every director, officer, employee and partner."],
    ["Related-Party Transactions", "Tiered approval: Audit Committee for material, full Board for significant, independent fairness opinion above thresholds."],
    ["Whistleblower Protection", "Independent confidential hotline operated by an external provider in every operating language."],
  ];
  return (
    <>
      <PageHero eyebrow="Investor Relations" title="Governance"
        lead="The Group's governance framework is built for a multinational portfolio — disciplined, transparent, and aligned with global listing standards." />
      <section className="max-w-3xl mx-auto px-6 py-16 space-y-8">
        {items.map(([t, b]) => (
          <div key={t}>
            <h2 className="font-display text-2xl text-navy">{t}</h2>
            <p className="mt-2 text-ink/75 leading-relaxed">{b}</p>
          </div>
        ))}
      </section>
    </>
  );
}
