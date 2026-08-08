import fs from "node:fs";

const file = "Obst.html";
const before = '<script src="word-scenes-custom.js"></script><script src="word-scene.js"></script>';
const after = '<script src="word-scenes-custom.js"></script><script src="word-scenes-obst-a.js"></script><script src="word-scenes-obst-b.js"></script><script src="word-scenes-obst-c.js"></script><script src="word-scenes-obst-d.js"></script><script src="word-scene.js"></script>';
const source = fs.readFileSync(file, "utf8");

if (!source.includes(before)) {
  throw new Error("Expected Obst script line was not found; no file was changed.");
}

fs.writeFileSync(file, source.replace(before, after), "utf8");
