"""Phase 03 — Governance Foundation deliverables.

Generates:
  - Holdings-Operating-Agreement.docx (Delaware C-Corp parent, multi-tier sub-entities)
  - Shareholders-Agreement.docx
  - Buy-Sell-Agreement.docx
  - Board-Charter-and-Committee-Charters.docx
  - Corporate-Secretariat-Playbook.docx
  - Conglomerate-Capital-Budget.xlsx (15 SBGs x 5-year capex/opex/headcount)
  - Multi-Jurisdiction-Registration-Guide.docx
  - Code-of-Conduct-and-Ethics.docx
  - Related-Party-Transaction-Policy.docx
"""
from pathlib import Path
from datetime import date
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import afano_data as A

BASE = Path(__file__).parent.parent / "03_Governance-Foundation"
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


# ---------- 1. Holdings Operating Agreement ----------
def operating_agreement():
    doc = new_doc()
    cover(doc, "Holdings Operating Agreement",
          "AFANO Group Holdings, Inc. — Delaware C-Corporation")

    H(doc, "Article I — Formation and Purpose", 1)
    P(doc, "1.1  Formation. AFANO Group Holdings, Inc. (the 'Corporation') is a "
           "Delaware C-corporation formed under the Delaware General Corporation "
           "Law for the purpose of operating as a multinational, diversified "
           "holding company.")
    P(doc, "1.2  Purpose. The Corporation's purpose is to acquire, hold, manage, "
           "finance, govern and divest equity interests in operating subsidiaries "
           "organized across 15 Strategic Business Groups (SBGs), to allocate "
           "capital across those SBGs, and to provide centralized treasury, audit, "
           "legal, ESG, investor relations, brand stewardship and corporate-"
           "development services to its subsidiaries.")
    P(doc, "1.3  Registered Office. The registered office is located in the State "
           "of Delaware; principal executive offices may be located at any address "
           "designated by the Board of Directors from time to time.")
    P(doc, "1.4  Term. The Corporation has perpetual existence.")

    H(doc, "Article II — Capital Structure", 1)
    P(doc, "2.1  Authorized Shares. The Corporation is authorized to issue Common "
           "Stock and one or more series of Preferred Stock as approved by the "
           "Board, subject to the limitations of the Certificate of Incorporation.")
    P(doc, "2.2  Classes. Common Stock is divided into Class A (one vote per "
           "share, founder-held) and Class B (ten votes per share, founder-"
           "supermajority for as long as the Founder remains Executive Chair). "
           "Class A is the class offered to outside investors and (at the Board's "
           "discretion) to the public on an IPO.")
    P(doc, "2.3  Preferred Stock. Preferred Stock may be issued in series to "
           "support strategic acquisitions, sovereign-investor partnerships, or "
           "private placements without dilution of common voting rights, subject "
           "to Section 3.3 below.")

    H(doc, "Article III — Governance", 1)
    P(doc, "3.1  Board of Directors. The Corporation is managed by a Board of "
           "Directors. The Board shall comprise no fewer than seven (7) and no "
           "more than fifteen (15) directors. At least one-third of directors "
           "shall be independent, and the chairs of the Audit, Risk, and "
           "Nominating & ESG committees shall be independent.")
    P(doc, "3.2  Officers. The Corporation's officers shall include a Chairman, "
           "a Chief Executive Officer, a Chief Financial Officer, a Chief Legal "
           "Officer, a Chief Risk Officer, a Chief Investment Officer, a Chief "
           "Sustainability Officer, and a Corporate Secretary.")
    P(doc, "3.3  Reserved Matters. Notwithstanding any general authority of the "
           "CEO, the following actions require Board approval and, where indicated, "
           "stockholder approval:")
    for item in [
        "Acquisition or disposition of any subsidiary, business or asset with enterprise value > USD 25,000,000.",
        "Issuance of any new class or series of equity.",
        "Incurrence of indebtedness > USD 50,000,000.",
        "Approval of the consolidated annual budget and 5-year capital plan.",
        "Initial public offering or dual-listing of the Corporation or any subsidiary.",
        "Material change to the brand-stewardship policy or House of Brands architecture.",
        "Adoption or material amendment of the ESG framework.",
        "Appointment or removal of the CEO, CFO, CLO, or external auditor.",
        "Any transaction with a Related Party above the de-minimis threshold (see Related-Party-Transaction-Policy.docx).",
    ]:
        bullet(doc, item)

    H(doc, "Article IV — Subsidiary Architecture", 1)
    P(doc, "4.1  Intermediate Holding Entities. Each of the 15 Strategic Business "
           "Groups is held through a wholly-owned intermediate holding entity "
           "(an 'IHE') incorporated in the jurisdiction most favorable to its "
           "operations and capital-raising plans. IHEs may be incorporated in "
           "Delaware, Mauritius (Africa hub), Singapore (APAC hub), UAE ADGM "
           "(MENA hub), Luxembourg or the United Kingdom.")
    P(doc, "4.2  Operating Subsidiaries. Each Business Unit beneath an IHE is "
           "separately incorporated in its country of principal operations. The "
           "Corporation may, at its discretion, list any operating subsidiary on "
           "any recognized stock exchange, sell it, contribute it to a joint "
           "venture, or wind it down — subject only to Article III reserved "
           "matters.")
    P(doc, "4.3  Brand Independence. Each operating subsidiary carries an "
           "independent brand and domain consistent with the Brand & Domain "
           "Architecture and the House of Brands policy.")

    H(doc, "Article V — Capital Allocation", 1)
    P(doc, "5.1  Centralized Treasury. Cash management, FX, hedging, intercompany "
           "lending and group-level debt issuance are centralized at the Holdings "
           "Treasury function.")
    P(doc, "5.2  Capital Allocation Discipline. The Corporation's capital is "
           "allocated annually across the 15 SBGs based on risk-adjusted return "
           "on invested capital (ROIC), strategic fit, and ESG performance. Each "
           "SBG must compete for capital — there is no automatic right of "
           "renewal.")
    P(doc, "5.3  Dividend Policy. The Corporation does not commit to a fixed "
           "dividend; cash is reinvested in subsidiaries, used for share "
           "repurchases, or returned to stockholders as the Board determines.")

    H(doc, "Article VI — Indemnification and Limitation of Liability", 1)
    P(doc, "Directors and officers are indemnified to the fullest extent "
           "permitted by Delaware General Corporation Law §§ 102(b)(7) and 145.")

    H(doc, "Article VII — Amendments", 1)
    P(doc, "This Operating Agreement may be amended by the affirmative vote of "
           "the holders of a majority of the outstanding voting power, except "
           "that Articles III (Governance), IV (Subsidiary Architecture), and "
           "V (Capital Allocation) require a two-thirds supermajority.")

    H(doc, "Signatures", 1)
    P(doc, "_________________________________________"); P(doc, "Founder / Executive Chair", color=GREY)
    P(doc, ""); P(doc, "_________________________________________"); P(doc, "Chief Executive Officer", color=GREY)
    P(doc, ""); P(doc, "_________________________________________"); P(doc, "Corporate Secretary", color=GREY)

    out = BASE / "Holdings-Operating-Agreement.docx"
    doc.save(out); print(f"WROTE {out}")


