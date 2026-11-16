import re
CSS2=open("style2.css").read()
IC={'mail':'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>','tel':'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>'}
XS=lambda:'<svg aria-hidden="true" viewBox="0 0 700 700" class="ix"><line x1="80" y1="80" x2="620" y2="620" stroke-width="110"/><line x1="620" y1="80" x2="80" y2="620" stroke-width="110"/></svg>'
fs=fs.replace(CSS,CSS+"\n"+CSS2)
fs=fs.replace('family=Schibsted+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet">','family=Schibsted+Grotesk:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">',1)
# hero
a=fs.index('<section class="dyp hero"');b=fs.index('</section>',a)+10
hero='''<section class="dyp hero" style="color:#fff">
<div class="wrap hgrid">
<div><h1>Hvem vil dere <em>vinne</em> neste gang?</h1>
<p class="hlead">Excellerate hjelper ledere med å styrke konkurransekraften gjennom salgsutvikling og lederutvikling. Vi har hjulpet over 5 000 norske virksomheter med å finne, vinne og beholde de riktige kundene.</p>
<div class="hbtn"><a class="kn g" href="#samtale">Book en samtale</a><a class="xl-lenke lys" href="#mangler">Hva mangler hos dere?<span class="pil"></span></a></div></div>
<div class="hph"><img src="@@HERO@@" alt="Mann i samtale med kolleger"><div class="hpill"><i></i><div><b>Siden 1988</b>Salg og ledelse</div></div></div>
</div></section>'''.replace("@@HERO@@",U(IMG["hero"]))
fs=fs[:a]+hero+fs[b:]
# inngangskort: X-vannmerke
fs=fs.replace('<a class="ing" href="#"><span class="io">','<a class="ing" href="#">'+XS()+'<span class="io">')
# sitater
a=fs.index('<section class="dyp" style="background:#1B3A4B;color:#fff"><div class="wrap" style="padding-top:88px;padding-bottom:88px;display:grid');b=fs.index('</section>',a)+10
def qk(t,n,r,i):
    inner='<img src="%s" alt="%s">'%(U({'TF':'thomasfehnportrait','PG':'perGriwellportrait'}[i]),n)
    return '<div class="qk">'+XS()+'<div class="avw"><div class="av">%s</div></div><div style="position:relative"><p class="l">%s</p><p class="n">%s</p><p class="r">%s</p></div></div>'%(inner,t,n,r)
def qs(t,n,r,i,on):
    inner='<img src="%s" alt="%s">'%(U({'TF':'thomasfehnportrait','PG':'perGriwellportrait'}[i]),n)
    return '<div class="qslide%s"><div class="avw"><div class="av">%s</div></div><div><p class="l">%s</p><p class="n">%s</p><p class="r">%s</p></div></div>'%(" on" if on else "",inner,t,n,r)
QS=[("«Vi har skapt nye verdier, etablert nye informasjonskanaler og har fått et eget årshjul med tiltak for å bygge kultur.»","Thomas Fehn","Konserndirektør IT og digitalisering, Saint-Gobain Distribution","TF"),("«Med dyktig ledelse og assistanse fra spesialister i Excellerate, har selskapet løftet den kommersielle kulturen til et nytt nivå.»","Per Griwell","Kommersiell direktør, Thon Hotels","PG")]
q='<section class="qs"><div class="wrap" style="padding-top:72px;padding-bottom:72px"><div class="qk qrot" role="region" aria-roledescription="karusell" aria-label="Kundesitater">'+XS()+'<div class="qslides" aria-live="off">'+"".join(qs(*x,k==0) for k,x in enumerate(QS))+'</div><div class="qdots">'+"".join('<button type="button" class="qd%s" data-q="%d" aria-label="Vis sitat %d"></button>'%(" on" if k==0 else "",k,k+1) for k in range(len(QS)))+'</div></div></div></section>'
fs=fs[:a]+q+fs[b:]
# slik jobber vi: ingen tall i nodene er skjult via css. footer-CTA
fs=fs.replace('<a class="xl-btn-p xl-btn-g" href="#">Book en samtale</a>','<div style="display:flex;gap:14px;flex-wrap:wrap;align-items:center"><a class="kn g" href="#">Book en samtale</a><a class="kn l" href="mailto:post@excellerate.no">'+IC['mail']+' post@excellerate.no</a><a class="kn l" href="tel:+4722490000">'+IC['tel']+' +47 22 49 00 00</a></div>')
fs=fs.replace('class="xl-btn-p xl-btn-g"','class="kn g"')

