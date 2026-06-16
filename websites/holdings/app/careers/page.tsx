import { PageHero } from "@/components/PageHero";

export const metadata = { title: "Careers" };

export default function Careers() {
  return (
    <>
      <PageHero eyebrow="Join the Group" title="Careers"
        lead="Each operating subsidiary recruits independently for its own talent needs. The Holdings Office recruits for the corporate centre — finance, legal, IR, ESG, brand, and corporate development." />
      <section className="max-w-3xl mx-auto px-6 py-16 space-y-6 text-ink/75 leading-relaxed">
        <p>The Group is a House of Brands. Most opportunities live with the operating
          subsidiaries — please use the divisional sites to find roles in finance,
          energy, technology, healthcare, infrastructure, and beyond.</p>
        <p>For Holdings Office roles, contact <a className="text-navy underline hover:text-gold" href="mailto:careers@afanogroup.com">careers@afanogroup.com</a>.</p>
      </section>
    </>
  );
}
