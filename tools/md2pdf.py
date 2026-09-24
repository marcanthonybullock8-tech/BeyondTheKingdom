#!/usr/bin/env python3
"""Convert the project's Markdown documents to styled PDFs.

Usage: python3 tools/md2pdf.py docs/*.md   (PDFs are written to pdf/)
"""
import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (HRFlowable, Paragraph,
                                Preformatted, SimpleDocTemplate, Spacer, Table,
                                TableStyle)

GOLD = colors.HexColor("#B8860B")
PURPLE = colors.HexColor("#3B1F5C")

ss = getSampleStyleSheet()
S = {
    "h1": ParagraphStyle("h1", parent=ss["Title"], textColor=PURPLE, fontSize=22, spaceAfter=10),
    "h2": ParagraphStyle("h2", parent=ss["Heading2"], textColor=PURPLE, fontSize=15, spaceBefore=12),
    "h3": ParagraphStyle("h3", parent=ss["Heading3"], textColor=GOLD, fontSize=12),
    "body": ParagraphStyle("body", parent=ss["BodyText"], fontSize=10.5, leading=14),
    "quote": ParagraphStyle("quote", parent=ss["BodyText"], fontSize=10.5, leading=14,
                            leftIndent=18, textColor=PURPLE),
    "cell": ParagraphStyle("cell", parent=ss["BodyText"], fontSize=9, leading=11),
    "code": ParagraphStyle("code", parent=ss["Code"], fontSize=9, leading=11,
                           backColor=colors.HexColor("#F4F0E6"), borderPadding=6),
    "footer": ParagraphStyle("footer", fontSize=8, alignment=TA_CENTER, textColor=colors.grey),
}


def inline(text):
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"<b><i>\1</i></b>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<i>\1</i>", text)
    return text


def build(md_path, out_dir):
    lines = Path(md_path).read_text(encoding="utf-8").splitlines()
    flow, i = [], 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if s.startswith("```"):
            block = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            flow.append(Preformatted("\n".join(block), S["code"]))
        elif s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                    rows.append([Paragraph(inline(c), S["cell"]) for c in cells])
                i += 1
            t = Table(rows, repeatRows=1, hAlign="LEFT",
                      colWidths=[6.8 * inch / len(rows[0])] * len(rows[0]))
            t.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E9E1F2")),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#999999")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]))
            flow += [t, Spacer(1, 8)]
            continue
        elif re.match(r"^\s*(-|\d+\.)\s", line):
            counters = {}
            while i < len(lines) and re.match(r"^\s*(-|\d+\.)\s", lines[i]):
                m = re.match(r"^(\s*)(-|\d+\.)\s(.*)", lines[i])
                level = len(m.group(1)) // 2
                counters = {k: v for k, v in counters.items() if k <= level}
                if m.group(2) == "-":
                    bullet = "\u2022" if level % 2 == 0 else "\u2013"
                else:
                    counters[level] = counters.get(level, 0) + 1
                    bullet = f"{counters[level]}."
                style = ParagraphStyle(f"li{level}", parent=S["body"],
                                       leftIndent=18 + level * 18,
                                       bulletIndent=6 + level * 18, spaceAfter=2)
                flow.append(Paragraph(inline(m.group(3)), style, bulletText=bullet))
                i += 1
            flow.append(Spacer(1, 4))
            continue
        elif s.startswith("# "):
            flow.append(Paragraph(inline(s[2:]), S["h1"]))
        elif s.startswith("## "):
            flow.append(Paragraph(inline(s[3:]), S["h2"]))
        elif s.startswith("### "):
            flow.append(Paragraph(inline(s[4:]), S["h3"]))
        elif s == "---":
            flow.append(HRFlowable(width="100%", color=GOLD, spaceBefore=6, spaceAfter=6))
        elif s.startswith(">"):
            flow.append(Paragraph(inline(s.lstrip("> ")), S["quote"]))
        elif s:
            flow.append(Paragraph(inline(s), S["body"]))
        else:
            flow.append(Spacer(1, 4))
        i += 1

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.grey)
        canvas.drawCentredString(letter[0] / 2, 0.5 * inch,
                                 f"BEYOND THE KINGDOM  ·  Page {doc.page}")
        canvas.restoreState()

    out = Path(out_dir) / (Path(md_path).stem + ".pdf")
    SimpleDocTemplate(str(out), pagesize=letter, leftMargin=0.85 * inch,
                      rightMargin=0.85 * inch, topMargin=0.8 * inch,
                      bottomMargin=0.8 * inch, title=Path(md_path).stem.replace("_", " "),
                      author="Beyond the Kingdom Writers' Room").build(
        flow, onFirstPage=footer, onLaterPages=footer)
    return out


if __name__ == "__main__":
    out_dir = Path(__file__).resolve().parent.parent / "pdf"
    out_dir.mkdir(exist_ok=True)
    for p in sys.argv[1:]:
        print(build(p, out_dir))
