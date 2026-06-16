import { EndorsementFooter } from "@/components/EndorsementFooter";

export default function Home() {
  return (
    <>
      <header className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-6 flex items-center justify-between">
          <div className="font-display text-2xl tracking-wide">AFANO Energy & Natural Resources Group</div>
          <nav className="hidden md:flex gap-6 text-sm">
            <a href="#about" className="text-white/85 hover:text-white">About</a>
            <a href="#units" className="text-white/85 hover:text-white">Business Units</a>
            <a href="#contact" className="text-white/85 hover:text-white">Contact</a>
          </nav>
        </div>
      </header>

      <section id="hero" className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-24">
          <div className="text-xs tracking-[0.4em] uppercase opacity-80">AFANO SBG 2</div>
          <h1 className="font-display text-5xl md:text-6xl mt-4 max-w-3xl leading-[1.05]">AFANO Energy & Natural Resources Group</h1>
          <p className="mt-6 max-w-2xl text-white/90 text-lg leading-relaxed">Renewable generation, power utilities, oil and gas, mining and resource trading.</p>
        </div>
      </section>

      <section id="units" className="max-w-6xl mx-auto px-6 py-20">
        <div className="text-xs text-brand tracking-[0.4em] uppercase">Operating Subsidiaries</div>
        <h2 className="font-display text-3xl text-afano-navy mt-3">Business Units</h2>
        <div className="mt-10 grid md:grid-cols-2 gap-6">
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Renewable Energy</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Solar Energy: Utility-Scale PV, Rooftop Solar, Off-Grid Solar</li>
            <li>· Wind & Hybrid Systems: Onshore Wind, Hybrid Solar-Wind, Microgrids</li>
            <li>· Hydrogen & Clean Fuels: Green Hydrogen Production, Fuel Cell Technology</li>
            <li>· Carbon Credits & Emissions Trading: Voluntary Carbon Markets, Offsets</li>
            <li>· Energy Storage: Battery Systems, Grid-Scale Storage Solutions</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Power & Utilities</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Power Generation: Utility-Scale, Independent Power Production, Gas Peakers</li>
            <li>· Power Distribution: Grid Infrastructure, Rural Electrification, Smart Metering</li>
            <li>· Water & Sanitation Utilities: Water Treatment, Distribution, Wastewater</li>
            <li>· District Heating & Cooling Systems</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Mining & Natural Resources</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Mining Operations: Exploration, Extraction, Processing</li>
            <li>· Mineral Trading: Cobalt, Lithium, Gold, Manganese</li>
            <li>· Resource Development: Artisanal Mining Formalisation, Community Mining</li>
            <li>· Critical Minerals for Battery & EV Supply Chains</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Oil, Gas & Petrochemicals</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Upstream Exploration & Production</li>
            <li>· Midstream Storage, Transportation & Pipeline</li>
            <li>· Downstream Refining & Petrochemicals</li>
            <li>· LNG Trading & Gas Distribution</li>
            <li>· Trading & Marketing</li>
          </ul>
        </div>
        </div>
      </section>

      <section id="about" className="border-t border-mist bg-ivory">
        <div className="max-w-3xl mx-auto px-6 py-16">
          <h2 className="font-display text-3xl text-afano-navy">About this Division</h2>
          <p className="mt-4 text-ink/75 leading-relaxed">AFANO Energy & Natural Resources Group is a Strategic Business Group of AFANO Group Holdings — operated as a wholly-owned intermediate holding entity. Each Business Unit is separately incorporated and trades under its own independent brand and domain.</p>
        </div>
      </section>

      <section id="contact" className="max-w-3xl mx-auto px-6 py-16">
        <h2 className="font-display text-3xl text-afano-navy">Contact</h2>
        <p className="mt-4 text-ink/75">Reach this division at <a className="text-brand underline" href="mailto:hello@energy.afanogroup.com">hello@energy.afanogroup.com</a>. For Group-level inquiries, visit <a className="text-brand underline" href="https://afanogroup.com">afanogroup.com</a>.</p>
      </section>

      <EndorsementFooter />
    </>
  );
}
