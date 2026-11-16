# Om oss. Tekst og tall er hentet fra excellerate.no/om-oss, /gap-vision og /kontakt 14.11.2026. Ingen tall er lagt til.
# 1988 er hentet fra selskapsopplysninger i grunnlagsnotatet og må bekreftes av Per Kjetil.
def _kpi(v,l): return '<div class="omk"><b>%s</b><span>%s</span></div>'%(_E5(v),_E5(l))
_ptall=('<section class="omt"><div class="wrap"><div class="omkg">'+_kpi("5 000","bedrifter utviklet")+_kpi("300 000","ledere og medarbeidere utviklet")+_kpi("600+","utviklingsprogrammer")+_kpi("17","fageksperter")+'</div>'
        '<p class="ksrc" style="margin-top:28px;border:0;padding:0">Kilde: excellerate.no/gap-vision og /vare-konsulenter, 14. november 2026. Tallene må bekreftes av Excellerate før lansering.</p></div></section>')
def _dc(h,t,n): return '<div class="omd"><span class="omn">%s</span><h3>%s</h3><p>%s</p></div>'%(n,_E5(h),_E5(t))
_gjor=('<section class="wrap omsec" id="gjor"><div class="omh"><h2>Det vi gjør</h2><p class="omi">Kundene kommer til oss når de vil selge mer, lede bedre, styrke arbeidskulturen eller lykkes med en endring. Vi tar ned kompleksiteten og bygger mestring hos ledere og medarbeidere.</p></div>'
  '<div class="omdg">'
  +_dc("Innsikt og fakta","Vi viser hvor verdien faktisk skapes, i kundeporteføljen, i salgsarbeidet og i lederatferden.","1")
  +_dc("Rådgivning og metodeverk","Innen salg og salgsutvikling, strategi og ledelse. Vi omsetter innsikten til tydelige valg og prioriteringer.","2")
  +_dc("Kompetanseheving og implementering","Vi sikrer rett adferd og høy gjennomføringsevne, så resultatene varer, ikke bare intensjonene.","3")
  +'</div></section>')
_st=lambda y,h,t:'<li><b>%s</b><div><h3>%s</h3><p>%s</p></div></li>'%(_E5(y),_E5(h),_E5(t))
_hist=('<section class="omhist" id="historie"><div class="wrap omhg"><div><h2>Snart fire tiår med å utvikle ledere og selgere</h2>'
  '<p class="omi">Excellerate het tidligere Euro Business School. Navnet sier hva vi vil, å gjøre kundene fremragende, og å skape fart og retning, <i>accelerate</i>.</p>'
  '<ol class="omtl">'+_st("1988","Startet som Euro Business School","Selskapet het Euro Business School.")+_st("Siden","Ledere og selgere over hele Norden","Utviklingsprogrammer med metodeverk som er prøvd i praksis.")+_st("I dag","Innsikt og AI i tillegg til trening","GAP Vision kobler kundeinnsikt til adferden i frontlinjen.")+'</ol>'
  '<figure class="omq"><blockquote><p>«Vi har lært av de beste. Vi har lært opp de beste.»</p></blockquote></figure></div>'
  '<div class="omimg"><img src="%s" alt="Leder som står foran en gruppe kolleger i et møte" loading="lazy">'+_xw("omx")+'</div></div></section>')%U("kxa08")
_vl=lambda h,t:'<div class="omv"><h3>%s</h3><p>%s</p></div>'%(_E5(h),_E5(t))
_verdi=('<section class="wrap omsec"><div class="omh"><h2>Verdien vi skaper</h2></div><div class="omvg">'
  +_vl("Skarpere valg","Kommersielle valg basert på fakta, ikke synsing.")+_vl("Mestring som varer","Selgere og ledere som mestrer oppgavene bedre, og holder retningen over tid.")
  +_vl("Endring som leverer","Vi følger med hele veien, fra beslutning til gjennomføring.")+_vl("Kultur som lønner seg","Motivasjon, mestring og målbar avkastning på investeringene.")+'</div></section>')
