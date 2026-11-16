# Tre stemningstester: A (Salgsvekst-slekt), B (dagens stil + dybde), C (blanding)
IC={'mail':'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
'tel':'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>',
'cal':'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>'}
NAV='<a href="#">Tjenester</a><a href="#">Bransjer</a><a href="#">Fageksperter</a><a href="#">Kunnskap</a><a href="#">Referanser</a><a href="#">Om oss</a>'
SWITCH='<div class="sw"><span>Forslag:</span><a href="forslag-a.html"%s>A. Salgsvekst-slekt</a><a href="forslag-b.html"%s>B. Dagens stil med dybde</a><a href="forslag-c.html"%s>C. Blanding</a><a href="index.html">Tilbake til forsiden</a></div>'
def sw(k): return SWITCH%tuple(' class="on"' if k==x else '' for x in 'abc')

BASE='''*{box-sizing:border-box}body{margin:0;color:#231F20;-webkit-font-smoothing:antialiased}a{color:inherit}
.sw{display:flex;gap:18px;align-items:center;flex-wrap:wrap;padding:10px 40px;background:#0F2430;color:#D3DCDF;font:500 14px/20px Inter,system-ui,sans-serif}.sw a{text-decoration:none;color:#fff;opacity:.7}.sw a.on{opacity:1;border-bottom:2px solid #7EA257}.sw span{opacity:.6}
.wrap{max-width:1240px;margin:0 auto;padding:0 40px}
header.h{background:#fff;border-bottom:1px solid #D3DCDF}.h .wrap{display:flex;align-items:center;justify-content:space-between;height:76px}.h nav{display:flex;gap:30px;font-size:15px;font-weight:500}.h nav a{text-decoration:none}
.fl{display:flex;gap:16px;flex-wrap:wrap;align-items:center}
@media(max-width:900px){.g2{grid-template-columns:1fr!important}.h nav{display:none}}
'''
def page(k,title,css,body):
    return '<!DOCTYPE html><html lang="nb"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Schibsted+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet"><style>%s%s</style></head><body>%s<header class="h"><div class="wrap"><a href="index.html"><img src="img/logo-xl.png" alt="Excellerate" style="height:22px;display:block"></a><nav>%s</nav></div></header>%s</body></html>'%(title,BASE,css,sw(k),NAV,body)

HERO_P='Excellerate hjelper ledere med å styrke konkurransekraften gjennom salgsutvikling og lederutvikling. Vi finner, vinner og beholder flere kunder sammen med dere. Siden 1988.'
Q1='«Vi har skapt nye verdier, etablert nye informasjonskanaler og har fått et eget årshjul med tiltak for å bygge kultur.»'
QN='Thomas Fehn'; QR='Konserndirektør IT og digitalisering, Saint-Gobain Distribution'
STEPS=[('Finn','de riktige kundene'),('Vinn','dem i møtet'),('Behold','dem over tid')]

