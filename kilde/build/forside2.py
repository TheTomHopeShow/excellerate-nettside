# Forside v2 (14.11.2026): inngangskort med bilde og kundens egne utsagn som navigasjon, og overskrift utenfor «Slik jobber vi». Forslag, ikke avtalt.
_f=open("Forside.dc.html").read()
_Ef=lambda t:t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
_K=[("kxa05","Salgsutvikling","Når salget står stille","Tjenester-Salg.dc.html",[("Tjenester-Salg.dc.html#verdisalg","Kundene snakker bare om pris")]),
    ("kxa14","Lederutvikling","Når strategien ikke blir til handling","Tjenester-Ledelse.dc.html",[("Tjenester-Ledelse.dc.html#strategi","Strategien blir ikke til handling"),("Tjenester-Ledelse.dc.html#kontakt","Lederne mister kontakten med folkene")]),
    ("kxa11","Kulturutvikling","Når kulturen står i veien for målene","Tjenester-Kultur.dc.html",[("Tjenester-Kultur.dc.html#kulturen","Kulturen står i veien for målene"),("Tjenester-Kultur.dc.html#analyse","Vi vet ikke hvor skoen trykker")]),
    ("kxa16","KI, adopsjon og sikkerhet","Når KI vokser fortere enn kontrollen","Tjenester-KI.dc.html",[("Tjenester-KI.dc.html#hvorfor","Kan vi bevise at AI-en er til å stole på?")])]
def _kort(img,omr,h,href,qs):
    return ('<a class="fmc" href="%s"><span class="im"><img src="%s" alt="" loading="lazy"></span>'
     '<span class="bd"><h3>%s</h3><p>%s</p><span class="xl-lenke">Utforsk %s<span class="pil"></span></span></span></a>')%(href,U(img),_Ef(omr),_Ef(h),_Ef(omr[0].lower()+omr[1:]))
_QS=[("Tjenester-Salg.dc.html#verdisalg","Kundene snakker bare om pris"),("Tjenester-Ledelse.dc.html#strategi","Strategien blir ikke til handling"),("Tjenester-Kultur.dc.html#kulturen","Kulturen står i veien for målene"),("Tjenester-Kultur.dc.html#analyse","Vi vet ikke hvor skoen trykker"),("Tjenester-Ledelse.dc.html#kontakt","Lederne mister kontakten med folkene"),("Tjenester-KI.dc.html#hvorfor","Kan vi bevise at AI-en er til å stole på?")]
_PROB='<section class="wrap" id="problem" style="padding-bottom:88px"><div class="svq"><h2>Hvilket problem vil dere løse?</h2><div class="svqg">'+"".join('<a href="%s">%s</a>'%(a,_Ef(b)) for a,b in _QS)+'</div></div></section>'
_a=_f.index('<section id="mangler"'); _b=_f.index('</section>',_a)+10
_new=('<section id="mangler" class="sec"><div class="wrap"><h2 style="font-size:40px;line-height:46px;font-weight:500;max-width:18em">Hva mangler for at dere skal lykkes?</h2>'
 '<p style="margin-top:16px;font-size:21px;line-height:32px;font-weight:500;color:#566B76;max-width:34em">Oftest er ikke problemet strategien, men at den aldri blir til vane. Velg der dere kjenner dere igjen.</p>'
 '<div class="fmg">'+"".join(_kort(*k) for k in _K)+'</div></div></section>'+_PROB)
_f=_f[:_a]+_new+_f[_b:]
# Slik jobber vi: overskrift utenfor blokken
_o='<span class="tey"><i></i>Slik jobber vi</span><h2>Fra innsikt<br><em>til varig endring.</em></h2><p>Tre steg, sammen med dere.</p>'
assert _o in _f
_steps='<ol class="fmst"><li><b>Innsikt og fakta</b><span>forstå situasjonen</span></li><li><b>Rådgivning og metodeverk</b><span>finne riktig vei</span></li><li><b>Kompetanseheving</b><span>det som virker i hverdagen</span></li></ol>'
_f=_f.replace(_o,_steps)
_p='<div class="wrap"><div class="trp2">'
assert _p in _f
_f=_f.replace(_p,'<div class="wrap fmh"><h2 style="font-size:40px;line-height:46px;font-weight:500">Fra innsikt til varig endring</h2><p style="margin-top:12px;font-size:21px;line-height:32px;font-weight:500;color:#566B76">Slik jobber vi, tre steg sammen med dere.</p></div><div class="wrap" style="margin-top:40px"><div class="trp2">',1)
open("Forside.dc.html","w").write(_f)
print("forside2 ok")