a=fs.index('<div class="lrows">');b=fs.index('<div style="height:64px"></div>',a)
pick=['thon','maxbo','ramirent','synsam','wikborg','boligpartner','dn','fargerike','ruter','hertz','extra','polarn']
ids=dict(LOGOS2);
cells="".join('<div class="lc"><img src="%s" alt="%s"></div>'%(U(ids[n]),NM[n]) for n in pick)
fs=fs[:a]+'<div class="wrap"><div class="lgrid">'+cells+'</div></div>'+fs[b:]

fs=fs.replace('<div style="height:64px"></div></section>','<div style="height:8px"></div></section>',1)

fs=fs.replace('<h2 style="font-size:32px;line-height:38px;font-weight:500">Takk for tilliten</h2>','<h2 style="font-size:40px;line-height:46px;font-weight:500">Takk for tilliten</h2>',1)

# ---------- Resultater hos kunder ----------
def rc(img,navn,omr,tall,enhet,tekst,pos="50% 50%"):
    return '<a class="rc" href="#">'+XS()+'<div class="rci"><img src="%s" alt="" style="object-position:%s"></div><div class="rcb"><span class="rcl">%s</span><p class="rct">%s<small>%s</small></p><p class="rcx">%s</p><span class="xl-lenke">Les caset<span class="pil"></span></span></div></a>'%(img,pos,navn+" · "+omr,tall,enhet,tekst)
RC=rc(U(IMG["thon"]),"Thon Hotels","Pipeline","92 → 124"," mill. kr","Pipelinen økte fra 92 til 124 millioner kroner, og omsetningen vokste 5 prosent.")+rc(U(IMG["bolig"]),"BoligPartner","Leder- og salgsutvikling","+26"," % vekst","I 2014 falt bransjen 22 prosent. Treffprosenten økte fra 28 til 42,5.")+rc(U("wikborgnyttbilde"),"Wikborg Rein","Kompetanseutvikling","14"," dager","Alle advokater i Norge fikk opplæring i informasjonssikkerhet.","35% 30%")
a=fs.index('<div class="g3" style="margin-top:48px">');b=fs.index('</div>\n</div></section>',a)
fs=fs[:a]+'<div class="g3 rcg" style="margin-top:48px">'+RC+fs[b:]
# ---------- Møt fagekspertene ----------
CH={"salg":"Salg","ledelse":"Ledelse","kultur":"Kultur","ki":"KI"}
def fx(e):
    img='<img src="%s" alt="%s">'%(U(e[3]),e[0]) if e[3] else '<span class="fxph">TH</span>'
    ch="".join('<span class="fxch">%s</span>'%CH[o] for o in e[4].split() if o in CH)
    return '<a class="fx" href="'+FL(e)+'">'+XS()+'<div class="fxp">%s<span class="fxa" aria-hidden="true"></span></div><div class="fxt"><h3>%s</h3><p class="r">%s</p><p class="t">%s</p><div class="fxcs">%s</div></div></a>'%(img,e[0],e[1],e[2],ch)
