export function NetworkEmblem({ size = 320, color = "#C8A04A", bg = "#0B1F3A" }: { size?: number; color?: string; bg?: string }) {
  const cx = 200, cy = 200, r = 130;
  const nodes = Array.from({ length: 15 }, (_, i) => {
    const a = (i / 15) * Math.PI * 2 - Math.PI / 2;
    return { x: cx + r * Math.cos(a), y: cy + r * Math.sin(a) };
  });
  return (
    <svg viewBox="0 0 400 400" width={size} height={size} xmlns="http://www.w3.org/2000/svg">
      <rect width="400" height="400" fill={bg} />
      {nodes.flatMap((n, i) =>
        nodes.slice(i + 1).map((m, j) => (
          <line key={`l-${i}-${j}`} x1={n.x} y1={n.y} x2={m.x} y2={m.y}
                stroke={color} strokeWidth="0.5" opacity="0.18" />
        ))
      )}
      <circle cx={cx} cy={cy} r="32" fill="none" stroke={color} strokeWidth="1.6" />
      <circle cx={cx} cy={cy} r="10" fill={color} />
      {nodes.map((n, i) => (
        <g key={`n-${i}`}>
          <circle cx={n.x} cy={n.y} r="11" fill={bg} stroke={color} strokeWidth="1.4" />
          <circle cx={n.x} cy={n.y} r="4" fill={color} />
        </g>
      ))}
    </svg>
  );
}