# ---------- 2. Shareholders Agreement ----------
def shareholders_agreement():
    doc = new_doc()
    cover(doc, "Shareholders Agreement",
          "Founder, Co-Founders, and Outside Investors")
    sections = [
        ("Article I — Parties and Purpose",
         "This Agreement governs the relationship among the holders of equity "
         "in AFANO Group Holdings, Inc. and is intended to align long-term "
         "interests, protect minority rights, and preserve the founder's "
         "stewardship of the conglomerate identity through the Class B "
         "supermajority structure."),
        ("Article II — Transfer Restrictions",
         "No party may transfer Class A or Class B shares without (a) compliance "
         "with the Buy-Sell Agreement, (b) right-of-first-refusal to the "
         "Corporation and then to other holders pro rata, and (c) consent of the "
         "Board where the transfer would result in a change of control."),
        ("Article III — Drag-Along and Tag-Along",
         "Holders of a majority of voting power may compel a sale of the "
         "Corporation; minority holders have a tag-along right to participate "
         "on the same terms."),
        ("Article IV — Pre-Emptive Rights",
         "Existing holders have a pro-rata right to participate in any new "
         "issuance, other than (i) issuances under the equity incentive plan, "
         "(ii) issuances in connection with a strategic acquisition, and "
         "(iii) issuances on an IPO."),
        ("Article V — Information Rights",
         "All holders receive (a) audited consolidated annual financials, "
         "(b) unaudited quarterly management accounts, (c) the annual capital "
         "budget, and (d) the ESG report."),
        ("Article VI — Founder Reserved Matters",
         "So long as the Founder holds Class B shares representing at least 10% "
         "of issued share capital, the Founder's affirmative vote is required "
         "for (i) any change to the House of Brands architecture, (ii) any "
         "transaction that would result in the AFANO master mark being applied "
         "to a customer-facing operating brand, and (iii) liquidation."),
        ("Article VII — Dispute Resolution",
         "Disputes are resolved by binding arbitration under the rules of the "
         "International Chamber of Commerce, seated in London or Singapore at "
         "the election of the claimant."),
    ]
    for title, body in sections:
        H(doc, title, 1); P(doc, body)
    out = BASE / "Shareholders-Agreement.docx"
    doc.save(out); print(f"WROTE {out}")


