import fs from "node:fs";
const file="Urlaub-Ausfluege.html";
let html=fs.readFileSync(file,"utf8");
html=html.replace(/\],"no":72\};\s*<\/script>/,'],"no":72}</script>');
fs.writeFileSync(file,html,"utf8");
