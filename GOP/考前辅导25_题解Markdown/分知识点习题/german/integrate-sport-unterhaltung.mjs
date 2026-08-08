import fs from "node:fs";

function replaceOnce(source, needle, replacement, label) {
  const count = source.split(needle).length - 1;
  if (count !== 1) throw new Error(`${label}: expected 1 match, found ${count}`);
  return source.replace(needle, replacement);
}

let index = fs.readFileSync("index.html", "utf8");
index = replaceOnce(
  index,
  " {id:'natur',   de:'Natur, Zeit & Zahlen'",
  " {id:'freizeit',de:'Sport & Unterhaltung', cn:'运动 · 娱乐',    c:'#C56A3D', desc:'从俱乐部训练、户外冬季运动到影院剧场——会参加，也会安全享受。'},\n {id:'natur',   de:'Natur, Zeit & Zahlen'",
  "new group"
);
index = replaceOnce(index, '{g:"sozial",de:"Freizeit & Hobbys"', '{g:"freizeit",de:"Freizeit & Hobbys"', "move Freizeit");
index = replaceOnce(index, '{g:"sozial",de:"Sport & Fitness"', '{g:"freizeit",de:"Sport & Fitness"', "move Sport");

const cards = `
,/* SPORT_UNTERHALTUNG_START */
{g:"freizeit",de:"Mannschaftssport & Verein",cn:"团队运动 · 足球 · 俱乐部",en:"Team sports & clubs",w:32,f:"Mannschaftssport-Verein.html",ok:true,ic:\`<circle cx="8" cy="12" r="4"/><circle cx="16" cy="12" r="4"/><path d="M11.4 9.8h1.2M11.4 14.2h1.2M12 7V5M12 19v-2"/>\`},
{g:"freizeit",de:"Outdoor & Wintersport",cn:"户外 · 骑行 · 游泳 · 冬季运动",en:"Outdoor & winter sports",w:28,f:"Outdoor-Wintersport.html",ok:true,ic:\`<path d="M3 19 9 8l3 5 3-7 6 13z" fill="currentColor" fill-opacity=".14"/><path d="M3 19 9 8l3 5 3-7 6 13z"/><path d="M5 19h14M15 6l2 2"/>\`},
{g:"freizeit",de:"Kultur & Veranstaltungen",cn:"文化 · 演出 · 观展",en:"Culture & events",w:28,f:"Kultur-Veranstaltungen.html",ok:true,ic:\`<path d="M4 5h16v14H4z" fill="currentColor" fill-opacity=".12"/><path d="M4 5h16v14H4z"/><path d="m9 9 6 3-6 3z"/><path d="M7 3v2M17 3v2"/>\`}
/* SPORT_UNTERHALTUNG_END */`;
index = replaceOnce(index, "\n/* FOOD_CONVENIENCE_END */", `${cards}\n/* FOOD_CONVENIENCE_END */`, "new cards");

index = replaceOnce(index, '<div class="st"><b>9</b><span>Lebensbereiche 场景</span></div>', '<div class="st"><b id="sG">9</b><span>Lebensbereiche 场景</span></div>', "group stat");
index = replaceOnce(index, "document.getElementById('sW').textContent=totalW.toLocaleString('de-DE');", "document.getElementById('sW').textContent=totalW.toLocaleString('de-DE');\ndocument.getElementById('sG').textContent=G.length;", "dynamic group stat");
index = index.replace("69 Themen · 9 Lebensbereiche · A1–B1", '<span id="fT">69</span> Themen · <span id="fG">9</span> Lebensbereiche · A1–B1');
index = replaceOnce(index, "document.getElementById('sG').textContent=G.length;", "document.getElementById('sG').textContent=G.length;\ndocument.getElementById('fT').textContent=T.length;\ndocument.getElementById('fG').textContent=G.length;", "dynamic footer");
fs.writeFileSync("index.html", index, "utf8");

for (const file of ["Freizeit-Hobbys.html","Sport-Fitness.html","Mannschaftssport-Verein.html","Outdoor-Wintersport.html","Kultur-Veranstaltungen.html"]) {
  let html = fs.readFileSync(file, "utf8");
  html = html.replace(/"g":"(?:sozial|sport|sport-unterhaltung)"/, '"g":"freizeit"');
  fs.writeFileSync(file, html, "utf8");
}
