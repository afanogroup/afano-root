"""Phase 04 — Operations Launch deliverables.

Generates:
  - 15-SBG-Capability-Statements.docx (one chapter per division)
  - Group-Marketing-and-Brand-Standards.docx
  - Shared-Services-SOPs.docx
  - Investor-Relations-Playbook.docx
  - ESG-Sustainability-Framework.docx
  - Cybersecurity-and-Data-Governance-Policy.docx
"""
from pathlib import Path
from datetime import date
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import afano_data as A

BASE = Path(__file__).parent.parent / "04_Operations-Launch"
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


def capability_statements():
    doc = new_doc()
    cover(doc, "Group Capability Statements",
          "15 Strategic Business Groups — Investor & Procurement Ready")
    P(doc, "Each Capability Statement is structured for use in: government "
           "procurement (SAM.gov, EU TED, AfDB, World Bank, UN), private-"
           "sector RFPs, sovereign-investor outreach, and IR roadshows. "
           "Statements are written in the third person and exclude forward-"
           "looking statements that could be construed as projections under "
           "SEC Rule 175.", italic=True, color=GREY)
    doc.add_page_break()

    for d in A.DIVISIONS:
        num, name, color_hex, sub, glyph, summary, bus = d
        color = RGBColor.from_string(color_hex.lstrip("#"))
        H(doc, f"SBG {num} — {name}", 1, color=color, size=20)
        P(doc, summary, italic=True, color=GREY)
        H(doc, "Mission", 2, color=color, size=13)
        P(doc, f"To deliver world-class {name.lower()} solutions across "
               "Africa, the Middle East and global frontier markets, "
               "operating as an independent, IPO-ready subsidiary of "
               "AFANO Group Holdings.")
        H(doc, "Core Capabilities (Business Units)", 2, color=color, size=13)
        for bu_name, services in bus:
            P(doc, bu_name, bold=True, color=NAVY)
            for s in services[:5]:
                bullet(doc, s)
        H(doc, "Differentiators", 2, color=color, size=13)
        bullet(doc, "Multinational holding-backed governance and capital access.")
        bullet(doc, "Independent operating brand and management team.")
        bullet(doc, "Cross-divisional supply-chain and customer synergies.")
        bullet(doc, "ESG-aligned operations (GRI / SASB / TCFD compliant).")
        bullet(doc, "Regulatory experience across multiple operating jurisdictions.")
        H(doc, "Target Markets", 2, color=color, size=13)
        bullet(doc, "Government and sovereign clients (federal, state, municipal).")
        bullet(doc, "Multinational corporates with regional expansion needs.")
        bullet(doc, "Multilateral institutions (World Bank, AfDB, IFC, UN agencies).")
        bullet(doc, "Private-sector enterprise clients across operating sectors.")
        H(doc, "Past Performance Themes", 2, color=color, size=13)
        P(doc, "Captured separately in the Past-Performance Annex maintained "
               "by the Business Development function; refresh quarterly.")
        doc.add_page_break()

    out = BASE / "15-SBG-Capability-Statements.docx"
    doc.save(out); print(f"WROTE {out}")


