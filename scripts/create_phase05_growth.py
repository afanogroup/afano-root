"""Phase 05 — Growth & Expansion deliverables.

Generates:
  - M&A-Playbook.docx
  - International-Market-Entry-Guide.docx
  - Public-Private-Partnership-Playbook.docx
  - Government-Contracting-Master-Guide.docx
  - FDI-Inbound-and-Outbound-Strategy.docx
"""
from pathlib import Path
from datetime import date
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import afano_data as A

BASE = Path(__file__).parent.parent / "05_Growth-Expansion"
NAVY = RGBColor(0x0B, 0x1F, 0x3A)
GOLD = RGBColor(0xC8, 0xA0, 0x4A)
GREY = RGBColor(0x55, 0x55, 0x55)


def new_doc():
    doc = Document()
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(11)
    for s in doc.sections:
        s.top_margin = Inches(0.8); s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.9); s.right_margin = Inches(0.9)
    return doc

def H(doc, text, level=1, color=NAVY, size=None):
    p = doc.add_heading("", level=level)
    r = p.add_run(text); r.bold = True; r.font.color.rgb = color
    if size: r.font.size = Pt(size)

def P(doc, text, bold=False, italic=False, color=None, size=None, align=None):
    p = doc.add_paragraph()
    r = p.add_run(text); r.bold = bold; r.italic = italic
    if color: r.font.color.rgb = color
    if size: r.font.size = Pt(size)
    if align is not None: p.alignment = align

def bullet(doc, text):
    doc.add_paragraph(text, style="List Bullet")

def cover(doc, title, subtitle):
    P(doc, ""); P(doc, "")
    P(doc, "AFANO GROUP HOLDINGS", bold=True, color=NAVY, size=28, align=WD_ALIGN_PARAGRAPH.CENTER)
    P(doc, title, bold=True, color=NAVY, size=22, align=WD_ALIGN_PARAGRAPH.CENTER)
    P(doc, subtitle, italic=True, color=GOLD, size=13, align=WD_ALIGN_PARAGRAPH.CENTER)
    P(doc, f"Effective: {date.today().isoformat()}  ·  Version 1.0",
      color=GREY, size=10, align=WD_ALIGN_PARAGRAPH.CENTER)
    doc.add_page_break()


def ma_playbook():
    doc = new_doc()
    cover(doc, "M&A Playbook",
          "Source · Diligence · Negotiate · Close · Integrate")
    H(doc, "1. Strategic Rationale", 1)
    P(doc, "Acquisitions accelerate scale where organic growth is slower than "
           "market windows allow. Targets must satisfy three filters: "
           "(a) strategic fit with one of the 15 SBGs, (b) ROIC > Group "
           "blended WACC + 300 bps within 3 years, (c) cultural compatibility "
           "with the House of Brands model.")
    H(doc, "2. Sourcing Channels", 1)
    bullet(doc, "Bulge-bracket and regional M&A advisors retained on success-fee.")
    bullet(doc, "Sector-specialist boutiques (one per SBG).")
    bullet(doc, "Direct outreach to founder-owned businesses where succession is unresolved.")
    bullet(doc, "Distressed pipeline from restructuring advisors and DIP lenders.")
    bullet(doc, "Auction processes (selective participation only).")
    H(doc, "3. Diligence Workstreams", 1)
    for ws in [
        "Commercial — market, customers, competition, pricing.",
        "Financial — quality of earnings, working capital, hidden liabilities.",
        "Legal — corporate, IP, regulatory, litigation, sanctions.",
        "Tax — historical, transfer-pricing, structuring optimization.",
        "Operational — SCM, IT, real estate.",
        "HR — leadership, culture, retention, comp & benefits.",
        "ESG — climate, human rights, governance.",
        "Cyber — historical incidents, security posture, IP exfiltration.",
        "Insurance — adequacy, claims history.",
    ]:
        bullet(doc, ws)
    H(doc, "4. Deal Structuring", 1)
    P(doc, "Default: cash + earn-out tied to 2-year EBITDA performance. "
           "Use Group equity only where founder rollover meaningfully aligns "
           "interests. Preferred jurisdictions for SPV: Mauritius for Africa "
           "deals, Delaware for North America, Luxembourg for Europe, "
           "Singapore for APAC.")
    H(doc, "5. Integration Playbook", 1)
    bullet(doc, "Day 0: communications cascade, retention letters, brand-stewardship review.")
    bullet(doc, "Day 30: integration plan ratified; HR and finance integration kickoff.")
    bullet(doc, "Day 90: technology integration milestones; first MBR with Holdings CFO.")
    bullet(doc, "Day 180: synergy realization tracker live.")
    bullet(doc, "Day 365: post-mortem review with Investment Committee.")
    H(doc, "6. Brand Decisions Post-Close", 1)
    P(doc, "Default: retain target brand under House of Brands policy. "
           "Add the 'An AFANO Group Company' endorsement footer on website "
           "and corporate stationery only. Customer-facing brand transition "
           "is rare and requires Board approval.")
    out = BASE / "M&A-Playbook.docx"
    doc.save(out); print(f"WROTE {out}")


