import fs from "node:fs";
const file = "Tiefkuehl-Fertiggerichte.html";
const before = '<script src="word-scenes-custom.js"></script><script src="word-scene.js"></script>';
const after = '<script src="word-scenes-custom.js"></script><script src="word-scenes-tiefkuehl-a.js"></script><script src="word-scenes-tiefkuehl-b.js"></script><script src="word-scenes-tiefkuehl-c.js"></script><script src="word-scene.js"></script>';
const source = fs.readFileSync(file, "utf8");
if (!source.includes(before)) throw new Error("Expected Tiefkühl script line was not found; no file was changed.");
fs.writeFileSync(file, source.replace(before, after), "utf8");
