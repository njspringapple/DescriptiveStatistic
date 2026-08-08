import fs from "node:fs";
const file="word-scenes-flugreise-gepaeck-a.js";
const before=fs.readFileSync(file,"utf8");
const oldText='Maßgeblich ist bei diesem <strong>Fluggesellschaft</strong>-Wechsel die konkrete Buchung; speichere die Bestätigung als Nachweis.';
const newText='Maßgeblich ist bei diesem Wechsel der <strong>Fluggesellschaft</strong> die konkrete Buchung; speichere die Bestätigung als Nachweis.';
if(!before.includes(oldText))throw new Error("Expected dialogue not found");
fs.writeFileSync(file,before.replace(oldText,newText),"utf8");
