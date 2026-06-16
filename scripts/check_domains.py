"""Live RDAP availability check for every domain candidate.

Writes 01_Branding-Domains/Domain-Architecture.xlsx with:
  Division | BU | Candidate | TLD | Full | RDAP status | Notes | Recommendation

RDAP returns:
  200 + body  -> registered (taken)
  404         -> available
  429 / 5xx   -> rate limited / unknown
"""
from pathlib import Path
import time
import urllib.request
import urllib.error
import json
import re

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

import afano_data as A
import domain_candidates as DC

OUT_XLSX = Path(__file__).parent.parent / "01_Branding-Domains" / "Domain-Architecture.xlsx"
OUT_JSON = Path(__file__).parent.parent / "01_Branding-Domains" / "Domain-Architecture.json"

UA = "AfanoGroupHoldingsBrandResearch/1.0 (+afanogroup.com)"
RDAP_BOOTSTRAP = "https://rdap.org/domain/"

# Cache so we don't hammer RDAP if names repeat.
_cache: dict[str, dict] = {}


def sanitize(name: str) -> str:
    return re.sub(r"[^a-z0-9-]", "", name.lower())


def rdap_check(fqdn: str, retries: int = 2, delay: float = 0.6) -> dict:
    if fqdn in _cache:
        return _cache[fqdn]
    url = RDAP_BOOTSTRAP + fqdn
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "application/rdap+json, application/json",
    })
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=12) as r:
                code = r.status
                body = r.read(8192)
                result = {"code": code, "status": "REGISTERED", "raw": body[:400].decode("utf-8", "replace")}
                try:
                    j = json.loads(body)
                    events = j.get("events") or []
                    for e in events:
                        if e.get("eventAction") == "registration":
                            result["registered_on"] = e.get("eventDate")
                except Exception:
                    pass
                _cache[fqdn] = result
                return result
        except urllib.error.HTTPError as e:
            if e.code == 404:
                result = {"code": 404, "status": "AVAILABLE", "raw": "not registered"}
                _cache[fqdn] = result
                return result
            if e.code in (429, 500, 502, 503, 504) and attempt < retries:
                time.sleep(delay * (attempt + 1) * 2)
                continue
            result = {"code": e.code, "status": f"HTTP {e.code}", "raw": str(e)[:200]}
            _cache[fqdn] = result
            return result
        except urllib.error.URLError as e:
            if attempt < retries:
                time.sleep(delay * (attempt + 1))
                continue
            result = {"code": 0, "status": "ERROR", "raw": str(e)[:200]}
            _cache[fqdn] = result
            return result
        except Exception as e:
            result = {"code": 0, "status": "ERROR", "raw": str(e)[:200]}
            _cache[fqdn] = result
            return result
    return {"code": 0, "status": "UNKNOWN", "raw": ""}


def division_name(num: int) -> str:
    for d in A.DIVISIONS:
        if d[0] == num:
            return d[1]
    return f"SBG {num}"


def status_fill(status: str) -> PatternFill:
    if status == "AVAILABLE":
        return PatternFill(start_color="C8E6C9", end_color="C8E6C9", fill_type="solid")
    if status == "REGISTERED":
        return PatternFill(start_color="FFCDD2", end_color="FFCDD2", fill_type="solid")
    return PatternFill(start_color="FFF9C4", end_color="FFF9C4", fill_type="solid")


