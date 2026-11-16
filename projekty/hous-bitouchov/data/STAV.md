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
- Křest Josefa Petra přečten a zapsán. Rodiče: Josef Hausa, podruh × Anežka Špidlenová z Příkrého čp. 49.
- Sourozenci: v Bítouchově 1809–1832 žádný další křest tohoto páru (deník ř. 3–4). Pozor – v Bítouchově je víc Josefů Hausů
  (čp. 39, 40/15, 8/25, 7), každý s jinou ženou; rozhoduje jméno matky.
- Další kroky: (1) úmrtí Bítouchov 1823–1836 (Z Semily sign. 5206, ARON f6257136) – nezemřel Josef Petr nebo některý rodič?
  (2) sňatek: oddíl Bítouchova v O sign. 5202 (fol. 321–325) a Příkrý před 1821; (3) křty 1833–1850 (index sign. 5213,
  ARON 55b2a874; knihy 5195–5197); od 1840/41 patří Bítouchov i Příkrý k farnosti Bozkov (N sign. 4860, index 4867);
  (4) doověřit neověřené křty z deníku ř. 4.
- Web ani zveřejnění se neřešilo.
