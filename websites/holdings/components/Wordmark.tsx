export function Wordmark({ color = "#F5F0E3", subColor = "#C8A04A" }: { color?: string; subColor?: string }) {
  return (
    <div className="flex items-baseline gap-3 select-none">
      <span style={{ fontFamily: "Georgia, serif", fontWeight: 700, fontSize: 28, color, letterSpacing: "0.06em" }}>
        AFANO
      </span>
      <span style={{ fontFamily: "Inter, sans-serif", fontWeight: 400, fontSize: 12, color: subColor, letterSpacing: "0.25em", textTransform: "uppercase" }}>
        Group Holdings
      </span>
    </div>
  );
}
