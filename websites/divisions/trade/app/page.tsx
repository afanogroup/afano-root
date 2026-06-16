import { EndorsementFooter } from "@/components/EndorsementFooter";

export default function Home() {
  return (
    <>
      <header className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-6 flex items-center justify-between">
          <div className="font-display text-2xl tracking-wide">AFANO Trade, Commerce & Consumer Services Group</div>
          <nav className="hidden md:flex gap-6 text-sm">
            <a href="#about" className="text-white/85 hover:text-white">About</a>
            <a href="#units" className="text-white/85 hover:text-white">Business Units</a>
            <a href="#contact" className="text-white/85 hover:text-white">Contact</a>
          </nav>
        </div>
      </header>

      <section id="hero" className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-24">
          <div className="text-xs tracking-[0.4em] uppercase opacity-80">AFANO SBG 10</div>
          <h1 className="font-display text-5xl md:text-6xl mt-4 max-w-3xl leading-[1.05]">AFANO Trade, Commerce & Consumer Services Group</h1>
          <p className="mt-6 max-w-2xl text-white/90 text-lg leading-relaxed">International trade, distribution, e-commerce, retail and procurement.</p>
        </div>
      </section>

      <section id="units" className="max-w-6xl mx-auto px-6 py-20">
        <div className="text-xs text-brand tracking-[0.4em] uppercase">Operating Subsidiaries</div>
        <h2 className="font-display text-3xl text-afano-navy mt-3">Business Units</h2>
        <div className="mt-10 grid md:grid-cols-2 gap-6">
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">International Trade</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Import Services</li>
            <li>· Export Services</li>
            <li>· Trade Facilitation</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Distribution</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Wholesale Distribution</li>
            <li>· Supply Chain Distribution</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">E-Commerce</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Online Marketplace</li>
            <li>· Digital Commerce Platforms</li>
            <li>· Cross-Border E-Commerce (NEW)</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Retail</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Consumer Retail</li>
            <li>· Franchise Operations</li>
            <li>· Department Stores & Specialty Retail (NEW)</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Procurement & Sourcing</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Strategic Sourcing</li>
            <li>· Vendor Management</li>
            <li>· Contract Management</li>
            <li>· Global Procurement</li>
          </ul>
        </div>
        </div>
      </section>

      <section id="about" className="border-t border-mist bg-ivory">
        <div className="max-w-3xl mx-auto px-6 py-16">
          <h2 className="font-display text-3xl text-afano-navy">About this Division</h2>
          <p className="mt-4 text-ink/75 leading-relaxed">AFANO Trade, Commerce & Consumer Services Group is a Strategic Business Group of AFANO Group Holdings — operated as a wholly-owned intermediate holding entity. Each Business Unit is separately incorporated and trades under its own independent brand and domain.</p>
        </div>
      </section>

      <section id="contact" className="max-w-3xl mx-auto px-6 py-16">
        <h2 className="font-display text-3xl text-afano-navy">Contact</h2>
        <p className="mt-4 text-ink/75">Reach this division at <a className="text-brand underline" href="mailto:hello@trade.afanogroup.com">hello@trade.afanogroup.com</a>. For Group-level inquiries, visit <a className="text-brand underline" href="https://afanogroup.com">afanogroup.com</a>.</p>
      </section>

      <EndorsementFooter />
    </>
  );
}
