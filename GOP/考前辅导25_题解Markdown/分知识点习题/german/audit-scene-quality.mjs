import fs from "node:fs";
import vm from "node:vm";

const pages=process.argv.slice(2);
if(!pages.length)throw new Error("Usage: node audit-scene-quality.mjs PAGE...");
const sandbox={window:{WORD_SCENE_CUSTOM:{}}};vm.createContext(sandbox);
const loaded=new Set();
for(const page of pages){
  const html=fs.readFileSync(page,"utf8");
  const scripts=[...html.matchAll(/<script src="([^"]+)"><\/script>/g)].map(match=>match[1])
    .filter(file=>/^word-scenes-.+\.js$/.test(file));
  for(const file of scripts)if(!loaded.has(file)){
    vm.runInContext(fs.readFileSync(file,"utf8"),sandbox,{filename:file});
    loaded.add(file);
  }
}
const seenGerman=new Map(),duplicateGerman=[],sceneFingerprints=new Map(),duplicateScenes=[];
let sceneCount=0,lineCount=0,failed=false;
for(const page of pages){
  const html=fs.readFileSync(page,"utf8");
  const match=html.match(/window\.PAGE=(\{.*?\})<\/script>/s);
  const words=JSON.parse(match[1]).words.map(row=>row[0].replace(/^(der|die|das)\s+/,""));
  const scenes=sandbox.window.WORD_SCENE_CUSTOM[page]||{};
  const locations=new Set();
  for(const [word,scene] of Object.entries(scenes)){
    sceneCount++;locations.add(scene.location);
    const fingerprint=scene.lines.map(line=>line.de.replace(/<[^>]+>/g,"").trim()).join(" | ");
    if(sceneFingerprints.has(fingerprint))duplicateScenes.push([sceneFingerprints.get(fingerprint),`${page}:${word}`]);
    else sceneFingerprints.set(fingerprint,`${page}:${word}`);
    for(const line of scene.lines){
      lineCount++;
      const de=line.de.replace(/<[^>]+>/g,"").replace(/\s+/g," ").trim();
      if(seenGerman.has(de))duplicateGerman.push([seenGerman.get(de),`${page}:${word}`,de]);
      else seenGerman.set(de,`${page}:${word}`);
    }
  }
  const missing=words.filter(word=>!scenes[word]);
  console.log(JSON.stringify({page,words:words.length,scenes:Object.keys(scenes).length,
    distinctLocations:locations.size,missing}));
  if(missing.length)failed=true;
}
console.log(JSON.stringify({sceneCount,lineCount,duplicateGerman,duplicateScenes,passed:!failed&&!duplicateGerman.length&&!duplicateScenes.length}));
if(failed||duplicateGerman.length||duplicateScenes.length)process.exitCode=1;
