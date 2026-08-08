import fs from "node:fs";
const file = "Kaltgetraenke.html";
const before = '<script src="word-scenes-custom.js"></script><script src="word-scene.js"></script>';
const after = '<script src="word-scenes-custom.js"></script><script src="word-scenes-kalt-a.js"></script><script src="word-scenes-kalt-b.js"></script><script src="word-scenes-kalt-c.js"></script><script src="word-scenes-kalt-d.js"></script><script src="word-scene.js"></script>';
const source = fs.readFileSync(file, "utf8");
if (!source.includes(before)) throw new Error("Expected Kaltgetränke script line was not found; no file was changed.");
fs.writeFileSync(file, source.replace(before, after), "utf8");
