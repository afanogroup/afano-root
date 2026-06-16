import { PageHero } from "@/components/PageHero";

export const metadata = { title: "Legal & Disclosures" };

export default function Legal() {
  const items = [
    ["Corporate Information", "AFANO Group Holdings, Inc. is a Delaware C-Corporation. Operating subsidiaries are separately incorporated."],
    ["Brand Use Policy", "The AFANO master mark is reserved for the holding company. Subsidiary brand use is governed by the Brand Standards."],
    ["Forward-Looking Statements", "Statements on this site that are not historical facts are forward-looking and subject to risks and uncertainties."],
    ["Modern Slavery Statement", "The Group complies with the UK Modern Slavery Act and equivalent regimes; statement published annually."],
    ["Privacy", "The Group complies with GDPR, NDPR, CCPA, PDPA, POPIA, and LGPD; data subject requests can be made via privacy@afanogroup.com."],
    ["Cookies", "Strictly necessary cookies only; no third-party tracking on this site."],
  ];
  return (
    <>
      <PageHero eyebrow="Legal" title="Legal & Disclosures" />
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
