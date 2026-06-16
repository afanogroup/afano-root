"""Generate the AFANO visual identity package as SVG masters.

Outputs to 02_Visual-Identity/:
  - grand-seal.svg            heraldic master seal (15 outer nodes)
  - network-emblem.svg        interconnected network mark (hero/IR use)
  - network-node.svg          single hexagonal node (favicon/app icon base)
  - wordmark.svg              AFANO wordmark for letterhead
  - wordmark-stacked.svg      AFANO wordmark above 'GROUP HOLDINGS' for IR
  - endorsement.svg           'An AFANO Group Company' lockup for subsidiaries
  - sigils/<slug>.svg         15 divisional sigils
  - colors.json               canonical color tokens
"""
from pathlib import Path
import json
import math
import afano_data as A

OUT = Path(__file__).parent.parent / "02_Visual-Identity"
SIG = OUT / "sigils"
OUT.mkdir(parents=True, exist_ok=True)
SIG.mkdir(parents=True, exist_ok=True)

NAVY = "#0B1F3A"
NAVY_DEEP = "#061327"
GOLD = "#C8A04A"
GOLD_DEEP = "#A37A2A"
IVORY = "#F5F0E3"
INK = "#0A0F1A"
MIST = "#D9DEE6"
WHITE = "#FFFFFF"