# ---------- 3. Buy-Sell Agreement ----------
def buy_sell_agreement():
    doc = new_doc()
    cover(doc, "Buy-Sell Agreement",
          "Triggering Events, Valuation, and Funding Mechanism")
    sections = [
        ("Article I — Triggering Events",
         "Trigger events: (a) death or disability of a holder, (b) involuntary "
         "transfer, (c) termination of employment for cause, (d) bankruptcy of a "
         "holder, (e) divorce settlement attempting to transfer shares, and "
         "(f) voluntary departure subject to the lock-up schedule."),
        ("Article II — Right and Obligation to Purchase",
         "Upon a trigger event the Corporation has a first-position option to "
         "purchase; if declined, remaining holders have a pro-rata option; if "
         "declined, the trigger holder's shares may be transferred subject to "
         "Article II of the Shareholders Agreement."),
        ("Article III — Valuation",
         "Fair market value is determined by (a) most recent agreed annual "
         "valuation if within 12 months, (b) failing that, the average of two "
         "independent valuations by Big Four firms appointed one by each side, "
         "and (c) failing convergence within 10%, a third 'baseball arbitration' "
         "valuer selects the closer of the two."),
        ("Article IV — Funding",
         "The Corporation maintains key-person life insurance on the Founder "
         "and CEO sufficient to fund a buyout on death. Other buyouts may be "
         "funded by cash, a five-year promissory note at SOFR + 300 bps, or a "
         "combination at the Corporation's election."),
        ("Article V — Founder Successor Plan",
         "On the Founder's death, disability, or retirement, the Class B "
         "supermajority converts to Class A on a 1:1 basis unless the Board "
         "(by 75% vote) confirms a successor who shall hold the Class B."),
    ]
    for title, body in sections:
        H(doc, title, 1); P(doc, body)
    out = BASE / "Buy-Sell-Agreement.docx"
    doc.save(out); print(f"WROTE {out}")


