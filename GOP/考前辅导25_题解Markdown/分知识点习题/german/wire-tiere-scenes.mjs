import fs from "node:fs";
const page="Tiere.html";
let html=fs.readFileSync(page,"utf8");
if(!html.includes('src="word-scenes-tiere.js"')){
  html=html.replace('<script src="word-scene.js"></script>','<script src="word-scenes-tiere.js"></script><script src="word-scene.js"></script>');
  fs.writeFileSync(page,html,"utf8");
}
