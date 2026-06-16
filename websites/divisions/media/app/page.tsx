import { EndorsementFooter } from "@/components/EndorsementFooter";

export default function Home() {
  return (
    <>
      <header className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-6 flex items-center justify-between">
          <div className="font-display text-2xl tracking-wide">AFANO Media, Communications & Entertainment Group</div>
          <nav className="hidden md:flex gap-6 text-sm">
            <a href="#about" className="text-white/85 hover:text-white">About</a>
            <a href="#units" className="text-white/85 hover:text-white">Business Units</a>
            <a href="#contact" className="text-white/85 hover:text-white">Contact</a>
          </nav>
        </div>
      </header>

      <section id="hero" className="bg-brand text-white">
        <div className="max-w-6xl mx-auto px-6 py-24">
          <div className="text-xs tracking-[0.4em] uppercase opacity-80">AFANO SBG 9</div>
          <h1 className="font-display text-5xl md:text-6xl mt-4 max-w-3xl leading-[1.05]">AFANO Media, Communications & Entertainment Group</h1>
          <p className="mt-6 max-w-2xl text-white/90 text-lg leading-relaxed">Broadcasting, digital media, creative services and entertainment production.</p>
        </div>
      </section>

      <section id="units" className="max-w-6xl mx-auto px-6 py-20">
        <div className="text-xs text-brand tracking-[0.4em] uppercase">Operating Subsidiaries</div>
        <h2 className="font-display text-3xl text-afano-navy mt-3">Business Units</h2>
        <div className="mt-10 grid md:grid-cols-2 gap-6">
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Broadcasting</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Television Networks</li>
            <li>· Radio Networks</li>
            <li>· Streaming Networks</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Digital Media</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Content Creation</li>
            <li>· Social Media Management</li>
            <li>· Podcast Production</li>
            <li>· Digital Marketing: SEO, SEM, Social, Content, Email, Marketing Automation</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Creative Services</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Advertising</li>
            <li>· Public Relations</li>
            <li>· Branding & Identity</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Entertainment</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Film Production</li>
            <li>· Music Production</li>
            <li>· Event Production</li>
            <li>· Sports Entertainment & Live Events (NEW)</li>
          </ul>
        </div>
        <div className="border border-mist p-6 bg-white">
          <h3 className="font-display text-xl text-afano-navy">Publishing (NEW)</h3>
          <ul className="mt-3 space-y-1 text-sm text-ink/75">
            <li>· Book Publishing</li>
            <li>· Magazines & Journals</li>
            <li>· Digital Publications</li>
          </ul>
        </div>
        </div>
      </section>

      <section id="about" className="border-t border-mist bg-ivory">
        <div className="max-w-3xl mx-auto px-6 py-16">
          <h2 className="font-display text-3xl text-afano-navy">About this Division</h2>
          <p className="mt-4 text-ink/75 leading-relaxed">AFANO Media, Communications & Entertainment Group is a Strategic Business Group of AFANO Group Holdings — operated as a wholly-owned intermediate holding entity. Each Business Unit is separately incorporated and trades under its own independent brand and domain.</p>
        </div>
      </section>

      <section id="contact" className="max-w-3xl mx-auto px-6 py-16">
        <h2 className="font-display text-3xl text-afano-navy">Contact</h2>
        <p className="mt-4 text-ink/75">Reach this division at <a className="text-brand underline" href="mailto:hello@media.afanogroup.com">hello@media.afanogroup.com</a>. For Group-level inquiries, visit <a className="text-brand underline" href="https://afanogroup.com">afanogroup.com</a>.</p>
      </section>

      <EndorsementFooter />
    </>
  );
}
