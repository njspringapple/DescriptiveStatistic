import fs from "node:fs";
import vm from "node:vm";

const targets={
  "Begruessung.html":["word-scenes-begruessung-a.js","word-scenes-begruessung-b.js"],
  "Familie.html":["word-scenes-familie-a.js","word-scenes-familie-b.js"],
  "Gefuehle.html":["word-scenes-gefuehle-a.js","word-scenes-gefuehle-b.js"],
  "Termin.html":["word-scenes-termin-a.js","word-scenes-termin-b.js"],
  "Feste.html":["word-scenes-feste-a.js","word-scenes-feste-b.js"],
  "Tagesablauf.html":["word-scenes-tagesablauf-a.js","word-scenes-tagesablauf-b.js"],
  "Freizeit-Hobbys.html":["word-scenes-freizeit-a.js","word-scenes-freizeit-b.js"],
  "Sport-Fitness.html":["word-scenes-sport-a.js","word-scenes-sport-b.js"],
  "Kinderbetreuung.html":["word-scenes-kinderbetreuung-a.js","word-scenes-kinderbetreuung-b.js"],
  "Freundschaft-Beziehungen.html":["word-scenes-freundschaft-a.js","word-scenes-freundschaft-b.js"]
};
const sandbox={window:{WORD_SCENE_CUSTOM:{}}};vm.createContext(sandbox);
for(const files of Object.values(targets))for(const file of files){
  if(!fs.existsSync(file))throw new Error(`Scene file missing: ${file}`);
  vm.runInContext(fs.readFileSync(file,"utf8"),sandbox,{filename:file});
}
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
console.log(JSON.stringify({major:"Alltag & Miteinander",totalWords,totalScenes,totalLines,passed:!failed}));
if(failed)process.exitCode=1;
