"""Generate Branding-Architecture.docx — companion to Domain-Architecture.xlsx.

Reads 01_Branding-Domains/Domain-Architecture.json produced by check_domains.py
and writes a narrative document covering:
  - House of Brands rationale
  - Per-SBG recommended primary domain (with live RDAP status)
  - Per-Business-Unit recommended primary domain
  - Endorsement footer policy
  - Trademark / WIPO / USPTO next-step checklist
"""
from pathlib import Path
import json
from collections import defaultdict
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import afano_data as A

BASE = Path(__file__).parent.parent
IN_JSON = BASE / "01_Branding-Domains" / "Domain-Architecture.json"
OUT = BASE / "01_Branding-Domains" / "Branding-Architecture.docx"

NAVY = RGBColor(0x0B, 0x1F, 0x3A)
GOLD = RGBColor(0xC8, 0xA0, 0x4A)
GREY = RGBColor(0x55, 0x55, 0x55)
GREEN = RGBColor(0x2E, 0x7D, 0x32)
RED = RGBColor(0xC6, 0x28, 0x28)
AMBER = RGBColor(0xB7, 0x86, 0x00)


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


def bullet(doc, text, color=None, bold=False):
    p = doc.add_paragraph("", style="List Bullet")
    r = p.add_run(text)
    if color:
        r.font.color.rgb = color
    r.bold = bold


