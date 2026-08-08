import fs from "node:fs";
import vm from "node:vm";
const pages=process.argv.slice(2);
for(const page of pages){
  const html=fs.readFileSync(page,"utf8");
  const sandbox={window:{WORD_SCENE_CUSTOM:{}}};vm.createContext(sandbox);
  for(const m of html.matchAll(/<script src="([^"]+)"><\/script>/g)){
    const file=m[1];
    if((file==="word-scenes-custom.js"||/^word-scenes-.+\.js$/.test(file))&&fs.existsSync(file))vm.runInContext(fs.readFileSync(file,"utf8"),sandbox,{filename:file});
  }
  const by={};
  for(const [word,scene] of Object.entries(sandbox.window.WORD_SCENE_CUSTOM[page]||{}))(by[scene.location]??=[]).push(word);
  console.log(JSON.stringify({page,duplicates:Object.entries(by).filter(([,words])=>words.length>1)}));
}
