import { EndorsementFooter } from "@/components/EndorsementFooter";

export default function Home() {
  return (
    <>
      <header className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-6 flex items-center justify-between">
          <div className="font-display text-2xl tracking-wide">AFANO Professional & Business Services Group</div>
          <nav className="hidden md:flex gap-6 text-sm">
            <a href="#about" className="text-white/85 hover:text-white">About</a>
            <a href="#units" className="text-white/85 hover:text-white">Business Units</a>
            <a href="#contact" className="text-white/85 hover:text-white">Contact</a>
          </nav>
        </div>
      </header>

      <section id="hero" className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-24">
          <div className="text-xs tracking-[0.4em] uppercase opacity-80">AFANO SBG 13</div>
          <h1 className="font-display text-5xl md:text-6xl mt-4 max-w-3xl leading-[1.05]">AFANO Professional & Business Services Group</h1>
          <p className="mt-6 max-w-2xl text-white/90 text-lg leading-relaxed">Management consulting, project management, outsourcing, legal, accounting and professional services.</p>
        </div>
      </section>

      <section id="units" className="max-w-6xl mx-auto px-6 py-20">
        <div className="text-xs text-brand tracking-[0.4em] uppercase">Operating Subsidiaries</div>
        <h2 className="font-display text-3xl text-afano-navy mt-3">Business Units</h2>
        <div className="mt-10 grid md:grid-cols-2 gap-6">
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Strategy, Consulting & PMO</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Strategy Consulting: Corporate Strategy, Market Entry, Competitive Intelligence</li>
            <li>· Business Transformation & Change Management</li>
            <li>· PMO Services: Program Management, Portfolio Management</li>
            <li>· Governance, Risk & Compliance Advisory: ERM, Internal Controls, Audit Readiness</li>
            <li>· Organisational Development & HR Consulting</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Business Outsourcing & BPO</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Administrative Services & Secretarial Support</li>
            <li>· Back Office Operations: Finance, HR, Procurement</li>
            <li>· Customer Contact Centres: Multilingual, Omnichannel</li>
            <li>· Knowledge Process Outsourcing (KPO)</li>
            <li>· Robotic Process Automation as a Service</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Legal Services</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Corporate Law: M&A, Joint Ventures, Commercial Contracts</li>
            <li>· Intellectual Property: Patents, Trademarks, Licensing</li>
            <li>· Regulatory & Compliance Counsel</li>
            <li>· Cross-Border Transaction Counsel & Arbitration</li>
            <li>· Employment & Labour Law</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Accounting, Tax & Audit</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Tax Advisory: International Tax, Transfer Pricing, VAT</li>
            <li>· External Audit & Assurance</li>
            <li>· Forensic Accounting & Anti-Fraud Investigation</li>
            <li>· Financial Reporting: IFRS, US GAAP Conversion</li>
            <li>· Internal Audit Co-sourcing & Outsourcing</li>
          </ul>
        </div>
        </div>
      </section>

      <section id="about" className="border-t border-mist bg-ivory">
        <div className="max-w-3xl mx-auto px-6 py-16">
          <h2 className="font-display text-3xl text-afano-navy">About this Division</h2>
          <p className="mt-4 text-ink/75 leading-relaxed">AFANO Professional & Business Services Group is a Strategic Business Group of AFANO Group Holdings — operated as a wholly-owned intermediate holding entity. Each Business Unit is separately incorporated and trades under its own independent brand and domain.</p>
        </div>
      </section>

      <section id="contact" className="max-w-3xl mx-auto px-6 py-16">
        <h2 className="font-display text-3xl text-afano-navy">Contact</h2>
        <p className="mt-4 text-ink/75">Reach this division at <a className="text-brand underline" href="mailto:hello@business.afanogroup.com">hello@business.afanogroup.com</a>. For Group-level inquiries, visit <a className="text-brand underline" href="https://afanogroup.com">afanogroup.com</a>.</p>
      </section>

      <EndorsementFooter />
    </>
  );
}
