# Ekte artikler fra blogg.excellerate.no (16 nyeste). Brødtekst ordrett fra bloggen. Kortversjoner og bildevalg er utkast.
import json as _jj, re as _rr, html as _hh2, unicodedata as _ud
_BODY={b["slug"]:b for b in _jj.load(open("ex-body.json"))}
_ALL={x["slug"]:x for x in _jj.load(open("/mnt/user-data/uploads/Downloads/ex-alle.json"))}
_MON=["januar","februar","mars","april","mai","juni","juli","august","september","oktober","november","desember"]
def _dfull(d): y,m,dd=d.split("-"); return "%d. %s %s"%(int(dd),_MON[int(m)-1],y)
def _aslug(s): return s.lower().replace("å","a").replace("ø","o").replace("æ","ae")
KORT={
1:["Kunder sender signaler lenge før de ber om tilbud. Et kjøpssignal er atferd som viser endring i behov, prioritet eller beslutningsberedskap.","Noen signaler er synlige for alle, som utlyste stillinger og anbud. De mest verdifulle er ofte de ubevisste, som endringer i ledergruppen eller ny språkbruk på nettsider.","Salgsorganisasjoner er bygget for dialog, ikke observasjon. Å følge signalene systematisk gjør salgsarbeidet mer presist og mindre avhengig av timing-flaks."],
2:["Endringsprosesser mislykkes sjelden fordi folk er motvillige. De mislykkes fordi lederne starter med konklusjonen i stedet for å ta medarbeiderne med på veien dit.","Forfatteren trekker frem tre erkjennelser: endring innebærer tap og sorg, forakt forgifter, og det er lov å føle seg dårlig.","Metoden for å møte uro er å se «trollene» før man starter: hva kan gå galt, hvordan forebygger vi det, hvordan håndterer vi det, og når evaluerer vi."],
3:["Excellerate og Mentr.ai samarbeider om en personlig AI-assistent som støtter selgeren før, under og etter kundemøtet.","Under møtet gir løsningen råd i sanntid, foreslår spørsmål og peker ut kjøpssignaler. Etter møtet får selgeren oppfølging og anbefalte neste steg.","Artikkelen oppgir gevinster fra norske pilotkunder, blant annet kortere salgssyklus og mindre administrativt arbeid, og viser til frokostmøter for mer innsikt."],
4:["Excellerate (tidligere Euro Business School) søker erfarne fageksperter innen salgsutvikling, lederutvikling, strategi og kultur.","Modellen gir hver enkelt stor frihet og et faglig miljø med likesinnede. Fagekspertene er tilknyttet gjennom en avtale med eget selskap.","Leveransene spenner fra opplæring og utviklingsprogrammer til rådgivning, coaching, kick-off og webinarer."],
5:["Ros og anerkjennelse er blant de sterkeste driverne for arbeidsglede og prestasjon, men mange kvier seg for å gi og ta imot den.","Forfatteren viser til en Harvard-studie der de som fikk en positiv beskjed løste en kreativ oppgave oftere enn kontrollgruppen, og til undersøkelser fra Gallup og BI.","Rosen må være konkret og meningsfull. Forslaget er å rose minst én kollega hver dag."],
6:["Selvledelse handler om å gjøre egen utvikling til en fast del av hverdagen, i stedet for å jage raske resultater og KPI-er.","Det starter med en visjon som sier hvem du må være, hva du må prioritere og hva du tror på.","De beste gjør ikke nødvendigvis mer, men prioriterer smartere ut fra egne verdier."],
7:["Mange strategier havner i en skuff etter strategisamlingen. Utfordringen er sjelden målene, men etterlevelsen.","Strategier feiler gjerne fordi kompleksiteten undervurderes, evnen til å gjennomføre overvurderes, driften tar all tid, eller medarbeiderne ikke er involvert.","Kulturen må trekke i samme retning som strategien. Forfatteren foreslår en analyse av bedriftskulturen."],
8:["Utviklingsorientert ledelse handler om å søke fakta og innsikt, og å bygge en kultur der det er trygt å prøve og feile.","Artikkelen viser hvordan verktøyet GAP Vision analyserer salgskvalitet og kobler kundens opplevelse til salgsresultater.","Målet er at lederen baserer valg på data og ikke antakelser, og kan overføre beste praksis til resten av teamet."],
9:["Utviklingsorientert lederskap handler om å skape endring, ikke bare håndtere den, med nysgjerrighet, visjon og evne til å inspirere.","Artikkelen peker på gevinster som motivasjon, endringsdyktighet, innovasjon, bedre samarbeid og lavere fravær.","Lederen må bygge tillit, gi ansvar og fremme læring. Forfatteren kaller det fundamentet for bærekraftig vekst, ikke en trend."],
10:["Tilbakemeldingskulturen er en undervurdert driver for prestasjon, ved siden av lederutvikling og KPI-er.","De beste salgsteamene bruker systematisk feedback og coaching som strategisk verktøy, ikke som HR-tiltak, skriver forfatteren og viser til RAIN Group.","Overfladisk ros kan virke demotiverende. Prestasjonskultur vokser der folk tør å være konstruktivt ærlige."],
11:["Trivsel og tilfredshet er ikke det samme som arbeidsglede. Tilfredshet handler om hva folk tenker om jobbens vilkår, glede om hva de føler på jobben nå.","Forfatteren mener tilfredshet er fundamentet, men at det er glede som gir bedre prestasjoner, mer lojale medarbeidere og bedre kundeservice.","Rådet er å la målinger av tilfredshet få mindre plass, og heller sette søkelys på hvordan man skaper arbeidsglede."],
12:["En undersøkelse fra Infact for Amesto og SuperOffice viser at én av fem ikke kan forklare hvorfor kunder avslutter, og at en tredjedel ikke vet hvilke kunder som er på vei ut.","Per Kjetil Parr peker på manglende salgsferdigheter, for lite innsikt i kundens verdikjede og for få utviklingsmøter som vanlige årsaker.","Kundene vil fortsatt snakke med en selger, men forventer verdi utover det de allerede vet."],
13:["businessMastering og Excellerate har inngått et strategisk samarbeid om organisasjonsutvikling, kultur, ledelse og salg.","Rune Semundseth, kjent som forfatter av blant annet Kulturkoden, inngår i Excellerates faggruppe.","Samarbeidet ble markert med et gratis miniseminar om kulturutvikling i Oslo."],
14:["Det er fire drivere i oppkjøpsprosesser: strategiske verdier, juridisk trygghet, økonomiske utsikter, og menneskene og kulturen.","Ifølge fagekspertene er de tre første ofte godt ivaretatt, mens humankapitalen blir glemt.","Excellerate tilbyr en fusjons- og oppkjøpsanalyse som kartlegger fem områder, og som bør gjøres tidlig etter oppkjøpet, men ikke før det har gått en måned."],
15:["Mange oppkjøp og fusjoner når ikke målene sine. Artikkelen viser til undersøkelser som anslår feilrater på 70 til 90 prosent.","Mangelfull håndtering av menneskene er ifølge artikkelen den største enkeltfaktoren.","Excellerate har utviklet en GAP-oppkjøpsanalyse. Artikkelen anbefaler målinger 30, 90, 180 og 360 dager etter at oppkjøpet er annonsert."],
16:["Uten strategisk kundesegmentering brukes ressursene på kunder som ikke nødvendigvis gir lønnsomhet og vekst.","Per Kjetil Parr spør hvem som egentlig har valgt hvem, og mener bedrifter bør velge kundene sine ut fra objektive kriterier.","Løsningen er lønnsomhetsanalyser og en inndeling av kundene i prioriterte grupper, i tråd med Pareto-prinsippet."],
}
ALT={1:"Kvinne som snakker i telefon ved en laptop",2:"Utsnitt av en tekst om endring, med en liten figur på ordene",3:"Illustrasjon av en hjerne og en person ved en datamaskin",4:"Tre kolleger i et møte, to av dem håndhilser",5:"To kolleger gir hverandre high five",6:"To kolleger ser på en dataskjerm sammen",7:"Illustrasjon av to løpere på vei mot en målstrek",8:"Presentasjon ved en tavle med diagrammer i et møterom",9:"To forretningsmenn går sammen med kaffe i hånden",10:"Papirklipp-illustrasjon av en grønn by med vindmøller og trær",11:"Modell som viser sammenhengen mellom arbeidsglede og tilfredshet",12:"Mann ved en laptop som tar seg til hodet",13:"Fire kolleger i diskusjon rundt et bord",14:"Perm merket Due diligence på et skrivebord",15:"Hånd som signerer et dokument",16:"Sjakkbrikker på et sjakkbrett"}
HEROALT={}
def _txt(h): return _hh2.unescape(_rr.sub(r"<[^>]+>","",h)).replace("\xa0"," ").strip()
def _blocks(h): return _rr.findall(r"<(?:p|h2|h3|ul|ol|blockquote)>.*?</(?:p|h2|h3|ul|ol|blockquote)>|<img data-i=\"\d+\">",h,_rr.S)
def _cut_form(bl):
    # fjern oppfordring til skjema som ikke finnes på den nye siden
    if not bl: return bl
    t=_txt(bl[-1])
    if "skjema" in t.lower():
        m=_rr.search(r"(Fyll (?:ut|inn)|Hvis du ønsker|Vil du|Ønsker du)[^<]*skjema[^<]*$",bl[-1])
        if m and m.start()>0 and _rr.sub(r"<[^>]+>","",bl[-1][:m.start()]).strip(): bl[-1]=bl[-1][:m.start()]+"</p>" if bl[-1].startswith("<p>") else bl[-1]
        else: bl=bl[:-1]
        if bl and bl[-1].startswith("<p>") and _txt(bl[-1]).endswith("?") and len(_txt(bl[-1]))<110 and "skjema" not in _txt(bl[-1]).lower(): pass
    return bl