# ---------- 4. Board Charter + Committee Charters ----------
def board_charter():
    doc = new_doc()
    cover(doc, "Board Charter and Committee Charters",
          "Audit · Risk · Nominating & ESG · Compensation · Investment")

    H(doc, "Part 1 — Board Charter", 1)
    P(doc, "Purpose. The Board exists to set strategy, allocate capital, oversee "
           "management and risk, and steward the long-term value of AFANO Group "
           "Holdings on behalf of all stakeholders.")
    P(doc, "Composition.", bold=True)
    bullet(doc, "7-15 directors; at least one-third independent.")
    bullet(doc, "Independent Lead Director if Chair is non-independent.")
    bullet(doc, "Geographic diversity across the Group's footprint regions.")
    bullet(doc, "Sector expertise covering at least 5 of the 15 SBGs.")
    P(doc, "Meetings.", bold=True)
    bullet(doc, "Minimum 6 regular meetings per year; quarterly executive sessions of independent directors.")
    bullet(doc, "Annual strategy off-site with executive committee.")
    bullet(doc, "Annual board effectiveness review by external facilitator every third year.")

    H(doc, "Part 2 — Audit Committee Charter", 1)
    P(doc, "Composition: minimum 3 independent directors, all financially "
           "literate, at least one with formal accounting credentials. "
           "Responsibilities: oversight of financial reporting, internal "
           "controls, internal audit function, external auditor appointment "
           "and independence, whistleblower hotline.")

    H(doc, "Part 3 — Risk Committee Charter", 1)
    P(doc, "Composition: minimum 3 directors, one independent chair. "
           "Responsibilities: enterprise risk framework, geopolitical risk "
           "register, cyber risk oversight, insurance program review, climate "
           "transition risk.")

    H(doc, "Part 4 — Nominating & ESG Committee Charter", 1)
    P(doc, "Responsibilities: director nominations, succession planning, board "
           "evaluation, ESG strategy, sustainability reporting (GRI / SASB / "
           "TCFD), human-rights due diligence in the Group's supply chain.")

    H(doc, "Part 5 — Compensation Committee Charter", 1)
    P(doc, "Responsibilities: CEO and named-officer compensation, equity "
           "incentive plan, clawback policy, pay-ratio disclosure, "
           "performance-equity targets tied to ESG metrics.")

    H(doc, "Part 6 — Investment Committee Charter", 1)
    P(doc, "Responsibilities: review and approve acquisitions, divestitures, "
           "and material capital commitments above CEO authority. Reports "
           "monthly to the Board on M&A pipeline, exit pipeline, and the "
           "Capital Partners portfolio.")
    out = BASE / "Board-Charter-and-Committee-Charters.docx"
    doc.save(out); print(f"WROTE {out}")


# ---------- 5. Corporate Secretariat Playbook ----------
def secretariat_playbook():
    doc = new_doc()
    cover(doc, "Corporate Secretariat Playbook",
          "Board Mechanics · Subsidiary Governance · Statutory Filings")
    H(doc, "1. Role of the Corporate Secretary", 1)
    P(doc, "The Corporate Secretary is the steward of the Group's governance "
           "machinery. The Secretary reports administratively to the General "
           "Counsel and substantively to the Board Chair.")
    H(doc, "2. Annual Governance Calendar", 1)
    months = [
        ("Jan", "Board strategy off-site; prior-year audit kickoff."),
        ("Feb", "Audit Committee review of draft annual financials."),
        ("Mar", "Annual report; Form 10-K (if listed); ESG report draft."),
        ("Apr", "AGM notice and proxy materials issued."),
        ("May", "Annual General Meeting."),
        ("Jun", "Mid-year capital allocation review."),
        ("Jul", "H1 results; subsidiary AGM cycle begins."),
        ("Aug", "Risk register annual refresh."),
        ("Sep", "Director nominations and re-election cycle."),
        ("Oct", "5-year capital plan refresh; budget kickoff."),
        ("Nov", "Compensation Committee equity grant cycle."),
        ("Dec", "Board self-evaluation; statutory filing close."),
    ]
    for m, body in months:
        bullet(doc, f"{m}: {body}")
    H(doc, "3. Subsidiary Governance Standards", 1)
    P(doc, "Every operating subsidiary, regardless of jurisdiction, maintains:")
    bullet(doc, "Local board of at least 3 directors including one Holdings appointee.")
    bullet(doc, "Quarterly management accounts filed with Holdings Treasury.")
    bullet(doc, "Annual statutory accounts filed locally and copied to Holdings.")
    bullet(doc, "Local Company Secretary or equivalent with direct line to Group Corporate Secretary.")
    bullet(doc, "Resolutions register, minute book, share register, statutory registers.")
    bullet(doc, "Annual Group governance attestation signed by local Chair and Managing Director.")
    out = BASE / "Corporate-Secretariat-Playbook.docx"
    doc.save(out); print(f"WROTE {out}")


