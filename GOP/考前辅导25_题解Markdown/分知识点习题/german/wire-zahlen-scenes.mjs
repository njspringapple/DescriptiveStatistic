import fs from "node:fs";
const file="Zahlen.html";
const html=fs.readFileSync(file,"utf8");
const marker='<script src="word-scenes-zahlen.js"></script>';
if(!html.includes(marker)){
  const anchor='<script src="word-scenes-custom.js"></script>';
  if(!html.includes(anchor))throw new Error("word-scenes-custom.js anchor missing");
  fs.writeFileSync(file,html.replace(anchor,`${anchor}${marker}`),"utf8");
}