def status_color(status):
    if status == "AVAILABLE":
        return GREEN
    if status == "REGISTERED":
        return RED
    return AMBER


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    rows = json.loads(IN_JSON.read_text(encoding="utf-8"))

    doc = Document()
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(11)
    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.9)
        s.right_margin = Inches(0.9)

    # Cover
    P(doc, ""); P(doc, "")
    P(doc, "AFANO GROUP HOLDINGS", bold=True, color=NAVY, size=30,
      align=WD_ALIGN_PARAGRAPH.CENTER)
    P(doc, "Branding & Domain Architecture", italic=True, color=GOLD, size=18,
      align=WD_ALIGN_PARAGRAPH.CENTER)
    P(doc, "House of Brands · Independent Domains · Endorsed by AFANO",
      color=GREY, size=11, align=WD_ALIGN_PARAGRAPH.CENTER)
    doc.add_page_break()

    H(doc, "1. Brand Architecture Model", 1)
    P(doc,
      "AFANO Group Holdings operates a House of Brands. The AFANO master mark "
      "is reserved for the holding company, its investor-facing communications, "
      "and a discreet 'An AFANO Group Company' endorsement footer on each "
      "operating subsidiary's site. Every operating subsidiary trades under an "
      "independent brand and domain that does not begin or end with 'afano' "
      "or 'cybit'.")
    P(doc, "Comparable precedents:", bold=True)
    bullet(doc, "Procter & Gamble — Tide, Gillette, Pampers all independent of P&G.")
    bullet(doc, "Mitsubishi Corporation — Nikon, Kirin, Mitsubishi UFJ each carries its own identity within the keiretsu.")
    bullet(doc, "Berkshire Hathaway — GEICO, Duracell, Dairy Queen retain independent brand equity.")
    bullet(doc, "Unilever — Dove, Knorr, Ben & Jerry's all kept their pre-acquisition identity.")
    P(doc,
      "This architecture lets a Business Unit be sold, spun-off, IPO'd, or "
      "operated as a joint venture without rename risk to the customer-facing "
      "identity.", italic=True, color=GREY)

    H(doc, "2. Verification Methodology", 1)
    P(doc,
      "Each candidate domain was checked live against the public RDAP "
      "(Registration Data Access Protocol) bootstrap at rdap.org/domain/. "
      "RDAP returns HTTP 404 for unregistered names and HTTP 200 with a "
      "registration record for taken names. Results are color-coded in the "
      "companion Domain-Architecture.xlsx:")
    bullet(doc, "GREEN = AVAILABLE (RDAP 404).", color=GREEN, bold=True)
    bullet(doc, "RED = REGISTERED (RDAP 200 — taken).", color=RED, bold=True)
    bullet(doc, "AMBER = rate-limited or TLD not in RDAP bootstrap; manual whois follow-up required.", color=AMBER, bold=True)
    P(doc,
      "RDAP availability is the threshold check only. Before purchase, every "
      "primary pick must clear: (a) USPTO TESS trademark search, (b) WIPO "
      "Global Brand Database search, (c) registrar parked-status visual "
      "check, (d) Wayback Machine prior-use review.", color=GREY, italic=True, size=9)

    # Build a status lookup
    div_picks = defaultdict(list)  # sbg -> list of (fqdn, status, rationale)
    bu_picks = defaultdict(list)   # bu_name -> list of (fqdn, status, rationale)
    sbg_of_bu = {}                 # bu_name -> sbg number
    for r in rows:
        item = (r["fqdn"], r["status"], r["rationale"], r["recommendation"])
        if r["level"] == "Division":
            div_picks[r["sbg"]].append(item)
        else:
            bu_picks[r["business_unit"]].append(item)
            sbg_of_bu[r["business_unit"]] = r["sbg"]

    H(doc, "3. Recommended Division Domains (15 SBGs)", 1)
    P(doc,
      "Each SBG is assigned an independent division-level brand. The PRIMARY "
      "pick is the first candidate; alternates are shown for fallback if "
      "trademark conflict or registrar parking is later discovered.")
    for d in A.DIVISIONS:
        num, name, color_hex, *_ = d
        picks = div_picks.get(num, [])
        H(doc, f"SBG {num} — {name}", level=2,
          color=RGBColor.from_string(color_hex.lstrip("#")), size=14)
        if not picks:
            P(doc, "No candidates recorded.", color=GREY, italic=True)
            continue
        for fqdn, status, rationale, rec in picks:
            tag = "PRIMARY" if rec == "PRIMARY PICK" else "alt"
            line = f"[{tag}] {fqdn} — {status} — {rationale}"
            p = doc.add_paragraph()
            r = p.add_run(f"[{tag}] ")
            r.bold = True
            r.font.color.rgb = NAVY if tag == "PRIMARY" else GREY
            r2 = p.add_run(f"{fqdn}")
            r2.bold = True
            p.add_run(f" — ")
            r3 = p.add_run(status)
            r3.font.color.rgb = status_color(status)
            r3.bold = True
            p.add_run(f" — {rationale}")

    H(doc, "4. Recommended Business-Unit Domains", 1)
    P(doc,
      "Each Business Unit receives its own independent brand and domain — the "
      "foundation of the spin-off, IPO and M&A optionality described in the "
      "Strategy document. Three live properties are retained under their "
      "existing brands: cybitsolutions.net (Cybersecurity BU), cybit360.com "
      "(Academy BU), and srv1736078.hstgr.cloud (FinTech BU — to migrate to "
      "an independent domain pre-launch).")

    # Group BU picks by SBG
    bu_by_sbg = defaultdict(list)
    for bu_name, picks in bu_picks.items():
        bu_by_sbg[sbg_of_bu[bu_name]].append((bu_name, picks))

    for d in A.DIVISIONS:
        num, name, color_hex, *_ = d
        bus = bu_by_sbg.get(num, [])
        if not bus:
            continue
        H(doc, f"SBG {num} — {name}", level=2,
          color=RGBColor.from_string(color_hex.lstrip("#")), size=13)
        for bu_name, picks in bus:
            H(doc, bu_name, level=3, color=NAVY, size=11)
            for fqdn, status, rationale, rec in picks:
                tag = "PRIMARY" if rec == "PRIMARY PICK" else "alt"
                p = doc.add_paragraph()
                r = p.add_run(f"[{tag}] ")
                r.bold = True
                r.font.color.rgb = NAVY if tag == "PRIMARY" else GREY
                r2 = p.add_run(f"{fqdn}")
                r2.bold = True
                p.add_run(" — ")
                r3 = p.add_run(status)
                r3.font.color.rgb = status_color(status)
                r3.bold = True
                p.add_run(f" — {rationale}")

    doc.add_page_break()

    H(doc, "5. Endorsement Lockup Policy", 1)
    P(doc,
      "Every operating subsidiary website displays a single 'An AFANO Group "
      "Company' endorsement footer with the AFANO Network Node mark, linking "
      "back to afanogroup.com. This is the entire scope of the AFANO "
      "endorsement; no further AFANO co-branding is permitted in customer-"
      "facing contexts. Investor-facing properties (IR pages, ESG report, "
      "annual report) may use AFANO master marks more prominently.")
    bullet(doc, "Footer height: maximum 40% of subsidiary's own wordmark.")
    bullet(doc, "Color: subsidiary's brand color OR AFANO Navy — never both on same surface.")
    bullet(doc, "Endorsement link target: afanogroup.com root, not a campaign URL.")
    bullet(doc, "Endorsement may be omitted on transactional UI (checkout, login, app screens) to preserve focus.")

    H(doc, "6. Pre-Acquisition Checklist (per domain)", 1)
    P(doc, "Before purchase, the Brand Stewardship function executes:")
    bullet(doc, "USPTO TESS search — confirm no live federal trademark conflict in target classes.")
    bullet(doc, "WIPO Global Brand Database — confirm no international mark conflict.")
    bullet(doc, "Nigerian Trade Marks Registry, EUIPO, UKIPO, JPO sweep for material jurisdictions.")
    bullet(doc, "Wayback Machine — verify no prior reputational use of the name.")
    bullet(doc, "Registrar visual check — confirm not parked, not in adult/gambling/regulated category.")
    bullet(doc, "Google + social handle availability (Instagram, LinkedIn, X, TikTok) — handles must be ownable.")
    bullet(doc, "Cost-of-acquisition budget for premium variants (.io, .ai, .energy, .capital).")
    bullet(doc, "Defensive registrations — purchase .com, .net, .org, country-code TLDs for top markets.")

    H(doc, "7. Defensive Registration Plan", 1)
    P(doc,
      "For each PRIMARY domain purchase, register the following defensive "
      "variants to prevent typosquatting, brand dilution and competitor cyber-"
      "squatting:")
    bullet(doc, ".com, .net, .org of the primary brand.")
    bullet(doc, ".africa and .co for African market protection.")
    bullet(doc, ".ai and .io for technology-adjacent BUs.")
    bullet(doc, "Top country-code TLDs: .ng, .za, .ke, .gh, .ae, .uk, .us.")
    bullet(doc, "Common misspellings of the primary brand.")
    P(doc, "Estimated annual defensive-registration budget: USD 25,000–40,000 "
           "across 15 division brands + 60+ BU brands.", color=GREY, italic=True, size=9)

    H(doc, "8. Companion Workbook", 1)
    P(doc,
      "Domain-Architecture.xlsx (this folder) contains the full machine-"
      "readable table — every candidate, TLD, RDAP code, registered-on date "
      "where available, recommendation flag and rationale — for handoff to "
      "domain procurement, brand counsel, and the Holdings Treasury function.")

    doc.save(OUT)
    print(f"WROTE {OUT}")


if __name__ == "__main__":
    main()