def market_entry():
    doc = new_doc()
    cover(doc, "International Market Entry Guide",
          "Africa · GCC · EU · North America · APAC · LatAm")
    regions = [
        ("West Africa (ECOWAS)",
         "Anchor: Nigeria. CAC registration, NCDMB for energy, NDIC for "
         "banking. Use Mauritius IHE for dividend efficiency. Local content "
         "rules require Nigerian board representation and local procurement "
         "thresholds in oil & gas (30-50%) and ICT (15-25%)."),
        ("East Africa (EAC)",
         "Anchor: Kenya. Nairobi as APAC-adjacent hub for impact-investment "
         "capital. Local incorporation under the Companies Act 2015. "
         "Tax incentives in SEZs (Mombasa, Konza)."),
        ("Southern Africa (SADC)",
         "Anchor: South Africa. JSE as a dual-listing venue post-IPO. "
         "B-BBEE compliance required for state-related procurement; "
         "minimum 30% black ownership for material government contracts."),
        ("North Africa / MENA",
         "Anchors: UAE (ADGM, DIFC), Saudi Arabia (NEOM, Riyadh). Free-zone "
         "incorporation for holdings; onshore LLC for trading. Saudi "
         "Tadawul main market for dual listing of Saudi-anchored "
         "subsidiaries."),
        ("European Union",
         "Anchor: Luxembourg (holdings) and Ireland (operational EU hub). "
         "EU CSRD and CSDDD apply to material EU-trading subsidiaries. "
         "Dublin and Paris as Tier-1 finance-talent markets."),
        ("United Kingdom",
         "Companies House registration. London for specialty insurance, "
         "PE/VC capital, commodity trading. AIM as a venue for early-stage "
         "subsidiary listings."),
        ("North America",
         "Delaware C-Corp for top-tier US holding entities. State-level "
         "registration as foreign corporation in states of operation. "
         "Federal SAM.gov, state SBIR equivalents, CFIUS review for "
         "inbound investment."),
        ("APAC",
         "Anchor: Singapore (holding hub). Operational footprints via "
         "Singapore Pte Ltd subsidiaries. India through GIFT City for "
         "financial services. Vietnam, Indonesia, Philippines via local "
         "JVs to satisfy ownership-cap rules."),
        ("Latin America",
         "Anchor: Mexico City (USMCA gateway) or São Paulo (Brazil scale). "
         "Local LLC (S de RL de CV / Ltda). FX controls and capital "
         "repatriation rules vary by country; treasury planning critical."),
    ]
    for r, body in regions:
        H(doc, r, 1)
        P(doc, body)
    out = BASE / "International-Market-Entry-Guide.docx"
    doc.save(out); print(f"WROTE {out}")


