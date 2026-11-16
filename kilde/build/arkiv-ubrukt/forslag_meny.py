# Menyforslag: ny mega-meny i v2-språk + sidepanel (variant B) + fikset søk.
# Skriver kun site/forslag-meny.html. Rører ikke live-sidene.
import re, html as H
src = open('/home/claude/fs/build/build.py').read()
i = src.index('EX=['); j = src.index(']\nTOM')
NAMES = [m.group(1, 2) for m in re.finditer(r'\("([^"]+)","([^"]+)"', src[i:j])]
PORT = ["per-kjetil","perchristian","anne","leif","carl","erik","neda","morten","petter","arvid","rita","atle","janick","bard","paal","jorg"]
PEOPLE = [(n, r, "img/portrett-%s.jpg" % p) for (n, r), p in zip(NAMES, PORT)] + [("Tom Hope", "Kommersiell leder", "img/portrett-tom.jpg")]
# Utvalg som vises i nedtrekket (de samme åtte som i dagens meny)
SEL = ["Per Kjetil Parr","Per Christian Svae","Anne Katrine Brånen","Tom Hope","Leif Ottesen","Carl Haakon Klafstad","Erik Simensen","Neda Maria Kaizumi"]
PM = {p[0]: p for p in PEOPLE}

XS = lambda c, w=120: '<svg aria-hidden="true" class="x" viewBox="0 0 700 700"><line x1="80" y1="80" x2="620" y2="620" stroke="%s" stroke-width="%d"/><line x1="620" y1="80" x2="80" y2="620" stroke="%s" stroke-width="%d"/></svg>' % (c, w, c, w)
ARR = '<span class="pil" aria-hidden="true"></span>'

def lead(t, p, l, cta=True):
    return '<div class="ml">%s<h3>%s</h3><p>%s</p><a class="tl" href="#">%s%s</a></div>' % (XS("#DCE7E0"), t, p, l, ARR)

def grp(t, items):
    return '<div class="gp"><p class="gh">%s</p>%s</div>' % (t, "".join('<a class="it" href="#"><b>%s</b><i>%s</i></a>' % (a, b) for a, b in items))

def fcard(img, kicker, title):
    return '<a class="fc" href="#"><span class="fi"><img src="%s" alt=""></span><i>%s</i><b>%s</b></a>' % (img, kicker, title)

def mega(label, inner, cols):
    return '<div class="ni"><a class="nl" href="#">%s</a><div class="mega"><div class="wrap"><div class="mg" style="grid-template-columns:%s">%s</div></div></div></div>' % (label, cols, inner)

# ---------- Nedtrekk ----------
TJ = mega("Tjenester",
  lead("Tjenester", "Fire områder som henger sammen. Velg der dere trenger mest.", "Se alle tjenester")
  + '<div class="gps">'
  + grp("Salgsutvikling", [("Rådgivende verdisalg","Selg på verdi, ikke pris"),("Kunstig intelligens i salg","Mer tid til kundesamtaler"),("Salgsledelse","Ledere som løfter teamet"),("Kundeinnsikt","Fakta før møtet")])
  + grp("Lederutvikling", [("Strategi til handling","Fra plan til daglig praksis"),("Coaching","Én til én med en fagekspert"),("Organisasjonsutvikling","Struktur som bærer strategien")])
  + grp("Kulturutvikling", [("Prestasjonskultur","Vaner som gir resultater"),("Kommersiell kultur","Hele huset tenker kunde")])
  + grp("KI, adopsjon og sikkerhet", [("AI Act og compliance","Klar for regelverket"),("KI i hverdagen","Fra pilot til bruk"),("Informasjonssikkerhet","Trygg bruk av data")])
  + '</div>' + fcard("img/case-thon.jpg", "Referanse", "Thon Hotels: et kommersielt kulturløft"),
  "280px 1fr 280px")

def bcard(img, t, items):
    return '<div class="bc"><a class="bi" href="#"><img src="%s" alt=""></a><a class="bh" href="#">%s%s</a><div class="bl">%s</div></div>' % (img, t, ARR, "".join('<a href="#">%s</a>' % x for x in items))
