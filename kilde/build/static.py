import re,os,shutil,json,html
exec(open("build.py").read().split("CSS=open")[0])   # EX, TOM, ids
P="/home/claude/fs/port2/"
FILES={
 "ada7e947b5c8e2c12becc01388af3908":("logo-xl.png","/home/claude/fs/img2/logo-xl.png"),
 "273ca0248b7b016d07f43035c6e9ccb9":("logo-xl-hvit.png","/home/claude/fs/img2/logo-xl-hvit.png"),
 "449778221839df47ba9d0b43b87eccac":("hero.jpg","/home/claude/fs/img2/hero.jpg"),
 "f2317b46c9c65fe0104ea745a8be3d6a":("case-thon.jpg","/home/claude/fs/img2/case-thon.jpg"),
 "e8f05e9ae6dc33aa02e3441e383e7070":("case-boligpartner.jpg","/home/claude/fs/img2/case-boligpartner.jpg"),
 "4e3a10f6a89f893e0cc65fedfaae7499":("case-wikborg.jpg","/home/claude/fs/img2/case-wikborg.jpg"),
}
for i,n in zip([l[0] for l in LOGOS],["logo-dn.png","logo-ramirent.jpg","logo-maxbo.jpg","logo-olivia.jpg","logo-synsam.jpg","logo-polarn.jpg"]):
    FILES[i]=(n,"/home/claude/fs/img2/"+n)
