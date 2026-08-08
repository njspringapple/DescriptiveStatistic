import fs from "node:fs";
import vm from "node:vm";

const targets={
  "Fahrzeuge.html":["word-scenes-fahrzeuge-a.js","word-scenes-fahrzeuge-b.js"],
  "Bahnhof.html":["word-scenes-bahnhof-a.js","word-scenes-bahnhof-b.js"],
  "Stadt.html":["word-scenes-stadt-a.js","word-scenes-stadt-b.js"],
  "Weg.html":["word-scenes-weg-a.js","word-scenes-weg-b.js"],
  "Reise.html":["word-scenes-reise-a.js","word-scenes-reise-b.js"],
  "Auto-Tanken.html":["word-scenes-auto-a.js","word-scenes-auto-b.js"]
};
const sandbox={window:{WORD_SCENE_CUSTOM:{}}};vm.createContext(sandbox);
for(const files of Object.values(targets))for(const file of files)
  vm.runInContext(fs.readFileSync(file,"utf8"),sandbox,{filename:file});
let failed=false,totalWords=0,totalScenes=0,totalLines=0;
for(const [page,files] of Object.entries(targets)){
  const html=fs.readFileSync(page,"utf8");
  const match=html.match(/window\.PAGE=(\{.*?\})<\/script>/s);
  if(!match)throw new Error(`PAGE data missing in ${page}`);
  const words=JSON.parse(match[1]).words.map(row=>row[0].replace(/^(der|die|das)\s+/,""));
  const scenes=sandbox.window.WORD_SCENE_CUSTOM[page]||{};
  const missing=words.filter(word=>!scenes[word]);
  const extra=Object.keys(scenes).filter(word=>!words.includes(word));
  const malformed=Object.entries(scenes).filter(([,scene])=>
    !scene.scene||!scene.location||!scene.prop||!Array.isArray(scene.lines)||scene.lines.length!==4||
    scene.lines.some(line=>!line.who||!line.de||!line.zh||!line.en)
  ).map(([word])=>word);
  const lines=Object.values(scenes).reduce((sum,scene)=>sum+scene.lines.length,0);
  totalWords+=words.length;totalScenes+=Object.keys(scenes).length;totalLines+=lines;
  console.log(JSON.stringify({page,files,words:words.length,scenes:Object.keys(scenes).length,lines,missing,extra,malformed}));
  if(missing.length||extra.length||malformed.length)failed=true;
}
console.log(JSON.stringify({major:"Unterwegs & Reisen",totalWords,totalScenes,totalLines,passed:!failed}));
if(failed)process.exitCode=1;
