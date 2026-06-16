import { PageHero } from "@/components/PageHero";

export const metadata = { title: "Leadership" };

export default function Leadership() {
  const exec = [
    ["Founder & Executive Chair", "Founder"],
    ["Chief Executive Officer", "TBA"],
    ["Chief Financial Officer", "TBA"],
    ["Chief Legal Officer", "TBA"],
    ["Chief Risk Officer", "TBA"],
    ["Chief Investment Officer", "TBA"],
    ["Chief Sustainability Officer", "TBA"],
    ["Corporate Secretary", "TBA"],
  ];
  return (
    <>
      <PageHero eyebrow="The Group" title="Leadership"
        lead="The Holdings Office and the SBG executive committee — accountable to the Board and the Group's stakeholders." />
      <section className="max-w-4xl mx-auto px-6 py-16">
        <h2 className="font-display text-2xl text-navy mb-6">Executive Committee</h2>
        <div className="grid sm:grid-cols-2 gap-6">
          {exec.map(([role, name]) => (
            <div key={role} className="border-l-2 border-gold pl-4 py-1">
              <div className="text-xs uppercase tracking-widest text-ink/55">{role}</div>
              <div className="font-display text-lg text-navy mt-1">{name}</div>
            </div>
          ))}
        </div>
        <p className="mt-12 text-sm text-ink/55">
          Director and committee appointments published annually in the Group's
          governance report.
        </p>
      </section>
    </>
  );
}
