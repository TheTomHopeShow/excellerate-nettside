# Nye Fagekspertene- og Fagekspert-sider i forsidens format (kjøres på slutten av build.py)
exec(open('personer.py').read()); PD=P
import re as _re
_fs=open("Forside.dc.html").read()
_m=_re.search(r'<section id="samtale" class="dyp".*?</section>',_fs,_re.S)
_old=_re.search(r'<section id="samtale" class="dyp".*?</section>',FOOTER,_re.S)
if _m and _old and "post@excellerate.no</a>" in _m.group(0): FOOTER=FOOTER.replace(_old.group(0),_m.group(0),1)
_S2=open("style2.css").read(); _S4=open("style4.css").read()
_INTER='family=Schibsted+Grotesk:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
def _xs(): return '<svg aria-hidden="true" viewBox="0 0 700 700" class="ix"><line x1="80" y1="80" x2="620" y2="620" stroke-width="110"/><line x1="620" y1="80" x2="80" y2="620" stroke-width="110"/></svg>'
def _hx(): return '<svg aria-hidden="true" viewBox="0 0 700 700" class="hx"><line x1="80" y1="80" x2="620" y2="620" stroke-width="110"/><line x1="620" y1="80" x2="80" y2="620" stroke-width="110"/></svg>'
_CH={"salg":"Salg","ledelse":"Ledelse","kultur":"Kultur","ki":"KI"}
def _fx(e):
    img='<img src="%s" alt="%s">'%(U(e[3]),e[0]) if e[3] else '<span class="fxph">TH</span>'
    ch="".join('<span class="fxch">%s</span>'%_CH[o] for o in e[4].split() if o in _CH)
    href="Fagekspert-%s.dc.html"%PD[e[0]]["slug"] if e[0] in PD else "Fagekspertene.dc.html"
    return '<a class="fx" data-omr="%s" href="%s">'%(e[4],href)+_xs()+'<div class="fxp">%s<span class="fxa" aria-hidden="true"></span></div><div class="fxt"><h3>%s</h3><p class="r">%s</p><p class="t">%s</p><div class="fxcs">%s</div></div></a>'%(img,e[0],e[1],e[2],ch)
def _page(path, body):
    t=open(path).read()
    t=t.replace(CSS,CSS+"\n"+_S2+"\n"+_S4,1)
    t=t.replace('family=Schibsted+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet">',_INTER,1)
    return t
# ---- oversikt ----
_ov=head("Fagekspertene")+HEADER
_ov+='''<section class="dyp hero kort" style="color:#fff"><div class="wrap kw">'''+_hx()+'''<h1>Fagekspertene</h1><p class="hl">Ett team med erfaring fra salg, ledelse og kultur. Vi er organisert med ett mål for øyet, å sikre våre kunder økt resultat og konkurransekraft.</p></div></section>
<section style="background:#F3F6F5"><div class="wrap" style="padding-top:40px;padding-bottom:96px">
<div class="fpl" role="group" aria-label="Filtrer på område"><button class="pill on" data-f="0">Alle</button><button class="pill" data-f="1">Salgsutvikling</button><button class="pill" data-f="2">Lederutvikling</button><button class="pill" data-f="3">Kulturutvikling</button><button class="pill" data-f="4">KI og sikkerhet</button></div>
<div class="fgr">'''+"".join(_fx(e) for e in LED+EXP)+'''</div></div></section>'''
# Nyhetsbrev-modulen (NBM, definert i v2.py) legges inn her: Fagekspertene er en
# hovedside der leseren er i "bli kjent"-modus, ikke klar til å booke møte ennå.
_foot_fe=FOOTER.replace('<footer class="dyp fl"',NBM+'<footer class="dyp fl"',1)
open("Fagekspertene.dc.html","w").write(_ov+_foot_fe+script(3000))
# ---- enkeltsider: én per fagekspert (Per Kjetil er malen) ----
import html as _h
_FN={"Arvid Madland Lyngnes":"Arvid","Bård Fossli Jensen":"Bård","Rita Berg Hansen":"Rita"}
_OMR={"salg":"Salgsutvikling","ledelse":"Lederutvikling","kultur":"Kulturutvikling","ki":"KI og sikkerhet"}
def _fn(n): return _FN.get(n," ".join(n.split()[:-1]))
def _tel(t):
    d="".join(c for c in t if c.isdigit())
    if d.startswith("47") and len(d)==10: d=d[2:]
    return d,"%s %s %s"%(d[:3],d[3:5],d[5:])
