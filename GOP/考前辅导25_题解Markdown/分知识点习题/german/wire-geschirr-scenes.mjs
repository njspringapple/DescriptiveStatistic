import fs from "node:fs";
const file="Geschirr.html",expected='<script src="word-scenes-custom.js"></script><script src="word-scene.js"></script>';
const replacement='<script src="word-scenes-custom.js"></script><script src="word-scenes-geschirr-a.js"></script><script src="word-scenes-geschirr-b.js"></script><script src="word-scenes-geschirr-c.js"></script><script src="word-scene.js"></script>';
const s=fs.readFileSync(file,"utf8");if(!s.includes(expected))throw new Error("Expected script sequence not found");fs.writeFileSync(file,s.replace(expected,replacement),"utf8");console.log("Wired",file);
