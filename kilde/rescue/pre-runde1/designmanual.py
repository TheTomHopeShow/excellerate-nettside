# Bygger site/designmanual.html (designmanual for Excellerate). Rører ikke andre sider.
import re, shutil, os, json
SRC = open('/home/claude/fs/build/build.py').read()
exec(SRC[SRC.index('EX=['):SRC.index('TOM=')])  # kun data
SITE = '/home/claude/fs/site/'
CSS = open('/home/claude/fs/build/dm_css.css').read() + open('/home/claude/fs/build/style5.css').read() + '.pg .kn5{display:block}.pg .kn5 .kkv,.pg .kn5 .kex2,.pg .kn5 .kcta{max-width:760px}.rg{margin-top:12px;font-size:15px;line-height:23px;color:var(--grey);max-width:760px}.rg b{color:var(--ink);font-weight:600}.dmgrid{display:grid;grid-template-columns:1fr 1fr;gap:40px 48px;margin-top:48px;align-items:start}.dmgrid>div>small{display:block;font-size:14px;font-weight:600;color:var(--grey);margin-bottom:14px}@media(max-width:900px){.dmgrid{grid-template-columns:1fr}}'
EXD = {e[0]: e for e in EX}

ICON = ('<svg class="ic" viewBox="222 268 49 59" aria-hidden="true"><path d="M224.4,269.4l28.5,56.3c2.8,0,9.2,0,15.5,0l-28.4-56.3z" fill="#356A89"/>'
        '<circle cx="261.5" cy="277.9" r="9.1" fill="#7EA257"/><circle cx="231.5" cy="317.2" r="9.1" fill="#7EA257"/></svg>')
def icon(h=40, bg=None):
    return '<svg viewBox="222 268 49 59" style="height:%dpx;width:auto;display:block" aria-hidden="true"><path d="M224.4,269.4l28.5,56.3c2.8,0,9.2,0,15.5,0l-28.4-56.3z" fill="#356A89"/><circle cx="261.5" cy="277.9" r="9.1" fill="#7EA257"/><circle cx="231.5" cy="317.2" r="9.1" fill="#7EA257"/></svg>' % h
def X(stroke, w=110, cls="x", style=""):
    return ('<svg aria-hidden="true" class="%s" style="%s" viewBox="0 0 700 700"><line x1="80" y1="80" x2="620" y2="620" stroke="%s" stroke-width="%d"/>'
            '<line x1="620" y1="80" x2="80" y2="620" stroke="%s" stroke-width="%d"/></svg>') % (cls, style, stroke, w, stroke, w)
def fit(w, h, inner, extra=""):
    return '<div class="fit" data-w="%d" data-h="%s"><div class="mk" style="width:%dpx;%s">%s</div></div>' % (w, h, w, ("height:%dpx;" % h if h != "auto" else "") + extra, inner)
LOGO = 'img/logo-xl.png'; LOGOH = 'img/logo-xl-hvit.png'

CHAP = ["Forside","Idéen","Logo","Farger","Skrift","Former og bevegelse","Komponenter","Stemme og bilder","Nettsiden","LinkedIn","Instagram","Annonser","Nyhetsbrev","Webinar","Artikkelbokser","Kunnskapssenter","Kontaktbokser","Mobil, bilder og fart","Typografi og lesbarhet","Status"]

def pg(i, cls, inner):
    return '<section class="pg %s" id="s%d" data-t="%s">%s</section>' % (cls, i, CHAP[i], inner)
def head(kick, title, lead="", tag=""):
    return '%s<div class="pk"><i></i>%s</div><h2>%s</h2>%s' % (tag, kick, title, ('<p class="lead">%s</p>' % lead) if lead else "")
FORSLAG = '<span class="tag f">Forslag, ikke godkjent</span>'
AVTALT = '<span class="tag">Avtalt</span>'

S = []
# ---------- 0 Forside ----------
S.append('<section class="cov" id="s0" data-t="Forside">' + X('#244A5E', 110) +
 '<div class="wrap"><img class="logo" src="%s" alt="Excellerate"><h1>Designmanual.<br><em>Slik ser vi ut.</em></h1>'
 '<p>Historien bak identiteten, de bærende elementene, og hvordan vi bruker dem på nett, i sosiale medier, annonser, nyhetsbrev og webinarer.</p>'
 '<div class="meta"><span>Utkast 13. november 2026</span><span>Utarbeidet av Tom Hope</span><span>Til gjennomgang med Per Kjetil Parr og Leif Ottesen</span></div></div></section>' % LOGOH)

# ---------- 1 Idéen ----------
S.append(pg(1, 'hz', '<div class="wrap">' + head('Idéen', 'Der to blikk møtes.',
 'X-en i logoen er bygget av én blå strek og to grønne prikker. Vi har gitt dem en betydning. Den styrer hvordan vi bruker dem overalt.', AVTALT) +
 '<div class="ide"><div class="stage">' + ICON + '</div><div class="leg">'
 '<div><i class="sw1" style="background:#356A89"></i><section><b>Blå: det som kan måles og ses utenfra</b><p>Fakta, tall og det markedet kan se. Blått er vårt objektive blikk.</p></section></div>'
 '<div><i class="sw1 c" style="background:#7EA257"></i><section><b>Grønn: retning og handling</b><p>Det som skal skje videre. Grønt er neste steg, aldri pynt.</p></section></div>'
 '<div><svg viewBox="222 268 49 59" style="height:36px;width:auto;display:block"><path d="M224.4,269.4l28.5,56.3c2.8,0,9.2,0,15.5,0l-28.4-56.3z" fill="#356A89"/><circle cx="261.5" cy="277.9" r="9.1" fill="#7EA257"/><circle cx="231.5" cy="317.2" r="9.1" fill="#7EA257"/></svg><section><b>X: innsikten</b><p>Der det objektive og det subjektive møtes. Tallene på den ene siden, menneskene på den andre.</p></section></div>'
 '<div><svg viewBox="0 0 44 44" style="height:36px;width:36px;display:block"><circle cx="11" cy="22" r="9" fill="#7EA257"/><circle cx="33" cy="22" r="9" fill="#7EA257"/></svg><section><b>Prikkene: leder og fagekspert</b><p>To mennesker som møtes i X-en og finner ut hva som mangler for at dere skal lykkes.</p></section></div></div></div>'
 '<div class="rules"><div><b>Blått for fakta</b><p>Tall, kilder og det som kan dokumenteres får blå flater og blå tekst.</p></div>'
 '<div><b>Grønt for handling</b><p>Knapper, neste steg og bevegelse. Grønt brukes ikke som dekor.</p></div>'
 '<div><b>X-en som vannmerke</b><p>Rolig, stor og avskåret mot kanten. Maks én per flate, aldri bak tekst som må leses nøye, og aldri bak bilder. Ikke i hero. På kort er den skjult og dukker opp når man peker på kortet.</p></div></div>'
 '<p class="note">Bakgrunnen: Excellerate har røtter tilbake til Euro Business School, grunnlagt i 1988. Identiteten bygger videre på logoen vi har, ikke på noe nytt. Fortellingen over er laget i dette designarbeidet og er til godkjenning.</p></div>'))

# ---------- 2 Logo ----------
dont = [('Strukket', 'transform:scaleX(1.5)'), ('Andre farger', 'filter:hue-rotate(150deg) saturate(1.6)'), ('Skygge og effekter', 'filter:drop-shadow(3px 4px 3px rgba(0,0,0,.55))'), ('Rotert', 'transform:rotate(-12deg)'), ('Bak travelt bilde', '')]
dh = ''
for t, st in dont:
    if t == 'Bak travelt bilde':
        dh += '<div><div class="bx" style="background:url(img/salg.jpg) center/cover"><img src="%s" alt="" style="opacity:.9"></div>%s</div>' % (LOGO, t)
    else:
        dh += '<div><div class="bx"><img src="%s" alt="" style="%s"></div>%s</div>' % (LOGO, st, t)
S.append(pg(2, '', '<div class="wrap">' + head('Logo', 'Logoen står som den er.', 'Den består av ordmerket og X-en med de to grønne prikkene. Vi endrer verken form, farge eller proporsjoner.', AVTALT) +
 '<div class="lg"><div class="lt"><img src="%s" alt="Excellerate"></div><div class="lt d"><img src="%s" alt="Excellerate, hvit"></div><div class="lt m"><img src="%s" alt="Excellerate"></div></div>'
 '<p class="cap">Fargelogo på hvit og lys bakgrunn. Hvit logo på dyp blå og på mørke flater. Fargene i logoen er #356A89 og #7EA257.</p>'
 '<div class="g2" style="margin-top:48px;align-items:start"><div><span class="tag f">Forslag, ikke godkjent</span><h3 style="font-size:30px;color:var(--deep)">Frirom og minste størrelse</h3>'
 '<p class="lead" style="font-size:17px;line-height:27px">Frirommet rundt logoen er minst høyden på logoen selv. På skjerm bruker vi ikke logoen mindre enn 20 px i høyde. Det er størrelsen i topplinjen på siden.</p>'
 '<div class="fl" style="margin-top:22px"><span>Ikon: X med to prikker, til profilbilder</span><span>Hvit logo på mørk bakgrunn</span><span>Fargelogo på hvit og lys bakgrunn</span></div></div>'
 '<div style="display:grid;place-items:center"><div class="clr"><img src="%s" alt=""></div></div></div>'
 '<h3 style="font-size:26px;color:var(--deep);margin-top:56px">Slik bruker vi den ikke</h3><div class="dont">%s</div>'
 '<p class="note">Logofilene (SVG, PNG, EPS, AI og PDF, også i hvit og som ikon) ligger i Dropbox under Excellerate / Brand identity / Logo. Ikonet i manualen er hentet fra de offisielle logofilene.</p></div>' % (LOGO, LOGOH, LOGO, LOGO, dh)))

