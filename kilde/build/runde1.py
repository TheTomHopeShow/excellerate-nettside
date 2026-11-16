# Runde 1 etter gjennomgangen 15.11.2026 (avtalt med Tom): fart, meny, tilgjengelighet, telefonformat, skygger.
import re,glob
GIF="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="
JS='<script id="menybilder">(function(){var h=document.querySelector("header.hdr nav.hnav");if(!h)return;var d=0;function last(){if(d)return;d=1;h.querySelectorAll("img[data-src]").forEach(function(i){i.src=i.getAttribute("data-src");i.removeAttribute("data-src")})}["pointerenter","focusin","touchstart","click"].forEach(function(e){h.addEventListener(e,last,{passive:true})})})();</script>'
# Rettet 16.11.2026: lytteren sto på hele header.hdr, ikke bare nav.hnav (megamenyen).
# Det gjorde at et trykk på mobilmenyknappen (#mbtn, som også ligger i header.hdr)
# trigget nedlasting av alle megameny-bildene (28 bilder, over 1 MB), selv om de
# aldri vises i mobilmenyen (#mpanel har bare tekstlenker, ingen bilder).
# nav.hnav er display:none på mobil, og et skjult element mottar ingen pointer-/
# touch-/klikk-hendelser, så lytteren kan nå aldri trigges fra mobilmenyen.
BRID=["handel","bank","bygg","it"]
def tlf(d):
    return "+47 %s %s %s %s"%(d[:2],d[2:4],d[4:6],d[6:]) if d[0]=="2" else "+47 %s %s %s"%(d[:3],d[3:5],d[5:])
def segs(t,fn):  # kjør fn på tekst utenfor tagger, script og style
    out=[];i=0
    for m in re.finditer(r'<script.*?</script>|<style.*?</style>|<[^>]+>',t,re.S):
        out.append(fn(t[i:m.start()]));out.append(m.group(0));i=m.end()
    out.append(fn(t[i:]));return "".join(out)
for p in sorted(glob.glob("/home/claude/fs/site/*.html")):
    n=p.split("/")[-1][:-5];t=open(p).read()
    hm=re.search(r'<header class="hdr">.*?</header>',t,re.S)
    if hm:
        h=hm.group(0)
        # 1 menybilder lastes først ved bruk (ikke logoen)
        a,b=h.split('<nav class="hnav"',1)
        b=re.sub(r'<img((?:(?!data-src)[^>])*?)\ssrc="(img/[^"]+)"',lambda m:'<img%s src="%s" data-src="%s"'%(m.group(1),GIF,m.group(2)),b)
        h=a+'<nav class="hnav"'+b
        # 2 Book en samtale i toppen — fjernet igjen 15.11.2026 (Tom: dobler hero-knappen)
        h=h.replace('<a class="kn g hbk" href="kontakt.html#skjema">Book en samtale</a><button class="mbtn"','<button class="mbtn"',1)
        # 3 mobilmeny
        if 'href="gap-vision.html">GAP Vision</a></div>\n<div class="mc"><h4>Mer' not in h:
            h=re.sub(r'(<div class="mc"><h4>Tjenester</h4>.*?)(</div>)',r'\1<a href="gap-vision.html">GAP Vision</a>\2',h,count=1,flags=re.S)
            h=re.sub(r'(<div class="mc"><h4>Mer</h4>.*?)(</div>)',r'\1<a href="karriere.html">Karriere</a><a href="kontakt.html">Kontakt</a>\2',h,count=1,flags=re.S)
        # 5 søkeknapp
        h=h.replace('<input type="checkbox" id="sk" class="skx" aria-hidden="true">','<input type="checkbox" id="sk" class="skx" aria-label="Åpne søk">').replace('<label for="sk" class="sbtn" aria-label="Søk">','<label for="sk" class="sbtn">')
        t=t.replace(hm.group(0),h,1)
        if 'id="menybilder"' not in t: t=t.replace("</body>",JS+"</body>",1)
    # 4 bunntekst
    fm=re.search(r'<footer.*?</footer>',t,re.S)
    if fm and 'karriere.html' not in fm.group(0):
        t=t.replace(fm.group(0),fm.group(0).replace('<a href="gap-vision.html">GAP Vision</a>','<a href="gap-vision.html">GAP Vision</a>\n<a href="karriere.html">Karriere</a>',1),1)
    # 6 ankre på Bransjer
    if n=="bransjer" and 'id="handel"' not in t:
        k=iter(BRID);t=re.sub(r'<div class="svtile">',lambda m:'<div class="svtile" id="%s">'%next(k),t,count=4)
    # 7 overskriftsnivå
    t=re.sub(r'(<div class="svpv">.*?</div></div>)',lambda m:m.group(1).replace("<h4>",'<h4 aria-level="3">'),t,flags=re.S)
    t=t.replace('<div class="svpv"><div class="a"><h4>','<div class="svpv"><div class="a"><h4 aria-level="3">').replace('<div class="b"><h4>','<div class="b"><h4 aria-level="3">')
    if n=="fagekspertene": t=t.replace('<div class="fxt"><h3>','<div class="fxt"><h3 aria-level="2">')
    if n=="referanser": t=re.sub(r'(<div class="rcb">(?:<span[^>]*>[^<]*</span>)?)<h3>',r'\1<h3 aria-level="2">',t)
    # 8 tomme bilder i to artikler
    t=re.sub(r'<p>(?:<img loading="lazy" decoding="async" data-i="\d">\s*)+<br><em>[^<]*</em></p>','',t)
    t=re.sub(r'<img loading="lazy" decoding="async" data-i="\d">\s*','',t)
    # 9 sytten fageksperter
    t=t.replace('<b>16</b><span>fageksperter</span>','<b>17</b><span>fageksperter</span>').replace("fagmiljø av 16 fageksperter","fagmiljø av 17 fageksperter")
    # 10 telefon: +47 overalt, én skrivemåte
    nums=set(re.findall(r'href="tel:\+47(\d{8})"',t))|{"22490000","90890509","41088885"}
    def fx(s):
        for d in nums:
            pat=r'(?<![\d+])(?:\+47\s?)?'+r'\s?'.join(d)+r'(?!\d)'
            s=re.sub(pat,tlf(d),s)
        return s
    t=segs(t,fx)
    # 11 skygger skrevet rett på elementer i innholdet
    mi=t.find("<main");fi=t.find("<footer")
    if mi>0 and fi>mi:
        mid=re.sub(r'(style="[^"]*?)box-shadow:(?!\s*0 0 0 )[^;"]+;?',r'\1',t[mi:fi]);t=t[:mi]+mid+t[fi:]
    # 12 hero-bildet først
    t=re.sub(r'(<div class="(?:hph|svhi|pf)">\s*<img)(?![^>]*fetchpriority)',r'\1 fetchpriority="high"',t,count=1)
    # kontrast i stilene
    def css(m):
        c=m.group(0)
        c=re.sub(r'(?<![-a-z])color:#547B35',"color:#3F6A25",c,flags=re.I)
        c=re.sub(r'background:#7EA257;color:#fff',"background:#547B35;color:#fff",c,flags=re.I)
        return c
    t=re.sub(r'<style[^>]*>.*?</style>',css,t,flags=re.S)
    open(p,"w").write(t)
