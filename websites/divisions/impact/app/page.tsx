import { EndorsementFooter } from "@/components/EndorsementFooter";

export default function Home() {
  return (
    <>
      <header className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-6 flex items-center justify-between">
          <div className="font-display text-2xl tracking-wide">AFANO Social Impact & International Development Group</div>
          <nav className="hidden md:flex gap-6 text-sm">
            <a href="#about" className="text-white/85 hover:text-white">About</a>
            <a href="#units" className="text-white/85 hover:text-white">Business Units</a>
            <a href="#contact" className="text-white/85 hover:text-white">Contact</a>
          </nav>
        </div>
      </header>

      <section id="hero" className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-24">
          <div className="text-xs tracking-[0.4em] uppercase opacity-80">AFANO SBG 14</div>
          <h1 className="font-display text-5xl md:text-6xl mt-4 max-w-3xl leading-[1.05]">AFANO Social Impact & International Development Group</h1>
          <p className="mt-6 max-w-2xl text-white/90 text-lg leading-relaxed">Development, community programs, foundation grants and policy research. Operated on a not-for-profit basis where applicable.</p>
        </div>
      </section>

      <section id="units" className="max-w-6xl mx-auto px-6 py-20">
        <div className="text-xs text-brand tracking-[0.4em] uppercase">Operating Subsidiaries</div>
        <h2 className="font-display text-3xl text-afano-navy mt-3">Business Units</h2>
        <div className="mt-10 grid md:grid-cols-2 gap-6">
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">International Development</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Economic Development: Private Sector Development, Value Chain Strengthening</li>
            <li>· Institutional Strengthening: Capacity Building, Governance Reform</li>
            <li>· Donor-Funded Programs: USAID, UN, World Bank, African Development Bank</li>
            <li>· Climate Adaptation & Resilience Programs</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Community, Foundation & Grants</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Youth Programs: Mentorship, Leadership, Skills Development</li>
            <li>· Women Empowerment: Economic Inclusion, STEM for Girls</li>
            <li>· Scholarships, Grants & Charitable Giving</li>
            <li>· Community Infrastructure: Schools, Clinics, Water Points</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Research, Policy & Evaluation</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Policy Research & Advocacy</li>
            <li>· Monitoring & Evaluation (M&E): Impact Measurement, Logframes</li>
            <li>· Development Data & GIS Mapping</li>
            <li>· Think Tank & Knowledge Publications</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Humanitarian & Disaster Response</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Emergency Relief: Food, Water, Shelter, Non-Food Items</li>
            <li>· Refugee & Displacement Support</li>
            <li>· Resilience Programs: Livelihood Recovery, DRR</li>
            <li>· Health Emergency Response</li>
          </ul>
        </div>
        </div>
      </section>

      <section id="about" className="border-t border-mist bg-ivory">
        <div className="max-w-3xl mx-auto px-6 py-16">
          <h2 className="font-display text-3xl text-afano-navy">About this Division</h2>
          <p className="mt-4 text-ink/75 leading-relaxed">AFANO Social Impact & International Development Group is a Strategic Business Group of AFANO Group Holdings — operated as a wholly-owned intermediate holding entity. Each Business Unit is separately incorporated and trades under its own independent brand and domain.</p>
        </div>
      </section>

      <section id="contact" className="max-w-3xl mx-auto px-6 py-16">
        <h2 className="font-display text-3xl text-afano-navy">Contact</h2>
        <p className="mt-4 text-ink/75">Reach this division at <a className="text-brand underline" href="mailto:hello@impact.afanogroup.com">hello@impact.afanogroup.com</a>. For Group-level inquiries, visit <a className="text-brand underline" href="https://afanogroup.com">afanogroup.com</a>.</p>
      </section>

      <EndorsementFooter />
    </>
  );
}