# Glyph SVG paths centered around (0,0) within a 60x60 unit box.
GLYPHS = {
    "coin": (
        "<circle r='22' fill='none' stroke='currentColor' stroke-width='3'/>"
        "<text x='0' y='8' text-anchor='middle' font-family='Georgia,serif' "
        "font-weight='700' font-size='28' fill='currentColor'>$</text>"
    ),
    "flame": (
        "<path d='M0,-22 C10,-10 18,-2 18,8 C18,20 9,26 0,26 "
        "C-9,26 -18,20 -18,8 C-18,-2 -10,-10 0,-22 Z' "
        "fill='currentColor'/>"
        "<path d='M0,-8 C5,-2 9,4 9,10 C9,17 4,22 0,22 C-4,22 -9,17 -9,10 "
        "C-9,4 -5,-2 0,-8 Z' fill='" + IVORY + "' opacity='0.85'/>"
    ),
    "node": (
        "<polygon points='0,-22 19,-11 19,11 0,22 -19,11 -19,-11' "
        "fill='none' stroke='currentColor' stroke-width='3'/>"
        "<circle r='5' fill='currentColor'/>"
        "<line x1='0' y1='-22' x2='0' y2='-7' stroke='currentColor' stroke-width='2'/>"
        "<line x1='19' y1='-11' x2='4' y2='-3' stroke='currentColor' stroke-width='2'/>"
        "<line x1='19' y1='11' x2='4' y2='3' stroke='currentColor' stroke-width='2'/>"
        "<line x1='0' y1='22' x2='0' y2='7' stroke='currentColor' stroke-width='2'/>"
        "<line x1='-19' y1='11' x2='-4' y2='3' stroke='currentColor' stroke-width='2'/>"
        "<line x1='-19' y1='-11' x2='-4' y2='-3' stroke='currentColor' stroke-width='2'/>"
    ),
    "pillar": (
        "<rect x='-18' y='-22' width='36' height='6' fill='currentColor'/>"
        "<rect x='-18' y='16' width='36' height='6' fill='currentColor'/>"
        "<rect x='-14' y='-14' width='6' height='28' fill='currentColor'/>"
        "<rect x='-3' y='-14' width='6' height='28' fill='currentColor'/>"
        "<rect x='8' y='-14' width='6' height='28' fill='currentColor'/>"
    ),
    "leaf": (
        "<path d='M0,-22 C16,-16 22,0 14,18 C8,22 -2,22 -8,18 "
        "C-16,4 -10,-12 0,-22 Z' fill='currentColor'/>"
        "<path d='M0,-18 C-2,-4 -4,8 -6,16' stroke='" + IVORY + "' "
        "stroke-width='2' fill='none'/>"
    ),
    "caduceus": (
        "<line x1='0' y1='-22' x2='0' y2='22' stroke='currentColor' stroke-width='3'/>"
        "<path d='M-12,-14 C0,-6 0,6 -12,14' fill='none' stroke='currentColor' stroke-width='3'/>"
        "<path d='M12,-14 C0,-6 0,6 12,14' fill='none' stroke='currentColor' stroke-width='3'/>"
        "<circle cx='0' cy='-22' r='4' fill='currentColor'/>"
    ),
    "compass": (
        "<circle r='22' fill='none' stroke='currentColor' stroke-width='3'/>"
        "<polygon points='0,-16 6,0 0,16 -6,0' fill='currentColor'/>"
        "<polygon points='0,-16 6,0 0,0' fill='" + IVORY + "' opacity='0.6'/>"
        "<circle r='3' fill='" + IVORY + "'/>"
    ),
    "torch": (
        "<path d='M0,-22 C10,-12 8,-2 0,4 C-8,-2 -10,-12 0,-22 Z' fill='currentColor'/>"
        "<rect x='-4' y='4' width='8' height='14' fill='currentColor'/>"
        "<rect x='-8' y='18' width='16' height='4' fill='currentColor'/>"
    ),
    "wave": (
        "<path d='M-22,-8 C-14,-16 -6,0 2,-8 C10,-16 18,0 22,-8' "
        "fill='none' stroke='currentColor' stroke-width='3' stroke-linecap='round'/>"
        "<path d='M-22,4 C-14,-4 -6,12 2,4 C10,-4 18,12 22,4' "
        "fill='none' stroke='currentColor' stroke-width='3' stroke-linecap='round'/>"
        "<path d='M-22,16 C-14,8 -6,24 2,16 C10,8 18,24 22,16' "
        "fill='none' stroke='currentColor' stroke-width='3' stroke-linecap='round'/>"
    ),
    "ship": (
        "<path d='M-22,4 L22,4 L18,16 L-18,16 Z' fill='currentColor'/>"
        "<rect x='-2' y='-22' width='4' height='26' fill='currentColor'/>"
        "<path d='M2,-22 L18,-2 L2,-2 Z' fill='currentColor'/>"
        "<path d='M-2,-16 L-14,-2 L-2,-2 Z' fill='currentColor'/>"
    ),
    "shield": (
        "<path d='M0,-22 L20,-14 L18,8 C16,18 8,22 0,24 C-8,22 -16,18 -18,8 "
        "L-20,-14 Z' fill='currentColor'/>"
        "<path d='M-8,-2 L-2,8 L10,-6' fill='none' stroke='" + IVORY + "' "
        "stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/>"
    ),
    "gear": (
        "<circle r='10' fill='currentColor'/>"
        "<g fill='currentColor'>"
        + "".join(
            f"<rect x='-3' y='-22' width='6' height='8' transform='rotate({a})'/>"
            for a in range(0, 360, 45)
        )
        + "</g>"
        "<circle r='4' fill='" + IVORY + "'/>"
    ),
    "bridge": (
        "<path d='M-22,8 C-12,-8 12,-8 22,8' fill='none' stroke='currentColor' stroke-width='3'/>"
        "<line x1='-22' y1='18' x2='22' y2='18' stroke='currentColor' stroke-width='3'/>"
        "<line x1='-16' y1='8' x2='-16' y2='18' stroke='currentColor' stroke-width='2'/>"
        "<line x1='-6' y1='1' x2='-6' y2='18' stroke='currentColor' stroke-width='2'/>"
        "<line x1='6' y1='1' x2='6' y2='18' stroke='currentColor' stroke-width='2'/>"
        "<line x1='16' y1='8' x2='16' y2='18' stroke='currentColor' stroke-width='2'/>"
    ),
    "hands": (
        "<path d='M-22,4 C-14,-4 -6,-4 0,2 C6,-4 14,-4 22,4 "
        "C22,14 12,22 0,22 C-12,22 -22,14 -22,4 Z' fill='currentColor'/>"
        "<path d='M-8,8 C-4,4 4,4 8,8' fill='none' stroke='" + IVORY + "' "
        "stroke-width='2'/>"
    ),
    "star": (
        "<polygon points='0,-22 6,-7 22,-7 9,3 14,18 0,9 -14,18 -9,3 -22,-7 -6,-7' "
        "fill='currentColor'/>"
    ),
}


def write(path: Path, content: str):
    path.write_text(content, encoding="utf-8")
    print(f"WROTE {path}")


# ---------- Wordmark ----------

def wordmark(stacked: bool = False) -> str:
    if stacked:
        return f"""<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 160'>
  <style>
    .a {{ font-family: Georgia, 'Times New Roman', serif; font-weight: 700; }}
    .b {{ font-family: Inter, Helvetica, Arial, sans-serif; letter-spacing: 0.4em; }}
  </style>
  <text x='200' y='90' text-anchor='middle' class='a' font-size='84' fill='{NAVY}'>AFANO</text>
  <line x1='80' y1='105' x2='320' y2='105' stroke='{GOLD}' stroke-width='2'/>
  <text x='200' y='132' text-anchor='middle' class='b' font-size='14' fill='{NAVY}'>GROUP HOLDINGS</text>
</svg>"""
    return f"""<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 360 80'>
  <text x='180' y='58' text-anchor='middle'
        font-family='Georgia, "Times New Roman", serif' font-weight='700'
        font-size='60' fill='{NAVY}' letter-spacing='4'>AFANO</text>
</svg>"""