# ---------- 3 Farger ----------
pal = [('#356A89', 'Blå', '53 · 106 · 137', 'Fra logoen. Fakta, tall, lenker og det objektive.', 'AVTALT'),
       ('#7EA257', 'Grønn', '126 · 162 · 87', 'Fra logoen. Prikker, streker og retning. Ikke til tekst.', 'AVTALT'),
       ('#1B3A4B', 'Dyp blå', '27 · 58 · 75', 'Mørke flater, overskrifter og hvit logo.', 'AVTALT'),
       ('#9CC06F', 'Lysgrønn', '156 · 192 · 111', 'Grønt på mørk bakgrunn: streker, prikker og understrek.', 'AVTALT'),
       ('#547B35', 'Knappegrønn', '84 · 123 · 53', 'Grønn knapp med hvit tekst. Mørknet for lesbarhet.', 'AVTALT'),
       ('#EAF0EC', 'Mint', '234 · 240 · 236', 'Rolige flater, kort og felt.', 'AVTALT'),
       ('#F3F6F5', 'Dis', '243 · 246 · 245', 'Sidebakgrunn mellom hvite seksjoner.', 'AVTALT'),
       ('#231F20', 'Tekst', '35 · 31 · 32', 'Brødtekst.', 'AVTALT'),
       ('#566B76', 'Dempet tekst', '86 · 107 · 118', 'Støttetekst og bildetekster.', 'AVTALT'),
       ('#D5DFE5', 'Linje', '213 · 223 · 229', 'Rammer og skillelinjer.', 'AVTALT')]
ph = ''.join('<div class="sw"><i style="background:%s;%s"></i><div><b>%s</b><code>%s</code><code>RGB %s</code><p>%s</p></div></div>' % (h, 'border-bottom:1px solid #D5DFE5' if h in ('#EAF0EC', '#F3F6F5', '#D5DFE5') else '', n, h, r, d) for h, n, r, d, _ in pal)
neu = [('#33383B', 'Brødtekst', '51 · 56 · 59', 'Lengre løpende tekst på lys bunn.'), ('#7B8E98', 'Svak tekst', '123 · 142 · 152', 'Hjelpetekst og plassholdere. Ikke til viktig tekst.'), ('#C5D2D8', 'Tekst på mørk', '197 · 210 · 216', 'Løpende tekst på dyp blå.'), ('#9FB6C3', 'Dempet på mørk', '159 · 182 · 195', 'Støttetekst på dyp blå.'), ('#4D6C7D', 'Deaktivert på mørk', '77 · 108 · 125', 'Utilgjengelige valg på dyp blå.'), ('#294F67', 'Linje og flate på mørk', '41 · 79 · 103', 'Rammer, knapper og hover på dyp blå.'), ('#DCE7E0', 'X på mint', '220 · 231 · 224', 'Vannmerket X på mint bunn.'), ('#244A5E', 'X på dyp blå', '36 · 74 · 94', 'Vannmerket X på dyp blå bunn.'), ('#4A83A3', 'X på blå', '74 · 131 · 163', 'Vannmerket X på blå bunn.')]
nh = ''.join('<div class="sw"><i style="background:%s;border-bottom:1px solid #D5DFE5"></i><div><b>%s</b><code>%s</code><code>RGB %s</code><p>%s</p></div></div>' % (h, n, h, r, t) for h, n, r, t in neu)
cr = [('Hvit på dyp blå', '#1B3A4B', '#fff', '12,0'), ('Hvit på blå', '#356A89', '#fff', '5,9'), ('Hvit på knappegrønn', '#547B35', '#fff', '4,9'), ('Dyp blå på lysgrønn', '#9CC06F', '#1B3A4B', '5,8'),
      ('Dyp blå på mint', '#EAF0EC', '#1B3A4B', '10,4'), ('Dempet tekst på hvit', '#fff', '#566B76', '5,6'), ('Hvit på grønn (logofargen)', '#7EA257', '#fff', '2,9')]
ct = ''.join('<tr><td><span class="pv" style="background:%s;color:%s;border:1px solid #D5DFE5">Aa</span></td><td>%s</td><td>%s : 1</td><td class="%s">%s</td></tr>' % (b, f, n, v, 'ok' if float(v.replace(',', '.')) >= 4.5 else 'no', 'Brukes til tekst' if float(v.replace(',', '.')) >= 4.5 else 'Ikke til tekst') for n, b, f, v in cr)
S.append(pg(3, 'hz', '<div class="wrap">' + head('Farger', 'Logoens to farger bærer alt.', 'Blå og grønn kommer fra logoen. Resten er laget for å gi ro rundt dem: en dyp blå, rolige flater og én mørk grønn som gjør at hvit tekst kan leses på knappene.', AVTALT) +
 '<div class="pal">%s</div>' % ph +
 '<div style="margin-top:44px"><span class="tag f">Forslag, ikke godkjent</span><h3 style="font-size:26px;color:var(--deep)">Nøytrale toner</h3><p class="cap" style="margin-bottom:18px">Alle gråtoner på nettsiden hører til ett av disse trinnene. Flere nyanser tillates ikke.</p><div class="pal">%s</div></div>' % nh +
 '<div style="margin-top:44px"><span class="tag f">Forslag, ikke godkjent</span><h3 style="font-size:26px;color:var(--deep)">Slik fordeler vi fargene</h3><div class="bal"><i style="flex:55;background:#fff"></i><i style="flex:15;background:#EAF0EC"></i><i style="flex:15;background:#1B3A4B"></i><i style="flex:9;background:#356A89"></i><i style="flex:6;background:#7EA257"></i></div><p class="cap">Mest hvitt og lyst. Dyp blå som tyngde. Blå og grønn som signaler, i små doser.</p></div>'
 '<table class="ct"><tr><th style="width:90px"></th><th>Kombinasjon</th><th>Kontrast</th><th>Bruk</th></tr>%s</table>'
 '<p class="src">Kontrastverdiene er regnet ut etter WCAG-formelen. Minst 4,5 : 1 kreves for vanlig tekst. Derfor brukes ikke logoens grønne til tekst, og knappene bruker den mørkere grønnen.</p></div>' % ct))

# ---------- 4 Skrift ----------
S.append(pg(4, '', '<div class="wrap">' + head('Skrift', 'Inter. Rolig og lett å lese.', 'Én skrift for alt, i to vekter. Inter har en åpen lisens, støtter norske tegn og fungerer like godt på skjerm som i dokumenter.', AVTALT) +
 '<div class="spec"><div class="big">Hva mangler for at dere skal lykkes?</div><div class="aa">ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ abcdefghijklmnopqrstuvwxyzæøå 0123456789 %&amp;€</div></div>'
 '<div class="sc2">'
 '<div><span>Hovedoverskrift</span><em style="font-size:56px;line-height:56px;letter-spacing:-.04em">Fra innsikt til varig endring.</em><span>56–70 / 58–68 · vekt 500 · -0,04 em</span></div>'
 '<div><span>Seksjonsoverskrift</span><em style="font-size:40px;line-height:46px;letter-spacing:-.04em">Fire områder som henger sammen</em><span>40–44 / 46–48 · vekt 500</span></div>'
 '<div><span>Kortoverskrift</span><em style="font-size:28px;line-height:32px;letter-spacing:-.04em">Rådgivende verdisalg</em><span>22–30 / 28–34 · vekt 500</span></div>'
 '<div><span>Ingress</span><em style="font-size:20px;line-height:31px">Vi hjelper deg å finne, vinne og beholde de rette kundene.</em><span>20 / 31 · vekt 500</span></div>'
 '<div><span>Brødtekst og meny</span><em style="font-size:16px;line-height:25px">Tjenester, Bransjer, Fageksperter, Kunnskap, Referanser, Om oss</em><span>16–18 / 25–28 · vekt 500</span></div>'
 '<div><span>Knapper og etiketter</span><em style="font-size:15px;font-weight:600">Book en samtale</em><span>15–16 · vekt 600</span></div>'
 '<div><span>Liten tekst</span><em style="font-size:14px;line-height:21px;color:#566B76">Kilde: Computas og Norstat, «KI-paradoksene 2026»</em><span>13–14 / 20–21 · vekt 500</span></div></div>'
 '<p class="note">Overskrifter har stram bokstavavstand (-0,04 em) for en rolig, moderne flate. I Word, PowerPoint og e-post som ikke kan vise Inter, brukes Arial som reserve. Denne reserven er et forslag.</p></div>'))

# ---------- 5 Former ----------
fm = [('Signaturhjørnet', '<div style="width:120px;height:80px;background:#EAF0EC;border-radius:4px 20px 4px 20px;border:1px solid #D5DFE5"></div>', 'Paneler, kort og kontaktfelt. To skarpe og to runde hjørner.', '4px 20px 4px 20px'),
      ('Knappehjørnet', '<div style="width:130px;height:44px;background:#547B35;border-radius:4px 12px 4px 12px"></div>', 'Knapper, chips og menyvalg. Samme form, mindre.', '4px 12px 4px 12px'),
      ('Bilder og felt', '<div style="display:flex;gap:14px;align-items:center"><div style="width:84px;height:64px;background:linear-gradient(135deg,#356A89,#1B3A4B);border-radius:18px"></div><div style="width:70px;height:40px;background:#fff;border:1px solid #1B3A4B;border-radius:8px"></div></div>', 'Hero-bilder har signaturhjørnet i stor utgave, med en blå flate forskjøvet mot nedre høyre. Ingen ramme, ingen skygge. Andre bilder har rundt hjørne. Skjemafelt er rolige og rette.', '4/28 hero · 18 px øvrige bilder · 8 px felt'),
      ('Portrett', '<div style="display:flex;gap:14px;align-items:center"><img src="img/portrett-leif.jpg" alt="" style="width:64px;height:64px;border-radius:50%;object-fit:cover;object-position:50% 14%"><img src="img/portrett-leif.jpg" alt="" style="width:64px;height:76px;border-radius:12px;object-fit:cover;object-position:50% 14%"></div>', 'Små runde portretter i meny og søk. Store, like beskårne portretter på kortene.', 'Rund · stor, brystbilde'),
      ('X som vannmerke', '<div style="position:absolute;inset:0;overflow:hidden">' + X('#DCE7E0', 110, 'x', 'right:-50px;bottom:-60px;width:170px;height:170px') + '</div>', 'Stor, avskåret mot kanten. Maks én per flate.', 'Stolpe 110/700'),
      ('Grønn prikk og strek', '<div style="display:flex;gap:18px;align-items:center"><span style="width:12px;height:12px;border-radius:50%;background:#7EA257;display:block"></span><span style="display:block;width:60px;height:2px;background:#7EA257"></span></div>', 'Prikken er neste steg. Streken under lenker og overskrifter er 2 px.', '#7EA257 · #9CC06F på mørkt'),
      ('Skygge', '<div style="width:120px;height:70px;background:#fff;border-radius:4px 20px 4px 20px;box-shadow:0 24px 50px -30px rgba(27,58,75,.45)"></div>', 'Bare myke skygger, bare på utvalgte paneler. Aldri på hvert kort.', 'Svak og lang'),
      ('Bevegelse', '<div style="font-size:14px;line-height:22px;color:#1B3A4B;text-align:center">inn 0,25 s<br>ut 0,08 s</div>', 'Hover tar sakte inn og slipper raskt. Prikken i knappen hopper. Fokusring og hover på blå knapper er #294F67. Rolig bevegelse reduseres hvis brukeren ber om det.', '0,25 s / 0,08 s')]
