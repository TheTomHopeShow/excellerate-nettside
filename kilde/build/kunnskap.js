
(()=>{
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
/* lesefremdrift */
const bar=$('.kbar');
if(bar){const u=()=>{const d=document.documentElement,h=d.scrollHeight-innerHeight;bar.style.width=(h>0?Math.min(100,scrollY/h*100):0)+'%';const p=$('.ktm .pr');if(p)p.style.width=bar.style.width};addEventListener('scroll',u,{passive:true});u()}
/* innhold: aktiv seksjon + mobilvisning */
const hs=$$('.kbd h2[id]');
if(hs.length){
 const links=$$('.ktoc a,.ktm nav a'),cur=$('.ktm button span');
 const setOn=id=>{links.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+id));const h=document.getElementById(id);if(cur&&h)cur.textContent=h.textContent};
 const io=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting)setOn(e.target.id)})},{rootMargin:'-120px 0px -65% 0px'});
 hs.forEach(h=>io.observe(h));setOn(hs[0].id);
 const tm=$('.ktm');
 if(tm){const bt=$('button',tm);bt.addEventListener('click',()=>{const o=!tm.classList.contains('o');tm.classList.toggle('o',o);bt.setAttribute('aria-expanded',o)});
  $$('nav a',tm).forEach(a=>a.addEventListener('click',()=>{tm.classList.remove('o');bt.setAttribute('aria-expanded','false')}));
  document.addEventListener('click',e=>{if(!tm.contains(e.target)){tm.classList.remove('o');bt.setAttribute('aria-expanded','false')}})}
 links.forEach(a=>a.addEventListener('click',e=>{const h=document.getElementById(a.getAttribute('href').slice(1));if(h){e.preventDefault();h.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'auto':'smooth',block:'start'});history.replaceState(null,'','#'+h.id)}}));
}
/* til toppen */
$$('[data-top]').forEach(b=>b.addEventListener('click',()=>scrollTo({top:0,behavior:'smooth'})));
/* del */
$$('[data-share]').forEach(b=>b.addEventListener('click',async()=>{const l=b.dataset.share;if(l==='li'){open('https://www.linkedin.com/sharing/share-offsite/?url='+encodeURIComponent(location.href),'_blank','noopener');return}
 try{if(navigator.share)await navigator.share({title:document.title,url:location.href});else{await navigator.clipboard.writeText(location.href);const t=b.getAttribute('aria-label');b.setAttribute('aria-label','Lenken er kopiert');b.title='Lenken er kopiert';setTimeout(()=>{b.setAttribute('aria-label',t);b.title=''},2000)}}catch(e){}}));
/* lytt (demo med nettleserens talesyntese) */
const ly=$('[data-lytt]');
if(ly){ if(!('speechSynthesis' in window)){ly.style.display='none'}else{
 const lab=$('span',ly);let on=false;
 const stop=()=>{speechSynthesis.cancel();on=false;ly.classList.remove('on');lab.textContent='Lytt til artikkel'};
 ly.addEventListener('click',()=>{if(on){stop();return}
  const txt=$$('.kbd p,.kbd h2,.kbd h3,.kbd li').map(x=>x.textContent).join('. ');
  const u=new SpeechSynthesisUtterance(txt);u.lang='nb-NO';u.onend=stop;u.onerror=stop;speechSynthesis.speak(u);on=true;ly.classList.add('on');lab.textContent='Stopp opplesing'});
 addEventListener('pagehide',()=>speechSynthesis.cancel())}}
/* oversikt: filter + søk */
const gr=$('.kgr[data-f]');
if(gr){
 const st={t:'',o:'',r:'',q:''},cards=$$('.kc',gr),cnt=$('.kcount'),tom=$('.ktom');
 let run=()=>{let n=0;cards.forEach(c=>{const ok=(!st.t||c.dataset.t===st.t)&&(!st.o||(c.dataset.o||'').split(' ').includes(st.o))&&(!st.r||(c.dataset.r||'').split(' ').includes(st.r))&&(!st.q||c.textContent.toLowerCase().includes(st.q));c.classList.toggle('gjem',!ok);if(ok)n++});
  cnt.textContent=n===cards.length?'Viser alt ('+n+')':'Viser '+n+' av '+cards.length;tom.style.display=n?'none':'block'};
 const tabs=$$('.ktab'),sels=$$('.ksent select');
 const fit=x=>{const m=document.createElement('span');const cs=getComputedStyle(x);m.style.cssText='position:absolute;visibility:hidden;white-space:nowrap;font:'+cs.font+';letter-spacing:'+cs.letterSpacing;m.textContent=x.options[x.selectedIndex].text;document.body.appendChild(m);x.style.width=Math.ceil(m.getBoundingClientRect().width)+34+'px';m.remove()};
 sels.forEach(fit);if(document.fonts)document.fonts.ready.then(()=>sels.forEach(fit));
 const base=c=>(!st.o||(c.dataset.o||'').split(' ').includes(st.o))&&(!st.r||(c.dataset.r||'').split(' ').includes(st.r))&&(!st.q||c.textContent.toLowerCase().includes(st.q));
 const counts=()=>tabs.forEach(t=>{const v=t.dataset.v;t.querySelector('.n').textContent=cards.filter(c=>base(c)&&(!v||c.dataset.t===v)).length});
 const run0=run;run=()=>{run0();counts()};
 sels.forEach(x=>x.addEventListener('change',()=>{st[x.dataset.g]=x.value;fit(x);run()}));
 tabs.forEach(t=>t.addEventListener('click',()=>{st.t=t.dataset.v;tabs.forEach(y=>y.classList.toggle('on',y===t));run()}));
 const si=$('.ksok input');if(si)si.addEventListener('input',()=>{st.q=si.value.trim().toLowerCase();run()});
 const rs=$('[data-reset]');if(rs)rs.addEventListener('click',()=>{st.t=st.o=st.r=st.q='';if(si)si.value='';sels.forEach(x=>{x.selectedIndex=0;fit(x)});tabs.forEach((x,i)=>x.classList.toggle('on',i===0));run()});
 const qp=new URLSearchParams(location.search);
 [['omrade','o'],['rolle','r']].forEach(([n,g])=>{const v=qp.get(n),x=sels.find(y=>y.dataset.g===g);if(v&&x&&[...x.options].some(o=>o.value===v)){x.value=v;st[g]=v;fit(x)}});
 {const f=qp.get('format'),t=tabs.find(y=>y.dataset.v===f);if(t){st.t=f;tabs.forEach(y=>y.classList.toggle('on',y===t))}}
 {const q=qp.get('q');if(q&&si){si.value=q;st.q=q.toLowerCase()}}
 run();
}
/* skjema (demo, sender ingenting) */
$$('.kfo form').forEach(f=>f.addEventListener('submit',e=>{e.preventDefault();f.closest('.kfo').classList.add('ok');f.closest('.kfo').scrollIntoView({block:'nearest',behavior:'smooth'})}));
})();