# ---------- Network Node ----------

def network_node(stroke: str = NAVY, fill_dot: str = GOLD, bg: str | None = None) -> str:
    bg_layer = f"<rect width='100%' height='100%' fill='{bg}'/>" if bg else ""
    return f"""<svg xmlns='http://www.w3.org/2000/svg' viewBox='-50 -50 100 100'>
  {bg_layer}
  <g stroke='{stroke}' stroke-width='3' fill='none' stroke-linejoin='round' stroke-linecap='round'>
    <polygon points='0,-38 33,-19 33,19 0,38 -33,19 -33,-19'/>
    <line x1='0' y1='-38' x2='0' y2='-10'/>
    <line x1='33' y1='-19' x2='8' y2='-5'/>
    <line x1='33' y1='19' x2='8' y2='5'/>
    <line x1='0' y1='38' x2='0' y2='10'/>
    <line x1='-33' y1='19' x2='-8' y2='5'/>
    <line x1='-33' y1='-19' x2='-8' y2='-5'/>
  </g>
  <circle r='8' fill='{fill_dot}'/>
</svg>"""


# ---------- Network Emblem ----------

def network_emblem() -> str:
    # 15 nodes around a center, connected with subtle web.
    ring_r = 130
    nodes = []
    lines = []
    cx, cy = 0, 0
    pts = []
    for i in range(15):
        theta = -math.pi / 2 + 2 * math.pi * i / 15
        x = ring_r * math.cos(theta)
        y = ring_r * math.sin(theta)
        pts.append((x, y))
    # Connect each to the next two for a web effect.
    for i in range(15):
        for step in (1, 2):
            x1, y1 = pts[i]
            x2, y2 = pts[(i + step) % 15]
            lines.append(
                f"<line x1='{x1:.1f}' y1='{y1:.1f}' x2='{x2:.1f}' y2='{y2:.1f}'/>"
            )
    # Connect each to the center.
    for x, y in pts:
        lines.append(
            f"<line x1='0' y1='0' x2='{x:.1f}' y2='{y:.1f}' opacity='0.45'/>"
        )
    for x, y in pts:
        nodes.append(
            f"<circle cx='{x:.1f}' cy='{y:.1f}' r='8' fill='{GOLD}' stroke='{NAVY}' stroke-width='2'/>"
        )
    central = (
        f"<circle r='28' fill='{NAVY}'/>"
        f"<circle r='28' fill='none' stroke='{GOLD}' stroke-width='2'/>"
        f"<text x='0' y='10' text-anchor='middle' font-family='Georgia,serif' "
        f"font-weight='700' font-size='30' fill='{IVORY}'>A</text>"
    )
    return f"""<svg xmlns='http://www.w3.org/2000/svg' viewBox='-180 -180 360 360'>
  <g stroke='{NAVY}' stroke-width='1.5' fill='none' opacity='0.85'>
    {''.join(lines)}
  </g>
  {''.join(nodes)}
  {central}
</svg>"""


# ---------- Grand Seal ----------

def grand_seal() -> str:
    # Outer ring with text, inner monogram, 15 outer nodes representing SBGs.
    outer = 180
    inner = 152
    node_r = outer - 12
    nodes = []
    for i in range(15):
        theta = -math.pi / 2 + 2 * math.pi * i / 15
        x = node_r * math.cos(theta)
        y = node_r * math.sin(theta)
        nodes.append(
            f"<circle cx='{x:.1f}' cy='{y:.1f}' r='6' fill='{GOLD}'/>"
        )
    # Define a circle path for text-on-path.
    text_r = outer - 22
    path_d = (
        f"M {-text_r},0 "
        f"A {text_r},{text_r} 0 1,1 {text_r},0 "
        f"A {text_r},{text_r} 0 1,1 {-text_r},0"
    )
    return f"""<svg xmlns='http://www.w3.org/2000/svg' viewBox='-200 -200 400 400'>
  <defs>
    <path id='sealCircle' d='{path_d}'/>
    <radialGradient id='sealBg' cx='50%' cy='50%' r='50%'>
      <stop offset='0%' stop-color='{NAVY}'/>
      <stop offset='100%' stop-color='{NAVY_DEEP}'/>
    </radialGradient>
  </defs>
  <circle r='{outer}' fill='url(#sealBg)'/>
  <circle r='{outer}' fill='none' stroke='{GOLD}' stroke-width='3'/>
  <circle r='{outer - 6}' fill='none' stroke='{GOLD}' stroke-width='1' opacity='0.6'/>
  <circle r='{inner}' fill='none' stroke='{GOLD}' stroke-width='1'/>
  {''.join(nodes)}
  <text font-family='Georgia, "Times New Roman", serif' font-weight='700'
        font-size='18' fill='{IVORY}' letter-spacing='6'>
    <textPath href='#sealCircle' startOffset='25%' text-anchor='middle'>
      AFANO GROUP HOLDINGS
    </textPath>
  </text>
  <text font-family='Georgia, "Times New Roman", serif' font-style='italic'
        font-size='12' fill='{GOLD}' letter-spacing='2'>
    <textPath href='#sealCircle' startOffset='75%' text-anchor='middle'>
      EST. MMXXVI  ·  GLOBAL  ·  INDEPENDENT
    </textPath>
  </text>
  <text x='0' y='28' text-anchor='middle'
        font-family='Georgia, "Times New Roman", serif' font-weight='700'
        font-size='120' fill='{GOLD}'>A</text>
  <rect x='-60' y='52' width='120' height='2' fill='{GOLD}'/>
</svg>"""