# ---------- 6. Multi-Jurisdiction Registration Guide ----------
def jurisdictions():
    doc = new_doc()
    cover(doc, "Multi-Jurisdiction Registration Guide",
          "Delaware · Nigeria · Mauritius · ADGM · Singapore · London")
    rows = [
        ("Delaware, USA",
         "Top-Tier Parent Domicile",
         "Delaware General Corporation Law: predictable case law, Chancery "
         "Court expertise, preferred by US institutional investors. Use for "
         "Group parent and US operating subsidiaries.",
         "Steps: file Certificate of Incorporation, appoint registered agent "
         "(CSC, CT Corp), federal EIN, Delaware franchise tax."),
        ("Nigeria",
         "Operating Heartland (CAC, FIRS)",
         "Corporate Affairs Commission registration as a private limited "
         "liability company. Required for direct local operations, federal "
         "and state government contracts, NCDMB pre-qualification for "
         "energy, and SBI accreditation for defense / security tenders.",
         "Steps: name reservation, MEMART, allotment of share capital, "
         "CAC certificate, FIRS tax registration, state SBIR equivalent, "
         "sector-specific licenses."),
        ("Mauritius (IFC)",
         "Africa Holding Hub",
         "Global Business Corporation (GBC) under the Financial Services "
         "Commission. Treaty network with 40+ African states, withholding-"
         "tax efficiency for pan-African dividend flows. Use as IHE for "
         "Africa-facing SBGs.",
         "Steps: appoint Management Company, Constitution, GBC application, "
         "Tax Residence Certificate annual renewal."),
        ("Abu Dhabi Global Market (ADGM)",
         "MENA Hub",
         "ADGM is a common-law financial free zone. Use as IHE for MENA "
         "financial-services, energy, and aerospace subsidiaries. 0% "
         "corporate tax for qualifying activities, English-language "
         "judiciary."),
        ("Singapore",
         "APAC Hub",
         "Singapore Private Limited Company under ACRA. Strong treaty "
         "network across APAC, sophisticated capital-markets ecosystem, "
         "preferred by sovereign wealth funds. Use as IHE for APAC-facing "
         "SBGs.",
         "Steps: ACRA BizFile registration, resident director, company "
         "secretary, registered office, post-incorporation tax filings."),
        ("United Kingdom",
         "International Capital Markets",
         "London is the natural secondary listing venue and a hub for "
         "specialty insurance, commodity trading, and PE/VC capital. Use "
         "Companies House Ltd for UK trading subsidiaries.",
         "Steps: Companies House incorporation, HMRC corporation tax "
         "registration, VAT if applicable, PSC register."),
    ]
    for jur, role, body, *steps in rows:
        H(doc, jur, 1)
        P(doc, role, bold=True, color=GOLD)
        P(doc, body)
        if steps:
            P(doc, steps[0], color=GREY, size=10)
    out = BASE / "Multi-Jurisdiction-Registration-Guide.docx"
    doc.save(out); print(f"WROTE {out}")


# ---------- 7. Code of Conduct ----------
def code_of_conduct():
    doc = new_doc()
    cover(doc, "Code of Conduct and Ethics",
          "Standards for Directors, Officers, Employees, and Partners")
    sections = [
        ("1. Our Standards",
         "AFANO Group Holdings expects every director, officer, employee, "
         "contractor and partner to act with integrity, honesty and respect "
         "in every jurisdiction in which the Group operates."),
        ("2. Anti-Bribery and Anti-Corruption",
         "The Group complies with the US Foreign Corrupt Practices Act, the "
         "UK Bribery Act 2010, and equivalent laws in every host country. No "
         "facilitation payments, no gifts above the de-minimis threshold, no "
         "political contributions without Board approval."),
        ("3. Sanctions and Trade Compliance",
         "The Group complies with OFAC, EU, UK and UN sanctions. Every "
         "counterparty above the screening threshold is cleared against the "
         "Group's third-party due-diligence platform before onboarding."),
        ("4. Human Rights and Labor",
         "Aligned with the UN Guiding Principles on Business and Human "
         "Rights. Zero tolerance for forced labor, child labor, and unsafe "
         "working conditions across the supply chain."),
        ("5. Data Protection and Privacy",
         "Compliance with GDPR, NDPR (Nigeria Data Protection Regulation), "
         "CCPA, PDPA, and equivalent regimes in every operating market."),
        ("6. Conflicts of Interest",
         "Directors, officers and senior employees disclose conflicts "
         "annually and as they arise; outside boards, investments and "
         "family relationships are recorded in the conflicts register."),
        ("7. Whistleblower Protection",
         "An independent, confidential third-party hotline operates 24/7 "
         "in the languages of all operating markets. Retaliation is "
         "grounds for immediate dismissal."),
        ("8. Environmental Stewardship",
         "Aligned with the Group's ESG Sustainability Framework and TCFD-"
         "consistent climate transition plan."),
        ("9. Sanctions for Breach",
         "Breach is grounds for disciplinary action up to and including "
         "termination, civil claim and referral to law-enforcement."),
    ]
    for title, body in sections:
        H(doc, title, 1); P(doc, body)
    out = BASE / "Code-of-Conduct-and-Ethics.docx"
    doc.save(out); print(f"WROTE {out}")


