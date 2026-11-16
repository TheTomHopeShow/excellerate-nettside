# Kildekode for excellerate.no

Denne mappen er selve byggesystemet som genererer nettstedet i rotmappen av
dette repoet. Den ble lagt inn her 16.11.2026, slik at kildekoden ligger
sammen med det den produserer, i stedet for bare i arbeidsmiljøet.

## Hvordan bygget kjøres

```bash
cd kilde/build
bash build_all.sh
```

Dette leser kilder fra `kilde/build/` og `kilde/rescue/`, og skriver den
ferdige, statiske siten til en `site/`-mappe. Det **skriver ikke** direkte inn
i repoets rotmappe — resultatet må kopieres inn der manuelt (se under), slik
at man alltid ser nøyaktig hva som endrer seg før det committes.

For å oppdatere den live siten etter et bygg:

```bash
# fra repoets rot
find . -mindepth 1 -maxdepth 1 \! -name '.git' \! -name 'kilde' -exec rm -rf {} +
cp -a kilde/build/../site/. .     # eller den stien build_all.sh faktisk skriver til
git add -A
git commit -m "..."
git push
```

(I praksis har build_all.sh blitt kjørt fra en arbeidsmappe utenfor selve
repoet, med `site/`-mappen ett nivå opp fra `build/`. Se stien øverst i
`build_all.sh` — `cd /home/claude/fs/build` — som forutsetter denne
mappestrukturen. Kjøres bygget fra `kilde/build/` i stedet, må den første
linjen i `build_all.sh` endres til `cd kilde/build`, og `site/`-mappen vil da
havne som `kilde/site/`.)

## Mappestruktur

- **`build/`** — Python-skriptene som genererer hver side. `build_all.sh` er
  inngangspunktet og viser nøyaktig hvilke skript som kjører, i hvilken
  rekkefølge. De fleste sidene bygges fra `.dc.html`-filer (en eksport fra
  designverktøyet) som skriptene fyller med innhold og gjør om til ferdig
  HTML. `build/arkiv-ubrukt/` inneholder skript som ikke er del av bygget —
  se `LESMIG.md` der for hvorfor de er arkivert, ikke slettet.

- **`rescue/`** — frosne kopier av enkelte sider (`tjenester.html`,
  `bransjer.html`) og enkelte `.dc.html`-kilder (Tjenester-undersidene,
  GAP Vision). Disse kopieres inn og overskriver de vanlige kildene ved hvert
  bygg (se `tjenester3.py` og `build_all.sh`). Grunnen til at dette finnes:
  disse sidene ble på et tidspunkt redigert direkte i det ferdige resultatet,
  og «rescue»-kopien er det stedet disse redigeringene faktisk bor. **Dette
  er den vanligste kilden til at en rettelse ikke slår igjennom etter et nytt
  bygg** — rediger alltid filen i `rescue/`, ikke bare den tilsynelatende
  kilden i `build/`, for disse sidene. `sync_rescue_header.py` kjøres etter
  disse kopieringene for å synke inn meny, CSS og mobilmenypanelet på nytt
  (hentet fra en fersk, uforurenset side — se kommentaren i filen for hvorfor
  nettopp `gap-vision.html` er valgt som kilde, og ikke en annen side).
  `rescue/pre-runde1/` er en eldre sikkerhetskopi av noen skript fra en
  tidligere runde, ikke i bruk.

## Kjente fallgruver

1. **De fire Tjenester-undersidene** (salg, ledelse, kultur, KI) kopieres fra
   `rescue/Tjenester-*.dc.html` ved hvert bygg. En endring i
   `build/tjenester2.py`/`tjenester2b.py` (arkivert) eller direkte i
   `build/Tjenester-*.dc.html` har **ingen effekt** — disse blir overskrevet.
   Rediger `rescue/Tjenester-*.dc.html` i stedet.
2. **tjenester.html og bransjer.html** kopieres i sin helhet fra
   `rescue/tjenester.html` og `rescue/bransjer.html`, og går aldri gjennom
   `static.py`. Meny, CSS og mobilmenypanel synkes inn etterpå av
   `sync_rescue_header.py`, men alt annet innhold på disse to sidene må
   redigeres direkte i rescue-filen.
3. En endring i delt sidestruktur (toppmeny, mobilmenypanel, footer) må testes
   mot **alle** disse unntakene, ikke bare mot en vanlig side — et bygg som
   ser riktig ut på forsiden kan likevel mangle endringen på Tjenester-sidene.

## Styringsregel

Les designmanualens kapittel 7 («Stemme og bilder») og
`claude/tekstgjennomgang-forslag-15-11.md` i Claude-prosjektet før noen
endring i tekst eller design. Dette gjelder uavhengig av hvilken sesjon eller
hvilken AI-modell som utfører endringen.
