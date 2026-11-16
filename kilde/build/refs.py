# Referanser (caser). Tekst, tall og sitater er hentet fra excellerate.no/referanser 14.11.2026. Ingen tall er lagt til.
import json as _rj, re as _rre
_RS=_rj.load(open("/mnt/user-data/uploads/Downloads/ref-cases.json"))
def _lines(slug):
    t=_RS[slug]["text"]; i=t.index("Kontakt\n",t.index("Konsulenter"))+8; j=t.index("Personvern")
    return [l.strip() for l in t[i:j].split("\n") if l.strip()]
def _sect(slug,start,end=None,mark_end=None):
    L=_lines(slug); a=[k for k,l in enumerate(L) if l.startswith(start)][0]
    b=len(L)
    if end:
        e=[k for k,l in enumerate(L) if k>a and l.startswith(end)]
        if e:b=e[0]
    return L[a:b]
def _body(lines,h3=False):
    out=[];ul=[]
    def fl():
        nonlocal ul
        if ul: out.append("<ul>"+"".join("<li>%s</li>"%_E5(x) for x in ul)+"</ul>"); ul=[]
    for l in lines:
        if l.startswith(("•","- ")) and not l.startswith("– "): ul.append(l.lstrip("•- ").strip()); continue
        fl()
        if l.startswith("–") or l.startswith("-Vi"): out.append('<p class="rfi">%s</p>'%_E5(l))
        elif h3 and len(l)<64 and not l.endswith((".","?","!")) : out.append("<h3>%s</h3>"%_E5(l))
        else: out.append("<p>%s</p>"%_E5(l))
    fl(); return "".join(out)
