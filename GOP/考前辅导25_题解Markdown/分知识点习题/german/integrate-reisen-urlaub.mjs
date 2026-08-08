import fs from "node:fs";

function once(source, needle, replacement, label) {
  const count = source.split(needle).length - 1;
  if (count !== 1) throw new Error(`${label}: expected 1 match, found ${count}`);
  return source.replace(needle, replacement);
}

let index=fs.readFileSync("index.html","utf8");
index=once(
  index,
  " {id:'shopping',de:'Einkaufen & Geld'",
  " {id:'reiseurlaub',de:'Reisen & Urlaub',       cn:'旅游 · 度假',    c:'#2F7F76', desc:'机票、行李、住宿、观光与突发变更——把一趟旅行从计划说到回家。'},\n {id:'shopping',de:'Einkaufen & Geld'",
  "travel group"
);
index=once(index,"{g:'verkehr',de:'Reise & Hotel'","{g:'reiseurlaub',de:'Reise & Hotel'","move Reise card");

const cards=`
,/* REISEN_URLAUB_START */
{g:"reiseurlaub",de:"Flugreise & Gepäck",cn:"航空 · 机场流程 · 行李问题",en:"Air travel & baggage",w:34,f:"Flugreise-Gepaeck.html",ok:true,ic:\`<path d="m3 13 7-2 4-7 2 1-2 6 6 2v2l-7-1-4 5-2-1 2-5-6 2z" fill="currentColor" fill-opacity=".14"/><path d="m3 13 7-2 4-7 2 1-2 6 6 2v2l-7-1-4 5-2-1 2-5-6 2z"/>\`},
{g:"reiseurlaub",de:"Unterkunft & Buchung",cn:"住宿 · 预订 · 入住退房",en:"Accommodation & booking",w:30,f:"Unterkunft-Buchung.html",ok:true,ic:\`<path d="M3 20V9l9-6 9 6v11"/><path d="M6 20v-7h12v7M9 13v7M15 13v7"/><path d="M2 20h20"/>\`},
{g:"reiseurlaub",de:"Urlaub & Ausflüge",cn:"度假 · 观光 · 行程安排",en:"Holidays & excursions",w:30,f:"Urlaub-Ausfluege.html",ok:true,ic:\`<circle cx="7" cy="7" r="3"/><path d="M7 1v2M1 7h2M3 3l1.4 1.4"/><path d="M3 20c3-6 6-9 9-9s5 3 9 9"/><path d="M8 20l4-5 4 5"/>\`}
/* REISEN_URLAUB_END */`;
index=once(index,"\n/* FOOD_CONVENIENCE_END */",`${cards}\n/* FOOD_CONVENIENCE_END */`,"travel cards");
fs.writeFileSync("index.html",index,"utf8");

for(const file of ["Reise.html","Flugreise-Gepaeck.html","Unterkunft-Buchung.html","Urlaub-Ausfluege.html"]){
  let html=fs.readFileSync(file,"utf8");
  html=html.replace(/"g":"(?:verkehr|reiseurlaub|reisen|travel)"/,'"g":"reiseurlaub"');
  fs.writeFileSync(file,html,"utf8");
}
