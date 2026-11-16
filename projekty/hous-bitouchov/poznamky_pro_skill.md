# Poznámky pro správce skillu „rodokmen“

Sem Claude průběžně zapisuje, co by se mělo ve skillu zlepšit: chyby nástrojů, nové archivy a postupy, nápady.
Jen technické věci, žádné údaje o rodině. Nic se neposílá automaticky – když budete chtít, Claude poznámky vypíše
a vy je zkopírujete do e-mailu na sarsonj@gmail.com. Klidně připište i vlastní zkušenosti – užitečné změny autor rád
zapracuje do skillu, aby je měli i ostatní. Děkujeme!


## 2026-11-16 (skill 0.10.1, cloud)
- Uživatel dal odkaz na **matriky.online** (`matriky.online/zamrsk/000-05192/202/`). Skill ten web nezná. Odkaz jde převést:
  `zamrsk` = SOA Zámrsk (ARON), `05192` = signatura, `202` = číslo snímku shodné s ARONem. Svazek se v ARONu najde přes
  `aron_search.py "<obec>"` a filtr na „sign.: 5192“. Hodilo by se hledání podle signatury (`aron_search.py --sign 5192`)
  a zmínka o matriky.online v `portaly.md`.
- Zadání „najdi sourozence osoby z tohoto zápisu“ (bez rodiny, bez výchozí osoby) skill výslovně nepopisuje; založil jsem
  projekt s osobou ze zápisu jako č. 1. Stálo by za krátký postup „hledání sourozenců“: rejstřík N → všechny křty otce
  téhož jména → ověřit matku na snímku (ve vsi bývá víc mužů stejného jména).
- Knihy řazené po vsích: celá strana zmenšená na 1900 px na výšku je nečitelná; osvědčilo se rozřezat každou stranu na
  horní a dolní polovinu (`convert x.jpg -crop 50%x100% +repage -crop 100%x50% +repage -resize 1900x`). Nástroj na to chybí
  (`overit.py` dělí jen výřez zápisu).
- Rejstříky fary Semily: N 1809–1832 je do 1822 po vsích, pak chronologicky a s pomlčkami místo jména otce; O 1682–1828
  má pokračování písmen na konci knihy („pokračování viz strana 134“); Z 1682–1843 je dvojjazyčný tištěný formulář.
  Obecná rada do `matriky.md`: u rejstříku nejdřív zjistit řazení (po vsích × chronologicky) a hledat odkazy na pokračování.
- `kontrola.py` hlásí chybějící obec u předka s nejistým místem („ze Lhoty (?)“) – u nejistého čtení by to mohlo mlčet.
- ImageMagick v cloudu jen verze 6 (`convert`), nástroje s ní fungují.
- Hledání sourozenců: vyplatilo se hledat podle **matky** (jméno, otec, dům), ne podle příjmení otce – dítě se našlo pod
  jinak zapsaným příjmením otce v sousední farnosti (ves nevěsty). Rejstřík by ho neukázal. Stálo by za zmínku v `metodika.md`.
- Auto mode: kontrola příkazu několikrát po sobě vrátila „no verdict“ u stahování snímků ve smyčce; pomohlo počkat a zopakovat.
