import { EndorsementFooter } from "@/components/EndorsementFooter";

export default function Home() {
  return (
    <>
      <header className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-6 flex items-center justify-between">
          <div className="font-display text-2xl tracking-wide">AFANO Tourism, Hospitality & Mobility Group</div>
          <nav className="hidden md:flex gap-6 text-sm">
            <a href="#about" className="text-white/85 hover:text-white">About</a>
            <a href="#units" className="text-white/85 hover:text-white">Business Units</a>
            <a href="#contact" className="text-white/85 hover:text-white">Contact</a>
          </nav>
        </div>
      </header>

      <section id="hero" className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-24">
          <div className="text-xs tracking-[0.4em] uppercase opacity-80">AFANO SBG 7</div>
          <h1 className="font-display text-5xl md:text-6xl mt-4 max-w-3xl leading-[1.05]">AFANO Tourism, Hospitality & Mobility Group</h1>
          <p className="mt-6 max-w-2xl text-white/90 text-lg leading-relaxed">Tourism, hospitality, travel, mobility, automotive, aviation and maritime.</p>
        </div>
      </section>

      <section id="units" className="max-w-6xl mx-auto px-6 py-20">
        <div className="text-xs text-brand tracking-[0.4em] uppercase">Operating Subsidiaries</div>
        <h2 className="font-display text-3xl text-afano-navy mt-3">Business Units</h2>
        <div className="mt-10 grid md:grid-cols-2 gap-6">
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Tourism</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Tourism Camps: Eco-Tourism, Adventure</li>
            <li>· Destination Management: Planning, Marketing</li>
            <li>· Tour Operations: Guided Tours, Cultural Tours</li>
            <li>· Cultural Tourism: Heritage Programs, Cultural Events</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Hospitality</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Hotels & Resorts: Business, Luxury, Beach, Eco</li>
            <li>· Event & Conference Centers: Conventions, Corporate Events, Weddings, Exhibitions</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Travel Services</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Travel Agency: Flight, Hotel Booking</li>
            <li>· Corporate Travel: Business Travel Management, Executive Travel</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Mobility</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Vehicle Rentals: Daily Rentals, Fleet Leasing</li>
            <li>· Transportation: Shuttle, Corporate Transportation</li>
            <li>· Ride-Hailing & Last-Mile Mobility (NEW)</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Automotive</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Vehicle Sales: New, Used</li>
            <li>· Auto Repair: Maintenance, Diagnostics</li>
            <li>· Auto Finance & Insurance (NEW)</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Aviation (NEW)</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Charter & Executive Aviation</li>
            <li>· MRO (Maintenance, Repair, Overhaul)</li>
            <li>· Ground Handling & Airport Services</li>
            <li>· Cargo Aviation</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Maritime & Ports (NEW)</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Shipping & Freight Forwarding</li>
            <li>· Port Operations & Terminals</li>
            <li>· Coastal & Inland Waterways Logistics</li>
            <li>· Marine Services</li>
          </ul>
        </div>
        </div>
      </section>

      <section id="about" className="border-t border-mist bg-ivory">
        <div className="max-w-3xl mx-auto px-6 py-16">
          <h2 className="font-display text-3xl text-afano-navy">About this Division</h2>
          <p className="mt-4 text-ink/75 leading-relaxed">AFANO Tourism, Hospitality & Mobility Group is a Strategic Business Group of AFANO Group Holdings — operated as a wholly-owned intermediate holding entity. Each Business Unit is separately incorporated and trades under its own independent brand and domain.</p>
        </div>
      </section>

      <section id="contact" className="max-w-3xl mx-auto px-6 py-16">
        <h2 className="font-display text-3xl text-afano-navy">Contact</h2>
        <p className="mt-4 text-ink/75">Reach this division at <a className="text-brand underline" href="mailto:hello@travel.afanogroup.com">hello@travel.afanogroup.com</a>. For Group-level inquiries, visit <a className="text-brand underline" href="https://afanogroup.com">afanogroup.com</a>.</p>
      </section>

      <EndorsementFooter />
    </>
  );
}