def marketing_standards():
    doc = new_doc()
    cover(doc, "Group Marketing and Brand Standards",
          "House of Brands · Endorsement Lockup · Voice & Visual System")
    sections = [
        ("1. House of Brands Architecture",
         "AFANO Group Holdings operates a House of Brands. The AFANO master "
         "mark is reserved for the holding company; operating subsidiaries "
         "trade under independent brands. See 02_Visual-Identity/AFANO-Brand-"
         "Guidelines.docx for the full visual system."),
        ("2. Endorsement Lockup",
         "Every operating subsidiary website carries an 'An AFANO Group Company' "
         "endorsement footer with the Network Node mark, linking to "
         "afanogroup.com. This is the only AFANO co-branding permitted in "
         "customer-facing contexts."),
        ("3. Brand Stewardship Function",
         "Located within the Holdings Office. Reviews all subsidiary creative "
         "above USD 50,000 in spend, all new product names, all domain "
         "purchases. Operates with a 5-business-day turnaround SLA."),
        ("4. Voice and Tone",
         "Group voice: authoritative, restrained, multinational. Avoid "
         "superlatives. Refer to subsidiaries by their independent name first; "
         "AFANO endorsement is footnote-level."),
        ("5. Approved Channels and Budgets",
         "Each SBG maintains its own marketing budget. Group-level marketing "
         "spend covers: IR communications, ESG report distribution, sovereign-"
         "investor outreach, master-brand awareness in Tier-1 financial press "
         "(FT, Wall Street Journal, Economist, Nikkei, Bloomberg)."),
        ("6. Trademark Registration",
         "Group Brand Stewardship maintains a global trademark portfolio. "
         "Every primary domain and brand is filed in: USPTO, EUIPO, UKIPO, "
         "JPO, Nigerian Trade Marks Registry, OAPI, ARIPO. Defensive "
         "filings extended to the top 20 host markets."),
        ("7. Crisis Communications",
         "Single Group spokesperson; subsidiaries do not comment on Group-"
         "level matters. Subsidiary crises are handled by the subsidiary's "
         "own communications function with Group oversight."),
    ]
    for title, body in sections:
        H(doc, title, 1); P(doc, body)
    out = BASE / "Group-Marketing-and-Brand-Standards.docx"
    doc.save(out); print(f"WROTE {out}")


def shared_services():
    doc = new_doc()
    cover(doc, "Shared-Services SOPs",
          "Finance · HR · IT · Procurement · Legal — the Keiretsu Model")
    H(doc, "Operating Model", 1)
    P(doc, "Following the Mitsubishi keiretsu pattern: each subsidiary "
           "retains operating autonomy and P&L responsibility, but consumes "
           "shared services from Holdings on a transfer-pricing basis. This "
           "preserves scale economics, governance consistency, and audit "
           "trail without burdening operating leaders with back-office "
           "overhead.")
    units = [
        ("Group Finance & Treasury",
         "Consolidated financial reporting, cash-pooling, FX hedging, "
         "intercompany lending, debt issuance, tax planning. Sub-units bill "
         "for service on a published rate card; rates updated annually."),
        ("Group HR",
         "Executive search for subsidiary CEOs and named officers, equity "
         "plan administration, expat mobility, compensation benchmarking, "
         "Group-wide DEI program. Subsidiaries run their own day-to-day HR."),
        ("Group IT",
         "Identity (Entra ID), endpoint management, SOC, network "
         "backbone, ERP (consolidated), email & collaboration platform. "
         "Subsidiaries pay a per-seat allocation."),
        ("Group Procurement",
         "Master agreements (cloud, telco, insurance, professional services, "
         "vehicles). Subsidiaries draw from master agreements; bypass "
         "requires CFO approval."),
        ("Group Legal",
         "M&A, financing, regulatory, IP, litigation oversight. "
         "Subsidiaries retain their own commercial counsel."),
        ("Group Internal Audit",
         "Reports directly to Audit Committee. Risk-based three-year audit "
         "cycle covering every operating subsidiary."),
        ("Group ESG",
         "GRI / SASB / TCFD reporting, materiality assessment, climate "
         "transition plan, supplier human-rights diligence."),
        ("Brand Stewardship",
         "See Group-Marketing-and-Brand-Standards.docx."),
        ("Investor Relations",
         "Quarterly results, annual report, AGM, ratings agencies, ESG "
         "investor calls. Subsidiaries route all IR inquiries through "
         "Group IR."),
    ]
    for u, body in units:
        H(doc, u, 1)
        P(doc, body)
    H(doc, "Transfer-Pricing Methodology", 1)
    P(doc, "Cost-plus 5-10% on direct service costs; benchmarked annually "
           "against independent comparable studies to satisfy OECD BEPS and "
           "host-country transfer-pricing rules.")
    out = BASE / "Shared-Services-SOPs.docx"
    doc.save(out); print(f"WROTE {out}")