BR = mega("Bransjer",
  lead("Bransjer", "Fire vertikaler med egne landingssider. KI-tilbudet gjelder alle fire.", "Se alle bransjer")
  + bcard("img/salg.jpg", "Handel og forhandlernett", ["Retail og faghandel","Bil"])
  + bcard("img/kunnskap-artikler.jpg", "Bank, forsikring og eiendomsmegling", ["Sparebank","Forsikring","Megling"])
  + bcard("img/kunnskap-guide.jpg", "Bygg og eiendom", ["Entreprenør og anlegg","Tekniske fag","Utleie og drift"])
  + bcard("img/kunnskap-webinar.jpg", "IT og teknologi", ["Programvare","Konsulent","Drift"]),
  "280px repeat(4,1fr)")

def pr(n):
    _, r, img = PM[n]
    return '<a class="pp" href="#"><span class="pc"><img src="%s" alt=""></span><b>%s</b><i>%s</i></a>' % (img, n, r)
cta = '<div class="cc">%s<h4>Snakk med en fagekspert</h4><p>Ring, skriv eller book en samtale direkte.</p><a class="kn g" href="#">Book en samtale</a></div>' % XS("#2C5568")
FA = mega("Fageksperter",
  lead("Fagekspertene", "Ett team med erfaring fra salg, ledelse og kultur.", "Se alle fagekspertene")
  + '<div class="pg">' + "".join(pr(n) for n in SEL) + '</div>' + cta,
  "280px 1fr 280px")

KU = mega("Kunnskap",
  lead("Kunnskapssenter", "Artikler, guider og arrangementer fra fagekspertene.", "Åpne kunnskapssenteret")
  + '<div class="gps three">'
  + grp("Les", [("Artikler","Korte tekster om salg og ledelse"),("Fagartikler","Dypere og mer faglig")])
  + grp("Lær", [("Guider","Steg for steg"),("Webinarer og arrangementer","Møt fagekspertene")])
  + grp("Hold deg oppdatert", [("Nyhetsbrev","Det nyeste fra oss"),("Siste fra fagekspertene","")])
  + '</div>' + fcard("img/kunnskap-guide.jpg", "Guide", "Rådgivende verdisalg: prinsipper og beste praksis i B2B-salg"),
  "280px 1fr 280px")

RE = mega("Referanser",
  lead("Referanser", "Resultater hos kunder, med tall vi kan stå inne for.", "Alle referanser")
  + fcard("img/case-thon.jpg", "Referanse", "Thon Hotels: et kommersielt kulturløft")
  + fcard("img/case-boligpartner.jpg", "Referanse", "BoligPartner: leder- og salgsutvikling")
  + fcard("img/case-wikborg2.jpg", "Referanse", "Wikborg Rein: forenklet kompetanseutvikling"),
  "280px repeat(3,1fr)")

OM = mega("Om oss",
  lead("Om oss", "Vi hjelper deg å finne, vinne og beholde de rette kundene.", "Les mer om oss")
  + '<div class="gps three">'
  + grp("Om Excellerate", [("Om oss",""),("Vår historie – siden 1988",""),("Verdier",""),("Partnere","")])
  + grp("Mennesker", [("Fagekspertene",""),("Karriere","")])
  + '<div class="gp"><p class="gh">Kontakt</p><a class="it" href="#"><b>Kontakt oss</b><i></i></a><span class="ad">Stortorvet 7, Oslo<br>+47 22 49 00 00<br>post@excellerate.no</span></div>'
  + '</div>' + fcard("img/resepsjon.jpg", "Besøk oss", "Stortorvet 7, Oslo"),
  "280px 1fr 280px")

NAV = TJ + BR + FA + KU + RE + OM

# ---------- Sidepanel (variant B / mobilmeny) ----------
def sub(k, groups):
    return '<div class="sp" data-k="%s">%s</div>' % (k, "".join('<div class="spg"><p>%s</p>%s</div>' % (t, "".join('<a href="#">%s</a>' % x for x in its)) for t, its in groups))