# ---------------- A ----------------
cssA='''body{font-family:Inter,system-ui,sans-serif;background:#F1F4F4}
h1,h2,h3{font-weight:500;letter-spacing:-0.045em;margin:0}
.pan{background:#1B3A4B;color:#fff;border-radius:28px;margin:32px auto 0;max-width:1240px;overflow:hidden;position:relative;display:grid;grid-template-columns:1fr 1.05fr;min-height:560px;box-shadow:0 20px 50px rgba(27,58,75,.18)}
.pan .t{padding:64px 56px;display:flex;flex-direction:column;justify-content:center}
.ey{font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:#7EA257;font-weight:600;display:flex;gap:10px;align-items:center}.ey::before{content:"";width:7px;height:7px;border-radius:50%;background:#7EA257}
.pan h1{font-size:68px;line-height:68px;margin-top:22px}.pan h1 em{font-style:normal;color:#9CC06F}
.pan p{margin:24px 0 0;font-size:19px;line-height:30px;color:#C5D2D8;max-width:28em}
.b1{display:inline-flex;gap:10px;align-items:center;background:#7EA257;color:#14290A;font:600 16px Inter,sans-serif;padding:15px 24px;border-radius:12px;text-decoration:none}
.b2{display:inline-flex;gap:10px;align-items:center;background:transparent;color:#fff;font:600 16px Inter,sans-serif;padding:15px 22px;border-radius:12px;text-decoration:none;border:1px solid #4D6C7D}
.sec{max-width:1240px;margin:0 auto;padding:88px 40px 0}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:36px}
.card{background:#fff;border-radius:22px;padding:30px;box-shadow:0 8px 30px rgba(27,58,75,.07)}
.ic{display:flex;align-items:center;gap:12px}.ic i{width:46px;height:46px;border-radius:50%;background:#EAF1E2;color:#4F7A2B;display:grid;place-items:center;font-style:normal;font-weight:600}.ic u{flex:0 0 44px;height:2px;background:#7EA257}
.card h3{font-size:24px;line-height:30px;margin-top:24px}.card p{margin:8px 0 0;font-size:17px;line-height:26px;color:#566B76}
.q{background:#fff;border-radius:28px;padding:56px;display:grid;grid-template-columns:auto 1fr;gap:40px;align-items:center;box-shadow:0 8px 30px rgba(27,58,75,.07);border-left:6px solid #7EA257}
.av{width:132px;height:132px;border-radius:50%;background:#DCE7E0;color:#356A89;display:grid;place-items:center;font:600 38px Inter,sans-serif;letter-spacing:-.02em;box-shadow:0 0 0 6px #fff,0 0 0 7px #D3DCDF;position:relative}
.av::after{content:"";position:absolute;right:6px;bottom:6px;width:20px;height:20px;border-radius:50%;background:#7EA257;border:4px solid #fff}
.q p.l{font-size:32px;line-height:42px;letter-spacing:-.03em;font-weight:500;margin:0}.q .n{margin-top:22px;font-weight:600;font-size:17px}.q .r{color:#566B76;font-size:15px}
.bar{background:#fff;border-radius:22px;padding:34px 40px;display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap;border-left:6px solid #7EA257;box-shadow:0 8px 30px rgba(27,58,75,.07)}
.bar h3{font-size:30px;letter-spacing:-.035em}
.sb{display:inline-flex;gap:10px;align-items:center;padding:13px 20px;border:1px solid #D3DCDF;border-radius:12px;background:#F7F9F9;font:600 16px Inter,sans-serif;text-decoration:none;color:#231F20}.sb.p{background:#356A89;color:#fff;border-color:#356A89}
'''
stair='''<svg viewBox="0 0 560 520" style="width:100%;height:100%;position:absolute;inset:0" aria-hidden="true">
<defs><pattern id="gr" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#fff" stroke-opacity=".05"/></pattern></defs><rect width="560" height="520" fill="url(#gr)"/>
<path d="M60 430H180V340H300V250H420V160H500" fill="none" stroke="#9CC06F" stroke-width="3" stroke-dasharray="9 8" stroke-linejoin="round"/>
<circle cx="60" cy="430" r="11" fill="#9CC06F"/><circle cx="180" cy="340" r="9" fill="#1B3A4B" stroke="#fff" stroke-width="3"/><circle cx="300" cy="250" r="9" fill="#1B3A4B" stroke="#fff" stroke-width="3"/><circle cx="420" cy="160" r="9" fill="#1B3A4B" stroke="#fff" stroke-width="3"/><circle cx="500" cy="160" r="13" fill="#9CC06F"/>
<g font-family="Inter" fill="#fff"><text x="52" y="468" font-size="20" font-weight="600" letter-spacing="-0.5">Her er dere</text><text x="52" y="490" font-size="14" fill="#9FB4BF">forstå situasjonen</text>
<rect x="318" y="84" rx="10" width="172" height="52" fill="#16313F" stroke="#35566A"/><text x="334" y="108" font-size="16" font-weight="600">Flere kunder</text><text x="334" y="127" font-size="13" fill="#9FB4BF">vunnet og beholdt</text></g></svg>'''
bodyA='''<section style="padding:0 20px"><div class="pan g2"><div class="t"><span class="ey">Salgsutvikling og lederutvikling</span><h1>Hvem vil dere <em>vinne</em> neste gang?</h1><p>%s</p><div class="fl" style="margin-top:34px"><a class="b1" href="#">Book en samtale</a><a class="b2" href="#">Hva mangler hos dere?</a></div></div><div style="position:relative;min-height:440px">%s</div></div></section>
<section class="sec"><h2 style="font-size:46px;line-height:48px">Finn, vinn og behold.<br>Samme metode hele veien.</h2>
<div class="cards">%s</div></section>
<section class="sec"><div class="q g2"><div class="av">TF</div><div><p class="l">%s</p><p class="n">%s</p><p class="r">%s</p></div></div></section>
<section class="sec" style="padding-bottom:88px"><div class="bar"><div><h3>La oss ta en samtale</h3><p style="margin:6px 0 0;color:#566B76">Ring, skriv eller book direkte med en av fagekspertene.</p></div><div class="fl"><a class="sb" href="#">%s Send e-post</a><a class="sb" href="#">%s Ring oss</a><a class="sb p" href="#">%s Book et møte</a></div></div></section>'''%(HERO_P,stair,''.join('<div class="card"><div class="ic"><i>%d</i><u></u></div><h3>%s %s</h3><p>%s</p></div>'%(i+1,a,b,c) for i,(a,b,c) in enumerate([('Finn','riktige kunder','Hvem passer best, og hvorfor skal de snakke med dere nå.'),('Vinn','dem i møtet','Selgere som skaper tillit og tar gode beslutninger sammen med kunden.'),('Behold','dem over tid','Ledere som utvikler kulturen som får kundene til å bli.')])),Q1,QN,QR,IC['mail'],IC['tel'],IC['cal'])

