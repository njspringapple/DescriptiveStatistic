(function(){
  'use strict';
  const STORAGE_KEY='deutschInSzenen.deepseek';
  const API_URL='https://api.deepseek.com/chat/completions';
  const MODEL='deepseek-v4-flash';

  function getConfig(){
    try{return JSON.parse(localStorage.getItem(STORAGE_KEY)||'{}')}catch{return {}}
  }
  function hasKey(){return Boolean(getConfig().apiKey)}
  function maskKey(key){return key?key.slice(0,5)+'••••••••'+key.slice(-4):''}
  function ensureSettings(){
    if(document.querySelector('.ai-settings-modal'))return;
    document.body.insertAdjacentHTML('beforeend',`
      <div class="ai-settings-modal" role="dialog" aria-modal="true" aria-labelledby="ai-settings-title">
        <div class="ai-settings-card">
          <div class="ai-settings-head">
            <div><span>AI Teacher</span><h2 id="ai-settings-title">DeepSeek 设置</h2></div>
            <button type="button" class="ai-settings-close" aria-label="关闭">×</button>
          </div>
          <p class="ai-settings-intro">API Key 仅保存在当前浏览器的 localStorage 中，不会写入项目文件。AI 讲解会直接从浏览器发送到 DeepSeek。</p>
          <label class="ai-key-label">DeepSeek API Key
            <span class="ai-key-field"><input class="ai-key-input" type="password" autocomplete="off" spellcheck="false" placeholder="sk-…"><button type="button" class="ai-key-reveal">显示</button></span>
          </label>
          <div class="ai-settings-meta"><span>模型</span><b>${MODEL}</b></div>
          <div class="ai-settings-status" role="status"></div>
          <div class="ai-settings-actions">
            <button type="button" class="ai-settings-save">保存设置</button>
            <button type="button" class="ai-settings-clear">删除 Key</button>
          </div>
          <p class="ai-settings-note">注意：这是适合个人本地学习的 BYOK 方式。不要在公共电脑保存 Key，也不要把包含 Key 的浏览器配置分享给别人。</p>
        </div>
      </div>`);
    const modal=document.querySelector('.ai-settings-modal');
    const input=modal.querySelector('.ai-key-input');
    const status=modal.querySelector('.ai-settings-status');
    const close=()=>{modal.classList.remove('show');document.body.classList.remove('ai-settings-open');if(location.hash==='#ai-settings')history.replaceState(null,'',location.pathname+location.search)};
    modal.querySelector('.ai-settings-close').onclick=close;
    modal.onclick=e=>{if(e.target===modal)close()};
    modal.querySelector('.ai-key-reveal').onclick=e=>{
      const reveal=input.type==='password';input.type=reveal?'text':'password';e.currentTarget.textContent=reveal?'隐藏':'显示';
    };
    modal.querySelector('.ai-settings-save').onclick=()=>{
      const apiKey=input.value.trim();
      if(!apiKey){status.textContent='请先填写 API Key。';status.dataset.kind='error';input.focus();return}
      localStorage.setItem(STORAGE_KEY,JSON.stringify({apiKey}));
      input.value=apiKey;status.textContent='已保存在当前浏览器：'+maskKey(apiKey);status.dataset.kind='ok';
      document.dispatchEvent(new CustomEvent('ai-config-changed'));
    };
    modal.querySelector('.ai-settings-clear').onclick=()=>{
      localStorage.removeItem(STORAGE_KEY);input.value='';status.textContent='已从当前浏览器删除 API Key。';status.dataset.kind='ok';
      document.dispatchEvent(new CustomEvent('ai-config-changed'));
    };
    addEventListener('keydown',e=>{if(e.key==='Escape'&&modal.classList.contains('show'))close()});
  }
  function openSettings(){
    ensureSettings();
    const modal=document.querySelector('.ai-settings-modal'),input=modal.querySelector('.ai-key-input'),config=getConfig();
    input.type='password';input.value=config.apiKey||'';
    modal.querySelector('.ai-key-reveal').textContent='显示';
    const status=modal.querySelector('.ai-settings-status');
    status.textContent=config.apiKey?'当前已保存：'+maskKey(config.apiKey):'尚未设置 API Key';
    status.dataset.kind=config.apiKey?'ok':'';
    modal.classList.add('show');document.body.classList.add('ai-settings-open');setTimeout(()=>input.focus(),80);
  }
  function strip(html){
    const node=document.createElement('div');node.innerHTML=String(html||'');return node.textContent.trim();
  }
  function buildPrompt(context){
    const dialogue=context.lines.map((line,index)=>
      `${index+1}. 德语：${strip(line.de)}\n   中文：${line.zh}\n   英语：${line.en}`
    ).join('\n');
    return `请讲解下面这个德国生活场景对话。

目标词：${context.word}
场景：${context.location}

${dialogue}

学习者情况：
- 母语是中文，英语词汇量约5000–6000，德语接近零基础。
- 当前重点是听、说、读，不要求拼写，也不想先系统学习语法。
- 希望通过固定搭配、语义块和生活场景培养语感。

请严格依据本段对话，用自然、清楚、不过度学术化的中文讲解，德语示例保留原文。按以下结构输出：
## 场景在说什么
用2–3句话说明人物关系、意图和真实使用情境。
## 逐句拆解
逐句拆成可直接开口使用的语义块；解释每块含义、语气和中英对应。不要逐词机械翻译。
## 重点词汇
讲解目标词及真正值得记的词：名词给冠词和复数，动词给原形，形容词说明本句形式。
## 固定搭配
列出本场景最实用的搭配和可替换槽位，并给出简短生活例句。
## 语法直觉
只解释理解和开口必须知道的语法，使用“这里为什么这样说”的方式，不堆术语。
## 德国生活提醒
说明这段话在德国是否自然、礼貌，以及市场购物中的实际表达习惯。
## 现在就会说
给出5条由易到难的口头练习，附中文提示，最后一条要求学习者独立表达。

要求：内容准确、具体、避免泛泛而谈；总长度控制在1200–1800个中文字符；不要编造原对话中不存在的文化事实。`;
  }
  const DIALOGUE_LEVELS={
    A1:{turns:4,maxWords:7,segments:'每句1–2个'},
    A2:{turns:5,maxWords:10,segments:'每句2–3个'},
    B1:{turns:6,maxWords:14,segments:'每句2–4个'},
    B2:{turns:8,maxWords:18,segments:'每句3–5个'},
    C1:{turns:10,maxWords:24,segments:'每句3–6个'}
  };
  function dialoguePrompt(context,level){
    const spec=DIALOGUE_LEVELS[level];
    return [
      '请为德国生活德语学习网站生成一段全新的场景对话，并只返回一个JSON对象。',
      '',
      '目标词：'+context.word,
      '中文意思：'+(context.zh||''),
      '英文意思：'+(context.en||''),
      '主题分类：'+(context.category||''),
      'CEFR级别：'+level,
      '',
      '难度和长度必须严格符合：',
      '- 一共'+spec.turns+'轮，一行就是一个人物的一次发言。',
      '- 每句德语最多约'+spec.maxWords+'个词。',
      '- 使用'+level+'词汇、语法、语气和信息密度；A1/A2直接具体，B1开始加入原因与处理，B2/C1允许更自然复杂的协商与细节。',
      '- 场景必须是学习者在德国真实可能遇到的生活场景，围绕目标词自然展开，禁止“这个词什么时候使用”一类教学式假对话。',
      '- 目标词或其正常变形至少自然出现两次。',
      '- right是顾客/学习者，left是店员/当地人；双方交替说话，第一句由right开始。',
      '- 中文和英文必须准确翻译当句德语，不增删信息。',
      '',
      'JSON结构必须严格如下：',
      '{"level":"'+level+'","sceneTitle":"简短中文场景名","location":"简短德语地点 · 中文情境","lines":[{"who":"right","sync":{"de":[{"id":"s1","text":"德语语义块"}],"zh":[{"id":"s1","text":"对应中文语义块"}],"en":[{"id":"s1","text":"corresponding English chunk"}]}}]}',
      '',
      '分段要求：',
      '- '+spec.segments+'语义块；按固定搭配和表达意群切分，不能机械按字数切。',
      '- 同一句de/zh/en必须使用完全相同的一组id；允许三种语言因为语序不同而调整id顺序。',
      '- 每个数组拼接后必须构成完整自然的一句话，标点放在相应语义块中。',
      '- text中禁止HTML、Markdown和换行。',
      '- 不要输出解释、代码围栏或JSON以外的文字。'
    ].join('\n');
  }
  function normalizeDialogue(raw,context,level){
    const spec=DIALOGUE_LEVELS[level],dialogue=raw?.dialogue||raw;
    if(!dialogue||!Array.isArray(dialogue.lines)||dialogue.lines.length!==spec.turns)throw new Error('AI返回的对话轮数不符合'+level+'要求，应为'+spec.turns+'轮。');
    const join=(parts,lang)=>parts.map(part=>String(part.text||'').trim()).join(lang==='zh'?'':' ').replace(/\s+([,.;:!?])/g,'$1').trim();
    const lines=dialogue.lines.map((line,index)=>{
      const sync=line?.sync;if(!sync)throw new Error('第'+(index+1)+'句缺少三语分段。');
      const arrays=['de','zh','en'].map(lang=>sync[lang]);
      if(arrays.some(parts=>!Array.isArray(parts)||!parts.length))throw new Error('第'+(index+1)+'句的三语分段不完整。');
      const baseIds=arrays[0].map(part=>String(part.id||''));
      if(new Set(baseIds).size!==baseIds.length||baseIds.some(id=>!id))throw new Error('第'+(index+1)+'句包含无效分段ID。');
      for(const parts of arrays.slice(1)){
        const ids=parts.map(part=>String(part.id||''));
        if(ids.length!==baseIds.length||ids.some(id=>!baseIds.includes(id))||new Set(ids).size!==ids.length)throw new Error('第'+(index+1)+'句的三语分段ID不一致。');
      }
      const cleanSync=Object.fromEntries(['de','zh','en'].map(lang=>[lang,sync[lang].map(part=>({id:String(part.id),text:String(part.text||'').trim()}))]));
      if(Object.values(cleanSync).flat().some(part=>!part.text||/[<>]/.test(part.text)))throw new Error('第'+(index+1)+'句包含空分段或HTML。');
      return {who:index%2===0?'right':'left',de:join(cleanSync.de,'de'),zh:join(cleanSync.zh,'zh'),en:join(cleanSync.en,'en'),sync:cleanSync};
    });
    const target=String(context.word||'').replace(/^(der|die|das)\s+/i,'').toLowerCase();
    if(target&&!lines.map(line=>line.de.toLowerCase()).join(' ').includes(target))throw new Error('AI生成的对话没有自然使用目标词。');
    return {level,sceneTitle:String(dialogue.sceneTitle||level+'生活场景').trim(),location:String(dialogue.location||context.location||'Deutschland · Alltag').trim(),lines};
  }
  function parseDialogueJson(content){
    const clean=String(content||'').trim().replace(/^\s*```(?:json)?\s*/i,'').replace(/\s*```\s*$/,'');
    try{return JSON.parse(clean)}catch{}
    const start=clean.indexOf('{'),end=clean.lastIndexOf('}');
    if(start>=0&&end>start){
      try{return JSON.parse(clean.slice(start,end+1))}catch{}
    }
    return null;
  }
  async function generateDialogue(context,level,{signal}={}){
    if(!DIALOGUE_LEVELS[level])throw new Error('不支持的CEFR级别。');
    const config=getConfig();if(!config.apiKey)throw Object.assign(new Error('NO_API_KEY'),{code:'NO_API_KEY'});
    const maxTokens=level==='C1'?7000:level==='B2'?4800:3200;
    let lastProblem='';
    for(let attempt=0;attempt<2;attempt++){
      let response;
      try{
        const retryNote=attempt?'\n\n上一次输出不是完整有效的JSON。请重新从头生成，确保闭合所有数组、对象和引号；不要缩短轮数，也不要输出JSON之外的文字。':'';
        response=await fetch(API_URL,{method:'POST',signal,headers:{'Content-Type':'application/json','Authorization':'Bearer '+config.apiKey},body:JSON.stringify({
          model:MODEL,
          messages:[
            {role:'system',content:'你是严谨的德语CEFR课程设计师和中英德翻译。你只输出符合指定JSON结构、适合德国真实生活的对话。'},
            {role:'user',content:dialoguePrompt(context,level)+retryNote}
          ],
          response_format:{type:'json_object'},thinking:{type:'disabled'},temperature:attempt?.45:.78,max_tokens:maxTokens,stream:false
        })});
      }catch(error){
        if(error.name==='AbortError')throw error;
        throw Object.assign(new Error('无法连接DeepSeek，请检查网络后重试。'),{code:'NETWORK'});
      }
      let data={};try{data=await response.json()}catch{}
      if(!response.ok){
        const detail=data?.error?.message||'HTTP '+response.status;
        const messages={401:'API Key无效或已失效。',402:'DeepSeek账户余额不足。',429:'请求过于频繁，请稍后再试。'};
        throw Object.assign(new Error((messages[response.status]||'DeepSeek请求失败。')+' '+detail),{code:'HTTP_'+response.status});
      }
      const choice=data?.choices?.[0],content=choice?.message?.content?.trim();
      if(!content)throw new Error('DeepSeek没有返回对话内容。');
      const parsed=parseDialogueJson(content);
      if(parsed)return {dialogue:normalizeDialogue(parsed,context,level),model:data.model||MODEL,usage:data.usage||null};
      lastProblem=choice?.finish_reason==='length'?'输出达到长度上限':'返回内容不是完整JSON';
    }
    throw new Error(level+'对话较长，AI连续两次'+lastProblem+'。请再点一次“更新本级”。');
  }
  async function explain(context,{signal}={}){
    const config=getConfig();
    if(!config.apiKey)throw Object.assign(new Error('NO_API_KEY'),{code:'NO_API_KEY'});
    let response;
    try{
      response=await fetch(API_URL,{
        method:'POST',signal,
        headers:{'Content-Type':'application/json','Authorization':'Bearer '+config.apiKey},
        body:JSON.stringify({
          model:MODEL,
          messages:[
            {role:'system',content:'你是一位擅长场景教学的德语老师。你的讲解对象是中文母语初学者；重视真实德国生活、听说训练、固定搭配和语感。只输出最终讲解，不展示思考过程。'},
            {role:'user',content:buildPrompt(context)}
          ],
          thinking:{type:'disabled'},
          temperature:.65,
          max_tokens:2200,
          stream:false
        })
      });
    }catch(error){
      if(error.name==='AbortError')throw error;
      throw Object.assign(new Error('无法连接 DeepSeek。请检查网络；如果浏览器提示跨域限制，需要通过同源代理调用 API。'),{code:'NETWORK'});
    }
    let data={};try{data=await response.json()}catch{}
    if(!response.ok){
      const detail=data?.error?.message||`HTTP ${response.status}`;
      const messages={401:'API Key 无效或已失效。',402:'DeepSeek 账户余额不足。',429:'请求过于频繁，请稍后再试。'};
      throw Object.assign(new Error((messages[response.status]||'DeepSeek 请求失败。')+' '+detail),{code:'HTTP_'+response.status});
    }
    const content=data?.choices?.[0]?.message?.content?.trim();
    if(!content)throw new Error('DeepSeek 没有返回讲解内容，请重新生成。');
    return {content,model:data.model||MODEL,usage:data.usage||null};
  }
  function escapeHtml(value){return String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
  function renderMarkdown(value){
    const safe=escapeHtml(value).replace(/\r/g,'');
    return safe.split('\n').map(line=>{
      const clean=line.trim();
      const inline=text=>text.replace(/\*\*(.+?)\*\*/g,'<strong>$1</strong>');
      if(/^###\s+/.test(clean))return '<h4>'+inline(clean.replace(/^###\s+/,''))+'</h4>';
      if(/^##\s+/.test(clean))return '<h3>'+inline(clean.replace(/^##\s+/,''))+'</h3>';
      if(/^#\s+/.test(clean))return '<h2>'+inline(clean.replace(/^#\s+/,''))+'</h2>';
      if(/^[-*]\s+/.test(clean))return '<p class="ai-teacher-item">• '+inline(clean.replace(/^[-*]\s+/,''))+'</p>';
      if(/^\d+\.\s+/.test(clean))return '<p class="ai-teacher-item">'+inline(clean)+'</p>';
      if(!clean)return '<span class="ai-teacher-space"></span>';
      return '<p>'+inline(clean)+'</p>';
    }).join('');
  }
  document.addEventListener('click',e=>{if(e.target.closest('[data-ai-settings]')){e.preventDefault();openSettings()}});
  if(location.hash==='#ai-settings')setTimeout(openSettings);
  window.AITeacher={getConfig,hasKey,openSettings,generateDialogue,explain,renderMarkdown,model:MODEL,dialogueLevels:Object.keys(DIALOGUE_LEVELS)};
})();