def main():
    OUT_XLSX.parent.mkdir(parents=True, exist_ok=True)
    wb = Workbook()
    ws = wb.active
    ws.title = "Domain Architecture"

    headers = [
        "SBG #", "Division", "Level", "Business Unit / Division",
        "Candidate", "TLD", "Full Domain",
        "RDAP Code", "Status", "Recommendation", "Rationale",
    ]
    ws.append(headers)
    for c in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=c)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="0B1F3A", end_color="0B1F3A", fill_type="solid")
        cell.alignment = Alignment(vertical="center")

    rows_data = []  # for JSON dump

    # Map BU display name to SBG number.
    bu_to_sbg = {}
    for d in A.DIVISIONS:
        num = d[0]
        for bu_name, _ in d[6]:
            bu_to_sbg[bu_name] = num

    # 1) Division-level candidates.
    total = 0
    for num, candidates in DC.DIVISION_CANDIDATES.items():
        div = division_name(num)
        for i, (name, tld, rationale) in enumerate(candidates):
            sname = sanitize(name)
            fqdn = f"{sname}.{tld}"
            result = rdap_check(fqdn)
            total += 1
            rec = "PRIMARY PICK" if i == 0 else "alternate"
            ws.append([
                num, div, "Division", div,
                sname, tld, fqdn,
                result.get("code"), result.get("status"),
                rec, rationale,
            ])
            rows_data.append({
                "sbg": num, "division": div, "level": "Division",
                "business_unit": div, "candidate": sname, "tld": tld,
                "fqdn": fqdn, "rdap_code": result.get("code"),
                "status": result.get("status"), "recommendation": rec,
                "rationale": rationale,
                "registered_on": result.get("registered_on"),
            })
            # color the status cell
            r = ws.max_row
            ws.cell(row=r, column=9).fill = status_fill(result["status"])
            if i == 0:
                ws.cell(row=r, column=10).font = Font(bold=True)
            time.sleep(0.25)
            print(f"[{total:3d}] {fqdn:40s} -> {result['status']}")

    # 2) Business-Unit-level candidates.
    for bu_name, candidates in DC.BU_CANDIDATES.items():
        sbg = bu_to_sbg.get(bu_name, "?")
        div = division_name(sbg) if isinstance(sbg, int) else "?"
        for i, (name, tld, rationale) in enumerate(candidates):
            sname = sanitize(name)
            fqdn = f"{sname}.{tld}"
            result = rdap_check(fqdn)
            total += 1
            rec = "PRIMARY PICK" if i == 0 else "alternate"
            ws.append([
                sbg, div, "Business Unit", bu_name,
                sname, tld, fqdn,
                result.get("code"), result.get("status"),
                rec, rationale,
            ])
            rows_data.append({
                "sbg": sbg, "division": div, "level": "Business Unit",
                "business_unit": bu_name, "candidate": sname, "tld": tld,
                "fqdn": fqdn, "rdap_code": result.get("code"),
                "status": result.get("status"), "recommendation": rec,
                "rationale": rationale,
                "registered_on": result.get("registered_on"),
            })
            r = ws.max_row
            ws.cell(row=r, column=9).fill = status_fill(result["status"])
            if i == 0:
                ws.cell(row=r, column=10).font = Font(bold=True)
            time.sleep(0.25)
            print(f"[{total:3d}] {fqdn:40s} -> {result['status']}")

    widths = [7, 36, 14, 36, 22, 10, 28, 10, 14, 18, 48]
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = "A2"

    # Summary sheet.
    ws2 = wb.create_sheet("Summary")
    ws2.append(["SBG #", "Division", "Primary Division Domain", "Status"])
    for c in range(1, 5):
        cell = ws2.cell(row=1, column=c)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="0B1F3A", end_color="0B1F3A", fill_type="solid")
    for num, candidates in DC.DIVISION_CANDIDATES.items():
        if not candidates:
            continue
        primary = candidates[0]
        fqdn = f"{sanitize(primary[0])}.{primary[1]}"
        result = _cache.get(fqdn, {"status": "UNKNOWN"})
        ws2.append([num, division_name(num), fqdn, result["status"]])
        ws2.cell(row=ws2.max_row, column=4).fill = status_fill(result["status"])
    for i, w in enumerate([7, 38, 28, 14], 1):
        ws2.column_dimensions[get_column_letter(i)].width = w
    ws2.freeze_panes = "A2"

    wb.save(OUT_XLSX)
    OUT_JSON.write_text(json.dumps(rows_data, indent=2), encoding="utf-8")
    print(f"WROTE {OUT_XLSX}")
    print(f"WROTE {OUT_JSON}")


if __name__ == "__main__":
    main()