S.append(pg(5, 'mt', '<div class="wrap">' + head('Former og bevegelse', 'Få former, brukt konsekvent.', 'To hjørneformer og én skygge gjør at alt henger sammen, fra knapp til kontaktfelt.', AVTALT) +
 '<div class="fm">' + ''.join('<div class="it"><div class="sh">%s</div><b>%s</b><p>%s</p><code>%s</code></div>' % (a, t, d, c) for t, a, d, c in fm) + '</div></div>'))

# ---------- 6 Komponenter ----------
lei = EXD['Leif Ottesen']
S.append(pg(6, '', '<div class="wrap">' + head('Komponenter', 'Byggeklossene, slik de virker.', 'Dette er de samme delene som nettsiden er bygget av. Prøv å holde musen over dem.', AVTALT) +
 '<div class="cp"><div class="bx2"><small>Knapper</small><div class="row"><a class="kn g">Ta en samtale</a><a class="kn o">Les mer</a><a class="tl">Se alle fagekspertene<span class="pil"></span></a></div></div>'
 '<div class="bx2 dk"><small>Knapper på mørk bakgrunn</small><div class="row"><a class="kn g">Ta en samtale</a><a class="kn l">Les mer</a><a class="tl on">Se hvordan vi jobber<span class="pil"></span></a></div></div>'
 '<div class="bx2" style="background:var(--mint);border-color:var(--mint)"><small>Felt</small><div class="fld"><input placeholder="Din e-postadresse" aria-label="E-post"><a class="kn g">Abonner</a></div></div>'
 '<div class="bx2"><small>Kontaktfelt</small><div class="bar2"><div><h3>La oss ta en samtale</h3><p>Ring, skriv eller book direkte.</p></div><a class="kn g">Book en samtale</a></div></div>'
 '<div class="bx2"><small>Områdekort (mint, snur til mørkt)</small><a class="ing">' + X('#DCE7E0', 110) + '<span>Salgsutvikling</span><h3>Selg på verdi, ikke pris</h3></a></div>'
 '<div class="bx2"><small>Fagekspertkort</small><div class="ex"><div class="im"><img src="img/portrett-leif.jpg" alt=""></div><div class="t"><b>Leif Ottesen</b><i>Partner og hovedspesialist</i><p>' + lei[2] + '</p></div></div></div>'
 '<div class="bx2" style="background:var(--haze);border-color:var(--haze)"><small>Kundesitat med portrett (eksempel)</small><div style="display:flex;gap:22px;align-items:center;background:#fff;border-radius:4px 20px 4px 20px;padding:26px"><img src="img/portrett-tom.jpg" alt="" style="width:84px;height:84px;border-radius:50%;object-fit:cover;object-position:50% 14%;flex:none"><div><p style="margin:0;font-size:19px;line-height:27px;letter-spacing:-.02em;color:#1B3A4B">«Her står et ekte sitat fra en kunde.»</p><small style="display:block;margin-top:10px;color:#566B76">Navn Navnesen, rolle, virksomhet</small></div></div></div>'
 '<div class="bx2" style="background:var(--haze);border-color:var(--haze)"><small>Kundesitat med bilde (eksempel)</small><div style="display:flex;gap:22px;align-items:stretch;background:#fff;border-radius:4px 20px 4px 20px;overflow:hidden"><img src="img/resepsjon.jpg" alt="" style="width:150px;object-fit:cover;flex:none"><div style="padding:26px 26px 26px 0"><p style="margin:0;font-size:19px;line-height:27px;letter-spacing:-.02em;color:#1B3A4B">«Her står et ekte sitat fra en kunde.»</p><small style="display:block;margin-top:10px;color:#566B76">Navn Navnesen, rolle, virksomhet</small></div></div></div>'
 '<div class="bx2 dk" style="grid-column:1/3;position:relative;overflow:hidden"><small>Veien (forslag A): fra der kunden er, til målet</small><svg viewBox="30 20 500 300" style="width:100%;max-width:520px;display:block;margin:6px auto 0" aria-hidden="true"><path d="M60 270H180V210H300V150H420V90H500" fill="none" stroke="#9CC06F" stroke-width="3" stroke-dasharray="9 8" stroke-linejoin="round"/><circle cx="60" cy="270" r="11" fill="#9CC06F"/><circle cx="180" cy="210" r="9" fill="#1B3A4B" stroke="#fff" stroke-width="3"/><circle cx="300" cy="150" r="9" fill="#1B3A4B" stroke="#fff" stroke-width="3"/><circle cx="420" cy="90" r="9" fill="#1B3A4B" stroke="#fff" stroke-width="3"/><circle cx="500" cy="90" r="13" fill="#9CC06F"/><g font-family="Inter" fill="#fff"><text x="52" y="308" font-size="20" font-weight="600">Her er dere</text><rect x="318" y="26" rx="10" width="172" height="52" fill="#16313F" stroke="#35566A"/><text x="334" y="50" font-size="16" font-weight="600">Flere kunder</text><text x="334" y="68" font-size="13" fill="#9FB4BF">vunnet og beholdt</text></g></svg></div></div></div>'
))

# ---------- 7 Stemme og bilder ----------
S.append(pg(7, 'hz', '<div class="wrap">' + head('Stemme og bilder', 'Rolig, menneskelig og tydelig.', 'Hvordan vi skriver og hva vi viser avgjør om designet føles ekte.', FORSLAG) +
 '<div class="st"><div class="card"><h3>Slik skriver vi</h3><p>Korte setninger. Ingen buzzord. Vi snakker til intelligente mennesker, verken ovenfra eller over hodet på dem. Vi sier fageksperter, ikke konsulenter.</p></div>'
 '<div class="card"><h3>Håp, ikke frykt</h3><p>Vi peker mot muligheter. Vi bruker ikke frykt, haster eller overdrevne løfter. Tall har alltid en kilde, ellers står de ikke der.</p></div>'
 '<div class="card"><h3>Finne. Vinne. Beholde.</h3><p>Vår egen setning for hva vi hjelper kundene med. Spørsmålet vi åpner med er «Hva mangler for at dere skal lykkes?».</p></div></div>'
 '<div class="ph3"><div><img src="img/salg.jpg" alt=""></div><div><img src="img/resepsjon.jpg" alt=""></div><div><img src="img/kunnskap-webinar.jpg" alt=""></div></div>'
 '<p class="note">Bildestil: ekte mennesker i ekte situasjoner, naturlig lys og direkte blikk. Ingen stockbilder med smilende hender. Mennesker på bilder er norske eller europeiske. Det er avtalt 14. november 2026. Fagekspertenes portretter kommer fra fagekspertene selv. Artikkelbilder hentes i full størrelse fra originalen, aldri fra en nedskalert kopi. Lisens for bildene på bloggen er ikke bekreftet og står åpen. Kunders navn, logoer, sitater og bilder brukes bare med samtykke.</p></div>'))

# ---------- 8 Nettsiden ----------
S.append(pg(8, 'dp', '<div class="wrap">' + head('Nettsiden', 'Slik ser forsiden ut.', 'Alt i denne manualen er hentet fra siden under. Den lever på sin egen adresse og oppdateres underveis.', AVTALT) +
 '<div style="margin-top:40px;border-radius:12px;overflow:hidden;box-shadow:0 30px 70px -30px rgba(0,0,0,.6)"><img src="img/dm-forside.jpg" alt="Forsiden" style="width:100%;display:block"></div>'
 '<div class="row" style="margin-top:28px"><a class="kn g" href="index.html">Åpne nettsiden</a></div></div>'))

# ---------- 9 LinkedIn ----------
def li_profile():
    return fit(1128, 480,
     '<div style="height:191px;background:#1B3A4B;position:relative;overflow:hidden">' + X('#244A5E', 110, 'x', 'position:absolute;right:-40px;top:-190px;width:430px;height:430px') +
     '<div style="position:absolute;left:230px;top:0;bottom:0;display:flex;align-items:center;color:#fff;font-size:40px;letter-spacing:-.04em">Hva mangler for at dere skal lykkes?</div></div>'
     '<div style="position:absolute;left:36px;top:110px;width:150px;height:150px;background:#fff;border:4px solid #fff;border-radius:10px;display:grid;place-items:center;box-shadow:0 2px 10px rgba(0,0,0,.18)">' + icon(96) + '</div>'
     '<div style="padding:84px 40px 0"><div style="font-size:42px;font-weight:600;letter-spacing:-.03em;color:#231F20">Excellerate</div><div style="font-size:22px;color:#566B76;margin-top:6px">Finne. Vinne. Beholde. Siden 1988.</div>'
     '<div style="font-size:18px;color:#8A9BA4;margin-top:8px">Salgsutvikling, lederutvikling, kulturutvikling og KI · Oslo</div>'
     '<div style="display:flex;gap:14px;margin-top:22px"><span style="background:#356A89;color:#fff;padding:12px 30px;border-radius:30px;font-size:19px;font-weight:600">Følg</span><span style="border:2px solid #356A89;color:#356A89;padding:10px 28px;border-radius:30px;font-size:19px;font-weight:600">Besøk nettsiden</span></div></div>')
def post_stat():
    return fit(1200, 627, '<div style="position:absolute;inset:0;background:#1B3A4B">' + X('#244A5E', 110, 'x', 'position:absolute;right:-150px;top:-130px;width:760px;height:760px') + '</div>'
     '<img src="img/logo-xl-hvit.png" style="position:absolute;left:70px;top:60px;height:34px" alt="">'
     '<div style="position:absolute;left:70px;top:170px;width:820px;color:#fff;font-size:84px;line-height:86px;letter-spacing:-.04em">Bare <span style="color:#9CC06F">8 %</span> har målt en konkret gevinst av KI.</div>'
     '<div style="position:absolute;left:70px;bottom:54px;color:#C5D2D8;font-size:22px">Kilde: Computas og Norstat, «KI-paradoksene 2026», 914 virksomheter</div>')
