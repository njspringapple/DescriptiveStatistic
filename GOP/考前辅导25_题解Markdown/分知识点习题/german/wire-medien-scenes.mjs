import fs from "node:fs";

const page="Medien.html";
let html=fs.readFileSync(page,"utf8");
const anchor='<script src="word-scenes-custom.js"></script>';
const scripts=`${anchor}<script src="word-scenes-medien-a.js"></script><script src="word-scenes-medien-b.js"></script>`;
if(!html.includes("word-scenes-medien-a.js")){
  if(!html.includes(anchor))throw new Error("scene script anchor not found");
  html=html.replace(anchor,scripts);
  fs.writeFileSync(page,html,"utf8");
}