a=fs.index('<div class="tog" tabindex="0"');b=fs.index('</div>\n</div></section>',a)
fs=fs[:a]+'<div class="tog" tabindex="0" aria-label="Fagekspertene">'+"".join(fx(e) for e in LED)+SEP+"".join(fx(e) for e in EXP)+fs[b:]
fs=fs.replace('Ett team, ett mål: resultater hos dere. Bla sidelengs.','Ett team, ett mål: resultater hos dere.')
_i=fs.index('Møt fagekspertene</h2>');_o='<a class="xl-lenke" href="Fagekspertene.dc.html">Se alle fagekspertene<span class="pil"></span></a></div>';_j=fs.index(_o,_i)
fs=fs[:_j]+'<div class="tgs"><a class="xl-lenke" href="Fagekspertene.dc.html">Se alle fagekspertene<span class="pil"></span></a><button type="button" class="tgb" data-d="-1" aria-label="Forrige"><span></span></button><button type="button" class="tgb" data-d="1" aria-label="Neste"><span></span></button></div></div>'+fs[_j+len(_o):]

# ---------- Slik jobber vi (trapp, som Backe-panelet) ----------
def lab(x,y,t,s,cls=""):
    return '<span class="stl %s" style="left:%.2f%%;top:%.2f%%"><b>%s</b><i>%s</i></span>'%(cls,x/560*100,y/400*100,t,s)
STAIR='<svg class="stsv" viewBox="0 0 560 400" aria-hidden="true"><path d="M30 330H140V265H270V200H400V135H520" fill="none" stroke="#9CC06F" stroke-width="3.5" stroke-dasharray="10 8" stroke-linejoin="round"/><circle cx="30" cy="330" r="12" fill="#9CC06F"/><circle cx="140" cy="265" r="9" fill="#1B3A4B" stroke="#fff" stroke-width="3"/><circle cx="270" cy="200" r="9" fill="#1B3A4B" stroke="#fff" stroke-width="3"/><circle cx="400" cy="135" r="9" fill="#1B3A4B" stroke="#fff" stroke-width="3"/><circle cx="520" cy="135" r="14" fill="#fff" stroke="#9CC06F" stroke-width="5"/></svg>'
STL=lab(22,350,"Her er dere","hvor står dere i dag?","s0")+lab(154,282,"Innsikt og fakta","forstå situasjonen","s1")+lab(284,217,"Rådgivning og metodeverk","finne riktig vei","s2")+lab(414,152,"Kompetanseheving","det som virker i hverdagen","s3")+lab(548,62,"Flere kunder","resultater over tid","s4")
SL='<section class="sec" style="padding-top:24px;padding-bottom:88px"><div class="wrap"><div class="trp2">'+XS()+'<div class="trl"><span class="tey"><i></i>Slik jobber vi</span><h2>Fra innsikt<br><em>til varig endring.</em></h2><p>Tre steg, sammen med dere.</p><a class="xl-lenke lys" href="#">Se hvordan vi jobber<span class="pil"></span></a></div><div class="trr"><div class="stw">'+STAIR+STL+'</div><ul class="trm"><li><b>Innsikt og fakta</b>forstå situasjonen</li><li><b>Rådgivning og metodeverk</b>finne riktig vei</li><li><b>Kompetanseheving</b>det som virker i hverdagen</li></ul><div class="trb"><img src="'+LOGOH+'" alt="Excellerate"><span>Finne. Vinne. Beholde.</span></div></div></div></div></section>'
a2=fs.index('<section class="sec" style="padding-bottom:72px">');b2=fs.index('Vi har lært opp de beste.',a2);b2=fs.index('</div></section>',b2)+len('</div></section>')
fs=fs[:a2]+SL+fs[b2:]
# ---------- Kunnskapssenter ----------
K1,K2,K3="/_blob/6aee73de7614899efc4561a8f50ec8d6","/_blob/db80b62da762e5e37fd701b9e92157de","/_blob/0a081d31223ec6fa18fe5a9f2aa94d8b"
def kt(cls,inner,img=None,href="#"):
    im='<img class="kbi" src="%s" alt="">'%img if img else ""
    return '<a class="kb %s" href="%s">%s%s</a>'%(cls,href,im,inner)