def T(v,l,kind="Resultat",viz=None,note=""): return dict(v=v,l=l,k=kind,viz=viz,n=note)
def V(mn,mx,a,b,la,lb): return dict(mn=mn,mx=mx,a=a,b=b,la=la,lb=lb)
CASES=[
dict(slug="thon",id="krf01",nm="Thon Hotels",bransje="Hotell",vimeo=("357301610",""),
 h="Thon Hotels løftet den kommersielle kulturen og økte pipelinen med 32 millioner kroner",
 ti="Thon Hotels, 32 millioner mer i pipeline | Excellerate",
 ing="Thon Hotels savnet de konkrete verktøyene de trengte for å skape besøksglede for kundene og arbeidsglede for de ansatte.",
 kpi=[T("+32 mill. kr","Økning i pipelinen, fra 92 til 124 millioner kroner",viz=V(0,140,92,124,"92 mill.","124 mill.")),T("+5 %","Økt omsetning i 2018"),T("2018","Årets resultatskaper, gitt for ledelse, salg og service","Utmerkelse")],
 fakta=[("Bransje","Hotell"),("Periode","2018"),("Utmerkelse","Årets resultatskaper 2018")],
 q=("Med dyktig ledelse og assistanse fra spesialister i Excellerate, har selskapet løftet den kommersielle kulturen til et nytt nivå.","Per Griwell","Kommersiell direktør, Thon Hotels"),
 sek=[("Utgangspunktet",_sect("thon","Thon Hotels savnet","Gjennomføring")),("Gjennomføring",_sect("thon","Gjennomføring","Resultat")[1:]),("Resultat",_sect("thon","Resultat")[1:])]),
dict(slug="boligpartner",id="krf02",nm="BoligPartner",bransje="Boligbygging",vimeo=("121393140",""),
 h="BoligPartner økte salget med 26 prosent mens bransjen falt 22 prosent",
 ti="BoligPartner, +26 % da bransjen falt 22 % | Excellerate",
 ing="BoligPartner har realisert mer enn 6 300 boligdrømmer siden 1993. Første halvår 2014 vokste de mens markedet falt.",
 kpi=[T("+26 %","Flere solgte enheter første halvår 2014. Bransjen falt 22 %",viz=V(-30,30,-22,26,"Bransjen −22 %","BoligPartner +26 %")),T("42,5 %","Hit-rate fra salgsløp til kontrakt, opp fra ca. 28 %",viz=V(0,50,28,42.5,"28 %","42,5 %")),T("747","Enheter solgt")],
 fakta=[("Bransje","Boligbygging, ferdighus"),("Størrelse","Over 6 300 boliger siden 1993"),("Periode","2014")],
 q=None,
 sek=[("Om kunden",_sect("boligpartner","BoligPartner leverer","Gjennomføring")),("Gjennomføring",_sect("boligpartner","Gjennomføring","Resultat")[1:]),("Resultat",_sect("boligpartner","Resultat")[1:])]),
dict(slug="hertz",id="krf03",nm="Hertz Norge",bransje="Bilutleie og bildeling",vimeo=("344037268","ca74ce56b1"),
 h="Hertz Norge bygger en strategi for å lede innen mobilitet i 2025",
 ti="Hertz Norge, strategi for mobilitet i 2025 | Excellerate",
 ing="Hertz skal være førstevalget innen bilutleie, også i den nye delingsøkonomien, med heldigitale delings- og mobilitetsløsninger.",
 kpi=[T("500+","Utleiepunkter i Norge","Fakta"),T("ca. 10 000","Nye biler i den norske bilflåten","Fakta"),T("2025","Målet: Hertz Norge er ledende på mobilitet","Mål")],
 fakta=[("Bransje","Bilutleie og bildeling"),("Fakta","Over 500 utleiepunkter, representert på samtlige flyplasser"),("Mål","Ledende på mobilitet i 2025")],
 q=("Vi kommer til å jobbe kontinuerlig med Excellerate og strategiprosjektet i mange år fremover. Denne investeringen kommer til å bære seg selv, og gi bedre resultater for bedriften. Og dermed også dens ansatte og eiere.","Trygve Simonsen","Administrerende direktør, Hertz Norge"),
 sek=[("Om kunden",_sect("hertz","Hertz er Norges","Gjennomføring")),("Gjennomføring",_sect("hertz","Gjennomføring","Resultat")[1:]),("Resultat",_sect("hertz","Resultat")[1:])]),
dict(slug="wikborg-rein",id="krf04",nm="Wikborg Rein",bransje="Advokat",vimeo=("324958719","d592782742"),
 h="Wikborg Rein fikk alle advokater i Norge compliant på informasjonssikkerhet på 14 dager",
 ti="Wikborg Rein, compliant på 14 dager | Excellerate",
 ing="Wikborg Rein har startet en stor digital omstilling og valgte å implementere en digital læringsplattform sammen med Excellerate.",
 kpi=[T("14 dager","Til samtlige advokater i Norge var compliant innen informasjonssikkerhet"),T("WR LMS","Digital læringsplattform for onboarding, reboarding og utviklingssamtaler","Løsning"),T("5 byer","Kontorer i Oslo, Bergen, London, Singapore og Shanghai","Fakta")],
 fakta=[("Bransje","Advokat"),("Fakta","Norges største advokatfirma"),("Periode","2018")],
 q=("Excellerate har bidratt med gode løsninger på hvordan vi kan forenkle og forbedre kompetanseutviklingen internt. Systemet er enkelt å bruke både for oss som utvikler moduler og for brukerne.","Line Daler","Learning Consultant, Wikborg Rein"),
 sek=[("Om kunden",_sect("wikborg-rein","Wikborg Rein er Norges","Gjennomføring")),("Gjennomføring",_sect("wikborg-rein","Gjennomføring","Resultat")[1:]),("Resultat",_sect("wikborg-rein","Resultat")[1:])]),
dict(slug="ark",id="krf05",nm="Ark Bokhandel",bransje="Bokhandel",vimeo=("472978598",""),
 h="Ark økte mersalget med 40 prosent på tre måneder med kundeinnsikt",
 ti="Ark, 40 % mer mersalg på tre måneder | Excellerate",
 ing="I 2018 bestemte ARK seg for å sette fokus på utvikling og kompetanseheving basert på reell kundeinnsikt.",
 kpi=[T("+40 %","Høyere score på mersalg i løpet av tre måneder"),T("12–15 mill. kr","Bedre bunnlinje, slik Ark selv forventer det","Forventet"),T("50 000","Svar fra ekte kunder på litt over tre måneder")],
 fakta=[("Bransje","Bokhandel"),("Størrelse","142 butikker, nettbutikk og leseapp"),("Periode","2018")],
 q=("Med Excellerate Insight skal vi bedre bunnlinja vår med 12-15 millioner kroner, og det er bare i år. Helt fantastisk!","Stein Ove Gudmundsrud","Driftsdirektør, Ark"),
 sek=[("Om kunden",_sect("ark","ARK er Norges","Gjennomføring")),("Gjennomføring",_sect("ark","Gjennomføring","Resultat")[1:]),("Resultat",_sect("ark","Resultat")[1:])]),
dict(slug="fortum",id="krf06",nm="Fortum",bransje="Energi",vimeo=("210760726",""),
 h="Fortum økte salget med 25 prosent, med 51 prosent færre kundehenvendelser",
 ti="Fortum, 25 % mer salg og 51 % færre henvendelser | Excellerate",
 ing="I 2014 tok Fortum en beslutning om å selge nettselskapet. Det skapte usikkerhet og redsel om egen fremtid blant de ansatte.",
 kpi=[T("+25 %","Flere salg av nye strømkontrakter fra kundesenteret i 2016"),T("−51 %","Færre kundehenvendelser fra 2015 til 2016","Kontekst"),T("3 mål","Økt salg, flere lojale kunder og bedre tilgjengelighet","Mål")],
 fakta=[("Bransje","Energi"),("Avdeling","Kundesenteret i Norge"),("Periode","2015 til 2016")],
 q=("Samarbeidet med Excellerate har gjort at vi har styrket vår teamfølelse, vi har trosset denne «frykten» sammen og vi har jobbet med gleden av å levere positive resultater.","Annette Vanem Jønsson","Head of Sales and customer service, Fortum"),
 sek=[("Utgangspunktet",_sect("fortum","Strømmarkedet er","Resultat")[0:1]+_sect("fortum","I 2014 tok","Resultat")),("Resultat",_sect("fortum","Fortum Norge er")[0:])]),
dict(slug="saint-gobain-distribution",id="krf07",nm="Saint-Gobain Distribution",bransje="Distribusjon av VVS og byggevarer",vimeo=None,
 h="Saint-Gobain Distribution snudde medarbeidertilfredsheten fra minus 11 til 21",
 ti="Saint-Gobain, fra −11 til 21 i tilfredshet | Excellerate",
 ing="En medarbeidertilfredshet på minus 11 gjorde myke verdier til en strategisk prioritet.",
 kpi=[T("21","Medarbeidertilfredshet i siste undersøkelse, opp fra minus 11",viz=V(-20,40,-11,21,"−11","21")),T("82","«Ansatte som ser seg selv på lønningslisten om to år», indeks. Opp fra 61 i 2021",viz=V(0,100,61,82,"61","82")),T("2023","Årets resultatskaper, kåret av Excellerates rådgivere","Utmerkelse")],
 fakta=[("Bransje","Distribusjon av VVS og byggevarer"),("Størrelse","Over 24 milliarder kroner i omsetning, over 4 000 ansatte (konsernet)"),("Utmerkelse","Årets resultatskaper 2023")],
 q=("Vi har skapt nye verdier, etablert nye informasjonskanaler og har fått et eget årshjul med tiltak for å bygge kultur. Det er utnevnt endringsagenter som hjelper oss innføre de nye verdiene.","Thomas Fehn","Konserndirektør for IT og digitalisering, Saint-Gobain Distribution"),
 sek=[("Saken",_sect("saint-gobain-distribution","Giganten Saint Gobain","Disse tjenestene"))],tj=True),
]
# Saint-Gobain: tjenester
_sg=_lines("saint-gobain-distribution"); _a=[k for k,l in enumerate(_sg) if l.startswith("Disse tjenestene")][0]; _b=[k for k,l in enumerate(_sg) if l.startswith("I gjennomføringen")][0]
CASES[-1]["tjl"]=(_sg[_a+2:_b],_sg[_b+1:])
for c in CASES: c["fo"]=_E5(c["nm"])
_BYS={c["slug"]:c for c in CASES}
_KIND={"Resultat":"res","Forventet":"for","Fakta":"fak","Mål":"mal","Utmerkelse":"utm","Løsning":"fak","Kontekst":"fak"}
def _pos(p):
    return 'left:0' if p<20 else ('right:0;left:auto;transform:none' if p>80 else 'left:%.1f%%'%p)
