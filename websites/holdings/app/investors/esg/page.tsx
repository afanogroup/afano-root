import { PageHero } from "@/components/PageHero";

export const metadata = { title: "ESG & Sustainability" };

export default function ESG() {
  return (
    <>
      <PageHero eyebrow="ESG" title="Net zero by 2050. Aligned by design."
        lead="GRI Universal Standards, SASB sector standards, TCFD climate disclosures, and CDP — built into the operating cadence, not bolted on." />
      <section className="max-w-3xl mx-auto px-6 py-16 space-y-8">
        <p className="text-lg text-ink/75 leading-relaxed">
          AFANO Group Holdings commits to net-zero Scope 1+2 emissions by 2045 and Scope 3 by 2050, with
          science-based targets validated under the SBTi framework. The Chief Sustainability Officer reports
          to the CEO and to the Nominating & ESG Committee.
        </p>
        {[
          ["Climate", "Baseline Scope 1+2+3 inventory in Year 1; 30% reduction in Scope 1+2 intensity by Year 5; >70% renewable energy in operations by Year 10."],
          ["Social & Human Rights", "Aligned with the UN Guiding Principles. Annual human-rights due diligence across Tier-1 and material Tier-2 suppliers."],
          ["Governance", "ESG-linked compensation represents 15% of long-term incentive for the CEO and named officers."],
        ].map(([t, b]) => (
          <div key={t}>
            <h2 className="font-display text-2xl text-navy">{t}</h2>
            <p className="mt-2 text-ink/75 leading-relaxed">{b}</p>
          </div>
        ))}
      </section>
    </>
  );
}
