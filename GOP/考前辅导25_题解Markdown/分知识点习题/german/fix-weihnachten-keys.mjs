import fs from "node:fs";
const file="word-scenes-weihnachten-advent-b.js";
let text=fs.readFileSync(file,"utf8");
text=text.replace('"ersten Weihnachtstag":','"erste Weihnachtstag":');
text=text.replace('"zweiten Weihnachtstag":','"zweite Weihnachtstag":');
fs.writeFileSync(file,text,"utf8");
