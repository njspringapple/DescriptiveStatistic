import fs from "node:fs";
import vm from "node:vm";

const targets={
  "Supermarkt.html":["word-scenes-supermarkt-a.js","word-scenes-supermarkt-b.js"],
  "Kleidung-kaufen.html":["word-scenes-kleidung-kaufen-a.js","word-scenes-kleidung-kaufen-b.js"],
  "Geld.html":["word-scenes-geld-a.js","word-scenes-geld-b.js"],
  "Post.html":["word-scenes-post-a.js","word-scenes-post-b.js"],
  "Bank-Konto.html":["word-scenes-bank-a.js","word-scenes-bank-b.js"],
  "Vertraege-Kundenservice.html":["word-scenes-vertraege-a.js","word-scenes-vertraege-b.js"],
  "Laeden-Dienstleistungen.html":["word-scenes-laeden-a.js","word-scenes-laeden-b.js"]
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
console.log(JSON.stringify({major:"Einkaufen & Geld",totalWords,totalScenes,totalLines,passed:!failed}));
if(failed)process.exitCode=1;
