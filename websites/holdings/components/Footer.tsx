import Link from "next/link";

export function Footer() {
  return (
    <footer className="bg-navy text-ivory/80 mt-24">
      <div className="max-w-7xl mx-auto px-6 py-14 grid md:grid-cols-4 gap-10 text-sm">
        <div>
          <div className="font-display text-ivory text-xl tracking-widest">AFANO</div>
          <div className="text-xs text-gold tracking-[0.3em] mt-1">GROUP HOLDINGS</div>
          <p className="mt-5 text-ivory/70 leading-relaxed">A multinational holding company stewarding 15 Strategic Business Groups across finance, energy, technology, infrastructure, and beyond.</p>
        </div>
        <div>
          <div className="text-gold uppercase text-xs tracking-widest mb-4">The Group</div>
          <ul className="space-y-2">
            <li><Link href="/about" className="hover:text-gold">About</Link></li>
            <li><Link href="/divisions" className="hover:text-gold">Divisions</Link></li>
            <li><Link href="/leadership" className="hover:text-gold">Leadership</Link></li>
            <li><Link href="/news" className="hover:text-gold">News</Link></li>
          </ul>
        </div>
        <div>
          <div className="text-gold uppercase text-xs tracking-widest mb-4">Investors</div>
          <ul className="space-y-2">
            <li><Link href="/investors" className="hover:text-gold">Investor Relations</Link></li>
            <li><Link href="/investors/governance" className="hover:text-gold">Governance</Link></li>
            <li><Link href="/investors/esg" className="hover:text-gold">ESG</Link></li>
            <li><Link href="/sustainability" className="hover:text-gold">Sustainability</Link></li>
          </ul>
        </div>
        <div>
          <div className="text-gold uppercase text-xs tracking-widest mb-4">Engage</div>
          <ul className="space-y-2">
            <li><Link href="/careers" className="hover:text-gold">Careers</Link></li>
            <li><Link href="/contact" className="hover:text-gold">Contact</Link></li>
            <li><Link href="/legal" className="hover:text-gold">Legal & Disclosures</Link></li>
          </ul>
        </div>
      </div>
      <div className="border-t border-ivory/10">
        <div className="max-w-7xl mx-auto px-6 py-5 text-xs text-ivory/50 flex flex-wrap justify-between gap-3">
          <div>© {new Date().getFullYear()} AFANO Group Holdings, Inc. All rights reserved.</div>
          <div>afanogroup.com  ·  Delaware C-Corporation</div>
        </div>
      </div>
    </footer>
  );
}
