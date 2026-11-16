(()=>{const r=document.getElementById('bk');if(!r)return;
const M=['januar','februar','mars','april','mai','juni','juli','august','september','oktober','november','desember'],D=['Man','Tir','Ons','Tor','Fre','Lør','Søn'],DL=['søndag','mandag','tirsdag','onsdag','torsdag','fredag','lørdag'];
const now=new Date(),t0=new Date(now.getFullYear(),now.getMonth(),now.getDate());
let vm=new Date(t0.getFullYear(),t0.getMonth(),1),sd=null,st=null;
const g=s=>r.querySelector(s),cal=g('.bkg'),mh=g('.bkm'),tl=g('.bkt'),fm=g('.bkf'),cf=g('.bkc'),pr=g('.bkp'),nx=g('.bkn'),bt=g('.bkb');
const ok=d=>{const w=d.getDay();return d>t0&&w>0&&w<6&&(d-t0)/864e5<=90};
const slots=d=>{const h=d.getDate()*7+d.getMonth()*3,o=[];for(let i=0;i<14;i++){const m=9*60+i*30;if((h+i*5)%4===0)continue;o.push(("0"+Math.floor(m/60)).slice(-2)+":"+(m%60?"30":"00"))}return o};
const step=n=>{r.dataset.s=n;[...r.querySelectorAll('.bks li')].forEach((l,i)=>l.className=i+1<n?'dn':i+1===n?'on':'')};
function drawCal(){mh.textContent=M[vm.getMonth()]+' '+vm.getFullYear();pr.disabled=vm<=new Date(t0.getFullYear(),t0.getMonth(),1);cal.innerHTML=D.map(d=>'<span class="bkw">'+d+'</span>').join('');
const first=(new Date(vm.getFullYear(),vm.getMonth(),1).getDay()+6)%7,n=new Date(vm.getFullYear(),vm.getMonth()+1,0).getDate(),cells=[];
for(let i=0;i<first;i++)cells.push(null);for(let d=1;d<=n;d++)cells.push(new Date(vm.getFullYear(),vm.getMonth(),d));while(cells.length%7)cells.push(null);
for(let w=0;w<cells.length;w+=7){const wk=cells.slice(w,w+7);if(!wk.some(x=>x&&ok(x)))continue;wk.forEach(dt=>{if(!dt){cal.insertAdjacentHTML('beforeend','<span></span>');return}
const b=document.createElement('button');b.type='button';b.textContent=dt.getDate();b.disabled=!ok(dt);if(sd&&+sd===+dt)b.className='on';b.setAttribute('aria-label',DL[dt.getDay()]+' '+dt.getDate()+'. '+M[dt.getMonth()]);b.onclick=()=>{sd=dt;st=null;drawCal();drawTimes();step(2)};cal.appendChild(b)})}}
function drawTimes(){if(!sd){tl.innerHTML='<p class="bkh">Velg en dag i kalenderen først.</p>';return}
g('.bkd').textContent=DL[sd.getDay()]+' '+sd.getDate()+'. '+M[sd.getMonth()];
tl.innerHTML=slots(sd).map(s=>'<button type="button" data-t="'+s+'"'+(st===s?' class="on"':'')+'>'+s+'</button>').join('');
tl.querySelectorAll('button').forEach(b=>b.onclick=()=>{st=b.dataset.t;drawTimes();step(3);g('.bkx').textContent=DL[sd.getDay()]+' '+sd.getDate()+'. '+M[sd.getMonth()]+' kl. '+st})}
pr.onclick=()=>{vm=new Date(vm.getFullYear(),vm.getMonth()-1,1);drawCal()};nx.onclick=()=>{vm=new Date(vm.getFullYear(),vm.getMonth()+1,1);drawCal()};
bt.onclick=()=>step(r.dataset.s==='3'?2:1);
fm.addEventListener('submit',e=>{e.preventDefault();g('.bkdone').textContent='Takk. Dette er en demo: ingen avtale er sendt ennå. Her kobler vi senere på kalenderen (HubSpot eller Outlook).';fm.hidden=true;g('.bkx').hidden=true;step(4)});
drawCal();drawTimes();step(1)})();
