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

## Established in Episode #0002 (Tue Jan 4, 2005)
- **The Piedmont Park victim is Lamar Whitlock** (b. Aug 12, 1961, d. Jan 3, 2005, aged 43). He was a Merriweather numbers runner, "a deacon" who drove a hearse part-time. His widow is Bernice. On Dec 10, 2004 (the day after the Smilley announcement), he deposited $20K in cash, source unknown.
- **The counterfeit tell:** real Blackwater coins have **7 crests** on the wave and are hand-cut. The park coin has **6** and is laser-cut from real onyx. The APD lab (Elxa, Jeremy, lab tech) and Ghost both know this. Elxa ordered it kept from the press, the FBI, Hughes, and "especially my family."
- Silas sent Mama Dee a black-lily wreath reading "SWEET AUBURN TRUCE — REST IN PEACE." Mama Dee reads it as a question: "Did you do this?" Sovereign's orders: Mama Dee takes Silas a sweet-potato pie Wednesday, swears on the Code, and promises proof **by Friday**. Saint keeps the streets cold. Roman finds the shooter ALIVE. Ghost finds the coin maker. Tobias traces the $20K. Silas and Mama Dee have known each other since age 12 (the Royal Peacock).
- Marc asked Ghost for Warren Hughes's phone records (Celeste let slip that "he" is high up at APD). Martin's one-sided call came at 12:14 AM ("Exactly as you said it would"). **Martin's suspect list circles ROBERT BULLOCK**, and he planted that suspicion with Natasha. Natasha asked Robert, who said, "I don't ask what they do at night."
- **Camille Rhodes is introduced**: senior partner and Robert's mistress (they've been involved since 1999). She wears Smile. Otis asked whether Bullock & Associates represents Blackwater. Nana Ruby noticed Robert's changed shirt.
- Joan asked Victor whether he called the mayor. He deflected: "Trust me on purpose." Winston: "The coffee's fresh, ma'am."
- Gloria will withdraw her petition in exchange for **one Sunday a month**, and Amond must ask Harmony himself. Gloria has held Lyric 11 times. Lyric likes greens. Amond still has the Tiffany gift Harmony didn't take.
- Esther kept Simone's invitation in her desk drawer (handwritten: "Welcome, neighbor. — S. T. D."). Odessa said "Wear red." Celeste is also wearing red. Esther saw Lucius's tremor. Yvette told Peter that Arianna hasn't cried since New Year's 2002.
- Simone's "other pearls" are black Tahitian pearls Alexander bought in Papeete in 1952. She has worn them three times: the night of the cross, the Nixon dinner, and Alexander's funeral. She calls Marc at midnight every birthday.
- The birthday ice sculpture is a crowned swan ("a duck that won the lottery").

