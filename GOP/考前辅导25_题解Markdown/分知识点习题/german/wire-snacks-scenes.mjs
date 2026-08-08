import fs from "node:fs";
const file = "Suesses-Snacks.html";
const before = '<script src="word-scenes-custom.js"></script><script src="word-scene.js"></script>';
const after = '<script src="word-scenes-custom.js"></script><script src="word-scenes-snacks-a.js"></script><script src="word-scenes-snacks-b.js"></script><script src="word-scenes-snacks-c.js"></script><script src="word-scene.js"></script>';
const source = fs.readFileSync(file, "utf8");
if (!source.includes(before)) throw new Error("Expected Snacks script line was not found; no file was changed.");
fs.writeFileSync(file, source.replace(before, after), "utf8");
