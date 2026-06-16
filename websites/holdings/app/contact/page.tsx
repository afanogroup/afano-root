import { PageHero } from "@/components/PageHero";

export const metadata = { title: "Contact" };

export default function Contact() {
  const channels = [
    ["Investor Relations", "ir@afanogroup.com"],
    ["Media & Press", "press@afanogroup.com"],
    ["Corporate Development", "corpdev@afanogroup.com"],
    ["General Counsel", "legal@afanogroup.com"],
    ["Brand Stewardship", "brand@afanogroup.com"],
    ["Group Sustainability", "esg@afanogroup.com"],
  ];
  return (
    <>
      <PageHero eyebrow="Contact" title="Reach the Holdings Office"
        lead="For commercial inquiries with a specific division, please use the subsidiary's own contact channels." />
      <section className="max-w-3xl mx-auto px-6 py-16 grid sm:grid-cols-2 gap-6">
        {channels.map(([t, e]) => (
          <div key={t} className="border border-mist p-6 bg-white">
            <div className="text-xs uppercase tracking-widest text-gold">{t}</div>
            <a href={`mailto:${e}`} className="font-display text-lg text-navy block mt-2 no-underline hover:text-gold">{e}</a>
          </div>
        ))}
      </section>
    </>
  );
}
