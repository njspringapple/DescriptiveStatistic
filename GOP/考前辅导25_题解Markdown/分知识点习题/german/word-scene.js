(() => {
  const FILE_SCENES=[
    [/Restaurant|Fruehstueck|Getraenke/,'restaurant','Café · Restaurant'],
    [/Arzt|Apotheke|Versicherung|Notfall|Koerper|Koerperpflege/,'clinic','Praxis · Apotheke'],
    [/Bahnhof|Fahrzeuge|Weg|Reise/,'station','Bahnhof · Unterwegs'],
    [/Auto-Tanken|Reparatur|Elektro/,'workshop','Werkstatt · Service'],
    [/Bank|Geld|Vertraege/,'bank','Beratung · Service'],
    [/Amt|Aufenthalt|Bewerbung/,'office','Büro · Behörde'],
    [/Buero|Berufe/,'office','Arbeitsplatz'],
    [/Schule|Computer|Handy|Medien/,'school','Lernen · Medien'],
    [/Wohnung|Moebel|Haushalt|Nachbarschaft|Muell/,'home','Zu Hause'],
    [/Sport|Tiere|Wetter|Stadt|Freizeit/,'outdoor','Draußen · Freizeit'],
    [/Kleidung|Schuhe|Supermarkt|Laeden|Post/,'market','Geschäft · Einkauf'],
    [/Familie|Gefuehle|Termin|Feste|Begruessung|Freundschaft|Kinder|Tagesablauf/,'home','Alltag · Gespräch']
  ];
  const ctxFor=p=>FILE_SCENES.find(([r])=>r.test(p.file||''))?.slice(1)||((p.g==='essen')?['market','Markt · Küche']:['market','Alltagsszene']);
  const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const acc=a=>a==='der'?'den':a==='die'?'die':a==='das'?'das':'';
  function normalize(raw,index,page){
    const de=raw.w||raw.de||'',a=(raw.a||'').toLowerCase(),label=(a&&a!=='other'?`${a} ${de}`:de);
    const icon=raw.icon||window.TERM_ICONS?.[page.file]?.[index]||page.icons?.[index%Math.max(1,page.icons.length)]||'💬';
    return {de,a,label,accLabel:a?`${acc(a)} ${de}`:de,zh:raw.zh||'相关表达',en:raw.en||'related expression',icon,svg:raw.svg||''};
  }
  function linesFor(v,scene){
    const noun=['der','die','das'].includes(v.a),target=`<strong>${esc(v.label)}</strong>`,zh=esc(v.zh),en=esc(v.en);
    if(scene==='clinic')return [
      ['left',`Guten Tag. Es geht heute um ${target}.`,`您好。今天要谈的是“${zh}”。`,`Hello. Today it is about “${en}”.`],
      ['right',noun?`Können Sie mir ${esc(v.accLabel)} bitte genauer erklären?`:`Können Sie mir erklären, wie man „${esc(v.de)}“ benutzt?`,`您能更具体地给我解释“${zh}”吗？`,`Could you explain “${en}” to me in more detail?`],
      ['left',`Natürlich. Wir schauen uns ${target} gemeinsam an.`,`当然。我们一起来了解“${zh}”。`,`Of course. Let us look at “${en}” together.`],
      ['right',`Danke. Jetzt weiß ich, was ich tun muss.`,`谢谢，现在我知道该怎么做了。`,`Thank you. Now I know what I need to do.`]];
    if(scene==='station')return [
      ['right',noun?`Entschuldigung, wo finde ich ${esc(v.accLabel)}?`:`Entschuldigung, wie kann ich hier „${esc(v.de)}“?`,`请问在哪里能找到“${zh}”？`,`Excuse me, where can I find “${en}”?`],
      ['left',`Gehen Sie geradeaus. Dort sehen Sie ${target}.`,`请直走，您会在那里看到“${zh}”。`,`Go straight ahead. You will see “${en}” there.`],
      ['right',`Muss ich dabei noch etwas beachten?`,`我还需要注意什么吗？`,`Is there anything else I need to consider?`],
      ['left',`Ja, achten Sie bitte auf die Anzeige. Gute Fahrt!`,`有，请注意显示信息。祝您旅途愉快！`,`Yes, please watch the display. Have a good journey!`]];
    if(['office','bank'].includes(scene))return [
      ['right',`Guten Tag. Ich habe eine Frage zu ${target}.`,`您好，我想咨询“${zh}”。`,`Hello. I have a question about “${en}”.`],
      ['left',`Gern. Haben Sie die nötigen Unterlagen dabei?`,`当然。您带齐所需材料了吗？`,`Certainly. Do you have the required documents with you?`],
      ['right',`Ja. Was muss ich als Nächstes machen?`,`带了。下一步我需要做什么？`,`Yes. What do I need to do next?`],
      ['left',`Wir prüfen alles gemeinsam und bestätigen ${target}.`,`我们一起检查，然后确认“${zh}”。`,`We will check everything together and confirm “${en}”.`]];
    if(scene==='school')return [
      ['left',`Heute lernen wir ${target}.`,`今天我们学习“${zh}”。`,`Today we are learning “${en}”.`],
      ['right',`Können Sie bitte ein Beispiel zeigen?`,`您可以演示一个例子吗？`,`Could you show an example, please?`],
      ['left',`Ja. Achten Sie besonders auf die Verwendung von ${target}.`,`可以，请特别注意“${zh}”的用法。`,`Yes. Pay special attention to how “${en}” is used.`],
      ['right',`Jetzt ist es klar. Danke!`,`现在清楚了，谢谢！`,`It is clear now. Thank you!`]];
    if(scene==='home'||scene==='workshop')return [
      ['right',`Schau mal, hier ist ${target}.`,`看，这里是“${zh}”。`,`Look, here is “${en}”.`],
      ['left',noun?`Wofür brauchen wir ${esc(v.accLabel)}?`:`Wann sagt oder macht man „${esc(v.de)}“?`,`我们什么时候会用到“${zh}”？`,`When do we need or use “${en}”?`],
      ['right',`Das gehört zu unserem Alltag. Ich zeige es dir.`,`这是日常生活的一部分，我演示给你看。`,`It is part of everyday life. I will show you.`],
      ['left',`Gut, dann machen wir es gemeinsam.`,`好，那我们一起来做。`,`Good, then let us do it together.`]];
    if(scene==='outdoor')return [
      ['right',`Sieh mal! Dort ist ${target}.`,`快看！那里是“${zh}”。`,`Look! There is “${en}”.`],
      ['left',`Ja, das passt gut zu unserer heutigen Situation.`,`是的，这很符合我们今天的场景。`,`Yes, it fits our situation today.`],
      ['right',`Lass uns ${target} genauer ansehen.`,`让我们仔细看看“${zh}”。`,`Let us take a closer look at “${en}”.`],
      ['left',`Gute Idee. So kann ich mir das Wort merken.`,`好主意，这样我就能记住这个词。`,`Good idea. That helps me remember the word.`]];
    return [
      ['right',noun?`Guten Tag. Ich suche ${esc(v.accLabel)}.`:`Guten Tag. Ich möchte „${esc(v.de)}“.`,`您好，我在找“${zh}”。`,`Hello. I am looking for “${en}”.`],
      ['left',`Natürlich. Hier finden Sie ${target}.`,`当然。“${zh}”就在这里。`,`Of course. You can find “${en}” here.`],
      ['right',`Das sieht gut aus. Ich nehme es, bitte.`,`看起来不错，我要这个。`,`That looks good. I will take it, please.`],
      ['left',`Sehr gern. Brauchen Sie sonst noch etwas?`,`好的。您还需要别的吗？`,`Certainly. Do you need anything else?`]];
  }
  let modal,lines=[],at=0,currentLine=0,playLimit=0,playing=false,timer,segmentTimers=[],rate=1,speechLang='de',voices={de:null,en:null,zh:null},sceneContext=null,aiController=null,aiSpeechChunks=[],aiSpeechIndex=0,aiSpeechPaused=false,aiSpeechRate=1,aiSpeechMode='bilingual',aiSpeechTimer=null,dynamicContext=null,dynamicLevel=null;
  function preferredVoice(list,lang){
    const matches=list.filter(voice=>voice.lang.toLowerCase().startsWith(lang));
    return matches.sort((a,b)=>{
      const score=voice=>/natural|online|xiaoxiao|xiaoyi|yunxi|google|katja|conrad/i.test(voice.name)?2:/microsoft|apple/i.test(voice.name)?1:0;
      return score(b)-score(a);
    })[0]||null;
  }
  const voicePick=()=>{if('speechSynthesis'in window){const list=speechSynthesis.getVoices();voices.de=preferredVoice(list,'de');voices.en=preferredVoice(list,'en');voices.zh=preferredVoice(list,'zh')}};
  function ensure(){
    if(modal)return;document.body.insertAdjacentHTML('beforeend',`<div class="ws-modal" role="dialog" aria-modal="true"><div class="ws-box"><div class="ws-head"><span class="ws-kicker">Mini-Szene</span><b class="ws-title"></b><div class="ws-level-tools" hidden><label>Niveau <select aria-label="对话级别"><option value="A1">A1</option><option value="A2">A2</option><option value="B1">B1</option><option value="B2">B2</option><option value="C1">C1</option></select></label><button type="button" class="ws-dialogue-refresh">↻ 更新本级</button></div><button class="ws-close" aria-label="关闭">×</button></div><section class="ws-dialogue-picker" hidden><div class="ws-dialogue-picker-inner"><span class="ws-dialogue-kicker">AI Dialogue · CEFR</span><h2></h2><p class="ws-dialogue-intro">选择你的德语水平。AI会根据级别生成不同长度、词汇和语法难度的德国生活对话。</p><div class="ws-level-grid"></div><div class="ws-dialogue-status" role="status"></div></div></section><div class="ws-stage"><div class="ws-location"></div><div class="ws-speech"></div><div class="ws-person ws-left"><div class="ws-face"><i class="ws-eye a"></i><i class="ws-eye b"></i><i class="ws-mouth"></i></div><div class="ws-body"></div><div class="ws-arm"></div></div><div class="ws-person ws-right"><div class="ws-face"><i class="ws-eye a"></i><i class="ws-eye b"></i><i class="ws-mouth"></i></div><div class="ws-body"></div><div class="ws-arm"></div></div><div class="ws-prop"></div><div class="ws-counter"></div></div><div class="ws-subtitles"><div class="ws-dots"></div><div class="ws-sub-de"></div><div class="ws-sub-zh"></div><div class="ws-sub-en"></div></div><div class="ws-controls"><label class="ws-language" hidden>播放语言 <select aria-label="播放语言"><option value="de">德语</option><option value="en">英语</option></select></label><label class="ws-rate">语速 <input type="range" min=".6" max="1.5" step=".05" value="1"><output>1.00×</output></label><button class="ws-btn ws-ai-open" hidden>✦ AI 老师讲解</button><button class="ws-btn ws-replay">▶ 再播放一次</button><button class="ws-btn alt ws-stop">■ 停止</button></div><section class="ws-ai-panel" hidden><div class="ws-ai-head"><div><b>AI 老师讲解</b><span>DEEPSEEK · 中文</span></div><button type="button" class="ws-ai-dismiss" aria-label="收起 AI 讲解">×</button></div><div class="ws-ai-audio"><button type="button" class="ws-ai-speak" disabled>▶ 朗读讲解</button><button type="button" class="ws-ai-pause" disabled>Ⅱ 暂停</button><button type="button" class="ws-ai-speech-stop" disabled>■ 停止</button><label>朗读 <select class="ws-ai-speech-mode" aria-label="AI 讲解朗读模式"><option value="bilingual">中德双语</option><option value="zh">只读中文</option></select></label><label>语速 <input class="ws-ai-speech-rate" type="range" min=".7" max="1.5" step=".1" value="1"><output>1.0×</output></label></div><div class="ws-ai-body"></div><div class="ws-ai-foot"><span class="ws-ai-model"></span><button type="button" class="ws-ai-regenerate">↻ 重新讲解</button></div></section></div></div>`);modal=document.querySelector('.ws-modal');modal.addEventListener('click',e=>{const target=e.target.closest?.('.ws-sync');if(target){e.preventDefault();speakPhrase(target.dataset.sync)}});modal.addEventListener('keydown',e=>{const target=e.target.closest?.('.ws-sync');if(target&&(e.key==='Enter'||e.key===' ')){e.preventDefault();speakPhrase(target.dataset.sync)}});modal.querySelector('.ws-close').onclick=close;modal.onclick=e=>{if(e.target===modal)close()};modal.querySelector('.ws-replay').onclick=()=>play();modal.querySelector('.ws-stop').onclick=stop;modal.querySelector('.ws-dialogue-refresh').onclick=()=>generateDynamicDialogue(dynamicLevel,true);modal.querySelector('.ws-level-tools select').onchange=e=>selectDynamicLevel(e.target.value);modal.querySelector('.ws-ai-open').onclick=openAITeacher;modal.querySelector('.ws-ai-regenerate').onclick=()=>generateAIExplanation();modal.querySelector('.ws-ai-dismiss').onclick=collapseAITeacher;modal.querySelector('.ws-ai-speak').onclick=startAIReading;modal.querySelector('.ws-ai-pause').onclick=toggleAIReading;modal.querySelector('.ws-ai-speech-stop').onclick=stopAIReading;const aiModeSelect=modal.querySelector('.ws-ai-speech-mode');aiModeSelect.onchange=()=>{aiSpeechMode=aiModeSelect.value;if(modal.dataset.aiSpeaking==='true')startAIReading()};const aiRateInput=modal.querySelector('.ws-ai-speech-rate'),aiRateOutput=modal.querySelector('.ws-ai-speech-rate+output');aiRateInput.oninput=()=>{aiSpeechRate=Number(aiRateInput.value);aiRateOutput.value=aiSpeechRate.toFixed(1)+'×'};const langSelect=modal.querySelector('.ws-language select');langSelect.onchange=()=>{speechLang=langSelect.value;play()};const input=modal.querySelector('.ws-rate input'),out=modal.querySelector('.ws-rate output');input.oninput=()=>{rate=Number(input.value);out.value=rate.toFixed(2)+'×'};addEventListener('keydown',e=>{if(e.key==='Escape'&&modal.classList.contains('show'))close()});if('speechSynthesis'in window){speechSynthesis.onvoiceschanged=voicePick;voicePick()}}
  const strip=s=>String(s??'').replace(/<[^>]+>/g,'');
  function autoSyncLine(line){
    const tokenize=(text,lang)=>{
      if(lang==='zh'&&globalThis.Intl?.Segmenter){
        return [...new Intl.Segmenter('zh',{granularity:'word'}).segment(strip(text))].map(item=>item.segment).filter(item=>item.trim());
      }
      return String(text||'').trim().split(/\s+/).filter(Boolean);
    };
    const balanced=(tokens,count)=>Array.from({length:count},(_,index)=>{
      const start=Math.round(index*tokens.length/count),end=Math.round((index+1)*tokens.length/count);
      return tokens.slice(start,end);
    });
    const join=(tokens,lang)=>lang==='zh'?tokens.join(''):tokens.join(' ').replace(/\s+([,.;:!?])/g,'$1');
    const clauses=(text,lang,commas=false)=>{
      const source=String(text||'').trim();if(!source)return [];
      if(lang==='zh')return source.match(commas?/[^。！？；，]+[。！？；，]?/g:/[^。！？；]+[。！？；]?/g)||[source];
      return source.split(commas?/(?<=[.!?;,])\s+/:/(?<=[.!?;])\s+/).filter(Boolean);
    };
    const languages=['de','zh','en'];
    for(const commas of [false,true]){
      const sets=Object.fromEntries(languages.map(lang=>[lang,clauses(line[lang],lang,commas)]));
      const counts=languages.map(lang=>sets[lang].length),count=counts[0];
      if(count>1&&count<=6&&counts.every(value=>value===count)){
        return Object.fromEntries(languages.map(lang=>[lang,sets[lang].map((text,index)=>({id:'auto-'+index,text:text.trim()}))]));
      }
    }
    const deTokens=tokenize(line.de,'de'),zhTokens=tokenize(line.zh,'zh'),enTokens=tokenize(line.en,'en');
    const desired=Math.min(6,Math.max(1,Math.ceil(deTokens.length/3)));
    const count=Math.max(1,Math.min(desired,deTokens.length,zhTokens.length,enTokens.length));
    const make=(tokens,lang)=>balanced(tokens,count).map((part,index)=>({id:'auto-'+index,text:join(part,lang)}));
    return {de:make(deTokens,'de'),zh:make(zhTokens,'zh'),en:make(enTokens,'en')};
  }
  function syncMarkup(sync,lang,fallback){
    const parts=sync?.[lang];
    if(!parts?.length)return lang==='de'?fallback:esc(fallback);
    return parts.map(part=>'<span class="ws-sync" data-sync="'+esc(part.id)+'" role="button" tabindex="0" title="点击单独朗读这一段">'+(lang==='de'?part.text:esc(part.text))+'</span>').join(' ');
  }
  function setActiveSegment(id){
    modal.querySelectorAll('.ws-sync').forEach(node=>node.classList.toggle('active',node.dataset.sync===id));
  }
  function speakPhrase(id){
    const line=lines[currentLine],sync=line?.[4],part=sync?.[speechLang]?.find(item=>item.id===id);
    if(!part)return;
    stop();setActiveSegment(id);
    const plain=strip(part.text),who=line[0];
    modal.dataset.playingSegment=id;modal.dataset.spokenText=plain;modal.dataset.spokenLang=speechLang;
    modal.querySelector('.ws-left').classList.toggle('talk',who==='left');
    modal.querySelector('.ws-right').classList.toggle('talk',who==='right');
    const finish=()=>modal.querySelectorAll('.ws-person').forEach(node=>node.classList.remove('talk'));
    if('speechSynthesis'in window){
      const utterance=new SpeechSynthesisUtterance(plain);
      utterance.lang=speechLang==='en'?'en-US':'de-DE';utterance.rate=rate;
      const selectedVoice=voices[speechLang];if(selectedVoice)utterance.voice=selectedVoice;
      utterance.onend=finish;utterance.onerror=finish;speechSynthesis.speak(utterance);
    }else timer=setTimeout(finish,Math.max(700,(plain.match(/[A-Za-zÄÖÜäöüß]+/g)||[]).length*430/rate));
  }
  function clearSegmentTimers(){segmentTimers.forEach(clearTimeout);segmentTimers=[]}
  function segmentForChar(sync,lang,charIndex){
    let cursor=0;
    for(const part of sync?.[lang]||[]){
      const end=cursor+strip(part.text).length;
      if(charIndex<=end)return part.id;
      cursor=end+1;
    }
    return sync?.[lang]?.at(-1)?.id;
  }
  function scheduleSegments(sync,lang){
    clearSegmentTimers();
    const parts=sync?.[lang]||[];
    if(!parts.length)return;
    const weights=parts.map(part=>Math.max(1,(strip(part.text).match(/[A-Za-zÄÖÜäöüß]+/g)||[]).length));
    const total=weights.reduce((sum,n)=>sum+n,0);
    const duration=Math.max(1700,total*430/rate);
    let elapsed=0;
    parts.forEach((part,index)=>{
      segmentTimers.push(setTimeout(()=>setActiveSegment(part.id),elapsed));
      elapsed+=duration*weights[index]/total;
    });
  }
  function render(i){
    const [who,de,zh,en,sync]=lines[i];currentLine=i;
    const spoken=speechLang==='en'?en:de;
    const secondary=speechLang==='en'?de:en;
    const secondaryLang=speechLang==='en'?'de':'en';
    modal.querySelector('.ws-speech').innerHTML=syncMarkup(sync,speechLang,spoken);
    modal.querySelector('.ws-speech').classList.add('show');
    modal.querySelector('.ws-sub-de').innerHTML=syncMarkup(sync,speechLang,spoken);
    modal.querySelector('.ws-sub-zh').innerHTML=syncMarkup(sync,'zh',zh);
    modal.querySelector('.ws-sub-en').innerHTML=syncMarkup(sync,secondaryLang,secondary);
    modal.querySelector('.ws-left').classList.toggle('talk',who==='left');
    modal.querySelector('.ws-right').classList.toggle('talk',who==='right');
    [...modal.querySelectorAll('.ws-dots i,.ws-dots button')].forEach((d,n)=>d.classList.toggle('on',n===i));
    if(sync?.[speechLang]?.length)setActiveSegment(sync[speechLang][0].id);
  }
  function next(){
    if(!playing||at>=playLimit){playing=false;clearSegmentTimers();modal.querySelectorAll('.ws-person').forEach(x=>x.classList.remove('talk'));return}
    const line=lines[at++];
    render(at-1);
    const plain=strip(speechLang==='en'?line[3]:line[1]);
    scheduleSegments(line[4],speechLang);
    if('speechSynthesis'in window){
      const u=new SpeechSynthesisUtterance(plain);
      u.lang=speechLang==='en'?'en-US':'de-DE';u.rate=rate;const selectedVoice=voices[speechLang];if(selectedVoice)u.voice=selectedVoice;
      let boundarySeen=false;
      u.onboundary=e=>{if(e.name==='word'&&line[4]){if(!boundarySeen){boundarySeen=true;clearSegmentTimers()}setActiveSegment(segmentForChar(line[4],speechLang,e.charIndex))}};
      u.onend=()=>{clearSegmentTimers();timer=setTimeout(next,380)};
      speechSynthesis.speak(u);
    }else timer=setTimeout(next,Math.max(1900,(plain.match(/[A-Za-zÄÖÜäöüß]+/g)||[]).length*430/rate));
  }
  function updateAIAudioButtons(){
    if(!modal)return;const ready=modal.dataset.aiReady==='true',speaking=modal.dataset.aiSpeaking==='true';
    modal.querySelector('.ws-ai-speak').disabled=!ready||speaking||!('speechSynthesis'in window);
    modal.querySelector('.ws-ai-pause').disabled=!speaking;
    modal.querySelector('.ws-ai-speech-stop').disabled=!speaking;
    modal.querySelector('.ws-ai-pause').textContent=aiSpeechPaused?'▶ 继续':'Ⅱ 暂停';
  }
  function setAIAudioReady(ready){modal.dataset.aiReady=String(Boolean(ready));updateAIAudioButtons()}
  function clearAIReadingHighlight(){modal?.querySelectorAll('.ws-ai-body .is-reading').forEach(node=>node.classList.remove('is-reading'))}
  function resetAIReadingState(){
    clearTimeout(aiSpeechTimer);aiSpeechTimer=null;aiSpeechChunks=[];aiSpeechIndex=0;aiSpeechPaused=false;clearAIReadingHighlight();
    if(modal){modal.dataset.aiSpeaking='false';delete modal.dataset.aiSpeechLang;modal.querySelector('.ws-ai-speak').textContent='▶ 朗读讲解'}updateAIAudioButtons();
  }
  function stopAIReading(){if('speechSynthesis'in window)speechSynthesis.cancel();resetAIReadingState()}
  function pushAISpeechChunk(chunks,text,lang,node){
    let clean=String(text||'').replace(/^[\s•\-–—"“”'‘’=：:]+|[\s"“”'‘’=]+$/g,'').trim();if(!clean)return;
    if(lang==='zh'&&!/[\u3400-\u9fff]/.test(clean))return;
    if(lang==='de'&&!/[A-Za-zÄÖÜäöüß]/.test(clean))return;
    const limit=lang==='de'?120:72;
    const sentences=lang==='zh'?(clean.match(/[^。！？!?；;]+[。！？!?；;]?/g)||[clean]):(clean.match(/[^.!?;]+[.!?;]?/g)||[clean]);
    sentences.forEach(sentence=>{const part=sentence.trim();for(let i=0;i<part.length;i+=limit)chunks.push({text:part.slice(i,i+limit),lang,node})});
  }
  function collectAISpeechChunks(){
    const chunks=[],latin=/[A-Za-zÄÖÜäöüß][A-Za-zÄÖÜäöüß0-9'’\-]*(?:[ \t]+[A-Za-zÄÖÜäöüß][A-Za-zÄÖÜäöüß0-9'’\-]*)*/g;
    modal.querySelectorAll('.ws-ai-body h2,.ws-ai-body h3,.ws-ai-body h4,.ws-ai-body p').forEach(node=>{
      const text=node.textContent.trim();if(!text)return;let cursor=0,match;
      while((match=latin.exec(text))){
        pushAISpeechChunk(chunks,text.slice(cursor,match.index),'zh',node);
        if(aiSpeechMode==='bilingual')pushAISpeechChunk(chunks,match[0],'de',node);
        cursor=match.index+match[0].length;
      }
      pushAISpeechChunk(chunks,text.slice(cursor),'zh',node);
    });
    return chunks;
  }
  function speakNextAIChunk(){
    if(modal.dataset.aiSpeaking!=='true'||aiSpeechPaused)return;
    if(aiSpeechIndex>=aiSpeechChunks.length){resetAIReadingState();return}
    const item=aiSpeechChunks[aiSpeechIndex++];clearAIReadingHighlight();item.node.classList.add('is-reading');item.node.scrollIntoView?.({block:'center',behavior:'smooth'});
    modal.dataset.aiSpeechLang=item.lang;modal.querySelector('.ws-ai-speak').textContent='朗读中 · '+(item.lang==='de'?'德语':'中文');
    const utterance=new SpeechSynthesisUtterance(item.text);utterance.lang=item.lang==='de'?'de-DE':'zh-CN';utterance.rate=item.lang==='de'?Math.max(.65,aiSpeechRate*.9):aiSpeechRate;utterance.pitch=1;
    const selectedVoice=item.lang==='de'?voices.de:voices.zh;if(selectedVoice)utterance.voice=selectedVoice;
    utterance.onend=()=>{aiSpeechTimer=setTimeout(speakNextAIChunk,item.lang==='de'?260:150)};utterance.onerror=()=>resetAIReadingState();speechSynthesis.speak(utterance);
  }
  function startAIReading(){
    if(modal.dataset.aiReady!=='true'||!('speechSynthesis'in window))return;stop();
    aiSpeechChunks=collectAISpeechChunks();modal.dataset.aiQueueZh=String(aiSpeechChunks.filter(item=>item.lang==='zh').length);modal.dataset.aiQueueDe=String(aiSpeechChunks.filter(item=>item.lang==='de').length);if(!aiSpeechChunks.length)return;
    aiSpeechIndex=0;aiSpeechPaused=false;modal.dataset.aiSpeaking='true';updateAIAudioButtons();speakNextAIChunk();
  }
  function toggleAIReading(){
    if(modal.dataset.aiSpeaking!=='true'||!('speechSynthesis'in window))return;
    aiSpeechPaused=!aiSpeechPaused;if(aiSpeechPaused){clearTimeout(aiSpeechTimer);aiSpeechTimer=null;speechSynthesis.pause()}else{speechSynthesis.resume();if(!speechSynthesis.speaking)speakNextAIChunk()}updateAIAudioButtons();
  }
  function collapseAITeacher(){stopAIReading();if(modal.dataset.aiReady!=='true')aiController?.abort();modal.querySelector('.ws-ai-panel').hidden=true;modal.querySelector('.ws-box').classList.remove('ai-open')}
  function openAITeacher(){
    stop();const panel=modal.querySelector('.ws-ai-panel');panel.hidden=false;modal.querySelector('.ws-box').classList.add('ai-open');if(modal.dataset.aiReady==='true')return;setAIAudioReady(false);
    if(!window.AITeacher){modal.querySelector('.ws-ai-body').innerHTML='<div class="ws-ai-error">AI 模块未加载，请刷新页面后重试。</div>';return}
    if(!AITeacher.hasKey()){
      modal.querySelector('.ws-ai-body').innerHTML='<div class="ws-ai-empty"><p>还没有设置 DeepSeek API Key。请先在首页右上角的“AI 设置”中保存 Key。</p><a class="ws-ai-link" href="index.html#ai-settings" target="_blank" rel="noopener">打开首页设置</a></div>';
      modal.querySelector('.ws-ai-model').textContent='Key 仅保存在浏览器本地';return;
    }
    generateAIExplanation();
  }
  async function generateAIExplanation(){
    if(!sceneContext||!window.AITeacher)return;
    if(!AITeacher.hasKey()){openAITeacher();return}
    stopAIReading();aiController?.abort();aiController=new AbortController();
    const body=modal.querySelector('.ws-ai-body'),foot=modal.querySelector('.ws-ai-foot');
    modal.querySelector('.ws-ai-panel').hidden=false;modal.querySelector('.ws-box').classList.add('ai-open');foot.hidden=true;setAIAudioReady(false);
    body.innerHTML='<div class="ws-ai-loading"><div><i></i><br>AI 老师正在阅读完整对话并准备中文讲解…</div></div>';
    try{
      const result=await AITeacher.explain(sceneContext,{signal:aiController.signal});
      body.innerHTML=AITeacher.renderMarkdown(result.content);
      const tokens=result.usage?.total_tokens?` · ${result.usage.total_tokens} tokens`:'';
      modal.querySelector('.ws-ai-model').textContent=(result.model||AITeacher.model)+tokens;foot.hidden=false;setAIAudioReady(true);
    }catch(error){
      if(error.name==='AbortError')return;
      const setup=error.code==='NO_API_KEY'?'<br><a class="ws-ai-link" href="index.html#ai-settings" target="_blank" rel="noopener">打开首页设置</a>':'';
      body.innerHTML='<div class="ws-ai-error"><strong>暂时无法生成讲解</strong><br>'+esc(error.message)+setup+'</div>';foot.hidden=false;setAIAudioReady(false);
    }
  }

  const DIALOGUE_STORE_KEY='deutschInSzenen.dialogues.v1';
  const LEVEL_DETAILS={
    A1:['4轮','最短句 · 基础购物表达'],
    A2:['5轮','简单问答 · 常见原因'],
    B1:['6轮','说明需求 · 处理问题'],
    B2:['8轮','自然协商 · 更多细节'],
    C1:['10轮','灵活表达 · 细腻语气']
  };
  function readDialogueStore(){
    try{return JSON.parse(localStorage.getItem(DIALOGUE_STORE_KEY)||'{}')}catch{return {}}
  }
  function dynamicStorageKey(){return dynamicContext.page.file+'::'+dynamicContext.v.de}
  function dynamicRecord(){return readDialogueStore()[dynamicStorageKey()]||{levels:{}}}
  function writeDynamicRecord(record){
    const store=readDialogueStore();store[dynamicStorageKey()]=record;
    try{localStorage.setItem(DIALOGUE_STORE_KEY,JSON.stringify(store))}
    catch(error){throw new Error('浏览器本地存储空间不足。请删除不需要的历史对话后再试。')}
  }
  function saveDynamicDialogue(level,result){
    const record=dynamicRecord();record.levels=record.levels||{};
    record.levels[level]={dialogue:result.dialogue,model:result.model,generatedAt:new Date().toISOString()};
    record.lastLevel=level;writeDynamicRecord(record);
  }
  function setDynamicLastLevel(level){
    const record=dynamicRecord();record.lastLevel=level;writeDynamicRecord(record);
  }
  function showDynamicPicker(message='',kind=''){
    stop();aiController?.abort();
    const picker=modal.querySelector('.ws-dialogue-picker'),box=modal.querySelector('.ws-box'),record=dynamicRecord();
    modal.querySelector('.ws-title').textContent=dynamicContext.v.label;
    modal.querySelector('.ws-level-tools').hidden=true;
    modal.querySelector('.ws-ai-panel').hidden=true;
    box.classList.remove('ai-open');box.classList.add('dialogue-choosing');
    picker.hidden=false;picker.querySelector('h2').textContent='为 '+dynamicContext.v.label+' 选择对话级别';
    const levels=window.AITeacher?.dialogueLevels||['A1','A2','B1','B2','C1'];
    picker.querySelector('.ws-level-grid').innerHTML=levels.map(level=>{
      const saved=Boolean(record.levels?.[level]),detail=LEVEL_DETAILS[level];
      return '<button type="button" data-level="'+level+'" class="'+(saved?'saved':'')+'"><b>'+level+'</b><span>'+detail[0]+'</span><small>'+detail[1]+'</small><em>'+(saved?'已保存 · 点击播放':'AI生成')+'</em></button>';
    }).join('');
    picker.querySelectorAll('[data-level]').forEach(button=>button.onclick=()=>{
      const level=button.dataset.level;
      if(dynamicRecord().levels?.[level])loadDynamicDialogue(level);else generateDynamicDialogue(level,false);
    });
    const status=picker.querySelector('.ws-dialogue-status');
    if(!window.AITeacher?.hasKey())status.innerHTML='尚未设置DeepSeek API Key。<a href="index.html#ai-settings" target="_blank" rel="noopener">打开首页AI设置</a>';
    else status.textContent=message;
    status.dataset.kind=kind;
    modal.classList.add('show');document.body.style.overflow='hidden';
  }
  function loadDynamicDialogue(level){
    const saved=dynamicRecord().levels?.[level];if(!saved)return showDynamicPicker('这个级别还没有历史对话。','error');
    dynamicLevel=level;setDynamicLastLevel(level);
    const dialogue=saved.dialogue,custom={...dynamicContext.custom,location:dialogue.location,lines:dialogue.lines,aiDialogue:true};
    const pickerStatus=modal.querySelector('.ws-dialogue-status');pickerStatus.dataset.kind='';pickerStatus.textContent='';
    showScene(dynamicContext.v,custom);
    const tools=modal.querySelector('.ws-level-tools'),select=tools.querySelector('select');
    tools.hidden=false;select.value=level;
    [...select.options].forEach(option=>option.textContent=option.value+(dynamicRecord().levels?.[option.value]?' · 已保存':' · 未生成'));
  }
  function selectDynamicLevel(level){
    if(dynamicRecord().levels?.[level])loadDynamicDialogue(level);else generateDynamicDialogue(level,false);
  }
  async function generateDynamicDialogue(level,replace=false){
    if(!dynamicContext||!window.AITeacher)return;
    if(!AITeacher.hasKey()){showDynamicPicker('请先设置API Key。','error');return}
    showDynamicPicker('', '');
    const picker=modal.querySelector('.ws-dialogue-picker'),status=picker.querySelector('.ws-dialogue-status');
    picker.querySelectorAll('[data-level]').forEach(button=>button.disabled=true);
    status.dataset.kind='loading';
    status.innerHTML='<i></i><b>'+(replace?'正在更新':'正在生成')+' '+level+' 对话…</b><span>AI正在设计真实场景、三语翻译和语义分段</span>';
    aiController?.abort();aiController=new AbortController();
    try{
      const result=await AITeacher.generateDialogue({
        word:dynamicContext.v.label,zh:dynamicContext.v.zh,en:dynamicContext.v.en,
        category:dynamicContext.page.zh||dynamicContext.page.de,location:dynamicContext.custom.location
      },level,{signal:aiController.signal});
      saveDynamicDialogue(level,result);loadDynamicDialogue(level);
    }catch(error){
      if(error.name==='AbortError')return;
      showDynamicPicker(error.message,'error');
    }
  }
  function openDynamicDialogue(v,custom,page,index){
    dynamicContext={v,custom,page,index};dynamicLevel=null;
    const record=dynamicRecord(),last=record.lastLevel;
    if(last&&record.levels?.[last])loadDynamicDialogue(last);else showDynamicPicker();
    return true;
  }
  function play(){stop();at=0;playLimit=lines.length;playing=true;next()}function playSegment(index){stop();at=index;playLimit=Math.min(lines.length,index+1);playing=true;next()}function stop(){playing=false;clearTimeout(timer);clearSegmentTimers();if('speechSynthesis'in window)speechSynthesis.cancel();resetAIReadingState();modal?.querySelectorAll('.ws-person').forEach(x=>x.classList.remove('talk'))}function close(){stop();aiController?.abort();modal.querySelector('.ws-box').classList.remove('ai-open');modal.classList.remove('show');document.body.style.overflow=''}
  function has({page={},word={}}){const key=word.w||word.de||'';return Boolean(window.WORD_SCENE_CUSTOM?.[page.file]?.[key])}

  function showScene(v,custom){
    aiController?.abort();
    sceneContext={word:v.label,location:custom.location,lines:custom.lines.map(x=>({de:x.de,zh:x.zh,en:x.en}))};
    const aiButton=modal.querySelector('.ws-ai-open'),aiPanel=modal.querySelector('.ws-ai-panel');
    aiButton.hidden=custom.aiTeacher===false;aiPanel.hidden=true;
    modal.querySelector('.ws-box').classList.remove('ai-open','dialogue-choosing');
    modal.querySelector('.ws-dialogue-picker').hidden=true;
    modal.querySelector('.ws-level-tools').hidden=!dynamicContext;
    setAIAudioReady(false);modal.querySelector('.ws-ai-body').innerHTML='';
    modal.querySelector('.ws-ai-foot').hidden=false;modal.querySelector('.ws-ai-model').textContent='';
    speechLang='de';
    const languageControl=modal.querySelector('.ws-language'),languageSelect=languageControl.querySelector('select'),enabledLanguages=custom.playbackLanguages||['de','en'];
    languageControl.hidden=enabledLanguages.length<2;languageSelect.value='de';
    const scene=custom.scene,location=custom.location;
    lines=custom.lines.map(x=>[x.who,x.de,x.zh,x.en,x.sync||autoSyncLine(x)]);
    modal.querySelector('.ws-title').textContent=v.label;
    modal.querySelector('.ws-location').textContent=location;
    modal.querySelector('.ws-stage').className='ws-stage ws-'+scene;
    const dots=modal.querySelector('.ws-dots'),selectableSegments=custom.selectableSegments!==false;
    dots.classList.toggle('selectable',selectableSegments);
    if(selectableSegments){
      dots.setAttribute('role','group');dots.setAttribute('aria-label','选择播放段落');
      dots.innerHTML=lines.map((_,i)=>'<button type="button" data-line="'+i+'" aria-label="播放第 '+(i+1)+' 段"><span>'+(i+1)+'</span></button>').join('');
      dots.querySelectorAll('button').forEach(button=>button.onclick=()=>playSegment(Number(button.dataset.line)));
    }else{
      dots.removeAttribute('role');dots.removeAttribute('aria-label');dots.innerHTML=lines.map(()=>'<i></i>').join('');
    }
    modal.querySelector('.ws-prop').innerHTML='<span class="ws-prop-icon">'+esc(custom.prop||v.icon)+'</span>';
    modal.classList.add('show');document.body.style.overflow='hidden';play();return true;
  }
  function open({page={},word={},index=0}){
    ensure();const v=normalize(word,index,page),custom=window.WORD_SCENE_CUSTOM?.[page.file]?.[v.de];
    if(!custom)return false;
    if(custom.aiDialogue)return openDynamicDialogue(v,custom,page,index);
    dynamicContext=null;dynamicLevel=null;return showScene(v,custom);
  }
  window.WordScene={open,close,has,autoSyncLine};
})();
