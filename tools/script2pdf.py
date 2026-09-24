#!/usr/bin/env python3
"""Render a Beyond the Kingdom screenplay (.fountain-style) to an industry-format PDF.

Usage: python3 tools/script2pdf.py episodes/BTK-0001.fountain   (writes pdf/episodes/BTK-0001.pdf)

Markup (a small Fountain subset):
  Key: Value lines at the top  -> title page, ended by a line "==="
  # ACT ONE                     -> act header (new page)
  INT. / EXT. / INT./EXT. ...   -> scene heading (auto-numbered)
  ^INT. ...                     -> unnumbered sub-heading (intercut or continuous location)
  ~ Monday, January 3 ...       -> date/time stamp under a scene heading
  NAME / NAME (CONT'D) etc.     -> character cue (all caps, followed by dialogue)
  (parenthetical)               -> parenthetical inside dialogue
  ... TO: / FADE OUT.           -> transition (right-aligned)
  > centered text <             -> centered line
  !text                         -> forced action line
  ===                           -> page break
"""
import re
import sys
from pathlib import Path

from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (CondPageBreak, KeepTogether, PageBreak, Paragraph,
                                SimpleDocTemplate, Spacer)

ROOT = Path(__file__).resolve().parent.parent
FONT, SIZE, LEAD = "Courier", 12, 12
BASE = dict(fontName=FONT, fontSize=SIZE, leading=LEAD)

ST = {
    "action": ParagraphStyle("action", **BASE, spaceBefore=LEAD),
    "heading": ParagraphStyle("heading", fontName="Courier-Bold", fontSize=SIZE, leading=LEAD,
                              spaceBefore=LEAD * 2),
    "stamp": ParagraphStyle("stamp", fontName="Courier-Oblique", fontSize=SIZE, leading=LEAD),
    "character": ParagraphStyle("character", **BASE, leftIndent=2.2 * inch, spaceBefore=LEAD),
    "paren": ParagraphStyle("paren", **BASE, leftIndent=1.6 * inch, rightIndent=1.9 * inch),
    "dialogue": ParagraphStyle("dialogue", **BASE, leftIndent=1.0 * inch, rightIndent=1.5 * inch),
    "transition": ParagraphStyle("transition", **BASE, alignment=TA_RIGHT, spaceBefore=LEAD),
    "centered": ParagraphStyle("centered", **BASE, alignment=TA_CENTER, spaceBefore=LEAD),
    "act": ParagraphStyle("act", fontName="Courier-Bold", fontSize=SIZE, leading=LEAD,
                          alignment=TA_CENTER, spaceAfter=LEAD),
    "title": ParagraphStyle("title", fontName="Courier-Bold", fontSize=20, leading=24,
                            alignment=TA_CENTER),
    "titleline": ParagraphStyle("titleline", **BASE, alignment=TA_CENTER, spaceBefore=6),
}

HEADING_RE = re.compile(r"^(INT\.|EXT\.|INT\./EXT\.|I/E\.)\s")
CUE_RE = re.compile(r"^[A-Z0-9 .'\-\"#&]+(\s\((V\.O\.|O\.S\.|CONT'D|ON TV|ON PHONE|O\.C\.)\))*(\s\(CONT'D\))?$")


def esc(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)