FILES.update({"krf01":("krf01.jpg","/home/claude/fs/img2/krf01.jpg"),"krf02":("krf02.jpg","/home/claude/fs/img2/krf02.jpg"),"krf03":("krf03.jpg","/home/claude/fs/img2/krf03.jpg"),"krf04":("krf04.jpg","/home/claude/fs/img2/krf04.jpg"),"krf05":("krf05.jpg","/home/claude/fs/img2/krf05.jpg"),"krf06":("krf06.jpg","/home/claude/fs/img2/krf06.jpg"),"krf07":("krf07.jpg","/home/claude/fs/img2/krf07.jpg"),"kxb01":("inl-01.jpg","/home/claude/fs/img2/inl-01.jpg"),"kxb02":("inl-02.jpg","/home/claude/fs/img2/inl-02.jpg"),"kxb03":("inl-03.jpg","/home/claude/fs/img2/inl-03.jpg"),"kxb04":("inl-04.jpg","/home/claude/fs/img2/inl-04.jpg"),"kxb05":("inl-05.jpg","/home/claude/fs/img2/inl-05.jpg"),"kxb06":("inl-06.jpg","/home/claude/fs/img2/inl-06.jpg"),"kxb07":("inl-07.jpg","/home/claude/fs/img2/inl-07.jpg"),"kxb08":("inl-08.jpg","/home/claude/fs/img2/inl-08.jpg"),"kxb09":("inl-09.jpg","/home/claude/fs/img2/inl-09.jpg"),"kxb10":("inl-10.jpg","/home/claude/fs/img2/inl-10.jpg"),"kxb11":("inl-11.jpg","/home/claude/fs/img2/inl-11.jpg"),"kxb12":("inl-12.jpg","/home/claude/fs/img2/inl-12.jpg"),"kxb13":("inl-13.jpg","/home/claude/fs/img2/inl-13.jpg"),"kxb14":("inl-14.jpg","/home/claude/fs/img2/inl-14.jpg"),"kxb15":("inl-15.jpg","/home/claude/fs/img2/inl-15.jpg"),"kxb16":("inl-16.jpg","/home/claude/fs/img2/inl-16.jpg"),"kxa01":("art-01.jpg","/home/claude/fs/img2/art-01.jpg"),"kxa02":("art-02.jpg","/home/claude/fs/img2/art-02.jpg"),"kxa03":("art-03.jpg","/home/claude/fs/img2/art-03.jpg"),"kxa04":("art-04.jpg","/home/claude/fs/img2/art-04.jpg"),"kxa05":("art-05.jpg","/home/claude/fs/img2/art-05.jpg"),"kxa06":("art-06.jpg","/home/claude/fs/img2/art-06.jpg"),"kxa07":("art-07.jpg","/home/claude/fs/img2/art-07.jpg"),"kxa08":("art-08.jpg","/home/claude/fs/img2/art-08.jpg"),"kxa09":("art-09.jpg","/home/claude/fs/img2/art-09.jpg"),"kxa10":("art-10.jpg","/home/claude/fs/img2/art-10.jpg"),"kxa11":("art-11.jpg","/home/claude/fs/img2/art-11.jpg"),"kxa12":("art-12.jpg","/home/claude/fs/img2/art-12.jpg"),"kxa13":("art-13.jpg","/home/claude/fs/img2/art-13.jpg"),"kxa14":("art-14.jpg","/home/claude/fs/img2/art-14.jpg"),"kxa15":("art-15.jpg","/home/claude/fs/img2/art-15.jpg"),"kxa16":("art-16.jpg","/home/claude/fs/img2/art-16.jpg"),"dummy-kultur":("dummy-kultur.jpg","/home/claude/fs/img2/kultur.jpg"),"dummy-ledelse":("dummy-ledelse.jpg","/home/claude/fs/img2/ledelse.jpg"),"dummy-resepsjon2":("dummy-hero2.jpg","/home/claude/fs/img2/case-wikborg.jpg"),"6aee73de7614899efc4561a8f50ec8d6":("kunnskap-artikler.jpg","/home/claude/fs/img2/ima221927.jpg"),"db80b62da762e5e37fd701b9e92157de":("kunnskap-guide.jpg","/home/claude/fs/img2/ima247254.jpg"),"0a081d31223ec6fa18fe5a9f2aa94d8b":("kunnskap-webinar.jpg","/home/claude/fs/img2/ima247313.jpg"),"849777fa2adc082495a1b5f2620cc53e":("salg.jpg","/home/claude/fs/img2/salg.jpg")})
exec(open("build.py").read().split("def logos")[0].split("LOGOS2=")[0] if False else "")
LG=[('dn', '75986caba0dfad1f626e6001440ce741'), ('ramirent', '073f67801711f3af9361815c73c48e45'), ('maxbo', '4fc5e3edfd43e5b30c5455dd7be5421a'), ('olivia', 'dcf3b4b9a0cbf12e3cd25d5762a539a5'), ('synsam', 'b7a727122b1f97cd786a6510795368b2'), ('polarn', 'f56939b7a719714c010de083d098e7d0'), ('thon', '14f9860af6633694b8167ae0b25622da'), ('boligpartner', 'd121a342e1c6cbabb2e7f27a679b3aea'), ('wikborg', '358607f0e262168a2eaa554fc54d3ff9'), ('fargerike', '3c96c29276610052d23e75b81adb13f1'), ('ferda', 'e71907b8a83cee7f30ad2ea6f694973d'), ('tv2', '8dad736121cdd657464d2f81f1f449ad'), ('ark', 'fbfd2783dd56195ebf28a32f7b62050c'), ('ruter', 'd7e797615a7b33627569773b14cc8cb5'), ('hertz', '6dfe181ef2bf7c9b751447484960330c'), ('extra', '8a8dba666d1dc28ff1fb7d0c4f267c56')]
for n,i in LG: FILES[i]=("logo-%s.png"%n,"/home/claude/fs/logos/%s.png"%n)
FILES["6c10bbc2090df8189f1fdb57970dafa0"]=("resepsjon.jpg","/home/claude/fs/img2/resepsjon.jpg")
pm={"per-kjetil":"6e79c34f6888cf0540771ec6fd3725e6","perchristian":"a9f9978820a3587c847a40de24da0e26","anne":"be853d39f56f0feaa31720a0f8c0b638","leif":"969b476beb8395999267c78979871aa5","carl":"a151209eaacecd8d6811f9016a082826","erik":"6cc98c6eaa36582248ae7c2544d2de76","neda":"8938c7306fc35962f98043cec2818075","morten":"8c85eb7736a88bbde93365d7b58aba04","petter":"6baef23b730b43fa4f20c43997c38364","arvid":"e42614462905675094d6d977aad41a30","rita":"dae83e810e9026d82587b7c5dfb21804","atle":"b769848d9f3cf7823afe4193d83e4ae5","janick":"8bf2abf8b8ba92ef0ea3bfc857964c3f","bard":"7c00fbd36f0c419cd1f6fe68d8e7ae30","paal":"3085cddbc4f266ad4f047a10548ac1d9","jorg":"83d996a6c37055cb52ba0b33b4f831d4","tom":"75486eeb0933d5c536faece725b36211"}
for n,i in pm.items(): FILES[i]=("portrett-%s.jpg"%n,P+n+".jpg")
FILES["thomasfehnportrait"]=("portrett-thomas.jpg",P+"thomas.jpg")
FILES["perGriwellportrait"]=("portrett-griwell.jpg",P+"griwell.jpg")
FILES["wikborgnyttbilde"]=("case-wikborg2.jpg","/home/claude/fs/img2/case-wikborg2.jpg")
FILES["sairegistry"]=("sai-registry.jpg","/home/claude/fs/img2/sai-registry.jpg")
FILES["saiposter"]=("sai-poster.jpg","/home/claude/fs/img2/sai-poster.jpg")
FILES["nedahero"]=("neda-hero.jpg","/home/claude/fs/img2/neda-hero.jpg")
FILES["nedastage"]=("neda-stage.jpg","/home/claude/fs/img2/neda-stage.jpg")
FILES["nedafull"]=("neda-stage-full.jpg","/home/claude/fs/img2/neda-stage-full.jpg")
FILES["stortorvet7"]=("stortorvet7.jpg","/home/claude/fs/img2/stortorvet7.jpg")
FILES["nedaai"]=("neda-ai-hero.jpg","/home/claude/fs/img2/neda-ai-hero.jpg")
OUT="/home/claude/fs/site/"
shutil.rmtree(OUT+"img",ignore_errors=True);os.makedirs(OUT+"img")
for i,(n,src) in FILES.items(): shutil.copy(src,OUT+"img/"+n)
os.makedirs(OUT+"video",exist_ok=True); shutil.copy("/home/claude/fs/video/sai-intro.mp4",OUT+"video/sai-intro.mp4")
PAGES={"Forside.dc.html":"index.html","Fagekspertene.dc.html":"fagekspertene.html"}
import glob
for _p in sorted(glob.glob("Fagekspert-*.dc.html")+glob.glob("Kunnskap*.dc.html")+glob.glob("Referanse*.dc.html")+glob.glob("Om-oss*.dc.html")+glob.glob("Kontakt.dc.html")+glob.glob("Tjenester*.dc.html")+glob.glob("Bransjer.dc.html")+glob.glob("GAP-Vision.dc.html")+glob.glob("Karriere.dc.html")+glob.glob("Karriere-Passer.dc.html")): PAGES[_p]=_p.replace(".dc","").lower()

