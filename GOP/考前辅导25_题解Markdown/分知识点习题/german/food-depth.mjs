import fs from 'node:fs';
const W=s=>s.trim().split('\n').map(line=>{const [de,zh,en,icon]=line.split('|').map(x=>x.trim());return [de,zh,en,'',icon]});
const U={
'Fleisch.html':{de:'Fleisch & Geflügel',zh:'肉类 · 禽肉 · 肉制品',en:'Meat & poultry',icons:['🥩'],words:W(`
das Fleisch|肉类|meat|🍖
das Rindfleisch|牛肉|beef|🐄
das Schweinefleisch|猪肉|pork|🐖
das Kalbfleisch|小牛肉|veal|🐄
das Lammfleisch|羊肉|lamb|🐑
das Wildfleisch|野味肉|game meat|🦌
das Hackfleisch|肉末|minced meat|🥩
gemischtes Hackfleisch|混合肉末|mixed mince|🥩
das Gulasch|炖肉块|goulash meat|🍲
das Steak|牛排|steak|🥩
das Schnitzel|肉排|schnitzel|🍖
das Kotelett|带骨肉排|chop|🍖
der Braten|烤肉|roasting joint|🍖
die Roulade|德式肉卷|beef roulade|🥩
die Leber|肝|liver|🫀
das Hähnchen|鸡|chicken|🐔
die Hähnchenbrust|鸡胸肉|chicken breast|🍗
die Hähnchenkeule|鸡腿|chicken leg|🍗
das Putenfleisch|火鸡肉|turkey meat|🦃
die Putenbrust|火鸡胸肉|turkey breast|🦃
die Ente|鸭|duck|🦆
die Gans|鹅|goose|🪿
die Fleischtheke|肉类柜台|meat counter|🧑‍🍳
der Metzger|男肉贩 / 屠夫|butcher|👨‍🍳
die Metzgerin|女肉贩|butcher|👩‍🍳
mariniert|腌制好的|marinated|🫙
paniert|裹面包屑的|breaded|🍞
mager|瘦的|lean|✅
durchwachsen|肥瘦相间的|marbled|🥩
das Bio-Fleisch|有机肉|organic meat|🌿`)},
'Getraenke.html':{words:W(`
das Wasser|水|water|💧
das Leitungswasser|自来水|tap water|🚰
das Mineralwasser|矿泉水|mineral water|💦
Wasser mit Kohlensäure|有气水|sparkling water|🫧
Wasser ohne Kohlensäure|无气水|still water|💧
der Saft|果汁|juice|🧃
der Orangensaft|橙汁|orange juice|🍊
der Apfelsaft|苹果汁|apple juice|🍎
die Apfelschorle|苹果汽水|apple spritzer|🍎
der Smoothie|果昔|smoothie|🥤
die Limonade|汽水|lemonade|🍋
die Cola|可乐|cola|🥤
die Spezi|可乐橙汁混合饮料|cola-orange drink|🥤
der Eistee|冰茶|iced tea|🧋
die Milch|牛奶|milk|🥛
der Kaffee|咖啡|coffee|☕
der Filterkaffee|滴滤咖啡|filter coffee|☕
der Espresso|浓缩咖啡|espresso|☕
der Cappuccino|卡布奇诺|cappuccino|☕
der Tee|茶|tea|🫖
der Kräutertee|花草茶|herbal tea|🌿
der Kakao|可可饮料|cocoa|🍫
das Bier|啤酒|beer|🍺
das alkoholfreie Bier|无酒精啤酒|alcohol-free beer|🍺
der Wein|葡萄酒|wine|🍷
der Rotwein|红葡萄酒|red wine|🍷
der Weißwein|白葡萄酒|white wine|🥂
der Sekt|起泡酒|sparkling wine|🍾
die Flasche|瓶|bottle|🍾
der Kasten|整箱饮料|crate|📦`)},
'Restaurant.html':{words:W(`
das Restaurant|餐厅|restaurant|🍽️
die Gaststätte|餐馆|inn|🏠
das Café|咖啡馆|café|☕
der Biergarten|啤酒花园|beer garden|🍺
der Tisch|桌子|table|🪑
die Reservierung|预订|reservation|📅
die Speisekarte|菜单|menu|📋
die Getränkekarte|酒水单|drinks menu|🍷
die Tageskarte|今日菜单|daily menu|📅
der Kellner|男服务员|waiter|👨‍🍳
die Kellnerin|女服务员|waitress|👩‍🍳
bestellen|点餐|to order|✍️
die Vorspeise|前菜|starter|🥗
das Hauptgericht|主菜|main course|🍲
die Beilage|配菜|side dish|🍚
der Nachtisch|甜点|dessert|🍰
das Menü|套餐|set menu|📋
vegetarisch|素食的|vegetarian|🥬
vegan|纯素的|vegan|🌱
glutenfrei|无麸质的|gluten-free|🌾
die Allergie|过敏|allergy|⚠️
scharf|辣的|spicy|🌶️
durchgebraten|全熟的|well done|🔥
die Rechnung|账单|bill|🧾
getrennt zahlen|分开付款|to pay separately|💳
zusammen zahlen|一起付款|to pay together|💳
das Trinkgeld|小费|tip|💶
einpacken lassen|要求打包|to ask for takeaway packing|🥡`)},
'Geschirr.html':{words:W(`
der Teller|盘子|plate|🍽️
der tiefe Teller|汤盘|soup plate|🥣
die Tasse|杯子|cup|☕
der Becher|马克杯|mug|🥤
das Glas|玻璃杯|glass|🥛
die Schüssel|碗 / 大钵|bowl|🥣
die Gabel|叉子|fork|🍴
das Messer|刀|knife|🔪
der Löffel|勺子|spoon|🥄
der Teelöffel|茶匙|teaspoon|🥄
der Topf|锅|pot|🍲
die Pfanne|平底锅|frying pan|🍳
der Deckel|盖子|lid|🫙
das Schneidebrett|砧板|chopping board|🪵
das Sieb|滤网|sieve|🕸️
der Schneebesen|打蛋器|whisk|🥚
der Pfannenwender|锅铲|spatula|🍳
die Reibe|擦丝器|grater|🧀
der Dosenöffner|开罐器|tin opener|🥫
der Flaschenöffner|开瓶器|bottle opener|🍾
die Küchenwaage|厨房秤|kitchen scales|⚖️
der Messbecher|量杯|measuring jug|🥛
die Frischhaltedose|保鲜盒|food container|📦
die Alufolie|铝箔|aluminium foil|🪙
das Backpapier|烘焙纸|baking paper|📜
der Kochlöffel|木勺|wooden spoon|🥄`)},
'Gewuerze.html':{words:W(`
das Salz|盐|salt|🧂
der Pfeffer|胡椒|pepper|🌶️
der Zucker|糖|sugar|🍬
das Mehl|面粉|flour|🌾
das Öl|食用油|oil|🫗
das Olivenöl|橄榄油|olive oil|🫒
das Sonnenblumenöl|葵花籽油|sunflower oil|🌻
der Essig|醋|vinegar|🍶
der Balsamico|香醋|balsamic vinegar|🍶
die Butter|黄油|butter|🧈
der Knoblauch|大蒜|garlic|🧄
die Zwiebel|洋葱|onion|🧅
der Ingwer|姜|ginger|🫚
das Basilikum|罗勒|basil|🌿
die Petersilie|欧芹|parsley|🌿
der Schnittlauch|细香葱|chives|🌿
der Dill|莳萝|dill|🌿
der Rosmarin|迷迭香|rosemary|🌿
der Thymian|百里香|thyme|🌿
der Zimt|肉桂|cinnamon|🫙
das Paprikapulver|红椒粉|paprika powder|🌶️
das Currypulver|咖喱粉|curry powder|🍛
die Sojasoße|酱油|soy sauce|🍶
der Senf|芥末酱|mustard|🟡
der Ketchup|番茄酱|ketchup|🍅
die Mayonnaise|蛋黄酱|mayonnaise|🥚
die Brühe|高汤|stock|🥣
die Gewürzmischung|混合香料|spice blend|🫙`)},
'Supermarkt.html':{words:W(`
der Supermarkt|超市|supermarket|🛒
der Discounter|折扣超市|discount supermarket|🏷️
der Einkaufswagen|购物车|shopping trolley|🛒
der Einkaufskorb|购物篮|shopping basket|🧺
das Regal|货架|shelf|🗄️
die Abteilung|商品分区|department|📍
die Kühltheke|冷藏柜台|chilled counter|🧊
die Tiefkühltruhe|冷冻柜|freezer cabinet|❄️
die Frischetheke|生鲜柜台|fresh food counter|🥩
die Kasse|收银台|checkout|💳
die Selbstbedienungskasse|自助收银台|self-checkout|🤳
das Kassenband|收银传送带|checkout belt|➖
der Warentrenner|商品分隔条|checkout divider|▰
der Kassenbon|购物小票|receipt|🧾
das Sonderangebot|特价商品|special offer|🏷️
der Rabatt|折扣|discount|％
die Kundenkarte|会员卡|loyalty card|💳
der Pfandbon|退瓶凭条|deposit voucher|🎫
die Packung|一包 / 一盒|packet|📦
die Flasche|一瓶|bottle|🍾
die Dose|一罐|tin|🥫
das Glas|一玻璃罐|jar|🫙
der Becher|杯装容器|tub|🥣
die Tüte|袋|bag|🛍️
das Stück|件 / 块|piece|🧩
das Kilo|公斤|kilogram|⚖️
das Gramm|克|gram|⚖️
wiegen|称重|to weigh|⚖️
ausverkauft|售罄|sold out|❌
das Haltbarkeitsdatum|保质日期|best-before date|📅`)}}
const root=new URL('.',import.meta.url),indexPath=new URL('index.html',root);let index=fs.readFileSync(indexPath,'utf8');
for(const [file,u] of Object.entries(U)){
 const path=new URL(file,root),s=fs.readFileSync(path,'utf8'),m=s.match(/<script>window\.PAGE=(.*?)<\/script>/s);if(!m)throw new Error(`PAGE missing: ${file}`);
 const p=JSON.parse(m[1]);Object.assign(p,u);const out=s.replace(/<title>.*?<\/title>/s,`<title>${p.de.replaceAll('&','&amp;')}</title>`).replace(/<script>window\.PAGE=.*?<\/script>/s,`<script>window.PAGE=${JSON.stringify(p).replaceAll('</script>','<\\/script>')}</script>`);fs.writeFileSync(path,out,'utf8');
 index=index.replace(new RegExp(`de:'[^']*',cn:'[^']*',en:'[^']*',w:\\d+,f:'${file.replace(/[.*+?^${}()|[\\]\\]/g,'\\$&')}'`),`de:'${p.de.replaceAll("'","\\'")}',cn:'${p.zh}',en:'${p.en}',w:${p.words.length},f:'${file}'`);
}
const total=Array.from(index.matchAll(/,w:(\d+),f:/g)).reduce((n,m)=>n+Number(m[1]),0);index=index.replace(/<b id="sW">[\d.,]+<\/b>/,`<b id="sW">${total}</b>`);fs.writeFileSync(indexPath,index,'utf8');console.log(`Expanded ${Object.keys(U).length} core food pages; index total ${total}.`);
