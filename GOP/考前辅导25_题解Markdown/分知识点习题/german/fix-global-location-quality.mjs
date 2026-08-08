import fs from "node:fs";
const edits=[
  ["word-scenes-brot-a.js",'location:"Café · Frühstück bestellen",prop:"🥯"','location:"Bahnhofscafé · Bagel zum Mitnehmen",prop:"🥯"'],
  ["word-scenes-getraenke-a.js",'location:"Supermarkt · Kühlregal",prop:"🥤"','location:"Biomarkt · Kühltheke für Säfte",prop:"🥤"'],
  ["word-scenes-molkerei-c.js",'scene:"market", location:"Supermarkt · Kühlregal", prop:"🧈"','scene:"market", location:"Bio-Supermarkt · Vegane Backfette vergleichen", prop:"🧈"'],
  ["word-scenes-snacks-a.js",
   '{who:"right",de:"Möchten Sie zusätzlich heiße Kirschen oder Sahne?",zh:"还要加热樱桃或奶油吗？",en:"Would you also like hot cherries or cream?"}',
   '{who:"right",de:"Zur <strong>Waffel</strong> gibt es heiße Kirschen, Apfelmus oder Sahne; was darf ich dazugeben?",zh:"华夫饼可以搭配热樱桃、苹果泥或奶油；您要加哪一种？",en:"The waffle comes with hot cherries, apple sauce or cream; what may I add?"}']
];
for(const [file,from,to] of edits){
  let source=fs.readFileSync(file,"utf8");
  if(!source.includes(from))throw new Error(`target missing in ${file}`);
  source=source.replace(from,to);
  fs.writeFileSync(file,source,"utf8");
}