_T="Tjenester.dc.html#"; _B="Bransjer.dc.html#"
_S="Tjenester-Salg.dc.html#";_L="Tjenester-Ledelse.dc.html#";_K="Tjenester-Kultur.dc.html#";_I="Tjenester-KI.dc.html#"
RULES=[("Rådgivende verdisalg",_S+"verdisalg"),("Kunstig intelligens i salg",_S+"ki-salg"),("Salgsledelse",_S+"finne"),("Kundeinnsikt",_S+"finne"),
 ("Strategi til handling",_L+"strategi"),("Coaching",_L+"program"),("Organisasjonsutvikling",_K+"metode"),("Prestasjonskultur",_K+"kulturen"),("Kommersiell kultur",_K+"kommersiell"),
 ("AI Act og compliance",_I+"aiact"),("AI Act",_I+"aiact"),("KI i hverdagen",_I+"ki-hverdag"),("Informasjonssikkerhet",_I+"infosikkerhet"),
 ("Salgsutvikling","Tjenester-Salg.dc.html"),("Lederutvikling","Tjenester-Ledelse.dc.html"),("Kulturutvikling","Tjenester-Kultur.dc.html"),("KI, adopsjon og sikkerhet","Tjenester-KI.dc.html"),("KI og sikkerhet","Tjenester-KI.dc.html"),
 ("Se alle tjenester","Tjenester.dc.html"),("Tjenester","Tjenester.dc.html"),("Se alle bransjer","Bransjer.dc.html"),("Bransjer","Bransjer.dc.html"),
 ("Kjøpssignaler","Kunnskap-fanger-du-opp-kjopssignalene.dc.html"),("Arbeidsglede","Kunnskap-glede-viktigere-enn-trivsel-tilfredshet.dc.html"),
 ("Book en samtale","Kontakt.dc.html"),("Personvern","https://excellerate.no/personvern/"),("Se hvordan vi jobber","Om-oss.dc.html#gjor"),("GAP Vision AI lansert","https://excellerate.no/gap-vision/gap-vision-ai/"),("GAP Vision","GAP-Vision.dc.html"),
 ("KompetanseKundedrevet",_S+"finne"),("Kundedrevet kompetanseutvikling",_S+"finne"),("LedelseUtviklingsplaner","Tjenester-Ledelse.dc.html"),("Utviklingsplaner for ledere","Tjenester-Ledelse.dc.html"),("SalgSalgs- og","Tjenester-Salg.dc.html"),("Salgs- og leveranseverdikjeder","Tjenester-Salg.dc.html"),
 ("Thon Hotels","Referanse-thon.dc.html"),("ReferanseThon Hotels","Referanse-thon.dc.html"),("BoligPartner","Referanse-boligpartner.dc.html"),("Wikborg Rein","Referanse-wikborg-rein.dc.html"),
 ("Handel og forhandlernett",_B+"handel"),("Retail og faghandel",_B+"handel"),("Bil",_B+"handel"),("Bank, forsikring og eiendomsmegling",_B+"bank"),("Sparebank",_B+"bank"),("Forsikring",_B+"bank"),("Megling",_B+"bank"),
 ("Bygg og eiendom",_B+"bygg"),("Entreprenør og anlegg",_B+"bygg"),("Tekniske fag",_B+"bygg"),("Utleie og drift",_B+"bygg"),("IT og teknologi",_B+"it"),("Programvare",_B+"it"),("Konsulent",_B+"it"),("Drift",_B+"it")]