def _process(a):
    n=a["n"]; b=_BODY[a["slug"]]; bl=_blocks(b["html"])
    ing=_txt(a["ing"])
    # fjern første avsnitt når det er ingressen på nytt
    if bl and bl[0].startswith("<p>"):
        t0=_txt(bl[0]); 
        if t0[:40]==ing[:40] or ing.startswith(t0[:60]): bl=bl[1:]
    out=[]; fig_done=False
    for x in bl:
        if x.startswith("<img"):
            i=int(_rr.search(r"\d+",x).group()); src=b["imgs"][i]["src"]
            if "kahnemann" in src and not fig_done:
                out.append("@@KAHN@@"); fig_done=True
            continue
        if x=="<h2></h2>" or _txt(x)=="" : continue
        if "hybrodmodell" in x: continue
        out.append(x)
    out=_cut_form(out)
    # h2 med id
    toc=[];res=[]
    for x in out:
        if x.startswith("<h2>"):
            t=_txt(x); id="s%d"%(len(toc)+1); toc.append((id,t)); res.append('<h2 id="%s">%s</h2>'%(id,_E5(t)))
        elif x=="@@KAHN@@":
            res.append('<figure class="kf"><img src="%s" alt="%s" loading="lazy"><figcaption>Figur: Daniel Kahnemans hybridmodell, slik den vises i den opprinnelige artikkelen.</figcaption></figure>'%(U("kxb11"),_E5(ALT[11])))
        else: res.append(x)
    # bilde i artikkelen: etter første seksjon (før andre h2), ellers etter tredje avsnitt
    if n!=11:
        fig='<figure class="kf"><img src="%s" alt="%s" loading="lazy"></figure>'%(U("kxb%02d"%n),_E5(ALT[n]))
        idx=[i for i,x in enumerate(res) if x.startswith("<h2")]
        pos=idx[1] if len(idx)>=2 else min(3,len(res))
        res.insert(pos,fig)
    words=len(_rr.sub(r"<[^>]+>"," ","".join(res)).split())
    return "".join(res),toc,words
