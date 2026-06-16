import { DIVISIONS } from "@/lib/divisions";
import { notFound } from "next/navigation";

export function generateStaticParams() {
  return DIVISIONS.map((d) => ({ slug: d.slug }));
}

export function generateMetadata({ params }: { params: { slug: string } }) {
  const d = DIVISIONS.find((x) => x.slug === params.slug);
  return { title: d?.name ?? "Division" };
}

export default function DivisionPage({ params }: { params: { slug: string } }) {
  const d = DIVISIONS.find((x) => x.slug === params.slug);
  if (!d) notFound();
  return (
    <>
      <section style={{ background: d.color }} className="text-ivory">
        <div className="max-w-7xl mx-auto px-6 py-20">
          <div className="text-xs tracking-[0.4em] uppercase opacity-80">SBG {String(d.num).padStart(2, "0")}</div>
          <h1 className="font-display text-5xl mt-3">{d.name}</h1>
          <p className="mt-5 max-w-3xl text-ivory/85 text-lg leading-relaxed">{d.summary}</p>
        </div>
      </section>

      <section className="max-w-7xl mx-auto px-6 py-20">
        <div className="text-xs text-gold tracking-[0.4em] uppercase">Operating Subsidiaries</div>
        <h2 className="font-display text-3xl text-navy mt-3">Business Units</h2>
        <div className="mt-10 grid md:grid-cols-2 gap-8">
          {d.businessUnits.map((bu) => (
            <div key={bu.name} className="border border-mist p-6 bg-white">
              <h3 className="font-display text-xl text-navy">{bu.name}</h3>
              <ul className="mt-4 space-y-2 text-sm text-ink/75">
                {bu.services.map((s) => (<li key={s}>· {s}</li>))}
              </ul>
            </div>
          ))}
        </div>
      </section>

      <section className="border-t border-mist bg-ivory">
        <div className="max-w-4xl mx-auto px-6 py-16 text-center">
          <div className="text-xs text-gold tracking-[0.4em] uppercase">Brand & Domain</div>
          <p className="mt-4 text-ink/70">
            Each business unit operates under an independent brand and domain — see the
            Brand & Domain Architecture for the current candidate list, RDAP availability, and
            primary picks.
          </p>
        </div>
      </section>
    </>
  );
}
