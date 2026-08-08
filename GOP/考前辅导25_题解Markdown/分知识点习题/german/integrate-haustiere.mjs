import fs from "node:fs";
function once(s,n,r,l){const c=s.split(n).length-1;if(c!==1)throw new Error(`${l}: ${c}`);return s.replace(n,r)}
let index=fs.readFileSync("index.html","utf8");
index=once(index,
  " {id:'kleidung',de:'Kleidung & Körper'",
  " {id:'haustiere',de:'Haustiere',             cn:'宠物 · 养护',    c:'#8A6C45',desc:'从领养登记、租房与公共交通，到兽医、寄养和小动物福利。'},\n {id:'kleidung',de:'Kleidung & Körper'",
  "pets group");
const cards=`
,/* HAUSTIERE_START */
{g:"haustiere",de:"Hund & Alltag",cn:"养狗 · 登记 · 外出 · 医疗",en:"Dogs in daily life",w:34,f:"Hund-Alltag.html",ok:true,ic:\`<path d="M5 12c0-4 3-7 7-7s7 3 7 7v6H5z" fill="currentColor" fill-opacity=".12"/><path d="M5 12c0-4 3-7 7-7s7 3 7 7v6H5z"/><path d="M7 7 4 4v6M17 7l3-3v6"/><circle cx="9" cy="12" r=".7"/><circle cx="15" cy="12" r=".7"/><path d="M10 15h4"/>\`},
{g:"haustiere",de:"Katze & Haltung",cn:"养猫 · 家居 · 医疗 · 照看",en:"Cats & responsible care",w:32,f:"Katze-Haltung.html",ok:true,ic:\`<path d="M6 9 5 3l4 3a8 8 0 0 1 6 0l4-3-1 6v5a6 6 0 0 1-12 0z" fill="currentColor" fill-opacity=".12"/><path d="M6 9 5 3l4 3a8 8 0 0 1 6 0l4-3-1 6v5a6 6 0 0 1-12 0z"/><path d="M9 13h.01M15 13h.01M10 16h4"/>\`},
{g:"haustiere",de:"Kleintiere & Tierbedarf",cn:"小动物 · 饲养条件 · 宠物用品",en:"Small pets & supplies",w:32,f:"Kleintiere-Tierbedarf.html",ok:true,ic:\`<ellipse cx="12" cy="14" rx="7" ry="5" fill="currentColor" fill-opacity=".12"/><ellipse cx="12" cy="14" rx="7" ry="5"/><path d="M8 10C6 5 7 3 9 3s2 4 2 7M13 10c0-3 0-7 2-7s3 2 1 7"/><circle cx="10" cy="13" r=".6"/><circle cx="14" cy="13" r=".6"/>\`}
/* HAUSTIERE_END */`;
index=once(index,"\n/* FOOD_CONVENIENCE_END */",`${cards}\n/* FOOD_CONVENIENCE_END */`,"pet cards");
fs.writeFileSync("index.html",index,"utf8");
