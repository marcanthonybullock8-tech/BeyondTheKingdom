# Beyond the Kingdom

A daytime soap opera writers' room. The series premieres (in-universe) Monday, January 3, 2005.

- `docs/` — series bible (Markdown source)
  - 01 Series Format Bible
  - 02 Character Bible
  - 03 Donohue Global Holdings
  - 04 Belmont Crest
  - 05 The Smilleys & Smilley International
  - 06 The Blackwater Syndicate & BSI
  - 07 Supporting Cast
  - 08 Cast Categories & Episode Counts
  - 09 World Building
  - 10 Season 1 Storylines
  - 11 Season 1 Episode Guide (generated from `data/season1_synopses.txt`)
- `pdf/` — PDF editions of every document, plus `Beyond_the_Kingdom_Complete_Series_Bible.pdf`
- `data/birthdays.csv` — every character's birthday
- `data/season1_synopses.txt` — the 180 Season 1 synopses, one per line
- `tools/ages.py` — exact ages on any date: `python3 tools/ages.py 2005-01-05`
- `tools/build_episode_guide.py` — assigns airdates, weeks, and sweeps, then writes Doc 11
- `tools/md2pdf.py`, `tools/combine_pdfs.py` — PDF builders (`pip install reportlab pymupdf`)