TOP = [("tj","Tjenester"),("br","Bransjer"),("fa","Fageksperter"),("ku","Kunnskap"),("re","Referanser"),("om","Om oss")]
SUBS = (sub("tj",[("Salgsutvikling",["Rådgivende verdisalg","Kunstig intelligens i salg","Salgsledelse","Kundeinnsikt"]),("Lederutvikling",["Strategi til handling","Coaching","Organisasjonsutvikling"]),("Kulturutvikling",["Prestasjonskultur","Kommersiell kultur"]),("KI, adopsjon og sikkerhet",["AI Act og compliance","KI i hverdagen","Informasjonssikkerhet"])])
 + sub("br",[("Bransjer",["Handel og forhandlernett","Bank, forsikring og eiendomsmegling","Bygg og eiendom","IT og teknologi"])])
 + sub("fa",[("Fagekspertene",["Se alle fagekspertene"]+[p[0] for p in PEOPLE[:6]])])
 + sub("ku",[("Les",["Artikler","Fagartikler"]),("Lær",["Guider","Webinarer og arrangementer"]),("Hold deg oppdatert",["Nyhetsbrev","Siste fra fagekspertene"])])
 + sub("re",[("Referanser",["Thon Hotels","BoligPartner","Wikborg Rein","Alle referanser"])])
 + sub("om",[("Om Excellerate",["Om oss","Vår historie – siden 1988","Verdier","Partnere"]),("Mennesker",["Fagekspertene","Karriere"]),("Kontakt",["Kontakt oss","Stortorvet 7, Oslo"])]))
DRAWER = ('<div class="dov" id="dov"></div><aside class="drw" id="drw" aria-label="Meny" aria-hidden="true">' + XS("#2C5568", 100)
 + '<button class="dx" id="dx" aria-label="Lukk meny"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 5l14 14M19 5 5 19"/></svg></button>'
 + '<div class="dg"><nav class="dt" aria-label="Hovedmeny">' + "".join('<button data-k="%s"%s>%s%s</button>' % (k, ' class="on"' if k == "tj" else "", t, ARR) for k, t in TOP) + '</nav>'
 + '<div class="ds">' + SUBS + '</div></div>'
 + '<div class="df"><a class="kn g" href="#">Book en samtale</a><span>Stortorvet 7, Oslo · +47 22 49 00 00 · post@excellerate.no</span></div></aside>')

# ---------- Søk ----------
CHIPS = ["Når kundene bare snakker om pris","Strategi til handling","AI Act","Rådgivende verdisalg"]
SOK = ('<div class="sok"><div class="wrap"><div class="sf"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#356A89" stroke-width="2"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/></svg><input id="sinp" type="search" placeholder="Søk i tjenester, caser og fagekspertene" aria-label="Søk"></div>'
 + '<div class="sc1"><p class="kt">Vanlige søk</p><div class="chips">' + "".join('<a class="chip" href="#">%s</a>' % c for c in CHIPS) + '</div></div>'
 + '<div class="sc2"><p class="kt">Fagekspertene</p><div class="sirk">' + "".join('<a class="sk" href="#" data-n="%s"><span class="pc"><img src="%s" alt=""></span><b>%s</b></a>' % ((n + " " + r).lower(), img, n) for n, r, img in PEOPLE) + '</div></div></div></div>')