def ir_playbook():
    doc = new_doc()
    cover(doc, "Investor Relations Playbook",
          "Pre-IPO · IPO · Post-Listing · Sovereign & Institutional Outreach")
    sections = [
        ("1. IR Function Charter",
         "The IR function is the Group's single voice to the capital markets. "
         "Reports to the CFO; works with the General Counsel on Regulation FD, "
         "Reg D, market-abuse, and inside-information protocols."),
        ("2. Annual IR Calendar",
         "Q1: Annual report, AGM, post-AGM roadshow (NY, London, Singapore, "
         "Dubai, Lagos). Q2: H1 trading update; Capital Markets Day. "
         "Q3: ESG report; sovereign-investor outreach. Q4: budget guidance; "
         "ratings-agency annual reviews."),
        ("3. Pre-IPO Stakeholder Mapping",
         "Tier 1 — Top 30 global institutional investors. Tier 2 — Top 15 "
         "sovereign wealth funds (GIC, Temasek, ADIA, Mubadala, NSIA, PIC, "
         "PIF, ADQ, NIC, etc.). Tier 3 — Top 20 Africa-focused funds. "
         "Tier 4 — DFIs (IFC, AfDB, EBRD, BII, FMO, DEG, Proparco)."),
        ("4. Disclosure Framework",
         "Aligned with NYSE/NASDAQ listing standards even pre-listing. "
         "Material non-public information is restricted to the insider list; "
         "blackout windows enforced 30 days before quarterly results."),
        ("5. Ratings-Agency Relationships",
         "Maintain dialogue with Moody's, S&P, Fitch and (for sukuk) IIRA. "
         "Annual review cycle even before debt issuance to build the "
         "credit story."),
        ("6. Activist and Hostile Defense",
         "Standby relationships with two M&A advisory firms, two PR firms, "
         "and one proxy-solicitor. Annual board education on activist "
         "defense tactics."),
        ("7. ESG-Specific Outreach",
         "Annual call with the PRI Steward signatories most heavily invested "
         "in conglomerate-discount stocks. Materiality refresh aligned with "
         "SASB sector standards across the 15 SBGs."),
        ("8. Subsidiary IPO Choreography",
         "When a Business Unit is IPO-ready, the Group decides between "
         "(a) spin-off (tax-free distribution), (b) carve-out (partial IPO, "
         "Group retains majority), or (c) trade sale. The Carve-Out Playbook "
         "covers operational separation."),
    ]
    for title, body in sections:
        H(doc, title, 1); P(doc, body)
    out = BASE / "Investor-Relations-Playbook.docx"
    doc.save(out); print(f"WROTE {out}")


def esg_framework():
    doc = new_doc()
    cover(doc, "ESG Sustainability Framework",
          "GRI · SASB · TCFD · UN SDGs · Net Zero by 2050")
    H(doc, "1. Vision", 1)
    P(doc, "AFANO Group Holdings commits to operating as a responsible "
           "multinational, achieving net-zero Scope 1 and 2 emissions by 2045 "
           "and Scope 3 by 2050, with science-based targets validated under "
           "the SBTi framework.")
    H(doc, "2. Reporting Standards", 1)
    bullet(doc, "Global Reporting Initiative (GRI) Universal Standards — annual report.")
    bullet(doc, "SASB sector standards mapped per SBG.")
    bullet(doc, "TCFD climate disclosures — physical & transition risk.")
    bullet(doc, "UN Sustainable Development Goals — priority SDGs 4, 7, 8, 9, 11, 13, 17.")
    bullet(doc, "CDP Climate, Water, Forests questionnaires annually.")
    bullet(doc, "EU Corporate Sustainability Reporting Directive (CSRD) — for EU-trading subsidiaries.")
    H(doc, "3. Material Topics by SBG", 1)
    for d in A.DIVISIONS:
        num, name, color_hex, *_ = d
        H(doc, f"SBG {num} — {name}", 2,
          color=RGBColor.from_string(color_hex.lstrip("#")), size=12)
        P(doc, "Material topics tracked by the ESG team; specifics maintained "
               "in the SASB-mapped materiality matrix updated annually.",
          color=GREY, size=9, italic=True)
    H(doc, "4. Governance", 1)
    P(doc, "ESG strategy is owned by the Chief Sustainability Officer (CSO) "
           "reporting to the CEO and to the Nominating & ESG Committee. "
           "Compensation for the CEO and named officers includes ESG-linked "
           "performance metrics representing 15% of long-term incentive.")
    H(doc, "5. Climate Transition Plan", 1)
    bullet(doc, "Baseline: Scope 1+2+3 inventory completed Year 1.")
    bullet(doc, "Years 2-5: 30% reduction in Scope 1+2 emissions intensity.")
    bullet(doc, "Years 5-10: 50% reduction; renewable energy in operations >70%.")
    bullet(doc, "Years 10-20: Scope 3 supply-chain decarbonization; net-zero Scope 1+2.")
    bullet(doc, "Years 20-25: Net-zero Scope 3; residual offsets via certified removals only.")
    H(doc, "6. Social and Human Rights", 1)
    P(doc, "Group commits to the UN Guiding Principles on Business and Human "
           "Rights. Annual human-rights due diligence audit covering Tier-1 "
           "and material Tier-2 suppliers across the 15 SBGs.")
    out = BASE / "ESG-Sustainability-Framework.docx"
    doc.save(out); print(f"WROTE {out}")


