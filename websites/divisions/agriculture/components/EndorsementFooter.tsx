export function EndorsementFooter() {
  return (
    <footer className="bg-afano-navy text-ivory mt-24">
      <div className="max-w-6xl mx-auto px-6 py-10 flex flex-col md:flex-row items-center justify-between gap-4">
        <div className="flex items-center gap-3 text-sm">
          <svg viewBox="0 0 40 40" width="28" height="28" xmlns="http://www.w3.org/2000/svg">
            <polygon points="20,4 35,12 35,28 20,36 5,28 5,12" fill="none" stroke="#C8A04A" strokeWidth="2" />
            <circle cx="20" cy="20" r="6" fill="#C8A04A" />
          </svg>
          <span className="tracking-[0.3em] uppercase text-xs text-afano-gold">An AFANO Group Company</span>
        </div>
        <a href="https://afanogroup.com" className="text-xs text-ivory/70 hover:text-afano-gold no-underline">afanogroup.com</a>
      </div>
    </footer>
  );
}