_AUTH_ROLE={}
def _real(a):
    n=a["n"]; name=a["author"]; slugp=_aslug(a["slug"])
    body,toc,words=_process(a)
    known=name in _BY and name in PD
    d=PD[name] if known else None
    mod=(_ALL[a["slug"]].get("mod") or a["date"])
    fmt=a["fmt"]; fag=fmt=="fag"
    chip=("Fagartikkel · " if fag else "Artikkel · ")+(a["tags"][0] if a["tags"] else "Excellerate")
    rl=_BY[name][1] if known else "Forfatter"
    if known:
        av='<img src="%s" alt="">'%U(_BY[name][3]); nm='<a class="nm" href="Fagekspert-%s.dc.html">%s</a>'%(d["slug"],_E5(name))
    else:
        ini="".join(w[0] for w in name.split()[:2]).upper(); av='<span class="kav x" aria-hidden="true" style="width:48px;height:48px">%s</span>'%_E5(ini); nm='<span class="nm">%s</span>'%_E5(name)
    toc_html="".join('<li><a href="#%s">%s</a></li>'%(i,_E5(t)) for i,t in toc)
    ld=_jj.dumps({"@context":"https://schema.org","@type":"Article","headline":a["title"],"description":a["ing"],"datePublished":a["date"],"dateModified":mod,"inLanguage":"nb","image":"img/art-%02d.webp"%n,"author":dict({"@type":"Person","name":name},**({"url":"https://excellerate.no/konsulent/%s/"%d["slug"]} if known else {})),"publisher":{"@type":"Organization","name":"Excellerate AS","url":"https://excellerate.no"}},ensure_ascii=False)
    kv='<div class="kkv%s"><h2>%s</h2><ul>%s</ul><p class="knote2">Utkast til kortversjon. Skrives av Excellerate og godkjennes av forfatteren.</p></div>'%(" hf" if fag else "","Hovedfunn" if fag else "Kortversjonen","".join("<li>%s</li>"%_E5(x) for x in KORT[n]))
    meta='<div class="row"><span class="kchip">%s</span><span class="kmeta">Publisert %s</span><span class="kmeta">Lesetid %d min</span></div>'%(_E5(chip),_dfull(a["date"]),max(1,round(words/200)))
    toc_nav=('<nav class="ktoc" aria-label="Innhold"><h2>'+_IC["list"]+'Innhold</h2><ol>'+toc_html+'</ol></nav>') if toc else ""
    tm=('<div class="ktm"><button type="button" aria-expanded="false">'+_IC["list"]+'Innhold<span></span><i></i></button><nav aria-label="Innhold">'+"".join('<a href="#%s">%s</a>'%(i,_E5(t)) for i,t in toc)+'</nav><div class="pr"></div></div>') if toc else '<div class="ktm"><div class="pr"></div></div>'
    if known:
        fn=_fn5(name); mail=d["mail"] or "post@excellerate.no"; tl=_tel(d["tlf"] or "22490000")
        cta='<div class="kcta">'+_xw("ix")+'<img src="%s" alt=""><div><h2>Ta en uforpliktende samtale</h2><p>Vil du høre hvordan dette ser ut hos dere? %s tar gjerne en prat.</p><div class="kbs"><a class="kn g" href="Fagekspert-%s.dc.html#book">Book en samtale</a><a class="kn l" href="mailto:%s">Send e-post</a><a class="kn l" href="tel:+47%s">Ring %s</a></div></div></div>'%(U(_BY[name][3]),_E5(fn),d["slug"],mail,tl[0],tl[1])
        more=_E5(fn)
        exb='<a class="kex2" href="Fagekspert-%s.dc.html"><img src="%s" alt=""><div><small>Artikkelens fagekspert</small><b>%s</b><span>%s. Se profil og book en samtale.</span></div><i class="pi"></i></a>'%(d["slug"],U(_BY[name][3]),_E5(name),_E5(rl))
    else:
        cta='<div class="kcta">'+_xw("ix")+'<div><h2>Ta en uforpliktende samtale</h2><p>Vil du høre hvordan dette ser ut hos dere? Fagekspertene i Excellerate tar gjerne en prat.</p><div class="kbs"><a class="kn g" href="Fagekspertene.dc.html">Finn riktig fagekspert</a><a class="kn l" href="mailto:post@excellerate.no">Send e-post</a><a class="kn l" href="tel:+4722490000">Ring 22 49 00 00</a></div></div></div>'
        more="Excellerate"; exb=""
    src='<p class="ksrc">Opprinnelig publisert %s på <a href="https://blogg.excellerate.no/%s" rel="noopener">blogg.excellerate.no</a>.</p>'%(_dfull(a["date"]),__import__("urllib.parse").parse.quote(a["slug"]))
    rel=[b for b in _EX16 if b["n"]!=n]; k0=[i for i,b in enumerate(rel) if b["n"]>n][:1]; k0=k0[0] if k0 else 0
    rel=[rel[(k0+i)%len(rel)] for i in range(3)]
    relh="".join(_kc(b["fmt"],b["o"],b["r"],title=b["title"],ing=b["ing"],forf=b["author"],meta=_dt(b["date"]),img=b["id"],href="Kunnskap-%s.dc.html"%_aslug(b["slug"])) for b in rel)
    page=('<script type="application/ld+json">'+ld+'</script><div class="kbar" aria-hidden="true"></div>'+tm+
     '<section class="wrap kah"><a class="kab" href="Kunnskap.dc.html">Kunnskapssenter</a><div class="kat">'+meta+'<h1>%s</h1><p class="kin">%s</p></div>'%(_E5(a["title"]),_E5(a["ing"]))
     +'<div class="kimg"><img src="%s" alt=""></div></section>'%U(a["id"])
     +'<section class="wrap kar"><div class="kl"><div class="kls">'+toc_nav+'</div></div>'
     '<article class="kbd"><div class="kby">%s<div>%s<div class="rl">%s</div></div><div class="act"><button class="kbt" type="button" data-lytt>%s<span>Lytt til artikkel</span></button></div></div>'%(av,nm,_E5(rl),_IC["lyd"])
     +'<p class="kdat">Sist oppdatert %s</p>'%_dfull(mod)+kv+exb+body+src+cta+_kkb()
     +'<div class="kne"><a class="kab" href="Kunnskap.dc.html">Alle artikler</a></div></article>'
     '<div class="kr"><div class="krs"><button class="ik" type="button" data-share="li" aria-label="Del på LinkedIn">'+_IC["li"]+'</button><button class="ik" type="button" data-share="lenke" aria-label="Del eller kopier lenke">'+_IC["del"]+'</button><button class="top" type="button" data-top>Til toppen</button></div></div></section>'
     '<section class="krel"><div class="wrap"><h2>Les også</h2><div class="kgr">'+relh+'</div></div></section>')
    _write("Kunnskap-%s.dc.html"%_aslug(a["slug"]),"%s | Excellerate"%a["title"],page,3400)
for _a in _EX16: _real(_a)
