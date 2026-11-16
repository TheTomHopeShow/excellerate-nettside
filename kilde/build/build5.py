# Kunnskapssenter: oversikt + artikkel + fagartikkel + e-bok (skjema) + arrangement (kjøres etter build4.py)
import html as _h5, re as _re5
_S5=open("style5.css").read()
_E5=_h5.escape
_BY={e[0]:e for e in EX}
def _ex(n): return _BY[n]
def _fn5(n): return _fn(n)
K1,K2,K3="6aee73de7614899efc4561a8f50ec8d6","db80b62da762e5e37fd701b9e92157de","0a081d31223ec6fa18fe5a9f2aa94d8b"
_IC={
 "sok":'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>',
 "lock":'<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 018 0v3"/></svg>',
 "list":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 6h12M8 12h12M8 18h12M4 6h.01M4 12h.01M4 18h.01"/></svg>',
 "lyd":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M11 5L6 9H3v6h3l5 4zM15.5 8.5a5 5 0 010 7M18.5 5.5a9 9 0 010 13"/></svg>',
 "del":'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.6 10.5l6.8-4M8.6 13.5l6.8 4"/></svg>',
 "li":'<b>in</b>',
 "x":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19" stroke-width="4"/></svg>',
}
def _xw(cls=""): return '<svg aria-hidden="true" viewBox="0 0 700 700"%s><line x1="80" y1="80" x2="620" y2="620" stroke-width="110"/><line x1="620" y1="80" x2="80" y2="620" stroke-width="110"/></svg>'%(' class="%s"'%cls if cls else "")
_TN={"art":"Artikkel","fag":"Fagartikkel","gui":"Guide","ebo":"E-bok","arr":"Arrangement"}
_OMN={"salg":"Salgsutvikling","ledelse":"Lederutvikling","kultur":"Kulturutvikling","ki":"KI og sikkerhet"}
def _av(n):
    if n and n in _BY: return '<img class="kav" src="%s" alt="">'%U(_BY[n][3])
    ini="".join(w[0] for w in (n or "E").replace(" og "," ").split()[:2]).upper()
    return '<span class="kav x" aria-hidden="true">%s</span>'%_E5(ini)
_POOL=["dummy-kultur","dummy-ledelse","4497"+"78221839df47ba9d0b43b87eccac","6c10bbc2090df8189f1fdb57970dafa0","849777fa2adc082495a1b5f2620cc53e",K1,K2,K3,"dummy-resepsjon2"]
_PC=[0]
def _pool():
    i=_PC[0];_PC[0]+=1;return _POOL[i%len(_POOL)]
def _kc(t,o,r,title,ing,forf=None,meta="",img=None,href="Kunnskap-Artikkel.dc.html",ex=False,dato=None,cover=None):
    if t in("gui","ebo"):
        top='<div class="kci"><img src="%s" alt=""><span class="kfmt">%s</span></div>'%(U(img or _pool()),"PDF-guide" if t=="gui" else "E-bok")
    elif t=="arr":
        d1,d2=dato or ("Dato","kommer")
        top='<div class="kci dk"><img src="%s" alt=""><div class="kdt"><b>%s</b><span>%s</span></div></div>'%(U(img or _pool()),_E5(d1),_E5(d2))
    else: top='<div class="kci"><img src="%s" alt=""></div>'%U(img or _pool())
    tag='<div class="ktr"><span class="ktag %s">%s</span>'%(t,_TN[t])+('<span class="kex">Eksempel</span>' if ex else "")+'</div>'
    if t=="arr": foot='<div class="kcf"><span class="klock">Se detaljer og meld deg på</span></div>'
    elif t in("ebo","gui"): foot='<div class="kcf"><span class="klock">%s Gratis med skjema</span></div>'%_IC["lock"]
    else: foot='<div class="kcf">%s<div><b>%s</b>%s</div></div>'%(_av(forf),_E5(forf or "Fagekspert"),_E5(meta))
    return '<a class="kc" data-t="%s" data-o="%s" data-r="%s" href="%s">%s<div class="kcb">%s<h3>%s</h3><p>%s</p>%s</div></a>'%(t,o,r,href,top,tag,_E5(title),_E5(ing),foot)
