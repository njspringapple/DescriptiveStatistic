import fs from 'node:fs';
const W=s=>s.trim().split('\n').map(line=>{const [de,zh,en,icon]=line.split('|').map(x=>x.trim());return [de,zh,en,'',icon]});
const pages=[
{g:'essen',file:'Molkerei-Eier.html',de:'Milch, Käse & Eier',zh:'牛奶 · 奶制品 · 奶酪 · 鸡蛋',en:'Dairy, cheese & eggs',icons:['🥛'],words:W(`
die Milch|牛奶|milk|🥛
die Vollmilch|全脂牛奶|whole milk|🥛
die fettarme Milch|低脂牛奶|low-fat milk|🥛
die H-Milch|常温奶|long-life milk|🧃
die Frischmilch|鲜牛奶|fresh milk|🥛
die Buttermilch|酪乳|buttermilk|🥛
der Joghurt|酸奶|yoghurt|🥣
der Naturjoghurt|原味酸奶|plain yoghurt|🥣
der Fruchtjoghurt|水果酸奶|fruit yoghurt|🍓
der Quark|凝乳奶酪|quark|🥣
der Frischkäse|奶油奶酪|cream cheese|🧀
der Käse|奶酪|cheese|🧀
der Gouda|高达奶酪|Gouda|🧀
der Emmentaler|埃曼塔奶酪|Emmental|🧀
der Mozzarella|马苏里拉奶酪|mozzarella|⚪
der Feta|菲达奶酪|feta|🧀
der Hartkäse|硬质奶酪|hard cheese|🧀
der Schnittkäse|切片奶酪|sliced cheese|🧀
die Sahne|奶油|cream|🥛
die Schlagsahne|淡奶油|whipping cream|🍰
die saure Sahne|酸奶油|sour cream|🥣
der Schmand|德式酸奶油|sour cream|🥣
die Butter|黄油|butter|🧈
die Margarine|人造黄油|margarine|🧈
das Ei|鸡蛋|egg|🥚
das Freilandei|散养鸡蛋|free-range egg|🥚
das Bio-Ei|有机鸡蛋|organic egg|🥚
die Eierpackung|鸡蛋盒|egg carton|🧺
die Hafermilch|燕麦奶|oat milk|🌾
die Sojamilch|豆奶|soya milk|🫘`)},
{g:'essen',file:'Wurst-Aufschnitt.html',de:'Wurst & Aufschnitt',zh:'香肠 · 火腿 · 冷切',en:'Sausage & cold cuts',icons:['🌭'],words:W(`
die Wurst|香肠|sausage|🌭
die Bratwurst|煎烤香肠|bratwurst|🌭
die Weißwurst|白香肠|white sausage|🌭
die Currywurst|咖喱香肠|currywurst|🍛
die Bockwurst|博克香肠|bockwurst|🌭
die Wiener Würstchen|维也纳小香肠|Vienna sausage|🌭
die Rostbratwurst|烤肠|grilled sausage|🔥
die Blutwurst|血肠|blood sausage|🌭
die Leberwurst|肝肠|liver sausage|🌭
die Mettwurst|生肉香肠|Mettwurst|🌭
die Salami|萨拉米|salami|🍕
der Schinken|火腿|ham|🥓
der Kochschinken|熟火腿|cooked ham|🥓
der Rohschinken|生火腿|cured ham|🥓
der Speck|培根|bacon|🥓
der Aufschnitt|冷切拼盘|cold cuts|🍖
die Mortadella|摩泰台拉香肠|mortadella|🍖
die Fleischwurst|肉肠|meat sausage|🌭
das Mett|调味生猪肉末|seasoned raw pork|🥩
die Pastete|肉酱 / 肉派|pâté|🥧
die Wursttheke|香肠柜台|deli counter|🧑‍🍳
aufgeschnitten|切成片的|sliced|🔪
geräuchert|烟熏的|smoked|💨
vegetarischer Aufschnitt|素冷切|vegetarian cold cuts|🌱`)},
{g:'essen',file:'Fisch-Meeresfruechte.html',de:'Fisch & Meeresfrüchte',zh:'鱼类 · 海鲜 · 水产',en:'Fish & seafood',icons:['🐟'],words:W(`
der Fisch|鱼|fish|🐟
der Lachs|三文鱼|salmon|🐟
der Räucherlachs|烟熏三文鱼|smoked salmon|💨
der Thunfisch|金枪鱼|tuna|🐟
der Kabeljau|鳕鱼|cod|🐟
der Seelachs|狭鳕|pollock|🐟
die Forelle|鳟鱼|trout|🐠
der Hering|鲱鱼|herring|🐟
die Makrele|鲭鱼|mackerel|🐟
die Scholle|鲽鱼|plaice|🐟
der Zander|梭鲈|pike-perch|🐟
das Fischfilet|鱼柳|fish fillet|🔪
die Garnele|虾|prawn|🦐
die Nordseekrabbe|北海小虾|North Sea shrimp|🦐
die Krabbe|螃蟹|crab|🦀
der Hummer|龙虾|lobster|🦞
die Muschel|贝类|mussel|🦪
die Miesmuschel|青口贝|blue mussel|🦪
die Auster|牡蛎|oyster|🦪
der Tintenfisch|鱿鱼|squid|🦑
der Oktopus|章鱼|octopus|🐙
die Fischtheke|水产柜台|fish counter|🧑‍🍳
tiefgekühlt|冷冻的|frozen|❄️
grätig|多鱼刺的|bony|🦴
entgrätet|已去鱼刺的|deboned|✅
aus nachhaltiger Fischerei|来自可持续渔业|sustainably caught|🌊`)},
{g:'essen',file:'Suesses-Snacks.html',de:'Süßes & Snacks',zh:'糖果 · 巧克力 · 咸味零食',en:'Sweets & snacks',icons:['🍫'],words:W(`
die Schokolade|巧克力|chocolate|🍫
die Vollmilchschokolade|牛奶巧克力|milk chocolate|🍫
die Zartbitterschokolade|黑巧克力|dark chocolate|🍫
der Schokoriegel|巧克力棒|chocolate bar|🍫
das Bonbon|糖果|sweet|🍬
das Gummibärchen|小熊软糖|gummy bear|🐻
die Lakritze|甘草糖|liquorice|⚫
der Keks|饼干|biscuit|🍪
die Waffel|华夫饼|wafer|🧇
das Gebäck|甜点 / 糕点|pastry|🥮
die Chips|薯片|crisps|🥔
die Salzstange|咸味脆棒|pretzel stick|🥨
die Erdnussflips|花生玉米脆|peanut puffs|🥜
das Popcorn|爆米花|popcorn|🍿
die Nuss|坚果|nut|🥜
die Erdnuss|花生|peanut|🥜
die Cashewnuss|腰果|cashew|🥜
die Mandel|杏仁|almond|🌰
das Studentenfutter|混合坚果果干|trail mix|🥜
die Trockenfrüchte|果干|dried fruit|🍇
der Müsliriegel|谷物棒|cereal bar|🌾
der Cracker|薄脆饼干|cracker|🫓
der Snack|零食|snack|🍿
süß|甜的|sweet|🍬
salzig|咸的|salty|🧂
knusprig|酥脆的|crunchy|🍪
die Familienpackung|家庭装|family pack|📦
die Nascherei|甜食|treat|🍭`)},
{g:'essen',file:'Fruehstueck-Aufstriche.html',de:'Frühstück & Aufstriche',zh:'早餐 · 谷物 · 面包酱',en:'Breakfast & spreads',icons:['🥐'],words:W(`
das Frühstück|早餐|breakfast|🥐
das Müsli|什锦麦片|muesli|🥣
die Haferflocken|燕麦片|oats|🌾
die Cornflakes|玉米片|cornflakes|🌽
das Knuspermüsli|脆麦片|granola|🥣
der Porridge|燕麦粥|porridge|🥣
das Brötchen|小面包|bread roll|🥖
der Toast|吐司|toast|🍞
das Knäckebrot|脆面包|crispbread|🫓
der Zwieback|烤面包干|rusk|🍞
die Marmelade|果酱|jam|🫙
die Konfitüre|果酱|fruit preserve|🫙
der Honig|蜂蜜|honey|🍯
die Nuss-Nougat-Creme|榛子巧克力酱|chocolate spread|🍫
die Erdnussbutter|花生酱|peanut butter|🥜
der Brotaufstrich|面包酱|spread|🫙
der Kräuterfrischkäse|香草奶油奶酪|herb cream cheese|🌿
die Leberwurst|肝肠酱|liver sausage|🌭
das gekochte Ei|水煮蛋|boiled egg|🥚
das Spiegelei|煎蛋|fried egg|🍳
das Rührei|炒蛋|scrambled egg|🍳
der Kaffee|咖啡|coffee|☕
der Orangensaft|橙汁|orange juice|🍊
frühstücken|吃早餐|to have breakfast|🍽️
den Tisch decken|摆餐桌|to set the table|🍽️
der Brotbelag|面包上的配料|bread topping|🧀`)},
{g:'essen',file:'Grundnahrungsmittel.html',de:'Grundnahrungsmittel',zh:'主食 · 米面 · 豆类 · 谷物',en:'Staple foods',icons:['🍚'],words:W(`
die Nudeln|面条 / 意面|pasta|🍝
die Spaghetti|意大利细面|spaghetti|🍝
die Penne|通心粉|penne|🍝
die Vollkornnudeln|全麦意面|wholegrain pasta|🍝
der Reis|大米|rice|🍚
der Langkornreis|长粒米|long-grain rice|🍚
der Basmatireis|巴斯马蒂香米|basmati rice|🍚
der Vollkornreis|糙米|brown rice|🍚
der Couscous|库斯库斯|couscous|🥣
der Bulgur|布格麦|bulgur|🌾
die Hirse|小米|millet|🌾
der Hafer|燕麦|oats|🌾
der Weizen|小麦|wheat|🌾
der Roggen|黑麦|rye|🌾
die Linse|小扁豆|lentil|🫘
die rote Linse|红扁豆|red lentil|🫘
die Kichererbse|鹰嘴豆|chickpea|🫘
die Kidneybohne|红腰豆|kidney bean|🫘
die weiße Bohne|白豆|white bean|🫘
die Erbse|豌豆|pea|🫛
das Mehl|面粉|flour|🌾
das Weizenmehl|小麦面粉|wheat flour|🌾
das Vollkornmehl|全麦面粉|wholemeal flour|🌾
die Stärke|淀粉|starch|🥔
die Kartoffel|土豆|potato|🥔
das Kartoffelpüree|土豆泥|mashed potato|🥣
die Beilage|配菜 / 主食配菜|side dish|🍽️
das Grundnahrungsmittel|主食|staple food|🍚`)},
{g:'essen',file:'Tiefkuehl-Fertiggerichte.html',de:'Tiefkühlkost & Fertiggerichte',zh:'冷冻食品 · 方便食品 · 即食餐',en:'Frozen & convenience food',icons:['❄️'],words:W(`
die Tiefkühlkost|冷冻食品|frozen food|❄️
das Tiefkühlgemüse|冷冻蔬菜|frozen vegetables|🥦
die Tiefkühlbeeren|冷冻浆果|frozen berries|🫐
die Tiefkühlpizza|冷冻披萨|frozen pizza|🍕
die Pommes frites|炸薯条|chips|🍟
die Kroketten|炸土豆丸|croquettes|🥔
die Fischstäbchen|鱼条|fish fingers|🐟
das Eis|冰淇淋|ice cream|🍨
der Eiswürfel|冰块|ice cube|🧊
das Fertiggericht|方便餐|ready meal|🍱
die Dosensuppe|罐头汤|canned soup|🥫
die Tütensuppe|袋装速食汤|packet soup|🍲
die Instantnudeln|方便面|instant noodles|🍜
die Mikrowellenmahlzeit|微波即食餐|microwave meal|📻
die Lasagne|千层面|lasagne|🍝
die Ravioli|意式饺子|ravioli|🥟
der Flammkuchen|德式薄饼|tarte flambée|🫓
die Gemüsepfanne|什锦蔬菜锅|vegetable stir-fry|🥦
das Hähnchengericht|鸡肉餐|chicken meal|🍗
die Backware|烘焙食品|baked goods|🥐
gekühlt|冷藏的|chilled|🧊
tiefgekühlt|冷冻的|frozen|❄️
auftauen|解冻|to defrost|🌡️
aufwärmen|加热|to heat up|🔥
das Mindesthaltbarkeitsdatum|最佳食用期|best-before date|📅
das Verbrauchsdatum|食用期限|use-by date|⏳`)},
{g:'essen',file:'Konserven-Vorrat.html',de:'Konserven & Vorrat',zh:'罐头 · 干货 · 储备食品',en:'Tinned food & pantry',icons:['🥫'],words:W(`
die Konserve|罐头食品|tinned food|🥫
die Dose|罐头|tin|🥫
das Glas|玻璃罐|jar|🫙
die Dosentomate|番茄罐头|tinned tomato|🍅
der Mais|玉米罐头|sweetcorn|🌽
die Bohnenkonserve|豆类罐头|tinned beans|🫘
die Kichererbsen|鹰嘴豆|chickpeas|🫘
der Thunfisch in der Dose|金枪鱼罐头|tinned tuna|🐟
die Sardine|沙丁鱼|sardine|🐟
die Suppe|汤|soup|🍲
der Eintopf|炖菜|stew|🍲
die Brühe|高汤|stock|🥣
der Brühwürfel|浓汤块|stock cube|🧊
das Tomatenmark|番茄膏|tomato purée|🍅
die passierten Tomaten|番茄泥|sieved tomatoes|🍅
die Essiggurke|酸黄瓜|gherkin|🥒
das Sauerkraut|酸菜|sauerkraut|🥬
die Olive|橄榄|olive|🫒
das Apfelmus|苹果泥|apple sauce|🍎
das Kompott|水果煮酱|compote|🍐
der Vorrat|储备|supply|📦
der Vorratsschrank|食品储藏柜|pantry cupboard|🗄️
haltbar|耐储存的|shelf-stable|📅
geöffnet|已开封的|opened|🔓
ungeöffnet|未开封的|unopened|🔒
kühl und trocken lagern|阴凉干燥保存|store cool and dry|🧊`)},
{g:'essen',file:'Vegetarisch-Vegan.html',de:'Vegetarisch & Vegan',zh:'素食 · 纯素 · 食物替代品',en:'Vegetarian & vegan food',icons:['🌱'],words:W(`
vegetarisch|素食的|vegetarian|🥬
vegan|纯素的|vegan|🌱
pflanzlich|植物性的|plant-based|🌿
die Fleischalternative|肉类替代品|meat substitute|🌱
der Tofu|豆腐|tofu|⬜
der Räuchertofu|烟熏豆腐|smoked tofu|💨
der Tempeh|天贝|tempeh|🫘
der Seitan|面筋制品|seitan|🌾
das Sojagranulat|大豆颗粒|soya mince|🫘
der Veggie-Burger|素汉堡|veggie burger|🍔
die vegane Wurst|纯素香肠|vegan sausage|🌭
die Hafermilch|燕麦奶|oat milk|🌾
die Sojamilch|豆奶|soya milk|🫘
die Mandelmilch|杏仁奶|almond milk|🥜
der Käseersatz|奶酪替代品|cheese substitute|🧀
der Ei-Ersatz|鸡蛋替代品|egg substitute|🥚
die Hülsenfrucht|豆类|pulse|🫘
die Pflanzencreme|植物奶油|plant cream|🥛
die Zutatenliste|配料表|ingredients list|📋
tierische Zutaten|动物性配料|animal ingredients|🐄
ohne Gelatine|不含明胶|without gelatine|✅
das Vegan-Siegel|纯素认证标志|vegan label|🌱
die Allergie|过敏|allergy|⚠️
glutenfrei|无麸质的|gluten-free|🌾
laktosefrei|无乳糖的|lactose-free|🥛
Bio|有机的|organic|🌿`)},
{g:'sozial',file:'Tagesablauf.html',de:'Tagesablauf & Routinen',zh:'作息 · 日常安排 · 习惯',en:'Daily routine',icons:['⏰'],words:W(`
der Alltag|日常生活|everyday life|🏠
der Tagesablauf|每日作息|daily routine|📋
aufwachen|醒来|to wake up|⏰
aufstehen|起床|to get up|🛏️
duschen|洗澡|to shower|🚿
sich anziehen|穿衣|to get dressed|👕
frühstücken|吃早餐|to have breakfast|🥐
aus dem Haus gehen|出门|to leave home|🚪
zur Arbeit fahren|去上班|to go to work|🚆
arbeiten|工作|to work|💼
eine Pause machen|休息|to take a break|☕
Mittag essen|吃午饭|to have lunch|🍽️
einkaufen gehen|去购物|to go shopping|🛒
nach Hause kommen|回家|to come home|🏠
kochen|做饭|to cook|🍳
zu Abend essen|吃晚饭|to have dinner|🍲
aufräumen|整理|to tidy up|🧹
fernsehen|看电视|to watch TV|📺
spazieren gehen|散步|to go for a walk|🚶
sich ausruhen|休息|to rest|🛋️
ins Bett gehen|上床睡觉|to go to bed|🛏️
einschlafen|入睡|to fall asleep|😴
pünktlich|准时的|punctual|⏰
regelmäßig|规律地|regularly|🔁
manchmal|有时|sometimes|🤔
normalerweise|通常|normally|📅`)},
{g:'sozial',file:'Freizeit-Hobbys.html',de:'Freizeit & Hobbys',zh:'休闲 · 兴趣 · 外出活动',en:'Leisure & hobbies',icons:['🎨'],words:W(`
die Freizeit|空闲时间|free time|⏳
das Hobby|爱好|hobby|🎨
lesen|阅读|to read|📖
Musik hören|听音乐|to listen to music|🎵
ein Instrument spielen|演奏乐器|to play an instrument|🎸
fotografieren|摄影|to take photos|📷
malen|画画|to paint|🎨
zeichnen|素描|to draw|✏️
kochen|烹饪|to cook|🍳
backen|烘焙|to bake|🥧
gärtnern|园艺|to garden|🌱
wandern|徒步|to hike|🥾
spazieren gehen|散步|to walk|🚶
reisen|旅行|to travel|🧳
ins Kino gehen|去电影院|to go to the cinema|🎬
ins Konzert gehen|去音乐会|to go to a concert|🎤
ins Theater gehen|去剧院|to go to the theatre|🎭
Freunde treffen|见朋友|to meet friends|👥
ausgehen|外出娱乐|to go out|🌃
tanzen|跳舞|to dance|💃
spielen|玩耍|to play|🎲
das Brettspiel|桌游|board game|🎲
das Computerspiel|电脑游戏|computer game|🎮
der Verein|协会 / 俱乐部|club|👥
mitmachen|参加|to join in|🙋
sich entspannen|放松|to relax|😌`)},
{g:'sozial',file:'Sport-Fitness.html',de:'Sport & Fitness',zh:'运动 · 健身 · 俱乐部',en:'Sport & fitness',icons:['🏃'],words:W(`
der Sport|运动|sport|🏅
die Fitness|健身|fitness|💪
das Fitnessstudio|健身房|gym|🏋️
der Sportverein|体育俱乐部|sports club|👥
trainieren|训练|to train|🏋️
laufen|跑步|to run|🏃
joggen|慢跑|to jog|🏃
wandern|徒步|to hike|🥾
Rad fahren|骑自行车|to cycle|🚲
schwimmen|游泳|to swim|🏊
Fußball spielen|踢足球|to play football|⚽
Tennis spielen|打网球|to play tennis|🎾
Basketball spielen|打篮球|to play basketball|🏀
Volleyball spielen|打排球|to play volleyball|🏐
Yoga machen|做瑜伽|to do yoga|🧘
das Training|训练|training|📋
das Spiel|比赛|match|🏟️
die Mannschaft|球队|team|👥
der Trainer|男教练|coach|🧑‍🏫
die Trainerin|女教练|coach|👩‍🏫
die Mitgliedschaft|会员资格|membership|🪪
der Mitgliedsbeitrag|会员费|membership fee|💶
die Umkleide|更衣室|changing room|🚪
die Sportschuhe|运动鞋|sports shoes|👟
die Sportkleidung|运动服|sportswear|👕
sich aufwärmen|热身|to warm up|🔥
sich verletzen|受伤|to get injured|🤕
der Muskelkater|肌肉酸痛|muscle soreness|💪`)},
{g:'kleidung',file:'Apotheke.html',de:'In der Apotheke',zh:'药店 · 药物 · 用药说明',en:'At the pharmacy',icons:['💊'],words:W(`
die Apotheke|药店|pharmacy|⚕️
der Apotheker|男药剂师|pharmacist|👨‍⚕️
die Apothekerin|女药剂师|pharmacist|👩‍⚕️
das Medikament|药物|medicine|💊
die Tablette|药片|tablet|💊
die Kapsel|胶囊|capsule|💊
der Saft|药水|medicinal syrup|🧴
die Tropfen|滴剂|drops|💧
die Salbe|药膏|ointment|🧴
das Spray|喷雾剂|spray|💨
das Pflaster|创可贴|plaster|🩹
der Verband|绷带|bandage|🩹
das Schmerzmittel|止痛药|painkiller|💊
das Fiebermittel|退烧药|fever medicine|🌡️
der Hustensaft|止咳糖浆|cough syrup|🧴
das Nasenspray|鼻喷剂|nasal spray|👃
das Rezept|处方|prescription|📃
rezeptpflichtig|处方药的|prescription-only|📃
rezeptfrei|非处方的|over-the-counter|✅
die Nebenwirkung|副作用|side effect|⚠️
die Dosierung|剂量|dosage|🥄
einnehmen|服用|to take medicine|💊
zweimal täglich|每天两次|twice daily|2️⃣
vor dem Essen|饭前|before meals|🍽️
nach dem Essen|饭后|after meals|🍽️
die Packungsbeilage|药品说明书|patient leaflet|📄
die Notdienstapotheke|值班药店|emergency pharmacy|🚨
verträglich|耐受良好的|well tolerated|✅`)},
{g:'kleidung',file:'Versicherung-Krankenkasse.html',de:'Versicherung & Krankenkasse',zh:'保险 · 医保 · 报销',en:'Insurance & health fund',icons:['🛡️'],words:W(`
die Versicherung|保险|insurance|🛡️
die Krankenversicherung|医疗保险|health insurance|⚕️
die Krankenkasse|医保机构|health insurance fund|🏥
die Versichertenkarte|医保卡|health insurance card|💳
die Versicherungskarte|保险卡|insurance card|💳
die Versicherungsnummer|保险号码|insurance number|🔢
der Beitrag|保费|contribution|💶
der Zusatzbeitrag|附加保费|additional contribution|💶
die Leistung|保险待遇|benefit|✅
die Kostenübernahme|费用承担|cost coverage|💶
die Erstattung|报销|reimbursement|↩️
der Eigenanteil|自付部分|co-payment|💶
die Zuzahlung|附加自付费|co-payment|💶
die Rechnung|账单|invoice|🧾
der Antrag|申请|application|📝
die Bescheinigung|证明|certificate|📄
die Arbeitsunfähigkeitsbescheinigung|病假证明|sick note|📄
krankgeschrieben|被开病假的|signed off sick|🤒
die Haftpflichtversicherung|个人责任险|liability insurance|🛡️
die Hausratversicherung|家庭财产险|contents insurance|🏠
die Rechtsschutzversicherung|法律费用险|legal expenses insurance|⚖️
die Kfz-Versicherung|机动车保险|car insurance|🚗
versichert|已投保的|insured|✅
einen Schaden melden|报案 / 报损|to report a claim|📞
die Schadensnummer|理赔编号|claim number|🔢
die Selbstbeteiligung|免赔额|deductible|💶
die Kündigungsfrist|解约期限|notice period|📅
die Pflegeversicherung|护理保险|long-term care insurance|🧑‍⚕️`)},
{g:'kleidung',file:'Notfall.html',de:'Notfall & Hilfe',zh:'急救 · 报警 · 消防 · 求助',en:'Emergency & help',icons:['🚨'],words:W(`
der Notfall|紧急情况|emergency|🚨
der Notruf|紧急电话|emergency call|📞
die 112|急救与消防电话 112|emergency number 112|1️⃣
die 110|报警电话 110|police number 110|1️⃣
der Rettungsdienst|急救服务|emergency medical service|🚑
der Krankenwagen|救护车|ambulance|🚑
die Feuerwehr|消防队|fire brigade|🚒
die Polizei|警察|police|👮
der Unfall|事故|accident|💥
der Verkehrsunfall|交通事故|traffic accident|🚗
die Verletzung|伤势|injury|🤕
die Blutung|出血|bleeding|🩸
bewusstlos|失去意识的|unconscious|😵
atmen|呼吸|to breathe|🫁
die Erste Hilfe|急救|first aid|🩹
wiederbeleben|心肺复苏|to resuscitate|❤️
der Feuerlöscher|灭火器|fire extinguisher|🧯
der Rauchmelder|烟雾报警器|smoke detector|🚨
brennen|着火|to burn|🔥
Hilfe rufen|呼救|to call for help|📣
Wo ist der Notfall?|紧急情况在哪里？|Where is the emergency?|📍
Was ist passiert?|发生了什么？|What happened?|❓
Bleiben Sie ruhig.|请保持冷静。|Stay calm.|😌
die Adresse angeben|说明地址|to give the address|📍
der ärztliche Bereitschaftsdienst|非急诊值班医疗服务|out-of-hours medical service|116117
die 116117|医疗值班服务电话|medical on-call number|☎️`)},
{g:'shopping',file:'Bank-Konto.html',de:'Bank & Konto',zh:'银行 · 账户 · 转账',en:'Banking & accounts',icons:['🏦'],words:W(`
die Bank|银行|bank|🏦
das Girokonto|活期账户|current account|💳
das Sparkonto|储蓄账户|savings account|🐖
die IBAN|国际银行账号|IBAN|🔢
die BIC|银行识别码|BIC|🔢
die Bankkarte|银行卡|bank card|💳
die Girokarte|德国借记卡|girocard|💳
die Kreditkarte|信用卡|credit card|💳
die PIN|密码|PIN|🔒
der Geldautomat|自动取款机|cash machine|🏧
Geld abheben|取现|to withdraw cash|💶
Geld einzahlen|存钱|to deposit cash|💰
die Überweisung|银行转账|bank transfer|↗️
überweisen|转账|to transfer|📤
der Dauerauftrag|定期转账指令|standing order|🔁
das Lastschriftverfahren|自动扣款|direct debit|🔄
die Abbuchung|扣款|debit|➖
die Gutschrift|入账|credit|➕
der Kontostand|账户余额|account balance|💶
der Kontoauszug|银行对账单|bank statement|📄
die Kontoführungsgebühr|账户管理费|account fee|💶
das Onlinebanking|网上银行|online banking|💻
die Banking-App|银行应用|banking app|📱
die TAN|交易验证码|transaction code|🔐
das Dispolimit|透支额度|overdraft limit|📉
das Konto eröffnen|开户|to open an account|✅
das Konto sperren|冻结账户|to block an account|🔒
die Karte ist verloren|银行卡丢失|the card is lost|⚠️`)},
{g:'sozial',file:'Kinderbetreuung.html',de:'Kindergarten & Kinderbetreuung',zh:'托儿所 · 幼儿园 · 儿童照护',en:'Childcare & kindergarten',icons:['🧸'],words:W(`
das Kind|孩子|child|🧒
das Baby|婴儿|baby|👶
die Kita|日托机构|daycare centre|🏫
der Kindergarten|幼儿园|kindergarten|🏫
die Kinderkrippe|托儿所|nursery|👶
der Hort|课后托管|after-school care|🏫
die Tagesmutter|日托妈妈|childminder|👩
der Tagesvater|日托爸爸|childminder|👨
die Betreuung|照护|care|🤲
der Betreuungsplatz|托育名额|childcare place|🪑
die Anmeldung|报名|registration|📝
die Warteliste|等候名单|waiting list|📋
der Gutschein|托育券|voucher|🎫
die Eingewöhnung|适应期|settling-in period|🤝
die Erzieherin|女幼教|nursery teacher|👩‍🏫
der Erzieher|男幼教|nursery teacher|👨‍🏫
die Abholberechtigung|接孩子授权|collection authorisation|📄
die Abholzeit|接孩子时间|collection time|🕒
die Bringzeit|送孩子时间|drop-off time|🕗
das Mittagessen|午餐|lunch|🍽️
der Mittagsschlaf|午睡|nap|😴
die Windel|尿布|nappy|🧷
die Wechselkleidung|备用衣服|spare clothes|👕
die Brotdose|饭盒|lunch box|🍱
die Trinkflasche|水壶|drinking bottle|🍼
die Elternversammlung|家长会|parents' meeting|👥
krankmelden|请病假|to report sick|🤒
die Schließzeit|闭园时间|closure time|📅`)},
{g:'wohnen',file:'Nachbarschaft-Hausordnung.html',de:'Nachbarschaft & Hausordnung',zh:'邻里 · 楼规 · 租住礼仪',en:'Neighbours & house rules',icons:['🏘️'],words:W(`
der Nachbar|男邻居|neighbour|👨
die Nachbarin|女邻居|neighbour|👩
die Nachbarschaft|社区 / 邻里|neighbourhood|🏘️
die Hausordnung|楼规|house rules|📜
die Ruhezeit|安静时段|quiet hours|🤫
die Nachtruhe|夜间安静时间|night-time quiet|🌙
die Mittagsruhe|午间安静时间|afternoon quiet|🕛
der Lärm|噪音|noise|🔊
die Ruhestörung|扰民|noise disturbance|📢
das Treppenhaus|楼梯间|stairwell|🪜
der Hausflur|公共走廊|communal hallway|🚪
der Hausmeister|物业管理员|caretaker|🧑‍🔧
die Hausverwaltung|物业管理处|property management|🏢
die Kehrwoche|轮值清扫周|cleaning rota|🧹
der Waschkeller|公共洗衣房|laundry room|🧺
der Fahrradkeller|自行车地下室|bike cellar|🚲
der Gemeinschaftsgarten|公共花园|communal garden|🌳
die Klingel|门铃|doorbell|🔔
der Briefkasten|信箱|letterbox|📮
das Namensschild|姓名牌|nameplate|🏷️
die Haustür|楼门|front door|🚪
abschließen|锁门|to lock|🔒
lüften|通风|to air|🪟
Bescheid sagen|告知|to let someone know|💬
sich beschweren|投诉|to complain|📣
Rücksicht nehmen|体谅他人|to be considerate|🤝`)},
{g:'wohnen',file:'Muell-Recycling.html',de:'Mülltrennung & Recycling',zh:'垃圾分类 · 回收 · 押金瓶',en:'Waste sorting & recycling',icons:['♻️'],words:W(`
der Müll|垃圾|waste|🗑️
die Mülltrennung|垃圾分类|waste separation|♻️
der Restmüll|其他垃圾|residual waste|⚫
der Biomüll|厨余垃圾|organic waste|🟤
das Altpapier|废纸|waste paper|📦
die Papiertonne|纸类垃圾桶|paper bin|🔵
die Biotonne|厨余垃圾桶|organic waste bin|🟤
die Restmülltonne|其他垃圾桶|residual waste bin|⚫
die Wertstofftonne|可回收物垃圾桶|recycling bin|🟡
der Gelbe Sack|黄色回收袋|yellow recycling bag|🟡
das Altglas|废玻璃|waste glass|🍾
der Glascontainer|玻璃回收箱|glass container|🟢
das Weißglas|白色玻璃|clear glass|⚪
das Braunglas|棕色玻璃|brown glass|🟤
das Grünglas|绿色玻璃|green glass|🟢
der Sperrmüll|大件垃圾|bulky waste|🛋️
der Elektroschrott|电子垃圾|electronic waste|🔌
die Batterie|电池|battery|🔋
der Wertstoffhof|回收站|recycling centre|🏭
das Pfand|容器押金|deposit|🪙
die Pfandflasche|押金瓶|deposit bottle|🍾
der Pfandautomat|退瓶机|bottle return machine|♻️
die Einwegflasche|一次性瓶|single-use bottle|1️⃣
die Mehrwegflasche|可重复使用瓶|reusable bottle|🔁
wegwerfen|扔掉|to throw away|🗑️
recyceln|回收利用|to recycle|♻️
entsorgen|处理废弃物|to dispose of|🚮
die Abholung|垃圾清运|collection|🚛`)},
{g:'wohnen',file:'Reparatur-Handwerker.html',de:'Reparatur & Handwerker',zh:'报修 · 工匠 · 房屋故障',en:'Repairs & tradespeople',icons:['🧰'],words:W(`
die Reparatur|维修|repair|🧰
der Handwerker|工匠 / 维修工|tradesperson|🧑‍🔧
der Hausmeister|物业维修管理员|caretaker|🧑‍🔧
der Elektriker|电工|electrician|⚡
der Installateur|水暖工|plumber|🔧
der Heizungsmonteur|暖气维修工|heating engineer|♨️
der Schlüsseldienst|开锁服务|locksmith|🔑
der Maler|油漆工|painter|🎨
der Schreiner|木工|carpenter|🪚
die Werkstatt|维修店|workshop|🏭
der Termin|预约|appointment|📅
der Kostenvoranschlag|报价单|quotation|🧾
die Rechnung|账单|invoice|🧾
die Anfahrt|上门路程费|call-out journey|🚐
die Arbeitszeit|工时|labour time|⏱️
das Ersatzteil|备件|spare part|⚙️
kaputt|坏了的|broken|💥
undicht|漏水 / 漏气的|leaking|💧
verstopft|堵塞的|blocked|🚫
der Wasserhahn tropft|水龙头滴水|the tap is dripping|🚰
die Heizung funktioniert nicht|暖气不工作|the heating is not working|🥶
der Strom ist ausgefallen|停电了|the power is out|🔦
die Sicherung|保险丝 / 空开|fuse|⚡
der Wasserschaden|水损|water damage|🌊
der Schimmel|霉菌|mould|🦠
reparieren|维修|to repair|🔧
austauschen|更换|to replace|🔄
den Schaden melden|报修|to report damage|📞`)},
{g:'shopping',file:'Vertraege-Kundenservice.html',de:'Verträge & Kundenservice',zh:'合同 · 订阅 · 客服 · 解约',en:'Contracts & customer service',icons:['📄'],words:W(`
der Vertrag|合同|contract|📄
die Vertragsnummer|合同编号|contract number|🔢
die Kundennummer|客户编号|customer number|🔢
der Kundenservice|客户服务|customer service|🎧
die Hotline|客服热线|hotline|☎️
die Warteschleife|电话等待队列|hold queue|⏳
die Laufzeit|合同期限|contract term|📅
die Mindestlaufzeit|最低合同期|minimum term|📅
die Kündigungsfrist|解约通知期|notice period|⏰
die automatische Verlängerung|自动续约|automatic renewal|🔁
die Kündigung|解约|cancellation|❌
kündigen|解约|to cancel|✍️
widerrufen|撤销合同|to withdraw|↩️
der Widerruf|撤销权|withdrawal|↩️
die Bestätigung|确认|confirmation|✅
die Rechnung|账单|invoice|🧾
die Mahnung|催款函|payment reminder|⚠️
die Abbuchung|扣款|debit|➖
die Lastschrift|自动扣款|direct debit|🔄
das Abonnement|订阅|subscription|📰
der Tarif|资费套餐|plan|📊
der Anbieter|服务商|provider|🏢
der Anschluss|线路 / 接口|connection|🔌
die Störung|故障|fault|🛠️
eine Störung melden|报障|to report a fault|📞
die Reklamation|投诉 / 退换申诉|complaint|📣
sich beschweren|投诉|to complain|😠
die Gutschrift|退款入账|credit note|💶
die Erstattung|退款|refund|↩️
die Bearbeitungszeit|处理时间|processing time|⏳`)},
{g:'arbeit',file:'Aufenthalt-Behoerden.html',de:'Aufenthalt & Behörden',zh:'居留 · 外管局 · 户籍登记',en:'Residence & authorities',icons:['🛂'],words:W(`
die Ausländerbehörde|外国人管理局|foreigners authority|🏛️
das Bürgeramt|市民服务中心|citizens' office|🏛️
das Einwohnermeldeamt|居民登记处|registration office|🏛️
die Anmeldung|住址登记|registration|📝
die Meldebescheinigung|住址登记证明|registration certificate|📄
der Wohnsitz|居住地|residence|🏠
der Aufenthaltstitel|居留许可|residence permit|🪪
die Aufenthaltserlaubnis|居留许可证|residence permit|🪪
die Niederlassungserlaubnis|永久居留许可|settlement permit|✅
das Visum|签证|visa|🛂
der Reisepass|护照|passport|🛂
die Fiktionsbescheinigung|临时居留证明|temporary residence certificate|📄
die Arbeitserlaubnis|工作许可|work permit|💼
die Einbürgerung|入籍|naturalisation|🇩🇪
die Staatsangehörigkeit|国籍|nationality|🌍
der Antrag|申请|application|📝
das Formular|表格|form|📋
der Termin|预约|appointment|📅
die Unterlage|材料 / 文件|document|📄
der Nachweis|证明材料|proof|📎
das Passfoto|证件照|passport photo|📷
die Gebühr|手续费|fee|💶
die Bearbeitungszeit|办理时间|processing time|⏳
die Verlängerung|延期 / 续签|extension|🔁
verlängern|延长 / 续签|to extend|📅
beantragen|申请|to apply for|✍️
gültig|有效的|valid|✅
abgelaufen|已过期的|expired|⌛
die Verpflichtungserklärung|经济担保书|declaration of commitment|📄
der Integrationskurs|融入课程|integration course|📚`)},
{g:'verkehr',file:'Auto-Tanken.html',de:'Auto, Tanken & Panne',zh:'汽车 · 加油 · 停车 · 故障',en:'Car, fuel & breakdowns',icons:['⛽'],words:W(`
das Auto|汽车|car|🚗
der Führerschein|驾驶证|driving licence|🪪
der Fahrzeugschein|车辆行驶证|vehicle registration|📄
die Tankstelle|加油站|petrol station|⛽
das Benzin|汽油|petrol|⛽
der Diesel|柴油|diesel|⛽
bleifrei|无铅的|unleaded|✅
tanken|加油|to refuel|⛽
der Tank|油箱|fuel tank|🚗
die Zapfsäule|加油泵|fuel pump|⛽
der Reifendruck|胎压|tyre pressure|🛞
der Reifen|轮胎|tyre|🛞
die Autowäsche|洗车|car wash|🫧
der Parkplatz|停车位|parking space|🅿️
der Parkschein|停车票|parking ticket|🎫
die Parkscheibe|停车计时盘|parking disc|🅿️
das Parkhaus|停车楼|multi-storey car park|🏢
das Halteverbot|禁止停车|no stopping|🚫
die Panne|车辆故障|breakdown|⚠️
der Pannendienst|道路救援|breakdown service|🚙
das Warndreieck|三角警示牌|warning triangle|🔺
die Warnweste|反光背心|high-visibility vest|🦺
das Starthilfekabel|搭电线|jump lead|🔌
die Batterie|汽车电瓶|battery|🔋
der Abschleppdienst|拖车服务|towing service|🚛
die Werkstatt|修车厂|garage|🔧
der TÜV|车辆年检|vehicle inspection|✅
die Umweltplakette|环保车贴|emissions sticker|🟢`)},
{g:'shopping',file:'Laeden-Dienstleistungen.html',de:'Geschäfte & Dienstleistungen',zh:'商店 · 服务场所 · 营业信息',en:'Shops & services',icons:['🏪'],words:W(`
das Geschäft|商店|shop|🏪
der Laden|店铺|shop|🏬
der Supermarkt|超市|supermarket|🛒
der Discounter|折扣超市|discount supermarket|🏷️
die Drogerie|日化用品店|drugstore|🧴
die Bäckerei|面包店|bakery|🥖
die Metzgerei|肉店|butcher's|🥩
die Apotheke|药店|pharmacy|⚕️
der Kiosk|报刊亭 / 小卖部|kiosk|🏪
der Wochenmarkt|周市集|weekly market|🥕
das Kaufhaus|百货商店|department store|🏬
das Einkaufszentrum|购物中心|shopping centre|🏢
der Baumarkt|建材工具店|DIY store|🔨
das Möbelhaus|家具店|furniture store|🛋️
die Reinigung|干洗店|dry cleaner's|👔
der Waschsalon|自助洗衣店|launderette|🧺
der Friseursalon|理发店|hair salon|💇
die Änderungsschneiderei|改衣店|alterations shop|🧵
der Schlüsseldienst|锁匠|locksmith|🔑
die Postfiliale|邮局网点|post office branch|📮
die Öffnungszeit|营业时间|opening time|🕒
der Ruhetag|休息日|closing day|📅
geöffnet|营业中|open|🔓
geschlossen|已关门|closed|🔒
ausverkauft|售罄|sold out|❌
vorrätig|有库存|in stock|✅
die Selbstbedienung|自助服务|self-service|🙋
die Bedienung|人工服务|service|🧑‍💼`)},
{g:'sozial',file:'Freundschaft-Beziehungen.html',de:'Freundschaft & Beziehungen',zh:'朋友 · 伴侣 · 邀请 · 相处',en:'Friendship & relationships',icons:['🤝'],words:W(`
der Freund|男朋友 / 男性朋友|friend / boyfriend|👨
die Freundin|女朋友 / 女性朋友|friend / girlfriend|👩
die Freundschaft|友谊|friendship|🤝
der Partner|男伴侣|partner|👨
die Partnerin|女伴侣|partner|👩
das Paar|一对伴侣|couple|💑
die Beziehung|关系 / 恋爱关系|relationship|❤️
ledig|单身 / 未婚的|single|🙋
verheiratet|已婚的|married|💍
geschieden|离婚的|divorced|💔
zusammenleben|共同生活|to live together|🏠
sich kennenlernen|相识|to get to know each other|🤝
sich treffen|见面|to meet|📅
einladen|邀请|to invite|💌
die Einladung|邀请|invitation|💌
zusagen|答应参加|to accept|✅
absagen|取消 / 婉拒|to decline|❌
Bescheid sagen|告知|to let someone know|💬
sich verabreden|约定见面|to arrange to meet|📅
sich unterhalten|交谈|to chat|💬
helfen|帮助|to help|🤲
vertrauen|信任|to trust|🤝
sich entschuldigen|道歉|to apologise|🙇
sich streiten|争吵|to argue|😠
sich versöhnen|和好|to make up|🕊️
Kontakt halten|保持联系|to keep in touch|📱
zu Besuch kommen|来访|to visit|🏠
etwas gemeinsam machen|一起做某事|to do something together|👥`)},
];
const root=new URL('.',import.meta.url);
const template=fs.readFileSync(new URL('Fleisch.html',root),'utf8');
for(const [i,p] of pages.entries()){
  p.no=45+i;
  let out=template.replace(/<title>.*?<\/title>/s,`<title>${p.de.replaceAll('&','&amp;')}</title>`);
  out=out.replace(/<script>window\.PAGE=.*?<\/script>/s,`<script>window.PAGE=${JSON.stringify(p).replaceAll('</script>','<\\/script>')}</script>`);
  fs.writeFileSync(new URL(p.file,root),out,'utf8');
}
let index=fs.readFileSync(new URL('index.html',root),'utf8');
const start='/* LIFE_EXPANSION_START */',end='/* LIFE_EXPANSION_END */';
const rows=pages.map(p=>`{g:${JSON.stringify(p.g)},de:${JSON.stringify(p.de)},cn:${JSON.stringify(p.zh)},en:${JSON.stringify(p.en)},w:${p.words.length},f:${JSON.stringify(p.file)},ok:true,ic:\`<text x="12" y="16" text-anchor="middle" font-size="13" fill="currentColor" stroke="none">${p.icons[0]}</text>\`}`).join(',\n');
const block=`${start}\n${rows}\n${end}\n`;
if(index.includes(start)) index=index.replace(new RegExp('/\\* LIFE_EXPANSION_START \\*/[\\s\\S]*?/\\* LIFE_EXPANSION_END \\*/\\n?'),block);
else { const renderPos=index.indexOf('   渲染'); const closePos=index.lastIndexOf('];',renderPos); if(closePos<0)throw new Error('T array end not found'); index=index.slice(0,closePos)+','+'\n'+block+']'+index.slice(closePos+1); }
const totalThemes=44+pages.length,totalWords=Array.from(index.matchAll(/w:(\d+),f:/g)).reduce((n,m)=>n+Number(m[1]),0);
index=index.replace(/<b id="sT">\d+<\/b>/,`<b id="sT">${totalThemes}</b>`).replace(/<b id="sW">[\d.,]+<\/b>/,`<b id="sW">${totalWords}</b>`).replace(/<span id="pTxt">\d+ \/ \d+ fertig<\/span>/,`<span id="pTxt">${totalThemes} / ${totalThemes} fertig</span>`).replace(/44 Themen/g,`${totalThemes} Themen`);
fs.writeFileSync(new URL('index.html',root),index,'utf8');
console.log(`Added ${pages.length} real-life categories with ${pages.reduce((n,p)=>n+p.words.length,0)} terms.`);
