import fs from "node:fs";

const page="Computer.html";
const html=fs.readFileSync(page,"utf8");
const marker='<script src="word-scenes-custom.js"></script>';
const addition=marker+'<script src="word-scenes-computer-a.js"></script><script src="word-scenes-computer-b.js"></script>';
if(!html.includes(marker))throw new Error(`${marker} missing in ${page}`);
if(!html.includes("word-scenes-computer-a.js")){
  fs.writeFileSync(page,html.replace(marker,addition),"utf8");
}
