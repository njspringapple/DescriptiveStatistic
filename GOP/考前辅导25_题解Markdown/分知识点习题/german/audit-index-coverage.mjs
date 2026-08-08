import fs from "node:fs";
import vm from "node:vm";

const html=fs.readFileSync("index.html","utf8");
const gBody=html.match(/const G=(\[[\s\S]*?\]);\s*\/\* ={10,}/)?.[1];
const tBody=html.match(/const T=(\[[\s\S]*?\]);\s*\/\* ={10,}\s*渲染/)?.[1];
if(!gBody||!tBody)throw new Error("Cannot parse G/T from index.html");
const context={};vm.createContext(context);
vm.runInContext(`G=${gBody};T=${tBody}`,context);
const pageFiles=fs.readdirSync(".").filter(f=>f.endsWith(".html")&&/"file"\s*:/.test(fs.readFileSync(f,"utf8")));
const cards=context.T;
const groups=new Set(context.G.map(g=>g.id));
const cardFiles=new Set(cards.map(t=>t.f));
const duplicateFiles=[...cardFiles].filter(f=>cards.filter(t=>t.f===f).length>1);
const missingCards=pageFiles.filter(f=>!cardFiles.has(f));
const missingPages=cards.filter(t=>!fs.existsSync(t.f)).map(t=>t.f);
const invalidGroups=cards.filter(t=>!groups.has(t.g)).map(t=>({file:t.f,group:t.g}));
const countMismatches=[];
for(const card of cards){
  if(!fs.existsSync(card.f))continue;
  const source=fs.readFileSync(card.f,"utf8");
  const json=source.match(/window\.PAGE=(\{[\s\S]*?\})<\/script>/)?.[1];
  if(!json)continue;
  const page=JSON.parse(json);
  if(page.words.length!==card.w)countMismatches.push({file:card.f,index:card.w,page:page.words.length});
}
const result={groups:context.G.length,cards:cards.length,pageFiles:pageFiles.length,totalWords:cards.reduce((s,t)=>s+t.w,0),missingCards,missingPages,duplicateFiles,invalidGroups,countMismatches};
result.passed=!missingCards.length&&!missingPages.length&&!duplicateFiles.length&&!invalidGroups.length&&!countMismatches.length&&cards.length===pageFiles.length;
console.log(JSON.stringify(result));
if(!result.passed)process.exitCode=1;
