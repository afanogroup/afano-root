"""Generate AFANO-Brand-Guidelines.docx."""
from pathlib import Path
from docx import Document
from docx.shared import Pt, RGBColor, Inches, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
import afano_data as A

OUT = Path(__file__).parent.parent / "02_Visual-Identity" / "AFANO-Brand-Guidelines.docx"
NAVY = RGBColor(0x0B, 0x1F, 0x3A)
GOLD = RGBColor(0xC8, 0xA0, 0x4A)
GREY = RGBColor(0x55, 0x55, 0x55)


def H(doc, text, level=1, color=NAVY, size=None):
    p = doc.add_heading("", level=level)
    r = p.add_run(text)
    r.bold = True
    r.font.color.rgb = color
    if size:
        r.font.size = Pt(size)


def P(doc, text, bold=False, italic=False, color=None, size=None, align=None):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = bold
    r.italic = italic
    if color:
        r.font.color.rgb = color
    if size:
        r.font.size = Pt(size)
    if align is not None:
        p.alignment = align


def bullet(doc, text):
    doc.add_paragraph(text, style="List Bullet")


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc = Document()
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(11)
    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.9)
        s.right_margin = Inches(0.9)

    # Cover
    P(doc, "")
    P(doc, "")
    P(doc, "AFANO GROUP HOLDINGS", bold=True, color=NAVY, size=32,
      align=WD_ALIGN_PARAGRAPH.CENTER)
    P(doc, "Brand Guidelines", italic=True, color=GOLD, size=18,
      align=WD_ALIGN_PARAGRAPH.CENTER)
    P(doc, "Identity · Voice · Application", color=GREY, size=12,
      align=WD_ALIGN_PARAGRAPH.CENTER)
    P(doc, "Version 1.0", color=GREY, size=10,
      align=WD_ALIGN_PARAGRAPH.CENTER)
    doc.add_page_break()

    H(doc, "1. The Brand Architecture Model", 1)
    P(doc,
      "AFANO Group Holdings follows a House of Brands architecture (Procter & "
      "Gamble, Mitsubishi keiretsu, Unilever). The AFANO master mark is reserved "
      "for the holding company and its investor-facing communications. Operating "
      "subsidiaries trade under independent brands and domains.")
    P(doc, "Rationale:", bold=True)
    bullet(doc, "Allows divestiture, IPO, JV, or M&A without customer-facing rename risk.")
    bullet(doc, "Prevents reputational contagion across unrelated industries.")
    bullet(doc, "Permits market-appropriate brand positioning per division.")

    H(doc, "2. Master Identity Assets", 1)
    P(doc, "Five primary marks comprise the AFANO master identity:")
    bullet(doc, "Grand Seal — heraldic mark for legal, ceremonial, IR cover use.")
    bullet(doc, "Network Emblem — 15-node interconnected web for corporate hero and ESG report.")
    bullet(doc, "Network Node — single hexagonal node used as favicon, app icon, and sigil base.")
    bullet(doc, "Wordmark (horizontal) — primary text mark for letterhead and footers.")
    bullet(doc, "Wordmark (stacked) — formal stacked mark for IR decks and annual reports.")
    P(doc, "SVG masters and rendered PNGs live in 02_Visual-Identity/. Do not "
           "recolour, reproportion, or reconstruct these marks. If a mark does "
           "not exist for a use case, request it through Brand Stewardship.",
      color=GREY, size=9, italic=True)

    H(doc, "3. Color System", 1)
    P(doc, "AFANO Master Palette (Holdings / IR / Legal use only):", bold=True)
    bullet(doc, "AFANO Navy — #0B1F3A — RGB(11,31,58) — CMYK(96,80,40,40) — primary.")
    bullet(doc, "AFANO Navy Deep — #061327 — accent for gradients and ceremonial backgrounds.")
    bullet(doc, "AFANO Gold — #C8A04A — RGB(200,160,74) — accent only; never primary on screen.")
    bullet(doc, "Ivory — #F5F0E3 — neutral light, replaces white for ceremonial contexts.")
    bullet(doc, "Mist — #D9DEE6 — surface neutral for layout grids.")
    bullet(doc, "Ink — #0A0F1A — body copy on light surfaces.")
    P(doc, "Each of the 15 SBGs has an independent primary brand color that is "
           "NOT AFANO Navy. The intent is brand independence at the divisional level.",
      bold=True)
    for d in A.DIVISIONS:
        num, name, color, sub, glyph, *_ = d
        bullet(doc, f"SBG {num} ({sub}): {color} — {name}")

    H(doc, "4. Typography", 1)
    bullet(doc, "Display / Ceremonial: Georgia, GT Sectra, or Tiempos. Serif. Used for IR, legal, annual report.")
    bullet(doc, "Operational / UI: Inter (open source). Grotesk. Used for digital products, dashboards, websites.")
    bullet(doc, "Numerals: Use tabular numerals for financial tables.")
    bullet(doc, "Hierarchy: H1 32–42pt serif; H2 18–22pt serif; body 11pt grotesk; caption 9pt grotesk italic.")

    H(doc, "5. Clearspace, Minimum Sizes, Don'ts", 1)
    bullet(doc, "Grand Seal: minimum 32px digital, 12mm print. Clearspace equal to height of central monogram on all sides.")
    bullet(doc, "Network Emblem: minimum 64px digital. Clearspace equal to one node-ring diameter.")
    bullet(doc, "Network Node: scalable to 16px favicon; below 16px, use the solid gold dot only.")
    bullet(doc, "Wordmark: minimum height 20px digital, 6mm print.")
    P(doc, "Never:", bold=True)
    bullet(doc, "Recolour the Grand Seal (gold-on-navy is canonical; reverse permitted only on dark backgrounds).")
    bullet(doc, "Combine AFANO master marks with operating-subsidiary marks on the same surface (Endorsement Lockup excepted).")
    bullet(doc, "Apply gradients, drop shadows, bevels, or 3D effects.")
    bullet(doc, "Outline, stretch, skew, or rotate any mark.")
    bullet(doc, "Use the AFANO master marks on consumer packaging or storefronts.")

    H(doc, "6. The Endorsement Lockup", 1)
    P(doc,
      "Subsidiaries display the AFANO endorsement only in low-prominence "
      "contexts: website footer, About page, ESG report attribution, "
      "corporate stationery. The lockup is 'AN AFANO GROUP COMPANY' set "
      "alongside the Network Node mark, in the subsidiary's brand color or "
      "AFANO Navy. Maximum visual weight is 40% of the subsidiary's own "
      "wordmark on the same surface.")
    P(doc, "endorsement.svg is the canonical asset.", color=GREY, italic=True, size=9)

    H(doc, "7. Divisional Sigils", 1)
    P(doc,
      "Each SBG has a sigil — a hexagonal Network Node with an outer orbit "
      "ring and a division-specific glyph in the division's primary color. "
      "Sigils are used:")
    bullet(doc, "On the AFANO holdings site division grid.")
    bullet(doc, "On internal Group documents that reference multiple divisions.")
    bullet(doc, "In M&A, IR and ESG decks where divisional attribution is required.")
    bullet(doc, "NEVER on a Business Unit's customer-facing materials.")

    H(doc, "8. Voice & Editorial", 1)
    bullet(doc, "Tone: Authoritative, restrained, multinational. Avoid superlatives and hype.")
    bullet(doc, "Always 'AFANO Group Holdings' in first reference, 'the Group' thereafter.")
    bullet(doc, "Refer to subsidiaries by their independent name first; AFANO endorsement is footnote-level.")
    bullet(doc, "Currency: USD primary; secondary local currency in parentheses for regional materials.")
    bullet(doc, "Dates: ISO 8601 (YYYY-MM-DD) in tables; long form ('15 June 2026') in prose.")

    H(doc, "9. Digital Application", 1)
    bullet(doc, "Master holdings site: afanogroup.com — uses Grand Seal and Network Emblem prominently.")
    bullet(doc, "Subsidiary sites: independent brand identity; endorsement footer only.")
    bullet(doc, "Favicons: Network Node, gold dot on navy at 16/32, full hexagon at 64+.")
    bullet(doc, "Social media (Group accounts): Network Emblem avatar; subsidiary social uses subsidiary brand.")

    H(doc, "10. File Locations", 1)
    P(doc, "All SVG masters and exports live in 02_Visual-Identity/. The "
           "design-token JSON for code use lives at 02_Visual-Identity/colors.json. "
           "These tokens are mirrored into the @afano/ui package at "
           "websites/shared/ui/src/tokens.ts at build time.")

    doc.save(OUT)
    print(f"WROTE {OUT}")


if __name__ == "__main__":
    main()
