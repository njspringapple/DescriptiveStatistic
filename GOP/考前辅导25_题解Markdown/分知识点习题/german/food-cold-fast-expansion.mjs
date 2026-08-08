import fs from "node:fs";

const W = (text) => text.trim().split("\n").filter(Boolean).map((line) => {
  const [de, zh, en, icon] = line.split("|");
  return [de, zh, en, "", icon];
});

const pages = [
  {
    g: "essen",
    no: 70,
    file: "Kaltgetraenke.html",
    de: "Kaltgetränke & Getränkemarkt",
    zh: "冷饮 · 即饮饮料 · 饮料市场 · 瓶罐押金",
    en: "Cold drinks & drinks market",
    icons: ["🥤"],
    words: W(`
das Kaltgetränk|冷饮|cold drink|🥤
das Erfrischungsgetränk|清凉饮料 / 软饮|refreshment / soft drink|🥤
der Softdrink|软饮料|soft drink|🥤
die zuckerfreie Cola|无糖可乐|sugar-free cola|🥤
die Orangenlimonade|橙味汽水|orange lemonade|🍊
die Zitronenlimonade|柠檬汽水|lemon lemonade|🍋
die Fassbrause|德式麦芽果味汽水|German malt soft drink|🍺
das Tonic Water|汤力水|tonic water|🫧
das Bitter Lemon|苦柠檬汽水|bitter lemon|🍋
der Energy-Drink|能量饮料|energy drink|⚡
das Sportgetränk|运动饮料|sports drink|🏃
das isotonische Getränk|等渗饮料|isotonic drink|💧
der Eiskaffee|冰咖啡 / 德式咖啡冰淇淋饮|iced coffee|🧊
der Iced Latte|冰拿铁|iced latte|🧋
der Milchshake|奶昔|milkshake|🥛
der Bubble Tea|珍珠奶茶|bubble tea|🧋
der Slush|冰沙饮料|slush drink|🧊
das Radler|啤酒柠檬汽水混合饮料|shandy|🍺
das alkoholfreie Radler|无酒精啤酒柠檬饮|alcohol-free shandy|🍺
die Saftschorle|果汁气泡水|juice spritzer|🫧
der Multivitaminsaft|复合维生素果汁|multivitamin juice|🧃
der Traubensaft|葡萄汁|grape juice|🍇
der Getränkemarkt|饮料专卖超市|drinks market|🏪
der Pfand|瓶罐押金|deposit|♻️
die Pfandflasche|押金瓶|deposit bottle|🍾
die Mehrwegflasche|可重复使用瓶|returnable bottle|🔁
die Einwegflasche|一次性回收瓶|single-use bottle|♻️
die Getränkedose|饮料罐|drinks can|🥫
der Sechserträger|六瓶装提篮|six-pack carrier|📦
eisgekühlt|冰镇的|ice-cold|🧊
mit Eiswürfeln|加冰块|with ice cubes|🧊
ohne Eis|不加冰|without ice|🚫
`)
  },
  {
    g: "essen",
    no: 71,
    file: "Fastfood-Lieferservice.html",
    de: "Fast Food & Lieferservice",
    zh: "快餐 · 汉堡 · 披萨 · 外卖配送",
    en: "Fast food & delivery",
    icons: ["🍔"],
    words: W(`
das Fast Food|快餐|fast food|🍔
das Schnellrestaurant|快餐店|fast-food restaurant|🏪
die Fast-Food-Kette|连锁快餐品牌|fast-food chain|🔗
die Filiale|分店|branch|📍
der Burger|汉堡|burger|🍔
der Cheeseburger|芝士汉堡|cheeseburger|🍔
der Chickenburger|鸡肉汉堡|chicken burger|🍗
der Veggie-Burger|素食汉堡|veggie burger|🌱
das Burgerbrötchen|汉堡面包胚|burger bun|🍞
das Patty|汉堡肉饼 / 素食饼|patty|🥩
die Pommes|薯条|chips / fries|🍟
die Chicken-Nuggets|鸡块|chicken nuggets|🍗
der Wrap|卷饼|wrap|🌯
der Döner|土耳其烤肉夹饼|döner kebab|🥙
die Dönerbox|烤肉盒|döner box|🥡
die Falafel|炸鹰嘴豆丸|falafel|🧆
die Pizza|披萨|pizza|🍕
der Pizzarand|披萨边|pizza crust|🍕
der Belag|披萨配料 / 覆盖料|topping|🧀
die Extrazutat|额外配料|extra topping|➕
die Pizzabrötchen|披萨面包球|pizza rolls|🥖
der Dip|蘸酱|dip|🥣
das Bestellterminal|自助点餐机|self-order kiosk|🖥️
die Selbstbedienung|自助服务|self-service|🙋
die Bestellnummer|订单号 / 取餐号|order number|🔢
die Ausgabe|取餐处|collection counter|📦
hier essen|堂食|eat in|🍽️
zum Mitnehmen|外带|to take away|🥡
vorbestellen|提前下单|pre-order|📱
abholen|到店自取|collect|🛍️
liefern lassen|叫外卖配送|have delivered|🛵
die Abholbestellung|自取订单|collection order|🛍️
die Lieferbestellung|配送订单|delivery order|🛵
die Lieferadresse|配送地址|delivery address|🏠
die Liefergebühr|配送费|delivery fee|💶
der Mindestbestellwert|最低起送金额|minimum order value|🧾
die Lieferzeit|配送时间|delivery time|⏱️
der Gutscheincode|优惠码|voucher code|🏷️
die Bestellung ändern|修改订单|change the order|✏️
die Bestellung stornieren|取消订单|cancel the order|❌
`)
  }
];

