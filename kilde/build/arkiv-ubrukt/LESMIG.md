# Arkiv — ubrukte skript

Disse filene kjøres ikke av `build_all.sh` eller noen fil den kaller, direkte
eller indirekte. De er flyttet hit 16.11.2026 for å rydde opp i build-mappen,
siden flere av dem (særlig `tjenester2.py`/`tjenester2b.py`) ser ut som
plausible filer å redigere for Tjenester-sidene, men ikke har noen effekt på
den faktiske siden. Ingenting er slettet. Flyttingen er verifisert å gi et
byte-for-byte identisk bygg som før.

- **tjenester2.py, tjenester2b.py** — tidlige, ikke-avtalte utkast til de fire
  tjenestesidene (salg, ledelse, kultur, KI). Egen kommentar i filen sier
  «Forslag (ikke avtalt)». Siden som faktisk brukes i dag ligger i
  `/home/claude/rescue/Tjenester-*.dc.html`, kopiert inn av `tjenester3.py`.
- **forslag.py, forslag_d.py** — tre tidlige stemningstester (A/B/C) for
  forsiden, fra en tidlig fase av prosjektet. Erstattet av det som står i
  `build.py`/`v2.py`/`forside2.py` i dag.
- **forslag_meny.py** — et sandkasse-verktøy som bevisst skriver kun til en
  egen testside (`forslag-meny.html`), ikke til noen live side. Kan være nyttig
  å ha igjen hvis man vil prøve menyideer uten å røre live-sidene, men er ikke
  del av det faktiske bygget.
- **shot.py, shot2.py, t_filter.py, weigh.py** — Playwright-baserte
  skjermbilde- og målerverktøy, brukt til manuell kontroll under arbeidet, ikke
  til å generere sider.