def post_expert():
    return fit(1200, 627, '<div style="position:absolute;inset:0;background:#EAF0EC"></div>' + X('#DCE7E0', 110, 'x', 'position:absolute;right:-170px;bottom:-250px;width:700px;height:700px') +
     '<div style="position:absolute;left:80px;top:80px;width:400px;height:467px"><img src="img/portrett-leif.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 14%;border-radius:18px" alt=""></div>'
     '<div style="position:absolute;left:600px;top:120px;right:70px"><div style="font-size:26px;font-weight:600;color:#566B76">Møt fageksperten</div><div style="font-size:72px;line-height:74px;letter-spacing:-.04em;color:#1B3A4B;margin-top:18px">Leif Ottesen</div><div style="font-size:28px;color:#4A5F6A;margin-top:18px">Partner og hovedspesialist</div>'
     '<div style="margin-top:44px;display:inline-flex;gap:12px;align-items:center;background:#547B35;color:#fff;font-size:24px;font-weight:600;padding:18px 30px;border-radius:5px 15px 5px 15px">Les mer<span style="width:11px;height:11px;border-radius:50%;background:#fff"></span></div></div>'
     '<img src="img/logo-xl.png" style="position:absolute;left:80px;bottom:30px;height:26px;display:none" alt="">')
def slide(n):
    if n == 1:
        return fit(1080, 1080, '<div style="position:absolute;inset:0;background:#1B3A4B"></div>' + X('#244A5E', 110, 'x', 'position:absolute;right:-200px;bottom:-240px;width:800px;height:800px') +
         '<img src="img/logo-xl-hvit.png" style="position:absolute;left:80px;top:80px;height:34px" alt=""><div style="position:absolute;left:80px;top:280px;width:820px;color:#fff;font-size:100px;line-height:100px;letter-spacing:-.045em">Hva mangler for at dere skal lykkes?</div><div style="position:absolute;left:80px;bottom:80px;color:#C5D2D8;font-size:28px">Bla videre</div>')
    if n == 2:
        rows = ''.join('<div style="display:flex;gap:26px;align-items:center;padding:34px 0;border-top:2px solid #D5DFE5"><span style="width:20px;height:20px;border-radius:50%%;background:#7EA257;flex:none"></span><span style="font-size:52px;letter-spacing:-.03em;color:#1B3A4B">%s</span></div>' % t for t in ['Salgsutvikling', 'Lederutvikling', 'Kulturutvikling', 'KI, adopsjon og sikkerhet'])
        return fit(1080, 1080, '<div style="position:absolute;inset:0;background:#fff"></div><div style="position:absolute;left:80px;right:80px;top:130px"><div style="font-size:34px;font-weight:600;color:#566B76;margin-bottom:40px">Fire områder som henger sammen</div>' + rows + '</div>')
    return fit(1080, 1080, '<div style="position:absolute;inset:0;background:#EAF0EC"></div>' + X('#DCE7E0', 110, 'x', 'position:absolute;left:-220px;bottom:-260px;width:800px;height:800px') +
     '<div style="position:absolute;left:80px;top:230px;width:880px;color:#1B3A4B;font-size:96px;line-height:98px;letter-spacing:-.045em">La oss ta en samtale.</div>'
     '<div style="position:absolute;left:80px;top:560px;display:inline-flex;gap:16px;align-items:center;background:#547B35;color:#fff;font-size:34px;font-weight:600;padding:26px 44px;border-radius:7px 21px 7px 21px">Book en samtale<span style="width:15px;height:15px;border-radius:50%;background:#fff"></span></div>'
     '<div style="position:absolute;left:80px;bottom:80px;font-size:30px;color:#4A5F6A">post@excellerate.no · +47 22 49 00 00</div>')
def frame(inner, txt, who="Excellerate", sub="Sponset" ):
    return '<div class="frm"><div class="who"><i>' + icon(30) + '</i><div><b>%s</b><span>%s</span></div></div><div class="tx">%s</div>%s</div>' % (who, sub, txt, inner)
S.append(pg(9, 'hz', '<div class="wrap">' + head('LinkedIn', 'Profesjonell og faglig.', 'LinkedIn er vår flate for innsikt, referanser og fagekspertene. Ett budskap per innlegg, godt dokumentert, og alltid med et neste steg.', FORSLAG) +
 '<div style="margin-top:40px">' + li_profile() + '<p class="cap">Selskapsside. Omslag 1128 × 191 px, profilbilde 300 × 300 px. Hold viktig innhold i midten, for logoen dekker en del av omslaget.</p></div>'
 '<div class="g3" style="margin-top:48px"><div class="card"><h3>Innsikt</h3><p>Ett tall eller en iakttakelse, med kilde. «Bare 8 % har målt en gevinst av KI» er et eksempel.</p></div><div class="card"><h3>Fagekspertene</h3><p>Personene først. Presentasjoner, tanker og møter med fagekspertene.</p></div><div class="card"><h3>Resultater og arrangementer</h3><p>Referanser med samtykke, guider og invitasjoner til webinarer.</p></div></div>'
 '<div class="mgrid c2"><div>' + post_stat() + '<p class="cap">Innlegg, landskap: 1200 × 627 px. Innsikt med kilde.</p></div><div>' + post_expert() + '<p class="cap">Innlegg, landskap: 1200 × 627 px. Fagekspert.</p></div></div>'
 '<div class="mgrid c3" style="margin-top:28px"><div>' + slide(1) + '</div><div>' + slide(2) + '</div><div>' + slide(3) + '</div></div><p class="cap">Karusell (dokument), 1080 × 1080 px. Første bilde stopper scrollen, siste bilde ber om en handling.</p>'
 '<p class="src">Størrelsene følger anbefalingene i bransjens veiledere for 2026: selskapsside-omslag 1128 × 191 px, innlegg 1200 × 627 px og karusell 1080 × 1080 px. Kilder: <a href="https://www.dreikon.de/en/news/social-media/linkedin-image-sizes/">dreikon</a>, <a href="https://bannerboo.com/blog/linkedin-image-sizes/">Bannerboo</a>. Eksemplene er illustrasjoner, ikke publisert innhold.</p></div>'))

# ---------- 10 Instagram ----------
def tile(kind, a=None, b=None):
    if kind == 'img':
        return '<div style="position:relative;overflow:hidden"><img src="%s" style="width:100%%;height:100%%;object-fit:cover;object-position:%s;display:block" alt=""></div>' % (a, b or '50% 20%')
    if kind == 'mint':
        return '<div style="position:relative;overflow:hidden;background:#EAF0EC;display:flex;align-items:flex-end;padding:34px">' + X('#DCE7E0', 110, 'x', 'position:absolute;right:-90px;top:-100px;width:360px;height:360px') + '<span style="position:relative;font-size:46px;line-height:48px;letter-spacing:-.04em;color:#1B3A4B">%s</span></div>' % a
    if kind == 'deep':
        return '<div style="position:relative;overflow:hidden;background:#1B3A4B;display:flex;align-items:flex-end;padding:34px">' + X('#244A5E', 110, 'x', 'position:absolute;right:-90px;top:-100px;width:360px;height:360px') + '<span style="position:relative;font-size:46px;line-height:48px;letter-spacing:-.04em;color:#fff">%s</span></div>' % a
def ig_profile():
    g = [tile('img', 'img/resepsjon.jpg', '50% 50%'), tile('mint', 'Mandag. Kaffe først.'), tile('img', 'img/portrett-erik.jpg', '50% 14%'),
         tile('deep', 'Hva mangler hos dere akkurat nå?'), tile('img', 'img/kunnskap-webinar.jpg', '50% 40%'), tile('img', 'img/portrett-carl.jpg', '50% 14%'),
         tile('img', 'img/salg.jpg', '50% 40%'), tile('mint', 'Bak kulissene på Stortorvet 7'), tile('img', 'img/portrett-neda.jpg', '50% 14%')]
    return fit(1080, 1560, '<div style="padding:60px 60px 30px;display:flex;gap:50px;align-items:center"><div style="width:220px;height:220px;border-radius:50%;background:#fff;border:2px solid #D5DFE5;display:grid;place-items:center;flex:none">' + icon(120) + '</div>'
     '<div><div style="font-size:44px;font-weight:600;color:#231F20">excellerate</div><div style="font-size:30px;line-height:40px;color:#33383B;margin-top:14px">Hverdagen hos fagekspertene.<br>Finne. Vinne. Beholde.<br>Stortorvet 7, Oslo</div></div></div>'
     '<div style="display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:400px;gap:4px;margin-top:40px">' + ''.join(g) + '</div>')
def ig_post(n):
    if n == 1:
        return fit(1080, 1350, '<img src="img/resepsjon.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover" alt=""><div style="position:absolute;left:0;right:0;bottom:0;height:560px;background:linear-gradient(to top,rgba(27,58,75,.96),rgba(27,58,75,0))"></div>'
         '<div style="position:absolute;left:70px;bottom:80px;right:70px;color:#fff"><div style="font-size:30px;font-weight:600;color:#D3DCDF">Bak kulissene</div><div style="font-size:92px;line-height:92px;letter-spacing:-.045em;margin-top:16px">Mandag på Stortorvet 7.</div></div>')
    return fit(1080, 1350, '<div style="position:absolute;inset:0;background:#EAF0EC"></div>' + X('#DCE7E0', 110, 'x', 'position:absolute;right:-220px;top:-200px;width:820px;height:820px') +
     '<div style="position:absolute;left:80px;top:440px;right:80px;color:#1B3A4B;font-size:104px;line-height:104px;letter-spacing:-.045em">Hvem snakker du egentlig med?</div>'
     '<div style="position:absolute;left:80px;bottom:80px;display:flex;gap:16px;align-items:center"><span style="width:20px;height:20px;border-radius:50%;background:#7EA257"></span><span style="font-size:32px;color:#4A5F6A">Tre spørsmål før neste kundemøte</span></div>')
def ig_story():
    return fit(1080, 1920, '<div style="position:absolute;inset:0;background:#1B3A4B"></div>' + X('#244A5E', 110, 'x', 'position:absolute;right:-260px;top:-60px;width:1000px;height:1000px') +
     '<div style="position:absolute;left:80px;top:560px;right:80px;color:#fff;font-size:120px;line-height:120px;letter-spacing:-.045em">Hva mangler hos dere akkurat nå?</div>'
     '<div style="position:absolute;left:80px;right:80px;top:1130px;display:grid;gap:26px"><div style="background:#fff;color:#1B3A4B;border-radius:8px 24px 8px 24px;padding:38px 44px;font-size:48px;font-weight:600">Flere kunder</div><div style="background:#fff;color:#1B3A4B;border-radius:8px 24px 8px 24px;padding:38px 44px;font-size:48px;font-weight:600">Bedre ledelse</div></div>'
     '<img src="img/logo-xl-hvit.png" style="position:absolute;left:80px;bottom:180px;height:44px" alt="">')
