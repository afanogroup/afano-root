import { PageHero } from "@/components/PageHero";

export const metadata = { title: "News" };

export default function News() {
  return (
    <>
      <PageHero eyebrow="Newsroom" title="News & Press" lead="Group-level announcements appear here. Subsidiary press is published on the subsidiary's own site." />
      <section className="max-w-3xl mx-auto px-6 py-16 text-ink/70">
        <p>The newsroom feed is wired up at launch — connect the CMS or RSS source of your
          choice. The default layout is chronological with a press-release detail page.</p>
      </section>
    </>
  );
}
