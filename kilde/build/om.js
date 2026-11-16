(function(){var f=document.querySelector('.omf');if(!f)return;var q=new URLSearchParams(location.search),h=f.querySelector('[name=hvem]'),e=f.querySelector('[name=emne]');
function set(s,v){if(v&&[].some.call(s.options,function(o){return o.value===v}))s.value=v}
set(h,q.get('hvem'));set(e,q.get('emne'));
[].forEach.call(document.querySelectorAll('[data-who]'),function(a){a.addEventListener('click',function(){set(h,a.dataset.who)})});
[].forEach.call(document.querySelectorAll('[data-emne]'),function(a){a.addEventListener('click',function(){set(e,a.dataset.emne)})});
f.querySelector('form').addEventListener('submit',function(ev){ev.preventDefault();f.classList.add('ok');f.scrollIntoView({block:'nearest',behavior:'smooth'})});
var tm=[].slice.call(document.querySelectorAll('.ktm2'));
function mark(){tm.forEach(function(b){b.classList.toggle('on',b.dataset.emne===e.value)})}
tm.forEach(function(b){b.addEventListener('click',function(){set(e,b.dataset.emne);mark();f.scrollIntoView({behavior:'smooth',block:'center'});var n=f.querySelector('input:not([type=checkbox])');if(n)setTimeout(function(){n.focus({preventScroll:true})},500)})});
e.addEventListener('change',mark);mark();
if(location.hash==='#kontakt'&&q.get('hvem'))document.getElementById('kontakt').scrollIntoView();
})();