KB=(kt("k-stor",XS()+'<div class="kbp"><span class="bk">Fagartikkel</span><h3>Det som blir glemt når bedrifter kjøper bedrifter</h3><span class="lesl">Les artikkelen<span class="pil"></span></span></div>',U("kxa14"),"Kunnskap-glemt-bedrifter-kjoper-bedrifter.dc.html")
 +kt("k-art k-foto",'<span class="kbo"><span class="bk">Artikkel</span><h3>Tar salgsprosessen til et helt nytt nivå med AI</h3></span>',U("kxa03"),"Kunnskap-tar-salgsprosessen-til-et-helt-nytt-niva-med-ai.dc.html")
 +kt("k-fag k-bla",XS()+'<span class="bk">Fagartikler</span><h3>Fordypning for ledere og selgere</h3><span class="lesl">Les<span class="pil"></span></span>',None,"Kunnskap.dc.html?format=fag")
 +kt("k-split",'<div class="kbp"><span class="bk">Guide</span><h3>Rådgivende verdisalg, prinsipper og beste praksis i B2B-salg</h3><span class="lesl">Last ned<span class="pil"></span></span></div>',U(IMG["salg"]),"Kunnskap.dc.html?format=gui")
 +kt("k-web k-foto",'<span class="kbo"><span class="bk">Webinarer og arrangementer</span><h3>Kommende arrangementer</h3></span>',K3,"Kunnskap.dc.html?format=arr")
 +kt("k-case k-foto",'<span class="kbo"><span class="bk">Resultat hos kunde</span><h3>Thon Hotels, et kommersielt kulturløft</h3></span>',U(IMG["thon"]),"Referanse-thon.dc.html")
)
a=fs.index('<div class="bento">');b=fs.index('</div></div></section>',a)
fs=fs[:a]+'<div class="kbg">'+KB+'</div>'+fs[b+6:]


