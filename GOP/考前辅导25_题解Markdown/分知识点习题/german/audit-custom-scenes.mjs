import fs from "node:fs";
import vm from "node:vm";

const targets = {
  "Gemuese.html": [
    "word-scenes-gemuese.js",
    "word-scenes-gemuese-rest-a.js",
    "word-scenes-gemuese-rest-b.js",
    "word-scenes-gemuese-rest-c.js"
  ],
  "Obst.html": [
    "word-scenes-obst-a.js",
    "word-scenes-obst-b.js",
    "word-scenes-obst-c.js",
    "word-scenes-obst-d.js"
  ],
  "Molkerei-Eier.html": [
    "word-scenes-molkerei-a.js",
    "word-scenes-molkerei-b.js",
    "word-scenes-molkerei-c.js"
  ],
  "Fleisch.html": [
    "word-scenes-fleisch-a.js",
    "word-scenes-fleisch-b.js",
    "word-scenes-fleisch-c.js"
  ],
  "Wurst-Aufschnitt.html": [
    "word-scenes-wurst-a.js",
    "word-scenes-wurst-b.js",
    "word-scenes-wurst-c.js"
  ],
  "Fisch-Meeresfruechte.html": [
    "word-scenes-fisch-a.js",
    "word-scenes-fisch-b.js",
    "word-scenes-fisch-c.js"
  ],
  "Suesses-Snacks.html": [
    "word-scenes-snacks-a.js",
    "word-scenes-snacks-b.js",
    "word-scenes-snacks-c.js"
  ]
};

const sandbox = { window: { WORD_SCENE_CUSTOM: {} } };
vm.createContext(sandbox);
for (const files of Object.values(targets)) {
  for (const file of files) {
    vm.runInContext(fs.readFileSync(file, "utf8"), sandbox, { filename: file });
  }
}

function pageWords(file) {
  const html = fs.readFileSync(file, "utf8");
  const pageMatch = html.match(/window\.PAGE=(\{.*?\})<\/script>/s);
  if (pageMatch) {
    const page = JSON.parse(pageMatch[1]);
    return page.words.map((row) => row[0].replace(/^(der|die|das)\s+/, ""));
  }
  return [...html.matchAll(/\bw:"([^"]+)"/g)].map((match) => match[1]);
}

let failed = false;
let sharedSceneCount = 0;
for (const file of Object.keys(targets)) {
  const words = pageWords(file);
  const scenes = sandbox.window.WORD_SCENE_CUSTOM[file] || {};
  const expected = file === "Gemuese.html"
    ? words.filter((word) => word !== "Tomate")
    : words;
  const missing = expected.filter((word) => !scenes[word]);
  const extra = Object.keys(scenes).filter((word) => !expected.includes(word));
  const malformed = Object.entries(scenes).filter(([, scene]) =>
    !scene.location ||
    !scene.prop ||
    !Array.isArray(scene.lines) ||
    scene.lines.length !== 4 ||
    scene.lines.some((line) => !line.who || !line.de || !line.zh || !line.en)
  ).map(([word]) => word);
  const locations = new Set(Object.values(scenes).map((scene) => scene.location));
  sharedSceneCount += Object.keys(scenes).length;
  console.log(JSON.stringify({
    file,
    pageWords: words.length,
    sharedScenes: Object.keys(scenes).length,
    missing,
    extra,
    malformed,
    distinctLocations: locations.size
  }));
  if (missing.length || extra.length || malformed.length) failed = true;
}

console.log(JSON.stringify({
  sharedSceneCount,
  embeddedTomatoScene: 1,
  repairScene: 1,
  actualApprovedSceneCount: sharedSceneCount + 2
}));

if (failed) process.exitCode = 1;
