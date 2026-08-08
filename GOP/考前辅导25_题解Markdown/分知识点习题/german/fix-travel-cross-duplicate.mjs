import fs from "node:fs";
const file="word-scenes-unterkunft-buchung-a.js";
let source=fs.readFileSync(file,"utf8");
const old='{who:"right",de:"Ich brauche für die Dienstreise ein ruhiges <strong>Einzelzimmer</strong> mit Schreibtisch.",zh:"我出差需要一间安静且带书桌的单人间。",en:"I need a quiet single room with a desk for my business trip."},';
const next='{who:"right",de:"Für die Messewoche suche ich ein <strong>Einzelzimmer</strong>, möglichst zum Innenhof und mit einem richtigen Schreibtisch.",zh:"展会那周我想订一间单人房，最好朝内院并配有合适的书桌。",en:"For the trade-fair week I am looking for a single room, preferably facing the courtyard and with a proper desk."},';
if(!source.includes(old))throw new Error("target dialogue not found");
source=source.replace(old,next);
fs.writeFileSync(file,source,"utf8");