_tl=[("ark",0),("boligpartner",0),("thon",0)]
_res=('<section class="rtop"><div class="wrap"><p class="rtt">Resultater hos kunder</p><div class="rtg">'+"".join('<a href="Referanse-%s.dc.html"><b>%s</b><span>%s</span><i>%s</i></a>'%(s,_E5(_BYS[s]["kpi"][k]["v"]),_E5(_BYS[s]["kpi"][k]["l"]),_E5(_BYS[s]["nm"])) for s,k in _tl)+'</div>'
  '<p style="margin-top:28px"><a class="xl-lenke" href="Referanser.dc.html">Se alle referansene<span class="pil"></span></a></p></div></section>')
_ck='<svg aria-hidden="true" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="#9CC06F" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
_gap=('<section class="omgap" id="gapvision"><div class="wrap omgg"><div class="omgi"><img src="%s" alt="To kolleger ser på et nettbrett sammen" loading="lazy"></div><div>'
  '<span class="omkick">GAP Vision</span><h2>Kundeinnsikt som gir utvikling og vekst</h2>'
  '<p class="omi">Plattformen kobler kundeinnsikt til adferden i frontlinjen. Den peker på hvilke ferdigheter og kundeopplevelser som driver salg, lojalitet og marginer.</p>'
  '<ul class="omcl"><li>%s Bygget på over 600 utviklingsprogrammer i mer enn 50 bransjer</li><li>%s De beste medarbeiderne deler tips som blir beste praksis for resten</li><li>%s Kobles mot CRM og ERP, uten nye siloer</li></ul>'
  '<div class="kbs"><a class="kn g" href="#skjema" data-emne="gap">Be om en demo</a><a class="kn l" href="GAP-Vision.dc.html">Les mer om GAP Vision</a></div></div></div></section>')%(U("kxa16"),_ck,_ck,_ck)
_ledere=[EX[0],EX[1],EX[2],TOM]
_lt={"Per Kjetil Parr":"Har bygget miljøet siden starten.","Per Christian Svae":"Leder innsikt og teknologi.","Anne Katrine Brånen":"Knutepunktet mellom kunder, deltakere og konsulenter.","Tom Hope":"Leder salg og kundedialog."}
def _lc(e):
    h=FL(e)
    return '<a class="omp" href="%s"><img src="%s" alt="" loading="lazy"><b>%s</b><span>%s</span></a>'%(h,U(e[3]),_E5(e[0]),_E5(e[1]))
_fx=[e for e in EX if e[5]=="E"]
_folk=('<section class="wrap omsec" id="folk"><div class="omh"><h2>Menneskene du møter</h2><p class="omi">Excellerate er et fagmiljø av 17 fageksperter. De har drevet salg og ledelse selv, og jobber under samme merke og med samme metodeverk.</p></div>'
  '<div class="ompg">'+"".join(_lc(e) for e in _ledere)+'</div>'
  '<div class="omfx">'+"".join('<a href="%s" title="%s"><img src="%s" alt="%s" loading="lazy"></a>'%(FL(e),_E5(e[0]),U(e[3]),_E5(e[0])) for e in _fx)+'</div>'
  '<p style="margin-top:28px"><a class="xl-lenke" href="Fagekspertene.dc.html">Se alle fagekspertene<span class="pil"></span></a></p></section>')
_vt=lambda a,b:'<div class="omtv"><b>%s</b><span>%s</span></div>'%(a,b)
_verk=('<section class="wrap omsec" id="verktoy" style="padding-top:72px"><div class="omh"><h2>Verktøyene vi bruker</h2><p class="omi">Vi velger verktøy som gir innsikt og lærer folk noe, og vi kombinerer dem med egen erfaring.</p></div><div class="omtg">'
  +_vt("GAP Vision","Kundeinnsikt som kobles til adferden i frontlinjen.")+_vt("iSuite","Samler prioritering, kontekst og handling for selgeren på ett sted.")+_vt("Maze","Hverdagstrening for fremtidens retailbedrifter.")+_vt("Culture Intelligence","Data og analyse som hjelper bedrifter å ta gode valg om kultur.")+'</div></section>')
