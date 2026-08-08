import fs from "node:fs";
const file = "Vegetarisch-Vegan.html";
const expected = '<script src="word-scenes-custom.js"></script><script src="word-scene.js"></script>';
const replacement = '<script src="word-scenes-custom.js"></script><script src="word-scenes-vegan-a.js"></script><script src="word-scenes-vegan-b.js"></script><script src="word-scenes-vegan-c.js"></script><script src="word-scene.js"></script>';
const source = fs.readFileSync(file, "utf8");
if (!source.includes(expected)) throw new Error("Expected script sequence not found");
fs.writeFileSync(file, source.replace(expected, replacement), "utf8");
console.log("Wired", file);