import json as _j5
_MN=["jan.","feb.","mars","apr.","mai","juni","juli","aug.","sep.","okt.","nov.","des."]
def _dt(d): y,m,dd=d.split("-"); return "%d. %s %s"%(int(dd),_MN[int(m)-1],y)
_OM={"Salgsutvikling":"salg","Ledelse":"ledelse","Strategi":"ledelse","Kultur":"kultur","Faglig utvikling":"kultur"}
_RO={"Salgsutvikling":"salg mark","Ledelse":"ceo","Strategi":"ceo","Kultur":"ceo","Faglig utvikling":"ceo"}
def _aslug5(s): return s.lower().replace("å","a").replace("ø","o").replace("æ","ae")
_EX16=_j5.load(open("ex16.json"))
for _a in _EX16:
    _a["id"]="kxa%02d"%_a["n"]
    _a["fmt"]="fag" if "Analyse" in _a["tags"] else "art"
    _a["o"]=" ".join(dict.fromkeys(_OM[t] for t in _a["tags"] if t in _OM)) or "ledelse"
    _a["r"]=" ".join(dict.fromkeys(x for t in _a["tags"] if t in _RO for x in _RO[t].split())) or "ceo"
_HUB=[(a["fmt"],a["o"],a["r"],dict(title=a["title"],ing=a["ing"],forf=a["author"],meta=_dt(a["date"]),img=a["id"],href="Kunnskap-%s.dc.html"%a["slug"].lower().replace("å","a").replace("ø","o").replace("æ","ae"))) for a in _EX16]
_HUB+=[
 ("ebo","salg","salg mark ceo",dict(title="Se sammenhengen mellom kvalitet og suksess",ing="Et konkret og praktisk verktøy som viser hvordan høyere kvalitet i salgsprosessen gir vekst og bedre resultater.",cover="ACT on FACT",href="Kunnskap-Ebok.dc.html")),
 ("arr","salg ledelse","salg mark ceo",dict(title="Den smarteste AI-veien til kundeinnsikt og utvikling",ing="Frokostmøte i Oslo, Stortorvet 7.",forf=None,dato=("16. sep","2026 · 08.00–10.00"),href="Kunnskap-Arrangement.dc.html")),
 ("gui","salg","salg mark",dict(title="Guide til gode kundeundersøkelser",ing="Hjelper bedriften med å identifisere forbedringspotensial og sette i gang tiltak som skaper vekst.",cover="Kundeundersøkelser",href="Kunnskap-Ebok.dc.html")),
 ("ebo","ledelse kultur","ceo",dict(title="Arbeidsglede i nedgangstider, 7 tiltak som sikrer fremgang",ing="Verktøyene du trenger for å lede med tydelighet, trygghet og fremtidstro.",cover="Arbeidsglede",href="Kunnskap-Ebok.dc.html")),
]
def _grid(): return "".join(_kc(t,o,r,**k) for t,o,r,k in _HUB)
_PILL=lambda v,l,on=False:'<button class="pill%s" data-v="%s">%s</button>'%(" on" if on else "",v,l)
_OPT=lambda l:"".join('<option value="%s">%s</option>'%(v,t) for v,t in l)
_FIL=('<div class="kfil2"><p class="ksent">Jeg er <label><select data-g="r" aria-label="Din rolle">'+_OPT([("","i ledergruppen"),("mark","markedsdirektør"),("salg","salgsdirektør"),("ceo","daglig leder"),("ki","ansvarlig for KI og compliance")])+'</select></label> og vil lære om <label><select data-g="o" aria-label="Område">'+_OPT([("","alt vi skriver om"),("salg","salgsutvikling"),("ledelse","lederutvikling"),("kultur","kulturutvikling"),("ki","KI og sikkerhet")])+'</select></label>.<button class="kn o ksw" data-reset type="button">Nullstill</button></p>'
 '<div class="ktabs" role="group" aria-label="Format">'+"".join('<button type="button" class="ktab%s" data-v="%s"><svg aria-hidden="true" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">%s</svg><b>%s</b><small>%s</small><span class="n"></span></button>'%(" on" if v=="" else "",v,ic,l,d) for v,l,d,ic in [("","Alt","Alt på ett sted",'<rect x="4" y="4" width="7" height="7" rx="1"/><rect x="13" y="4" width="7" height="7" rx="1"/><rect x="4" y="13" width="7" height="7" rx="1"/><rect x="13" y="13" width="7" height="7" rx="1"/>'),("art","Artikler","Korte og praktiske",'<path d="M5 5h14M5 10h14M5 15h9"/>'),("fag","Fagartikler","Dypere, med data",'<path d="M4 19V9M10 19V5M16 19v-7M21 19H3"/>'),("gui","Guider","Bruk dem selv",'<path d="M5 4h10l4 4v12H5z"/><path d="M9 13l2 2 4-4"/>'),("ebo","E-bøker","Last ned og les",'<path d="M5 5a2 2 0 012-2h11v16H7a2 2 0 00-2 2z"/>'),("arr","Arrangementer","Møt fagekspertene",'<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/>')])+'</div></div>')