## Established in Episode #0003 (Wed Jan 5, 2005 — Marc's 23rd birthday)
- **The dawn ritual:** every birthday since he was 12, Victor takes Marc to the shuttered Hotel Donohue (400 block of Auburn Ave) and tells him something new. This year Victor gave him the **brass key to Room No. 1**, Alexander's 9x11 first office (used until 1958). Duke Ellington stayed in Room 412.
- **Gifts:** a 1964 Patek Philippe from Robert and Natasha (1964 = the Civil Rights Act). A 1969 cherry-red Harley Shovelhead from Alvin, delivered by flatbed (Alvin is still unseen, "in Miami"). A "FUNNIEST MAN ALIVE" T-shirt from Grace. Arianna gave scales-of-justice cufflinks. **Martin gave a 1640 first edition of *The Prince***, inscribed: "May you always be loved and feared in exactly the right proportion."
- **Simone gave Marc Alexander's 1936 gold pocket watch**, engraved "A. J. D. — 1936 — They closed every door." Alexander wound it every morning for 63 years. Simone kept it in a drawer for 5 years. Marc's toast: "To the empty chairs. May we fill them all."
- Grace sang "Crown Me" with a new second verse for Marc ("Just a boy with a crown in his yesterdays").
- **Esther came to the Crown Gate in the red Valentino at 9:41 PM.** She saw Marc laughing on a BSI security monitor, recognized Victoria's laugh, and said "Turn the car around." Officer Dante Hollis took her message: thanks to Mrs. Donohue, and happy birthday to her great-grandson. **Celeste saw it** (the SMILLEY 1 tag) and agreed not to report it as a birthday favor. Bernadette and CrestWatch reported it anyway. Simone kept the black pearls closed: "Not tonight... She's afraid of something inside the house." **Marc froze the gate-camera image of Esther's face** and asked, "Why do you keep coming to my gate?"
- **Silas's deadline is Friday night.** Lamar's funeral is Sat Jan 8, 11 AM, at Greater Cascade Baptist. Silas carries his own fork (since 1964). Mama Dee broke two of his fingers at the Royal Peacock when they were 12.
- **Ghost confirmed Hughes is the leak**: a 10:03 PM Monday call from his personal cell to the WBKG assignment desk, plus two calls on Dec 21. There are 11 shops worldwide that can laser-cut onyx (Italy 4, Germany 2, Hong Kong 1, India 2, Israel 1, South Africa 1). **Roman found traffic-camera footage** at 10th & Piedmont: a white cargo van, in from 6:40 to 7:05 PM Monday, with plates stolen from a Macon church van, driven by a tall white man who "moves like a soldier."
- Marc hinted to Elxa to pull command-staff personal phone records from around 10 PM Monday ("Birthday magic"). Jeremy pointed out that this needs a subpoena signed off by the DA (Arianna). **Elxa saw Victor toast the Mayor** in Robert's study. Joan confronted Victor in the Rolls ("You are not even good at it") and walked into the Manor without him. The Mayor and Victor mentioned "conversations in November."
- **Harmony met Arianna at the party** and has an appointment Thursday at 10 AM. Arianna found the file **MP-2002-0014 (Darnell Divine)** in the cold-case cart and hid it in her bottom desk drawer. Harmony told Amond "not yet" (following Esther's advice: "Let them earn it"). Gloria and Harmony had a gentle powder-room talk: Lyric likes greens with lots of hot sauce, "that's all Curtis." Both lawyers will still go to the hearing.
- Natasha told Camille, "You're not wearing perfume tonight... How considerate." **Martin gave Celeste his card** ("the truth deserves a good publicist"). Robert warned Martin that "the jury will see you fishing."

## Established in Episode #0004 (Thu Jan 6, 2005)
- **Harmony and Loretta met Arianna at 10 AM.** The 2002 report (Det. R. Sams, closed as "INACTIVE — no leads" after 9 days) says Dee left a private residence on the 3100 block of Northside Dr NW on foot at about 1:45 AM on Jan 1, 2002. Arianna snapped a pen and got blue ink on her palm: "I won't stop." The case goes to Cold Case investigator **Carla Mims** (22 years at the GBI), with a call every two weeks. Loretta: "I'll call you Arianna when you bring my baby home." Arianna came from the **Hendersons' party on Northside** that night; Yvette now links Northside to her "flu." Marc (at the gazebo): "Looking is not the same as finding." His answer to "Where is he?": "Somewhere nobody will ever have to see him the way you saw him."
- **Elxa's canary trap** (Arianna's idea, after she declined the subpoena for lack of basis): at next Wednesday's command-staff meeting, each officer gets one fake detail. Tolbert: a second phone. Kemp: a partial print. Washington: a red car. Albright: the wife hired a PI. **Hughes: "The Chief believes the coin was a fake."**
- **Simone gave Grace and Mallory the green leather TOUSSAINT FORMULARY (S.T., 1931)**, with Joan present. Condition: "Beat the Smilleys." Simone never sold the formulas to the company (it has licensed them since the 1946 merger). Vivienne offered $2M through a Paris lawyer in 1976, and Simone sent back a jar of Rose Balm. **Rose Balm No. 7:** Kumasi shea, beeswax from Hollis of Thomasville, rose attar, and ONE drop of vetiver ("Alexander can hush"). Vivienne told Delphine to find out who in the family is working on beauty products.
- Simone told Joan that Victor did call the mayor ("Of course he did"). **Victor is banished to the library for 7 nights** (night 1 was Jan 6). Their previous record was 4 days, over the Nixon dinner in 1974.
- Tobias: Lamar's $20K was sequential new $100 bills shipped Dec 6 by the Jacksonville branch of the Atlanta Fed to **Chatham Savings & Trust, Savannah** (a private bank for shipping and port families). Amond caught Marc staring at Esther's gate-cam frame.
- Esther put Harmony down as preferred broker ("wear the navy suit Tuesday 9 AM") and asked Crowe whether the Chicago PIs are licensed in Georgia. Victoria sings "Crown Me" (on V-103). Odessa has seen Lucius's tremor since October and knows Vivienne knows. **Gloria told her lawyer Stanley to request a hearing** after Harmony's "not yet." Curtis sides with Harmony. Kiara: "extremely Belmont Crest."
- Martin met Celeste at the Flying Biscuit: "start with the courthouse." Nana Ruby told Natasha: "Ask him where the first shirt went." **Big E paid his monthly protection to Saint** at 2:47 PM ("We don't do deacons").

