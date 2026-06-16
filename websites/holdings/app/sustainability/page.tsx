import { PageHero } from "@/components/PageHero";

export const metadata = { title: "Sustainability" };

export default function Sustainability() {
  return (
    <>
      <PageHero eyebrow="Sustainability" title="Built for the energy transition"
        lead="Aligned with the Paris Agreement, the UN Sustainable Development Goals, and the science-based targets framework." />
      <section className="max-w-3xl mx-auto px-6 py-16 space-y-6 text-ink/75 leading-relaxed">
        <p>The Group's sustainability program operates across all 15 SBGs, with materiality
          assessment refreshed annually against SASB sector standards. Climate, biodiversity,
          water, human rights, and community impact are tracked under a single Group-level
          framework.</p>
        <p>The full report is published on the <a className="text-navy underline hover:text-gold" href="/investors/esg">Investor Relations ESG page</a>.</p>
      </section>
    </>
  );
}