def fixlinks(body):
    import re as _r
    def f(m):
        t=_r.sub(r"<[^>]+>","",m.group(3)).strip()
        for k,h in RULES:
            if t.startswith(k): return m.group(1)+'href="%s"'%h+m.group(2)+m.group(3)+"</a>"
        return m.group(0)
    return _r.sub(r'(<a\b[^>]*?)href="#"([^>]*>)(.*?)</a>',f,body,flags=_r.S)
def conv(name):
    s=open(name).read()
    title=re.search(r"<title>(.*?)</title>",s).group(1)
    title={"Fagekspertene.dc.html":"Fagekspertene | Excellerate","Kunnskap.dc.html":"Kunnskapssenter, artikler og guider | Excellerate","Kunnskap-Arrangement.dc.html":"Frokostmøte og webinar | Excellerate"}.get(name,title)
    css=re.search(r"<style>\n(.*?)</style>",s,re.S).group(1)
    css+="\n"+open('style6.css').read()+"\n"+open('style7.css').read()
    body=re.search(r'<div style="width:100%;background:#fff;position:relative">\n(.*)</div>\n</x-dc>',s,re.S).group(1)
    body=fixlinks(body)
    for i,(n,_) in FILES.items(): body=body.replace("/_blob/"+i,"img/"+n)
    for k,v in PAGES.items(): body=body.replace(k,v)
    body=body.replace('Fagekspert.dc.html','fagekspertene.html')
    body=body.replace('Kunnskap.dc.html','kunnskap.html')
    body=body.replace('onClick="{{toggleMeny}}" aria-expanded="{{menyAapen}}">{{menyTekst}}','id="mbtn" aria-expanded="false">Meny')
    body=body.replace('<div style="{{menyStil}}">','<div id="mpanel" style="display:none">\n<div class="wrap msok"><label for="sk" class="msokf"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#356A89" stroke-width="2" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/></svg><span>Søk</span></label></div>')
    # Mobil: søk flyttet inn i menyen (avtalt 16.11.2026). Søkeikonet (.sbtn) skjules i
    # toppen på mobil via CSS (.skx:not(:checked) ~ .wrap .sbtn), og et søkefelt øverst
    # i mobilmenyen (.msokf) åpner i stedet det vanlige søkepanelet ved å krysse av #sk.
    js="""
const b=document.getElementById('mbtn'),p=document.getElementById('mpanel');p.addEventListener('click',e=>{if(e.target.closest('a'))b.click()});(()=>{const sk=document.getElementById('sk'),ms=p.querySelector('.msokf');if(!sk||!ms)return;ms.addEventListener('click',e=>{e.preventDefault();sk.checked=true;b.click();const i=document.getElementById('sinp');if(i)i.focus()});b.addEventListener('click',()=>{if(b.getAttribute('aria-expanded')!=='true')sk.checked=false})})();document.addEventListener('keydown',e=>{if(e.key==='Escape'&&b.getAttribute('aria-expanded')==='true')b.click()});
b.addEventListener('click',()=>{const o=b.getAttribute('aria-expanded')!=='true';b.setAttribute('aria-expanded',o);b.textContent=o?'Lukk':'Meny';p.style.cssText=o?'position:absolute;left:0;right:0;top:80px;background:#fff;border-bottom:1px solid #C5D2D8;max-height:calc(100vh - 80px);overflow:auto;box-shadow:0 18px 30px rgba(27,58,75,.12)':'display:none'});
"""
    if name.startswith("Forside"):
        STEG=re.search(r"const STEG = (\[.*?\]);",open("build.py").read(),re.S).group(1)
        for i in range(3):
            body=body.replace('<button class="{{c%d}}" onClick="{{v%d}}">'%(i,i),'<button class="st%s" data-i="%d">'%(" on" if i==0 else "",i))
        body=body.replace("{{stegTittel}}",'<span id="sT">Innsikt og fakta</span>').replace("{{stegTekst}}",'<span id="sX">Vi starter med å forstå hvor dere står, før vi foreslår noe. Fakta fra kunder, selgere og ledere gir et felles utgangspunkt.</span>').replace("{{stegDere}}",'<span id="sD">Et felles faktagrunnlag. En tydelig beskrivelse av hva som mangler.</span>')
        js+="const STEG="+re.sub(r"(\w):","\\1:",STEG)+";document.querySelectorAll('button.st').forEach(x=>x.addEventListener('click',()=>{const i=+x.dataset.i;document.querySelectorAll('button.st').forEach(y=>y.className='st'+(y===x?' on':''));sT.textContent=STEG[i].t;sX.textContent=STEG[i].x;sD.textContent=STEG[i].d}));"
    if name.startswith("Forside"):
        js+="""(()=>{const sl=[...document.querySelectorAll('.qslide')],dt=[...document.querySelectorAll('.qd')],box=document.querySelector('.qrot');if(!box||sl.length<2)return;let i=0,t,paused=false;const go=n=>{i=(n+sl.length)%sl.length;sl.forEach((s,k)=>s.classList.toggle('on',k===i));dt.forEach((d,k)=>d.classList.toggle('on',k===i))};const start=()=>{clearInterval(t);if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;t=setInterval(()=>{if(!paused)go(i+1)},7000)};dt.forEach((d,k)=>d.addEventListener('click',()=>{go(k);start()}));box.addEventListener('mouseenter',()=>paused=true);box.addEventListener('mouseleave',()=>paused=false);box.addEventListener('focusin',()=>paused=true);box.addEventListener('focusout',()=>paused=false);start()})();"""
    if name.startswith("Forside"):
        js+="""(()=>{const t=document.querySelector('.tog'),bs=[...document.querySelectorAll('.tgb')];if(!t||!bs.length)return;const up=()=>{bs[0].disabled=t.scrollLeft<8;bs[1].disabled=t.scrollLeft>t.scrollWidth-t.clientWidth-8};bs.forEach(b=>b.addEventListener('click',()=>t.scrollBy({left:(+b.dataset.d)*688,behavior:'smooth'})));t.addEventListener('scroll',up,{passive:true});addEventListener('resize',up);up()})();"""
    js+="""const si=document.getElementById('sinp');if(si)si.addEventListener('input',()=>{const q=si.value.trim().toLowerCase();document.querySelectorAll('.mxsk,.sok .mxa').forEach(c=>{const m=q?c.dataset.n.includes(q):!c.classList.contains('more');c.style.display=m?'flex':'none'})});"""
    if name.startswith("Forside"):
        js+="""document.querySelectorAll('.lrow').forEach((row,k)=>{const tr=row.firstElementChild;tr.style.animation='none';let half=0,hov=false,drag=false,lx=0;const h=()=>{half=(tr.scrollWidth+20)/2};h();addEventListener('load',h);row.scrollLeft=k?half:0;row.addEventListener('mouseenter',()=>hov=true);row.addEventListener('mouseleave',()=>{hov=false;drag=false});row.addEventListener('pointerdown',e=>{drag=true;lx=e.clientX});addEventListener('pointerup',()=>drag=false);row.addEventListener('pointermove',e=>{if(!drag)return;row.scrollLeft-=e.clientX-lx;lx=e.clientX});const rm=matchMedia('(prefers-reduced-motion:reduce)').matches;const step=()=>{if(!hov&&!drag&&!rm)row.scrollLeft+=k?-0.45:0.45;if(row.scrollLeft>=half)row.scrollLeft-=half;if(row.scrollLeft<=0)row.scrollLeft+=half;requestAnimationFrame(step)};step()});"""
    if name.startswith("Fagekspert-"): js+=open("booking.js").read()
    if name.startswith("Kunnskap"): js+=open("kunnskap.js").read()
    if name.startswith("Referanse"): js+=open("ref.js").read()
    if name.startswith(("Om-oss","Kontakt")): js+=open("om.js").read()
    if name.startswith("Fagekspertene"):
        js+="const F=['','salg','ledelse','kultur','ki'];document.querySelectorAll('button.pill').forEach(x=>x.addEventListener('click',()=>{const f=+x.dataset.f;document.querySelectorAll('button.pill').forEach(y=>y.classList.toggle('on',y===x));document.querySelectorAll('.fgr .fx').forEach(c=>{const o=(c.dataset.omr||'').split(' ');c.classList.toggle('gjem',f!==0&&o.indexOf(F[f])<0)})}));"
    js+="document.querySelectorAll('a[href=\"#\"]').forEach(a=>{a.title='Kommer';a.addEventListener('click',e=>e.preventDefault())});"
    _hi=body.index("</header>")+9
    _hh,_bb=body[:_hi],body[_hi:]
    _hh=_hh.replace("<h3>","<p class=\"mxt\">").replace("</h3>","</p>")
    _bb=_bb.replace('<section id="samtale"','<main id="main"><section id="samtale"',0)
    # lazy loading på alle bilder under første skjerm
    _first=_bb.find("</section>")
    _rest=re.sub(r'<img (?![^>]*loading=)',r'<img loading="lazy" decoding="async" ',_bb[_first:])
    _bb=_bb[:_first]+_rest
    # main rundt innholdet (fra første seksjon til footer)
    _fi=_bb.rfind('<footer')
    if _fi>0: _bb='<main id="main">'+_bb[:_fi]+'</main>'+_bb[_fi:]
    body='<a class="skip" href="#main">Hopp til innhold</a>'+_hh+_bb
    _m=re.search(r'class="(?:kin|hl)">(.*?)</p>',body)
    if name.startswith("Forside"): _d="Excellerate hjelper ledere med å styrke konkurransekraften gjennom salgsutvikling, lederutvikling og kulturutvikling. Siden 1988."
    elif name.startswith("Fagekspert-"):
        _n=re.search(r"<h1>(.*?)</h1>",body).group(1); _v=re.search(r'class="vl">(.*?)</p>',body); _c=re.findall(r'<div class="cs">(.*?)</div>',body)
        _a=", ".join(re.findall(r"<span>(.*?)</span>",_c[0])).lower() if _c else ""
        _d=(_n+" er fagekspert hos Excellerate"+(" innen "+_a if _a else "")+". "+(re.sub(r"<[^>]+>","",_v.group(1)).rstrip(".")+". " if _v else "")+"Book en samtale direkte.")
        if len(_d)>160: _d=_n+" er fagekspert hos Excellerate"+(" innen "+_a if _a else "")+". Book en samtale direkte."
    elif _m: _d=re.sub(r"<[^>]+>","",_m.group(1))
    else: _d=title.split(" | ")[0]+" hos Excellerate."
    if name=="Kunnskap-Arrangement.dc.html": _d="Frokostmøte eller webinar med fagekspertene i Excellerate. Se program, tid og sted, og meld deg på."
    _d=html.escape(_d,quote=True)
    meta=f'<meta name="description" content="{_d}"><meta property="og:title" content="{html.escape(title,quote=True)}"><meta property="og:description" content="{_d}"><meta property="og:type" content="website"><meta property="og:locale" content="nb_NO"><meta name="theme-color" content="#1B3A4B"><meta name="robots" content="noindex,nofollow">'
    assert "{{" not in body,(name,re.findall(r".{60}\{\{.{40}",body)[:3])
    return f'''<!doctype html>
<html lang="nb"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>{meta}
<link rel="preload" href="fonts/inter-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<style>
@font-face{{font-family:'Inter';font-style:normal;font-weight:100 900;font-display:swap;src:url(fonts/inter-latin-wght-normal.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}}@font-face{{font-family:'Inter';font-style:normal;font-weight:100 900;font-display:swap;src:url(fonts/inter-latin-ext-wght-normal.woff2) format('woff2');unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}}
{css}
html,body{{overflow-x:clip}}</style></head><body>
<div style="width:100%;background:#fff;position:relative">
{body}</div>
<script>{js}</script></body></html>'''
import re as _re
def _ext(h):
    def f(m):
        t=m.group(0)
        if 'target=' in t: return t
        t=_re.sub(r'\s*rel="[^"]*"','',t)
        return t[:-1]+' target="_blank" rel="noopener noreferrer">'
    return _re.sub(r'<a [^>]*href="https?://[^"]*"[^>]*>',f,h)
for k,v in PAGES.items(): open(OUT+v,"w").write(_ext(conv(k)))
print(os.listdir(OUT),len(os.listdir(OUT+"img")))