# ---------------- B ----------------
cssB='''body{font-family:"Schibsted Grotesk",system-ui,sans-serif;background:#fff}
h1,h2,h3{font-weight:600;letter-spacing:-0.02em;margin:0}
.hero{background:#1B3A4B;color:#fff;position:relative;overflow:hidden}
.hero .in{max-width:1240px;margin:0 auto;padding:88px 40px 104px;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center}
.hero h1{font-size:60px;line-height:66px}.hero p{margin:26px 0 0;font-size:21px;line-height:32px;font-weight:500;color:#D3DCDF;max-width:30em}
.ph{position:relative;margin:0 32px 32px 0}
.ph::before{content:"";position:absolute;left:32px;top:32px;right:-32px;bottom:-32px;background:#356A89}
.ph::after{content:"";position:absolute;left:32px;top:32px;width:96px;height:96px;background:#7EA257;mix-blend-mode:normal;display:none}
.ph img{position:relative;display:block;width:100%;height:500px;object-fit:cover;clip-path:polygon(0 0,calc(100% - 48px) 0,100% 48px,100% 100%,0 100%)}
.btn{position:relative;display:inline-block;padding:16px 28px;font:600 17px "Schibsted Grotesk",sans-serif;color:#fff;text-decoration:none;z-index:0}
.btn::before{content:"";position:absolute;inset:0;z-index:-1;background:#4F7A2B;clip-path:polygon(0 0,calc(100% - 18px) 0,100% 22px,100% 100%,0 100%)}
.lnk{font-weight:600;color:#fff;text-decoration:none;font-size:18px}
.sec{max-width:1240px;margin:0 auto;padding:96px 40px 0}
.stp{display:grid;grid-template-columns:repeat(3,1fr);margin-top:40px;position:relative}
.stp>div{padding:0 32px 0 0}.stp .no{width:56px;height:56px;border:2px solid #356A89;display:grid;place-items:center;font-weight:700;color:#356A89;font-size:20px;background:#fff;position:relative;z-index:1}
.stp::before{content:"";position:absolute;left:0;right:0;top:27px;height:2px;background:#D3DCDF}
.stp h3{font-size:28px;margin-top:22px}.stp p{margin:8px 0 0;font-size:18px;line-height:28px;color:#566B76}
.qb{background:#1B3A4B;color:#fff;margin-top:96px}.qb .in{max-width:1240px;margin:0 auto;padding:88px 40px;display:grid;grid-template-columns:300px 1fr;gap:80px;align-items:center}
.pq{position:relative;margin:0 28px 28px 0}.pq::before{content:"";position:absolute;left:28px;top:28px;right:-28px;bottom:-28px;background:#356A89}
.pq div{position:relative;height:300px;background:#DCE7E0;color:#356A89;display:grid;place-items:center;font:700 64px "Schibsted Grotesk",sans-serif;clip-path:polygon(0 0,calc(100% - 40px) 0,100% 40px,100% 100%,0 100%)}
.qb p.l{font-size:34px;line-height:46px;font-weight:500;margin:0;letter-spacing:-.01em}.qb .n{margin-top:24px;font-weight:600}.qb .r{color:#D3DCDF;font-size:15px}
.bk{max-width:1240px;margin:0 auto;padding:72px 40px 96px}
.bks{display:flex;gap:16px;flex-wrap:wrap;margin-top:24px}
.s1{position:relative;padding:14px 24px;font:600 16px "Schibsted Grotesk",sans-serif;text-decoration:none;color:#356A89;border:2px solid #356A89;display:inline-flex;gap:10px;align-items:center}
.s1.p{background:#356A89;color:#fff}
'''
bodyB='''<section class="hero"><div class="in g2"><div><h1>Hvem vil dere vinne neste gang?</h1><p>%s</p><div class="fl" style="margin-top:40px;gap:28px"><a class="btn" href="#">Book en samtale</a><a class="lnk" href="#">Hva mangler hos dere? →</a></div></div><div class="ph"><img src="img/hero.jpg" alt="Samtale mellom kolleger"></div></div></section>
<section class="sec"><h2 style="font-size:44px;line-height:50px;max-width:16em">Finn, vinn og behold de riktige kundene</h2><div class="stp g2">%s</div></section>
<section class="qb"><div class="in g2"><div class="pq"><div>TF</div></div><div><p class="l">%s</p><p class="n">%s</p><p class="r">%s</p></div></div></section>
<section class="bk"><h2 style="font-size:32px">La oss ta en samtale</h2><div class="bks"><a class="s1" href="#">%s Send e-post</a><a class="s1" href="#">%s Ring oss</a><a class="s1 p" href="#">%s Book et møte</a></div></section>'''%(HERO_P,''.join('<div><span class="no">%d</span><h3>%s %s</h3><p>%s</p></div>'%(i+1,a,b,c) for i,(a,b,c) in enumerate([('Finn','riktige kunder','Hvem passer best, og hvorfor skal de snakke med dere nå.'),('Vinn','dem i møtet','Selgere som skaper tillit og tar gode beslutninger sammen med kunden.'),('Behold','dem over tid','Ledere som utvikler kulturen som får kundene til å bli.')])),Q1,QN,QR,IC['mail'],IC['tel'],IC['cal'])