S.append(pg(10, '', '<div class="wrap">' + head('Instagram', 'Hverdagen hos oss, litt lettere.', 'Instagram er den myke siden: bak kulissene, menneskene og små spørsmål. Samme farger og former som ellers, men med mer humor og mindre tekst.', FORSLAG) +
 '<div class="g3" style="margin-top:40px;align-items:start"><div>' + ig_profile() + '<p class="cap">Profil og rutenett. Profilbilde 320 × 320 px, vises som sirkel. Bland bilder av mennesker, korte tekstflater og spørsmål.</p></div>'
 '<div>' + ig_post(1) + '<p class="cap">Innlegg 1080 × 1350 px (4:5). Ekte bilde, kort tekst.</p><div style="height:28px"></div>' + ig_post(2) + '<p class="cap">Tekstflate. Ett spørsmål som åpner en samtale.</p></div>'
 '<div>' + ig_story() + '<p class="cap">Story 1080 × 1920 px (9:16). Et enkelt spørsmål med to svar.</p></div></div>'
 '<div class="g3" style="margin-top:44px"><div class="card"><h3>Bak kulissene</h3><p>Kontoret, møter, hverdagen. Små glimt som viser at det er mennesker her.</p></div><div class="card"><h3>Fagekspertene</h3><p>Portretter og korte spørsmål til en fagekspert.</p></div><div class="card"><h3>Spørsmål og svar</h3><p>Stories med avstemning. Svarene brukes i LinkedIn og nyhetsbrevet.</p></div></div>'
 '<p class="src">Størrelsene følger bransjens veiledere for 2026: profilbilde 320 × 320 px, innlegg 1080 × 1350 px (4:5) og stories 1080 × 1920 px (9:16). Kilder: <a href="https://aokmarketing.com/instagram-social-media-sizing-cheat-sheet-2014">AOK Marketing</a>, <a href="https://moda.app/resources/sizes/instagram">Moda</a>. Eksemplene er illustrasjoner. Vi har ikke opprettet en konto.</p></div>'))

# ---------- 11 Annonser ----------
def ad_land():
    return fit(1200, 627, '<img src="img/salg.jpg" style="position:absolute;right:0;top:0;width:620px;height:627px;object-fit:cover" alt=""><div style="position:absolute;left:0;top:0;bottom:0;width:640px;background:#1B3A4B;border-radius:0 40px 40px 0"></div>' + X('#244A5E', 110, 'x', 'position:absolute;left:-180px;bottom:-230px;width:600px;height:600px') +
     '<img src="img/logo-xl-hvit.png" style="position:absolute;left:60px;top:56px;height:30px" alt=""><div style="position:absolute;left:60px;top:170px;width:520px;color:#fff;font-size:68px;line-height:70px;letter-spacing:-.045em">Hva mangler for at dere skal lykkes?</div>'
     '<div style="position:absolute;left:60px;bottom:60px;display:inline-flex;gap:12px;align-items:center;background:#547B35;color:#fff;font-size:24px;font-weight:600;padding:18px 30px;border-radius:5px 15px 5px 15px">Ta en samtale<span style="width:11px;height:11px;border-radius:50%;background:#fff"></span></div>')
def ad_sq():
    return fit(1080, 1080, '<div style="position:absolute;inset:0;background:#EAF0EC"></div>' + X('#DCE7E0', 110, 'x', 'position:absolute;right:-200px;top:-220px;width:820px;height:820px') +
     '<div style="position:absolute;left:80px;top:90px;font-size:32px;font-weight:600;color:#566B76">Guide</div><div style="position:absolute;left:80px;top:160px;width:860px;color:#1B3A4B;font-size:92px;line-height:94px;letter-spacing:-.045em">Rådgivende verdisalg i B2B-salg</div>'
     '<img src="img/kunnskap-guide.jpg" style="position:absolute;left:80px;right:80px;bottom:190px;width:920px;height:300px;object-fit:cover;border-radius:18px" alt="">'
     '<div style="position:absolute;left:80px;bottom:60px;display:inline-flex;gap:14px;align-items:center;background:#547B35;color:#fff;font-size:32px;font-weight:600;padding:24px 40px;border-radius:6px 18px 6px 18px">Last ned guiden<span style="width:14px;height:14px;border-radius:50%;background:#fff"></span></div>')
S.append(pg(11, 'mt', '<div class="wrap">' + head('Annonser', 'Samme ro, tydeligere handling.', 'Annonsene bruker de samme delene som resten: ett budskap, ett bilde eller en flate, og én knapp. Mindre tekst enn du tror du trenger.', FORSLAG) +
 '<div class="mgrid c2" style="align-items:start"><div>' + frame(ad_land() + '<div class="adh"><div><span>excellerate.no</span><b>Hva mangler for at dere skal lykkes?</b></div><span class="kn o" style="padding:8px 16px;font-size:14px">Ta en samtale</span></div>',
 'Fire områder, ett team. Se hvordan fagekspertene hjelper salgs- og ledergrupper å finne, vinne og beholde de rette kundene.') + '<p class="cap">LinkedIn, enkeltbilde 1200 × 627 px. Tekstene er eksempler.</p></div>'
 '<div>' + frame(ad_sq() + '<div class="adh"><div><span>excellerate.no</span><b>Last ned guiden</b></div><span class="kn o" style="padding:8px 16px;font-size:14px">Last ned</span></div>', 'Hva skiller de beste selgerne? Les guiden om rådgivende verdisalg.') + '<p class="cap">LinkedIn eller Instagram, kvadrat 1080 × 1080 px. Innholdsannonse for en guide.</p></div></div>'
 '<div class="rules" style="margin-top:44px"><div><b>Ett budskap</b><p>Ett spørsmål eller ett tall per annonse. Resten hører hjemme på landingssiden.</p></div><div><b>Én handling</b><p>Én grønn knapp. Samme ord som på siden: «Ta en samtale», «Last ned guiden».</p></div><div><b>Ingen overdrivelser</b><p>Ingen frykt, ingen hastverk, ingen løfter vi ikke kan dokumentere.</p></div></div>'
 '<p class="src">Størrelser: enkeltbilde 1200 × 627 px og kvadrat 1080 × 1080 px, i tråd med bransjens veiledere for annonser på LinkedIn. Kilde: <a href="https://socialpilot.co/blog/linkedin-post-sizes-guide">SocialPilot</a>.</p></div>'))

# ---------- 12 Nyhetsbrev ----------
def nl():
    item = lambda t, d: '<div style="padding:22px 0;border-top:1px solid #D5DFE5"><div style="font-size:14px;font-weight:600;color:#566B76">%s</div><div style="font-size:21px;line-height:27px;letter-spacing:-.02em;color:#1B3A4B;margin-top:6px">%s</div></div>' % (t, d)
    return fit(640, "auto", '<div style="background:#fff;width:640px">'
     '<div style="padding:26px 36px"><img src="img/logo-xl.png" style="height:22px;display:block" alt=""></div>'
     '<div style="background:#1B3A4B;position:relative;overflow:hidden;padding:44px 36px 48px">' + X('#244A5E', 110, 'x', 'position:absolute;right:-90px;top:-90px;width:320px;height:320px') + '<div style="position:relative;color:#C5D2D8;font-size:14px;font-weight:600">Nytt fra fagekspertene</div><div style="position:relative;color:#fff;font-size:38px;line-height:42px;letter-spacing:-.04em;margin-top:12px">Hva mangler for at dere skal lykkes?</div></div>'
     '<div style="padding:30px 36px 8px"><img src="img/kunnskap-guide.jpg" style="width:100%;height:230px;object-fit:cover;border-radius:14px;display:block" alt=""><div style="font-size:14px;font-weight:600;color:#566B76;margin-top:18px">Guide</div><div style="font-size:26px;line-height:31px;letter-spacing:-.03em;color:#1B3A4B;margin-top:6px">Rådgivende verdisalg: prinsipper og beste praksis i B2B-salg</div>'
     '<div style="margin-top:20px"><span style="display:inline-block;background:#547B35;color:#fff;font-size:15px;font-weight:600;padding:13px 22px;border-radius:4px 12px 4px 12px">Last ned guiden</span></div></div>'
     '<div style="padding:18px 36px 8px">' + item('Artikkel', 'Siste fra fagekspertene') + item('Webinar', 'Kommende webinarer og arrangementer') + '</div>'
     '<div style="background:#EAF0EC;padding:30px 36px;margin-top:20px"><div style="font-size:22px;letter-spacing:-.03em;color:#1B3A4B">La oss ta en samtale</div><div style="font-size:15px;line-height:23px;color:#4A5F6A;margin-top:6px">Ring +47 22 49 00 00 eller skriv til post@excellerate.no.</div></div>'
     '<div style="padding:26px 36px 34px;font-size:12px;line-height:19px;color:#566B76">Excellerate AS · Stortorvet 7, Oslo<br>Du får denne e-posten fordi du har meldt deg på vårt nyhetsbrev. <span style="text-decoration:underline">Meld deg av</span> · <span style="text-decoration:underline">Personvern</span></div></div>')
S.append(pg(12, '', '<div class="wrap">' + head('Nyhetsbrev', 'Én hovedsak, ett neste steg.', 'Nyhetsbrevet er en fortsettelse av nettsiden: samme rolige flater, samme knapper og samme tone. Bygget slik at det virker i alle e-postprogrammer.', FORSLAG) +
 '<div class="g2" style="align-items:start;margin-top:40px"><div style="max-width:520px">' + nl() + '<p class="cap">Eksempel på oppsett, 640 px bredt.</p></div>'
 '<div><div class="card"><h3>Oppsettet</h3><p>Topplinje med logo. Mørk overskriftsflate med X. Én hovedsak med bilde og én grønn knapp. To korte oppføringer. Samtale-feltet nederst. Avmelding og personvern i bunnen.</p></div>'
 '<div class="card" style="margin-top:20px"><h3>Slik bygger vi det</h3><p>Bredde 600–640 px. Tabellbasert oppsett, så det vises likt i Outlook og Gmail. Knapper som ren tekst med bakgrunnsfarge, ikke bilder. Inter erstattes av Arial i programmer som ikke støtter den. Alltid en tydelig avmelding.</p></div>'
 '<div class="card" style="margin-top:20px"><h3>Påmelding</h3><p>Nyhetsbrevmodulen nederst på forsiden har e-postfelt og innlogging med Apple, Google og LinkedIn. Den er ikke koblet til en e-posttjeneste ennå.</p></div></div></div></div>'))

