import fs from "node:fs";
const file="Farben.html";
const source=fs.readFileSync(file,"utf8");
const needle='<script src="word-scenes-custom.js"></script><script src="word-scene.js"></script>';
const replacement='<script src="word-scenes-custom.js"></script><script src="word-scenes-farben.js"></script><script src="word-scene.js"></script>';
if(!source.includes(needle))throw new Error("Farben.html script insertion point not found");
fs.writeFileSync(file,source.replace(needle,replacement),"utf8");