CSS = r'''
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Inter,system-ui,sans-serif;color:#231F20;-webkit-font-smoothing:antialiased;font-weight:500}
a{color:inherit;text-decoration:none}h1,h2,h3,h4{font-weight:500;letter-spacing:-.04em;margin:0}p{margin:0}button{font:inherit;cursor:pointer}
.wrap{max-width:1240px;margin:0 auto;padding:0 40px}
.sw{display:flex;gap:18px;align-items:center;flex-wrap:wrap;padding:10px 40px;background:#0F2430;color:#D3DCDF;font:500 14px/20px Inter,sans-serif}.sw a,.sw button{background:none;border:0;color:#fff;opacity:.7;font:inherit;padding:0 0 2px;cursor:pointer;text-decoration:none}.sw .on{opacity:1;border-bottom:2px solid #7EA257}
.x{position:absolute;pointer-events:none}
/* knapper */
.kn{display:inline-flex;gap:10px;align-items:center;font:600 15px Inter,sans-serif;padding:11px 18px;border-radius:4px 12px 4px 12px;cursor:pointer;border:1px solid transparent;transition:background .25s,border-color .25s,color .25s;white-space:nowrap}
.kn.g{background:#547B35;color:#fff}.kn.g:hover{background:#628C3F}
.kn.g::after{content:"";width:8px;height:8px;border-radius:50%;background:currentColor;transition:transform .3s}.kn.g:hover::after{transform:translate(3px,-4px) scale(1.5)}
.tl{display:inline-flex;gap:8px;align-items:center;font-weight:600;font-size:15px;color:#356A89;padding:4px 0;background:linear-gradient(#7EA257,#7EA257) left bottom/100% 2px no-repeat}
.pil{width:8px;height:8px;border-right:2px solid currentColor;border-top:2px solid currentColor;transform:rotate(45deg);transition:transform .25s;display:inline-block}.tl:hover .pil{transform:translateX(4px) rotate(45deg)}
/* header */
.hdr{position:sticky;top:0;z-index:50;background:#fff;border-bottom:1px solid #DDE5E8}
.hb{display:flex;align-items:center;justify-content:space-between;height:80px;gap:20px}
.hl{display:flex;align-items:center;gap:20px}
.logo img{height:22px;display:block}
.hnav{display:flex;gap:6px;height:80px}
.ni{height:80px;display:flex;align-items:center}
.nl{white-space:nowrap;position:relative;display:flex;align-items:center;height:80px;padding:0 14px;font-size:16px;color:#1B3A4B;font-weight:500;transition-duration:.08s}
.nl::after{content:"";position:absolute;left:14px;right:14px;bottom:22px;height:2px;background:#7EA257;transform:scaleX(0);transform-origin:left;transition:transform .2s}
.ni:hover .nl,.ni:focus-within .nl{color:#356A89}.ni:hover .nl::after,.ni:focus-within .nl::after{transform:scaleX(1)}
.hr{display:flex;align-items:center;gap:12px}
.ib{width:42px;height:42px;border-radius:50%;border:1px solid #D5DFE5;background:#fff;display:grid;place-items:center;color:#1B3A4B;transition:border-color .2s,color .2s}.ib:hover{border-color:#356A89;color:#356A89}
.sbtn .s2{display:none}.skx:checked ~ .hb .sbtn .s1{display:none}.skx:checked ~ .hb .sbtn .s2{display:block}.skx{position:absolute;opacity:0;pointer-events:none}
.mbtn{display:none;align-items:center;gap:10px;height:42px;padding:0 16px 0 14px;border-radius:4px 12px 4px 12px;border:1px solid #D5DFE5;background:#fff;color:#1B3A4B;font-weight:600;font-size:15px;transition:border-color .2s,color .2s}.mbtn:hover{border-color:#356A89;color:#356A89}
.mbtn i{width:18px;height:10px;border-top:2px solid currentColor;border-bottom:2px solid currentColor;display:block}
body.vb .mbtn{display:inline-flex}
/* mega */
.mega{position:absolute;left:0;right:0;top:100%;background:#fff;border-top:1px solid #DDE5E8;box-shadow:0 30px 50px -20px rgba(27,58,75,.22);visibility:hidden;opacity:0;transform:translateY(-6px);transition:opacity .08s,transform .08s,visibility 0s .08s}
.ni:hover .mega,.ni:focus-within .mega{visibility:visible;opacity:1;transform:none;transition:opacity .22s,transform .22s,visibility 0s}
.mega .wrap{padding-top:32px;padding-bottom:40px}
.mg{display:grid;gap:40px;align-items:stretch}
.ml{position:relative;overflow:hidden;background:#EAF0EC;border-radius:4px 20px 4px 20px;padding:28px 28px 30px;display:flex;flex-direction:column;gap:12px;min-height:300px}
.ml .x{right:-120px;bottom:-130px;width:300px;height:300px}.ml h3{font-size:30px;line-height:34px;color:#1B3A4B;position:relative}.ml p{color:#4A5F6A;font-size:16px;line-height:24px;position:relative;font-weight:500}.ml .tl{margin-top:auto;position:relative;align-self:flex-start}
.gps{display:grid;grid-template-columns:1fr 1fr;gap:26px 36px;align-content:start}.gps.three{grid-template-columns:repeat(3,1fr)}
.gh{font-size:15px;font-weight:600;color:#1B3A4B;margin:0 0 10px 12px;padding-bottom:8px;position:relative}.gh::after{content:"";position:absolute;left:0;bottom:0;width:24px;height:2px;background:#7EA257}
.it{display:block;padding:9px 12px;border-radius:4px 12px 4px 12px;transition:background .08s}.it b{display:block;font-size:16px;font-weight:500;color:#1B3A4B;line-height:22px}.it i{display:block;font-style:normal;font-size:14px;color:#566B76;line-height:20px;margin-top:1px;font-weight:500}
.it:hover{background:#EAF0EC;transition:background .22s}.it:hover b{color:#356A89}
.ad{display:block;font-size:14px;line-height:22px;color:#566B76;padding:9px 12px}
/* kort */
.fc{display:flex;flex-direction:column;gap:10px;transition:transform .25s}.fc .fi{display:block;border-radius:18px;overflow:hidden;aspect-ratio:4/3;background:#EAF0EC}.fc img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .5s}.fc:hover img{transform:scale(1.04)}
.fc i{font-style:normal;font-size:14px;font-weight:600;color:#566B76}.fc b{font-size:18px;line-height:24px;font-weight:500;color:#1B3A4B;letter-spacing:-.02em}.fc:hover b{color:#356A89}
.bc{display:flex;flex-direction:column;gap:10px}.bi{display:block;border-radius:18px;overflow:hidden;aspect-ratio:4/3}.bi img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .5s}.bi:hover img{transform:scale(1.04)}
.bh{display:flex;align-items:center;gap:8px;font-size:18px;line-height:24px;font-weight:500;color:#1B3A4B;letter-spacing:-.02em}.bh .pil{flex:0 0 8px;color:#7EA257;transition:transform .25s}.bh:hover{color:#356A89}.bh:hover .pil{transform:translateX(4px) rotate(45deg)}
.bl{display:flex;flex-wrap:wrap;gap:4px 14px}.bl a{font-size:14px;color:#566B76;font-weight:500;padding:2px 0}.bl a:hover{color:#356A89}
.pg{display:grid;grid-template-columns:repeat(4,1fr);gap:22px 18px;align-content:start}
.pp{display:flex;flex-direction:column;align-items:center;text-align:center;gap:2px}.pc{display:block;width:84px;height:84px;border-radius:50%;overflow:hidden;background:#EAF0EC;margin-bottom:8px;transition:box-shadow .2s}.pc img{width:100%;height:100%;object-fit:cover;object-position:50% 18%;display:block}
.pp:hover .pc{box-shadow:0 0 0 3px #fff,0 0 0 5px #7EA257}.pp b{font-size:15px;line-height:20px;color:#1B3A4B;font-weight:500}.pp i{font-style:normal;font-size:13px;line-height:18px;color:#566B76}
.cc{position:relative;overflow:hidden;background:#1B3A4B;color:#fff;border-radius:4px 20px 4px 20px;padding:28px;display:flex;flex-direction:column;gap:10px;justify-content:flex-end}.cc .x{right:-110px;top:-110px;width:280px;height:280px}.cc h4{font-size:26px;line-height:30px;position:relative}.cc p{color:#C5D2D8;font-size:15px;line-height:22px;position:relative;margin-bottom:10px}.cc .kn{position:relative;align-self:flex-start}
/* søk */
.sok{display:none;position:absolute;left:0;right:0;top:100%;background:#fff;border-top:1px solid #DDE5E8;box-shadow:0 30px 50px -20px rgba(27,58,75,.22)}.skx:checked ~ .sok{display:block}
.sok .wrap{padding-top:32px;padding-bottom:40px;display:flex;flex-direction:column;gap:28px}
.sf{display:flex;align-items:center;gap:14px;border:1px solid #C6D2D8;border-radius:8px;padding:0 18px;height:60px}.sf:focus-within{border-color:#356A89;box-shadow:0 0 0 3px #DCE7EE}.sf input{flex:1;border:0;outline:0;font:500 20px Inter,sans-serif;color:#231F20;background:none}
.kt{font-size:15px;font-weight:600;color:#1B3A4B;margin-bottom:12px}
.chips{display:flex;gap:10px;flex-wrap:wrap}.chip{background:#EAF0EC;color:#1B3A4B;border-radius:4px 12px 4px 12px;padding:9px 16px;font-size:15px;transition:background .08s}.chip:hover{background:#1B3A4B;color:#fff;transition:background .22s}
.sirk{display:grid;grid-template-columns:repeat(9,1fr);gap:18px 10px}
.sk{display:flex;flex-direction:column;align-items:center;text-align:center;gap:6px}.sk .pc{width:64px;height:64px;margin:0}.sk b{font-size:13px;line-height:17px;color:#1B3A4B;font-weight:500}.sk:hover .pc{box-shadow:0 0 0 3px #fff,0 0 0 5px #7EA257}.sk.dim{display:none}
/* side-panel */
.dov{position:fixed;inset:0;background:rgba(15,36,48,.45);opacity:0;visibility:hidden;transition:opacity .3s,visibility 0s .3s;z-index:90}
.drw{position:fixed;left:0;top:0;bottom:0;width:min(980px,94vw);background:#1B3A4B;color:#fff;z-index:100;transform:translateX(-102%);transition:transform .38s cubic-bezier(.2,.7,.2,1);display:flex;flex-direction:column;overflow:hidden;padding:36px 56px 32px}
.drw .x{right:-170px;bottom:-190px;width:620px;height:620px}
body.dopen .drw{transform:none}body.dopen .dov{opacity:1;visibility:visible;transition:opacity .3s}
.dx{align-self:flex-start;width:44px;height:44px;border-radius:50%;border:1px solid #4D6C7D;background:none;color:#fff;display:grid;place-items:center;position:relative;transition:border-color .2s}.dx:hover{border-color:#fff}
.dg{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:56px;margin-top:36px;position:relative;min-height:0}
.dt{display:flex;flex-direction:column;gap:2px}
.dt button{display:flex;align-items:center;justify-content:space-between;background:none;border:0;color:#9FB4BF;font-size:40px;line-height:54px;letter-spacing:-.04em;font-weight:500;text-align:left;padding:2px 0;transition:color .08s}.dt button .pil{opacity:0;color:#9CC06F;width:12px;height:12px;transition:opacity .2s,transform .25s}
.dt button.on,.dt button:hover{color:#fff;transition:color .22s}.dt button.on .pil{opacity:1}
.ds{position:relative}.sp{display:none;flex-direction:column;gap:22px;animation:fi .25s}.sp.on{display:flex}@keyframes fi{from{opacity:0;transform:translateX(-8px)}to{opacity:1;transform:none}}
.spg p{font-size:15px;font-weight:600;color:#9CC06F;margin-bottom:6px}.spg a{display:block;font-size:20px;line-height:32px;color:#E6EEF1;font-weight:500}.spg a:hover{color:#fff;text-decoration:underline;text-decoration-color:#9CC06F;text-underline-offset:6px;text-decoration-thickness:2px}
.df{position:relative;display:flex;gap:24px;align-items:center;flex-wrap:wrap;border-top:1px solid #36586B;padding-top:22px;margin-top:16px}.df span{font-size:14px;color:#9FB4BF}
/* eksempelside */
.demo{background:#F3F6F5;padding:72px 0 96px}.demo h1{font-size:56px;line-height:56px;color:#1B3A4B;max-width:14em}.demo p{margin-top:20px;font-size:18px;line-height:28px;color:#4A5F6A;max-width:40em}
.demo ul{margin:22px 0 0;padding-left:20px;font-size:17px;line-height:30px;color:#4A5F6A;max-width:40em}
.nb{margin-top:32px;border-left:3px solid #7EA257;padding:6px 0 6px 18px;font-size:15px;line-height:23px;color:#566B76;max-width:46em}
.ph{background:#fff;padding:80px 0}.ph .wrap>div{height:260px;border:1px dashed #C6D2D8;border-radius:18px;display:grid;place-items:center;color:#8AA0AB;font-size:15px}
@media(max-width:1100px){.mg{gap:24px}.nl{padding:0 9px}.nl::after{left:9px;right:9px}}
@media(max-width:900px){.hnav,.hbtn{display:none}.mbtn{display:inline-flex!important}.dg{grid-template-columns:1fr}.ds{display:none}.dt button{font-size:30px;line-height:44px}.drw{padding:24px 24px}.sirk{grid-template-columns:repeat(4,1fr)}.wrap{padding:0 20px}.demo h1{font-size:38px;line-height:40px}}
@media(prefers-reduced-motion:reduce){*{transition-duration:.01ms!important;animation:none!important}}
'''