# ---------- 13 Webinar ----------
def web_title():
    return fit(1920, 1080, '<div style="position:absolute;inset:0;background:#1B3A4B"></div>' + X('#244A5E', 110, 'x', 'position:absolute;right:-260px;top:-200px;width:1300px;height:1300px') +
     '<img src="img/logo-xl-hvit.png" style="position:absolute;left:130px;top:110px;height:54px" alt="">'
     '<div style="position:absolute;left:130px;top:330px;width:1100px"><div style="font-size:36px;font-weight:600;color:#9CC06F">Webinar</div><div style="color:#fff;font-size:150px;line-height:150px;letter-spacing:-.045em;margin-top:24px">Kunsten å lytte i salg</div></div>'
     '<div style="position:absolute;left:130px;bottom:120px;color:#C5D2D8;font-size:36px;display:flex;gap:46px"><span>[Dato]</span><span>[Klokkeslett]</span><span>Med [Navn], fagekspert</span></div>')
def web_invite():
    return fit(1200, 627, '<div style="position:absolute;inset:0;background:#EAF0EC"></div>' + X('#DCE7E0', 110, 'x', 'position:absolute;right:-160px;top:-180px;width:760px;height:760px') +
     '<img src="img/logo-xl.png" style="position:absolute;left:70px;top:60px;height:32px" alt="">'
     '<div style="position:absolute;left:70px;top:170px;width:760px"><div style="font-size:28px;font-weight:600;color:#566B76">Webinar · [dato] · [klokkeslett]</div><div style="color:#1B3A4B;font-size:92px;line-height:92px;letter-spacing:-.045em;margin-top:20px">Kunsten å lytte i salg</div></div>'
     '<div style="position:absolute;left:70px;bottom:56px;display:inline-flex;gap:12px;align-items:center;background:#547B35;color:#fff;font-size:24px;font-weight:600;padding:18px 30px;border-radius:5px 15px 5px 15px">Meld deg på<span style="width:11px;height:11px;border-radius:50%;background:#fff"></span></div>')
def web_lower():
    return fit(1920, 1080, '<div style="position:absolute;inset:0;background:linear-gradient(135deg,#5B7C8D,#2A4757)"></div><div style="position:absolute;left:0;right:0;top:0;bottom:0;display:grid;place-items:center;color:rgba(255,255,255,.35);font-size:44px">Bilde av foredragsholder</div>'
     '<div style="position:absolute;left:100px;bottom:100px;display:flex;align-items:stretch"><div style="width:10px;background:#9CC06F;border-radius:3px"></div><div style="background:#1B3A4B;padding:28px 46px 30px 36px;border-radius:0 6px 22px 0"><div style="color:#fff;font-size:54px;letter-spacing:-.03em">Navn Navnesen</div><div style="color:#C5D2D8;font-size:30px;margin-top:6px">Fagekspert · Excellerate</div></div></div>'
     '<img src="img/logo-xl-hvit.png" style="position:absolute;right:100px;top:90px;height:40px" alt="">')
S.append(pg(13, 'hz', '<div class="wrap">' + head('Webinar', 'Fra invitasjon til siste lysbilde.', 'Webinarene er motoren for innhold fra januar. Alt som vises, fra invitasjon til navnebånd, følger samme oppsett.', FORSLAG) +
 '<div class="mgrid c2" style="align-items:start"><div>' + web_invite() + '<p class="cap">Invitasjon for LinkedIn og e-post, 1200 × 627 px.</p></div><div>' + web_title() + '<p class="cap">Tittellysbilde, 1920 × 1080 px.</p></div></div>'
 '<div style="max-width:760px;margin-top:36px">' + web_lower() + '<p class="cap">Navnebånd over bilde av foredragsholder, 1920 × 1080 px. Grønn strek til venstre, dyp blå flate.</p></div>'
 '<p class="note">Tittel, dato og navn er plassholdere. «Kunsten å lytte i salg» er et eksempel på tema, ikke en avtale. Webinarplattform og plan avklares med den som bygger webinarstrategien.</p></div>'))

# ---------- 14 Status ----------

# ---------- 14 Artikkelbokser ----------
_X5 = '<svg aria-hidden="true" viewBox="0 0 700 700" class="ix"><line x1="80" y1="80" x2="620" y2="620" stroke-width="110"/><line x1="620" y1="80" x2="80" y2="620" stroke-width="110"/></svg>'
S.append(pg(14, 'hz', '<div class="wrap">' + head('Artikkelbokser', 'Boksene som holder en artikkel sammen.', 'Hver boks har én jobb, og er den samme på alle artikler. Slik blir artiklene raske å lese, og lette for både folk og søkemotorer å hente ut svaret fra.', FORSLAG) +
 '<div class="kn5"><div class="dmgrid">'
 '<div><small>Kortversjon</small><div class="kkv"><h2>Kortversjon</h2><ul><li>Svaret i én til tre setninger.</li><li>Det leseren skal gjøre eller huske.</li></ul></div><p class="rg"><b>Når:</b> øverst i hver artikkel, rett under ingressen. <b>Maks:</b> 3 punkter, én setning hver. Skal kunne stå alene som svar.</p></div>'
 '<div><small>Hovedfunn (mørk)</small><div class="kkv hf"><h2>Hovedfunn</h2><ul><li>Hovedpoeng én, i en setning.</li><li>Hovedpoeng to, i en setning.</li><li>Hovedpoeng tre, i en setning.</li></ul></div><p class="rg"><b>Når:</b> fagartikler og guider, der tallene og konklusjonene bærer innholdet. Bruk kortversjon i vanlige artikler, hovedfunn i fagartikler. Aldri begge.</p></div>'
 '<div><small>Ekspert-boks, lenker til fageksperten</small><a class="kex2" href="#"><img src="img/portrett-neda.jpg" alt=""><div><small>Artikkelens fagekspert</small><b>Neda Maria Kaizumi</b><span>Fagekspert. Se profil og book en samtale.</span></div><i class="pi"></i></a><p class="rg"><b>Når:</b> rett etter kortversjonen. <b>Regel:</b> lenker alltid til fagekspertens egen side, og samme navn står i byline og i artikkelens strukturerte data. Flere forfattere gir én boks hver.</p></div>'
 '<div><small>Personlig handling (slutten)</small><div class="kcta">' + _X5 + '<img src="img/portrett-neda.jpg" alt="Neda Maria Kaizumi"><div><h2>Ta en uforpliktende samtale</h2><p>Vil du høre hvordan dette ser ut hos dere?</p><div class="kbs"><a class="kn g" href="#">Book en samtale</a><a class="kn l" href="#">Send e-post</a></div></div></div><p class="rg"><b>Når:</b> én gang, til slutt. <b>Regel:</b> én hovedhandling, og alltid med fageksperten som har skrevet artikkelen. X-en er statisk her, og bare her.</p></div>'
 '<div><small>Tabell</small><div class="ktb"><table><thead><tr><th>Tilnærming</th><th>Passer når</th></tr></thead><tbody><tr><td>Alternativ A</td><td>Kort beskrivelse</td></tr><tr><td>Alternativ B</td><td>Kort beskrivelse</td></tr></tbody></table></div><p class="rg"><b>Når:</b> sammenligning av 2 til 5 alternativer. Ekte HTML-tabell med overskriftsrad, aldri bilde av tabell. Ruller sideveis på mobil.</p></div>'
 '<div><small>Vanlige spørsmål</small><div class="kfaq"><details open><summary>Spørsmål slik leseren stiller det?</summary><p>Kort, direkte svar på to til fire setninger.</p></details><details><summary>Hvor lang tid tar det?</summary><p>Svaret kommer her.</p></details></div><p class="rg"><b>Når:</b> 3 til 6 spørsmål nederst i lange artikler. Bare spørsmål som faktisk står på siden. Samme tekst i strukturerte data som på siden.</p></div>'
 '</div><div class="avt" style="margin-top:56px"><div><h3><i style="background:#356A89"></i>Brødtekst</h3><ul><li>Ingress: 1 til 2 setninger, inntil 30 ord</li><li>Avsnitt: 3 til 4 linjer, én tanke hver</li><li>Linjelengde: 60 til 75 tegn</li><li>Mellomtittel (H2) minst hver 250 til 300 ord</li><li>Sitat, tabell eller boks minst hver 600 ord</li></ul></div>'
 '<div><h3><i style="background:#7EA257"></i>Navigasjon</h3><ul><li>Innholdsfortegnelse til venstre på desktop</li><li>«Innhold»-rad som lukkes ut på mobil</li><li>Leseindikator øverst</li><li>Delingsrad til høyre, flat på mobil</li><li>Neste og forrige artikkel nederst, deretter «Les også»</li></ul></div>'
 '<div><h3><i style="background:#E0B000"></i>Kilder og dato</h3><ul><li>Kilder samles under «Kilder» med lenke og årstall</li><li>«Sist oppdatert» vises over teksten</li><li>Tall uten kilde publiseres ikke</li><li>Kundenavn og sitat bare med samtykke</li></ul></div></div></div></div>'))

# ---------- 15 Kunnskapssenter ----------
def _kcm(t, label, img, title, ing, foot, cls=""):
    return ('<a class="kc" href="#"><div class="kci %s"><img src="img/%s" alt="">%s</div><div class="kcb"><div class="ktr"><span class="ktag %s">%s</span></div><h3>%s</h3><p>%s</p>%s</div></a>' % (cls, img, ('<span class="kfmt">%s</span>' % label) if label else "", t, {"art":"Artikkel","fag":"Fagartikkel","gui":"Guide","ebo":"E-bok","arr":"Arrangement"}[t], title, ing, foot))
