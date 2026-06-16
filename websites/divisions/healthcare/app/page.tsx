import { EndorsementFooter } from "@/components/EndorsementFooter";

export default function Home() {
  return (
    <>
      <header className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-6 flex items-center justify-between">
          <div className="font-display text-2xl tracking-wide">AFANO Healthcare & Life Sciences Group</div>
          <nav className="hidden md:flex gap-6 text-sm">
            <a href="#about" className="text-white/85 hover:text-white">About</a>
            <a href="#units" className="text-white/85 hover:text-white">Business Units</a>
            <a href="#contact" className="text-white/85 hover:text-white">Contact</a>
          </nav>
        </div>
      </header>

      <section id="hero" className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-24">
          <div className="text-xs tracking-[0.4em] uppercase opacity-80">AFANO SBG 6</div>
          <h1 className="font-display text-5xl md:text-6xl mt-4 max-w-3xl leading-[1.05]">AFANO Healthcare & Life Sciences Group</h1>
          <p className="mt-6 max-w-2xl text-white/90 text-lg leading-relaxed">Clinical care, pharmaceuticals, life sciences, health technology and medical infrastructure.</p>
        </div>
      </section>

      <section id="units" className="max-w-6xl mx-auto px-6 py-20">
        <div className="text-xs text-brand tracking-[0.4em] uppercase">Operating Subsidiaries</div>
        <h2 className="font-display text-3xl text-afano-navy mt-3">Business Units</h2>
        <div className="mt-10 grid md:grid-cols-2 gap-6">
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Healthcare Services</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Clinical Services: Primary Care, Specialty Care, Chronic Disease Management</li>
            <li>· Telehealth: Virtual Consultations, Remote Patient Monitoring</li>
            <li>· Hospital & Clinic Operations: Greenfield Hospitals, Specialist Clinics</li>
            <li>· Mental Health & Wellness: Counselling, Psychiatric Services, Corporate Wellness</li>
            <li>· Maternal, Neonatal & Child Health Programs</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Pharmaceuticals & Medical Supplies</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Pharmacy Operations: Retail Pharmacy Chains, Hospital Pharmacy</li>
            <li>· Pharmaceutical Manufacturing: Generic Drugs, OTC Products</li>
            <li>· Medical Supplies: Equipment Distribution, Consumables, PPE</li>
            <li>· Chemical & Laboratory Distribution: Lab Chemicals, Pharmaceutical Inputs</li>
            <li>· Cold Chain Pharmaceutical Logistics</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Life Sciences & Biotechnology</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Laboratory Services: Diagnostics, Clinical Testing, Pathology</li>
            <li>· Biotechnology: Drug Discovery, Biologics, Gene Therapy Research</li>
            <li>· Contract Research Organisation (CRO): Clinical Trials, Regulatory Affairs</li>
            <li>· Genomics & Personalized Medicine: Genetic Testing, Precision Oncology</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Health Technology</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Electronic Medical Records: EMR/EHR, Hospital Information Systems</li>
            <li>· Telemedicine Platforms & Digital Health Apps</li>
            <li>· Health Analytics: Population Health, Predictive Risk Stratification</li>
            <li>· AI-Powered Diagnostics & Radiology AI</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Medical Devices & Diagnostics</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Imaging Equipment: MRI, CT, Ultrasound</li>
            <li>· Diagnostic Devices: Point-of-Care Testing, In-Vitro Diagnostics</li>
            <li>· Wearables & Remote Patient Monitoring Hardware</li>
            <li>· Surgical Robotics & Minimally Invasive Tools</li>
          </ul>
        </div>
        </div>
      </section>

      <section id="about" className="border-t border-mist bg-ivory">
        <div className="max-w-3xl mx-auto px-6 py-16">
          <h2 className="font-display text-3xl text-afano-navy">About this Division</h2>
          <p className="mt-4 text-ink/75 leading-relaxed">AFANO Healthcare & Life Sciences Group is a Strategic Business Group of AFANO Group Holdings — operated as a wholly-owned intermediate holding entity. Each Business Unit is separately incorporated and trades under its own independent brand and domain.</p>
        </div>
      </section>

      <section id="contact" className="max-w-3xl mx-auto px-6 py-16">
        <h2 className="font-display text-3xl text-afano-navy">Contact</h2>
        <p className="mt-4 text-ink/75">Reach this division at <a className="text-brand underline" href="mailto:hello@health.afanogroup.com">hello@health.afanogroup.com</a>. For Group-level inquiries, visit <a className="text-brand underline" href="https://afanogroup.com">afanogroup.com</a>.</p>
      </section>

      <EndorsementFooter />
    </>
  );
}