# ---------- 8. Related Party Transaction Policy ----------
def rpt_policy():
    doc = new_doc()
    cover(doc, "Related-Party Transaction Policy",
          "Identification · Disclosure · Approval · Disclosure")
    sections = [
        ("1. Definition", "A Related Party includes directors, named officers, "
         "5%+ shareholders, immediate family members of the foregoing, and any "
         "entity in which any such person holds a material economic interest."),
        ("2. Materiality Thresholds",
         "(a) De-minimis: under USD 100,000 — disclosure only. "
         "(b) Material: USD 100,000-1,000,000 — Audit Committee approval. "
         "(c) Significant: above USD 1,000,000 — full Board approval and "
         "independent fairness opinion."),
        ("3. Disclosure",
         "All Related-Party Transactions are disclosed in the annual report "
         "regardless of materiality."),
        ("4. Founder Companies",
         "Transactions between the Group and any company in which the Founder "
         "holds direct equity require an independent fairness opinion "
         "regardless of size, and unanimous independent-director approval."),
        ("5. Recusal", "The Related Party recuses from all discussion and vote."),
    ]
    for title, body in sections:
        H(doc, title, 1); P(doc, body)
    out = BASE / "Related-Party-Transaction-Policy.docx"
    doc.save(out); print(f"WROTE {out}")


