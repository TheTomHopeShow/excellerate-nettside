import re
# tjenester.html og bransjer.html hentes fra /home/claude/rescue/ i build_all.sh,
# som overskriver dem HELT (meny og innhold) med en egen, frossen kopi. Synker inn
# tre ting fra den ferske bygde versjonen, slik at menyendringer, tekstendringer
# (f.eks. CTA-seksjonen) og CSS-fikser (f.eks. mobiltilpasning) slår igjennom på
# disse to sidene:
# 1) <nav class="hnav">-blokken, hentet fra en vanlig bygget side (om-oss.html).
# 2) <section id="samtale">-blokken (CTA-seksjonen), hentet fra den ferske,
#    riktige versjonen av hver side selv (lagret til /tmp rett før rescue-cp i
#    build_all.sh), siden CTA-teksten er forskjellig per side.
# 3) <style>-blokken, hentet fra om-oss.html (samme CSS brukes på alle sider),
#    slik at den frosne rescue-kopien aldri sitter igjen med utdatert CSS.
# Kilde: gap-vision.html. Ikke om-oss.html (skriptet der har ekstra, sidespesifikk
# skjemalogikk som 16.11.2026 feilaktig ble synket inn i tjenester.html/bransjer.html),
# og ikke en av de fire Tjenester-undersidene (de hentes selv fra en frosset
# rescue-kopi via tjenester3.py, så NAVET DERES KAN VÆRE UTDATERT - å bruke en av
# dem som kilde ville spredd den samme staleness videre). GAP-Vision.dc.html og
# Karriere.dc.html skrives derimot direkte av tjenester3.py sin egen kode, ikke
# kopiert fra rescue, så gap-vision.html/karriere.html har alltid fersk meny og
# ingen ekstra skript (de er ikke Forside/Fagekspert-/Kunnskap/Referanse/Om-oss/Kontakt).
NAV_SRC = "/home/claude/fs/site/gap-vision.html"
TARGETS = {
    "/home/claude/fs/site/tjenester.html": "/tmp/_fresh_tjenester.html",
    "/home/claude/fs/site/bransjer.html": "/tmp/_fresh_bransjer.html",
}
# Tjenester-undersidene (salg, ledelse, kultur, KI) hentes fra samme frosne
# rescue-mekanisme (se tjenester3.py), og har derfor samme problem: menyen de
# har bakt inn blir stående igjen på en eldre versjon selv om den vanlige menyen
# oppdateres andre steder (f.eks. Fageksperter -> Mennesker-endringen 15.11.2026).
# Disse fire har egne, riktige CTA-seksjoner (#samtale) fra tjenester2.py, så de
# skal IKKE få CTA-en sin overskrevet - kun nav og style synkes inn.
NAV_ONLY_TARGETS = [
    "/home/claude/fs/site/tjenester-salg.html",
    "/home/claude/fs/site/tjenester-ledelse.html",
    "/home/claude/fs/site/tjenester-kultur.html",
    "/home/claude/fs/site/tjenester-ki.html",
]

nav_src = open(NAV_SRC).read()
m = re.search(r'<nav class="hnav".*?</nav>', nav_src, flags=re.S)
if not m:
    raise SystemExit("Fant ikke <nav class=\"hnav\"> i " + NAV_SRC)
nav = m.group(0)

sm = re.search(r'<style>.*?</style>', nav_src, flags=re.S)
if not sm:
    raise SystemExit("Fant ikke <style> i " + NAV_SRC)
style = sm.group(0)

# 4) <div id="mpanel">...</header>-blokken (selve mobilmenypanelet, inkl. det nye
#    søkefeltet lagt til 16.11.2026) og det første <script>-taggen rett etter
#    (mbtn/mpanel-logikken). Begge er identiske på tvers av alle sider, hentet
#    fra samme ferske kilde som nav og style over.
mp = re.search(r'<div id="mpanel".*?</header>', nav_src, flags=re.S)
if not mp:
    raise SystemExit("Fant ikke <div id=\"mpanel\"> i " + NAV_SRC)
mpanel = mp.group(0)

sc = re.search(r'<script>.*?</script>', nav_src, flags=re.S)
if not sc:
    raise SystemExit("Fant ikke mbtn/mpanel-<script> i " + NAV_SRC)
mpanel_script = sc.group(0)

for path, fresh_path in TARGETS.items():
    t = open(path).read()
    t2, n = re.subn(r'<nav class="hnav".*?</nav>', nav, t, count=1, flags=re.S)
    if n == 0:
        print("ADVARSEL: fant ingen nav å bytte i", path)
    else:
        t = t2
        print("synket meny inn i", path)
    t4, n3 = re.subn(r'<style>.*?</style>', style, t, count=1, flags=re.S)
    if n3 == 0:
        print("ADVARSEL: fant ingen <style> å bytte i", path)
    else:
        t = t4
        print("synket CSS inn i", path)
    t5, n4 = re.subn(r'<div id="mpanel".*?</header>', mpanel, t, count=1, flags=re.S)
    if n4 == 0:
        print("ADVARSEL: fant ingen <div id=\"mpanel\"> å bytte i", path)
    else:
        t = t5
        print("synket mobilmenypanel inn i", path)
    t6, n5 = re.subn(r'<script>.*?</script>', mpanel_script, t, count=1, flags=re.S)
    if n5 == 0:
        print("ADVARSEL: fant ingen mbtn/mpanel-<script> å bytte i", path)
    else:
        t = t6
        print("synket mobilmeny-script inn i", path)
    try:
        fresh = open(fresh_path).read()
    except FileNotFoundError:
        print("ADVARSEL: fant ikke fersk versjon", fresh_path, "- hopper over CTA-synk for", path)
        open(path, "w").write(t)
        continue
    fm = re.search(r'<section id="samtale".*?</section>', fresh, flags=re.S)
    if not fm:
        print("ADVARSEL: fant ingen #samtale-seksjon i", fresh_path)
        open(path, "w").write(t)
        continue
    t3, n2 = re.subn(r'<section id="samtale".*?</section>', fm.group(0), t, count=1, flags=re.S)
    if n2 == 0:
        print("ADVARSEL: fant ingen #samtale-seksjon å bytte i", path)
    else:
        t = t3
        print("synket CTA inn i", path)
    open(path, "w").write(t)

for path in NAV_ONLY_TARGETS:
    t = open(path).read()
    t2, n = re.subn(r'<nav class="hnav".*?</nav>', nav, t, count=1, flags=re.S)
    if n == 0:
        print("ADVARSEL: fant ingen nav å bytte i", path)
    else:
        t = t2
        print("synket meny inn i", path)
    t4, n3 = re.subn(r'<style>.*?</style>', style, t, count=1, flags=re.S)
    if n3 == 0:
        print("ADVARSEL: fant ingen <style> å bytte i", path)
    else:
        t = t4
        print("synket CSS inn i", path)
    open(path, "w").write(t)
