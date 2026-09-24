# Beyond the Kingdom — Writers' Room Canon Lock

These rules are LOCKED. Read `docs/` before writing anything new.

## Standing instructions from the creator
- The in-universe present is **2005**, starting **Monday, January 3, 2005** (Episode #0001). The story moves forward from there.
- Tell the story as a **daytime soap opera**, through: screenplay-format, character-driven dialogue; in-world news/media articles and headlines; and 2005-era social media/internet fan reaction.
- Every scene has a **date and time** stamp. Character **ages must be exact** to their birthdays on that date.
- Keep it realistic, creative, dramatic, original, and consistent. **Continuity is critical.** Nothing resets.
- **Make a PDF of everything.** Write Markdown in `docs/`, then run `python3 tools/md2pdf.py docs/<file>.md` (output goes to `pdf/`). Requires `pip install reportlab`.
- The cast is primarily African American, with a few non-Black characters.
- The creator writes the characters. Don't invent core-character bios, birthdays, or backstory without the creator's input.
- **No SORAS, ever** (the creator decided this on 2026-09-24). Every character, including Emma, Victoria, and Lyric, ages in real time from their locked birthdays.

## Locked format (see docs/01_Series_Format_Bible.md)
- 250 episodes/year, Mon–Fri. Broadcast-season numbering (Sep–Sep). Episode numbers are cumulative.
  - Season 1: Jan 3 – Sep 16, 2005, Eps #0001–#0180. Season 2: Sep 19, 2005 – Sep 15, 2006, Eps #0181–#0430.
- 95% serialized / 5% standalone-feel specials.
- Daytime Soap Opera / Serial Drama. TV-14 (D,L,S,V). 60-min slot, about 42 minutes of story.
- No episode titles: Episode # + air date + Prod. #BTK-####. Landmark episodes get promo event names only.
- Script: 75–90 pages (target 80). Teaser + 6 Acts. 24–30 scenes (target 28).
- 2005 tech only: no Twitter, iPhone, Instagram, or streaming. Facebook is college-only. YouTube launches in 2005.

## Canon documents (docs/ → pdf/)
01 Format Bible · 02 Character Bible · 03 Donohue Global Holdings · 04 Belmont Crest · 05 Smilleys & Smilley International · 06 Blackwater Syndicate & BSI · 07 Supporting Cast · 08 Cast Categories & Episode Counts · 09 World Building · 10 Season 1 Storylines · 11 Season 1 Episode Guide (generated) · 12 Opening Title Sequence · 13 Ownership & Share Structures.
Every birthday lives in `data/birthdays.csv`. For exact ages on any date, run `python3 tools/ages.py YYYY-MM-DD [name]`.
Doc 11 is generated. Edit `data/season1_synopses.txt` (one line per episode, in order), then run `python3 tools/build_episode_guide.py`.
After editing docs, run `python3 tools/md2pdf.py docs/*.md && python3 tools/combine_pdfs.py` (requires reportlab and pymupdf).

## Key canon (summary. The docs win on any conflict.)
- Belmont Crest: One Belmont Crest Parkway NW, Atlanta, GA 30327 (NW Buckhead, off West Paces Ferry Rd, on the Chattahoochee bluffs). Founded 1958. 1,140 acres. The Donohue compound is on Sovereign Way.
- Donohue Global Holdings: $10T valuation. Family fortune over $2.5T. Alexander (1905–1999, died 11:58 PM Dec 31, 1999). Simone (b. Nov 2, 1910) is alive. DGH was formed Jan 3, 1966. Victor was DGH CEO from 1966 to 1996 and has been Chairman since 1996. Natasha has been **DGH CEO** since 1996. **There is NO "Donohue Hospitality Group."** The hotels are a DGH division, Donohue Hotels & Resorts.
- Victor & Joan married June 20, 1959. (The user's brief also said 1969. 1959 was chosen because Jasmine was born in 1960.)
- The Crown Trust / 1996 Codicil: Marc-Anthony is Heir Apparent. Vice Chair-designate at 25 (Jan 5, 2007). The Disgrace Clause is Martin's weapon. The "Line of Issue" clause makes the twins Donohue heirs.
- Smilleys (Chicago → Atlanta, Jan 2005): Odessa, Lucius, Vivienne, Desmond, Luke, Delphine, Esther, Quentin. Smilley Tower is at 3434 Peachtree Rd NE. Their estate, Ravenhurst, borders Belmont Crest.
- Feud origin: the Savannah Betrayal, March 7, 1952. Simone holds the Savannah Letter.
- Blackwater Syndicate founded Sept 29, 2000 (the origin is Grace's July 15, 2000 rescue). BSI founded April 16, 2002. Marc = "Sovereign." The Seven, the empty Eighth Chair, the Onyx Coin, the Ten Laws. In this universe there is no real "Blackwater USA."
- Twins conceived Sat Sept 1, 2001, at a Sag Harbor masquerade (Esther wore a gold mask). Marc has zero idea. Esther's cover story is IVF with an anonymous donor. She is engaged to Sebastian Kingsley.
- Amond & Harmony: Lyric was conceived after a one-night stand in July 2001. They co-parent through lawyers and "don't know each other." Marc is Lyric's godfather. Esther always avoids Marc.
- Arianna: Fulton County DA, sworn in Jan 1, 2005. She killed Darnell Divine (Harmony's brother) on Jan 1, 2002, and Marc hid it.
- Elxa: APD Chief, sworn in Dec 20, 2004, at 24. The "Nepotism Chief" controversy. She hunts Sovereign.
- Katrina (Mon Aug 29, 2005, Elxa's 25th birthday) is a planned arc for BSI and Blackwater in Simone's hometown.
- Master Secrets Ledger: Doc 02 (plus the Smilley ledger in Doc 05).

## Ownership (Doc 13)
- DGH has 100M shares at $100K each. The Crown Trust holds all 2M Class A shares, which is 100% of the votes and 2% of the equity. The family dynasty trusts hold 24%, for a family total of 26% ($2.6T). The Foundation holds 4.2% ($420B). Employees hold 9%. The rest belongs to outside non-voting investors. Under the "Blood Rule," in-laws own nothing.
- Key trusts: Simone holds 6%, which passes to the Heir Apparent's line when she dies. The Heir Apparent Trust holds 1% (sealed until Marc turns 25). The Future Issue Trust holds 1% ($100B) for Marc's children, which secretly means the twins.
- Donohue Enterprises: DGH holds 95% (all of the votes), the Enterprise Partners' Plan 4.5%, and the Bellmen's Trust 0.5%. Certificate No. 1 is a golden-share veto held by Simone that passes to the Heir Apparent.
- Smilley has 190M shares at $10K each. Class A (10% of the equity) holds all of the votes. The family owns 33.7% ($640B). Votes: Lucius 34, Odessa 20, Desmond 16, Esther 12, Luke 6, Delphine 6, Vivienne 4, Quentin 2. A CEO needs a majority, so Odessa is the kingmaker.

## Opening titles (Doc 12)
- There are 23 standard "Hall of Portraits" credits for the adult Contract and Featured cast. Sebastian joins at #46 and Julian Cross at #74 (credited under the alias all season).
- Unique signature sequences go to **Victor, Joan, Natasha, and Jasmine**, plus **Alvin from #90**. The order is Alvin, Jasmine, Natasha, Joan, then Victor last. Children appear in the closing credits.

## Season 1 locks (Docs 08, 10, 11)
- Season 1 is Eps #0001–#0180, Jan 3 – Sep 16, 2005. There are no new episodes on Jan 20 (Inauguration), May 30, Jul 4, Sep 2 (Katrina coverage), or Sep 5.
- Sweeps: February sweeps are #23–#42. May sweeps are #83–#102. The 100th episode is Mon May 23 ("Auburn Crown": the first kiss between Marc and Esther).
- **Alvin first appears in Ep #90 (Mon May 9, 2005).** Before that, he's only mentioned as being in Miami.
- **Theodore, Reginald (#176), and Connie (#177) appear only in finale week (Eps #176–180).** They become Core Contract Cast in Season 2. Until then the audience hears only Martin's side of his calls.
- Harlow is alive as "Julian Cross" (introduced #74). Peter rebuilt his face in 2001.
- Finale #180: Esther's wedding, then gunfire, then "The girls are yours!" Martin knows both Sovereign's identity and the twins' paternity.

## Episode scripts (episodes/ → pdf/episodes/)
- Each script is `episodes/BTK-####.fountain`, written in the Fountain-style markup documented in `tools/script2pdf.py`. Render it with `python3 tools/script2pdf.py episodes/BTK-####.fountain`.
- Length: 75–90 numbered pages. The title page and cast page are unnumbered front matter. Use 24–30 numbered scenes. Intercuts and continuous locations use `^` unnumbered sub-headings. Every scene gets a `~` date/time stamp. Characters' ages go in the action line on first appearance.
- Every episode also gets a media and fan companion, `episodes/BTK-####_Media_and_Fans.md`. Render it with `python3 tools/md2pdf.py --out pdf/episodes <file>`.
- **2005 internet voice:** no emoji, no @-mentions, no hashtags, no "don't @ me." Use emoticons and text: :) ;) <3 LOL lmao. The platforms are Blogger, LiveJournal, BlackPlanet, AOL boards, MySpace bulletins, and AIM away messages.
- Sri Lanka was UTC+6 in 2005, so local time was EST + 11 hours.

## Established in Episode #0001 (Mon Jan 3, 2005)
- The Smilley Tower lights came on at sunrise, 7:42 AM. Victor slept at his office. Joan wore the "Washington pearls" (1963), a signal of war that Simone understood. Simone threatened to wear "the other pearls" if the Smilleys come to Marc's birthday.
- Marc and Simone have breakfast every Monday at the Dowager House. Marc calls her "Gorgeous." Marc reads to kids at Egleston on Mondays and Thursdays (Keyonna, 7; DeAndre, 9; Nurse Tonya). He gave Lyric a pony named "Marc" for Christmas 2004. Harmony lives in a townhouse.
- The twins call Marc "Funny man." Victoria shares his laugh, and Bea saw it. Lucius and Esther call Victoria "Dividend." Lucius's tremor is seen only by Vivienne.
- Marc and Celeste are dating. Robert took a call from "C. RHODES" on the balcony, and Natasha noticed. The Smilleys got an automatic courtesy invitation to Marc's birthday under the 1961 bylaws.
- Esther's car idled at the Crown Gate at 8:31 AM. She declined Sebastian's call. Odessa told her the 1952 story.
- Marc told Amond about the gold mask: her laugh and the smell of jasmine, "3 years, 4 months, 2 days."
- **First Onyx Coin victim:** an unidentified Black man in his early 40s, shot at close range and still wearing a Rolex, found by a dog walker at 9:52 PM by Lake Clara Meer. Hughes leaked the coin to WBKG. Martin toasted the news from his Midtown loft.
- **The audience learns Marc is Sovereign** at the River Gate boathouse (11:41 PM): "I never gave that order... Wake up the Seven."