def ppp_playbook():
    doc = new_doc()
    cover(doc, "Public-Private Partnership Playbook",
          "Concessions · BOT/BOOT · Availability Payments · Hybrid Annuity")
    sections = [
        ("1. PPP Eligible Sectors at AFANO",
         "Infrastructure & Real Estate (SBG 4), Energy (SBG 2), Transport "
         "(SBG 7 Mobility), Healthcare (SBG 6), Education (SBG 8), "
         "Industrial parks (SBG 12), Government & Defense services (SBG 11)."),
        ("2. PPP Structuring Options",
         "(a) BOT — Build-Operate-Transfer; (b) BOOT — Build-Own-Operate-"
         "Transfer; (c) DBFOM — Design-Build-Finance-Operate-Maintain; "
         "(d) Availability Payment — government pays for service availability "
         "rather than user fees; (e) Hybrid Annuity — capital part-funded "
         "by government, balance by SPV."),
        ("3. SPV Architecture",
         "Each PPP is housed in a dedicated SPV — limited recourse, project-"
         "finance ring-fenced. AFANO Group Holdings appears as sponsor and "
         "minority equity; senior debt from DFIs (AfDB, IFC, EBRD, AIIB) "
         "and commercial banks."),
        ("4. Concession-Agreement Critical Terms",
         "Tariff/charge mechanism, force majeure, government step-in, "
         "termination payment formula, change-in-law protection, dispute "
         "resolution (ICC arbitration default)."),
        ("5. ESG & Social Licence",
         "Resettlement Action Plan (RAP), Indigenous Peoples Plan (IPP), "
         "Gender Action Plan (GAP), Community Development Agreement (CDA) "
         "aligned with IFC Performance Standards 1-8."),
        ("6. Track Record Building",
         "Bid as junior partner on early concessions to build past "
         "performance; transition to sponsor/lead on subsequent deals "
         "after 2-3 successful exits or concessions in operation."),
        ("7. Project Finance Toolkit",
         "Senior debt, subordinated debt, mezzanine, equity bridge, "
         "viability gap funding (VGF), credit guarantees from MIGA / "
         "ATI / AGF / GuarantCo."),
    ]
    for title, body in sections:
        H(doc, title, 1); P(doc, body)
    out = BASE / "Public-Private-Partnership-Playbook.docx"
    doc.save(out); print(f"WROTE {out}")


def govt_contracting():
    doc = new_doc()
    cover(doc, "Government Contracting Master Guide",
          "SAM.gov · EU TED · AfDB · World Bank · UN · Sovereign Procurement")
    H(doc, "1. Tier-1 Federal Markets", 1)
    bullet(doc, "United States — SAM.gov (System for Award Management). NAICS code mapping per SBG; CAGE code; SBA size standards.")
    bullet(doc, "Nigeria — Bureau of Public Procurement (BPP). NIPC pioneer status where applicable.")
    bullet(doc, "European Union — TED (Tenders Electronic Daily); thresholds per Directive 2014/24/EU.")
    bullet(doc, "United Kingdom — Contracts Finder, Find a Tender, Crown Commercial Service frameworks.")
    bullet(doc, "Canada — buyandsell.gc.ca; Standing Offers and Supply Arrangements.")
    bullet(doc, "Saudi Arabia — Etimad portal; local content (Saudization) thresholds.")
    bullet(doc, "UAE — Tejari, ADNOC, ADQ procurement portals.")
    H(doc, "2. Multilateral Procurement", 1)
    bullet(doc, "World Bank — eConsultant2; UNGM registration for SBD eligibility.")
    bullet(doc, "African Development Bank — AfDB MapAfrica / Mark2Win.")
    bullet(doc, "Asian Infrastructure Investment Bank (AIIB).")
    bullet(doc, "Islamic Development Bank — IsDB Sustainable Procurement.")
    bullet(doc, "European Bank for Reconstruction and Development — EBRD Procurement.")
    bullet(doc, "Inter-American Development Bank — IDB.")
    bullet(doc, "United Nations Global Marketplace (UNGM) — single registration covers most UN agencies.")
    bullet(doc, "Global Fund, GAVI, UNICEF Supply Division.")
    H(doc, "3. Bid Calendar Cadence", 1)
    P(doc, "Group Business Development maintains a rolling 18-month opportunity "
           "calendar pulling RFPs above USD 5,000,000 from every Tier-1 portal. "
           "SBGs review weekly; go/no-go decision at SBG MD level; "
           "Group oversight where Group brand or balance sheet is in scope.")
    H(doc, "4. Capability Statements", 1)
    P(doc, "Maintained in 04_Operations-Launch/15-SBG-Capability-Statements.docx. "
           "Tailored versions per SBG generated on demand by BD.")
    H(doc, "5. Past-Performance Strategy", 1)
    P(doc, "Build past performance through subcontracting to incumbent primes; "
           "graduate to prime on subsequent procurements once 3+ successful "
           "subcontracts close. Pursue mentorship relationships with incumbent "
           "primes via SBA Mentor-Protégé and equivalent host-country programs.")
    H(doc, "6. Joint Venture & Teaming Strategy", 1)
    P(doc, "Use JV vehicles where past performance, local content rules, or "
           "set-aside programs require local participation. Joint venture "
           "agreement template maintained by Group Legal.")
    out = BASE / "Government-Contracting-Master-Guide.docx"
    doc.save(out); print(f"WROTE {out}")


