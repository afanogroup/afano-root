import Link from "next/link";
import type { Division } from "@/lib/divisions";

export function DivisionCard({ d }: { d: Division }) {
  return (
    <Link href={`/divisions/${d.slug}`} className="group block no-underline">
      <div className="relative overflow-hidden rounded-sm border border-mist bg-white hover:shadow-lg transition">
        <div className="h-2" style={{ background: d.color }} />
        <div className="p-6">
          <div className="text-xs tracking-[0.3em] uppercase" style={{ color: d.color }}>SBG {String(d.num).padStart(2, "0")}</div>
          <h3 className="font-display text-xl text-navy mt-2 leading-snug">{d.name}</h3>
          <p className="text-sm text-ink/70 mt-3 leading-relaxed line-clamp-3">{d.summary}</p>
          <div className="mt-5 text-xs text-ink/50 group-hover:text-gold transition">{d.businessUnits.length} business units →</div>
        </div>
      </div>
    </Link>
  );
}