def _viz(v):
    if not v: return ""
    p=lambda x:(x-v["mn"])/(v["mx"]-v["mn"])*100
    a,b=p(v["a"]),p(v["b"]); lo,hi=min(a,b),max(a,b)
    zero='<i class="rz" style="left:%.1f%%"></i>'%p(0) if v["mn"]<0 else ""
    return ('<div class="rviz" aria-hidden="true"><div class="rtr"><i class="rfl" style="left:%.1f%%;width:%.1f%%"></i>%s<i class="rd0" style="left:%.1f%%"></i><i class="rd1" style="left:%.1f%%"></i></div>'
      '<div class="rlb"><span style="%s">%s</span><span class="e" style="%s">%s</span></div></div>')%(lo,hi-lo,zero,a,b,_pos(a),_E5(v["la"]),_pos(b),_E5(v["lb"]))
def _kpis(c):
    return '<div class="rkp">'+"".join('<div class="rk %s"><span class="rkk">%s</span><b class="rkv">%s</b><p>%s</p>%s</div>'%(_KIND[k["k"]],_E5(k["k"]),_E5(k["v"]),_E5(k["l"]),_viz(k["viz"])) for k in c["kpi"])+'</div>'
_PLAY='<svg aria-hidden="true" width="26" height="26" viewBox="0 0 24 24"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg>'
def _video(c):
    if not c["vimeo"]: return '<div class="rfig"><img src="%s" alt="%s"></div>'%(U(c["id"]),_E5("Thomas Fehn, konserndirektør, foran Saint-Gobain-logoen"))
    vid,h=c["vimeo"]
    return '<div class="rfig"><button type="button" class="rfv" data-v="%s" data-h="%s" data-t="Film: %s"><img src="%s" alt=""><span class="rpl">%s</span><span class="rpt">Se filmen</span></button></div>'%(vid,h,_E5(c["nm"]),U(c["id"]),_PLAY)
