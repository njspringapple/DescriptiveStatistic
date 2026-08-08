import fs from "node:fs";
const file="word-scenes-berufe-a.js";
const from="女厨师处理过敏不凭经验 improvisieren，而是与负责方确认每次食材变化。";
const to="女厨师处理过敏时不凭经验临时变通，而是与负责方确认每次食材变化。";
const source=fs.readFileSync(file,"utf8");
if(!source.includes(from))throw new Error("Expected text not found");
fs.writeFileSync(file,source.replace(from,to),"utf8");
console.log("Fixed",file);
