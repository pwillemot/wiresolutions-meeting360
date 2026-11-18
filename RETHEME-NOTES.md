# Meeting 360 — Re-theme notes (Engie/AB InBev/solar → Wire Solutions / Tignes / steel cable)

The `index.html` text/data has been fully re-themed to **ArcelorMittal Wire Solutions**, hero
account **Tignes / Val d'Isère** (STGM), domain = **steel wire rope / cable**. Grounded in the
real demo-org records (Théo Kerdiles, the TS Panoramic dia 25 mm order, the Tichot épissure
€120K opportunity, the delivery case).

Backup of the original is at `index.html.engie-backup`.

## What changed in the text
- **Hero account:** AB InBev (Leuven brewery) → Tignes / Val d'Isère (STGM, French Alps)
- **Rep:** Sophie Laurent/Maréchal (inconsistent) → **Camille Fontaine** (unified)
- **Customer contacts:** Etienne Dubois → **Théo Kerdiles** (Responsable Technique & Grandes
  Inspections); Elena Vermeulen / Marco Rossi → **Timothé Lagache**
- **Account roster:** UCB → Méribel · Agfa-Gevaert → Val Thorens · Barco → Kittila Mine ·
  + Les Gets, Les Saisies, CERTEX Sweden, Obuasi, MENNENS, AB Cranes, ACE Winches
- **Domain:** solar + battery storage / CHP / metering → cable renewal & splice refurbishment,
  haul rope, épissure, diameter specs (dia 25 mm TS Panoramic, dia 47 mm Tichot 300 m / 2 splices)
- **Product name:** Energy & Utilities Cloud → Manufacturing Cloud; app title → "Wire Solutions Field 360"
- **Reference codes:** EC-2026-* → WS-2026-TIG-*
- Pre-meeting brief, Account 360 AI summary, and previous-notes blocks rewritten bespoke.

> The hero account name uses a typographic apostrophe (Val d'Isère, U+2019) on purpose — an ASCII
> apostrophe would break the single-quoted JS string literals. Do not "correct" it back to `'`.

## ⚠️ Media files still need swapping (binaries I can't regenerate)
The HTML now references these **new** filenames. Drop real Wire-Solutions/ropeway media into
`assets/` under these exact names (or re-point the refs back):

| New reference in index.html | Replace with |
|---|---|
| `assets/site-tignes.jpg` | Photo of the Tignes/Val d'Isère ski-lift site |
| `assets/site-meribel.jpg` | Méribel site |
| `assets/site-valthorens.jpg` | Val Thorens site |
| `assets/site-lessaisies.jpg` | Les Saisies site |
| `assets/Tignes.jpeg` | Account-360 hero image (ski-lift / haul rope) |
| `assets/theo-kerdiles.jpg` | Théo Kerdiles contact avatar |
| `assets/camille-fontaine.png` | Camille Fontaine (rep) avatar |
| `assets/Tignes1.jpeg` … `Tignes6.jpeg` | Visit-photo gallery (cable/sheave/splice shots) |
| `assets/PreMeetingBrief-tignes.mp3` | Re-recorded pre-meeting voice brief (Tichot story) |

Until these exist, those slots show broken/old images and the audio brief won't play. The
gallery thumbnails render CSS gradients, so the galleries still look fine without the jpegs.

## Known cosmetic leftovers (safe, invisible)
Internal JS variable/keys still contain old stems: `afxObs('chp')`, `agfaE`/`agfaS`, `wgE`, a
dormant `/chp unit/i` speech matcher. These are code identifiers, never shown to the user, and
renaming them risks breaking references — left as-is intentionally.

JS validated with `node --check` after the re-theme: **OK**.