def fdi_strategy():
    doc = new_doc()
    cover(doc, "FDI Inbound & Outbound Strategy",
          "Sovereign Co-Investment · Treaty Protection · BIT Network")
    sections = [
        ("1. Inbound FDI — Sovereign Co-Investment",
         "Targeted sovereign-wealth co-investors per SBG: Energy (Mubadala, "
         "ADQ, Equinor, Petronas), Financial Services (GIC, Temasek, PIF), "
         "Infrastructure (CIC, NSIA, ADIA), Technology (PIF, Temasek, "
         "Mubadala Capital). Standard structure: minority equity at SBG-level "
         "or SPV-level; reserved matters list aligned with industry norms."),
        ("2. Bilateral Investment Treaty (BIT) Coverage",
         "Group operating entities are domiciled to maximize BIT coverage: "
         "Mauritius (45+ African BITs), UAE (Saudi-UAE-Egypt BITs), "
         "Singapore (broad APAC coverage), Netherlands (sunset clauses "
         "permitting), UK (extensive treaty network)."),
        ("3. Inbound DFI Funding",
         "International Finance Corporation (IFC), Proparco (France), "
         "BII (UK), FMO (Netherlands), DEG (Germany), EBRD (Europe/MENA), "
         "AfDB (Africa), IsDB (OIC member states), AIIB (Asia). Standard "
         "terms: long tenor (8-15 years), USD or local-currency, ESG "
         "conditionality."),
        ("4. Inbound Multilateral Guarantees",
         "MIGA (political risk), ATI (Africa), AGF (SME guarantee), "
         "GuarantCo (infrastructure debt). Layer guarantees into project-"
         "finance debt stacks to lower the cost of capital."),
        ("5. Outbound FDI — Group-Led",
         "Group-led acquisitions and greenfield builds across operating "
         "jurisdictions. Outbound deal flow runs through the IHE most "
         "tax-efficient for the target jurisdiction's holding structure."),
        ("6. Outbound Capital Repatriation",
         "Tax-efficient repatriation routes by region: Mauritius for Africa, "
         "Singapore for APAC, Luxembourg for Europe, UAE for MENA. Annual "
         "transfer-pricing study supports IP and management-fee flows."),
        ("7. FDI Stakeholder Mapping",
         "Federal and state IPAs (Investment Promotion Agencies) in every "
         "operating market. Annual visit cadence at IPA-CEO level."),
    ]
    for title, body in sections:
        H(doc, title, 1); P(doc, body)
    out = BASE / "FDI-Inbound-and-Outbound-Strategy.docx"
    doc.save(out); print(f"WROTE {out}")


def main():
    BASE.mkdir(parents=True, exist_ok=True)
    ma_playbook()
    market_entry()
    ppp_playbook()
    govt_contracting()
    fdi_strategy()


if __name__ == "__main__":
    main()