## Established in Episode #0005 (Fri Jan 7, 2005)
- **Second victim: Earl "Big E" Tuggle** (b. Oct 22, 1953, d. Jan 6, 2005, aged 51), killed at about 11:52 PM through a door chained open six inches. His right wrist was grabbed. **A fake coin (6 crests) was in his hand, and his real Blackwater protection coin (7) sat on the counter.** His niece Latrice found him at 6:12 AM. Elxa logged both coins but kept the second out of the command-staff report.
- **FBI SA Kate Doyle and SA Danny Reyes** (Operation Deep Water, opened Nov 15) arrived. Elxa made them get a court order for the evidence. Doyle: "They don't kill their own customers." Through Jasmine's contact at Justice, the Deep Water file names **Bullock & Associates, BSI, and Donohue Shipping (Port of Savannah)**.
- **Jeremy is Commander of the Blackwater Task Force** (dedicated floor, 12 detectives). Elxa's whiteboard reads "WHO BENEFITS?" She wrote "SUCCESSION?" and erased it. She left Arianna a voicemail explaining the two-coin theory.
- Harold Jackson (retired 3 weeks) on the Harlow case: "Some cases you work until you find out what the truth would cost." He won't say who told him to close it.
- **The shooter's white van was found burned** off Hwy 138 in Clayton County at 4:10 AM Friday.
- **Martin's second one-sided call:** "Two... I was nowhere near it... Exactly as you predicted... The Smilley brother. Wednesday." **Martin called Desmond, and they will meet Wednesday at 9 PM at the Ritz-Carlton Buckhead bar.** Desmond called Luke "nephew" with a pause.
- **The truce holds.** Silas came to Dee's Kitchen at 7 PM, his first visit since 1975, when he buried Dolores's husband and she "paid" him in cornbread for a year. Amond showed him the seven-crest coin next to APD photos of the 6 and the 7. Silas lent Big E $4K in 1985. **Merriweather and Blackwater men will stand side by side outside Lamar's funeral** (Sat 11 AM, Greater Cascade), and "we share" the killer when found. Silas recognized Marc eating chicken in his Aston Martin: "Strange city."
- Law Ten was applied: Big E's grandchildren (in Latrice's care) get rent, school, and Christmas until they're grown. Mama Dee and Saint delivered it.
- **Celeste counted cases at the courthouse:** Bullock & Associates represented 3 of 7 Harlow defendants (2000), 11 of 19 check-cashing gambling cases (2001–04), and 4 plaintiffs in the insurance suits after the 2004 fires. Martin: "You run it when you have one more number." Natasha asked Robert where the first shirt went ("dry cleaner on Peachtree Battle," which closes at 6) and closed the dressing-room door "politely."
- Quentin DJ'd his first set at Velvet ("Alvin Donohue's, unofficially"). Harmony's broker Donna Keel gave her until the end of February to close a sale. Mallory learned someone called the Kumasi shea co-op hours before she did, asking about "Toussaint shea."
- **Cliffhanger:** Arianna read Harmony's LJ thank-you, ran out barefoot, and called Marc from **the curve by the guardrail on Northside Drive**, her hand on the door handle: "He was just walking home."

