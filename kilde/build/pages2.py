# Tjenester, Bransjer og ny Kontakt-side. Menytekstene er fra forrige runde (forslag). Artikkelkoblingene er forslag.
_ART=lambda s,t:'<a class="xl-lenke tjl" href="Kunnskap-%s.dc.html">Les: %s<span class="pil"></span></a>'%(s,_E5(t))
_HR={"verdisalg":"Tjenester-Salg.dc.html#verdisalg","ki-salg":"Tjenester-Salg.dc.html#ki-salg","salgsledelse":"Tjenester-Salg.dc.html#finne","kundeinnsikt":"Tjenester-Salg.dc.html#finne","strategi":"Tjenester-Ledelse.dc.html#strategi","coaching":"Tjenester-Ledelse.dc.html#program","organisasjon":"Tjenester-Kultur.dc.html#metode","prestasjon":"Tjenester-Kultur.dc.html#kulturen","kommersiell":"Tjenester-Kultur.dc.html#kommersiell","aiact":"Tjenester-KI.dc.html#aiact","ki-hverdag":"Tjenester-KI.dc.html#ki-hverdag","infosikkerhet":"Tjenester-KI.dc.html#infosikkerhet"}
_HS={"salg":"Tjenester-Salg.dc.html","ledelse":"Tjenester-Ledelse.dc.html","kultur":"Tjenester-Kultur.dc.html","ki":"Tjenester-KI.dc.html"}
def _tc(i,t,s,emne,art=None):
    return '<div class="tjc" id="%s"><h3>%s</h3><p>%s</p>%s<a class="kn o" href="%s">Les mer</a></div>'%(i,_E5(t),_E5(s),(_ART(*art) if art else ""),_HR[i])
def _ts(i,kick,h,intro,cards):
    return '<section class="wrap omsec tjs" id="%s"><div class="omh"><span class="omkick2">%s</span><h2>%s</h2><p class="omi">%s</p><p style="margin-top:18px"><a class="kn g" href="%s">Se hele området</a></p></div><div class="tjg">%s</div></section>'%(i,_E5(kick),_E5(h),_E5(intro),_HS[i],"".join(cards))
_tj=(_ts("salg","Salgsutvikling","Når salget står stille","Fra rådgivende verdisalg til KI og kundeinnsikt.",[
  _tc("verdisalg","Rådgivende verdisalg","Selg på verdi, ikke pris","salg",("kunsten-a-velge-de-riktige-kundene","Kunsten å velge de riktige kundene")),
  _tc("ki-salg","Kunstig intelligens i salg","Mer tid til kundesamtaler","salg",("tar-salgsprosessen-til-et-helt-nytt-niva-med-ai","Tar salgsprosessen til et helt nytt nivå med AI")),
  _tc("salgsledelse","Salgsledelse","Ledere som løfter teamet","salg"),
  _tc("kundeinnsikt","Kundeinnsikt","Fakta før møtet","salg",("hvem-sin-feil-er-det-nar-kundene-velger-deg-bort","Hvem sin feil er det når kundene velger deg bort?"))])
 +_ts("ledelse","Lederutvikling","Når strategien ikke blir til handling","Fra plan til daglig praksis.",[
  _tc("strategi","Strategi til handling","Fra plan til daglig praksis","ledelse",("utfordringen-er-etterlevelsen","Utfordringen er IKKE målene eller strategiene")),
  _tc("coaching","Coaching","Én til én med en fagekspert","ledelse"),
  _tc("organisasjon","Organisasjonsutvikling","Struktur som bærer strategien","ledelse",("strategisk-samarbeid-organisasjonsutvikling","Et strategisk samarbeid som styrker organisasjonsutviklingen"))])
 +_ts("kultur","Kulturutvikling","Når kulturen står i veien for målene","Vaner som gir resultater.",[
  _tc("prestasjon","Prestasjonskultur","Vaner som gir resultater","kultur",("glede-viktigere-enn-trivsel-tilfredshet","På jobb er glede viktigere enn trivsel og tilfredshet")),
  _tc("kommersiell","Kommersiell kultur","Hele huset tenker kunde","kultur",("baerekraftig-kommersiell-utvikling","Fundamentet for bærekraftig kommersiell utvikling"))])
 +_ts("ki","KI, adopsjon og sikkerhet","Når KI vokser fortere enn kontrollen","Regelverk, bruk og trygghet.",[
  _tc("aiact","AI Act og compliance","Klar for regelverket","ki"),_tc("ki-hverdag","KI i hverdagen","Fra pilot til bruk","ki"),_tc("infosikkerhet","Informasjonssikkerhet","Trygg bruk av data","ki")]))
