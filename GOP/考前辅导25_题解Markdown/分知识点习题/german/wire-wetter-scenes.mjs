import fs from "node:fs";
const file="Wetter.html";
let html=fs.readFileSync(file,"utf8");
const anchor='<script src="word-scenes-custom.js"></script>';
const insert=anchor+'<script src="word-scenes-wetter.js"></script>';
if(!html.includes('src="word-scenes-wetter.js"')){
  if(!html.includes(anchor))throw new Error("scene script anchor missing");
  html=html.replace(anchor,insert);
  fs.writeFileSync(file,html);
}