## Established in Episode #0006 (Mon Jan 10, 2005; teaser Fri Jan 7, funeral Sat Jan 8)
- Marc held Arianna at the Northside guardrail (added spring 2002): "I will handle this. I've always handled this." Saint retrieved the Aston at 1:20 AM; the gatehouse sends Simone a daily list (since 1958).
- **Lamar's funeral:** 20 Merriweather men and 20 Blackwater men lined the steps. Silas arrived with Mama Dee on his crooked-fingered arm. Saint paid Bernice's mortgage through 2005 and the funeral. Doyle and Reyes photographed it; Doyle noted "DEE'S KITCHEN — WHITFIELD." **Teddy Merriweather** (26, Silas's sister's son) is the hothead.
- Robert retrieved the unwashed shirt from **Camille's Park Place condo** (34th floor) Saturday; she left the Smile on it deliberately. Nana Ruby found it Monday; **Natasha keeps it in a locked Hermès box** in her study desk. Natasha visited Camille with Henri's cheese straws; the card read "Enjoy them. You've already had everything else of his."
- **Carla Mims introduced** (GBI 22 yrs; thermos; beaded-chain glasses; pins the victim's photo on the wall, including one in Arianna's office). Dee left **Lamont Grier's** party (3100 block). Arianna signed the letter seeking guest lists for all Northside parties between West Paces and Moores Mill. Divine family interview set for Friday 4 PM.
- Egleston: "The Dinosaur Princess" (Marc wrote it). Doyle served Magistrate Carver's order; someone faxed Elxa's command-staff report to the FBI from a **Kinko's on Ponce**. The canary meeting moved to Thursday.
- **Harmony slapped Amond** at Phipps ("You think money fixes everything?"). Marc told Amond not to put BSI on Dee's case; Amond knows Marc's car was on Northside Friday night ("Not as brothers").
- Tobias: $60K cash left Chatham on Dec 9 from **Harbour Point Logistics** (Garden City customs broker, Donohue Shipping subsidiary since 1998; founder Gerald Pettaway, in a nursing home) via a "bearer" designation letter. Victor summoned Donohue Shipping's GC. Natasha ordered **Nathaniel Greer** (Director of Global Security, Donohue Hotels & Resorts) to track Robert's and Camille's reservations.
- Lucius (Parkinson's since 2003, per Doc 05) had his Emory follow-up set with his Chicago neurologist, Dr. Harrington. Vivienne learned of the "Toussaint shea" calls.

## Established in Episode #0007 (Tue Jan 11, 2005)
- **Family council vote (Class A):** Harmony named exclusive buyer's rep for the $2B Atlanta program, 1.5% ($30M gross; Keel takes half). Yes: Lucius (raised **left** hand), Vivienne, Esther = 50; No: Luke, Delphine = 12; Desmond abstained; Odessa's 20 made it **70**. Luke: "Over my dead body." Lucius: "Then we'll miss you." Quentin absent. Ashe Capital is down 31% since June.
- Esther to Harmony: "You're the only person in Atlanta who's never lied to me." Harmony kept her cubicle by the restroom. Marc learned (on speaker) that **Esther is Harmony's best friend**.
- **Victor learned "Office of the Chairman" letterhead and his stamp were used** in October to request the Harbour Point file (courier log 10/14/04, signed **"M."**) and on the Oct 15 bearer letter to Chatham. Marc has a copy of the bearer letter.
- Delphine traced the Kumasi calls to the **Olson Estate** line; Vivienne wants to own Grace & Glory's suppliers before launch. Mallory locked the Formulary in her wall safe after Martin offered to "keep it safe."
- Hughes needled Elxa about the library exile; she named the Peachtree Strangler. Harold on Hughes: "Hurt men leak… take his badge in a room with the door closed."
- Odessa learned Marc is Lyric's godfather; Victoria cried "FUNNY MAN!" in front of her. Amond sent white peonies ("Proud of you. — A.").
- Greer: Camille used Donohue hotels (Thursdays, cash) only until **Feb 2000**, then stopped. Esther's note to Simone: "It wasn't a lack of respect. It was the opposite."
- Carla found Bernadette's Jan 3, 2002 column: Arianna, 19, in silver at the **Hendersons' (3244 Northside)**, "the designated driver." She circled it.

## Established in Episode #0008 (Wed Jan 12, 2005 — Mama Dee's 54th)
- Birthday flowers: yellow roses in green ink ("A friend") and white calla lilies delivered by Otis in the **hearse** ("No black lilies. — S.M."). The Seven threw her a party: a Hobart dishwasher and a restored 1970 wedding photo (her photos were lost in a 1974 house fire).
- Simone keeps Esther's note on top of the **Savannah Letter** (Savannah postmark, March 1952) in her rosewood secretary.
- Yvette confronted Arianna about the "flu" and the missing car. Esther and Harmony walked the 400 block of Auburn; Esther saw Marc's Aston in the hotel alley and fled. **Alexander's 1951–53 ledger has pages for Mar 4–18, 1952 razor-cut.**
- Elxa answered Hughes at the Council budget hearing ($118K/month, from ending the Governor's Mansion detail). Lucius's Parkinson's is progressing (levodopa increased; ~18 months before it's hard to hide).
- Silas's man found Teddy lunched Monday at the Cleveland Ave Waffle House with a tall man "like Australian, but not." Peter is getting calls from **+52 998 (Clínica Esperanza, Cancún)**: someone asked about his 2001 patient.
- **Martin and Desmond met at the Ritz-Carlton Buckhead bar.** Martin gave Desmond Harrington's visit as a free "gift." Desmond: no Zurich clinic did Esther's IVF; no photos of her the first week of Sept 2001; two visits to one gate. Martin: "Tell me about the twins." Crowe's man photographed them.
- Victor narrowed "M." to **Marc or Martin**. Mallory met **Q** on Velvet's roof; he wrote a 312 number on her palm.

## Established in Episode #0009 (Thu Jan 13, 2005)
- Mallory got home at 3:07 AM; Peter waited on the stairs. Simone served Victor a "7" cake.
- **Canary trap:** five folders, different page sixes. **Hughes leaked "fake coin" to WBKG at 9:52 AM** (ran 10:04). Elxa kept him and made him **FBI liaison to Deep Water** ("everybody gets one mistake… you've had yours"), honoring Harold's "closed door."
- Martin to his operator: "Then we give them something they can't call fake… Not a deacon this time."
- Harmony was served at her desk: **hearing Mon March 14, 2005, 9 AM; evaluation by Dr. Miriam Kessler.** Gloria's hearing request dated from Jan 6; she won't withdraw but wrote an apology. Esther: "Let a judge say it," and gave Harmony her lawyer, Mr. Kincaid. Amond brought "Other Raffe" and promised never to testify against her.
- **Carla's four questions:** Arianna said she saw **no one walking** (the lie). She said she drove a Volvo. Carla requested the Volvo's DMV title history (about two weeks).
- Esther has Crowe's photos of Desmond with **Martin Olson**. Quentin told Desmond his car was seen at the Ritz. Greer: Camille's Jaguar XJ8 is in the **Colony Square garage** every Thursday 8 PM–6 AM (hotel not yet identified; Ep 32). Robert arrives separately in a rental.
- The Waffle House tape shows the tall man only from behind. Roman was sent to Savannah. Silas: the man rented from Hertz with a **New Zealand license**.
- Cliff: Arianna told Marc she lied; Marc: "Tell me everything about Carla Mims."

## Established in Episode #0010 (Fri Jan 14, 2005)
- **Kruger Precision Stoneworks, Johannesburg, order KPS-2004-1187:** 2,000 six-crest discs for **Harbour Light Holdings (Pty) Ltd, Cape Town**, "Do NOT correct to seven," shipped Oct 22, 2004 Durban→Savannah on the Donohue Shipping vessel **MV Sovereign Dawn**; docked Nov 9, cleared Nov 11, consigned to Harbour Point. How Ghost got it is never shown. "He's planning a war."
- **The customs attorney of record is Bullock & Associates** (routine: B&A has filed every Donohue Shipping entry since 1991 via paralegal Doris in Savannah). Marc had Robert quietly pull the Harbour Point filings.
- **Chatham microfiche:** the Dec 9 withdrawal was by **"Cameron James Kerr," New Zealand license, b. 1968** (an alias). Mama Dee gave Silas the name; the truce holds "as long as he wants it to," and "we share." The tall man calls Teddy on **Monday**; Teddy will tell Silas.
- FBI lab: fake stone is from the **Northern Cape, South Africa**, machine-cut; real coins are hand-cut Brazilian onyx. Hughes carried it straight to Elxa. Condo lobby tape: the tall man passed toward the park at **6:48 PM Jan 3**. **Elxa and Doyle's truce** at Manuel's Tavern ("Military").
- Martin told Victor he requested the Harbour Point file for a Q4 portfolio review and put it on Victor's letterhead via Mrs. Ames; he denies the bank letter. Marc slipped and mentioned "the bank letter" to Victor, who "decided not to ask."
- Smilley holds an option on **441 and 443 Auburn Ave** (Leroy Reese: "Auburn Avenue remembers who tipped"). Lucius blessed the Auburn push; Esther hid Desmond's meeting from him.
- Carla learned **Dee always walked south on Northside to the Texaco at West Paces** to call Calvin ("only road down") and took Dee's pager. **Marc refused Ghost's idea to plant a false witness: "Then we let her look."**
- Peter told Jasmine he operated in Cancún for nine days in summer 2001 on a cash patient he won't name. Robert brought Natasha Henri's cheese straws (he knows). Q played "Lovin' You" from a car outside the Olson gate; Mallory is grounded two weeks.
- **CYRUS KNOX introduced** (first appearance): on a Midtown garage roof at 11:48 PM, Martin slid him a thick envelope: "Again. Bigger." Knox: "Someone they can't ignore." Martin: "Someone they can't call a criminal." "Cameron Kerr" has left the country. Sets up Ep 14 (Det. Terrence Oakes).
