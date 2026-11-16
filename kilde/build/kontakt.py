# Kontaktbokser. Tom og Per Kjetil er kontaktpunktene i salg. Telefon og e-post er hentet fra excellerate.no 14.11.2026.
# Toms e-post, telefon og tittel (Brobygger) er oppgitt av Tom 14.11.2026.
_KP=[dict(n="Per Kjetil Parr",r="Administrerende direktør",img=EX[0][3],key="per-kjetil",mail="pkp@excellerate.no",tlf=("+47 90 89 05 09","90890509"),book="Fagekspert-per-kjetil-parr.dc.html#book",
        t="Snakk med Per Kjetil om utvikling av ledere, salg og kultur. Han var med på oppstarten av Euro Business School."),
     dict(n="Tom Hope",r="Brobygger",img=TOM[3],key="tom",mail="th@excellerate.no",tlf=("+47 410 88 885","41088885"),book=None,
        t="Snakk med Tom om hva dere vil oppnå, så finner vi riktig fagekspert og neste steg sammen.")]
def _kkb():
    return ('<aside class="kkb" aria-label="Kontakt oss"><div class="kkf"><img src="%s" alt="Tom Hope"><img src="%s" alt="Per Kjetil Parr"></div>'
     '<div class="kkt"><h2>Usikker på hvem du bør snakke med?</h2><p>Tom Hope og Per Kjetil Parr hjelper deg til riktig fagekspert.</p></div>'
     '<div class="kkx"><a class="kn g" href="Kontakt.dc.html">Skriv til oss</a><a class="kn o" href="tel:+4722490000">Ring 22 49 00 00</a></div></aside>')%(U(TOM[3]),U(EX[0][3]))
def _kk(p):
    b=[]
    if p["book"]: b.append('<a class="kn g" href="%s">Book en samtale</a>'%p["book"])
    else: b.append('<a class="kn g" href="Kontakt.dc.html?hvem=%s#skjema" data-who="%s">Book en samtale</a>'%(p["key"],p["key"]))
    if p["mail"]: b.append('<a class="kn o" href="mailto:%s">Send e-post</a>'%p["mail"])
    t='<a class="kkl" href="tel:+47%s">%s</a>'%(p["tlf"][1],p["tlf"][0]) if p["tlf"] else ''
    return '<div class="kkp"><img src="%s" alt=""><div><b>%s</b><span>%s</span><p>%s</p>%s<div class="kbs">%s</div></div></div>'%(U(p["img"]),_E5(p["n"]),_E5(p["r"]),_E5(p["t"]),t,"".join(b))
