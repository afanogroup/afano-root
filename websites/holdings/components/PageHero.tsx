export function PageHero({ eyebrow, title, lead }: { eyebrow: string; title: string; lead?: string }) {
  return (
    <section className="bg-navy text-ivory">
      <div className="max-w-7xl mx-auto px-6 py-20">
        <div className="text-xs text-gold tracking-[0.4em] uppercase">{eyebrow}</div>
        <h1 className="font-display text-5xl mt-3">{title}</h1>
        {lead && <p className="mt-5 max-w-3xl text-ivory/85 text-lg leading-relaxed">{lead}</p>}
      </div>
    </section>
  );
}
