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
            f=["podruh v Bítouchově čp. 35 (1823)"],
            r=["semily_krest_josef_petr_housa_1823"],
            note="V Bítouchově žilo kolem 1810–1832 nejméně pět mužů jménem Josef Hausa; tento je doložen jen jako manžel Anežky Špidlenové. Sňatek zatím nenalezen."),
    3: dict(n="Anežka Špidlenová", y="", st="doc",
            f=["z Příkrého čp. 49", "26. 1. 1825 kmotra v Bítouchově jako žena Josefa Hausy, podruha"],
            r=["semily_krest_josef_petr_housa_1823"],
            note="Příjmení v křestním zápisu čteno nesnadno; tvar Špidlen podle jiných zápisů z Příkrého. Kmotrovství 1825: matrika N Semily sign. 5192, snímek 205 (zápis zatím nezařazen do dat)."),
    6: dict(n="Josef Špidlen", y="", st="doc", f=["Příkrý čp. 49"], r=["semily_krest_josef_petr_housa_1823"]),
    7: dict(n="Barbora Zemanová", y="", st="doc", f=["ze Lhoty (?)"], r=["semily_krest_josef_petr_housa_1823"],
            note="Čtení místa původu (Lhota) nejisté."),
}

# Rody = osm větví podle pradědečků a prababiček (čísla 8–15). Doplňte, jakmile je znáte:
# 8: ("Novákové", "Jedna věta, kdo to byli a odkud – ukáže se na webu u rodu."),
LINES = {
}

# Příbuzní mimo přímou linii (sourozenci, strýcové…): k = číslo předka, ke kterému patří.
# dict(k=16, n="Josef Novák (1865–1920)", t="Bratr Jana. Kovář v …", r=["klic_zapisu"])
SIDE = [
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
    ("Měl Josef Petr Housa (* 1823) sourozence?",
     "Otevřené: v Bítouchově není v letech 1809–1832 zapsán žádný další křest dítěte Josefa Hausy a Anežky Špidlenové; ostatní křty dětí „Josefa Hausy“ patří jiným mužům téhož jména s jinými manželkami. Zbývá prověřit úmrtí 1823–1836, křty po roce 1832 a sousední farnosti."),
    ("Kde a kdy se vzali Josef Housa a Anežka Špidlenová?",
     "Otevřené: v rejstříku oddaných farnosti Semily 1806–1828 ani v oddílu Příkrého 1821–1822 sňatek není."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
