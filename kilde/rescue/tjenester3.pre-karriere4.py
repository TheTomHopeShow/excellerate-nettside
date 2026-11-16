# Produktsider for tjenester: komponenter + Oversikt + Salg. Brødtekst er fra dagens excellerate.no (14.11.2026), delt i setninger uten endringer.
import re as _re3, json as _j3
_A16=_j3.load(open("ex16.json"))
_sn=lambda t:_re3.split(r'(?<=[.?!]) (?=[A-ZÆØÅ«])',t.strip())
def _chips(l): return '<ul class="tpch">'+"".join("<li>%s</li>"%_E5(x) for x in l)+'</ul>' if l else ''
_gvl=lambda t:'<section class="wrap" style="padding-top:24px"><p><a class="xl-lenke" href="GAP-Vision.dc.html">%s<span class="pil"></span></a></p></section>'%t
_srcn=lambda t:'<section class="wrap" style="padding-bottom:96px"><p class="ksrc">%s</p></section>'%t
_AR_ICON='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
_SI={"find":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l5 5"/></svg>',
 "win":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M8 12.5l3 3 5-6"/></svg>',
 "keep":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-4.6-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 11c0 5.4-7 10-7 10z"/></svg>',
 "map":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19V9M10 19V5M16 19v-7M22 19H2"/></svg>',
 "people":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.2"/><path d="M3 20c.8-3.6 3.2-5.4 6-5.4s5.2 1.8 6 5.4"/><circle cx="17.5" cy="9" r="2.4"/><path d="M17 14.6c2.2.2 3.6 1.8 4.2 4.6"/></svg>',
 "chart":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20h16M7 16v-5M12 16V6M17 16v-8"/></svg>',
 "doc":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4M10 12h5M10 16h5"/></svg>',
 "shield":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v5c0 5-3 8.5-7 10-4-1.5-7-5-7-10V6z"/><path d="M9 12l2.2 2.2L15.5 10"/></svg>'}
def _art(sl):
    a=[x for x in _A16 if x["slug"]==sl][0]; return a,U("kxa%02d"%int(a["n"]))
def _artc(sl,tag="Fagartikkel"):
    a,im=_art(sl)
    return '<a class="svk" href="Kunnskap-%s.dc.html"><span class="svki"><img src="%s" alt="" loading="lazy"></span><div><span class="svkt">%s</span><h3>%s</h3><p>%s</p></div></a>'%(_aslug5(sl),im,tag,_E5(a["title"]),_E5(a["ing"]))
def _arts(sls,h="Les mer",intro=""):
    return '<section class="wrap svsec" id="artikler"><span class="omkick2">Kunnskap</span><h2>%s</h2>%s<div class="svks">%s</div></section>'%(_E5(h),('<p class="omi">%s</p>'%_E5(intro) if intro else ""),"".join(_artc(s) for s in sls))
def _svhero(kick,h1,lead,imgid,emne,sek="Se resultater",sekh="#resultater"):
    return ('<section class="dyp hero kort svh" style="color:#fff"><div class="wrap kw">'+_xw("hx")+'<div class="svhg"><div class="svht"><span class="svkick">%s</span><h1>%s</h1><p class="hl">%s</p><div class="kbs"><a class="kn g" href="Kontakt.dc.html?emne=%s#skjema">Snakk med oss</a><a class="kn l" href="%s">%s</a></div></div>'
     '<div class="svhi"><img src="%s" alt=""></div></div></div></section>')%(_E5(kick),_E5(h1),_E5(lead),emne,sekh,_E5(sek),U(imgid))
def _row(i,kick,h,utf,gjor,panel,emne,arts="",flip=False,lab="Slik hjelper vi",btn="Snakk med oss om dette"):
    return ('<section class="wrap svr%s" id="%s"><div class="svrp">%s</div><div class="svrt"><span class="omkick2">%s</span><h2>%s</h2><p class="svu">%s</p>'
     '<div class="svg"><b>%s</b>%s</div>%s</div></section>')%(" rv" if flip else "",i,panel,_E5(kick),_E5(h),_E5(utf),_E5(lab),"".join("<p>%s</p>"%_E5(x) for x in gjor),arts)
def _img(id_,alt=""): return '<img src="%s" alt="%s" loading="lazy">'%(U(id_),_E5(alt))
def _pp(imgid,gfx,alt=""): return '<div class="svpp"><img src="%s" alt="%s" loading="lazy">%s</div>'%(U(imgid),_E5(alt),gfx)
def _gfx(inner,cap=""): return '<div class="gfx">%s%s</div>'%(inner,('<p class="svcap">%s</p>'%_E5(cap) if cap else ""))
def _pv(la,ia,lb,ib,cap=""):
    return _gfx('<div class="svpv"><div class="a"><h4>%s</h4><ul>%s</ul></div><div class="m">%s</div><div class="b"><h4>%s</h4><ul>%s</ul></div></div>'%(_E5(la),"".join("<li>%s</li>"%_E5(x) for x in ia),_AR_ICON,_E5(lb),"".join("<li>%s</li>"%_E5(x) for x in ib)),cap)
def _sec(i,kick,h,inner="",intro="",cls="wrap svsec"):
    return '<section class="%s" id="%s"><span class="omkick2">%s</span><h2>%s</h2>%s%s</section>'%(cls,i,_E5(kick),_E5(h),('<p class="omi">%s</p>'%_E5(intro) if intro else ""),inner)
_T2=lambda t:" ".join(_sn(t)[:2])
def _jc(ic,h,p,chips,emne,btn,cls=""):
    return '<div class="svjc %s"><span class="svic">%s</span><h3>%s</h3><p>%s</p>%s</div>'%(cls,_SI[ic],_E5(h),_E5(p),_chips(chips))
def _journey(cards,f4=False):
    a='<span class="sva">%s</span>'%_AR_ICON
    return '<div class="svj%s">%s</div>'%(" f4" if f4 else "",a.join(cards))
def _people(tag,h="Fagekspertene dere møter",n=4,intro="",extra=(),tom=False):
    es=[e for e in EX if tag in e[4].split()][:n]+list(extra)
    tc=('<a class="svf" href="Kontakt.dc.html?emne=%s#skjema"><img src="%s" alt="Tom Hope" loading="lazy"><b>Tom Hope</b><span>%s</span></a>'%(tag,U(TOM[3]),_E5(TOM[1]))) if tom else ""
    cards=tc+"".join('<a class="svf" href="%s"><img src="%s" alt="%s" loading="lazy"><b>%s</b><span>%s</span></a>'%(FL(e),U(e[3]),_E5(e[0]),_E5(e[0]),_E5(e[1])) for e in es)
    return '<section class="wrap svsec" id="fageksperter"><span class="omkick2">Fagekspertene</span><h2>%s</h2>%s<div class="svfs">%s</div><p style="margin-top:26px"><a class="xl-lenke" href="Fagekspertene.dc.html">Se alle fagekspertene<span class="pil"></span></a></p></section>'%(_E5(h),('<p class="omi">%s</p>'%_E5(intro) if intro else ""),cards)
def _refs3(slugs,h="Resultater hos kunder"):
    return '<section class="wrap svsec" id="resultater"><span class="omkick2">Referanser</span><h2>%s</h2><div class="svrf">%s</div><p style="margin-top:26px"><a class="xl-lenke" href="Referanser.dc.html">Se alle referansene<span class="pil"></span></a></p></section>'%(_E5(h),"".join(_card(_BYS[s]) for s in slugs))
def _tpg(fn,title,body,note):
    _write(fn,title,body+_srcn(note),3000)
_cipher=lambda *a:a

# ================= SALG =================
_sk="Kilde: dagens excellerate.no/tjenester/salgsutvikling, hentet 14.11.2026. Brødteksten er delt i «utfordringen» og «slik hjelper vi», men ikke endret, bortsett fra én rettet skrivefeil. Bildene er fra Excellerates bildebibliotek. Diagrammene er illustrasjoner av prinsippene i teksten og viser ingen tall. Forslag, ikke avtalt: artikkelkoblinger, fagekspertene som vises, referansevalget og blokken om kunstig intelligens i salg (hentet fra ingressen i artikkelen)."
_P=lambda t,a,b:(" ".join(_sn(t)[:a]),_sn(t)[a:b])
_t_pris="Når kundene ikke ser forskjell på deg og konkurrentene, blir pris det eneste de sammenligner. Da presses marginene, og salget blir et spørsmål om rabatter. Rådgivende Verdisalg er vårt innsiktsbaserte rammeverk for verdiskapende salg og rådgivning. Det bygger på anerkjent forskning og beste praksis, og vi kan dokumentere effekten. Selgerne lærer å forstå kundens virksomhet, sette ord på verdien de skaper og flytte samtalen fra pris til verdi. Slik styrker dere den kommersielle kulturen, øker både topp- og bunnlinjen og går fra å være en vanlig leverandør til å bli en partner som skaper verdi for kunden."
_t_kunder="Mange selskaper bruker like mye tid på alle kunder, uansett hvor mye kundene er verdt. Da får de mest lønnsomme kundene for lite oppmerksomhet, mens salgsressursene spres for tynt. Vi hjelper dere med å dele kundemassen inn i segmenter og finne kundene som gir størst verdi over tid, og som får dere til å utvikle dere gjennom krav og forventninger. Deretter lager vi betjeningskonsepter for hvert segment, trener teamene i hvordan de skal møte de ulike kundegruppene, og gjør selskapet til en mer attraktiv og viktig samarbeidspartner."
_t_forv="Kundene stiller høyere krav enn tidligere, og det de legger vekt på varierer mye. Uten en tydelig betjeningsmodell blir oppfølgingen tilfeldig, og lojaliteten svekkes uten at noen merker det før kunden er borte. Vi hjelper dere å finne ut hva som gjør at kundene velger dere, og hva som får dem til å bli. Sammen legger vi opp gjennomtenkte betjeningsmodeller som er forankret i organisasjonen, slik at dere selv styrer hvilke kunder som får de beste ressursene og den tetteste oppfølgingen. Resultatet er mer lojale kunder og mindre kundeavgang."
_seg=_gfx('<div class="xsg"><div><span>Segment 1</span><div class="tr"><i style="width:100%"></i></div></div><div><span>Segment 2</span><div class="tr"><i style="width:64%"></i></div></div><div><span>Segment 3</span><div class="tr"><i style="width:34%"></i></div></div></div><p class="svsn">Kundene som gir størst verdi over tid får de beste ressursene og den tetteste oppfølgingen.</p>',"Illustrasjon av prinsippet. Bredden viser verdi over tid, ikke tall.")
_sa=_P(_t_pris,2,6); _sb=_P(_t_kunder,2,4); _sc=_P(_t_forv,2,5)
_AI_ING="Excellerate og Mentr.ai tar salgsutvikling inn i en ny æra der kunstig intelligens gjør det mulig å levere bedre kundemøter, raskere salgsprosesser og høyere lønnsomhet."
_chip=lambda *x:_chips(list(x))
_fjv=_journey([
 _jc("find","Finne rett kunde",_T2("Verdien av kundemassen i selskapet starter med hvilke kunder dere henvender dere til. De beste kundene er de som gir dere størst verdi over tid og som også bidrar til å utvikle selskapet gjennom sine ønsker og krav. Vi bistår våre kunder med å segmentere ulike kundegrupper slik at det er tydelig for alle hvilke kunder dere ønsker dere."),["Kundesegmentering","Verdiproposisjon"],"salg","Jeg vil vite mer om å finne kunder"),
 _jc("win","Vinne rett kunde",_T2("Ny kunnskap og økt tilgang til informasjon gjør at kundene forventer mer av dere enn tidligere. Forretningsfilosofien Rådgivende Verdisalg er utviklet for å møte disse kundekravene. Den baserer seg på anerkjent forskning og beste praksis. Kunder som bygger sitt salgsarbeid på Rådgivende Verdisalg opplever vekst både i omsetning og økt lønnsomhet i hvert enkelt kundeforhold."),["Rådgivende verdisalg","Kundeinnsikt","Ledelse","Beste praksis","Analyse"],"salg","Jeg vil vite mer om å vinne kunder","g"),
 _jc("keep","Beholde rett kunde",_T2("Du brukte mye ressurser på å finne og vinne kunder, nå er det lurt å sikre at de forblir kunder. Dine kunder er forskjellige, de vektlegger ulike ting og de ønsker ulik betjening. Våre metoder for å sikre kundelojalitet og redusert kundeavgang, er bygget på årelang erfaring fra utallige kundeprosjekter og har bevist sin lønnsomhet."),["Bedriftskultur","Key account management","Kundesegmentering","Medarbeiderundersøkelse"],"salg","Jeg vil vite mer om å beholde kunder","d")])
def _rl(sl):
    a,im=_art(sl); return '<a class="svrc" href="Kunnskap-%s.dc.html"><span class="svrci"><img src="%s" alt="" loading="lazy"></span><span class="svrct"><small>Artikkel</small><b>%s</b><em>%s</em></span></a>'%(_aslug5(sl),im,_E5(a["title"]),_E5(a["ing"]))
def _cta3(h,tx,emne,k="Snakk med Tom"):
    return ('<section class="wrap kcs" style="padding-top:8px;padding-bottom:8px"><aside class="kkb" aria-label="Kontakt oss"><div class="kkf"><img src="%s" alt="Tom Hope"><img src="%s" alt="Per Kjetil Parr"></div>'
     '<div class="kkt"><h2>%s</h2><p>%s</p></div><div class="kkx"><a class="kn g" href="Kontakt.dc.html?emne=%s#skjema">%s</a><a class="kn o" href="tel:+4741088885">Ring 410 88 885</a></div></aside></section>')%(U(TOM[3]),U(EX[0][3]),_E5(h),_E5(tx),emne,_E5(k))
_gapbars='<svg viewBox="0 0 520 214" role="img" aria-label="Noen få selgere leverer langt over snittet, resten ligger under" style="width:100%;height:auto;display:block"><g font-family="Inter,sans-serif" font-size="21" font-weight="700"><rect x="0" y="34" width="44" height="156" rx="3" fill="#547B35"/><rect x="52" y="47" width="44" height="143" rx="3" fill="#547B35"/><rect x="104" y="122" width="44" height="68" rx="3" fill="#6F9A4B"/><rect x="156" y="129" width="44" height="61" rx="3" fill="#6F9A4B"/><rect x="208" y="132" width="44" height="58" rx="3" fill="#6F9A4B"/><rect x="260" y="136" width="44" height="54" rx="3" fill="#6F9A4B"/><rect x="312" y="139" width="44" height="51" rx="3" fill="#6F9A4B"/><rect x="364" y="142" width="44" height="48" rx="3" fill="#6F9A4B"/><rect x="416" y="144" width="44" height="46" rx="3" fill="#6F9A4B"/><rect x="468" y="148" width="44" height="42" rx="3" fill="#6F9A4B"/><line x1="0" y1="114" x2="520" y2="114" stroke="#1B3A4B" stroke-width="2" stroke-dasharray="6 5"/><text x="516" y="104" text-anchor="end" fill="#1B3A4B">Snittet</text><text x="98" y="30" fill="#547B35">Få selgere leverer langt over snittet</text><text x="0" y="208" fill="#33383B" font-weight="600">Selgerne i ett salgskorps</text></g></svg>'

# NØDLØSNING 14.11.2026 natt: byggekoden for Salg, Ledelse, Kultur, KI, Tjenester og Bransjer gikk tapt i en feilredigering.
# Ferdigbygde sider (siste gode versjon) gjenopprettes fra /home/claude/rescue. Tjenester og Bransjer kopieres som ferdig html i build_all.sh.
import shutil as _sh
for _f in ["Tjenester-Salg.dc.html","Tjenester-Ledelse.dc.html","Tjenester-Kultur.dc.html","Tjenester-KI.dc.html"]: _sh.copy("/home/claude/rescue/"+_f,_f)

# ---- GAP Vision. Tekst fra excellerate.no/gap-vision og /gap-vision/gap-vision-ai, hentet 14.11.2026. Kun stavefeil rettet.
_gt=["GAP Vision gir deg svar på hvordan dere kan finne, vinne og beholde flere kunder. Veien fra rådata til resultater er kort og treffsikker med våre kraftige AI-funksjoner. Plattformen kombinerer kundeinnsikt, beste praksis og med løpende tilførsel av tips og råd fra dine beste medarbeidere. Resultatet er en presis innsikt i hvor forbedringene ligger i salgs-, service- og leveranseprosessene. Med løpende personlig anerkjennelse og forslag til forbedringsområder fører dette til økt salg, sterkere kundelojalitet og lønnsom vekst.",
"Der tradisjonelle undersøkelser stopper ved rapporter og dashboards, kobler GAP Vision kundeinnsikt direkte til adferden i frontlinjen. AI-motoren analyserer tusenvis av kundeopplevelser og peker på hvilke ferdigheter, aktiviteter og kundeopplevelser som driver salg, lojalitet og marginer i dine verdikjeder. Innsikten omsettes til konkrete anbefalinger, personlige utviklingsplaner pr medarbeider som løpende coaching-grunnlag for hver enkelt leder.",
"GAP Vision blir smartere jo mer den brukes. Ansatte som presterer best, basert på blant annet kundenes tilbakemeldinger, får dele konkrete tips og eksempler, som evalueres, rangeres og videreforedles av AI-en og distribueres tilbake til resten av organisasjonen som beste praksis. Samtidig fanges løpende kundeopplevelser på tvers av verdikjeden, slik at dere kontinuerlig kan justere kursen og lukke prestasjonsgapene der effekten er størst.",
"GAP Vision er bygget på snart fire tiår med konsulenterfaring. Den er foret med data fra over 600 utviklingsprogrammer fra mer enn 500 000 deltakere og over 50 bransjer. Du kan måle prestasjoner på kritiske områder, identifisere gapet mellom ønsket og faktisk adferd, og koble dette til tiltakene som gir dokumenterbar effekt på topplinjen, styrker kundetilfredsheten og øker lojaliteten. Slik skaper du konkurransekraft som er vanskelig å kopiere, fordi den er bygget på egne kunder, egne prosesser og egen beste praksis.",
"GAP Vision kan i tillegg kobles mot data fra dine CRM- og ERP-løsninger som benyttes til å berike innsikten og analysene. Det gir en kraftfull innsikts- og utviklingsmotor uten nye siloer og krevende implementering, fordi innsikten visualiseres i grensesnittene dere allerede bruker, og du får et løpende beslutningsgrunnlag for bedre ledelse, skarpere kundekommunikasjon og mer presise forbedringstiltak."]
_gtt=lambda i:(_sn(_gt[i])[0]," ".join(_sn(_gt[i])[1:]))
_gsteps=_gfx('<ol class="svst"><li><b>Kunden vurderer</b><span>Kundenes opplevelse av salgs-, service- og leveranseprosessene</span></li><li><b>AI finner mønstre</b><span>Hvilke ferdigheter og aktiviteter som driver salg og lojalitet</span></li><li><b>Personlig utviklingsplan</b><span>Konkrete anbefalinger for hver medarbeider</span></li><li><b>Leder coacher</b><span>Utviklingsplanen er løpende grunnlag for coaching</span></li></ol>',"Slik går innsikten fra kunden til lederen.")
_gst_a,_gst_b=_gtt(1);_g2a,_g2b=_gtt(2);_g3a,_g3b=_gtt(3);_g4a,_g4b=_gtt(4)
_gstat=('<section class="omt"><div class="wrap"><div class="omkg">'+_kpi("Snart 40","år med beste praksis")+_kpi("600+","utviklingsprogrammer i datagrunnlaget")+_kpi("50+","bransjer")+_kpi("5 000","bedrifter utviklet")+'</div></div></section>')
_gpvAI=_pv("Slik er coachingen i dag",["«Du må bli bedre på behovsavdekking.»"],"Med GAP Vision AI",["«Her er de konkrete områdene hvor du kan forbedre kundedialogen.»","«Dette er hva de beste selgerne gjør annerledes.»"],"Eksempel fra beskrivelsen av GAP Vision AI.")
_gai=["identifisere hva som kjennetegner gode kundeopplevelser","avdekke forskjeller mellom høy- og lavpresterende selgere","finne konkrete utviklingsområder for den enkelte","gjøre kundeinnsikt tilgjengelig for salgsledere","gi et bedre grunnlag for målrettet coaching og trening","hjelpe teamet med å lære av det som allerede fungerer"]
_gaih='<div class="svar" style="grid-template-columns:repeat(3,minmax(0,1fr))">'+"".join('<div class="svjc svjm"><span class="svic">%s</span><h3>%s</h3></div>'%(_SI[i],_E5(t[0].upper()+t[1:])) for i,t in zip(["find","people","map","chart","doc","win"],_gai))+'</div>'
_gverk=[("people","Maze","Maze Feedback er den beste løsningen for hverdagstrening for fremtidens retailbedrifter."),("doc","Eloomi","Eloomi er et av verdens høyest rangerte e-læringsverktøy. Kombinert med vår erfaring gjør vi at din bedrift lykkes med digital læring og utvikling."),("find","Questback","Partnerskapet med Questback sikrer muligheten til å hente inn fakta og innsikt på vegne av våre oppdragsgivere."),("chart","Culture Intelligence","Med Culture Intelligence tilbys en bred innside av data og analyse for å hjelpe bedrifter å ta profesjonelle valg om sin kultur.")]
_gverkh='<div class="svar">'+"".join('<div class="svjc"><span class="svic">%s</span><h3>%s</h3><p>%s</p></div>'%(_SI[i],_E5(n),_E5(t)) for i,n,t in _gverk)+'</div>'
_gnote="Kilde: teksten er hentet fra dagens excellerate.no/gap-vision og /gap-vision/gap-vision-ai, 14.11.2026, delt i setninger. Rettet: «annerkjennelse», «forbedrings-områder» og et feilplassert komma. Tallene (snart 40 år, over 600 programmer, mer enn 500 000 deltakere, over 50 bransjer) er fra den siden og ikke kontrollert. Samme side oppgir også 300 000 utviklede medarbeidere og ledere i nøkkeltallene. Forslag, ikke godkjent: overskriftene på områdene og de fire trinnene i diagrammet er mine ord for det siden beskriver."
_gv=(_svhero("GAP Vision","GAP Vision","Kundeinnsikt som gir utvikling og vekst. Svar på hvordan dere finner, vinner og beholder flere kunder.","kxa16","gap","Se hvordan det virker","#intro")
 +_gstat
 +_row("intro","GAP Vision","Fra rådata til resultater",_sn(_gt[0])[0],[" ".join(_sn(_gt[0])[1:])],_gsteps,"gap","",False,"Slik virker det","Be om en demo")
 +_row("presisjon","Presis innsikt","Gir nøyaktig svar til dine ledere",_gst_a,[_gst_b],_img("kxa05","Håndtrykk mellom selger og kunde"),"gap","",True,"Slik virker det","Be om en demo")
 +_row("laerer","Smartere jo mer den brukes","En smart plattform som hjelper deg nå dine mål",_g2a,[_g2b],_img("kxa13","Et team i samtale rundt et bord"),"gap",_rl("innsikt-bak-riktig-lederfokus"),False,"Slik lærer den","Be om en demo")
 +_row("erfaring","Erfaring","Basert på 40 år med beste praksis",_g3a,[_g3b],_img("kxa14","Ledere i samtale"),"gap","",True,"Slik bygger vi","Be om en demo")
 +_row("integrasjon","Integrasjon","Ikke nok et system",_g4a,[_g4b],_img("kxa03","En selger bruker KI-verktøy i salgsarbeidet"),"gap","",False,"Slik kobles den","Be om en demo")
 +_cta3("Vil du se hvilke fordeler GAP Vision gir dere?","Ta kontakt for en demo av løsningen.","gap","Be om en demo")
 +_row("ai","GAP Vision AI","Hvorfor selger noen mer enn andre?","Finn ut hva de beste selgerne gjør annerledes, og bruk innsikten til å løfte resten av teamet.",["Hva om dere kunne identifisere hva som faktisk skiller de beste selgerne fra resten, basert på det kundene opplever, ikke bare på salgsresultatene? Med GAP Vision AI kan kundeinnsikt og AI brukes til å avdekke mønstre, styrker og utviklingsområder i salgsarbeidet. Slik får salgsledere et bedre grunnlag for å vite hva som bør trenes, hvem som trenger hva og hvor det største potensialet ligger."],_gpvAI,"gap","",True,"Fra magefølelse til konkret innsikt","Finn ut mer")
 +_sec("kan","Hva GAP Vision AI kan bidra til","Gjør de beste enda bedre, og løft resten",_gaih,"De fleste salgsledere vet hvem som presterer best. Men vet dere hvorfor? Hva gjør toppselgerne annerledes i kundedialogen, og hvilke av ferdighetene kan resten av teamet lære?")
 +_sec("potensial","Potensialet","Dere har sannsynligvis mer salgspotensial enn dere tror",'<p class="svu" style="max-width:760px">Det kan hende de beste metodene allerede finnes i deres eget salgsteam. Spørsmålet er om dere vet hva de er, og klarer å overføre dem til resten av organisasjonen. Med riktig bruk av AI kan kundedata og tilbakemeldinger bli mer enn rapporter i et system. De kan bli et konkret verktøy for å utvikle mennesker og skape bedre salgsresultater.</p>')
 +_cta3("Finn ut hva som skiller deres beste selgere fra resten","Fyll ut kontaktskjemaet, så ser vi sammen på hvordan GAP Vision AI kan gjøre kundeinnsikt til konkrete tiltak. Vi tar kontakt innen 24 timer.","gap","Be om en demo")
 +'<section class="svb" id="verktoy"><div class="wrap svsec" style="padding-bottom:88px"><span class="omkick2">Øvrige verktøy</span><h2>Verktøy vi bruker sammen med GAP Vision</h2>'+_gverkh+'</div></section>'
 +_refs3(["fortum"],"Resultater med GAP Vision")
 +_people("gap","Fagekspertene bak GAP Vision",0,extra=[EX[1],EX[0],[e for e in EX if e[0]=="Leif Ottesen"][0]]))
_tpg("GAP-Vision.dc.html","GAP Vision: kundeinnsikt som gir utvikling og vekst | Excellerate",_gv,_gnote)

# ---- Karriere (14.11.2026 natt, runde 2). Innhold fra utlysningen «Vi søker Norges beste konsulenter på salgsutvikling og lederutvikling» (excellerate.no, 29.10.2025) og bannerteksten på Om oss.
_kw_=lambda n:[e for e in EX if e[0].startswith(n)][0]
_kwall=[_kw_("Petter"),_kw_("Morten"),_kw_("Janick"),_kw_("Bård"),_kw_("Leif"),_kw_("Neda")]
_kwh=('<div class="kwl" aria-hidden="true">'+"".join('<img src="%s" alt="" loading="eager">'%U(e[3]) for e in _kwall)+'</div>')
_khero=('<section class="dyp hero kort svh" style="color:#fff"><div class="wrap kw">'+_xw("hx")+'<div class="svhg"><div class="svht"><span class="svkick">Karriere</span><h1>Bygg din praksis i et fagmiljø som løfter deg</h1>'
 '<p class="hl">Du jobber som konsulent gjennom eget selskap, med stor frihet og mesteparten av inntektene selv. Bak deg står Norges mest erfarne og etterspurte fagmiljø innen salgsutvikling og lederutvikling.</p>'
 '<div class="kbs"><a class="kn g" href="#interesse">Fortell oss om deg</a><a class="kn l" href="#modellen">Se hva du får</a></div></div>'+_kwh+'</div></div></section>')
_kstat=('<section class="omt"><div class="wrap"><div class="omkg">'+_kpi("Snart 40","år med fagmiljø")+_kpi("16","fageksperter")+_kpi("5 000","bedrifter utviklet")+_kpi("300 000","ledere og medarbeidere utviklet")+'</div></div></section>')
_kfet=('<section class="kfet"><div class="wrap"><span class="omkick2">Fagmiljøet</span><p>Du blir en del av et team som er genuint opptatt av å skape resultater for kundene.</p>'
 '<p class="kfs">Teamet består av eksperter med variert kompetanse innen ulike metoder og verktøy. Dette gir konsulentene muligheten til å utvikle seg i et miljø som verdsetter samarbeid, kreativitet og løsningsorientert tenkning.</p>'
 '<div class="kbs"><a class="kn g" href="#interesse">Fortell oss om deg</a><a class="kn l" href="#modellen">Se hva du får</a></div></div></section>')
_kdeg=_row("deg","Er det deg?","Du skaper resultater og vil mer","Vi søker enkeltpersoner med lidenskap for kundeutvikling og forretningsutvikling.",
 ["Du er problemløser og resultatorientert. Du har erfaring fra konsulentvirksomhet eller relaterte felt, og du er i leveranser i dag.","Du har et ønske om å utvikle deg i et dynamisk miljø, og du deler lidenskapen for å skape resultater for kundene. Da vil du trives hos oss."],
 _img("kxa13","Et team i samtale rundt et bord"),"annet","",False,"Dette leter vi etter","Fortell oss om deg").replace('href="Kontakt.dc.html?emne=annet#skjema"','href="#interesse"')
_kfag=[("chart","Bedriftsutvikling","Fakta og innsikt som hjelper virksomheter å finne, vinne og beholde de rette kundene, gjennom hele kundereisen.","Tjenester.dc.html","Se tjenestene"),
 ("win","Salgs-, service- og lederutvikling","Fra strategiske valg til trening og implementering, med metoder og verktøy som er prøvd i snart 40 år.","Tjenester-Salg.dc.html","Se salgsutvikling"),
 ("map","Kundesegmentering og betjeningskonsepter","Strategisk kundesegmentering og betjeningskonsepter som gjør det tydelig hvem vi skal vinne, og hvordan.","Tjenester-Ledelse.dc.html","Se lederutvikling"),
 ("people","Kultur og verdinormer","Utvikling av organisasjonskultur og verdinormer som støtter målene og lever i hverdagen.","Tjenester-Kultur.dc.html","Se kulturutvikling")]
_kar4=_sec("omrader","Fagfelt","Fire felt der du kan bidra",'<div class="kjg">'+"".join('<a class="kjc" href="%s"><span class="svic">%s</span><h3>%s</h3><p>%s</p><span class="kjl">%s<i class="pil"></i></span></a>'%(h,_SI[i],_E5(t),_E5(p),_E5(l)) for i,t,p,h,l in _kfag)+'</div>',"Teamet består av eksperter med variert kompetanse innen ulike metoder og verktøy, og du kan jobbe med varierte prosjekter, utfordringer og kunder.")
_klv=[("people","Opplæring og utviklingsprogrammer"),("find","Rådgivning"),("win","Coaching"),("keep","Kick-off-eventer"),("doc","Webinarer"),("chart","Digitale opplærings- og treningsarenaer")]
_klev=_sec("leveranser","Leveransene","Det du kommer til å levere",'<div class="klg">'+"".join('<div class="klt"><span class="svic">%s</span><b>%s</b></div>'%(_SI[i],_E5(t)) for i,t in _klv)+'</div>',"Slik jobber du med kundene dine i Excellerate.")
_kmod=('<section class="svb" id="modellen"><div class="wrap svsec" style="padding-bottom:96px"><span class="omkick2">Modellen</span><h2>En lønnsom og attraktiv modell</h2><p class="omi">Excellerate er merkevaren vi alle jobber under. Dette er Norges fremste miljø innen salgsutvikling og lederutvikling de siste 40 årene.</p><div class="kmx">'
 +"".join('<div class="svjc"><span class="svic">%s</span><h3>%s</h3><p>%s</p></div>'%(_SI[i],_E5(h),_E5(p)) for i,h,p in [
 ("keep","Stor frihet","Modellen gir hver konsulent stor frihet til å bruke alle sine ferdigheter."),
 ("people","Et faglig miljø","Likesinnede som konstruktivt utfordrer hverandre hver eneste dag."),
 ("chart","Eget selskap og mesteparten av inntektene","Du knyttes til oss gjennom en eksklusiv konsulentavtale fra eget selskap. Det er en svært lønnsom ordning, fordi du beholder mesteparten av inntektene selv.")])
 +'</div></div></section>')
_kbyg=('<section class="kbyg" id="bygget"><div class="wrap kyg"><div class="kyi"><img src="img/stortorvet7.jpg" alt="Stortorvet 7 i Oslo sentrum" loading="lazy"><img class="kys" src="/_blob/6c10bbc2090df8189f1fdb57970dafa0" alt="Resepsjonen til Excellerate" loading="lazy"></div>'
 '<div class="kyt"><span class="omkick2">Der du jobber</span><h2>Stortorvet 7, i hjertet av Oslo</h2>'
 '<p>Vi holder til i Stortorvet 7. Bygget ble kåret til Årets bygg 2023 av Byggeindustrien.</p>'
 '<p>Her møter du kolleger og kunder i lyse, åpne rom midt i byen.</p>'
 '<a class="kn o" href="Kontakt.dc.html">Besøk oss</a></div></div></section>')
_kqs=["Jeg driver eget selskap, eller er klar for å gjøre det.","Jeg leverer konsulenttjenester i dag, og har erfaring derfra.","Jeg brenner for kundeutvikling og forretningsutvikling.","Jeg liker å løse problemer, og vil måles på resultatene kundene får.","Jeg vil ha stor frihet til å bruke ferdighetene mine slik jeg selv mener er best.","Jeg trives med å utfordre og bli utfordret av faglige kolleger.","Jeg kan se meg selv i ett eller flere av de fire fagfeltene."]
_kq=('<section class="kqz" id="passer"><div class="wrap kqw"><span class="omkick2">Er dette for deg?</span><h2>Kjenner du deg igjen?</h2><p class="omi">Syv påstander om hvordan det er å jobbe sammen med oss. Det er ingen riktige svar, og ingenting blir lagret. Du får en oppsummering du kan bruke som utgangspunkt for en samtale.</p>'
 '<form class="kqf" id="kqf" onsubmit="return false">'
 +"".join('<fieldset><legend>%s</legend><div class="kqo"><label><input type="radio" name="q%d" value="2">Stemmer</label><label><input type="radio" name="q%d" value="1">Delvis</label><label><input type="radio" name="q%d" value="0">Stemmer ikke</label></div></fieldset>'%(_E5(x),i,i,i) for i,x in enumerate(_kqs))
 +'<button class="kn g" type="button" id="kqb">Se oppsummering</button></form>'
 '<div class="kqr" id="kqr" hidden><h3 id="kqh"></h3><p id="kqp"></p><ul id="kql"></ul><div class="kbs"><a class="kn g" href="#interesse" id="kqt">Ta svarene med i meldingen</a><a class="kn o" href="#interesse">Skriv uten svarene</a></div></div>'
 '<p class="kqn">Forslag til samtale, ikke en test. Spørsmålene bygger på utlysningen og er ikke en vurdering av deg.</p></div>'
 '<script>(function(){var Q=%s,b=document.getElementById("kqb");if(!b)return;b.onclick=function(){var s=0,m=[],a=0;for(var i=0;i<Q.length;i++){var r=document.querySelector("input[name=q"+i+"]:checked");if(!r){continue}a++;s+=+r.value;if(+r.value<2)m.push(Q[i])}'
 'if(a<Q.length){alert("Svar på alle påstandene først.");return}'
 'var h=s>=12?"Dette ligner mye på hvem vi leter etter":s>=7?"Du kjenner deg igjen i flere av punktene":"Dette ligger et stykke fra det vi tilbyr nå";'
 'var p=s>=12?"Fortell oss hva du leverer i dag, så tar vi en samtale.":s>=7?"Fortell oss hva du leter etter, så finner vi ut av det sammen.":"Det kan likevel bli en god samtale. Vi er åpne på hva modellen er: eget selskap, stor frihet og et fagmiljø.";'
 'document.getElementById("kqh").textContent=h;document.getElementById("kqp").textContent=p;var l=document.getElementById("kql");l.innerHTML="";m.forEach(function(x){var li=document.createElement("li");li.textContent=x;l.appendChild(li)});'
 'document.getElementById("kqr").hidden=false;window.__kqm=m};'
 'document.getElementById("kqt").onclick=function(){var t=document.querySelector("#interesse textarea");if(t){t.value="Jeg kjenner meg ikke helt igjen i dette, og vil gjerne snakke om det:"+String.fromCharCode(10)+"- "+(window.__kqm||[]).join(String.fromCharCode(10)+"- ")}}})();</script></section>')%__import__("json").dumps(_kqs,ensure_ascii=False)
_kex=[_kw_("Petter"),_kw_("Morten"),_kw_("Janick")]
_kfolk=('<section class="wrap svsec" id="folk"><span class="omkick2">Fagekspertene</span><h2>Slik er det å være konsulent hos oss</h2><p class="omi">Møt tre av fagekspertene du vil jobbe sammen med.</p><div class="svfs kf3">'
 +"".join('<a class="svf" href="%s"><img src="%s" alt="%s" loading="lazy"><b>%s</b><span>%s</span><em>%s</em></a>'%(FL(e),U(e[3]),_E5(e[0]),_E5(e[0]),_E5(e[1]),_E5(e[2])) for e in _kex)
 +'</div></section>')
_kform=('<section class="omkont" id="interesse"><div class="wrap omkg2"><div><span class="omkick2">Interessert?</span><h2>Fortell oss om deg</h2><p class="omi">Send oss en kort melding om hvem du er og hva du jobber med. Vi svarer på e-post, og du trenger ikke oppgi telefon.</p>'
 '<dl class="omadr"><div><dt>Skriv direkte til Per Kjetil Parr</dt><dd><a href="mailto:pkp@excellerate.no?subject=Karriere%20i%20Excellerate">pkp@excellerate.no</a></dd></div><div><dt>Telefon</dt><dd><a href="tel:+4722490000">+47 22 49 00 00</a></dd></div><div><dt>Les også</dt><dd><a href="Kunnskap-vi-soker-norges-beste-konsulenter-paa-salgsutvikling-og-lederutvikling.dc.html">Den opprinnelige utlysningen</a></dd></div></dl></div>'
 '<aside class="kfo omf"><h2>Send oss en melding</h2><p class="sub">Vi tar kontakt om du passer inn i miljøet.</p><form>'
 '<div class="two"><label>Navn<input required autocomplete="name"></label><label>E-post<input type="email" required autocomplete="email"></label></div>'
 '<div class="two"><label>Telefon (valgfritt)<input type="tel" autocomplete="tel"></label><label>Eget selskap i dag?<select name="selskap"><option value="">Velg</option><option value="ja">Ja</option><option value="nei">Nei</option></select></label></div>'
 '<label>Hva jobber du med, og hva er du best på?<textarea rows="4" placeholder="Fortell kort om erfaring, fagfelt og hva du leverer i dag"></textarea></label>'
 '<label class="ck"><input type="checkbox" required><span>Jeg godtar at Excellerate lagrer opplysningene mine for å svare meg. <a href="#">Personvern</a></span></label>'
 '<button class="kn g" type="submit">Send melding</button></form>'
 '<div class="tk"><span class="ktag arr">Takk</span><h2>Meldingen er sendt</h2><p class="sub">Du hører fra oss på e-post.</p><a class="kn o" href="Om-oss.dc.html">Les mer om oss</a></div></aside></div></section>')
_knote="Kilde: utlysningen «Vi søker Norges beste konsulenter på salgsutvikling og lederutvikling» på excellerate.no (29.10.2025) og bannerteksten på Om oss, lest 14.11.2026. Modellen, fagfeltene, hvem dere søker og leveransene er hentet derfra. Tallene (snart 40 år, 16 fageksperter, 5 000 og 300 000) er de samme som på Om oss. Forslag, ikke avtalt: overskriftene, teksten som utdyper fagfeltene (bygger på tjenestesidene), at kontakten går til Per Kjetil Parr, og skjemaet. Skjemaet er ikke koblet til e-post eller CRM ennå. Stortorvet 7: Årets bygg 2023 (Byggeindustrien, Byggedagene) er hentet fra olavolsen.no (14.3.2024); Tom husket «i fjor», kildene sier 2023. Fasadebildet av Stortorvet 7 er sendt av Tom og viser Excellerate-skilt som er lagt inn i bildet, så det er et redigert bilde og ikke et ekte foto av skiltingen. Rettigheter og fotograf må avklares. Resepsjonsbildet er fra Om oss. Ekspertene er foreløpig vist med profilteksten sin. Egne sitater om hverdagen mangler og må komme fra ekspertene selv. Mangler grunnlag, derfor ikke med: utlyste stillinger, ansettelsesprosess og lønn. Må godkjennes av Excellerate."
_tpg("Karriere.dc.html","Karriere: bygg din praksis i fagmiljøet | Excellerate",_khero+_kstat+_kfet+_kdeg+_kar4+_kbyg+_kfolk+_klev+_kmod+_kq+_kform,_knote)
_kf=open("Karriere.dc.html").read()
_ks=_kf.index('<section id="samtale"');_ke=_kf.index('</section>',_ks)+len('</section>')
open("Karriere.dc.html","w").write(_kf[:_ks]+_kf[_ke:])
