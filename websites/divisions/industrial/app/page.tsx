import { EndorsementFooter } from "@/components/EndorsementFooter";

export default function Home() {
  return (
    <>
      <header className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-6 flex items-center justify-between">
          <div className="font-display text-2xl tracking-wide">AFANO Industrial Manufacturing & Supply Chain Group</div>
          <nav className="hidden md:flex gap-6 text-sm">
            <a href="#about" className="text-white/85 hover:text-white">About</a>
            <a href="#units" className="text-white/85 hover:text-white">Business Units</a>
            <a href="#contact" className="text-white/85 hover:text-white">Contact</a>
          </nav>
        </div>
      </header>

      <section id="hero" className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-24">
          <div className="text-xs tracking-[0.4em] uppercase opacity-80">AFANO SBG 12</div>
          <h1 className="font-display text-5xl md:text-6xl mt-4 max-w-3xl leading-[1.05]">AFANO Industrial Manufacturing & Supply Chain Group</h1>
          <p className="mt-6 max-w-2xl text-white/90 text-lg leading-relaxed">Heavy industry, manufacturing, industrial processing and supply chain operations.</p>
        </div>
      </section>

      <section id="units" className="max-w-6xl mx-auto px-6 py-20">
        <div className="text-xs text-brand tracking-[0.4em] uppercase">Operating Subsidiaries</div>
        <h2 className="font-display text-3xl text-afano-navy mt-3">Business Units</h2>
        <div className="mt-10 grid md:grid-cols-2 gap-6">
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Manufacturing</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Construction Materials: Cement, Steel, Iron Rods, Roofing, Tiles</li>
            <li>· Consumer Goods Manufacturing: Household, Personal Care</li>
            <li>· Industrial Equipment Manufacturing: Pumps, Compressors, Generators</li>
            <li>· 3D Printing & Additive Manufacturing</li>
            <li>· Packaging Manufacturing: Flexible, Rigid, Sustainable</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Industrial Processing & Chemicals</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Material Processing: Steel Fabrication, Aluminium Rolling</li>
            <li>· Specialty Chemicals & Plastics Manufacturing</li>
            <li>· Fertiliser Production & Agrochemicals</li>
            <li>· Robotics Integration & Smart Factory Automation</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Supply Chain & Logistics</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Freight & Intermodal Logistics</li>
            <li>· Warehousing: Distribution Centres, Bonded Stores</li>
            <li>· Inventory Management & Demand Planning</li>
            <li>· Fleet Management & Transport Operations</li>
            <li>· 3PL & 4PL Logistics Services</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Textiles & Apparel</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Cotton Ginning, Spinning & Weaving</li>
            <li>· Garment Manufacturing & CMT (Cut, Make, Trim)</li>
            <li>· Branded Apparel & Retail Fashion Labels</li>
            <li>· Technical Textiles: Protective, Industrial, Medical</li>
          </ul>
        </div>
        </div>
      </section>

      <section id="about" className="border-t border-mist bg-ivory">
        <div className="max-w-3xl mx-auto px-6 py-16">
          <h2 className="font-display text-3xl text-afano-navy">About this Division</h2>
          <p className="mt-4 text-ink/75 leading-relaxed">AFANO Industrial Manufacturing & Supply Chain Group is a Strategic Business Group of AFANO Group Holdings — operated as a wholly-owned intermediate holding entity. Each Business Unit is separately incorporated and trades under its own independent brand and domain.</p>
        </div>
      </section>

      <section id="contact" className="max-w-3xl mx-auto px-6 py-16">
        <h2 className="font-display text-3xl text-afano-navy">Contact</h2>
        <p className="mt-4 text-ink/75">Reach this division at <a className="text-brand underline" href="mailto:hello@industry.afanogroup.com">hello@industry.afanogroup.com</a>. For Group-level inquiries, visit <a className="text-brand underline" href="https://afanogroup.com">afanogroup.com</a>.</p>
      </section>

      <EndorsementFooter />
    </>
  );
}
