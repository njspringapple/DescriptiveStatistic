import fs from "node:fs";
for (const file of ["word-scenes-outdoor-winter-a.js","word-scenes-outdoor-winter-b.js"]) {
  const text=fs.readFileSync(file,"utf8").replaceAll('scene:"shop"','scene:"market"');
  fs.writeFileSync(file,text,"utf8");
}