# ---------------- C ----------------
cssC='''body{font-family:Inter,system-ui,sans-serif;background:#fff}
h1,h2,h3{font-weight:500;letter-spacing:-0.045em;margin:0}
.hero{background:#1B3A4B;color:#fff;position:relative;overflow:hidden}
.hero::after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:56px;background:#fff;border-radius:56px 56px 0 0}
.hero .in{max-width:1240px;margin:0 auto;padding:80px 40px 128px;display:grid;grid-template-columns:1.05fr .95fr;gap:72px;align-items:center;position:relative;z-index:1}
.ey{font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:#9CC06F;font-weight:600;display:flex;gap:10px;align-items:center}.ey::before{content:"";width:7px;height:7px;border-radius:50%;background:#9CC06F}
.hero h1{font-size:72px;line-height:70px;margin-top:22px}.hero h1 em{font-style:normal;color:#9CC06F}
.hero p{margin:26px 0 0;font-size:20px;line-height:31px;color:#C5D2D8;max-width:28em}
.ph{position:relative;margin:0 36px 36px 0}.ph::before{content:"";position:absolute;left:36px;top:36px;right:-36px;bottom:-36px;background:#356A89;border-radius:28px}
.ph img{position:relative;display:block;width:100%;height:480px;object-fit:cover;border-radius:28px;box-shadow:0 24px 50px rgba(0,0,0,.25)}
.pill{position:absolute;left:-24px;bottom:28px;background:#fff;color:#231F20;border-radius:16px;padding:14px 18px;box-shadow:0 12px 30px rgba(0,0,0,.22);display:flex;gap:12px;align-items:center;font-size:14px;line-height:18px}.pill b{display:block;font-size:16px;letter-spacing:-.02em}.pill i{width:12px;height:12px;border-radius:50%;background:#7EA257}
.b1{position:relative;display:inline-flex;gap:10px;align-items:center;background:#7EA257;color:#14290A;font:600 17px Inter,sans-serif;padding:16px 28px;border-radius:999px;text-decoration:none}
.b1::after{content:"";width:9px;height:9px;border-radius:50%;background:#14290A;transition:transform .3s}.b1:hover::after{transform:translate(3px,-5px) scale(1.5)}
.b2{color:#fff;font:600 17px Inter,sans-serif;text-decoration:none;padding:16px 8px}
.sec{max-width:1240px;margin:0 auto;padding:72px 40px 0}
.path{position:relative;margin-top:48px}
.path svg{display:block;width:100%;height:80px}
.nodes{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:-28px}
.nd{background:#fff;border:1px solid #E3E9EB;border-radius:24px;padding:28px 30px;box-shadow:0 10px 34px rgba(27,58,75,.08);position:relative}
.nd .dt{position:absolute;top:-8px;left:30px;width:16px;height:16px;border-radius:50%;background:#7EA257;box-shadow:0 0 0 5px #fff}
.nd h3{font-size:28px;line-height:32px;margin-top:10px}.nd p{margin:8px 0 0;font-size:17px;line-height:26px;color:#566B76}
.q{margin-top:96px;background:#EEF3F0;border-radius:32px;padding:64px;display:grid;grid-template-columns:auto 1fr;gap:56px;align-items:center;position:relative;overflow:hidden}
.q::before{content:"“";position:absolute;right:48px;top:-30px;font:500 260px/1 Inter;color:#DCE7E0}
.av{position:relative;width:150px;height:150px;border-radius:50%;background:#356A89;color:#fff;display:grid;place-items:center;font:600 42px Inter,sans-serif;box-shadow:0 0 0 8px #fff,18px 18px 0 0 #7EA257}
.q p.l{position:relative;font-size:34px;line-height:44px;letter-spacing:-.035em;margin:0;font-weight:500}.q .n{margin-top:22px;font-weight:600}.q .r{color:#566B76;font-size:15px}
.bar{margin:96px auto 0;max-width:1240px;padding:0 40px 96px}
.bi{background:#1B3A4B;color:#fff;border-radius:28px;padding:44px 48px;display:flex;justify-content:space-between;align-items:center;gap:28px;flex-wrap:wrap}
.bi h3{font-size:36px;letter-spacing:-.04em}.bi p{margin:8px 0 0;color:#C5D2D8}
.sb{display:inline-flex;gap:10px;align-items:center;padding:14px 22px;border:1px solid #4D6C7D;border-radius:999px;font:600 16px Inter,sans-serif;text-decoration:none;color:#fff}.sb.p{background:#fff;color:#1B3A4B;border-color:#fff}
'''
wave='<svg viewBox="0 0 1200 80" preserveAspectRatio="none" aria-hidden="true"><path d="M0 40 C150 10 300 70 450 40 S750 10 900 40 1050 60 1200 36" fill="none" stroke="#7EA257" stroke-width="3" stroke-dasharray="2 7" stroke-linecap="round"/></svg>'
bodyC='''<section class="hero"><div class="in g2"><div><span class="ey">Salgsutvikling og lederutvikling</span><h1>Hvem vil dere <em>vinne</em> neste gang?</h1><p>%s</p><div class="fl" style="margin-top:38px;gap:20px"><a class="b1" href="#">Book en samtale</a><a class="b2" href="#">Hva mangler hos dere?</a></div></div><div class="ph"><img src="img/hero.jpg" alt="Samtale mellom kolleger"><div class="pill"><i></i><div><b>Siden 1988</b>Salg og ledelse</div></div></div></div></section>
<section class="sec" style="padding-top:24px"><h2 style="font-size:48px;line-height:50px;max-width:14em">Finn, vinn og behold de riktige kundene</h2>
<div class="path">%s<div class="nodes g2">%s</div></div>
<div class="q g2"><div class="av">TF</div><div><p class="l">%s</p><p class="n">%s</p><p class="r">%s</p></div></div></section>
<section class="bar"><div class="bi"><div><h3>La oss ta en samtale</h3><p>Ring, skriv eller book direkte med en av fagekspertene.</p></div><div class="fl"><a class="sb" href="#">%s Send e-post</a><a class="sb" href="#">%s Ring oss</a><a class="sb p" href="#">%s Book et møte</a></div></div></section>'''%(HERO_P,wave,''.join('<div class="nd"><span class="dt"></span><h3>%s %s</h3><p>%s</p></div>'%(a,b,c) for a,b,c in [('Finn','riktige kunder','Hvem passer best, og hvorfor skal de snakke med dere nå.'),('Vinn','dem i møtet','Selgere som skaper tillit og tar gode beslutninger sammen med kunden.'),('Behold','dem over tid','Ledere som utvikler kulturen som får kundene til å bli.')]),Q1,QN,QR,IC['mail'],IC['tel'],IC['cal'])

for k,t,c,b in [('a','Forslag A',cssA,bodyA),('b','Forslag B',cssB,bodyB),('c','Forslag C',cssC,bodyC)]:
    open('/home/claude/fs/site/forslag-%s.html'%k,'w').write(page(k,'Excellerate – '+t,c,b))
