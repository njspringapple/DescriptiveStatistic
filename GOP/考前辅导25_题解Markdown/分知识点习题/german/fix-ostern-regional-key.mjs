import fs from "node:fs";
const file="word-scenes-ostern-regionale-b.js";
const text=fs.readFileSync(file,"utf8");
fs.writeFileSync(file,text.replace('"regionaler Feiertag":{','"regionale Feiertag":{'),"utf8");
