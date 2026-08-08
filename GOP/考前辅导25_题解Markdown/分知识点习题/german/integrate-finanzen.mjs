import fs from "node:fs";
function once(s,n,r,label){const c=s.split(n).length-1;if(c!==1)throw new Error(`${label}: ${c}`);return s.replace(n,r)}
let index=fs.readFileSync("index.html","utf8");
index=once(index,
  " {id:'arbeit',  de:'Arbeit & Beruf'",
  " {id:'finanzen',de:'Finanzen, Investieren & Sparen',cn:'财务 · 投资',c:'#3E6C68',desc:'从家庭预算、银行账户到证券、贷款与养老——看懂风险、费用和办事材料。'},\n {id:'arbeit',  de:'Arbeit & Beruf'",
  "finance group");
index=once(index,'{g:"shopping",de:"Bank & Konto"','{g:"finanzen",de:"Bank & Konto"',"move bank");
const cards=`
,/* FINANZEN_START */
{g:"finanzen",de:"Budget & Sparen",cn:"预算 · 储蓄 · 日常财务",en:"Budgeting & saving",w:32,f:"Budget-Sparen.html",ok:true,ic:\`<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 7h8M8 11h5M8 15h3"/><path d="m14 16 2 2 4-5"/>\`},
{g:"finanzen",de:"Geldanlage & Wertpapiere",cn:"投资 · 证券 · 储蓄计划",en:"Investing & securities",w:36,f:"Geldanlage-Wertpapiere.html",ok:true,ic:\`<path d="M3 20V4M3 20h18"/><path d="m6 16 4-5 3 2 6-8"/><path d="m16 5h3v3"/>\`},
{g:"finanzen",de:"Kredit & Altersvorsorge",cn:"贷款 · 信用 · 养老保障",en:"Credit & retirement provision",w:34,f:"Kredit-Altersvorsorge.html",ok:true,ic:\`<path d="M4 9h16v11H4z" fill="currentColor" fill-opacity=".12"/><path d="M4 9h16v11H4zM2 9l10-5 10 5"/><path d="M8 12v5M12 12v5M16 12v5"/>\`}
/* FINANZEN_END */`;
index=once(index,"\n/* FOOD_CONVENIENCE_END */",`${cards}\n/* FOOD_CONVENIENCE_END */`,"finance cards");
fs.writeFileSync("index.html",index,"utf8");
for(const file of ["Bank-Konto.html","Budget-Sparen.html","Geldanlage-Wertpapiere.html","Kredit-Altersvorsorge.html"]){
  let html=fs.readFileSync(file,"utf8");
  html=html.replace(/"g":"(?:shopping|finanzen|finance)"/,'"g":"finanzen"');
  fs.writeFileSync(file,html,"utf8");
}
