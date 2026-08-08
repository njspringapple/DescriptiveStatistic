import fs from "node:fs";
const file = "Konserven-Vorrat.html";
const expected = '<script src="word-scenes-custom.js"></script><script src="word-scene.js"></script>';
const replacement = '<script src="word-scenes-custom.js"></script><script src="word-scenes-konserven-a.js"></script><script src="word-scenes-konserven-b.js"></script><script src="word-scenes-konserven-c.js"></script><script src="word-scene.js"></script>';
const source = fs.readFileSync(file, "utf8");
if (!source.includes(expected)) throw new Error("Expected script sequence not found");
fs.writeFileSync(file, source.replace(expected, replacement), "utf8");
console.log("Wired", file);
