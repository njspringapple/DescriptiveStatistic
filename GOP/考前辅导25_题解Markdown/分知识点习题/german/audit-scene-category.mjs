import fs from "node:fs";
import vm from "node:vm";

const [page,...files]=process.argv.slice(2);
if(!page||!files.length)throw new Error("Usage: node audit-scene-category.mjs PAGE SCENE_FILE...");
const html=fs.readFileSync(page,"utf8");
const match=html.match(/window\.PAGE=(\{.*?\})<\/script>/s);
if(!match)throw new Error(`PAGE data missing in ${page}`);
const words=JSON.parse(match[1]).words.map(row=>row[0].replace(/^(der|die|das)\s+/,""));
const sandbox={window:{WORD_SCENE_CUSTOM:{}}};
vm.createContext(sandbox);
for(const file of files)vm.runInContext(fs.readFileSync(file,"utf8"),sandbox,{filename:file});
const scenes=sandbox.window.WORD_SCENE_CUSTOM[page]||{};
const missing=words.filter(word=>!scenes[word]);
const extra=Object.keys(scenes).filter(word=>!words.includes(word));
const malformed=Object.entries(scenes).filter(([,scene])=>
  !scene.scene||!scene.location||!scene.prop||!Array.isArray(scene.lines)||scene.lines.length!==4||
  scene.lines.some(line=>!line.who||!line.de||!line.zh||!line.en)
).map(([word])=>word);
const result={page,words:words.length,scenes:Object.keys(scenes).length,
  lines:Object.values(scenes).reduce((sum,scene)=>sum+scene.lines.length,0),
  missing,extra,malformed,passed:!(missing.length||extra.length||malformed.length)};
console.log(JSON.stringify(result));
if(!result.passed)process.exitCode=1;