def cyber_policy():
    doc = new_doc()
    cover(doc, "Cybersecurity and Data Governance Policy",
          "Group-Wide Security Baseline · NIST CSF · ISO 27001 · NIS2 · GDPR · NDPR")
    sections = [
        ("1. Scope",
         "Applies to every Group company, every employee, every contractor "
         "and every system processing Group or customer data."),
        ("2. Frameworks",
         "Aligned with NIST CSF 2.0, ISO/IEC 27001:2022, EU NIS2 Directive, "
         "and where applicable PCI-DSS, HIPAA, SOC 2 Type II."),
        ("3. Group Security Operations Center",
         "24/7 SOC operated by the Cybersecurity Business Unit. Provides "
         "managed detection and response (MDR) to every operating subsidiary "
         "at no per-seat charge for high-risk SBGs (Financial Services, "
         "Healthcare, Government & Defense, Technology)."),
        ("4. Identity and Access Management",
         "Group-wide single-sign-on through Entra ID. Multi-factor "
         "authentication mandatory for all internal users; FIDO2 hardware "
         "keys required for privileged access."),
        ("5. Data Classification",
         "Four classes: Public, Internal, Confidential, Restricted. "
         "Restricted data (PII, M&A, IPO, customer financial) requires "
         "encryption at rest and in transit, access logging, and quarterly "
         "access reviews."),
        ("6. Data Protection",
         "GDPR, UK DPA, CCPA, NDPR (Nigeria), PDPA (Singapore), POPIA "
         "(South Africa), LGPD (Brazil). Data Protection Officer at "
         "Holdings level with regional deputies."),
        ("7. Incident Response",
         "Group IR plan with 1-hour notification SLA to Holdings CISO, "
         "4-hour escalation to General Counsel, 24-hour escalation to CEO. "
         "Quarterly tabletop exercises. Annual red-team engagement."),
        ("8. Third-Party Risk",
         "Every supplier above USD 50,000 per year completes the Group "
         "Cyber Risk Questionnaire; critical suppliers undergo annual "
         "independent attestation review (SOC 2, ISO 27001)."),
        ("9. Subsidiary IPO Carve-Out Considerations",
         "Where a subsidiary is being prepared for spinoff, cyber and data "
         "infrastructure must be separable on 24 months' notice. Plan "
         "maintained by Cybersecurity BU and reviewed annually."),
    ]
    for title, body in sections:
        H(doc, title, 1); P(doc, body)
    out = BASE / "Cybersecurity-and-Data-Governance-Policy.docx"
    doc.save(out); print(f"WROTE {out}")


def main():
    BASE.mkdir(parents=True, exist_ok=True)
    capability_statements()
    marketing_standards()
    shared_services()
    ir_playbook()
    esg_framework()
    cyber_policy()


if __name__ == "__main__":
    main()
