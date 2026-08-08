import fs from "node:fs";

const fixes=[
  {
    file:"word-scenes-bier-wein-spirituosen.js",
    from:'{who:"right",de:"Der Automat nimmt diese <strong>Pfandflasche</strong> nicht an.",zh:"机器不接受这个押金瓶。",en:"The machine will not accept this deposit bottle."}',
    to:'{who:"right",de:"Der Rückgabeautomat lehnt die <strong>Pfandflasche</strong> ab, obwohl das Mehrwegzeichen klar zu sehen ist.",zh:"退瓶机拒收这个押金瓶，尽管周转瓶标志清晰可见。",en:"The returns machine rejects the deposit bottle even though the reusable symbol is clearly visible."}'
  },
  {
    file:"word-scenes-vegan-b.js",
    from:'{who:"right",de:"Einen Cappuccino mit <strong>Hafermilch</strong>, bitte.",zh:"请来一杯燕麦奶卡布奇诺。",en:"A cappuccino with oat milk, please."}',
    to:'{who:"right",de:"Können Sie den Cappuccino vollständig mit <strong>Hafermilch</strong> zubereiten und die normale Milch weglassen?",zh:"卡布奇诺可以完全用燕麦奶制作、不加普通牛奶吗？",en:"Can you make the cappuccino entirely with oat milk and leave out the regular milk?"}'
  }
];
for(const fix of fixes){
  let source=fs.readFileSync(fix.file,"utf8");
  if(!source.includes(fix.from))throw new Error(`target not found in ${fix.file}`);
  source=source.replace(fix.from,fix.to);
  fs.writeFileSync(fix.file,source,"utf8");
}
