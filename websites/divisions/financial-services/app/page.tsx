import { EndorsementFooter } from "@/components/EndorsementFooter";

export default function Home() {
  return (
    <>
      <header className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-6 flex items-center justify-between">
          <div className="font-display text-2xl tracking-wide">AFANO Financial Services Group</div>
          <nav className="hidden md:flex gap-6 text-sm">
            <a href="#about" className="text-white/85 hover:text-white">About</a>
            <a href="#units" className="text-white/85 hover:text-white">Business Units</a>
            <a href="#contact" className="text-white/85 hover:text-white">Contact</a>
          </nav>
        </div>
      </header>

      <section id="hero" className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-24">
          <div className="text-xs tracking-[0.4em] uppercase opacity-80">AFANO SBG 1</div>
          <h1 className="font-display text-5xl md:text-6xl mt-4 max-w-3xl leading-[1.05]">AFANO Financial Services Group</h1>
          <p className="mt-6 max-w-2xl text-white/90 text-lg leading-relaxed">Wealth, capital, banking, insurance and FinTech across emerging and developed markets.</p>
        </div>
      </section>

      <section id="units" className="max-w-6xl mx-auto px-6 py-20">
        <div className="text-xs text-brand tracking-[0.4em] uppercase">Operating Subsidiaries</div>
        <h2 className="font-display text-3xl text-afano-navy mt-3">Business Units</h2>
        <div className="mt-10 grid md:grid-cols-2 gap-6">
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Wealth & Investment Management</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Wealth Management: Financial Planning, Retirement Planning, Estate Planning, Family Office Services</li>
            <li>· Investment Management: Portfolio Management, Equity, Fixed Income, Alternatives</li>
            <li>· Asset Management: Institutional, Private, Fund Management, Investment Research</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Capital & Development Finance</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Project Finance: Infrastructure, Energy, Public-Private Partnership</li>
            <li>· Development Finance: SME Financing, Development Programs, Economic Growth Initiatives</li>
            <li>· Capital Advisory: Capital Raising, M&A Advisory, Business Valuation</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Financial Services & FinTech</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Credit Services: Credit Repair, Credit Monitoring, Debt Management</li>
            <li>· FinTech Solutions: Digital Payments, Mobile Banking, Financial Technology Platforms</li>
            <li>· Live site: https://srv1736078.hstgr.cloud/</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Banking & Lending (NEW)</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Commercial Banking: Corporate Banking, Trade Finance, Cash Management</li>
            <li>· Consumer Banking & Microfinance</li>
            <li>· Islamic Finance & Shariah-Compliant Products</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Insurance & Reinsurance (NEW)</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Life & Health Insurance</li>
            <li>· Property & Casualty Insurance</li>
            <li>· Reinsurance & Captive Insurance Solutions</li>
            <li>· Bancassurance partnerships</li>
          </ul>
        </div>
        </div>
      </section>

      <section id="about" className="border-t border-mist bg-ivory">
        <div className="max-w-3xl mx-auto px-6 py-16">
          <h2 className="font-display text-3xl text-afano-navy">About this Division</h2>
          <p className="mt-4 text-ink/75 leading-relaxed">AFANO Financial Services Group is a Strategic Business Group of AFANO Group Holdings — operated as a wholly-owned intermediate holding entity. Each Business Unit is separately incorporated and trades under its own independent brand and domain.</p>
        </div>
      </section>

      <section id="contact" className="max-w-3xl mx-auto px-6 py-16">
        <h2 className="font-display text-3xl text-afano-navy">Contact</h2>
        <p className="mt-4 text-ink/75">Reach this division at <a className="text-brand underline" href="mailto:hello@capital.afanogroup.com">hello@capital.afanogroup.com</a>. For Group-level inquiries, visit <a className="text-brand underline" href="https://afanogroup.com">afanogroup.com</a>.</p>
      </section>

      <EndorsementFooter />
    </>
  );
}