_hj=lambda o,t:'<a class="ing" href="#"><span class="io">%s</span><h3>%s</h3></a>'%(o,t)
_E=_h.escape
def _person(e):
    d=PD[e[0]]; fn=_fn(e[0]); slug=d["slug"]
    mail=d["mail"] or "post@excellerate.no"
    tl=_tel(d["tlf"] or "22490000")
    chips=["Salgsutvikling","Lederutvikling","Organisasjonsutvikling"] if e[0]=="Per Kjetil Parr" else [_OMR[o] for o in e[4].split() if o in _OMR]
    cs='<div class="cs">'+"".join("<span>%s</span>"%c for c in chips)+"</div>" if chips else ""
    om=d["om"]; _k=1 if len(om[0])>=450 else 2; vis=om[:_k]; rest=om[_k:]
    more=""
    if rest or d["erf"]:
        more='<details class="lm"><summary class="kn o"><span class="m1">Les mer om %s</span><span class="m2">Les mindre</span></summary><div class="lmb">'%_E(fn)
        more+="".join("<p>%s</p>"%_E(p) for p in rest)
        if d["erf"]:
            more+="<h3>%s</h3>"%_E(d.get("erf_tittel","Noen av %s sine erfaringer"%(fn if e[0]!="Per Kjetil Parr" else fn)))
            more+="".join("<p>%s</p>"%_E(p) for p in d["erf"])
        more+="</div></details>"
    _linksvg='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><path d="M15 3h6v6"/><path d="M10 14 21 3"/></svg>'
    li='<a class="kn l" href="https://www.linkedin.com/in/%s" target="_blank" rel="noopener noreferrer">%s LinkedIn</a>'%(d["li"],_linksvg) if d["li"] else ""
    t=head("Fagekspert")+HEADER
    t=t.replace("<title>Fagekspert</title>","<title>%s | Excellerate</title>"%_E(e[0]),1)
    t+='<section class="dyp hero kort" style="color:#fff"><div class="wrap kw">'+_hx()+'<p class="crb"><a href="Fagekspertene.dc.html">Fagekspertene</a> / %s</p>'%_E(e[0])
    t+='<div class="pg2"><div><p class="rl">%s</p><h1>%s</h1><p class="vl">%s</p>%s'%(_E(e[1]),_E(e[0]),_E(d["linje"]),cs)
    t+='<div class="bt2"><a class="kn g" href="mailto:%s">Send e-post</a>'%mail
    t+='<a class="kn l" href="tel:+47%s">Ring %s</a>'%tl+li+'</div></div>'
    t+='<div class="pf"><img src="%s" alt="%s"><span class="dt"></span></div></div></div></section>'%(U(e[3]),_E(e[0]))
    t+='<section class="sec" style="padding-top:72px;padding-bottom:72px"><div class="wrap fk"><div><h2>Om %s</h2>'%_E(fn)+"".join("<p>%s</p>"%_E(p) for p in vis)+more+'</div>'
    bk='<div class="bk bkc" id="bk" data-s="1"><div class="bkl"><div class="bkn2"><button type="button" class="bkp" aria-label="Forrige måned">&#8249;</button><span class="bkm"></span><button type="button" class="bkn" aria-label="Neste måned">&#8250;</button></div><div class="bkg"></div></div>'
    bk+='<div class="bkr"><ol class="bks"><li>Dag</li><li>Tid</li><li>Dine opplysninger</li></ol><button type="button" class="bkb">&#8249; Tilbake</button><h4 class="bkd">Velg tid</h4><p class="bkh">Velg en dag i kalenderen først.</p><div class="bkt"></div><p class="bkx"></p><form class="bkf"><label>Navn<input required autocomplete="name"></label><label>E-post<input type="email" required autocomplete="email"></label><label>Telefon (valgfritt)<input type="tel" autocomplete="tel"></label><button class="kn g" type="submit">Bekreft møtet</button></form><p class="bkdone"></p></div></div><p class="bkdemo">Eksempeltider. Kalenderen er ikke koblet til ekte kalender ennå.</p>'
    t+='<aside class="fkc dk" id="book">'+_xs()+'<img class="pav" src="%s" alt=""><h3>Møt %s</h3><p class="sub">Samtale på 30 minutter</p>'%(U(e[3]),_E(fn))+bk+'</aside></div></section>'
    if e[0]=="Per Kjetil Parr":
        t+='<section class="sec" style="background:#F3F6F5;padding-top:72px;padding-bottom:72px"><div class="wrap"><h2 style="font-size:36px;line-height:42px;font-weight:500">Dette hjelper Per Kjetil med</h2><div class="hj3">'+_hj("Kompetanse","Kundedrevet kompetanseutvikling")+_hj("Ledelse","Utviklingsplaner for ledere")+_hj("Salg","Salgs- og leveranseverdikjeder")+'</div></div></section>'
        q='«Med dyktig ledelse og assistanse fra spesialister i Excellerate, har selskapet løftet den kommersielle kulturen til et nytt nivå.»'
        who='<img src="/_blob/perGriwellportrait" alt="Per Griwell" style="width:64px;height:64px;border-radius:50%;object-fit:cover;object-position:50% 14%"><div><b style="display:block;font-size:17px;font-weight:600">Per Griwell</b><span style="font-size:15px;color:#566B76">Kommersiell direktør, Thon Hotels</span></div>'
    elif d["sitat"]:
        q='«%s»'%_E(d["sitat"])
        who='<img src="%s" alt="%s" style="width:64px;height:64px;border-radius:50%%;object-fit:cover;object-position:50%% 14%%"><div><b style="display:block;font-size:17px;font-weight:600">%s</b><span style="font-size:15px;color:#566B76">%s</span></div>'%(U(e[3]),_E(e[0]),_E(e[0]),_E(e[1]))
    else: q=None
    if q:
        fs="clamp(22px,2.6vw,32px)" if len(q)>200 else "clamp(26px,3.6vw,44px)"
        t+='<section class="sec" style="position:relative;overflow:hidden;background:#EAF0EC;padding-top:96px;padding-bottom:96px"><svg aria-hidden="true" viewBox="0 0 700 700" style="position:absolute;right:-120px;bottom:-200px;width:620px;height:620px;pointer-events:none"><line x1="80" y1="80" x2="620" y2="620" stroke="#DCE7E0" stroke-width="110"/><line x1="620" y1="80" x2="80" y2="620" stroke="#DCE7E0" stroke-width="110"/></svg><div class="wrap" style="position:relative"><span style="display:block;width:18px;height:18px;border-radius:50%;background:#7EA257;margin-bottom:32px"></span><p style="font-size:'+fs+';line-height:1.28;letter-spacing:-.03em;font-weight:500;color:#1B3A4B;max-width:30em">'+q+'</p><div style="margin-top:36px;display:flex;gap:16px;align-items:center">'+who+'</div></div></section>'
    fn_="Fagekspert-%s.dc.html"%slug
    t=t+FOOTER.replace('<a class="kn g" href="#">Book en samtale','<a class="kn g" href="#book">Book en samtale')+script(2700)
    open(fn_,"w").write(t)
    return fn_
_pages=["Fagekspertene.dc.html"]+[_person(e) for e in EX+[TOM]]
for _f in _pages:
    _n=_page(_f,None)
    open(_f,"w").write(_n)
