# Stav rodokmenu a pravidla práce

Tento soubor je vstupní bod. Po každém restartu (nová konverzace, zkrácený kontext) ho Claude čte jako první,
pak konec `research_log.md` a sekci „Rozpracováno“.

## Pro koho
- Výchozí osoba: Josef Petr Housa, * 7. 1. 1823 Bítouchov čp. 35 (farnost Semily). Zadání: najít všechny jeho sourozence.
- Kdo s Claudem pracuje a jak chce komunikovat: uživatel zadal odkaz na matriky.online (sign. 5192, snímek 202); česky, stručně. Vztah k rodině zatím neřekl.

## Kde co je
| Soubor | Obsah |
|---|---|
| `data/osoby.py` | Přímí předci podle Kekulého čísla + rody, boční příbuzní, otevřené otázky, hypotézy. |
| `data/zaznamy.json` | Každý použitý zápis z matriky (klíč = název obrázku). |
| `data/svazky.json` | Matriční svazky (archiv, signatura, odkaz). |
| `data/prepisy.json` | Přepis originálu a český překlad každého zápisu. |
| `data/zvyrazneni.json` | Rámečky – které místo výřezu čteme. |
| `data/research_log.md` | Deník VŠECH hledání, i neúspěšných. |
| `data/udaje_od_rodiny.md` | Co řekla rodina, rodinné dokumenty. |
| `data/zajimavosti.md`, `data/pribeh.md` | Texty na web. |
| `data/archivni_dotazy.md` | Co by šlo zjistit jen v archivu. |
| `data/mista.json`, `data/dokumenty.json`, `data/web.json` | Mapa, rodinné fotky a dokumenty, nastavení webu. |
| `vyrezy/`, `zdroje/` | Výřezy zápisů pro web (1800 px) a v plném rozlišení. |
| `dokumenty/` | Rodinné dokumenty a fotky od uživatele (originály). |
| `pracovni/` | Pracovní soubory (stažené stránky, kontrolní obrázky) – nejdou na web. |
| `web/` | Rodinný web. `cd web && npm run nahled` (data + sestavení + náhled); po změně dat stačí `npm run data && npm run build`. |

## Pravidla
1. Než něco ohlásím jako nové, prohledám `osoby.py`, `zaznamy.json` a `research_log.md` (jméno, místo, rok).
2. Údaj je „doloženo“ (doc) jen tehdy, když jsem ho přečetl přímo na snímku. Čtení od pomocníků ověřím sám.
3. Každé hledání (i neúspěšné) zapíšu do `research_log.md`.
4. Nejistá čtení označím (?) – nic nedomýšlím.
5. Ke každému novému zápisu: výřez (`tools/vyrez.py`), rámeček (`tools/ramecek.py`) a přepis s překladem.
6. Po změně dat spustím `python3 -I tools/kontrola.py`.

## Rozpracováno (aktualizovat průběžně)
- Křest Josefa Petra (1823) zapsán. Rodiče: Josef Hausa × Anežka Špidlenová z Příkrého čp. 49; sňatek 20. 11. 1815 Příkrý
  (údaj uživatele, ženich omylem „Jan“; zápis jsem nečetl – O Bozkov sign. 4862, ARON c35d0273). Josef má být sedlák.
- Nalezeno: Anežka Marie * 2. 8. 1818 Příkrý čp. 40, stejná matka, otec zapsán „Růžek (?) Josef, sedlák z Bítouchova“ –
  pravděpodobná sestra (SIDE, prob). Zeptat se uživatele, zda zná jméno „Růžek“ (po chalupě?).
- Negativní: Bítouchov křty 1809–1832 (deník 3–4); Příkrý křty 1816–1839 celé (deník 10–11); úmrtí Bítouchov 12/1824–1848
  (deník 8, 12) a Příkrý 1815–1840 (deník 12) – Anežka ani další děti nikde.
- Stopa: † 2. 9. 1841 Bítouchov čp. 35 Josef Hausa, výměnník, 80 let (zápis bitouchov_umrti_josef_hausa_1841) – otec?
  Pak by mu bylo při sňatku 1815 asi 54 → první manželství, nevlastní sourozenci. Zeptat se na věk ženicha v zápisu 1815.
- Další kroky: (1) přečíst sňatek 1815 (O Bozkov sign. 4862, ARON c35d0273) – věk, vdovec?; (2) když vdovec: křty
  Bítouchov před 1815 (N Semily sign. 5191, 5192 – oddíl Bítouchova sn. 190–196) a 1. sňatek; (3) křty Bítouchov 1833–1840
  (sign. 5195, 5196); (4) Anežka po 1848 (Z Bozkov sign. 5691 / index 5695, Z Semily 5208).
- V Bítouchově je víc Josefů Hausů (čp. 39 sedlák, 40/15, 8/25, 7) – rozhoduje jméno matky.
- Web ani zveřejnění se neřešilo.
