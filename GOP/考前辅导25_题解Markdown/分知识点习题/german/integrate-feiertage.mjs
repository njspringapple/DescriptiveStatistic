import fs from "node:fs";
function once(s,n,r,l){const c=s.split(n).length-1;if(c!==1)throw new Error(`${l}: ${c}`);return s.replace(n,r)}
let index=fs.readFileSync("index.html","utf8");
index=once(index,
  " {id:'natur',   de:'Natur, Zeit & Zahlen'",
  " {id:'feiertage',de:'Feiertage & Bräuche', cn:'节假日 · 习俗',c:'#9A604B',desc:'从法定假日与营业变化，到圣诞、复活节和地区节庆——会祝福，也会安排生活。'},\n {id:'natur',   de:'Natur, Zeit & Zahlen'",
  "holiday group");
index=once(index,"{g:'sozial',de:'Feste & Feiertage'","{g:'feiertage',de:'Feste & Feiertage'","move old holiday card");
const cards=`
,/* FEIERTAGE_START */
{g:"feiertage",de:"Feiertage & Kalender",cn:"法定假日 · 日历 · 营业与排班",en:"Public holidays & calendar",w:32,f:"Feiertage-Kalender.html",ok:true,ic:\`<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M8 3v4M16 3v4"/><path d="m8 15 2 2 5-5"/>\`},
{g:"feiertage",de:"Weihnachten & Advent",cn:"圣诞节 · 将临期 · 年末生活",en:"Christmas & Advent",w:32,f:"Weihnachten-Advent.html",ok:true,ic:\`<path d="m12 3-5 7h3l-4 6h5v5h2v-5h5l-4-6h3z" fill="currentColor" fill-opacity=".12"/><path d="m12 3-5 7h3l-4 6h5v5h2v-5h5l-4-6h3z"/>\`},
{g:"feiertage",de:"Ostern & regionale Feste",cn:"复活节 · 狂欢节 · 地区民俗",en:"Easter & regional festivals",w:32,f:"Ostern-Regionale-Feste.html",ok:true,ic:\`<ellipse cx="12" cy="13" rx="7" ry="9" fill="currentColor" fill-opacity=".12"/><ellipse cx="12" cy="13" rx="7" ry="9"/><path d="M7 10c3 2 7 2 10 0M6 15c4 2 8 2 12 0"/>\`}
/* FEIERTAGE_END */`;
index=once(index,"\n/* FOOD_CONVENIENCE_END */",`${cards}\n/* FOOD_CONVENIENCE_END */`,"holiday cards");
fs.writeFileSync("index.html",index,"utf8");
for(const file of ["Feste.html","Feiertage-Kalender.html","Weihnachten-Advent.html","Ostern-Regionale-Feste.html"]){
  let html=fs.readFileSync(file,"utf8");
  html=html.replace(/"g":"(?:sozial|feiertage|holiday)"/,'"g":"feiertage"');
  fs.writeFileSync(file,html,"utf8");
}