# ---------- Nyhetsbrev: egen modul før footeren ----------
IC={'google-icon': '<svg aria-hidden="true" viewBox="0 0 256 262" width="20" height="20"><path fill="#4285f4" d="M255.878 133.451c0-10.734-.871-18.567-2.756-26.69H130.55v48.448h71.947c-1.45 12.04-9.283 30.172-26.69 42.356l-.244 1.622l38.755 30.023l2.685.268c24.659-22.774 38.875-56.282 38.875-96.027"/><path fill="#34a853" d="M130.55 261.1c35.248 0 64.839-11.605 86.453-31.622l-41.196-31.913c-11.024 7.688-25.82 13.055-45.257 13.055c-34.523 0-63.824-22.773-74.269-54.25l-1.531.13l-40.298 31.187l-.527 1.465C35.393 231.798 79.49 261.1 130.55 261.1"/><path fill="#fbbc05" d="M56.281 156.37c-2.756-8.123-4.351-16.827-4.351-25.82c0-8.994 1.595-17.697 4.206-25.82l-.073-1.73L15.26 71.312l-1.335.635C5.077 89.644 0 109.517 0 130.55s5.077 40.905 13.925 58.602z"/><path fill="#eb4335" d="M130.55 50.479c24.514 0 41.05 10.589 50.479 19.438l36.844-35.974C195.245 12.91 165.798 0 130.55 0C79.49 0 35.393 29.301 13.925 71.947l42.211 32.783c10.59-31.477 39.891-54.251 74.414-54.251"/></svg>', 'apple': '<svg aria-hidden="true" viewBox="0 0 256 315" width="20" height="20"><path d="M213.803 167.03c.442 47.58 41.74 63.413 42.197 63.615c-.35 1.116-6.599 22.563-21.757 44.716c-13.104 19.153-26.705 38.235-48.13 38.63c-21.05.388-27.82-12.483-51.888-12.483c-24.061 0-31.582 12.088-51.51 12.871c-20.68.783-36.428-20.71-49.64-39.793c-27-39.033-47.633-110.3-19.928-158.406c13.763-23.89 38.36-39.017 65.056-39.405c20.307-.387 39.475 13.662 51.889 13.662c12.406 0 35.699-16.895 60.186-14.414c10.25.427 39.026 4.14 57.503 31.186c-1.49.923-34.335 20.044-33.978 59.822M174.24 50.199c10.98-13.29 18.369-31.79 16.353-50.199c-15.826.636-34.962 10.546-46.314 23.828c-10.173 11.763-19.082 30.589-16.678 48.633c17.64 1.365 35.66-8.964 46.64-22.262"/></svg>', 'linkedin-icon': '<svg aria-hidden="true" viewBox="0 0 256 256" width="20" height="20"><path fill="#0a66c2" d="M218.123 218.127h-37.931v-59.403c0-14.165-.253-32.4-19.728-32.4c-19.756 0-22.779 15.434-22.779 31.369v60.43h-37.93V95.967h36.413v16.694h.51a39.91 39.91 0 0 1 35.928-19.733c38.445 0 45.533 25.288 45.533 58.186zM56.955 79.27c-12.157.002-22.014-9.852-22.016-22.009s9.851-22.014 22.008-22.016c12.157-.003 22.014 9.851 22.016 22.008A22.013 22.013 0 0 1 56.955 79.27m18.966 138.858H37.95V95.967h37.97zM237.033.018H18.89C8.58-.098.125 8.161-.001 18.471v219.053c.122 10.315 8.576 18.582 18.89 18.474h218.144c10.336.128 18.823-8.139 18.966-18.474V18.454c-.147-10.33-8.635-18.588-18.966-18.453"/></svg>'}
def sob(k,t): return '<button type="button" class="nbs">%s<span>%s</span></button>'%(IC[k],t)
NBM=('<section class="nbm" aria-labelledby="nbt"><div class="wrap"><div class="nbi">'+XS()+'<div class="nbl"><span class="tey"><i></i>Nyhetsbrev</span><h2 id="nbt">Få ny innsikt rett i innboksen</h2><p>Artikler, guider og invitasjoner til arrangementer fra fagekspertene.</p></div>'
 '<form class="nbf" onsubmit="return false"><label for="nbe">E-postadresse</label><div class="nbr"><input id="nbe" type="email" placeholder="Din e-postadresse" autocomplete="email"><button type="submit" class="kn g">Abonner</button></div>'
 '<div class="nbo"><span>eller fortsett med</span></div><div class="nbb">'+sob('apple','Apple')+sob('google-icon','Google')+sob('linkedin-icon','LinkedIn')+'</div>'
 '<p class="nbp">Ved å abonnere godtar du at vi lagrer e-postadressen din. Du kan melde deg av når som helst. <a href="#">Personvern</a></p></form></div></div></section>')
_f=fs.index('<footer class="dyp fl"')
fs=fs[:_f]+NBM+fs[_f:]

fs=fs.replace('<p style="margin-top:16px;font-size:21px;line-height:32px;color:#C5D2D8">Ring oss på +47 22 49 00 00 eller skriv til post@excellerate.no.</p>','')
fs=fs.replace('<svg class="stsv" viewBox="0 0 560 400" aria-hidden="true">','<svg class="stsv" viewBox="0 0 560 400" aria-hidden="true"><line x1="270" y1="190" x2="270" y2="108" stroke="#9CC06F" stroke-width="2" stroke-dasharray="2 6" stroke-linecap="round" opacity=".6"/>',1)
fs=fs.replace('<span class="stl s0"','<div class="stc"><b>Deres mål</b><i>styrer retningen</i></div><span class="stl s0"',1)