def _fin(t,extra=""):
    return t
def _write(fn,title,body,h=3000,cta=None,nbm=False):
    foot=FOOTER
    if cta:
        foot=foot.replace('La oss ta en samtale om hva som mangler for at dere skal lykkes',cta,1)
    if nbm:
        # Nyhetsbrev-modulen (NBM, definert i v2.py): Kunnskapssenteret er
        # hovedsiden der det passer best, leseren er allerede i lære-modus.
        foot=foot.replace('<footer class="dyp fl"',NBM+'<footer class="dyp fl"',1)
    t=head(title)+HEADER+'<div class="kn5">'+body+'</div>'+foot+script(h)
    t=t.replace("<title>%s</title>"%title,"<title>%s</title>"%_E5(title),1)
    open(fn,"w").write(t)
    t=open(fn).read()
    t=t.replace(CSS,CSS+"\n"+_S2+"\n"+_S4+"\n"+_S5,1)
    t=t.replace('family=Schibsted+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet">',_INTER,1)
    open(fn,"w").write(t)
# ---------------- oversikt ----------------
_neda=_ex("Neda Maria Kaizumi"); _nS=PD[_neda[0]]["slug"]
_hub=('<section class="dyp hero kort" style="color:#fff"><div class="wrap kw"><h1>Kunnskapssenter</h1><p class="hl">Artikler, fagartikler, guider og arrangementer fra fagekspertene. Kunnskap skal deles.</p>'
 '<label class="ksok">'+_IC["sok"]+'<input type="search" placeholder="Søk i artikler, guider og arrangementer" aria-label="Søk"></label></div></section>'
 '<section style="background:#F3F6F5"><div class="wrap" style="padding-top:40px;padding-bottom:96px">'
 '<div class="kfe"><a class="kfb" href="Kunnskap-%s.dc.html"><img class="kfbg" src="%s" alt=""><span class="ktag fag">Fagartikkel</span><h2>%s</h2><p>%s</p><div class="kmeta" style="margin-top:22px"><span>%s</span><span>%s</span></div></a>'%(_aslug5(_EX16[13]["slug"]),U("kxa14"),_E5(_EX16[13]["title"]),_E5(_EX16[13]["ing"]),_E5(_EX16[13]["author"]),_dt(_EX16[13]["date"]))+
 '<div class="kfs"><a class="kfl" href="Kunnskap-%s.dc.html"><img class="kfi" src="%s" alt=""><span class="ktag art">Ny artikkel</span><h3>%s</h3><div class="kmeta"><span>%s</span><span>%s</span></div></a>'%(_aslug5(_EX16[2]["slug"]),U("kxa03"),_E5(_EX16[2]["title"]),_E5(_EX16[2]["author"]),_dt(_EX16[2]["date"]))+
 '<a class="kfl dato" href="Kunnskap-Arrangement.dc.html"><img class="kfi" src="%s" alt=""><span class="ktag arr">Neste arrangement</span><h3>Frokostmøte i Oslo</h3><div class="kmeta"><span>Dato kommer</span></div></a></div></div>'%U(K3)
 +_FIL+'<p class="kcount" aria-live="polite"></p><div class="kgr" data-f>'+_grid()+'</div>'
 '<div class="ktom">Ingen treff. <button class="kn o" data-reset type="button">Nullstill filter</button></div></div></section>'
 '<section class="kki">'+_hx()+'<div class="wrap"><h2>KI og sikkerhet</h2><p class="in">Et nytt område hos Excellerate. Her samler vi det vi vet om kvanteteknologi og trygg bruk av KI.</p>'
 '<div class="kkg"><a class="kkc" href="https://kvanteklar.no" target="_blank" rel="noopener"><small>kvanteklar.no</small><h3>Kvanteteknologi</h3><p>Kurs og produkter som gjør virksomheten klar for kvanteteknologi.</p><span class="lk">Gå til kvanteklar.no</span></a>'
 '<a class="kkc" href="https://sustainaiindex.com" target="_blank" rel="noopener"><small>sustainaiindex.com</small><h3>Sustain AI Index</h3><p>KI-compliance og validering, sammen med professorer og internasjonale aktører.</p><span class="lk">Gå til Sustain AI Index</span></a></div>'
 '<div class="kkx"><img src="%s" alt=""><span>Fagekspert på området er <a href="Fagekspert-%s.dc.html">%s</a>. <span style="color:#9FB6C3">Tekstene på kortene er forslag.</span></span></div></div></section>'%(U(_neda[3]),_nS,_neda[0])+
 '<section class="keb"><div class="wrap"><h2>Last ned e-bøker og guider</h2><p class="in">Gratis. Du oppgir navn og e-post, så sender vi deg dokumentet.</p><div class="kbg">'
 +"".join('<a class="kbk" href="Kunnskap-Ebok.dc.html"><div class="kci"><img src="%s" alt=""><span class="kfmt">%s</span></div><h3>%s</h3><span class="klock" style="margin:0">%s Last ned</span></a>'%(U(_pool()),"E-bok" if g=="" else "PDF-guide",_E5(t),_IC["lock"]) for g,c,t in [("","ACT on FACT","Se sammenhengen mellom kvalitet og suksess"),(" g","Arbeidsglede","Arbeidsglede i nedgangstider, 7 tiltak som sikrer fremgang"),("","Salg i dagens marked","Hvordan lykkes med salg i dagens marked?"),(" g","Kundeundersøkelser","Guide til gode kundeundersøkelser")])
 +'</div></div></section>')
