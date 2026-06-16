import { PageHero } from "@/components/PageHero";

export const metadata = { title: "About" };

export default function About() {
  return (
    <>
      <PageHero eyebrow="The Group" title="A multinational, founder-led conglomerate"
        lead="AFANO Group Holdings is structured to support multiple subsidiaries, multiple brands, international operations, public-private partnerships, government contracts, foreign direct investment, mergers and acquisitions, and IPO-ready business units." />
      <section className="max-w-3xl mx-auto px-6 py-16 prose prose-lg">
        <h2 className="font-display text-3xl text-navy">Our Architecture</h2>
        <p>The Group operates a four-tier hierarchy. AFANO Group Holdings is the parent
          company. Beneath it sit 15 Strategic Business Groups — each a wholly-owned
          intermediate holding entity. Beneath each SBG are independently incorporated
          Business Units. Beneath each Business Unit are the Services and Sub-Services
          delivered to customers.</p>
        <h2 className="font-display text-3xl text-navy mt-10">Why House of Brands</h2>
        <p>The AFANO master mark is reserved for the holding company and its
          investor-facing communications. Operating subsidiaries trade under independent
          brands and domains. This pattern — proven by Procter & Gamble, Mitsubishi,
          and Berkshire Hathaway — allows each Business Unit to be sold, spun off, or
          listed without rename risk and without reputational contagion.</p>
        <h2 className="font-display text-3xl text-navy mt-10">Centralized Capital, Decentralized Operations</h2>
        <p>Treasury, audit, ESG, investor relations, brand stewardship, and capital
          allocation are centralized at Holdings. Commercial strategy, P&L, and brand
          are decentralized at the Business Unit. Each SBG competes for capital each
          year — none is guaranteed renewal.</p>
      </section>
    </>
  );
}