_nav=lambda l:'<div class="tjn">'+"".join('<a href="#%s">%s</a>'%(a,b) for a,b in l)+'</div>'
_hj=lambda h,p,n:'<section class="dyp hero kort rov" style="color:#fff"><div class="wrap kw">'+_xw("hx")+'<h1>%s</h1><p class="hl">%s</p>%s</div></section>'%(h,p,n)
_tjn=_nav([("salg","Salgsutvikling"),("ledelse","Lederutvikling"),("kultur","Kulturutvikling"),("ki","KI, adopsjon og sikkerhet")])
_tjend='<section class="wrap" style="padding-bottom:96px"><p class="ksrc">De fire områdene har egne sider. Teksten på sidene for salg, ledelse og kultur er hentet fra dagens excellerate.no. Kortene her og artikkelkoblingene er forslag som må godkjennes av fagekspertene.</p></section>'
_write("Tjenester.dc.html","Tjenester, salg, ledelse, kultur og KI | Excellerate",_hj("Fire områder som henger sammen","Velg der dere trenger mest.",_tjn)+_tj+'<section class="wrap">'+_kkb()+'</section>'+_tjend,3000,cta="La oss finne ut hvilket av disse fire som gir mest igjen")
# ---------- Bransjer ----------
def _bs(i,img,h,items,rev=False):
    return ('<section class="wrap omsec bsj" id="%s"><div class="bsr%s"><div class="bsi"><img src="%s" alt="" loading="lazy"></div><div><h2>%s</h2><ul class="bsl">%s</ul>'
      '<div class="kbs"><a class="kn g" href="Kontakt.dc.html?emne=annet#skjema">Snakk med oss</a><a class="kn o" href="Referanser.dc.html">Se referanser</a></div></div></div></section>')%(i," rev" if rev else "",img,_E5(h),"".join("<li>%s</li>"%_E5(x) for x in items))
_br=(_bs("handel",U(IMG["salg"]),"Handel og forhandlernett",["Retail og faghandel","Bil"])
 +_bs("bank","/_blob/6aee73de7614899efc4561a8f50ec8d6","Bank, forsikring og eiendomsmegling",["Sparebank","Forsikring","Megling"],True)
 +_bs("bygg","/_blob/db80b62da762e5e37fd701b9e92157de","Bygg og eiendom",["Entreprenør og anlegg","Tekniske fag","Utleie og drift"])
 +_bs("it","/_blob/0a081d31223ec6fa18fe5a9f2aa94d8b","IT og teknologi",["Programvare","Konsulent","Drift"],True))
_write("Bransjer.dc.html","Bransjer: fire vertikaler | Excellerate",_hj("Fire vertikaler","KI, adopsjon og sikkerhet gjelder alle fire.",_nav([("handel","Handel og forhandlernett"),("bank","Bank, forsikring og eiendomsmegling"),("bygg","Bygg og eiendom"),("it","IT og teknologi")]))+_br+'<section class="wrap" style="padding-top:64px">'+_kkb()+'</section><section class="wrap" style="padding-bottom:96px"><p class="ksrc">Inndelingen er et forslag. Hver bransje får egen landingsside etter strategimøtet om hvilke bransjer vi går etter.</p></section>',3000,cta="La oss ta en samtale om hvordan dette ser ut i deres bransje")
# ---------- Kontakt (ny, utvidet) ----------
_ic=lambda d:'<svg aria-hidden="true" viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">%s</svg>'%d
_TEMA=[("salg","Salgsutvikling","Finne, vinne og beholde kunder",_ic('<path d="M4 19V9M10 19V5M16 19v-7M22 19H2"/>')),
 ("ledelse","Lederutvikling","Fra strategi til handling",_ic('<circle cx="12" cy="8" r="3.5"/><path d="M5 20c1-4 4-6 7-6s6 2 7 6"/>')),
 ("kultur","Kulturutvikling","Vaner som gir resultater",_ic('<path d="M12 21s-7-4.6-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 11c0 5.4-7 10-7 10z"/>')),
 ("ki","KI, adopsjon og sikkerhet","Fra pilot til trygg bruk",_ic('<rect x="5" y="5" width="14" height="14" rx="2"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/>')),
 ("gap","GAP Vision","Kundeinnsikt som gir vekst",_ic('<circle cx="11" cy="11" r="6.5"/><path d="M16 16l5 5"/>')),
 ("annet","Noe annet","Fortell oss hva dere tenker",_ic('<path d="M4 5h16v11H9l-5 4z"/>'))]