_write("Kunnskap.dc.html","Kunnskapssenter | Excellerate",_hub,3200,nbm=True)
# ---------------- artikkel / fagartikkel ----------------
_FILL=["Her skriver fageksperten. Hold avsnittene korte, tre til fire linjer. Én tanke per avsnitt.","Start med det leseren lurer på, og svar tidlig. Forklar deretter hvorfor, og vis et konkret eksempel fra en kunde eller en samtale.","Bruk vanlige ord. Skriv slik du ville forklart det til en kollega over en kopp kaffe."]
def _p(n=2): return "".join("<p>%s</p>"%_FILL[i%3] for i in range(n))
def _fig(c): return '<figure><div class="kimg2">%s</div><figcaption>%s</figcaption></figure>'%(_xw(),c)
def _art(kind):
    fag=kind=="fag"
    au=_ex("Neda Maria Kaizumi") if fag else _ex("Arvid Madland Lyngnes")
    d=PD[au[0]]; slug=d["slug"]; fn=_fn5(au[0]); mail=d["mail"] or "post@excellerate.no"; tl=_tel(d["tlf"] or "22490000")
    title="KI-compliance, hva må på plass før dere skalerer?" if fag else "Fanger du opp kjøpssignalene?"
    ing=("Hva en leder bør vite om regelverk, validering og ansvar, før KI går fra pilot til drift." if fag else "Kundene dine sender ut signaler de selv ikke er bevisste på. Her er hva du bør lære deg å se etter.")
    secs=[("hva","Hva handler dette om?"),("slik","Slik gjør du det i praksis"),("tre","Tre ting du kan prøve denne uken"),("faq","Vanlige spørsmål"),("kilder","Kilder")]
    if fag: secs=[("bakgrunn","Bakgrunn og avgrensning"),("status","Hva sier regelverket?"),("modell","En modell for validering"),("sammenlign","Sammenligning av tilnærminger"),("case","Eksempel fra en virksomhet"),("anbefaling","Anbefalinger"),("faq","Vanlige spørsmål"),("kilder","Kilder")]
    toc="".join('<li><a href="#%s">%s</a></li>'%(i,t) for i,t in secs)
    body=""
    for i,t in secs:
        if i=="faq":
            body+='<h2 id="faq">Vanlige spørsmål</h2><div class="kfaq">'+"".join('<details><summary>%s</summary><p>%s</p></details>'%(q,_FILL[1]) for q in ["Spørsmål som leseren faktisk stiller, formulert slik de ville spurt?","Et kort, direkte svar kommer her.","Hvor lang tid tar det?"])+'</div>'
        elif i=="kilder":
            body+='<h2 id="kilder">Kilder</h2><ol class="kkil"><li>Kilde, utgiver og år. Lenke til originalen.</li><li>Kilde, utgiver og år. Lenke til originalen.</li><li>Kilde, utgiver og år. Lenke til originalen.</li></ol>'
        else:
            body+='<h2 id="%s">%s</h2>'%(i,t)+_p(2)
            if i in("slik","modell"): body+=_fig("Bildetekst. Beskriv hva leseren ser, og hvorfor det er med.")
            if i=="tre": body+='<ul><li>Første konkrete ting leseren kan gjøre.</li><li>Andre konkrete ting.</li><li>Tredje konkrete ting.</li></ul><div class="tip"><b>Tips fra %s</b><p>Én praktisk detalj som ikke står i fagbøkene.</p></div>'%_E5(fn)
            if i=="sammenlign": body+='<div class="ktb"><table><thead><tr><th>Tilnærming</th><th>Passer når</th><th>Obs</th></tr></thead><tbody><tr><td>Alternativ A</td><td>Kort beskrivelse</td><td>Kort beskrivelse</td></tr><tr><td>Alternativ B</td><td>Kort beskrivelse</td><td>Kort beskrivelse</td></tr><tr><td>Alternativ C</td><td>Kort beskrivelse</td><td>Kort beskrivelse</td></tr></tbody></table></div>'
            if i in("status","case","bakgrunn") and fag and i!="bakgrunn": body+='<blockquote>Et sitat fra en kunde eller kilde, kort nok til å stå alene.<cite>Navn, tittel, virksomhet</cite></blockquote>'
            if i=="hva" and not fag: body+='<blockquote>Et sitat fra en kunde eller kilde, kort nok til å stå alene.<cite>Navn, tittel, virksomhet</cite></blockquote>'
    sh=_IC
    kv=('<div class="kkv%s"><h2>%s</h2><ul><li>Hovedpoeng én, i en setning.</li><li>Hovedpoeng to, i en setning.</li><li>Hovedpoeng tre, i en setning.</li></ul></div>'%(" hf" if fag else "","Hovedfunn" if fag else "Kortversjonen"))
    meta='<div class="row"><span class="kchip">%s</span><span class="kmeta">Publisert 14. november 2026</span><span class="kmeta">Lesetid %s</span><span class="kex">Eksempel</span></div>'%("Fagartikkel · KI og sikkerhet" if fag else "Artikkel · Salgsutvikling","14 min" if fag else "5 min")
    import json as _j
    ld='<script type="application/ld+json">'+_j.dumps({"@context":"https://schema.org","@type":"Article","headline":title,"description":ing,"datePublished":"2026-11-14","dateModified":"2026-11-14","inLanguage":"nb","author":{"@type":"Person","name":au[0],"jobTitle":au[1],"url":"https://excellerate.no/konsulent/%s/"%slug},"publisher":{"@type":"Organization","name":"Excellerate AS","url":"https://excellerate.no"}},ensure_ascii=False)+'</script>'
    page=(ld+'<div class="kbar" aria-hidden="true"></div>'
     '<div class="ktm"><button type="button" aria-expanded="false">'+_IC["list"]+'Innhold<span></span><i></i></button><nav aria-label="Innhold">'+"".join('<a href="#%s">%s</a>'%(i,t) for i,t in secs)+'</nav><div class="pr"></div></div>'
     '<section class="wrap kah"><a class="kab" href="Kunnskap.dc.html">Kunnskapssenter</a><div class="kat">'+meta+'<h1>%s</h1><p class="kin">%s</p></div>'%(_E5(title),_E5(ing))
     +'<div class="kimg">'+_xw()+'</div><p class="kimgc">Bilde: plassholder</p></section>'
     '<section class="wrap kar"><div class="kl"><div class="kls"><nav class="ktoc" aria-label="Innhold"><h2>'+_IC["list"]+'Innhold</h2><ol>'+toc+'</ol></nav></div></div>'
     '<article class="kbd"><div class="kby"><img src="%s" alt=""><div><a class="nm" href="Fagekspert-%s.dc.html">%s</a><div class="rl">%s</div></div><div class="act"><button class="kbt" type="button" data-lytt>%s<span>Lytt til artikkel</span></button></div></div>'%(U(au[3]),slug,_E5(au[0]),_E5(au[1]),_IC["lyd"])
     +'<p class="kdat">Sist oppdatert 14. november 2026</p>'+kv
     +'<a class="kex2" href="Fagekspert-%s.dc.html"><img src="%s" alt=""><div><small>Artikkelens fagekspert</small><b>%s</b><span>%s. Se profil og book en samtale.</span></div><i class="pi"></i></a>'%(slug,U(au[3]),_E5(au[0]),_E5(au[1]))
     +body
     +'<div class="kcta">'+_xw("ix")+'<img src="%s" alt=""><div><h2>Ta en uforpliktende samtale</h2><p>Vil du høre hvordan dette ser ut hos dere? %s tar gjerne en prat.</p><div class="kbs"><a class="kn g" href="Fagekspert-%s.dc.html#book">Book en samtale</a><a class="kn l" href="mailto:%s">Send e-post</a><a class="kn l" href="tel:+47%s">Ring %s</a></div></div></div>'%(U(au[3]),_E5(fn),slug,mail,tl[0],tl[1])
     +'<div class="kne"><a class="kab" href="Kunnskap.dc.html">Alle artikler</a><a class="kab" href="Kunnskap.dc.html">Mer fra %s</a></div></article>'%_E5(fn)
     +'<div class="kr"><div class="krs"><button class="ik" type="button" data-share="li" aria-label="Del på LinkedIn">'+_IC["li"]+'</button><button class="ik" type="button" data-share="lenke" aria-label="Del eller kopier lenke">'+_IC["del"]+'</button><button class="top" type="button" data-top>Til toppen</button></div></div></section>'
     '<section class="krel"><div class="wrap"><h2>Les også</h2><div class="kgr">'
     +_kc("art","salg","salg",title="Tar salgsprosessen til et helt nytt nivå med AI",ing="Excellerate og Mentr.ai tar salgsutvikling inn i en ny æra.",forf=None,meta="Lesetid 5 min",img=K2)
     +_kc("fag","ledelse","ceo",title="Innsikten bak «riktig» lederfokus",ing="Fremtidens vinnere har den utviklingsorienterte tilnærmingen til ledelse.",forf=None,meta="Lesetid 12 min",href="Kunnskap-Fagartikkel.dc.html")
     +_kc("ebo","salg","salg",title="Se sammenhengen mellom kvalitet og suksess",ing="Et praktisk verktøy for salgsprosessen.",cover="ACT on FACT",href="Kunnskap-Ebok.dc.html")
     +'</div></div></section>')
    # JSON-LD slug-fiks
    return page
