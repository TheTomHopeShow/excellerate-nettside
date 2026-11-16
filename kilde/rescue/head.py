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
