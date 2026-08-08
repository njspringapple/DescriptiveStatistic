(() => {
  const P=window.PAGE, root=document.documentElement;
  document.title=`Wortschatz ${String(P.no).padStart(2,'0')} · ${P.de} | 德语主题词汇卡`;
  document.querySelector('.eyebrow').textContent=`Thema ${String(P.no).padStart(2,'0')} · ${P.level||'Grundwortschatz A1–B1'}`;
  document.querySelector('h1').innerHTML=P.titleHtml||P.de.replace(/[äöüÄÖÜaeiouAEIOU]/,'<em>$&</em>');
  document.querySelector('.sub').innerHTML=`${P.zh} <span>${P.en} · ${P.words.length} Wörter</span>`;
  const palette=['#EBD8CF','#D8E5D1','#D7E2EC','#EADDC8','#E5D7E3','#D5E6E2','#EEE3C9','#DAD9EA'];
  const col={der:'var(--der)',die:'var(--die)',das:'var(--das)',other:'var(--other)'};
  const parsed=P.words.map((v,i)=>{
    const [de,zh,en,grammar='',icon='']=v;
    const m=de.match(/^(der|die|das)\s+(.+)$/i);
    return {de,zh,en,grammar,icon,a:m?m[1].toLowerCase():'other',w:m?m[2]:de,i};
  });
  const grid=document.getElementById('grid');
  grid.innerHTML=parsed.map((v,i)=>`<article class="card" data-art="${v.a}" data-key="${(v.de+' '+v.zh+' '+v.en).toLowerCase()}" data-say="${v.de.replace(/"/g,'&quot;')}">
    <div class="thumb" style="--tint:${palette[i%palette.length]}"><span class="num">${String(i+1).padStart(2,'0')}</span><span class="art-pill" style="background:${col[v.a]}">${v.a==='other'?'Wort':v.a}</span><div class="disc"><span class="pic">${v.icon||window.TERM_ICONS?.[P.file]?.[i]||P.icons[i%P.icons.length]}</span><span class="pic-no">${String(i+1).padStart(2,'0')}</span></div></div>
    <div class="body"><div class="wrow f-de"><h2 class="de">${v.a==='other'?v.w:`<span class="a">${v.a}</span>${v.w}`}</h2><button class="say" aria-label="发音">◖</button></div>
    <p class="meta f-de">${v.grammar?`Grammatik: <b>${v.grammar}</b>`:'Grundwortschatz · A1–B1'}</p><div class="hr"></div>
    <p class="en f-en">${v.en}</p><p class="zh f-zh">${v.zh}</p>
    <div class="ex"><span class="exde">Ich lerne heute „${v.de}“.</span><span class="exzh">我今天学习“${v.zh}”。</span></div></div></article>`).join('');
  const cards=[...grid.children],cnt=document.getElementById('count');let art='all',q='';
  function apply(){let n=0;cards.forEach(c=>{const ok=(art==='all'||c.dataset.art===art)&&c.dataset.key.includes(q);c.style.display=ok?'':'none';if(ok)n++});cnt.textContent=`${n} / ${cards.length} WÖRTER`}
  document.getElementById('q').oninput=e=>{q=e.target.value.trim().toLowerCase();apply()};
  document.getElementById('arts').onclick=e=>{const b=e.target.closest('[data-art]');if(!b)return;document.querySelectorAll('[data-art]').forEach(x=>x.classList.remove('on'));b.classList.add('on');art=b.dataset.art;apply()};
  const map={de:'.f-de',zh:'.f-zh',en:'.f-en'};
  document.getElementById('togs').onclick=e=>{const b=e.target.closest('[data-t]');if(!b)return;b.classList.toggle('off');const t=b.dataset.t,off=b.classList.contains('off');if(t==='ex')grid.classList.toggle('hd-ex',off);else document.querySelectorAll(map[t]).forEach(x=>x.classList.toggle('mask',off))};
  let voice=null;function pick(){voice=speechSynthesis.getVoices().find(v=>v.lang.startsWith('de'))||null}
  if('speechSynthesis'in window){speechSynthesis.onvoiceschanged=pick;pick()}
  function speak(txt,done){if(!('speechSynthesis'in window))return;speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(txt);u.lang='de-DE';u.rate=.82;if(voice)u.voice=voice;if(done)u.onend=done;speechSynthesis.speak(u)}
  grid.onclick=e=>{const c=e.target.closest('.card');if(!c)return;if(e.target.closest('.say')){e.stopPropagation();speak(c.dataset.say);return}c.classList.toggle('open');const i=cards.indexOf(c);if(!window.WordScene||!WordScene.open({page:P,word:parsed[i],index:i}))speak(c.dataset.say)};
  let playing=false;
  document.getElementById('play').onclick=function(){const vis=cards.filter(c=>c.style.display!=='none');if(playing){speechSynthesis.cancel();playing=false;this.textContent='▶ 朗读全部';return}playing=true;this.textContent='■ 停止';let i=0,btn=this;const next=()=>{cards.forEach(c=>c.classList.remove('speaking'));if(!playing||i>=vis.length){playing=false;btn.textContent='▶ 朗读全部';return}const c=vis[i++];c.scrollIntoView({behavior:'smooth',block:'center'});c.classList.add('open','speaking');speak(c.dataset.say,next)};next()};
  document.getElementById('shuffle').onclick=()=>{[...cards].sort(()=>Math.random()-.5).forEach(c=>grid.appendChild(c))};
  document.getElementById('print').onclick=()=>window.print();
  apply();
})();