_write("Kunnskap-Artikkel.dc.html","Fanger du opp kjøpssignalene? | Excellerate",_art("art"),3400)
_write("Kunnskap-Fagartikkel.dc.html","KI-compliance, hva må på plass før dere skalerer? | Excellerate",_art("fag"),4200)
exec(open("kontakt.py").read())
exec(open("articles.py").read())
# ---------------- e-bok / lead magnet ----------------
def _form(knapp,etter_t,etter_p,etter_k,er_arr=False):
    rolle='<label>Rolle<select required><option value="">Velg rolle</option><option>Markedsdirektør</option><option>Salgsdirektør</option><option>Daglig leder</option><option>KI, juss eller compliance</option><option>Annet</option></select></label>'
    ekstra='<label>Hvordan vil du delta?<select required><option>På stedet</option><option>Digitalt</option></select></label>' if er_arr else ''
    return ('<form><div class="two"><label>Fornavn<input required autocomplete="given-name"></label><label>Etternavn<input required autocomplete="family-name"></label></div>'
     '<label>E-post<input type="email" required autocomplete="email"></label><label>Telefon<input type="tel" autocomplete="tel"></label>'
     '<div class="two"><label>Virksomhet<input autocomplete="organization"></label>'+rolle+'</div>'+ekstra+
     '<label class="ck"><input type="checkbox" required><span>Jeg godtar at Excellerate lagrer opplysningene mine for å sende meg dette. <a href="#">Personvern</a></span></label>'
     '<label class="ck"><input type="checkbox"><span>Jeg vil gjerne få nyhetsbrev og invitasjoner fra Excellerate. Valgfritt.</span></label>'
     '<button class="kn g" type="submit">%s</button></form>'
     '<div class="tk"><span class="ktag gui">Takk</span><h2>%s</h2><p class="sub">%s</p>%s</div>'
     '<p class="dm">Demo. Skjemaet sender ingenting ennå.</p>')%(knapp,etter_t,etter_p,etter_k)
