import fs from "node:fs";
import vm from "node:vm";

const indexHtml=fs.readFileSync("index.html","utf8");
const gBody=indexHtml.match(/const G=(\[[\s\S]*?\]);\s*\/\* ={10,}/)?.[1];
const tBody=indexHtml.match(/const T=(\[[\s\S]*?\]);\s*\/\* ={10,}\s*渲染/)?.[1];
if(!gBody||!tBody)throw new Error("Cannot parse index groups/topics");
const indexContext={};vm.createContext(indexContext);
vm.runInContext(`G=${gBody};T=${tBody}`,indexContext);

const sceneContext={window:{WORD_SCENE_CUSTOM:{}}};vm.createContext(sceneContext);
const loaded=new Set();
for(const card of indexContext.T){
  if(!fs.existsSync(card.f))continue;
  const html=fs.readFileSync(card.f,"utf8");
  for(const match of html.matchAll(/<script src="([^"]+)"><\/script>/g)){
    const script=match[1];
    if((script==="word-scenes-custom.js"||/^word-scenes-.+\.js$/.test(script))&&!loaded.has(script)&&fs.existsSync(script)){
      vm.runInContext(fs.readFileSync(script,"utf8"),sceneContext,{filename:script});
      loaded.add(script);
    }
  }
}

vm.runInContext(fs.readFileSync("word-scene.js","utf8"),sceneContext,{filename:"word-scene.js"});
const autoSyncLine=sceneContext.window.WordScene.autoSyncLine;

function pageWords(file){
  const html=fs.readFileSync(file,"utf8");
  const page=html.match(/window\.PAGE\s*=(\{.*?\})<\/script>/s)?.[1];
  if(page)return JSON.parse(page).words.map(row=>row[0].replace(/^(der|die|das)\s+/,""));
  const data=html.match(/const D=(\[[\s\S]*?\]);\s*\n\s*\/\*/)?.[1]||html.match(/const D=(\[[\s\S]*?\]);/)?.[1];
  if(!data)throw new Error(`No PAGE or D vocabulary data in ${file}`);
  const ctx={};vm.createContext(ctx);vm.runInContext(`D=${data}`,ctx,{filename:file});
  return ctx.D.map(row=>row.w);
}

const clean=s=>String(s||"").replace(/<[^>]+>/g,"").replace(/\s+/g," ").trim();
const germanSeen=new Map(),sceneSeen=new Map();
const duplicateGerman=[],duplicateScenes=[],pages=[];
const presetDialogueBlocks=[...loaded].reduce((count,script)=>count+(fs.readFileSync(script,"utf8").match(/\blines\s*:/g)?.length||0),0);
let totalWords=0,totalScenes=0,totalLines=0,dynamicScenes=0;
for(const card of indexContext.T){
  if(!fs.existsSync(card.f)){pages.push({page:card.f,missingPage:true});continue}
  const pageHtml=fs.readFileSync(card.f,"utf8");
  const aiAssets=pageHtml.includes('<link rel="stylesheet" href="ai-teacher.css">')&&pageHtml.includes('<script src="ai-teacher.js"></script>')&&pageHtml.indexOf('<script src="ai-teacher.js"></script>')<pageHtml.indexOf('<script src="word-scene.js"></script>');
  const words=pageWords(card.f);
  const scenes=sceneContext.window.WORD_SCENE_CUSTOM[card.f]||{};
  const missing=words.filter(w=>!scenes[w]);
  const extra=Object.keys(scenes).filter(w=>!words.includes(w));
  const malformed=Object.entries(scenes).filter(([,s])=>!s.scene||!s.location||!s.prop||(!s.aiDialogue&&(!Array.isArray(s.lines)||s.lines.length!==4||s.lines.some(l=>!l.who||!l.de||!l.zh||!l.en)))).map(([w])=>w);
  const malformedSync=Object.entries(scenes).filter(([,scene])=>!scene.aiDialogue&&scene.lines.some(line=>{const sync=line.sync||autoSyncLine(line),counts=[sync.de?.length,sync.zh?.length,sync.en?.length];return !counts[0]||!counts.every(count=>count===counts[0])||[...sync.de,...sync.zh,...sync.en].some(part=>!part.id||!String(part.text||"").trim())})).map(([word])=>word);
  const locations=words.filter(w=>scenes[w]).map(w=>scenes[w].location);
  for(const word of words)if(scenes[word]){
    const scene=scenes[word];if(scene.aiDialogue){dynamicScenes++;continue}
    const sceneKey=scene.lines.map(l=>clean(l.de)).join(" || ");
    if(sceneSeen.has(sceneKey))duplicateScenes.push([sceneSeen.get(sceneKey),`${card.f}:${word}`]);else sceneSeen.set(sceneKey,`${card.f}:${word}`);
    for(const line of scene.lines){
      const key=clean(line.de);
      if(germanSeen.has(key))duplicateGerman.push([germanSeen.get(key),`${card.f}:${word}`,key]);else germanSeen.set(key,`${card.f}:${word}`);
    }
  }
  totalWords+=words.length;totalScenes+=words.length-missing.length;
  totalLines+=words.filter(w=>scenes[w]).reduce((n,w)=>n+(scenes[w].lines?.length||0),0);
  pages.push({page:card.f,indexWords:card.w,words:words.length,scenes:words.length-missing.length,lines:words.filter(w=>scenes[w]).reduce((n,w)=>n+(scenes[w].lines?.length||0),0),distinctLocations:new Set(locations).size,aiAssets,missing,extra,malformed,malformedSync,countMatches:card.w===words.length});
}
const failures=pages.filter(p=>p.missingPage||p.missing?.length||p.extra?.length||p.malformed?.length||p.malformedSync?.length||!p.aiAssets||p.countMatches===false||p.distinctLocations!==p.scenes);
const summary={groups:indexContext.G.length,pages:indexContext.T.length,aiReadyPages:pages.filter(p=>p.aiAssets).length,loadedSceneScripts:loaded.size,totalWords,totalScenes,dynamicScenes,totalLines,presetDialogueBlocks,duplicateGerman,duplicateScenes,failures,passed:!failures.length&&!duplicateGerman.length&&!duplicateScenes.length&&totalWords===totalScenes&&dynamicScenes===totalWords&&totalLines===0&&presetDialogueBlocks===0};
console.log(JSON.stringify(summary));
if(!summary.passed)process.exitCode=1;