def _card(c):
    k=c["kpi"][0]
    return '<a class="rcc" href="Referanse-%s.dc.html"><span class="rci"><img src="%s" alt=""></span><div class="rcb"><span class="rcm">%s</span><h3>%s</h3><p class="rcn"><b>%s</b> %s</p><span class="xl-lenke">Les referansen<span class="pil"></span></span></div></a>'%(c["slug"],U(c["id"]),_E5(c["bransje"]),_E5(c["nm"]),_E5(k["v"]),_E5(k["l"]))
def _page(c):
    secs=""
    for k,(h,ls) in enumerate(c["sek"]):
        secs+='<h2>%s</h2>%s'%(_E5(h),_body(ls,h3=(c["slug"]=="saint-gobain-distribution")))
        if k==0 and c["q"]:
            q=c["q"]; secs+='<figure class="rq"><blockquote><p>«%s»</p></blockquote><figcaption><b>%s</b>%s</figcaption></figure>'%(_E5(q[0]),_E5(q[1]),_E5(q[2]))
    if c.get("tj"):
        a,b=c["tjl"]; secs+='<h2>Disse tjenestene er levert inn i prosjektet</h2><div class="rsv"><div><h3>Innsikt</h3><ul>%s</ul></div><div><h3>I gjennomføringen</h3><ul>%s</ul></div></div>'%("".join("<li>%s</li>"%_E5(x) for x in a),"".join("<li>%s</li>"%_E5(x) for x in b))
    fk="".join("<div><dt>%s</dt><dd>%s</dd></div>"%(_E5(a),_E5(b)) for a,b in c["fakta"])
    rel=[x for x in CASES if x is not c]; i=CASES.index(c); rel=[CASES[(i+j)%len(CASES)] for j in (1,2,3)]
    return ('<section class="rhero"><svg aria-hidden="true" class="rx" viewBox="0 0 700 700"><line x1="80" y1="80" x2="620" y2="620" stroke="#244A5E" stroke-width="150"/><line x1="620" y1="80" x2="80" y2="620" stroke="#244A5E" stroke-width="150"/></svg>'
      '<div class="wrap rhg"><div class="rht"><a class="kab rab" href="Referanser.dc.html">Referanser</a><span class="rkick">%s</span><h1>%s</h1><p class="kin">%s</p></div>%s</div></section>'%(_E5(c["bransje"]),_E5(c["h"]),_E5(c["ing"]),_video(c))
      +'<section class="rkw"><div class="wrap">'+_kpis(c)+'</div></section>'
      +'<section class="wrap rbd"><aside class="rfa"><p class="rft">Kort om kunden</p><dl>%s</dl></aside><article class="rar">%s<p class="ksrc">Kilde: excellerate.no/referanser. Tall og sitater er hentet derfra og må bekreftes med kunden før lansering.</p></article></section>'%(fk,secs)
      +'<section class="wrap"><div class="kcta" style="margin-bottom:72px">'+_xw("ix")+'<div><h2>Vil dere ha tilsvarende resultater?</h2><p>Fortell oss hva dere vil løse. Vi finner riktig fagekspert og tar en uforpliktende samtale.</p><div class="kbs"><a class="kn g" href="Fagekspertene.dc.html">Finn riktig fagekspert</a><a class="kn l" href="mailto:post@excellerate.no">Send e-post</a><a class="kn l" href="tel:+4722490000">Ring 22 49 00 00</a></div></div></div></section>'
      +'<section class="wrap" style="padding-bottom:56px">'+_kkb()+'</section>'
      +'<section class="krel"><div class="wrap"><h2>Flere referanser</h2><div class="rcg">%s</div></div></section>'%"".join(_card(x) for x in rel))
