import { EndorsementFooter } from "@/components/EndorsementFooter";

export default function Home() {
  return (
    <>
      <header className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-6 flex items-center justify-between">
          <div className="font-display text-2xl tracking-wide">AFANO Sports, Recreation & Youth Development Group</div>
          <nav className="hidden md:flex gap-6 text-sm">
            <a href="#about" className="text-white/85 hover:text-white">About</a>
            <a href="#units" className="text-white/85 hover:text-white">Business Units</a>
            <a href="#contact" className="text-white/85 hover:text-white">Contact</a>
          </nav>
        </div>
      </header>

      <section id="hero" className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-24">
          <div className="text-xs tracking-[0.4em] uppercase opacity-80">AFANO SBG 15</div>
          <h1 className="font-display text-5xl md:text-6xl mt-4 max-w-3xl leading-[1.05]">AFANO Sports, Recreation & Youth Development Group</h1>
          <p className="mt-6 max-w-2xl text-white/90 text-lg leading-relaxed">Academies, recreation, youth development and sports management.</p>
        </div>
      </section>

      <section id="units" className="max-w-6xl mx-auto px-6 py-20">
        <div className="text-xs text-brand tracking-[0.4em] uppercase">Operating Subsidiaries</div>
        <h2 className="font-display text-3xl text-afano-navy mt-3">Business Units</h2>
        <div className="mt-10 grid md:grid-cols-2 gap-6">
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Sports Academies</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Football Academy: Grassroots, Elite, Scout Networks</li>
            <li>· Basketball & Athletics Academies</li>
            <li>· Swimming & Aquatic Sports Centers</li>
            <li>· Multi-Sport Elite Performance Centres</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Recreation & Community Sports</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Recreation Centers: Gyms, Courts, Tracks</li>
            <li>· Community Sports Programs & School Partnerships</li>
            <li>· Sports Tourism: Sports Camps, Training Retreats</li>
            <li>· Sports Nutrition & Performance Science Clinics</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Youth Development</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Leadership Programs: Youth Councils, Governance Training</li>
            <li>· Mentorship Programs: Industry Connect, Alumni Networks</li>
            <li>· Youth Entrepreneurship: Startup Incubation, Business Training</li>
            <li>· Innovation Challenges & Youth Employment Programs</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Sports Management & Technology</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Event Management: Tournaments, Leagues, International Events</li>
            <li>· Talent Management: Athlete Representation, Sponsorship Deals</li>
            <li>· Facility Management: Stadium Operations, Ground Maintenance</li>
            <li>· Fan Engagement & Sports Tech: App Platforms, Ticketing, Analytics</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">eSports & Gaming</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Pro Teams & Competitive Leagues</li>
            <li>· Gaming Arenas & LAN Centers</li>
            <li>· Tournaments, Events & Broadcasting Rights</li>
            <li>· Game Development & Gaming IP</li>
          </ul>
        </div>
        </div>
      </section>

      <section id="about" className="border-t border-mist bg-ivory">
        <div className="max-w-3xl mx-auto px-6 py-16">
          <h2 className="font-display text-3xl text-afano-navy">About this Division</h2>
          <p className="mt-4 text-ink/75 leading-relaxed">AFANO Sports, Recreation & Youth Development Group is a Strategic Business Group of AFANO Group Holdings — operated as a wholly-owned intermediate holding entity. Each Business Unit is separately incorporated and trades under its own independent brand and domain.</p>
        </div>
      </section>

      <section id="contact" className="max-w-3xl mx-auto px-6 py-16">
        <h2 className="font-display text-3xl text-afano-navy">Contact</h2>
        <p className="mt-4 text-ink/75">Reach this division at <a className="text-brand underline" href="mailto:hello@sports.afanogroup.com">hello@sports.afanogroup.com</a>. For Group-level inquiries, visit <a className="text-brand underline" href="https://afanogroup.com">afanogroup.com</a>.</p>
      </section>

      <EndorsementFooter />
    </>
  );
}
