import { EndorsementFooter } from "@/components/EndorsementFooter";

export default function Home() {
  return (
    <>
      <header className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-6 flex items-center justify-between">
          <div className="font-display text-2xl tracking-wide">AFANO Technology & Digital Innovation Group</div>
          <nav className="hidden md:flex gap-6 text-sm">
            <a href="#about" className="text-white/85 hover:text-white">About</a>
            <a href="#units" className="text-white/85 hover:text-white">Business Units</a>
            <a href="#contact" className="text-white/85 hover:text-white">Contact</a>
          </nav>
        </div>
      </header>

      <section id="hero" className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-24">
          <div className="text-xs tracking-[0.4em] uppercase opacity-80">AFANO SBG 3</div>
          <h1 className="font-display text-5xl md:text-6xl mt-4 max-w-3xl leading-[1.05]">AFANO Technology & Digital Innovation Group</h1>
          <p className="mt-6 max-w-2xl text-white/90 text-lg leading-relaxed">Cybersecurity, cloud, software engineering, AI, digital transformation and telecommunications.</p>
        </div>
      </section>

      <section id="units" className="max-w-6xl mx-auto px-6 py-20">
        <div className="text-xs text-brand tracking-[0.4em] uppercase">Operating Subsidiaries</div>
        <h2 className="font-display text-3xl text-afano-navy mt-3">Business Units</h2>
        <div className="mt-10 grid md:grid-cols-2 gap-6">
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Cybersecurity</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Governance Risk & Compliance: RMF, FedRAMP, NIST, CMMC</li>
            <li>· Security Operations: SOC, Incident Response, Threat Hunting</li>
            <li>· Identity & Access Management: IGA, PAM, SSO, MFA</li>
            <li>· Vulnerability Management: Assessments, Penetration Testing, Remediation</li>
            <li>· Live site: https://cybitsolutions.net</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Cloud & Infrastructure</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Cloud Services: AWS, Azure, Google Cloud</li>
            <li>· Infrastructure: Data Centers, Networking, Virtualization</li>
            <li>· Managed Services: Help Desk, NOC, Infrastructure Support</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Software Engineering</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Application Development: Web, Mobile, Enterprise</li>
            <li>· DevSecOps: CI/CD, Automation, Containerization</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Data, AI & Automation</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Data Analytics: BI, Data Warehousing, Dashboards</li>
            <li>· Artificial Intelligence: Machine Learning, Generative AI, Predictive Analytics</li>
            <li>· Automation: RPA, Workflow Automation</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Digital Transformation</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Government Solutions: eGovernment, Smart Cities, Digital Identity</li>
            <li>· Enterprise Transformation: ERP, CRM, Process Modernization</li>
            <li>· Website & Digital Experience: Design, Development, eCommerce, UI/UX, Portals</li>
            <li>· Digital Government: eCabinet, Digital Parliament, Citizen Portals, eVisa, eProcurement, Digital Tax</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Telecommunications (NEW)</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Mobile Network Operations</li>
            <li>· Fixed-Line & Broadband ISP</li>
            <li>· Tower Infrastructure</li>
            <li>· Submarine & Terrestrial Fibre</li>
            <li>· Satellite Communications</li>
          </ul>
        </div>
        </div>
      </section>

      <section id="about" className="border-t border-mist bg-ivory">
        <div className="max-w-3xl mx-auto px-6 py-16">
          <h2 className="font-display text-3xl text-afano-navy">About this Division</h2>
          <p className="mt-4 text-ink/75 leading-relaxed">AFANO Technology & Digital Innovation Group is a Strategic Business Group of AFANO Group Holdings — operated as a wholly-owned intermediate holding entity. Each Business Unit is separately incorporated and trades under its own independent brand and domain.</p>
        </div>
      </section>

      <section id="contact" className="max-w-3xl mx-auto px-6 py-16">
        <h2 className="font-display text-3xl text-afano-navy">Contact</h2>
        <p className="mt-4 text-ink/75">Reach this division at <a className="text-brand underline" href="mailto:hello@tech.afanogroup.com">hello@tech.afanogroup.com</a>. For Group-level inquiries, visit <a className="text-brand underline" href="https://afanogroup.com">afanogroup.com</a>.</p>
      </section>

      <EndorsementFooter />
    </>
  );
}