_ea=_ex("Per Kjetil Parr"); _eaS=PD[_ea[0]]["slug"]
_eb=('<section class="dyp hero kort" style="color:#fff"><div class="wrap kw">'+_hx()+'<p class="crb"><a href="Kunnskap.dc.html">Kunnskapssenter</a> / E-bok</p><span class="ktag ebo" style="color:#fff">E-bok · Gratis</span><h1 style="margin-top:14px">Se sammenhengen mellom kvalitet og suksess</h1><p class="hl">Et konkret og praktisk verktøy som viser hvordan høyere kvalitet i salgsprosessen gir vekst og bedre resultater.</p></div></section>'
 '<section class="sec" style="padding-top:72px;padding-bottom:96px"><div class="wrap klm"><div>'
 '<h2 class="s" style="margin-top:0">Dette får du</h2><ul class="dg"><li>Punkt som forklarer hva leseren får ut av dokumentet.</li><li>Et konkret verktøy de kan bruke i neste møte.</li><li>Eksempler fra virkelige kunder.</li></ul>'
 '<h2 class="s">Hvem passer den for?</h2><p style="margin-top:14px;font-size:19px;line-height:31px;color:#33383B">Skriv to-tre setninger om hvem dokumentet er laget for, og hvilket problem det løser.</p>'
 '<h2 class="s">Skrevet av</h2><div class="ksp" style="grid-template-columns:1fr"><a href="Fagekspert-%s.dc.html"><img src="%s" alt=""><div><b>%s</b><span>%s</span></div></a></div>'%(_eaS,U(_ea[3]),_ea[0],_ea[1])+
 '<p class="knote" style="margin-top:40px"><i></i><span><b>Eksempel.</b> Forfatter og innhold er plassholdere. Tittel og beskrivelse er fra dagens e-bokside.</span></p></div>'
 '<aside class="kfo"><div class="kcvw"><div class="kcv"><small>EXCELLERATE</small><b>ACT on FACT</b></div></div><h2>Last ned e-boken</h2><p class="sub">Fyll ut skjemaet, så får du den med en gang.</p>'
 +_form("Last ned e-boken","Her er e-boken","Du får også en kopi på e-post.",'<a class="kn g" href="#">Åpne e-boken</a>')+'</aside></div></section>')
