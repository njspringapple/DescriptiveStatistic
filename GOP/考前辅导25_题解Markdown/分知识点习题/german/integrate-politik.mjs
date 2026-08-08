import fs from "node:fs";
function once(s,n,r,l){const c=s.split(n).length-1;if(c!==1)throw new Error(`${l}: ${c}`);return s.replace(n,r)}
let index=fs.readFileSync("index.html","utf8");
index=once(index,
  " {id:'sozial',  de:'Kommunikation & Alltag'",
  " {id:'politik', de:'Politik & Gesellschaft', cn:'政治 · 社会',    c:'#596A8A',desc:'理解德国民主、选举、议会和地方参与——看懂通知，也能表达意见。'},\n {id:'sozial',  de:'Kommunikation & Alltag'",
  "politics group");
const cards=`
,/* POLITIK_START */
{g:"politik",de:"Staat & Demokratie",cn:"国家制度 · 民主 · 基本权利",en:"State & democracy",w:34,f:"Staat-Demokratie.html",ok:true,ic:\`<path d="M3 9 12 4l9 5"/><path d="M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 18h18M4 21h16"/>\`},
{g:"politik",de:"Wahlen & Parlament",cn:"选举 · 议会 · 立法",en:"Elections & parliament",w:34,f:"Wahlen-Parlament.html",ok:true,ic:\`<rect x="5" y="10" width="14" height="10" rx="1"/><path d="M8 10 10 4h5l2 6M9 7l6 2M3 20h18"/><path d="m10 15 2 2 4-4"/>\`},
{g:"politik",de:"Kommune & Beteiligung",cn:"地方政治 · 公民参与 · 社会融入",en:"Local government & participation",w:32,f:"Kommune-Beteiligung.html",ok:true,ic:\`<circle cx="8" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20v-3c0-3 2-5 5-5s5 2 5 5v3M14 20v-2c0-2 1-4 3-4s4 2 4 4v2"/>\`}
/* POLITIK_END */`;
index=once(index,"\n/* FOOD_CONVENIENCE_END */",`${cards}\n/* FOOD_CONVENIENCE_END */`,"politics cards");
fs.writeFileSync("index.html",index,"utf8");
