#!/usr/bin/env python3
"""Build docs/11_Season_1_Episode_Guide.md from data/season1_synopses.txt.

Each synopsis line is one new episode, in order. Airdates are assigned
Monday-Friday from Jan 3, 2005, skipping the locked preemption dates.
"""
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PREEMPTED = {
    date(2005, 1, 20): "No new episode: network coverage of the Presidential Inauguration",
    date(2005, 5, 30): "No new episode: Memorial Day",
    date(2005, 7, 4): "No new episode: Independence Day",
    date(2005, 9, 2): "No new episode: network news coverage of Hurricane Katrina",
    date(2005, 9, 5): "No new episode: Labor Day",
}
SWEEPS = [
    (date(2005, 2, 3), date(2005, 3, 2), "February Sweeps"),
    (date(2005, 4, 28), date(2005, 5, 25), "May Sweeps"),
]
MONTHS = {1: "JANUARY", 2: "FEBRUARY", 3: "MARCH", 4: "APRIL", 5: "MAY",
          6: "JUNE", 7: "JULY", 8: "AUGUST", 9: "SEPTEMBER"}


def main():
    lines = [l.strip() for l in (ROOT / "data" / "season1_synopses.txt").read_text().splitlines() if l.strip()]
    md = [
        "# BEYOND THE KINGDOM — Season 1 Episode Guide",
        "",
        "**Document 11 · Locked Canon · Episodes #0001–#0180**",
        "**Monday, January 3, 2005 – Friday, September 16, 2005 · 180 new episodes · Weekdays**",
        "",
        "Every episode's in-universe story day matches its airdate unless the synopsis says otherwise. "
        "Ages follow Document 02 and `tools/ages.py`.",
        "",
    ]
    ep, month, week = 0, None, None
    slots = []
    d = date(2005, 1, 3)
    while ep < len(lines):
        if d.weekday() < 5:
            if d in PREEMPTED:
                slots.append((d, None))
            else:
                ep += 1
                slots.append((d, ep))
        d += timedelta(days=1)
    for d, n in slots:
        if d.month != month:
            month = d.month
            md += ["---", "", f"## {MONTHS[month]} 2005", ""]
        wk = d - timedelta(days=d.weekday())
        if wk != week:
            week = wk
            label = f"### Week of {wk:%B} {wk.day}"
            for s, e, name in SWEEPS:
                if s <= d + timedelta(days=4 - d.weekday()) and d - timedelta(days=d.weekday()) <= e:
                    label += f" — *{name}*"
            md += [label, ""]
        day = f"{d:%a}., {d:%b}{'' if d.month == 5 else '.'} {d.day}"
        if n is None:
            md += [f"- **{day}** — *{PREEMPTED[d]}.*", ""]
        else:
            md += [f"- **#{n:04d} · {day}** — {lines[n - 1]}", ""]
    out = ROOT / "docs" / "11_Season_1_Episode_Guide.md"
    out.write_text("\n".join(md) + "\n")
    print(out, ep, "episodes")


if __name__ == "__main__":
    main()
