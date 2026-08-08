import fs from "node:fs";
import vm from "node:vm";
const pageFile="Freundschaft-Beziehungen.html";
const pageText=fs.readFileSync(pageFile,"utf8");
const match=pageText.match(/window\.PAGE=(\{.*?\})<\/script>/s);
if(!match)throw new Error("PAGE data not found");
const page=JSON.parse(match[1]);
const context={window:{}};
vm.createContext(context);
for(const file of ["word-scenes-freundschaft-a.js","word-scenes-freundschaft-b.js"]){
  vm.runInContext(fs.readFileSync(file,"utf8"),context,{filename:file});
}
const scenes=context.window.WORD_SCENE_CUSTOM[page.file]||{};
const normalize=word=>word.replace(/^(der|die|das)\s+/,"");
const words=page.words.map(row=>normalize(row[0]));
const missing=words.filter(word=>!scenes[word]);
const extra=Object.keys(scenes).filter(word=>!words.includes(word));
const bad=Object.entries(scenes).filter(([,scene])=>
  !scene.scene||!scene.location||!scene.prop||!Array.isArray(scene.lines)||
  scene.lines.length!==4||scene.lines.some(line=>
    !line.who||!line.de||!line.zh||!line.en||!line.de.includes("<strong>")
  )
).map(([word])=>word);
const lines=Object.values(scenes).reduce((sum,scene)=>sum+scene.lines.length,0);
console.log(JSON.stringify({words:words.length,scenes:Object.keys(scenes).length,lines,missing,extra,bad},null,2));
if(words.length!==28||missing.length||extra.length||bad.length)process.exit(1);
