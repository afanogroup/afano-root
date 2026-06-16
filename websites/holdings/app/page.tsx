import { DIVISIONS } from "@/lib/divisions";
import { DivisionCard } from "@/components/DivisionCard";
import { NetworkEmblem } from "@/components/NetworkEmblem";

export default function Home() {
  return (
    <>
      {/* Hero */}
      <section className="bg-navy text-ivory">
        <div className="max-w-7xl mx-auto px-6 py-24 md:py-32 grid md:grid-cols-2 gap-12 items-center">
          <div>
            <div className="text-xs text-gold tracking-[0.4em] uppercase">A Multinational Conglomerate</div>
            <h1 className="font-display text-5xl md:text-6xl leading-[1.05] mt-6">
              Capital. Brands. Continents.
            </h1>
            <p className="mt-6 text-lg text-ivory/80 leading-relaxed max-w-xl">
              AFANO Group Holdings is a diversified holding company stewarding 15 Strategic Business Groups —
              from financial services and energy to healthcare, infrastructure, and aerospace — across Africa,
              the Middle East, Europe, North America, and Asia-Pacific.
            </p>
            <div className="mt-10 flex gap-4">
              <a href="/divisions" className="bg-gold text-navy px-7 py-3 text-sm tracking-widest uppercase no-underline hover:bg-ivory transition">Explore Divisions</a>
              <a href="/investors" className="border border-ivory/30 text-ivory px-7 py-3 text-sm tracking-widest uppercase no-underline hover:border-gold hover:text-gold transition">Investors</a>
            </div>
          </div>
          <div className="flex justify-center">
            <NetworkEmblem size={380} />
          </div>
        </div>
      </section>

      {/* Pillars */}
      <section className="max-w-7xl mx-auto px-6 py-20 grid md:grid-cols-4 gap-10 border-b border-mist">
        {[
          { label: "Strategic Business Groups", value: "15" },
          { label: "Business Units", value: "60+" },
          { label: "Operating Jurisdictions", value: "12" },
          { label: "Architecture", value: "House of Brands" },
        ].map((s) => (
          <div key={s.label}>
            <div className="font-display text-4xl text-navy">{s.value}</div>
            <div className="text-xs uppercase tracking-widest text-ink/60 mt-2">{s.label}</div>
          </div>
        ))}
      </section>

      {/* Divisions grid */}
      <section className="max-w-7xl mx-auto px-6 py-20">
        <div className="flex items-end justify-between mb-12">
          <div>
            <div className="text-xs text-gold tracking-[0.4em] uppercase">Portfolio</div>
            <h2 className="font-display text-4xl text-navy mt-3">The 15 Strategic Business Groups</h2>
          </div>
          <a href="/divisions" className="text-sm text-navy hover:text-gold no-underline">View all →</a>
        </div>
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {DIVISIONS.map((d) => <DivisionCard key={d.num} d={d} />)}
        </div>
      </section>

      {/* Architecture note */}
      <section className="bg-ivory border-t border-mist">
        <div className="max-w-4xl mx-auto px-6 py-20 text-center">
          <div className="text-xs text-gold tracking-[0.4em] uppercase">House of Brands</div>
          <h2 className="font-display text-3xl text-navy mt-4">Independent brands. Shared discipline.</h2>
          <p className="mt-6 text-lg text-ink/70 leading-relaxed">
            Each operating subsidiary trades under its own brand and domain, free to be sold, spun off, or
            listed without rename risk. Capital, audit, treasury, and governance are centralized at Holdings —
            the keiretsu model adapted for a multinational portfolio.
          </p>
        </div>
      </section>
    </>
  );
}
