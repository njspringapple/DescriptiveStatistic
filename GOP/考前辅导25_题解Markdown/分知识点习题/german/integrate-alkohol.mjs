import fs from "node:fs";
function once(s,n,r,l){const c=s.split(n).length-1;if(c!==1)throw new Error(`${l}: ${c}`);return s.replace(n,r)}
let index=fs.readFileSync("index.html","utf8");
index=once(index,
  " {id:'wohnen',  de:'Wohnen & Haushalt'",
  " {id:'alkohol', de:'Alkohol & Trinkkultur', cn:'酒类 · 饮酒文化',c:'#8C4F43',desc:'看懂酒标、在酒吧自然交流，也能遵守年龄规则并安全拒酒、回家和求助。'},\n {id:'wohnen',  de:'Wohnen & Haushalt'",
  "alcohol group");
const cards=`
,/* ALKOHOL_START */
{g:"alkohol",de:"Bier, Wein & Spirituosen",cn:"啤酒 · 葡萄酒 · 烈酒",en:"Beer, wine & spirits",w:34,f:"Bier-Wein-Spirituosen.html",ok:true,ic:\`<path d="M6 4h9l-1 16H7z" fill="currentColor" fill-opacity=".12"/><path d="M6 4h9l-1 16H7zM7 10h7"/><path d="M15 7h2a3 3 0 0 1 0 6h-3"/>\`},
{g:"alkohol",de:"Bar & Kneipe",cn:"酒吧 · 小酒馆 · 安全夜生活",en:"Bar, pub & safe nights out",w:30,f:"Bar-Kneipe.html",ok:true,ic:\`<path d="M5 4h14l-5 7v7h3v2H7v-2h3v-7z" fill="currentColor" fill-opacity=".12"/><path d="M5 4h14l-5 7v7h3v2H7v-2h3v-7z"/><path d="M8 7h8"/>\`},
{g:"alkohol",de:"Alkohol · Regeln & Sicherheit",cn:"年龄规则 · 健康 · 急救",en:"Alcohol rules & safety",w:30,f:"Alkohol-Regeln-Sicherheit.html",ok:true,ic:\`<path d="M12 3 21 7v5c0 5-3.8 8-9 9-5.2-1-9-4-9-9V7z" fill="currentColor" fill-opacity=".12"/><path d="M12 3 21 7v5c0 5-3.8 8-9 9-5.2-1-9-4-9-9V7z"/><path d="M12 7v6M12 17h.01"/>\`}
/* ALKOHOL_END */`;
index=once(index,"\n/* FOOD_CONVENIENCE_END */",`${cards}\n/* FOOD_CONVENIENCE_END */`,"alcohol cards");
fs.writeFileSync("index.html",index,"utf8");
