# Project Phthisis — Gun Tiering Proposal (v2: Technology-based)

## Why v1 got scrapped

The first pass tiered guns by the ammo they fire, using your ammo material table. You're right that this breaks down — an Obrez and an AK-74 both happen to fire similar-tier rounds in that table, but one is a sawn-off improvised carbine and the other is a mass-produced select-fire service rifle. Caliber doesn't track "how advanced is this weapon." This version re-tiers all 204 guns by **design/technology sophistication** instead — action type, era, and role — completely independent of what ammo they take.

## The tier ladder

**Tier 0 — Improvised & Novelty.** Sawn-offs and field conversions (Obrez), flintlocks and caplock muzzleloaders (FuKa Model 15, Traditions Trapper .50cal), and joke/novelty guns (Kolibri pocket pistol, 'Hand'gun, LifeCard). Weak, slow, or literally not a real gun design — bottom of the ladder regardless of caliber.

**Tier 1 — Early Industrial Arms (pre-WWI/interwar manual actions).** Standard-issue bolt-action, lever-action, break-action, and pump firearms, plus early low-capacity revolvers — factory-made but manually cycled, no auto-loading. Kar98k, Springfield 1873 Trapdoor, Martini-Henry, Winchester 1897/1887, Mannlicher M1895, De Lisle Carbine, Welrod, low-caliber revolvers.

**Tier 2 — World War-Era Automatics.** The jump to auto-loading and automatic fire: first-generation SMGs (MP18/SMG08-18, Villar-Perosa, ZK-383, MAS-38), early automatic rifles and LMGs (Chauchat, Lewis Gun, MG08/15, MG42), and semi-auto service pistols of the same era (1911, Tokarev TT-33, Steyr M1912, Webley 1913).

**Tier 3 — Modern Service Arms.** The "this is what a standard modern military/police force issues" bracket, 1945–present: AK/M4/M16/G3/FAL/SCAR family rifles, MP5/UMP/Uzi-class SMGs, Glock/USP/CZ75-class pistols, and modern bolt-action precision rifles (M700, AWM, SSG69, AXMC/AXSR). This is the largest bucket by far (85 guns) — it's the baseline "competent modern weapon" tier.

**Tier 4a — Advanced & Specialist Arms.** Bullpups (AUG, QBZ-95, OTs-14 Groza, WA2000, DVL-10), PDWs and PDW-caliber platforms (P90, MPDR, Gepard PDW, KAC PDW, AR-57), select-fire machine pistols (Beretta 93R), and cutting-edge/next-gen rifles (SIG XM7/MCX Spear, RM277, AN-94, FN EVOLYS). These go beyond "standard issue" — niche, high-end, or genuinely next-generation designs.

**Tier 4b — Heavy Ordnance.** Anti-materiel rifles (.50 cal+: M107, AW50, GM6 Lynx, Tankgewehr M1918), miniguns, RPGs/rocket launchers, grenade launchers, and anti-tank ordnance (Fliegerfaust, Lunge Mine). Support/heavy weapons regardless of era — this stays a distinct bracket from small arms entirely, same as your original 4a/Anti-Materiel and 4b/Ordnance split.

**Utility (unranked)** — flamethrowers, the medic syringe, water guns, and the electric weapon. Gadget items, not combat progression; recommend leaving these always-available or on their own separate unlock rather than forcing them onto this ladder.

**Melee (unranked)** — the knife and the M1905 (no ammo, melee-type). Not part of gun progression.

## Distribution across all 204 guns

| Tier | Count |
|---|---|
| 0 — Improvised/Novelty | 7 |
| 1 — Early Industrial | 29 |
| 2 — World War Automatics | 23 |
| 3 — Modern Service | 85 |
| 4a — Advanced/Specialist | 31 |
| 4b — Heavy Ordnance | 19 |
| Utility | 8 |
| Melee | 2 |

Tier 3 is intentionally the biggest bucket — most packs (daffas, Suffuse, vanilla tacz) are built around modern military loadouts, so the bulk of the roster is "competent modern gun." Tiers 0–2 draw mostly from the two period packs (Apocalypse/bf1 WWI-WWII, ChocolateMan's fictional 1860s–1970s arms lineage).

## Calls I made that you should sanity-check

- **Modern bolt-action snipers (AWM, M700, SSG69, AXMC/AXSR, Kar98k excluded) → Tier 3, not Tier 1.** Action type is manual on all of these, but I split "pre-war military bolt rifle" (Tier 1) from "modern precision optics-ready sniper system" (Tier 3) since they're not comparable in-game. Kar98k stayed Tier 1 as the WWII service rifle it is.
- **ChocolateMan's `cbr11`/`cbr9` family** all carry explicit "Mod.19xx" years in their names (1875–1920) — I used those years directly rather than guessing, and kept them Tier 1 as a bolt/lever rifle family. `mu73`/`mua73` (Mod.1942, marked "MA" = presumably an automatic variant) went Tier 2 as WWII-era automatics, while `mu73m` ("MA90") reads as a modernized derivative and went Tier 3.
- **PDW-caliber SMGs (APC9, ARP9) → Tier 3, not 4a.** These fire standard 9mm rather than a proprietary PDW round, so I treated them as modern service SMGs rather than "advanced," reserving 4a for weapons whose whole design point is being specialist/next-gen (P90, MPDR, Gepard PDW).
- **`uji` ("Dual MAC10")** bumped to 4a for the akimbo dual-wield gimmick even though the base MAC10 is Tier 3 — flag if you'd rather keep it at 3 to match the base gun.
- **Tec-9, Python, Rhino .357, Saddam's Golden AK** — cosmetically or functionally quirky but not mechanically different from their tier-3 peers, so I left them at 3 rather than bumping for novelty alone.

## Recipe implication

Same as before: TACZ workbenches are cosmetic-only, so tiering has to live in what each recipe costs. This tier now has nothing to do with your ammo material table, so gun recipes and ammo recipes are two independent progressions — a Tier 3 gun doesn't necessarily need Tier 3 ammo materials to craft. If you want a coherent "smithing tech" cost curve for the gun side, I'd suggest a materials ladder scaled to sophistication (e.g. Tier 0–1: iron/wood/basic industrial scrap; Tier 2: steel + early alloys; Tier 3: steel/machined parts + electronics-adjacent components; Tier 4a: precision alloys + rare components; Tier 4b: heavy ordnance materials, likely reusing your existing tier-4 ammo materials since those are already framed as heavy/explosive). Let me know if you want me to draft that cost table next.

## Files

- `gun_index_techtier.csv` — all 204 guns with pack, gun id, weapon type, ammo, and the new tech tier, sorted by tier.
