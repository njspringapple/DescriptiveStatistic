import fs from "node:fs";
const file="audit-all-page-scenes.mjs";
let source=fs.readFileSync(file,"utf8");
source=source.replace('.filter(file=>fs.readFileSync(file,"utf8").includes("window.PAGE="));',
  '.filter(file=>/window\\.PAGE\\s*=/.test(fs.readFileSync(file,"utf8")));');
source=source.replace('const match=html.match(/window\\.PAGE=(\\{.*?\\})<\\/script>/s);',
  'const match=html.match(/window\\.PAGE\\s*=(\\{.*?\\})<\\/script>/s);');
fs.writeFileSync(file,source,"utf8");
console.log("Fixed",file);
