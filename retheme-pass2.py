import io
PATH = "/Users/pwillemot/claude-projects/ArcelorMittal/WireSolutions/meeting360/meeting360/index.html"
src = io.open(PATH, encoding="utf-8").read()

R = [
 # standalone first name in note bodies
 ("Etienne", "Théo"),
 # image filenames -> Tignes-named (media checklist will supply these files)
 ("Engie1.jpeg", "Tignes1.jpeg"),
 ("Engie2.jpeg", "Tignes2.jpeg"),
 ("Engie3.jpeg", "Tignes3.jpeg"),
 ("Engie4.jpeg", "Tignes4.jpeg"),
 ("Engie5.jpeg", "Tignes5.jpeg"),
 ("Engie6.jpeg", "Tignes6.jpeg"),
 ("Engie", "Tignes"),
 # missed combos / partials
 ("Agfa + Willemen", "Val Thorens + Les Saisies"),
 ("Agfa", "Val Thorens"),
 ("Willemen", "Les Saisies"),
 ("Barco", "Kittila Mine (Agnico Eagle)"),
 ("UCB", "Méribel (3 Vallées)"),
 # literal-ampersand consult label + solar partials
 ("Solar & Storage Consult", "Cable Supply Review"),
 ("Solar PV inverter metering", "Rope end-termination check"),
 ("solar + storage quote simulation", "cable + splice quote simulation"),
 ("solar + storage quote simulati", "cable + splice quote simulati"),
 ("Solar + splice refurbishment", "Cable renewal + splice refurbishment"),
 ("solar — scope", "cable renewal — scope"),
 ("solar paired to splice refurbishment", "cable renewal paired with splice refurbishment"),
 ("Solar PV", "Cable renewal"),
 ("solar", "cable renewal"),
 ("battery", "splice"),
 # residual CHP
 ("CHP", "haul rope"),
 ("GWh", "remontées mécaniques"),
 ("Mortsel", "Les Belleville"),
 ("Vermeulen", "Lagache"),
]
for f, r in R:
    src = src.replace(f, r)
io.open(PATH, "w", encoding="utf-8").write(src)
print("pass 2 done,", len(R), "rules")