def parse(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    meta, i = {}, 0
    while i < len(lines) and lines[i].strip() != "===":
        if ":" in lines[i]:
            k, v = lines[i].split(":", 1)
            meta[k.strip()] = v.strip()
        i += 1
    return meta, lines[i + 1:]


def build(path):
    meta, lines = parse(path)
    code = meta.get("Production", "").replace("Prod. #", "") or path.stem
    flow = [Spacer(1, 2.4 * inch), Paragraph(esc(meta.get("Title", "")), ST["title"]),
            Spacer(1, 0.3 * inch)]
    for key, label in (("Episode", ""), ("Event", ""), ("Air Date", "Air Date: "),
                       ("Production", ""), ("Story Day", "Story Day: ")):
        if key in meta:
            flow.append(Paragraph(esc(label + meta[key]), ST["titleline"]))
    flow += [Spacer(1, 1.6 * inch)]
    for key in ("Credit", "Draft"):
        if key in meta:
            flow.append(Paragraph(esc(meta[key]), ST["titleline"]))
    flow.append(PageBreak())

    scene, i, n, first_act = 0, 0, len(lines), True
    prev_blank = True
    while i < n:
        raw = lines[i]
        s = raw.strip()
        if not s:
            prev_blank = True
            i += 1
            continue
        if s == "===":
            flow.append(PageBreak())
        elif s.startswith("# "):
            if not first_act:
                flow.append(PageBreak())
            first_act = False
            flow.append(Paragraph(esc(s[2:].upper()), ST["act"]))
        elif HEADING_RE.match(s):
            scene += 1
            head = f"{scene}&nbsp;&nbsp;&nbsp;{esc(s)}"
            block = [Paragraph(head, ST["heading"])]
            if i + 2 < n and lines[i + 2].strip().startswith("~ "):
                block.append(Paragraph(esc(lines[i + 2].strip()[2:]), ST["stamp"]))
                i += 2
            flow.append(CondPageBreak(1.2 * inch))
            flow.append(KeepTogether(block))
        elif s.startswith("^"):
            flow.append(CondPageBreak(1.0 * inch))
            flow.append(Paragraph(esc(s[1:]), ST["heading"]))
        elif s.startswith("~ "):
            flow.append(Paragraph(esc(s[2:]), ST["stamp"]))
        elif s.startswith(">") and s.endswith("<"):
            flow.append(Paragraph(esc(s[1:-1].strip()), ST["centered"]))
        elif s.startswith("!"):
            flow.append(Paragraph(esc(s[1:].strip()), ST["action"]))
        elif s.endswith("TO:") or s in ("FADE OUT.", "FADE TO BLACK.", "INTERCUT WITH:",
                                        "END INTERCUT."):
            flow.append(Paragraph(esc(s), ST["transition"]))
        elif s == "FADE IN:":
            flow.append(Paragraph(s, ST["action"]))
        elif prev_blank and CUE_RE.match(s) and i + 1 < n and lines[i + 1].strip():
            block = [Paragraph(esc(s), ST["character"])]
            i += 1
            while i < n and lines[i].strip():
                d = lines[i].strip()
                style = ST["paren"] if d.startswith("(") and d.endswith(")") else ST["dialogue"]
                block.append(Paragraph(esc(d), style))
                i += 1
            # Keep a cue with at least its first line of dialogue.
            flow.append(KeepTogether(block[:2]))
            flow.extend(block[2:])
            prev_blank = False
            continue
        else:
            flow.append(Paragraph(esc(s), ST["action"]))
        prev_blank = False
        i += 1

    front_pages = 2  # title page + cast page are unnumbered front matter

    def page(canvas, doc):
        if doc.page <= front_pages:
            return
        canvas.saveState()
        canvas.setFont(FONT, SIZE)
        canvas.drawRightString(letter[0] - 1.0 * inch, letter[1] - 0.5 * inch,
                               f"{doc.page - front_pages}.")
        canvas.setFont(FONT, 9)
        canvas.drawString(1.5 * inch, letter[1] - 0.5 * inch,
                          f"BEYOND THE KINGDOM  #{code}")
        canvas.restoreState()

    out_dir = ROOT / "pdf" / "episodes"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{path.stem}.pdf"
    SimpleDocTemplate(str(out), pagesize=letter, leftMargin=1.5 * inch, rightMargin=1.0 * inch,
                      topMargin=1.0 * inch, bottomMargin=0.9 * inch,
                      title=f"Beyond the Kingdom {meta.get('Episode', '')}",
                      author="Beyond the Kingdom Writers' Room").build(
        flow, onFirstPage=page, onLaterPages=page)
    return out, scene


if __name__ == "__main__":
    for p in sys.argv[1:]:
        out, scenes = build(Path(p))
        print(out, f"{scenes} scenes")
