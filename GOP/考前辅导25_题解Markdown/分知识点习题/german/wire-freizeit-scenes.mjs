import fs from "node:fs";

const file="Freizeit-Hobbys.html";
const html=fs.readFileSync(file,"utf8");
const old='<script src="word-scenes-custom.js"></script><script src="word-scene.js"></script>';
const next='<script src="word-scenes-custom.js"></script><script src="word-scenes-freizeit-a.js"></script><script src="word-scenes-freizeit-b.js"></script><script src="word-scene.js"></script>';

if(html.includes(next)){
  console.log(`${file}: already wired`);
}else if(html.includes(old)){
  fs.writeFileSync(file,html.replace(old,next),"utf8");
  console.log(`${file}: wired`);
}else{
  throw new Error(`${file}: expected script sequence not found`);
}
