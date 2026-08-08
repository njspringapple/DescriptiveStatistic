import fs from "node:fs";
import vm from "node:vm";

const pages=fs.readdirSync(".").filter(file=>file.endsWith(".html")&&file!=="index.html")
  .filter(file=>/window\.PAGE\s*=/.test(fs.readFileSync(file,"utf8")));
const sandbox={window:{WORD_SCENE_CUSTOM:{}}};vm.createContext(sandbox);
const loaded=new Set();
for(const page of pages){
  const html=fs.readFileSync(page,"utf8");
  const scripts=[...html.matchAll(/<script src="([^"]+)"><\/script>/g)].map(match=>match[1])
    .filter(file=>file==="word-scenes-custom.js"||/^word-scenes-.+\.js$/.test(file));
  for(const script of scripts)if(!loaded.has(script)&&fs.existsSync(script)){
    vm.runInContext(fs.readFileSync(script,"utf8"),sandbox,{filename:script});
    loaded.add(script);
  }
}
let totalWords=0,totalScenes=0,totalLines=0,totalMissing=0,totalMalformed=0;
const incomplete=[];
for(const page of pages){
  const html=fs.readFileSync(page,"utf8");
  const match=html.match(/window\.PAGE\s*=(\{.*?\})<\/script>/s);
  if(!match)continue;
  const words=JSON.parse(match[1]).words.map(row=>row[0].replace(/^(der|die|das)\s+/,""));
  const scenes=sandbox.window.WORD_SCENE_CUSTOM[page]||{};
  const missing=words.filter(word=>!scenes[word]);
  const malformed=Object.entries(scenes).filter(([,scene])=>
    !scene.scene||!scene.location||!scene.prop||!Array.isArray(scene.lines)||scene.lines.length!==4||
    scene.lines.some(line=>!line.who||!line.de||!line.zh||!line.en)
  ).map(([word])=>word);
  totalWords+=words.length;
  totalScenes+=words.length-missing.length;
  totalMissing+=missing.length;
  totalMalformed+=malformed.length;
  totalLines+=words.filter(word=>scenes[word]).reduce((sum,word)=>sum+scenes[word].lines.length,0);
  if(missing.length||malformed.length)incomplete.push({page,words:words.length,scenes:words.length-missing.length,missing,malformed});
}
console.log(JSON.stringify({pages:pages.length,loadedSceneScripts:loaded.size,totalWords,totalScenes,totalLines,totalMissing,totalMalformed,completePages:pages.length-incomplete.length,incompletePages:incomplete.length}));
for(const result of incomplete)console.log(JSON.stringify(result));
if(process.argv.includes("--require-complete")&&(totalMissing||totalMalformed))process.exitCode=1;
