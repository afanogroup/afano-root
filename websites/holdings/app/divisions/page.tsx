import { DIVISIONS } from "@/lib/divisions";
import { DivisionCard } from "@/components/DivisionCard";

export const metadata = { title: "Divisions" };

export default function DivisionsIndex() {
  return (
    <section className="max-w-7xl mx-auto px-6 py-20">
      <div className="text-xs text-gold tracking-[0.4em] uppercase">Portfolio</div>
      <h1 className="font-display text-5xl text-navy mt-3">The 15 Strategic Business Groups</h1>
      <p className="mt-4 max-w-2xl text-ink/70 leading-relaxed">
        Each SBG operates as a wholly-owned intermediate holding entity. Its business units carry
        independent brands and domains — see each division page for the operating subsidiaries.
      </p>
      <div className="mt-12 grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {DIVISIONS.map((d) => <DivisionCard key={d.num} d={d} />)}
      </div>
    </section>
  );
}
