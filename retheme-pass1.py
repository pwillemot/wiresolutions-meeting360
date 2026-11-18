#!/usr/bin/env python3
# Re-theme the Meeting 360 prototype from Engie/AB InBev/solar -> ArcelorMittal Wire Solutions / Tignes / steel cable.
# Operates as ordered, literal string replacements on index.html. Order matters (longest/most-specific first).
import io, sys

PATH = "/Users/pwillemot/claude-projects/ArcelorMittal/WireSolutions/meeting360/meeting360/index.html"
src = io.open(PATH, encoding="utf-8").read()
orig_len = len(src)

# Each tuple: (find, replace). Applied in order with str.replace (all occurrences).
R = []

# ---- 1. Repeated narrative strings (do BEFORE token swaps so the long context matches) ----
# AI summary (appears 3x identically)
R.append((
 "Active solar + battery storage opportunity at the AB InBev Leuven brewery (~18 GWh/year). ~2,500 m² of usable roof identified; Etienne Dubois is championing a board-level business case. Target: payback 6–7 years with storage and coverage of the 6–9 pm evening peak. Action: run the bundle simulation and book the roof survey. FY26 energy supply agreement (EC-2026-0087) renewal in progress.",
 "Active cable renewal programme at the Tignes / Val d'Isère domain (STGM · ~80 remontées mécaniques). Just delivered the urgent dia 25 mm replacement cable for the TS Panoramic (on time). Théo Kerdiles has flagged a follow-up réfection d'épissure — 300 m of dia 47 mm cable with 2 splices on the Tichot appliance. Open opportunity €120K in Proposal/Quote. Action: send the Tichot splice-refurbishment quote and scope the next renewals across the domain."
))
# Previous notes (c360)
R.append((
 "Walked the roof with Etienne — ~2,500 m² usable for PV. Wants solar paired with battery storage and a bundle simulation for the board.",
 "Call with Théo — urgent order placed for the dia 25 mm replacement cable on the TS Panoramic (installation April). To follow up: réfection d'épissure 300 m dia 47 mm on the Tichot appliance (2 splices)."
))
R.append((
 "Etienne exploring on-site solar + battery storage to cut grid consumption and CO₂; keen to shave the 6–9 pm evening peak.",
 "Théo confirmed the Tichot appliance needs a splice refurbishment this cycle — 300 m dia 47 mm, 2 épissures. Lead time and splice certification are the key points."
))

# ---- 2. Reference codes ----
R.append(("EC-2026-0087", "WS-2026-TIG-047"))   # hero contract
R.append(("EC-2026-0042", "WS-2026-TIG-025"))   # main agreement
R.append(("EC-2026-001", "WS-2026-TIG-OPP"))
R.append(("CHP-TRND-007", "CABLE-TS-PANO-25"))

# ---- 3. People / contacts ----
R.append(("Etienne Dubois", "Théo Kerdiles"))
R.append(("Elena Vermeulen", "Timothé Lagache"))
R.append(("Marco Rossi", "Timothé Lagache"))
R.append(("Sophie Maréchal", "Camille Fontaine"))   # unify rep name -> single WS rep
R.append(("Sophie Laurent", "Camille Fontaine"))
R.append((">Sophie<", ">Camille<"))
R.append(("Good morning, Sophie", "Good morning, Camille"))
R.append(("heading to AB InBev", "heading to Tignes / Val d'Isère"))

# email domains / signoffs
R.append(("meridian-infra.com", "compagniedesalpes.fr"))
R.append(("jan.vercast@agfa.be", "contact@meribel-alpina.com"))
R.append(("s.laurent@arcelormittal.com", "camille.fontaine@arcelormittal.com"))
R.append(("Engie Belgium", "ArcelorMittal Wire Solutions"))

# ---- 4. Account names (hero + roster). Longest/most-specific first. ----
R.append(("AB InBev & Agfa-Gevaert", "Tignes / Val d'Isère & Val Thorens"))
R.append(("AB InBev", "Tignes / Val d'Isère"))
R.append(("ABInbev", "Tignes"))            # asset filename stem handled separately below
R.append(("Agfa-Gevaert", "Val Thorens (3 Vallées)"))
R.append(("UCB", "Méribel (3 Vallées)"))
R.append(("Barco", "Kittila Mine (Agnico Eagle)"))
R.append(("Northstar Components", "Les Gets (Portes du Soleil)"))
R.append(("Willemen Groep", "Les Saisies (Espace Diamant)"))
R.append(("Cedar Ridge Mining", "Obuasi Mine (AngloGold Ashanti)"))
R.append(("Summit Fabrication", "CERTEX Sweden"))
R.append(("Ironclad Forge", "ACE Winches"))
R.append(("Summit Distribution Co", "MENNENS Belgium"))
R.append(("Riverside Supply Depot", "AB Cranes"))
R.append(("Cascade Components", "AAA Wire Rope"))

