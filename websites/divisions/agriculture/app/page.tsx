import { EndorsementFooter } from "@/components/EndorsementFooter";

export default function Home() {
  return (
    <>
      <header className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-6 flex items-center justify-between">
          <div className="font-display text-2xl tracking-wide">AFANO Agriculture & Agribusiness Group</div>
          <nav className="hidden md:flex gap-6 text-sm">
            <a href="#about" className="text-white/85 hover:text-white">About</a>
            <a href="#units" className="text-white/85 hover:text-white">Business Units</a>
            <a href="#contact" className="text-white/85 hover:text-white">Contact</a>
          </nav>
        </div>
      </header>

      <section id="hero" className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-24">
          <div className="text-xs tracking-[0.4em] uppercase opacity-80">AFANO SBG 5</div>
          <h1 className="font-display text-5xl md:text-6xl mt-4 max-w-3xl leading-[1.05]">AFANO Agriculture & Agribusiness Group</h1>
          <p className="mt-6 max-w-2xl text-white/90 text-lg leading-relaxed">Production, processing, agritech and environmental services.</p>
        </div>
      </section>

      <section id="units" className="max-w-6xl mx-auto px-6 py-20">
        <div className="text-xs text-brand tracking-[0.4em] uppercase">Operating Subsidiaries</div>
        <h2 className="font-display text-3xl text-afano-navy mt-3">Business Units</h2>
        <div className="mt-10 grid md:grid-cols-2 gap-6">
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Agriculture Production</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Crop Farming: Staple Crops, Cash Crops, Greenhouse</li>
            <li>· Livestock: Poultry, Cattle, Dairy</li>
            <li>· Aquaculture: Fish Farming, Aquatic Processing</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Agribusiness</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Agricultural Consulting: Farm Management, Agritech Solutions</li>
            <li>· Commodity Trading: Cocoa, Agricultural Exports</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Food Processing</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Food Manufacturing: Beverages, Packaged Foods</li>
            <li>· Storage Services: Cold Storage, Commodity Storage</li>
            <li>· Consumer Products: Cocoa Products, Beverages, Mineral Drinks, Packaged Consumer Goods</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Environmental & Recycling Solutions</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Recycling: Plastic, Metal, Electronic Waste, Industrial Waste Processing</li>
            <li>· Circular Economy Programs</li>
          </ul>
        </div>
        </div>
      </section>

      <section id="about" className="border-t border-mist bg-ivory">
        <div className="max-w-3xl mx-auto px-6 py-16">
          <h2 className="font-display text-3xl text-afano-navy">About this Division</h2>
          <p className="mt-4 text-ink/75 leading-relaxed">AFANO Agriculture & Agribusiness Group is a Strategic Business Group of AFANO Group Holdings — operated as a wholly-owned intermediate holding entity. Each Business Unit is separately incorporated and trades under its own independent brand and domain.</p>
        </div>
      </section>

      <section id="contact" className="max-w-3xl mx-auto px-6 py-16">
        <h2 className="font-display text-3xl text-afano-navy">Contact</h2>
        <p className="mt-4 text-ink/75">Reach this division at <a className="text-brand underline" href="mailto:hello@agri.afanogroup.com">hello@agri.afanogroup.com</a>. For Group-level inquiries, visit <a className="text-brand underline" href="https://afanogroup.com">afanogroup.com</a>.</p>
      </section>

      <EndorsementFooter />
    </>
  );
}