_write("Kunnskap-Ebok.dc.html","Se sammenhengen mellom kvalitet og suksess | Excellerate",_eb,2800)
# ---------------- arrangement ----------------
_sp=[_ex("Per Kjetil Parr"),_ex("Leif Ottesen")]
_ar=('<section class="dyp hero kort" style="color:#fff"><div class="wrap kw">'+_hx()+'<p class="crb"><a href="Kunnskap.dc.html">Kunnskapssenter</a> / Arrangement</p><span class="ktag arr" style="color:#fff">Frokostmøte</span><h1 style="margin-top:14px">Tittel på arrangementet</h1><p class="hl">Kort ingress som sier hva deltakerne tar med seg, og hvem det passer for.</p>'
 '<div class="kmx"><div><span>Dato</span><b>Kommer</b></div><div><span>Tid</span><b>08.00–10.00</b></div><div><span>Sted</span><b>Stortorvet 7, Oslo</b></div><div><span>Pris</span><b>Gratis</b></div></div></div></section>'
 '<section class="sec" style="padding-top:72px;padding-bottom:96px"><div class="wrap klm"><div>'
 '<h2 class="s" style="margin-top:0">Dette tar du med deg</h2><ul class="dg"><li>Første konkrete utbytte.</li><li>Andre konkrete utbytte.</li><li>Tredje konkrete utbytte.</li></ul>'
 '<h2 class="s">Program</h2><ol class="kpg"><li><time>08.00</time><div><b>Frokost og nettverk</b><span>Kort beskrivelse.</span></div></li><li><time>08.30</time><div><b>Innlegg fra fageksperten</b><span>Kort beskrivelse.</span></div></li><li><time>09.15</time><div><b>Samtale og spørsmål</b><span>Kort beskrivelse.</span></div></li><li><time>10.00</time><div><b>Slutt</b><span></span></div></li></ol>'
 '<h2 class="s">Med på scenen</h2><div class="ksp">'+"".join('<a href="Fagekspert-%s.dc.html"><img src="%s" alt=""><div><b>%s</b><span>%s</span></div></a>'%(PD[s[0]]["slug"],U(s[3]),s[0],s[1]) for s in _sp)+'</div>'
 '<p class="knote" style="margin-top:40px"><i></i><span><b>Eksempel.</b> Sted, klokkeslett og frokost er fra forrige frokostmøte (16. september 2026). Dato, program og innledere er plassholdere. Samme mal brukes for webinarer. Da byttes sted mot «Digitalt», og påmeldingen gir lenke på e-post.</span></p></div>'
 '<aside class="kfo"><span class="ktag arr">Påmelding</span><h2 style="margin-top:8px">Meld deg på</h2><p class="sub">Gratis. Du får bekreftelse på e-post.</p>'
 +_form("Meld meg på","Du er påmeldt","Vi sender bekreftelse og kalenderinvitasjon på e-post.",'<a class="kn o" href="#">Legg til i kalender</a>',True)+'</aside></div></section>')
