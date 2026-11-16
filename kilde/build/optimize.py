# Etterbehandling: bilder -> WebP med width/height, kjøres etter static.py og designmanual.py
import re,os,glob
from PIL import Image
S="/home/claude/fs/site/"
cache={}
def conv(name):
    if name in cache: return cache[name]
    src=S+"img/"+name; base=os.path.splitext(name)[0]; out=S+"img/"+base+".webp"
    im=Image.open(src)
    w,h=im.size
    if max(w,h)>1600: im.thumbnail((1600,1600)); w,h=im.size
    if im.mode not in("RGB","RGBA"): im=im.convert("RGBA" if "transparency" in im.info or im.mode=="P" else "RGB")
    q=82
    im.save(out,"WEBP",quality=q,method=6)
    cache[name]=(base+".webp",w,h); return cache[name]
tot0=tot1=0
for f in glob.glob(S+"*.html"):
    t=open(f).read()
    def rep(m):
        tag=m.group(0)
        mm=re.search(r'src="img/([^"]+\.(?:jpg|png))"',tag)
        if not mm: return tag
        n,w,h=conv(mm.group(1))
        tag=tag.replace(mm.group(0),'src="img/%s"'%n)
        if 'aspect-ratio' not in tag:
            if 'style="' in tag: tag=tag.replace('style="','style="aspect-ratio:%d/%d;'%(w,h),1)
            else: tag=tag.replace('<img ','<img style="aspect-ratio:%d/%d" '%(w,h),1)
        return tag
    t=re.sub(r"<img [^>]*>",rep,t)
    t=re.sub(r'url\(["\']?img/([^)"\']+\.(?:jpg|png))["\']?\)',lambda m:'url(img/%s)'%conv(m.group(1))[0],t)
    open(f,"w").write(t)
used=set(re.findall(r'img/([^"\')\s]+)',"".join(open(f).read() for f in glob.glob(S+"*.html"))))
for f in glob.glob(S+"img/*"):
    n=os.path.basename(f)
    if n not in used: os.remove(f)
print("bilder:",len(os.listdir(S+"img")),"størrelse KB",sum(os.path.getsize(S+"img/"+x) for x in os.listdir(S+"img"))//1024)

# alt-tekst på portretter (dekorative bare når navnet står rett ved siden av)
NAMES={"anne":"Anne Katrine Brånen","arvid":"Arvid Madland Lyngnes","atle":"Atle Olsen","bard":"Bård Fossli Jensen","carl":"Carl Haakon Klafstad","erik":"Erik Simensen","janick":"Janick Løwe","jorg":"Jørg Lian","leif":"Leif Ottesen","morten":"Morten Brandt","neda":"Neda Maria Kaizumi","paal":"Paal Berg","per-kjetil":"Per Kjetil Parr","perchristian":"Per Christian Svae","petter":"Petter Kleppe","rita":"Rita Berg Hansen","tom":"Tom Hope","thomas":"Thomas Fehn","griwell":"Per Griwell"}
for f in glob.glob(S+"*.html"):
    t=open(f).read()
    def alt(m):
        k=m.group(2); n=NAMES.get(k)
        if not n: return m.group(0)
        after=re.sub(r"<[^>]+>"," ",t[m.end():m.end()+400])
        if n.split()[0] in after and n.split()[-1] in after: return m.group(0)
        return m.group(0).replace('alt=""','alt="%s"'%n,1)
    def alt(m):
        tag=m.group(0)
        if 'alt=""' not in tag: return tag
        k=re.search(r'portrett-([a-z-]+)\.webp',tag)
        n=NAMES.get(k.group(1)) if k else None
        if not n: return tag
        after=re.sub(r"<[^>]+>"," ",t[m.end():m.end()+400])
        if n.split()[0] in after and n.split()[-1] in after: return tag
        return tag.replace('alt=""','alt="%s"'%n,1)
    t=re.sub(r"<img [^>]*>",alt,t)
    open(f,"w").write(t)
