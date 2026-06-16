import { EndorsementFooter } from "@/components/EndorsementFooter";

export default function Home() {
  return (
    <>
      <header className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-6 flex items-center justify-between">
          <div className="font-display text-2xl tracking-wide">AFANO Government, Defense & National Security Group</div>
          <nav className="hidden md:flex gap-6 text-sm">
            <a href="#about" className="text-white/85 hover:text-white">About</a>
            <a href="#units" className="text-white/85 hover:text-white">Business Units</a>
            <a href="#contact" className="text-white/85 hover:text-white">Contact</a>
          </nav>
        </div>
      </header>

      <section id="hero" className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-24">
          <div className="text-xs tracking-[0.4em] uppercase opacity-80">AFANO SBG 11</div>
          <h1 className="font-display text-5xl md:text-6xl mt-4 max-w-3xl leading-[1.05]">AFANO Government, Defense & National Security Group</h1>
          <p className="mt-6 max-w-2xl text-white/90 text-lg leading-relaxed">Government consulting, defense technology, security services, public safety and homeland security solutions.</p>
        </div>
      </section>

      <section id="units" className="max-w-6xl mx-auto px-6 py-20">
        <div className="text-xs text-brand tracking-[0.4em] uppercase">Operating Subsidiaries</div>
        <h2 className="font-display text-3xl text-afano-navy mt-3">Business Units</h2>
        <div className="mt-10 grid md:grid-cols-2 gap-6">
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Government Consulting</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Public Sector Advisory</li>
            <li>· Government Modernization</li>
            <li>· Policy Implementation Support</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Defense Technology</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Cyber Defense</li>
            <li>· Command & Control Systems</li>
            <li>· ISR (Intelligence, Surveillance, Reconnaissance)</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Security Services</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Physical Security: Armed Guards, Unarmed Guards, Event Security, Executive Protection, VIP Protection, Security Training</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Public Safety</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Emergency Management</li>
            <li>· Critical Infrastructure Protection</li>
            <li>· Disaster Response Coordination</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Aerospace & Defense Manufacturing (NEW)</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· UAV / Drones</li>
            <li>· Satellite Systems</li>
            <li>· Defense Electronics</li>
            <li>· Munitions & Land Systems (regulated)</li>
          </ul>
        </div>
        </div>
      </section>

      <section id="about" className="border-t border-mist bg-ivory">
        <div className="max-w-3xl mx-auto px-6 py-16">
          <h2 className="font-display text-3xl text-afano-navy">About this Division</h2>
          <p className="mt-4 text-ink/75 leading-relaxed">AFANO Government, Defense & National Security Group is a Strategic Business Group of AFANO Group Holdings — operated as a wholly-owned intermediate holding entity. Each Business Unit is separately incorporated and trades under its own independent brand and domain.</p>
        </div>
      </section>

      <section id="contact" className="max-w-3xl mx-auto px-6 py-16">
        <h2 className="font-display text-3xl text-afano-navy">Contact</h2>
        <p className="mt-4 text-ink/75">Reach this division at <a className="text-brand underline" href="mailto:hello@shield.afanogroup.com">hello@shield.afanogroup.com</a>. For Group-level inquiries, visit <a className="text-brand underline" href="https://afanogroup.com">afanogroup.com</a>.</p>
      </section>

      <EndorsementFooter />
    </>
  );
}
