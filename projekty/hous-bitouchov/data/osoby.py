# Přímí předci podle Kekulého čísel: 1 = výchozí osoba (ten, pro koho rodokmen děláme),
# otec osoby n má číslo 2n, matka 2n+1. Tedy 2 = otec, 3 = matka, 4–7 prarodiče, 8–15 pradědečci a prababičky…
#
# Každá osoba:  číslo: dict(n="Jméno Příjmení", y="1850–1910", st="doc", f=[...], r=[...], note="...")
#   n    jméno; ženy rodným příjmením („Anna Dvořáková“), u nejistého čtení otazník („Marie Špalková (?)“)
#   y    roky života pro přehledy: "* 1931" (žije / úmrtí neznámé), "1850–1910", "asi 1720–1785", "1680 – před 1740"
#   st   stav doložení:  doc  = doloženo matrikou (čteno přímo ze snímku)
#                        prob = pravděpodobné (shoda údajů, ale ne přímý doklad)
#                        fam  = údaj od rodiny / z rodinného dokumentu
#                        mh   = jen z cizího rodokmenu na internetu (MyHeritage, Geni…) – neověřeno
#                        unk  = neznámé (jen místo v rodokmenu)
#   f    fakta jako krátké věty: "* 12. 3. 1873 Hořice čp. 477", "kovář", "× 28. 1. 1897 Anna Stejskalová", "† 14. 5. 1902"
#        (* narození, × sňatek, † úmrtí – podle těchto značek web pozná sňatky a místa pro mapu)
#   r    klíče zápisů z data/zaznamy.json, které osobu dokládají
#   note poznámka: proč je údaj nejistý, rozpory, odkud se vzal
#   sex  jen u osoby 1: "M" nebo "F" (u ostatních plyne z čísla)
# Žijící lidé: jen jméno a rok narození (soukromí), note="Žijící – údaje jen základní."
# Neznámý otec nemanželského dítěte: dict(n="otec neuveden", st="unk", f=[], note="…")

P = {
    1: dict(n="Josef Petr Housa", y="* 1823", st="doc", sex="M",
            f=["* 7. 1. 1823 Bítouchov čp. 35 (farnost Semily)"],
            r=["semily_krest_josef_petr_housa_1823"],
            note="Výchozí osoba hledání (zadání: najít sourozence). V matrice psán Hauſa (Hausa), v pozdějším rejstříku Housa."),
    2: dict(n="Josef Housa", y="", st="doc",
            f=["× 20. 11. 1815 Příkrý, Anežka Špidlenová (podle uživatele; zápis v bozkovské matrice, ženich omylem jako Jan)", "sedlák z Bítouchova (1816, 1818; údaj uživatele)", "1823 a 1825 zapsán jako podruh v Bítouchově čp. 35"],
            r=["semily_krest_josef_petr_housa_1823", "bitouchov_umrti_josef_hausa_1841", "prikry_snatek_hausa_spidlenova_1815"],
            note="V Bítouchově žilo kolem 1810–1832 nejméně pět mužů jménem Josef Hausa; tento je manžel Anežky Špidlenové. Sňatek 1815 a stav „sedlák“ sdělil uživatel – zápis o sňatku jsem zatím sám nečetl. V zápisu z roku 1823 stojí „podruh“; 1816 je „Josef Hausa, sedlák z Bítouchova“ kmotrem u Špidlenů v Příkrém čp. 49 (N Bozkov sign. 4858, snímek 163)."),
    3: dict(n="Anežka Špidlenová", y="", st="doc",
            f=["z Příkrého čp. 49", "26. 1. 1825 kmotra v Bítouchově jako žena Josefa Hausy, podruha"],
            r=["semily_krest_josef_petr_housa_1823", "prikry_krest_anezka_marie_1818", "prikry_snatek_hausa_spidlenova_1815"],
            note="Nezemřela v Bítouchově (prohledáno 12/1824–1848) ani v Příkrém (1815–1840). Příjmení v křestním zápisu čteno nesnadno; tvar Špidlen podle jiných zápisů z Příkrého. Kmotrovství 1825: matrika N Semily sign. 5192, snímek 205 (zápis zatím nezařazen do dat)."),
    6: dict(n="Josef Špidlen", y="", st="doc", f=["Příkrý čp. 49"], r=["semily_krest_josef_petr_housa_1823"]),
    7: dict(n="Barbora Zemanová", y="", st="doc", f=["z Roztok (podle křtu 1818; 1823 čteno nejistě jako „ze Lhoty“)"], r=["semily_krest_josef_petr_housa_1823"],
            note="Místo původu: 1818 zřetelně „z Roztok“."),
}

# Rody = osm větví podle pradědečků a prababiček (čísla 8–15). Doplňte, jakmile je znáte:
# 8: ("Novákové", "Jedna věta, kdo to byli a odkud – ukáže se na webu u rodu."),
LINES = {
}

# Příbuzní mimo přímou linii (sourozenci, strýcové…): k = číslo předka, ke kterému patří.
# dict(k=16, n="Josef Novák (1865–1920)", t="Bratr Jana. Kovář v …", r=["klic_zapisu"])
SIDE = [
    dict(k=2, n="Anna Marie (* 2. 8. 1818 Příkrý čp. 40)", t="Pravděpodobně starší sestra Josefa Petra: matka Anežka, dcera Josefa Špidlena z Příkrého čp. 49 a Barbory Zemanové z Roztok, stejná kmotra. Otec je zapsán jako „Josef Křížek, sedlák z Bítouchova“ – žádný Křížek z Bítouchova si ale Špidlenovou nevzal (prověřeno), takže jde nejspíš o omyl písaře.", r=["prikry_krest_anezka_marie_1818"]),
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
    ("Měl Josef Petr Housa (* 1823) sourozence?",
     "Vyřešeno (uzavřeno 16. 11. 2026): sestra Anna Marie * 2. 8. 1818 Příkrý (otec omylem zapsán jako Křížek). Jiné děti páru nejsou v Bítouchově 1816–1832 ani v Příkrém 1816–1839; Bítouchov 1833–1835 neprohlédnut. Hledání ukončeno na pokyn uživatele."),
    ("Proč je otec Anny Marie (1818) zapsán jako Josef Křížek, a ne Hausa?",
     "Hypotéza: omyl písaře. Josefové Křížkové v Bítouchově měli manželky Dolenskou (čp. 2, 1807), Tulákovou (čp. 27, 1812) a Marii z Proseče (čp. 8); žádný si nevzal Špidlenovou (rejstřík O Semily 1797–1828, sňatky Příkrý 1795–1818). Matka i babička se shodují s Anežkou."),
    ("Kdy a kde zemřela Anežka Housová, roz. Špidlenová?",
     "Otevřené: mezi zemřelými není v Bítouchově 12/1824–1848 ani v Příkrém 1815–1840. Pravděpodobně odešla jinam nebo zemřela po roce 1848."),
    ("Je Josef Hausa, výměnník z čp. 35, † 2. 9. 1841 ve věku 80 let, otcem Josefa Petra?",
     "Hypotéza: stejný dům čp. 35 a stejné jméno; byl by však při sňatku 1815 asi 54letý – nejspíš vdovec, a pak by Josef Petr mohl mít nevlastní sourozence z prvního manželství. Rozhodne věk ženicha v zápisu o sňatku 1815."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