for c in CASES: _write("Referanse-%s.dc.html"%c["slug"],c["ti"],_page(c),3000)
# Tom 15.11.2026: kundelogoer i farge til høyre i heroen, med samme forskjøvne rytme som Karriere-heroen.
_RLG=dict(LOGOS2)
_RL_SLUGS=["thon","boligpartner","hertz","wikborg","ark","ruter","dn","maxbo","extra"]
_RL_SQ={"thon","ark"}  # kvadratiske merker trenger mer høyde for å veie like mye som ordmerkene
_rlogos=('<div class="rlogos" aria-hidden="true">'+"".join('<div class="rlc%s"><img src="%s" alt="%s"></div>'%(" sq" if s in _RL_SQ else "",U(_RLG[s]),NM[s]) for s in _RL_SLUGS if s in _RLG)+'</div>')
_tot=('<section class="dyp hero kort rov svh" style="color:#fff"><div class="wrap kw"><div class="svhg"><div><h1>Referanser</h1><p class="hl">Resultater hos kunder, med tall vi kan stå inne for. Se filmene, les historiene og møt dem som gjorde jobben.</p></div>'
 +_rlogos+'</div></div></section>')
_hl=[("ark",0,0),("wikborg-rein",0,0),("boligpartner",0,0)]
_band='<section class="rtop"><div class="wrap"><p class="rtt">Utvalgte tall</p><div class="rtg">'+"".join('<a href="Referanse-%s.dc.html"><b>%s</b><span>%s</span><i>%s</i></a>'%(s,_E5(_BYS[s]["kpi"][k]["v"]),_E5(_BYS[s]["kpi"][k]["l"]),_E5(_BYS[s]["nm"])) for s,k,_ in _hl)+'</div></div></section>'
_ov=_tot+_band+'<section class="wrap rgw"><div class="rcg three">'+"".join(_card(c) for c in CASES)+'</div></section><section class="wrap"><div class="kcta" style="margin-bottom:96px">'+_xw("ix")+'<div><h2>Vil dere være den neste?</h2><p>Fortell oss hva dere vil løse. Vi tar en uforpliktende samtale.</p><div class="kbs"><a class="kn g" href="Fagekspertene.dc.html">Finn riktig fagekspert</a><a class="kn l" href="mailto:post@excellerate.no">Send e-post</a></div></div></div></section>'
_write("Referanser.dc.html","Referanser, resultater hos kunder | Excellerate",_ov,2400,cta="La oss snakke om hvordan deres resultater kan se ut")

exec(open("omoss.py").read())