_kk2="".join(_kk(p) for p in _KP)
_opt=lambda l:"".join('<option value="%s">%s</option>'%(v,t) for v,t in l)
_adr='<dl class="omadr"><div><dt>Besøksadresse</dt><dd>Stortorvet 7, 0155 Oslo</dd></div><div><dt>Telefon</dt><dd><a href="tel:+4722490000">+47 22 49 00 00</a></dd></div><div><dt>E-post</dt><dd><a href="mailto:post@excellerate.no">post@excellerate.no</a></dd></div></dl>'
_skjema=('<aside class="kfo omf" id="skjema"><h2>Send oss en melding</h2><p class="sub">Vi svarer deg på e-post. Du trenger ikke oppgi telefon.</p>'
  '<form><label>Hvem vil du snakke med?<select name="hvem"><option value="">Vet ikke ennå</option><option value="tom">Tom Hope</option><option value="per-kjetil">Per Kjetil Parr</option></select></label>'
  '<label>Hva gjelder det?<select name="emne"><option value="">Velg tema</option><option value="salg">Salgsutvikling</option><option value="ledelse">Lederutvikling</option><option value="kultur">Kulturutvikling</option><option value="ki">KI, adopsjon og sikkerhet</option><option value="gap">GAP Vision</option><option value="annet">Annet</option></select></label>'
  '<div class="two"><label>Navn<input required autocomplete="name"></label><label>Virksomhet<input autocomplete="organization"></label></div>'
  '<label>E-post<input type="email" required autocomplete="email"></label><label>Melding<textarea rows="4" placeholder="Hva vil dere oppnå?"></textarea></label>'
  '<label class="ck"><input type="checkbox" required><span>Jeg godtar at Excellerate lagrer opplysningene mine for å svare meg. <a href="#">Personvern</a></span></label>'
  '<button class="kn g" type="submit">Send melding</button></form>'
  '<div class="tk"><span class="ktag arr">Takk</span><h2>Meldingen er sendt</h2><p class="sub">Du hører fra oss på e-post.</p><a class="kn o" href="Kunnskap.dc.html">Les artikler i mellomtiden</a></div></aside>')
_kont=('<section class="omkont" id="kontakt"><div class="wrap omkg2"><div><h2>Snakk med oss</h2><p class="omi">Fortell oss hva dere vil løse. Vi tar en uforpliktende samtale, og finner riktig fagekspert hvis det er behov for det.</p>'
  '<div class="omkp">'+_kk2.replace("Kontakt.dc.html?hvem=tom#skjema","#skjema").replace("Kontakt.dc.html?hvem=per-kjetil#skjema","#skjema")+'</div>'+_adr+'</div>'+_skjema+'</div></section>')
_kar=('<section class="wrap omsec" id="karriere"><div class="omkar">'+_xw("omx2")+'<div><h2>Vil du bli en del av fagmiljøet?</h2><p>Vi er genuint opptatt av å skape resultater for kundene. Gjennom faglig og kollegial støtte tør vi mer, vil mer og skaper mer, sammen.</p></div>'
  '<div class="kbs"><a class="kn g" href="Karriere.dc.html">Se karrieremulighetene</a><a class="kn l" href="mailto:pkp@excellerate.no">Kontakt Per Kjetil</a></div></div>'
  '<p class="ksrc">Kilde: excellerate.no/om-oss, gap-vision og kontakt, 14. november 2026. Tekstene er forslag og må godkjennes av Excellerate før lansering.</p></section>')
_hero=('<section class="dyp hero kort rov" style="color:#fff"><div class="wrap kw">'+_xw("hx")+'<h1>Vi hjelper deg å finne, vinne og beholde de rette kundene</h1><p class="hl">Og å bygge organisasjonen som klarer det, dag etter dag.</p>'
  '<div class="kbs" style="margin-top:32px;display:flex;gap:12px;flex-wrap:wrap"><a class="kn g" href="#kontakt">Snakk med oss</a><a class="kn l" href="#folk">Møt menneskene</a></div></div></section>')
_write("Om-oss.dc.html","Om Excellerate, fagmiljøet bak salgs- og lederutvikling | Excellerate","<style>#samtale{display:none}</style>"+_hero+_ptall+_gjor+_hist+_verdi+_res+_gap+_folk+_verk+_kont+_kar,3200)

exec(open("pages2.py").read())
