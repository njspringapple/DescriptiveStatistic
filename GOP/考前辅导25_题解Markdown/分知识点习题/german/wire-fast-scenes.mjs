import fs from "node:fs";
const file = "Fastfood-Lieferservice.html";
const before = '<script src="word-scenes-custom.js"></script><script src="word-scene.js"></script>';
const after = '<script src="word-scenes-custom.js"></script><script src="word-scenes-fast-a.js"></script><script src="word-scenes-fast-b.js"></script><script src="word-scenes-fast-c.js"></script><script src="word-scenes-fast-d.js"></script><script src="word-scene.js"></script>';
const source = fs.readFileSync(file, "utf8");
if (!source.includes(before)) throw new Error("Expected Fast Food script line was not found; no file was changed.");
fs.writeFileSync(file, source.replace(before, after), "utf8");