# ---- 5. Towns / addresses ----
R.append(("Brouwerijplein 1, 3000 Leuven", "Rue de la Poste, 73320 Tignes"))
R.append(("Leuven brewery", "Tignes domain"))
R.append(("Leuven Site", "Tignes Site"))
R.append(("Leuven", "Tignes"))
R.append(("Allée de la Recherche 60, 1070 Brussel", "Route de Méribel, 73550 Méribel"))
R.append(("Septestraat 27, 2640 Mortsel", "Val Thorens, 73440 Les Belleville"))
R.append(("Beneluxpark 21, 8500 Kortrijk", "Kittilä, 99100 Finland"))
R.append(("Brussel-Hoofdstad", "Savoie (FR)"))
R.append(("Brussel", "Méribel"))
R.append(("Mortsel, BE", "Les Belleville, FR"))
R.append(("Kortrijk", "Kittilä"))
R.append(("Verviers, BE", "Les Saisies, FR"))
R.append(("Vlaanderen", "Savoie"))
R.append(("Gent", "Les Saisies"))
R.append(("Belgian enterprise accounts", "Alpine ropeway accounts"))

# ---- 6. Product / app naming ----
R.append(("Energy &amp; Utilities Cloud", "Manufacturing Cloud"))
R.append(("Energy & Utilities Cloud", "Manufacturing Cloud"))
R.append(("Engie Field Visit", "Wire Solutions Field 360"))
R.append(("manufacturing OEM & distributor accounts", "ropeway, mining & distributor accounts"))
R.append(("Midwest — IN, IL, OH", "Alpes & Export — FR, CH, Nordics"))
R.append((">Midwest<", ">Alpes & Export<"))
R.append(("Region / Territory: Midwest", "Region / Territory: Alpes & Export"))

# ---- 7. Task type labels ----
R.append(("Energy Asset Audit", "Cable Inspection"))
R.append(("Energy Supply QBR", "Account QBR"))
R.append(("Metering Check", "Splice Inspection"))
R.append(("Forecast Sign-off", "Forecast Sign-off"))
R.append(("New Distributor Onboarding", "New Distributor Onboarding"))
R.append(("Plant Walkthrough", "Site Walkthrough"))
R.append(("Energy Supply Agreement", "Cable Supply Agreement"))

# ---- 8. Domain language: solar/battery/CHP/metering -> steel cable/rope ----
R.append(("solar + battery storage", "cable renewal & splice refurbishment"))
R.append(("solar panels plus battery storage", "cable renewal and splice refurbishment"))
R.append(("solar paired with battery storage", "cable renewal paired with splice refurbishment"))
R.append(("solar PV & battery storage", "cable renewal & splice refurbishment"))
R.append(("solar PV & CHP", "cable renewal & splice"))
R.append(("Solar PV expansion", "Cable renewal programme"))
R.append(("Solar PV Array", "TS Panoramic haul rope"))
R.append(("solar PV", "cable renewal"))
R.append(("battery storage", "splice refurbishment"))
R.append(("Green Power Block GP-450", "Haul Rope dia 47 mm HR-47"))
R.append(("Green Gas Block GG-200", "Splice Kit dia 47 mm SK-47"))
R.append(("Flex Capacity CN-90", "Dia 25 mm Rope DR-25"))
R.append(("CHP cogeneration unit", "TS Panoramic haul rope"))
R.append(("CHP coolant leak", "splice wear flagged"))
R.append(("CHP Unit Outage", "Rope Inspection Finding"))
R.append(("CHP running hours", "rope operating hours"))
R.append(("CHP engine vibration mm/s RMS", "rope tension / wear (visual + MRT)"))
R.append(("CHP outage", "rope defect"))
R.append(("CHP uptime", "lift availability"))
R.append(("CHP units", "lift drive units"))
R.append(("three CHP units", "three lift drive stations"))
R.append(("steam-line insulation", "sheave liner wear"))
R.append(("Boiler-house submeter", "drive-station log"))
R.append(("HV metering", "rope end-termination"))
R.append(("submeter", "inspection log"))
R.append(("Submeter Cabinet", "Splice Zone"))
R.append(("Thermographic switchboard scan", "Magnetic Rope Test (MRT)"))
R.append(("winter peak load", "peak season inspection"))
R.append(("CHP", "haul rope"))

# energy metrics -> cable context (used in brief/360/KPI prose we didn't bespoke-rewrite)
R.append(("18 GWh/year", "~80 remontées mécaniques"))
R.append(("2,500 m² of usable roof", "300 m of dia 47 mm cable"))
R.append(("2,500 m²", "300 m"))
R.append(("6–9 pm evening peak", "seasonal inspection window"))
R.append(("payback 6–7 years with storage", "delivery ahead of the installation window"))
R.append(("6–7 years with storage", "ahead of the installation window"))
R.append(("1,200 MWh", "2 cables / season"))
R.append(("800 MWh", "300 m dia 47 mm"))
R.append(("1,000 MWh", "300 m"))
R.append(("720/800 MWh", "300 m"))
R.append(("264/400 MWh", "120 m"))
R.append(("400 MWh", "120 m"))
R.append(("MWh", "m"))
R.append(("€1,150/m", "€395/m"))
R.append(("€640/m", "€395/m"))
R.append(("roof survey", "site inspection"))
R.append(("bundle simulation", "quote simulation"))
R.append(("energy walkthrough", "cable inspection walkthrough"))
R.append(("Energy Review", "Technical Review"))
R.append(("Solar &amp; Storage Consult", "Cable Supply Review"))
R.append(("energy-intensity site", "high-usage ropeway site"))
R.append(("grid consumption", "cable wear"))

# apply
for find, rep in R:
    src = src.replace(find, rep)

io.open(PATH, "w", encoding="utf-8").write(src)
print(f"done. {orig_len} -> {len(src)} bytes. {len(R)} rules applied.")