# ---------- 9. Conglomerate Capital Budget XLSX ----------
def capital_budget():
    wb = Workbook()
    ws = wb.active
    ws.title = "5-Year Capital Plan"

    headers = ["SBG #", "Strategic Business Group",
               "Y1 Capex", "Y1 Opex", "Y1 HC",
               "Y2 Capex", "Y2 Opex", "Y2 HC",
               "Y3 Capex", "Y3 Opex", "Y3 HC",
               "Y4 Capex", "Y4 Opex", "Y4 HC",
               "Y5 Capex", "Y5 Opex", "Y5 HC",
               "5Y Total Capex", "5Y Total Opex"]
    ws.append(headers)
    for c in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=c)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="0B1F3A", end_color="0B1F3A", fill_type="solid")
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    # Indicative budget grid (USD millions, planning-stage estimates)
    # Conservative, high-capital SBGs get larger spend (energy, infra, mfg).
    plan = {
        1: (40, 30, 50,  60, 45, 80,  90, 60, 120,  120, 80, 160,  160, 100, 200),
        2: (200, 80, 120,  300, 120, 180,  450, 160, 240,  600, 200, 320,  800, 240, 400),
        3: (30, 40, 80,  50, 60, 130,  80, 90, 200,  120, 130, 280,  170, 180, 360),
        4: (150, 60, 90,  220, 90, 140,  320, 130, 200,  450, 180, 280,  600, 240, 360),
        5: (50, 35, 70,  80, 55, 110,  120, 80, 160,  170, 110, 220,  230, 145, 290),
        6: (60, 50, 100,  90, 75, 150,  140, 110, 220,  200, 150, 300,  280, 200, 400),
        7: (80, 60, 110,  120, 90, 170,  180, 130, 250,  250, 180, 340,  330, 240, 450),
        8: (20, 30, 60,  35, 45, 95,  55, 65, 140,  80, 90, 195,  110, 120, 260),
        9: (25, 35, 70,  40, 55, 110,  65, 80, 160,  95, 110, 220,  130, 145, 290),
        10: (45, 40, 80,  70, 60, 125,  105, 90, 180,  150, 125, 250,  205, 165, 330),
        11: (90, 55, 100,  140, 85, 155,  210, 125, 230,  300, 175, 320,  410, 235, 430),
        12: (180, 70, 110,  270, 105, 170,  390, 155, 250,  540, 215, 340,  720, 285, 450),
        13: (15, 35, 80,  25, 55, 130,  40, 80, 190,  60, 110, 260,  85, 145, 340),
        14: (10, 20, 40,  18, 32, 70,  28, 48, 110,  42, 68, 160,  60, 92, 220),
        15: (20, 25, 50,  35, 40, 85,  55, 60, 130,  80, 85, 180,  110, 115, 240),
    }
    for d in A.DIVISIONS:
        num, name, *_ = d
        cells = plan[num]
        row = [num, name]
        # capex y1..y5
        c1, o1, h1, c2, o2, h2, c3, o3, h3, c4, o4, h4, c5, o5, h5 = cells
        row += [c1, o1, h1, c2, o2, h2, c3, o3, h3, c4, o4, h4, c5, o5, h5]
        row += [c1+c2+c3+c4+c5, o1+o2+o3+o4+o5]
        ws.append(row)

    # Totals row
    last = ws.max_row
    total_row = ["", "TOTALS"]
    for col in range(3, 20):
        col_letter = get_column_letter(col)
        total_row.append(f"=SUM({col_letter}2:{col_letter}{last})")
    ws.append(total_row)
    for c in range(1, len(headers)+1):
        ws.cell(row=last+1, column=c).font = Font(bold=True)
        ws.cell(row=last+1, column=c).fill = PatternFill(start_color="E0E5EC", end_color="E0E5EC", fill_type="solid")

    widths = [6, 40] + [11]*15 + [16, 16]
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = "C2"

    # Assumptions sheet
    ws2 = wb.create_sheet("Assumptions")
    ws2.append(["Item", "Assumption"])
    for c in range(1, 3):
        ws2.cell(row=1, column=c).font = Font(bold=True, color="FFFFFF")
        ws2.cell(row=1, column=c).fill = PatternFill(start_color="0B1F3A", end_color="0B1F3A", fill_type="solid")
    assumptions = [
        ("Currency", "USD millions; FX hedged at Holdings Treasury."),
        ("Inflation", "5% blended across markets, 3% in OECD, 8-12% in frontier markets."),
        ("Discount Rate", "WACC 11% Group blended; SBG-level WACC adjusted for sector beta."),
        ("Capex Definition", "Tangible assets, plant, vehicles, IT systems, capitalized software."),
        ("Opex Definition", "Salaries, marketing, professional services, occupancy, technology."),
        ("Headcount (HC)", "Full-time equivalent; contractor headcount tracked separately."),
        ("Capital Allocation", "Annual ROIC review; no SBG is guaranteed renewal."),
        ("Funding Mix", "Initial: founder equity + non-dilutive grants. Years 2-3: senior debt at SOFR+250-400. Year 3+: bond program, sukuk, green bonds, sovereign co-investment."),
        ("Risk Reserve", "10% Group-level contingency held at Holdings."),
        ("Currency Hedge", "60-70% of forward 12-month FX exposure hedged."),
    ]
    for row in assumptions:
        ws2.append(row)
    ws2.column_dimensions["A"].width = 22
    ws2.column_dimensions["B"].width = 90

    out = BASE / "Conglomerate-Capital-Budget.xlsx"
    wb.save(out); print(f"WROTE {out}")


def main():
    BASE.mkdir(parents=True, exist_ok=True)
    operating_agreement()
    shareholders_agreement()
    buy_sell_agreement()
    board_charter()
    secretariat_playbook()
    jurisdictions()
    code_of_conduct()
    rpt_policy()
    capital_budget()


if __name__ == "__main__":
    main()