_ft = '<div class="kcf"><img class="kav" src="img/portrett-arvid.jpg" alt=""><div><b>Arvid Madland Lyngnes</b>Lesetid 5 min</div></div>'
S.append(pg(15, '', '<div class="wrap">' + head('Kunnskapssenter', 'Finn det du trenger, uten å lete.', 'Filteret er en setning som leseren fyller ut. Formatene er faner med antall. Alle kort har et bilde, så ingenting står tomt.', FORSLAG) +
 '<div class="kn5"><div class="kfil2" style="margin-top:44px"><p class="ksent">Jeg er <label><select aria-label="Din rolle" style="width:210px"><option>salgsdirektør</option></select></label> og vil lære om <label><select aria-label="Område" style="width:200px"><option>salgsutvikling</option></select></label>.<button class="kn o ksw" type="button">Nullstill</button></p><div class="ktabs"><button class="ktab on" type="button">Alt <span class="n">12</span></button><button class="ktab" type="button">Artikler <span class="n">5</span></button><button class="ktab" type="button">Fagartikler <span class="n">2</span></button><button class="ktab" type="button">Guider <span class="n">1</span></button><button class="ktab" type="button">E-bøker <span class="n">2</span></button><button class="ktab" type="button">Arrangementer <span class="n">2</span></button></div></div>'
 '<p class="rg" style="max-width:900px;margin-top:18px"><b>Hvorfor ikke tre rader med knapper?</b> Det ble tungt og så ut som et skjema. Setningen er lett å forstå, bruker standard nedtrekk som fungerer med tastatur og skjermleser og gir stor trykkflate på mobil. Fanene gir oversikt over hvor mye som finnes i hvert format. Alle valg kan nullstilles med én knapp, og antallet oppdateres underveis. Søk ligger i toppen av siden.</p>'
 '<div class="kgr" style="margin-top:40px">' + _kcm('art', '', 'kunnskap-artikler.jpg', 'Artikkel', 'Ett bilde, tittel, ingress og forfatter med portrett.', _ft) + _kcm('gui', 'PDF-guide', 'kunnskap-guide.jpg', 'Guide', 'Bilde med merke som viser at det er et dokument.', '<div class="kcf"><span class="klock">Gratis med skjema</span></div>') + _kcm('arr', '', 'kunnskap-webinar.jpg', 'Arrangement', 'Bilde med mørkt felt og dato.', '<div class="kcf"><span class="klock">Se detaljer og meld deg på</span></div>', 'dk').replace('<div class="kci dk"><img src="img/kunnskap-webinar.jpg" alt="">', '<div class="kci dk"><img src="img/kunnskap-webinar.jpg" alt=""><div class="kdt"><b>16. sep</b><span>08.00–10.00</span></div>') + '</div>'
 '<div class="avt" style="margin-top:56px"><div><h3><i style="background:#356A89"></i>Bilder på kort</h3><ul><li>Alle kort har bilde. Ingen tomme felt</li><li>Ikke bokomslag. Bruk foto av mennesker i en ekte situasjon</li><li>Guide og e-bok får merke nede til venstre</li><li>Arrangement får mørk overlegg med dato</li><li>Format 16:9, beskjæres automatisk</li></ul></div>'
 '<div><h3><i style="background:#7EA257"></i>Taksonomi</h3><ul><li>Format: artikkel, fagartikkel, guide, e-bok, arrangement</li><li>Område: de fire tilbudene</li><li>Rolle: hvem artikkelen er skrevet for</li><li>Én kategori per innhold, 2 til 5 stikkord</li><li>Stikkordsider indekseres ikke før de har minst 5 innhold</li></ul></div>'
 '<div><h3><i style="background:#E0B000"></i>Skjema og gating</h3><ul><li>Navn, e-post og virksomhet. Aldri telefon som krav</li><li>Samtykke i klartekst, før knappen</li><li>Bekreftelse viser neste steg</li><li>Artikler er alltid åpne. Bare guider og e-bøker har skjema</li></ul></div></div></div></div>'))

# ---------- 16 Kontaktbokser ----------
S.append(pg(16, 'hz', '<div class="wrap">' + head('Kontaktbokser', 'Det skal alltid være lett å ta kontakt.', 'Tre bokser med hver sin jobb. Tom og Per Kjetil er kontaktpunktene i salg. Fageksperten er kontaktpunktet når artikkelen er hennes eller hans.', FORSLAG) +
 '<div class="kn5"><div class="dmgrid">'
 '<div><small>Kompakt kontaktboks (kkb)</small><aside class="kkb"><div class="kkf"><img src="img/portrett-tom.jpg" alt=""><img src="img/portrett-per-kjetil.jpg" alt=""></div><div class="kkt"><h2>Usikker på hvem du bør snakke med?</h2><p>Tom Hope og Per Kjetil Parr hjelper deg til riktig fagekspert.</p></div><div class="kkx"><a class="kn g" href="#">Skriv til oss</a><a class="kn o" href="#">Ring 22 49 00 00</a></div></aside><p class="rg"><b>Når:</b> nederst på alle artikler og referanser, rett etter personlig handling. <b>Hvem:</b> alltid Tom og Per Kjetil. <b>Mål:</b> den som ikke vet hvem hun skal ringe, skal slippe å lete. Maks to knapper.</p></div>'
 '<div><small>Kontaktpersonkort (kkp)</small><div class="kkp"><img src="img/portrett-per-kjetil.jpg" alt=""><div><b>Per Kjetil Parr</b><span>Administrerende direktør</span><p>Én setning om hva personen kan hjelpe med.</p><a class="kkl" href="#">90 89 05 09</a><div class="kbs"><a class="kn g" href="#">Book en samtale</a><a class="kn o" href="#">Send e-post</a></div></div></div><p class="rg"><b>Når:</b> på Om oss, Kontakt og landingssider for tjenester og arrangementer. <b>Regel:</b> bilde, navn, tittel, én setning, én hovedknapp. Telefon og e-post vises bare når de er avklart med personen.</p></div>'
 '<div><small>Personlig handling og fageksperten</small><a class="kex2" href="#"><img src="img/portrett-neda.jpg" alt=""><div><small>Artikkelens fagekspert</small><b>Neda Maria Kaizumi</b><span>Fagekspert. Se profil og book en samtale.</span></div><i class="pi"></i></a><p class="rg"><b>Når:</b> i artikler skrevet av en fagekspert. Fageksperten kommer først, kontaktboksen med Tom og Per Kjetil kommer sist. Aldri to store handlingsbokser etter hverandre.</p></div>'
 '</div><div class="avt" style="margin-top:56px"><div><h3><i style="background:#356A89"></i>Hvor de står</h3><ul><li>Artikkel: fagekspert-boks øverst, personlig handling og kompakt kontaktboks nederst</li><li>Referanse: kontaktboks etter «Vil dere ha tilsvarende resultater?»</li><li>Om oss: to kontaktpersonkort ved siden av skjemaet</li><li>Forside og tjenestesider: kontaktpersonkort i siste seksjon</li></ul></div><div><h3><i style="background:#7EA257"></i>Lenker</h3><ul><li>Eksterne lenker åpnes i ny fane, så besøkende blir på nettstedet. Gjelder kart, LinkedIn, kilder og andre nettsteder</li><li>Interne lenker åpnes i samme fane</li><li>E-post og telefon åpner e-post- og telefonprogrammet</li></ul></div>'
 '<div><h3><i style="background:#7EA257"></i>Skjema</h3><ul><li>Navn, e-post og samtykke er påkrevd. Telefon aldri</li><li>«Hvem vil du snakke med?» forhåndsvelges fra boksen som ble trykket på</li><li>Tema forhåndsvelges fra siden brukeren kom fra</li><li>Bekreftelsen viser neste steg, ikke bare «takk»</li></ul></div>'
 '<div><h3><i style="background:#E0B000"></i>Åpent</h3><ul><li>Toms e-post og telefon på excellerate.no</li><li>Om Tom får egen profilside med booking</li><li>Hvor skjemaet sendes: e-post, CRM eller begge</li><li>Svartid vi kan love, for eksempel «innen en arbeidsdag»</li></ul></div></div></div></div>'))

# ---------- 17 Mobil, bilder og fart ----------
S.append(pg(17, 'mt', '<div class="wrap">' + head('Mobil, bilder og fart', 'Siden skal være lynrask, på alle skjermer.', 'Mobil er utgangspunktet, og regler for bilder og fart er en del av designet.', FORSLAG) +
 '<div class="avt" style="margin-top:44px"><div><h3><i style="background:#356A89"></i>Mobil</h3><ul><li>Brytpunkter: 1180 px og 720 px</li><li>Trykkflater minst 44 × 44 px</li><li>Ingen sideveis rulling på siden</li><li>Meny som panel med stor handlingsknapp</li><li>Skjemafelt minst 16 px tekst, så telefonen ikke zoomer</li><li>Sticky element får ikke dekke teksten</li><li>Tabeller ruller i sin egen boks</li></ul></div>'
 '<div><h3><i style="background:#7EA257"></i>Bilder</h3><ul><li>WebP, kvalitet rundt 75 til 80</li><li>Alltid fast bildeforhold (aspect-ratio), så siden ikke hopper</li><li>Første bilde på siden lastes direkte. Resten er «lazy»</li><li>Portretter 360 × 450 px. Foto maks 1600 px bredt</li><li>Beskrivende filnavn med bindestrek, små bokstaver</li><li>Alt-tekst som beskriver bildet. Tom alt bare når bildet er ren pynt</li><li>Mål: under 150 KB per bilde, de fleste under 60 KB</li></ul></div>'
 '<div><h3><i style="background:#E0B000"></i>Fart</h3><ul><li>LCP 2,5 sekunder eller raskere</li><li>INP 200 ms eller raskere</li><li>CLS 0,1 eller lavere</li><li>Målt hos ekte brukere, minst 75 % av besøkene</li><li>Skrift hostes selv (Inter, variabel, woff2). Ingen Google-fonter</li><li>Ingen tredjepartskode før samtykke</li><li>Forsiden under 1 MB totalt. Nå: ca. 0,6 MB</li></ul></div></div>'
 '<div class="bx2" style="margin-top:40px;max-width:900px"><small>X-en i design, slik vi bruker den</small><p class="rg" style="margin-top:6px">Statisk kun i hero og mørke flater, og i personlig handling i artikler. På kort vises X-en bare når musen holdes over. Aldri bak tekst som skal leses, og aldri mer enn én synlig per skjermbilde.</p></div>'
 '<p class="note">Terskelverdiene for fart er Googles «gode» grenser for Core Web Vitals (web.dev). Bildetall er våre egne mål.</p></div></div>'))

