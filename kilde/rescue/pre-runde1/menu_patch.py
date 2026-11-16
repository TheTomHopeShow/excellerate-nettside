# Forslag (Tom, 15.11.2026): menyen heter Mennesker, ikke Fageksperter. GAP Vision ligger under Tjenester.
# Om oss samler Om oss, Karriere og Kontakt. Kompakte heroer får ett tydelig neste steg, lange sider får hopplenker.
import re,glob
BTN='<div class="kbs" style="margin-top:32px;display:flex;gap:12px;flex-wrap:wrap">%s</div>'
def hopp(items): return '<nav class="hopp" aria-label="På denne siden"><div class="wrap">'+"".join('<a href="#%s">%s</a>'%i for i in items)+'</div></nav>'
HOPP={"om-oss":[("gjor","Det vi gjør"),("historie","Historien"),("gapvision","GAP Vision"),("folk","Menneskene"),("verktoy","Verktøyene"),("karriere","Karriere"),("kontakt","Kontakt")],
      "tjenester":[("omrader","Områdene"),("problem","Utfordringene"),("gjor","Slik hjelper vi"),("resultater","Resultater")]}
for p in glob.glob("/home/claude/fs/site/*.html"):
    n=p.split("/")[-1][:-5];t=open(p).read();o=t
    # meny og bunntekst
    t=t.replace('<div class="ni"><a href="fagekspertene.html">Fageksperter</a>','<div class="ni"><a href="fagekspertene.html">Mennesker</a>')
    t=t.replace('<p class="mxt">Fagekspertene</p><p>Ett team med erfaring','<p class="mxt">Menneskene</p><p>Ett team med erfaring')
    t=t.replace('<a href="fagekspertene.html">Fagekspertene</a>','<a href="fagekspertene.html">Mennesker</a>')
    t=re.sub(r'(<a class="mxi" href="om-oss.html#historie">.*?</a>)<a class="mxi" href="gap-vision.html"><b>GAP Vision</b><i>Kundeinnsikt og AI</i></a><a class="mxi" href="om-oss.html#folk">.*?</a>',r'\1',t,count=1,flags=re.S) if '#historie"><b>Vår historie' in t else t
    t=t.replace('<p class="crb"><a href="fagekspertene.html">Fagekspertene</a>','<p class="crb"><a href="fagekspertene.html">Mennesker</a>')
    # kompakte heroer: ett neste steg
    if n=="fagekspertene":
        t=t.replace("<title>Fagekspertene | Excellerate</title>","<title>Mennesker | Excellerate</title>").replace("<h1>Fagekspertene</h1>","<h1>Menneskene i Excellerate</h1>")
        if 'class="kbs"' not in t.split("</section>")[0]:
            t=t.replace('</p></div></section>','</p>'+BTN%'<a class="kn g" href="kontakt.html#skjema">Snakk med oss</a><a class="kn l" href="karriere.html">Bli en del av miljøet</a>'+'</div></section>',1)
    if n=="referanser" and 'class="kbs"' not in t.split("</section>")[0]:
        t=t.replace('</p></div></section>','</p>'+BTN%'<a class="kn g" href="kontakt.html#skjema">Snakk med oss</a>'+'</div></section>',1)
    # hopplenker på lange sider
    if n in HOPP and 'class="hopp"' not in t:
        i=t.find("</section>",t.find('class="dyp hero'))+len("</section>")
        t=t[:i]+hopp(HOPP[n])+t[i:]
    if t!=o: open(p,"w").write(t)

# Megameny lukkes etter klikk og åpner først igjen når musa har forlatt toppfeltet
JS='<script id="megalukk">(function(){var h=document.querySelector("header.hdr");if(!h)return;var K="megalukk";function lukk(){h.classList.add("nomega")}try{if(sessionStorage.getItem(K)){lukk()}}catch(e){}h.addEventListener("click",function(e){var a=e.target.closest(".mega a");if(!a)return;lukk();try{sessionStorage.setItem(K,"1")}catch(x){}if(document.activeElement&&document.activeElement.blur)document.activeElement.blur()});h.querySelectorAll(".ni>a").forEach(function(a){a.addEventListener("mouseenter",function(){h.classList.remove("nomega");try{sessionStorage.removeItem(K)}catch(e){}})})})();</script>'
for p in glob.glob("/home/claude/fs/site/*.html"):
    t=open(p).read()
    if "</body>" in t:
        t=re.sub(r'<script id="megalukk">.*?</script>','',t,flags=re.S)
        open(p,"w").write(t.replace("</body>",JS+"</body>",1))
