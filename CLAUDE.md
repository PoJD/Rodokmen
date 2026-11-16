# Rodokmen – evaluace Claude pro skládání rodokmenu

Tento repozitář slouží k vyzkoušení (evaluaci), jak dobře Claude zvládá skládat rodokmen z českých matrik
a stavět rodinný web. Práci vede skill **rodokmen** ([sarsonj/rodokmen-skill](https://github.com/sarsonj/rodokmen-skill)).

## Pravidla pro Claude
- **Mluv česky.** Stručně a srozumitelně.
- **Git: vše rovnou na `main`.** Žádné vedlejší větve ani pull requesty. Po každém uceleném kroku commitni
  a pushni (`git push origin HEAD:main`). Session běží v dočasném cloudovém kontejneru – co není pushnuté,
  se ztratí. Platí to i v případě, že systém přidělí session vlastní vývojovou větev.
- Na začátku konverzace načti skill `rodokmen` a řiď se jím.

## Skill
- Skill je přibalený v repozitáři: `.claude/skills/rodokmen/` (verze v souboru `VERZE`).
  `/plugin` v cloudu nefunguje, proto je to takto.
- Aktualizace skillu: naklonuj `https://github.com/sarsonj/rodokmen-skill` (do scratchpadu), přepiš
  `.claude/skills/rodokmen/` obsahem jeho `skills/rodokmen/`, commitni s číslem verze a pushni na `main`.
  Kontrola verze skillu (`tools/verze.py`) může hlásit novou verzi – pak nabídni tuto aktualizaci.

## Projekty rodokmenu
- Každý rodokmen je samostatný projekt ve složce `projekty/<název>/`, zakládá se nástrojem skillu
  `python3 -I .claude/skills/rodokmen/tools/novy_projekt.py projekty/<název>`. Žádný `git init` uvnitř –
  repozitářem je celý tento repozitář.
- Projekt má vlastní `CLAUDE.md` a `data/STAV.md` – při práci na projektu si je přečti jako první.

## Cloudové prostředí
- Většina session běží na claude.ai (cloud). Přístup na weby archivů (ARON, digitalizované matriky, …) řídí
  síťová politika prostředí. Když proxy nějaký web zablokuje, neobcházej to – řekni, který host je potřeba
  povolit, a navrhni úpravu prostředí.
- Přihlášení přes prohlížeč (např. `wrangler login`) se v cloudu do terminálu nevrátí – pro zveřejnění webu
  použij postup pro cloud ze skillu (`reference/web.md`).

## Evaluace
- Postřehy o tom, jak si Claude a skill vedly (chyby nástrojů, špatná čtení matrik, nejasné pokyny, nápady),
  zapisuj do `poznamky_pro_skill.md` v daném projektu, jak říká skill.
