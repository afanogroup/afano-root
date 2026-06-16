import Link from "next/link";
import { Wordmark } from "./Wordmark";

const NAV = [
  { href: "/about", label: "About" },
  { href: "/divisions", label: "Divisions" },
  { href: "/leadership", label: "Leadership" },
  { href: "/investors", label: "Investors" },
  { href: "/sustainability", label: "Sustainability" },
  { href: "/news", label: "News" },
  { href: "/careers", label: "Careers" },
  { href: "/contact", label: "Contact" },
];

export function Header() {
  return (
    <header className="bg-navy text-ivory">
      <div className="max-w-7xl mx-auto flex items-center justify-between px-6 py-5">
        <Link href="/" className="no-underline"><Wordmark /></Link>
        <nav className="hidden md:flex gap-7 text-sm tracking-wide">
          {NAV.map(n => (
            <Link key={n.href} href={n.href} className="text-ivory/85 hover:text-gold transition no-underline">{n.label}</Link>
          ))}
        </nav>
      </div>
    </header>
  );
}
