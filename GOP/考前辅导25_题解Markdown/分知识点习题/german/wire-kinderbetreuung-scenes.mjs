import fs from "node:fs";
const file="Kinderbetreuung.html";
const expected='<script src="word-scenes-custom.js"></script><script src="word-scene.js"></script>';
const replacement='<script src="word-scenes-custom.js"></script><script src="word-scenes-kinderbetreuung-a.js"></script><script src="word-scenes-kinderbetreuung-b.js"></script><script src="word-scene.js"></script>';
const s=fs.readFileSync(file,"utf8");
if(s.includes(replacement)){
  console.log("Already wired",file);
}else{
  if(!s.includes(expected))throw new Error("Expected script sequence not found");
  fs.writeFileSync(file,s.replace(expected,replacement),"utf8");
  console.log("Wired",file);
}