_write("Kunnskap-Arrangement.dc.html","Frokostmøte | Excellerate",_ar,2800)
print("build5 ok")

# ---------------- Forsiden: ny rekkefølge ----------------
_fs=open("Forside.dc.html").read()
_hd=_fs.index("</header>")+len("</header>")
_pos=[m.start() for m in _re5.finditer(r'<(?:section|footer)[ >]',_fs) if m.start()>_hd]
_ch=[_fs[_pos[i]:_pos[i+1]] for i in range(len(_pos)-1)]
_tail=_fs[_pos[-1]:]
_name=["hero","logoer","mangler","sitat","resultater","fageksperter","slik","kunnskap","samtale","nyhetsbrev"]
assert len(_ch)==len(_name),(len(_ch))
_d=dict(zip(_name,_ch))
_d["slik"]=_d["slik"].replace('<section class="sec" style="padding-top:24px;padding-bottom:88px">','<section class="sec" style="background:#F3F6F5;padding-top:88px;padding-bottom:88px">',1)
_d["kunnskap"]=_d["kunnskap"].replace('<section style="background:#F3F6F5">','<section style="background:#fff">',1)
_ord=["hero","logoer","mangler","slik","resultater","sitat","fageksperter","kunnskap","samtale","nyhetsbrev"]
open("Forside.dc.html","w").write(_fs[:_pos[0]]+"".join(_d[k] for k in _ord)+_tail)
print("forside omordnet")
