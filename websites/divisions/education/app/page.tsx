import { EndorsementFooter } from "@/components/EndorsementFooter";

export default function Home() {
  return (
    <>
      <header className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-6 flex items-center justify-between">
          <div className="font-display text-2xl tracking-wide">AFANO Education, Training & Workforce Development Group</div>
          <nav className="hidden md:flex gap-6 text-sm">
            <a href="#about" className="text-white/85 hover:text-white">About</a>
            <a href="#units" className="text-white/85 hover:text-white">Business Units</a>
            <a href="#contact" className="text-white/85 hover:text-white">Contact</a>
          </nav>
        </div>
      </header>

      <section id="hero" className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-24">
          <div className="text-xs tracking-[0.4em] uppercase opacity-80">AFANO SBG 8</div>
          <h1 className="font-display text-5xl md:text-6xl mt-4 max-w-3xl leading-[1.05]">AFANO Education, Training & Workforce Development Group</h1>
          <p className="mt-6 max-w-2xl text-white/90 text-lg leading-relaxed">Academies, higher education, vocational training, talent and workforce solutions.</p>
        </div>
      </section>

      <section id="units" className="max-w-6xl mx-auto px-6 py-20">
        <div className="text-xs text-brand tracking-[0.4em] uppercase">Operating Subsidiaries</div>
        <h2 className="font-display text-3xl text-afano-navy mt-3">Business Units</h2>
        <div className="mt-10 grid md:grid-cols-2 gap-6">
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">AFANO / Cybit Academy</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Technology Training: Cybersecurity, Cloud Computing, AI & Data Analytics</li>
            <li>· Professional Certifications: PMP, Security+, AWS, CISSP, CFA</li>
            <li>· Fast-Track Programs: Bootcamps, Intensive Courses, Hackathons</li>
            <li>· Professional Development: Leadership, Project Management, Business Analysis, Executive Coaching</li>
            <li>· Live site: https://cybit360.com</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Higher Education</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Online Degrees: Undergraduate, Graduate, MBA</li>
            <li>· Diplomas: Professional, Technical, Vocational</li>
            <li>· Research Partnerships & Academic Collaborations</li>
            <li>· Study-Abroad & International Exchange Programs</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Talent, Workforce & Career Solutions</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Vocational Training: Trades, Technical Skills, Apprenticeships</li>
            <li>· Leadership Development: Executive Programs, Management Training</li>
            <li>· Recruiting: Permanent Placement, Contract Staffing, Executive Search</li>
            <li>· Career Services: Resume Writing, Career Coaching, Interview Preparation</li>
            <li>· Managed Workforce: Staff Augmentation, Workforce Outsourcing, RPO</li>
            <li>· Labour Market Intelligence & Workforce Analytics</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">K-12 & Early Education</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Primary & Secondary Schools</li>
            <li>· STEM Enrichment & Robotics Programs</li>
            <li>· Edutech Curriculum Licensing & LMS Platforms</li>
            <li>· Early Childhood Development Centres</li>
          </ul>
        </div>
        </div>
      </section>

      <section id="about" className="border-t border-mist bg-ivory">
        <div className="max-w-3xl mx-auto px-6 py-16">
          <h2 className="font-display text-3xl text-afano-navy">About this Division</h2>
          <p className="mt-4 text-ink/75 leading-relaxed">AFANO Education, Training & Workforce Development Group is a Strategic Business Group of AFANO Group Holdings — operated as a wholly-owned intermediate holding entity. Each Business Unit is separately incorporated and trades under its own independent brand and domain.</p>
        </div>
      </section>

      <section id="contact" className="max-w-3xl mx-auto px-6 py-16">
        <h2 className="font-display text-3xl text-afano-navy">Contact</h2>
        <p className="mt-4 text-ink/75">Reach this division at <a className="text-brand underline" href="mailto:hello@education.afanogroup.com">hello@education.afanogroup.com</a>. For Group-level inquiries, visit <a className="text-brand underline" href="https://afanogroup.com">afanogroup.com</a>.</p>
      </section>

      <EndorsementFooter />
    </>
  );
}