JS = r'''
(function(){
var b=document.body;
function setV(v){b.classList.remove('va','vb');b.classList.add(v);document.querySelectorAll('.sw button').forEach(function(x){x.classList.toggle('on',x.dataset.v===v)});if(v==='va')close();}
document.querySelectorAll('.sw button').forEach(function(x){x.addEventListener('click',function(){setV(x.dataset.v)})});
function open(){b.classList.add('dopen');document.getElementById('drw').setAttribute('aria-hidden','false');document.getElementById('dx').focus()}
function close(){b.classList.remove('dopen');document.getElementById('drw').setAttribute('aria-hidden','true')}
document.getElementById('mb').addEventListener('click',open);
document.getElementById('dx').addEventListener('click',close);
document.getElementById('dov').addEventListener('click',close);
document.addEventListener('keydown',function(e){if(e.key==='Escape'){close();document.getElementById('sk').checked=false}});
var ts=document.querySelectorAll('.dt button'),ps=document.querySelectorAll('.sp');
function pick(k){ts.forEach(function(t){t.classList.toggle('on',t.dataset.k===k)});ps.forEach(function(p){p.classList.toggle('on',p.dataset.k===k)})}
ts.forEach(function(t){t.addEventListener('mouseenter',function(){pick(t.dataset.k)});t.addEventListener('click',function(){pick(t.dataset.k)});t.addEventListener('focus',function(){pick(t.dataset.k)})});
pick('tj');
var si=document.getElementById('sinp');
si.addEventListener('input',function(){var q=si.value.toLowerCase().trim();document.querySelectorAll('.sk').forEach(function(a){a.classList.toggle('dim',q&&a.dataset.n.indexOf(q)<0)})});
document.getElementById('sk').addEventListener('change',function(e){if(e.target.checked)setTimeout(function(){si.focus()},50)});
setV('vb');
})();
'''

