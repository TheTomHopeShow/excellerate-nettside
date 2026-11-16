import re
c=open('/home/claude/fs/build/style7.css').read()
blk=c[c.index('/*HEROBILDE-START*/'):c.index('/*HEROBILDE-END*/')+len('/*HEROBILDE-END*/')]
for f in ["tjenester","bransjer"]:
    p="/home/claude/fs/site/%s.html"%f;t=open(p).read()
    t=re.sub(r'<style id="herobilde">.*?</style>','',t,flags=re.S)
    t=t.replace("</head>",'<style id="herobilde">'+blk+'</style></head>',1);open(p,"w").write(t)

# Lapper (hvit etikett) på hero-bildet. Tekstene er hentet fra tall og tekst som allerede står på samme side.
import glob,html as H
LAPP={"tjenester":("600+","utviklingsprogrammer"),"bransjer":("4 bransjer","KI gjelder alle fire"),
 "tjenester-salg":("5 000","bedrifter utviklet"),"tjenester-ledelse":("300 000","ledere og medarbeidere utviklet"),
 "tjenester-kultur":("600+","utviklingsprogrammer"),"tjenester-ki":("20+","år med internasjonal ledererfaring"),
 "gap-vision":("600+","utviklingsprogrammer i datagrunnlaget")}
def pill(b,s): return '<div class="hpill lap"><i></i><div><b>%s</b>%s</div></div>'%(H.escape(b),H.escape(s))
for p in glob.glob("/home/claude/fs/site/*.html"):
    n=p.split("/")[-1][:-5];t=open(p).read()
    if 'class="hpill lap"' in t: continue
    if n in LAPP:
        t2=re.sub(r'(<div class="svhi">.*?<img[^>]*>)',lambda m:m.group(1)+pill(*LAPP[n]),t,count=1,flags=re.S)
    elif n.startswith("fagekspert-") and n!="fagekspert-ekstra":
        m=re.search(r'<div class="cs">(.*?)</div>',t,re.S)
        sp=re.findall(r"<span>(.*?)</span>",m.group(1)) if m else []
        if not sp: continue
        t2=re.sub(r'(<div class="pf"><img[^>]*>)',lambda m2:m2.group(1)+pill("Fagekspert"," · ".join(sp[:2])),t,count=1)
    else: continue
    open(p,"w").write(t2)