const root = new URL(".", import.meta.url);
const template = fs.readFileSync(new URL("Konserven-Vorrat.html", root), "utf8");
for (const page of pages) {
  let out = template.replace(/<title>.*?<\/title>/s, `<title>${page.de.replaceAll("&", "&amp;")}</title>`);
  out = out.replace(
    /<script>window\.PAGE=.*?<\/script>/s,
    `<script>window.PAGE=${JSON.stringify(page).replaceAll("</script>", "<\\/script>")}</script>`
  );
  fs.writeFileSync(new URL(page.file, root), out, "utf8");
}

let index = fs.readFileSync(new URL("index.html", root), "utf8");
const start = "/* FOOD_CONVENIENCE_START */";
const end = "/* FOOD_CONVENIENCE_END */";
const rows = pages.map((page) =>
  `{g:${JSON.stringify(page.g)},de:${JSON.stringify(page.de)},cn:${JSON.stringify(page.zh)},en:${JSON.stringify(page.en)},w:${page.words.length},f:${JSON.stringify(page.file)},ok:true,ic:\`<text x="12" y="16" text-anchor="middle" font-size="13" fill="currentColor" stroke="none">${page.icons[0]}</text>\`}`
).join(",\n");
const block = `${start}\n${rows}\n${end}\n`;

if (index.includes(start)) {
  index = index.replace(
    /\/\* FOOD_CONVENIENCE_START \*\/[\s\S]*?\/\* FOOD_CONVENIENCE_END \*\/\n?/,
    block
  );
} else {
  index = index.replace("/* LIFE_EXPANSION_END */", `,\n${block}/* LIFE_EXPANSION_END */`);
}

const totalThemes = Array.from(index.matchAll(/\{g:[^\n]+?f:/g)).length;
const totalWords = Array.from(index.matchAll(/w:(\d+),f:/g)).reduce((sum, match) => sum + Number(match[1]), 0);
index = index
  .replace(/<b id="sT">\d+<\/b>/, `<b id="sT">${totalThemes}</b>`)
  .replace(/<b id="sW">[\d.,]+<\/b>/, `<b id="sW">${totalWords}</b>`)
  .replace(/<span id="pTxt">\d+ \/ \d+ fertig<\/span>/, `<span id="pTxt">${totalThemes} / ${totalThemes} fertig</span>`);
fs.writeFileSync(new URL("index.html", root), index, "utf8");

console.log(`Added ${pages.length} categories with ${pages.reduce((sum, page) => sum + page.words.length, 0)} terms.`);
