import fs from "node:fs";
import vm from "node:vm";
const html=fs.readFileSync("index.html","utf8");
const body=html.match(/const T=(\[[\s\S]*?\]);\s*\/\* ={10,}\s*渲染/)?.[1];
const context={};vm.createContext(context);vm.runInContext(`T=${body}`,context);
const parsed=new Set(fs.readdirSync(".").filter(f=>f.endsWith(".html")&&/"file"\s*:/.test(fs.readFileSync(f,"utf8"))));
console.log(JSON.stringify(context.T.map(x=>x.f).filter(f=>!parsed.has(f))));