S.append(pg(18, 'mt', '<div class="wrap">' + head('Typografi og lesbarhet', 'Skrift velges etter kilder, ikke etter magefølelse.', 'Verdiene under gjelder alle sider. Før vi jobber videre på en side leser vi denne manualen. Endres en regel, endres manualen først.') + AVTALT +
 '<div class="avt" style="margin-top:44px"><div><h3><i style="background:#356A89"></i>Størrelser</h3><ul><li>Brødtekst i kort og bokser: 16 px, linjehøyde 25 px</li><li>Artikler: 18 px, linjehøyde 29 til 30 px</li><li>Ingress: 19 px, linjehøyde 30 px</li><li>Mobil: brødtekst 16 px, ingress 17 px</li><li>Overskrift i seksjon: 42/48 px, på mobil 32/38 px</li><li>Overskrift i rad: 32/38 px, på mobil 26/32 px</li></ul></div>'
 '<div><h3><i style="background:#7EA257"></i>Lesbarhet</h3><ul><li>Linjehøyde 1,5 til 1,6 ganger skriftstørrelsen</li><li>Minst 16 til 18 px mellom avsnitt</li><li>50 til 75 tegn per linje, aldri over 80</li><li>Vekt 400 i løpende tekst, 500 til 600 i overskrifter</li><li>Tekstbokser får aldri fast høyde</li></ul></div>'
 '<div><h3><i style="background:#E0B000"></i>Farge og kontrast</h3><ul><li>Brødtekst #33383B på hvitt: 11,9 til 1</li><li>Småtekst #5B666C på hvitt: 5,9 til 1</li><li>Hvit tekst på grønn knapp #547B35: 4,9 til 1</li><li>Kravet er 4,5 til 1 (WCAG AA)</li></ul></div></div>'
 '<div class="avt" style="margin-top:28px"><div><h3><i style="background:#356A89"></i>Komponenter</h3><ul><li>Portrettvegg (Karriere): seks portretter i tre kolonner med lett forskyvning, signaturhjørne 4px 20px 4px 20px, ingen skygge. Kun ekte fagekspertbilder, aldri stockfoto.</li><li>Manifest-setning: én stor setning (56 px, vekt 500) fra egen tekst, på hvit flate, med god luft. Maks én per side.</li><li>Bilde og diagram overlapper aldri</li><li>Én overskrift per blokk, påstanden står som ingress</li><li>Maks to grafikker per side, én artikkelboks per blokk</li><li>Infografikk: ett budskap per grafikk, som kan sies i én setning. Det er avtalt 14. november 2026 at standarden gjelder alle diagrammer</li><li>Infografikk: fjern det som ikke viser innhold (rutenett, skygger, bakgrunner). Navn står direkte ved dataene, ikke i tegnforklaring</li><li>Infografikk: tekst minst 16 px og kontrast minst 4,5:1. Flater og linjer som bærer innhold har kontrast minst 3:1 mot bakgrunnen. Lys grønn #B7CFA0 (1,7:1) er erstattet av #6F9A4B (3,3:1)</li><li>Infografikk: farge er aldri eneste bærer av mening. Fremhevet data er mørk grønn, resten midtgrønn eller blå. Illustrasjoner uten tall merkes «ikke måledata»</li><li>Infografikk: kilde og årstall står ved alle tall. Standarden bygger på Tufte (data-ink), Datawrapper og Flourish (direkte merking) og WCAG 1.4.11. Åpent: tekst i SVG blir for liten på mobil, og må bygges om som responsiv HTML</li><li>Artikkelbilde helt ut i kanten, alltid 16:9</li><li>Ingen hårlinje etter kontaktboksen</li><li>Kontakt: «Snakk med Tom», ikke knapp i hver blokk</li></ul></div>'
 '<div><h3><i style="background:#7EA257"></i>Bilder</h3><ul><li>Bildets bredde i piksler minst lik visningsbredden, helst det dobbelte</li><li>Portretter lagres i full størrelse, ikke nedskalert til 360 px</li><li>Bildetekst skal si noe, ellers ingen</li><li>Målt når siden bygges</li></ul></div>'
 '<div><h3><i style="background:#E0B000"></i>Arbeidsrutine</h3><ul><li>Les manualen og styringsdokumentet først</li><li>Endre regelen før siden</li><li>Ingen side får egne verdier</li><li>Sjekk på desktop og mobil før utlegging</li></ul></div></div>'
 '<p class="note">Kilder: W3C WCAG 1.4.12 og teknikk C21, Baymard (linjelengde), Butterick (Practical Typography), Smashing Magazine (16 px). Kontrastverdiene er regnet ut etter WCAGs formel. Se Styringsdokumentet, kapittel 19.</p></div>'))

S.append(pg(19, '', '<div class="wrap">' + head('Status', 'Hva er avtalt, og hva gjenstår?', 'Så vi alltid vet hva som står fast, og hva som fortsatt er et forslag.') +
 '<div class="avt"><div><h3><i style="background:#356A89"></i>Avtalt</h3><ul><li>Logoens to farger, blå #356A89 og grønn #7EA257</li><li>Fortellingen om X-en, de to prikkene og de to fargene</li><li>Inter som skrift</li><li>Knappesystemet: grønn hovedknapp med hvit tekst, linjeknapp og tekstlenke</li><li>Hjørneformene og hover-mønsteret</li><li>Hvit bakgrunn, myke skygger bare på utvalgte paneler</li><li>Meny og søk. Nyhetsbrev som egen modul</li><li>Kunnskapssenter, artikkel og fagartikkel som eksempelsider</li></ul></div>'
 '<div><h3><i style="background:#E0B000"></i>Forslag, til godkjenning</h3><ul><li>Frirom rundt logoen og minste størrelse</li><li>Fordelingen av farger</li><li>Arial som reserveskrift</li><li>Strategi og innholdsspor for LinkedIn og Instagram</li><li>Oppsett for annonser, nyhetsbrev og webinarer</li><li>Alle tekster i eksemplene</li><li>Artikkelbokser, filter og kort i kunnskapssenteret</li><li>Regler for mobil, bilder og fart</li></ul></div>'
 '<div><h3><i style="background:#7EA257"></i>Åpent</h3><ul><li>Inter skal også brukes på Fagekspertene og de andre sidene</li><li>Samtykke fra kunder til logoer, sitater og bilder</li><li>E-posttjeneste til nyhetsbrevet</li><li>Opprette Instagram-konto og avklare LinkedIn-sidens innhold</li><li>Foto av fagekspertene</li><li>Webinarplattform og plan</li></ul></div></div>'
 '<p class="note">Denne manualen oppdateres underveis. Siste utkast er alltid det som ligger på denne adressen.</p></div><div class="foot"><div class="wrap"><img src="img/logo-xl-hvit.png" alt="Excellerate"><div>Designmanual · utkast 14. november 2026</div></div></div>'))

BAR = ('<div class="bar"><div class="wrap"><a href="#s0"><img src="img/logo-xl.png" alt="Excellerate"></a><div class="nv"><span class="cnt" id="cnt">1 / 18</span>'
       '<button class="bb" id="pv" aria-label="Forrige"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 5l-7 7 7 7"/></svg></button>'
       '<button class="bb" id="nx" aria-label="Neste"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 5l7 7-7 7"/></svg></button>'
       '<button class="bb mn" id="mn">Innhold</button></div></div><div class="prog" id="prog"></div></div>'
       '<nav class="idx" id="idx" aria-label="Innhold">' + ''.join('<a href="#s%d"><span>%d</span>%s</a>' % (i, i + 1, t) for i, t in enumerate(CHAP)) + '</nav>')
JS = r'''
(function(){
var secs=[].slice.call(document.querySelectorAll('[id^=s]')).filter(function(e){return /^s\d+$/.test(e.id)});var cur=0;
function fitAll(){[].forEach.call(document.querySelectorAll('.fit'),function(f){var w=+f.dataset.w,m=f.firstChild,s=f.clientWidth/w;m.style.transform='scale('+s+')';var h=f.dataset.h==='auto'?m.offsetHeight:+f.dataset.h;f.style.height=(h*s)+'px'})}
window.addEventListener('resize',fitAll);window.addEventListener('load',fitAll);fitAll();if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fitAll);
function upd(){var y=window.scrollY+160,i=0;secs.forEach(function(s,k){if(s.offsetTop<=y)i=k});cur=i;document.getElementById('cnt').textContent=(i+1)+' / '+secs.length;document.getElementById('prog').style.width=((i)/(secs.length-1)*100)+'%'}
window.addEventListener('scroll',upd,{passive:true});upd();
function go(i){i=Math.max(0,Math.min(secs.length-1,i));secs[i].scrollIntoView({behavior:'smooth',block:'start'})}
document.getElementById('nx').onclick=function(){go(cur+1)};document.getElementById('pv').onclick=function(){go(cur-1)};
document.getElementById('mn').onclick=function(){document.body.classList.toggle('io')};
[].forEach.call(document.querySelectorAll('#idx a'),function(a){a.onclick=function(){document.body.classList.remove('io')}});
document.addEventListener('keydown',function(e){if(/INPUT|TEXTAREA/.test(document.activeElement.tagName))return;if(e.key==='ArrowRight'||e.key==='PageDown'){e.preventDefault();go(cur+1)}else if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();go(cur-1)}else if(e.key==='Home'){go(0)}else if(e.key==='End'){go(secs.length-1)}else if(e.key==='Escape'){document.body.classList.remove('io')}});
})();
'''
HTML = ('<!DOCTYPE html><html lang="nb"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Designmanual | Excellerate</title><meta name="description" content="Designmanual for nye excellerate.no: symbolikk, farger, skrift, komponenter, artikkelbokser, bilder og fartskrav."><meta name="robots" content="noindex,nofollow">'
        '<link rel="preload" href="fonts/inter-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin><style>@font-face{font-family:Inter;font-weight:100 900;font-display:swap;src:url(fonts/inter-latin-wght-normal.woff2) format(woff2)}</style>'
        '<style>' + CSS + '</style></head><body>' + BAR + '<main>' + ''.join(S) + '</main><script>' + JS + '</script></body></html>')
import re as _re
def _ext(h):
    def f(m):
        t=m.group(0)
        if 'target=' in t: return t
        return t[:-1]+' target="_blank" rel="noopener noreferrer">'
    return _re.sub(r'<a [^>]*href="https?://[^"]*"[^>]*>',f,h)
open(SITE + 'designmanual.html', 'w').write(_ext(HTML))
print(len(HTML))
