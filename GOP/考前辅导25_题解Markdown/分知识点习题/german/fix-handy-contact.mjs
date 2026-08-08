import fs from "node:fs";

const file="word-scenes-handy-b.js";
const source=fs.readFileSync(file,"utf8");
const before="falls meine Frau verspätet ist, holen Sie mich zuerst an.";
const after="falls meine Frau verspätet ist, rufen Sie mich zuerst an.";
if(!source.includes(before))throw new Error("Handy contact sentence not found");
fs.writeFileSync(file,source.replace(before,after),"utf8");