# ---------- Divisional sigil ----------

def divisional_sigil(num: int, name: str, color: str, glyph: str) -> str:
    g = GLYPHS.get(glyph, GLYPHS["node"])
    short = name.split("—")[0].strip().split(" Group")[0]
    label = short.replace("AFANO ", "").upper()
    return f"""<svg xmlns='http://www.w3.org/2000/svg' viewBox='-100 -100 200 240'>
  <g stroke='{color}' stroke-width='2.5' fill='none' opacity='0.4'>
    <polygon points='0,-78 68,-39 68,39 0,78 -68,39 -68,-39'/>
  </g>
  <g stroke='{color}' stroke-width='3' fill='none'>
    <polygon points='0,-62 54,-31 54,31 0,62 -54,31 -54,-31'/>
  </g>
  <g color='{color}' transform='scale(1.45)'>
    {g}
  </g>
  <text x='0' y='112' text-anchor='middle'
        font-family='Inter, Helvetica, Arial, sans-serif'
        font-weight='600' font-size='14' letter-spacing='4' fill='{color}'>
    {label}
  </text>
  <text x='0' y='130' text-anchor='middle'
        font-family='Georgia, serif' font-style='italic' font-size='10'
        fill='{INK}' opacity='0.6'>
    SBG {num:02d} · AFANO GROUP
  </text>
</svg>"""


# ---------- Endorsement lockup ----------

def endorsement() -> str:
    return f"""<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 380 60'>
  <g transform='translate(30,30) scale(0.45)'>
    {network_node().split('>',2)[2].rsplit('</svg>',1)[0]}
  </g>
  <text x='80' y='28' font-family='Inter, Helvetica, Arial, sans-serif'
        font-size='11' letter-spacing='3' fill='{NAVY}'>AN</text>
  <text x='80' y='46' font-family='Georgia, "Times New Roman", serif'
        font-weight='700' font-size='18' fill='{NAVY}' letter-spacing='2'>
    AFANO GROUP COMPANY
  </text>
</svg>"""


# ---------- Colors token export ----------

def colors_json() -> str:
    tokens = {
        "afano": {
            "navy": NAVY,
            "navyDeep": NAVY_DEEP,
            "gold": GOLD,
            "goldDeep": GOLD_DEEP,
            "ivory": IVORY,
            "ink": INK,
            "mist": MIST,
            "white": WHITE,
        },
        "divisions": {
            d[3]: {"name": d[1], "primary": d[2], "glyph": d[4]}
            for d in A.DIVISIONS
        },
    }
    return json.dumps(tokens, indent=2)


def main():
    write(OUT / "wordmark.svg", wordmark(stacked=False))
    write(OUT / "wordmark-stacked.svg", wordmark(stacked=True))
    write(OUT / "network-node.svg", network_node())
    write(OUT / "network-node-on-navy.svg", network_node(stroke=IVORY, fill_dot=GOLD, bg=NAVY))
    write(OUT / "network-emblem.svg", network_emblem())
    write(OUT / "grand-seal.svg", grand_seal())
    write(OUT / "endorsement.svg", endorsement())
    write(OUT / "colors.json", colors_json())
    for d in A.DIVISIONS:
        num, name, color, sub, glyph, *_ = d
        write(SIG / f"{sub}.svg", divisional_sigil(num, name, color, glyph))


if __name__ == "__main__":
    main()