_tm='<section class="ktw"><div class="wrap"><p class="ktt">Velg tema</p><div class="ktg" role="group" aria-label="Velg tema">'+"".join('<button type="button" class="ktm2" data-emne="%s">%s<b>%s</b><span>%s</span></button>'%(a,d,_E5(b),_E5(c)) for a,b,c,d in _TEMA)+'</div></div></section>'
_stp=lambda n,h,t:'<li><span>%s</span><div><h3>%s</h3><p>%s</p></div></li>'%(n,h,t)
_steg='<div class="kst"><h3>Slik går det videre</h3><ol>'+_stp("1","Du forteller oss hva dere vil løse","Noen få linjer holder. Telefon er valgfritt.")+_stp("2","Vi finner riktig fagekspert","Tom eller Per Kjetil kobler dere til den som kan fagfeltet best.")+_stp("3","Dere får en uforpliktende samtale","Vi tar kontakt og avtaler tid. Ingen forpliktelser.")+'</ol></div>'
_bes=('<section class="wrap omsec" style="padding-top:72px"><div class="kbe"><div class="kbi2"><img src="%s" alt="Stortorvet i Oslo" loading="lazy"></div><div><h2>Besøk oss</h2><p class="omi">Stortorvet 7, 0155 Oslo<br>Vi møter dere gjerne her, eller hos dere.</p>'
  '<div class="kbs" style="margin-top:24px;display:flex;gap:12px;flex-wrap:wrap"><a class="kn g" href="https://www.google.com/maps/search/?api=1&amp;query=Stortorvet+7+0155+Oslo" target="_blank" rel="noopener noreferrer">Åpne i kart</a><a class="kn o" href="https://www.linkedin.com/company/excellerate-norway/" target="_blank" rel="noopener noreferrer">Følg oss på LinkedIn</a></div></div></div></section>')%U("6c10bbc2090df8189f1fdb57970dafa0")
_selv=('<section class="wrap omsec" style="padding-top:24px;padding-bottom:96px"><div class="omh"><h2>Vil du lese litt først?</h2></div><div class="omdg ksl">'
  '<a class="omd" href="Kunnskap.dc.html"><span class="omn">1</span><h3>Kunnskapssenteret</h3><p>Artikler, guider og arrangementer fra fagekspertene.</p></a>'
  '<a class="omd" href="Referanser.dc.html"><span class="omn">2</span><h3>Referanser</h3><p>Resultater hos kunder, med tall vi kan stå inne for.</p></a>'
  '<a class="omd" href="Fagekspertene.dc.html"><span class="omn">3</span><h3>Fagekspertene</h3><p>Møt de 16 som jobber med dere.</p></a></div></section>')
_kside=('<section class="dyp hero kort rov" style="color:#fff"><div class="wrap kw">'+_xw("hx")+'<h1>Hva vil dere løse?</h1><p class="hl">Velg et tema, så tar vi det derfra. Vi svarer på e-post, og du trenger ikke oppgi telefon.</p></div></section>'
  +_tm+'<section class="omkont" id="kontakt" style="margin-top:0"><div class="wrap omkg2"><div><h2>Hvem vil du snakke med?</h2><div class="omkp">'+_kk2+'</div>'+_steg+_adr+'</div>'+_skjema+'</div></section>'+_bes+_selv)
_write("Kontakt.dc.html","Kontakt Excellerate | Excellerate","<style>#samtale{display:none}</style>"+_kside,2400)

exec(open("tjenester3.py").read())