PAGE = '''<!DOCTYPE html><html lang="nb"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Excellerate – Menyforslag</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"><style>%s</style></head>
<body class="vb">
<div class="sw"><span>Menyforslag:</span><button data-v="va">A. Kun nedtrekk</button><button data-v="vb" class="on">B. Nedtrekk + sidepanel</button><a href="forslag-d.html">Designelementer</a><a href="index.html">Tilbake til forsiden</a></div>
<header class="hdr"><input type="checkbox" id="sk" class="skx" aria-hidden="true" tabindex="-1">
<div class="wrap hb"><div class="hl"><a class="logo" href="index.html" aria-label="Excellerate, til forsiden"><img src="img/logo-xl.png" alt="Excellerate"></a>
<button class="mbtn" id="mb" aria-controls="drw"><i></i>Meny</button></div>
<nav class="hnav" aria-label="Hovedmeny">%s</nav>
<div class="hr"><label for="sk" class="ib sbtn" aria-label="Søk"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="s1"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/></svg><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="s2"><path d="M5 5l14 14M19 5 5 19"/></svg></label><a class="kn g hbtn" href="#">Book en samtale</a></div></div>
%s</header>
%s
<main><section class="demo"><div class="wrap"><h1>Slik kan menyen se ut på siten.</h1><p>Siden under er bare en plassholder, slik at du ser menyen over noe.</p>
<ul><li>Hold musen over Tjenester, Bransjer, Fageksperter, Kunnskap, Referanser og Om oss.</li><li>Trykk på forstørrelsesglasset for søket. Skriv et navn for å filtrere fagekspertene.</li><li>Bytt mellom A og B øverst. B har «Meny»-knappen ved logoen, som åpner sidepanelet. Det samme panelet blir mobilmenyen.</li></ul>
<p class="nb">Forslag: alle korte beskrivelser under lenkene, og bildene i Bransjer (foreløpig gjenbrukte bilder). Strukturen og lenkene er de samme som i dagens meny. Lenkene går ikke noe sted ennå.</p></div></section>
<section class="ph"><div class="wrap"><div>Resten av siden</div></div></section></main>
<script>%s</script></body></html>'''
out = PAGE % (CSS, NAV, SOK, DRAWER, JS)
open('/home/claude/fs/site/forslag-meny.html', 'w').write(out)
print(len(out))
