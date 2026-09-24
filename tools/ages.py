#!/usr/bin/env python3
"""Exact character ages on any in-universe date.

Usage: python3 tools/ages.py 2005-01-03 [name-filter]
"""
import csv
import sys
from datetime import date
from pathlib import Path

REGISTRY = Path(__file__).resolve().parent.parent / "data" / "birthdays.csv"


def age_on(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


def main():
    on = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else date(2005, 1, 3)
    flt = sys.argv[2].lower() if len(sys.argv) > 2 else ""
    with REGISTRY.open() as f:
        for row in csv.DictReader(f):
            if flt and flt not in row["name"].lower():
                continue
            born = date.fromisoformat(row["born"])
            died = date.fromisoformat(row["died"]) if row["died"] else None
            if died and died <= on:
                status = f"deceased {died:%b %d, %Y} (aged {age_on(born, died)})"
            elif born > on:
                status = "not yet born"
            else:
                status = f"age {age_on(born, on)}"
            print(f"{row['name']:<24} {row['family']:<11} b. {born:%b %d, %Y}  -> {status}")


if __name__ == "__main__":
    main()
