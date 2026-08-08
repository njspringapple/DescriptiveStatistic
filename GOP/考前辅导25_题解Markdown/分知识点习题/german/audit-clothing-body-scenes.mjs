import fs from "node:fs";
import vm from "node:vm";

const targets={
  "Kleidung.html":["word-scenes-kleidung-a.js","word-scenes-kleidung-b.js"],
  "Schuhe.html":["word-scenes-schuhe-a.js","word-scenes-schuhe-b.js"],
  "Koerper.html":["word-scenes-koerper-a.js","word-scenes-koerper-b.js"],
  "Arzt.html":["word-scenes-arzt-a.js","word-scenes-arzt-b.js"],
  "Koerperpflege.html":["word-scenes-koerperpflege-a.js","word-scenes-koerperpflege-b.js"],
  "Apotheke.html":["word-scenes-apotheke-a.js","word-scenes-apotheke-b.js"],
  "Versicherung-Krankenkasse.html":["word-scenes-versicherung-a.js","word-scenes-versicherung-b.js"],
  "Notfall.html":["word-scenes-notfall-a.js","word-scenes-notfall-b.js"]
};
const sandbox={window:{WORD_SCENE_CUSTOM:{}}};
vm.createContext(sandbox);
for(const files of Object.values(targets)){
  for(const file of files)vm.runInContext(fs.readFileSync(file,"utf8"),sandbox,{filename:file});
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
console.log(JSON.stringify({major:"Kleidung & Körper",totalWords,totalScenes,totalLines,passed:!failed}));
if(failed)process.exitCode=1;
