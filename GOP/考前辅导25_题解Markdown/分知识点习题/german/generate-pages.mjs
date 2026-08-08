import fs from 'node:fs';

const W=s=>s.trim().split('\n').map(line=>line.split('|').map(x=>x.trim()));
const pages=[
{no:4,file:'Fleisch.html',de:'Fleisch & Fisch',zh:'肉类与海鲜',en:'Meat & Fish',icons:['🥩','🍗','🐟','🦐'],words:W(`
das Rindfleisch|牛肉|beef
das Schweinefleisch|猪肉|pork
das Hähnchen|鸡肉 / 鸡|chicken
die Pute|火鸡|turkey
das Lammfleisch|羊肉|lamb
die Wurst|香肠|sausage
der Schinken|火腿|ham
das Hackfleisch|肉末|minced meat
das Schnitzel|炸肉排|schnitzel
das Steak|牛排|steak
der Fisch|鱼|fish
der Lachs|三文鱼|salmon
der Thunfisch|金枪鱼|tuna
die Forelle|鳟鱼|trout
die Garnele|虾|prawn
die Krabbe|螃蟹 / 小虾|crab
die Muschel|贝类|mussel
der Tintenfisch|鱿鱼|squid`)},
{no:5,file:'Getraenke.html',de:'Getränke',zh:'饮料 · 咖啡 · 酒',en:'Drinks',icons:['🥤','☕','🫖','🍷'],words:W(`
das Wasser|水|water
das Mineralwasser|矿泉水|mineral water
der Saft|果汁|juice
der Orangensaft|橙汁|orange juice
die Limonade|汽水 / 柠檬水|lemonade
die Cola|可乐|cola
die Milch|牛奶|milk
der Kaffee|咖啡|coffee
der Espresso|意式浓缩咖啡|espresso
der Cappuccino|卡布奇诺|cappuccino
der Tee|茶|tea
der Kakao|热可可|cocoa
das Bier|啤酒|beer
der Wein|葡萄酒|wine
der Rotwein|红葡萄酒|red wine
der Weißwein|白葡萄酒|white wine
der Sekt|起泡酒|sparkling wine
das Getränk|饮料|drink`)},
{no:6,file:'Restaurant.html',de:'Im Restaurant',zh:'餐厅点餐与结账',en:'At the restaurant',icons:['🍽️','📋','🥣','💶'],words:W(`
das Restaurant|餐厅|restaurant
der Tisch|桌子|table
die Speisekarte|菜单|menu
die Getränkekarte|酒水单|drinks menu
der Kellner|男服务员|waiter
die Kellnerin|女服务员|waitress
bestellen|点餐|to order
empfehlen|推荐|to recommend
die Vorspeise|前菜|starter
das Hauptgericht|主菜|main course
die Beilage|配菜|side dish
der Nachtisch|甜点|dessert
vegetarisch|素食的|vegetarian
lecker|美味的|delicious
die Rechnung|账单|bill
bezahlen|付款|to pay
das Trinkgeld|小费|tip
reservieren|预订|to reserve`)},
{no:7,file:'Geschirr.html',de:'Geschirr & Kochen',zh:'餐具与厨具',en:'Dishes & cooking',icons:['🍴','🥄','🍳','🥣'],words:W(`
der Teller|盘子|plate
die Tasse|杯子|cup
das Glas|玻璃杯|glass
die Schüssel|碗 / 大钵|bowl
die Gabel|叉子|fork
das Messer|刀|knife
der Löffel|勺子|spoon
der Teelöffel|茶匙|teaspoon
der Topf|锅|pot
die Pfanne|平底锅|frying pan
der Deckel|盖子|lid
das Schneidebrett|砧板|chopping board
der Herd|炉灶|stove
der Backofen|烤箱|oven
kochen|烹饪|to cook
braten|煎 / 炒|to fry
backen|烘焙|to bake
schneiden|切|to cut`)},
{no:8,file:'Gewuerze.html',de:'Gewürze & Zutaten',zh:'调料与配料',en:'Spices & ingredients',icons:['🧂','🌿','🫚','🫙'],words:W(`
das Salz|盐|salt
der Pfeffer|胡椒|pepper
der Zucker|糖|sugar
das Mehl|面粉|flour
das Öl|油|oil
der Essig|醋|vinegar
die Butter|黄油|butter
die Sahne|奶油|cream
das Ei|鸡蛋|egg
der Knoblauch|大蒜|garlic
die Zwiebel|洋葱|onion
der Ingwer|姜|ginger
das Basilikum|罗勒|basil
die Petersilie|欧芹|parsley
der Zimt|肉桂|cinnamon
das Gewürz|香料|spice
die Soße|酱汁|sauce
die Zutat|配料|ingredient`)},
{no:10,file:'Wohnung.html',de:'Wohnung & Räume',zh:'住房与房间',en:'Flat & rooms',icons:['🏠','🚪','🛋️','🪟'],words:W(`
die Wohnung|公寓|flat
das Haus|房子|house
das Zimmer|房间|room
das Wohnzimmer|客厅|living room
das Schlafzimmer|卧室|bedroom
das Kinderzimmer|儿童房|children's room
die Küche|厨房|kitchen
das Badezimmer|浴室|bathroom
der Flur|走廊|hallway
der Balkon|阳台|balcony
der Keller|地下室|cellar
der Dachboden|阁楼|attic
die Tür|门|door
das Fenster|窗户|window
die Wand|墙|wall
der Boden|地板|floor
die Treppe|楼梯|stairs
der Garten|花园|garden`)},
{no:11,file:'Haushalt.html',de:'Haushalt & Putzen',zh:'家务与清洁',en:'Chores & cleaning',icons:['🧹','🧽','🪣','🧺'],words:W(`
putzen|打扫|to clean
aufräumen|整理|to tidy up
staubsaugen|吸尘|to vacuum
wischen|擦洗|to mop
spülen|洗碗|to wash up
waschen|清洗|to wash
bügeln|熨烫|to iron
der Staubsauger|吸尘器|vacuum cleaner
der Besen|扫帚|broom
der Eimer|水桶|bucket
der Lappen|抹布|cleaning cloth
der Schwamm|海绵|sponge
das Waschmittel|洗衣液|detergent
der Müll|垃圾|rubbish
der Mülleimer|垃圾桶|waste bin
die Wäsche|待洗衣物|laundry
die Hausarbeit|家务|housework
sauber|干净的|clean`)},
{no:12,file:'Elektro.html',de:'Elektrogeräte',zh:'家用电器',en:'Appliances',icons:['🧺','📺','💡','🔌'],words:W(`
der Kühlschrank|冰箱|fridge
die Waschmaschine|洗衣机|washing machine
der Geschirrspüler|洗碗机|dishwasher
der Herd|炉灶|cooker
der Backofen|烤箱|oven
die Mikrowelle|微波炉|microwave
der Wasserkocher|电热水壶|kettle
die Kaffeemaschine|咖啡机|coffee machine
der Toaster|烤面包机|toaster
der Staubsauger|吸尘器|vacuum cleaner
das Bügeleisen|熨斗|iron
der Fernseher|电视机|television
die Lampe|灯|lamp
der Föhn|吹风机|hairdryer
die Steckdose|插座|socket
der Stecker|插头|plug
einschalten|打开电器|to switch on
ausschalten|关闭电器|to switch off`)},
{no:13,file:'Wohnungssuche.html',de:'Wohnungssuche',zh:'租房 · 看房 · 合同',en:'Finding a flat',icons:['🔑','🏢','📄','📐'],words:W(`
die Anzeige|房屋广告|advertisement
die Besichtigung|看房|viewing
der Vermieter|男房东|landlord
die Vermieterin|女房东|landlady
der Mieter|男租客|tenant
die Miete|房租|rent
die Kaltmiete|冷租|basic rent
die Warmmiete|暖租|rent including utilities
die Nebenkosten|附加费用|service charges
die Kaution|押金|deposit
der Mietvertrag|租赁合同|tenancy agreement
die Wohnfläche|居住面积|living space
möbliert|带家具的|furnished
zentral|位置中心的|central
ruhig|安静的|quiet
frei|空置的|available
einziehen|搬入|to move in
kündigen|解约|to give notice`)},
{no:14,file:'Kleidung.html',de:'Kleidung',zh:'服装 · 上衣下装外套',en:'Clothes',icons:['👕','👖','🧥','👗'],words:W(`
das T-Shirt|T恤|T-shirt
das Hemd|衬衫|shirt
die Bluse|女式衬衫|blouse
der Pullover|毛衣|jumper
die Jacke|夹克|jacket
der Mantel|大衣|coat
die Hose|裤子|trousers
die Jeans|牛仔裤|jeans
der Rock|半身裙|skirt
das Kleid|连衣裙|dress
der Anzug|西装|suit
die Unterwäsche|内衣|underwear
der Schlafanzug|睡衣|pyjamas
die Socke|袜子|sock
der Gürtel|腰带|belt
tragen|穿 / 戴|to wear
anziehen|穿上|to put on
ausziehen|脱下|to take off`)},
{no:15,file:'Schuhe.html',de:'Schuhe & Accessoires',zh:'鞋帽与配饰',en:'Shoes & accessories',icons:['👟','👜','🧢','⌚'],words:W(`
der Schuh|鞋|shoe
der Turnschuh|运动鞋|trainer
der Stiefel|靴子|boot
die Sandale|凉鞋|sandal
der Hausschuh|拖鞋|slipper
der Absatz|鞋跟|heel
die Tasche|包|bag
der Rucksack|双肩包|backpack
die Handtasche|手提包|handbag
der Hut|帽子|hat
die Mütze|便帽|cap
der Schal|围巾|scarf
der Handschuh|手套|glove
die Brille|眼镜|glasses
die Sonnenbrille|太阳镜|sunglasses
die Uhr|手表|watch
der Schmuck|首饰|jewellery
die Kette|项链|necklace`)},
{no:16,file:'Koerper.html',de:'Der Körper',zh:'身体部位',en:'The body',icons:['🧍','👁️','🖐️','🦵'],words:W(`
der Kopf|头|head
das Gesicht|脸|face
das Haar|头发|hair
das Auge|眼睛|eye
das Ohr|耳朵|ear
die Nase|鼻子|nose
der Mund|嘴|mouth
der Zahn|牙齿|tooth
der Hals|脖子 / 喉咙|neck
die Schulter|肩膀|shoulder
der Arm|手臂|arm
die Hand|手|hand
der Finger|手指|finger
der Bauch|肚子|belly
der Rücken|背部|back
das Bein|腿|leg
das Knie|膝盖|knee
der Fuß|脚|foot`)},
{no:17,file:'Arzt.html',de:'Beim Arzt',zh:'看病 · 症状 · 药',en:'At the doctor',icons:['🩺','🌡️','💊','🩹'],words:W(`
der Arzt|男医生|doctor
die Ärztin|女医生|doctor
der Patient|男病人|patient
die Praxis|诊所|surgery
der Termin|预约|appointment
die Krankheit|疾病|illness
der Schmerz|疼痛|pain
das Fieber|发烧|fever
der Husten|咳嗽|cough
der Schnupfen|感冒 / 流鼻涕|cold
die Erkältung|感冒|common cold
die Tablette|药片|tablet
das Medikament|药物|medicine
das Rezept|处方|prescription
untersuchen|检查|to examine
wehtun|疼|to hurt
krank|生病的|ill
gesund|健康的|healthy`)},
{no:18,file:'Koerperpflege.html',de:'Körperpflege',zh:'洗护与化妆品',en:'Personal care',icons:['🧴','🪥','🧼','🪞'],words:W(`
die Seife|肥皂|soap
das Shampoo|洗发水|shampoo
das Duschgel|沐浴露|shower gel
die Zahnbürste|牙刷|toothbrush
die Zahnpasta|牙膏|toothpaste
das Handtuch|毛巾|towel
der Kamm|梳子|comb
die Bürste|刷子|brush
der Rasierer|剃须刀|razor
die Creme|乳霜|cream
das Deo|除臭剂|deodorant
das Parfüm|香水|perfume
die Kosmetik|化妆品|cosmetics
der Lippenstift|口红|lipstick
der Spiegel|镜子|mirror
duschen|淋浴|to shower
sich waschen|洗漱|to wash oneself
sich rasieren|刮胡子|to shave`)},
{no:19,file:'Fahrzeuge.html',de:'Fahrzeuge',zh:'交通工具',en:'Vehicles',icons:['🚗','🚲','🚌','✈️'],words:W(`
das Auto|汽车|car
der Bus|公交车|bus
die Straßenbahn|有轨电车|tram
die U-Bahn|地铁|underground
die S-Bahn|市郊铁路|suburban train
der Zug|火车|train
das Fahrrad|自行车|bicycle
das Motorrad|摩托车|motorbike
der Lastwagen|卡车|lorry
das Taxi|出租车|taxi
das Flugzeug|飞机|aeroplane
das Schiff|船|ship
die Fähre|渡轮|ferry
der Roller|踏板车|scooter
fahren|驾驶 / 乘坐|to travel
einsteigen|上车|to get on
aussteigen|下车|to get off
umsteigen|换乘|to change`)},
{no:20,file:'Bahnhof.html',de:'Bahnhof & Flughafen',zh:'车站与机场',en:'Station & airport',icons:['🚉','🎫','🧳','🛫'],words:W(`
der Bahnhof|火车站|station
der Flughafen|机场|airport
der Bahnsteig|站台|platform
das Gleis|轨道 / 站台号|track
die Haltestelle|车站|stop
die Fahrkarte|车票|ticket
der Fahrplan|时刻表|timetable
die Abfahrt|出发|departure
die Ankunft|到达|arrival
die Verspätung|晚点|delay
der Schalter|柜台|counter
der Koffer|行李箱|suitcase
das Gepäck|行李|luggage
der Pass|护照|passport
die Bordkarte|登机牌|boarding pass
einchecken|办理值机|to check in
abfahren|发车|to depart
ankommen|到达|to arrive`)},
{no:21,file:'Stadt.html',de:'In der Stadt',zh:'城市与公共场所',en:'In the city',icons:['🏙️','🏛️','🏥','🌳'],words:W(`
die Stadt|城市|city
das Stadtzentrum|市中心|city centre
die Straße|街道|street
der Platz|广场|square
der Park|公园|park
das Rathaus|市政厅|town hall
die Bibliothek|图书馆|library
das Museum|博物馆|museum
das Theater|剧院|theatre
das Kino|电影院|cinema
die Apotheke|药店|pharmacy
das Krankenhaus|医院|hospital
die Bank|银行|bank
die Post|邮局|post office
die Polizei|警察局 / 警察|police
die Kirche|教堂|church
der Markt|市场|market
die Fußgängerzone|步行街|pedestrian zone`)},
{no:22,file:'Weg.html',de:'Weg & Richtung',zh:'问路与方向',en:'Directions',icons:['🧭','⬅️','➡️','🗺️'],words:W(`
der Weg|道路 / 路线|way
die Richtung|方向|direction
links|左边|left
rechts|右边|right
geradeaus|直走|straight ahead
hier|这里|here
dort|那里|there
vorne|前面|at the front
hinten|后面|at the back
gegenüber|在对面|opposite
neben|在旁边|next to
zwischen|在……之间|between
an der Ecke|在拐角处|at the corner
die Kreuzung|十字路口|crossroads
die Ampel|红绿灯|traffic light
abbiegen|转弯|to turn
überqueren|穿过|to cross
sich verlaufen|迷路|to get lost`)},
{no:23,file:'Reise.html',de:'Reise & Hotel',zh:'旅行与住宿',en:'Travel & hotel',icons:['🧳','🏨','🗺️','📸'],words:W(`
die Reise|旅行|journey
der Urlaub|假期|holiday
das Reiseziel|旅行目的地|destination
das Hotel|酒店|hotel
das Einzelzimmer|单人间|single room
das Doppelzimmer|双人间|double room
die Rezeption|前台|reception
der Zimmerschlüssel|房间钥匙|room key
die Übernachtung|住宿一晚|overnight stay
das Frühstück|早餐|breakfast
die Reservierung|预订|reservation
buchen|预订|to book
stornieren|取消预订|to cancel
übernachten|过夜|to stay overnight
der Reiseführer|旅行指南|guidebook
die Sehenswürdigkeit|景点|sight
der Ausflug|短途旅行|excursion
die Jugendherberge|青年旅舍|youth hostel`)},
{no:24,file:'Supermarkt.html',de:'Im Supermarkt',zh:'超市 · 包装与量词',en:'At the supermarket',icons:['🛒','🧃','🥫','⚖️'],words:W(`
der Supermarkt|超市|supermarket
der Einkaufswagen|购物车|shopping trolley
der Einkaufskorb|购物篮|shopping basket
das Regal|货架|shelf
die Kasse|收银台|checkout
der Kassenbon|小票|receipt
das Sonderangebot|特价商品|special offer
die Packung|一包 / 一盒|packet
die Flasche|一瓶|bottle
die Dose|一罐|tin
das Glas|一玻璃罐|jar
das Stück|件 / 块|piece
das Kilo|公斤|kilogram
das Gramm|克|gram
wiegen|称重|to weigh
einkaufen|购物|to shop`)},
{no:25,file:'Kleidung-kaufen.html',de:'Kleidung kaufen',zh:'试衣 · 尺码 · 退换',en:'Clothes shopping',icons:['🛍️','👚','🏷️','🧾'],words:W(`
das Kaufhaus|百货商店|department store
die Umkleidekabine|试衣间|changing room
die Größe|尺码|size
die Farbe|颜色|colour
der Preis|价格|price
das Etikett|标签|label
der Rabatt|折扣|discount
anprobieren|试穿|to try on
passen|合身|to fit
stehen|适合 / 好看|to suit
zu groß|太大|too large
zu klein|太小|too small
zu eng|太紧|too tight
umtauschen|换货|to exchange
zurückgeben|退货|to return
die Quittung|收据|receipt`)},
{no:26,file:'Geld.html',de:'Geld & Bezahlen',zh:'钱 · 支付 · 价格',en:'Money & paying',icons:['💶','💳','🪙','🏧'],words:W(`
das Geld|钱|money
der Euro|欧元|euro
der Cent|欧分|cent
der Schein|纸币|banknote
die Münze|硬币|coin
das Bargeld|现金|cash
die Karte|银行卡|card
die Kreditkarte|信用卡|credit card
das Konto|账户|account
der Geldautomat|自动取款机|cash machine
bezahlen|付款|to pay
kosten|价值 / 花费|to cost
bar|用现金|in cash
kontaktlos|非接触式的|contactless
günstig|实惠的|inexpensive
teuer|昂贵的|expensive`)},
{no:27,file:'Post.html',de:'Post & Paket',zh:'邮局与快递',en:'Post & parcels',icons:['📮','✉️','📦','🏷️'],words:W(`
die Post|邮局|post office
der Brief|信|letter
der Briefumschlag|信封|envelope
die Briefmarke|邮票|stamp
die Postkarte|明信片|postcard
das Paket|包裹|parcel
das Päckchen|小包裹|small parcel
der Absender|寄件人|sender
der Empfänger|收件人|recipient
die Adresse|地址|address
die Postleitzahl|邮政编码|postcode
das Porto|邮费|postage
verschicken|寄送|to send
abholen|领取|to collect
unterschreiben|签字|to sign
die Zustellung|投递|delivery`)},
{no:28,file:'Berufe.html',de:'Berufe',zh:'职业名称（阴阳性）',en:'Professions',icons:['👩‍⚕️','👨‍🏫','👩‍🍳','👷'],words:W(`
der Arzt|男医生|doctor
die Ärztin|女医生|doctor
der Lehrer|男教师|teacher
die Lehrerin|女教师|teacher
der Verkäufer|男售货员|sales assistant
die Verkäuferin|女售货员|sales assistant
der Koch|男厨师|cook
die Köchin|女厨师|cook
der Ingenieur|男工程师|engineer
die Ingenieurin|女工程师|engineer
der Fahrer|男司机|driver
die Fahrerin|女司机|driver
der Polizist|男警察|police officer
die Polizistin|女警察|police officer
der Journalist|男记者|journalist
die Journalistin|女记者|journalist`)},
{no:29,file:'Buero.html',de:'Im Büro',zh:'办公室与文具',en:'In the office',icons:['💻','📎','🗂️','🖨️'],words:W(`
das Büro|办公室|office
der Schreibtisch|办公桌|desk
der Bürostuhl|办公椅|office chair
der Computer|电脑|computer
der Bildschirm|显示器|screen
die Tastatur|键盘|keyboard
die Maus|鼠标|mouse
der Drucker|打印机|printer
das Papier|纸|paper
der Kugelschreiber|圆珠笔|ballpoint pen
der Bleistift|铅笔|pencil
der Ordner|文件夹|folder
die Büroklammer|回形针|paper clip
die Besprechung|会议|meeting
der Kollege|男同事|colleague
die Kollegin|女同事|colleague`)},
{no:30,file:'Bewerbung.html',de:'Bewerbung',zh:'简历与面试',en:'Job application',icons:['📄','🤝','💼','✍️'],words:W(`
die Bewerbung|求职申请|application
der Lebenslauf|简历|CV
das Anschreiben|求职信|cover letter
das Zeugnis|证书 / 证明|certificate
die Stellenanzeige|招聘广告|job advert
die Qualifikation|资质|qualification
die Berufserfahrung|工作经验|work experience
die Ausbildung|职业培训|training
das Praktikum|实习|internship
das Vorstellungsgespräch|面试|job interview
der Arbeitgeber|雇主|employer
der Bewerber|男应聘者|applicant
die Bewerberin|女应聘者|applicant
sich bewerben|申请职位|to apply
einstellen|录用|to hire
das Gehalt|工资|salary`)},
{no:31,file:'Amt.html',de:'Amt & Formulare',zh:'政府机关与表格',en:'Authorities & forms',icons:['🏛️','📝','🪪','🔢'],words:W(`
das Amt|政府机关|public office
die Behörde|行政机关|authority
das Bürgeramt|市民服务中心|citizens' office
das Formular|表格|form
der Antrag|申请|application
der Ausweis|身份证件|identity card
der Reisepass|护照|passport
die Anmeldung|登记|registration
die Abmeldung|注销登记|deregistration
die Geburtsurkunde|出生证明|birth certificate
die Unterschrift|签名|signature
der Familienstand|婚姻状况|marital status
die Staatsangehörigkeit|国籍|nationality
ausfüllen|填写|to fill in
beantragen|申请|to apply for
die Gebühr|手续费|fee`)},
{no:32,file:'Schule.html',de:'Schule & Studium',zh:'学校 · 大学 · 课程',en:'School & university',icons:['🎓','📚','✏️','🏫'],words:W(`
die Schule|学校|school
die Universität|大学|university
der Schüler|男学生|pupil
die Schülerin|女学生|pupil
der Student|男大学生|student
die Studentin|女大学生|student
der Lehrer|男教师|teacher
das Fach|科目|subject
der Unterricht|课程 / 授课|lesson
die Vorlesung|大学讲座|lecture
das Seminar|研讨课|seminar
die Prüfung|考试|exam
die Hausaufgabe|家庭作业|homework
das Wörterbuch|词典|dictionary
lernen|学习|to learn
studieren|上大学 / 研读|to study`)},
{no:33,file:'Computer.html',de:'Computer & Internet',zh:'电脑与网络',en:'Computer & internet',icons:['💻','⌨️','🌐','🖱️'],words:W(`
der Computer|电脑|computer
der Laptop|笔记本电脑|laptop
der Bildschirm|屏幕|screen
die Tastatur|键盘|keyboard
die Maus|鼠标|mouse
die Datei|文件|file
der Ordner|文件夹|folder
das Programm|程序|program
die Webseite|网页|website
das Internet|互联网|internet
das WLAN|无线网络|Wi-Fi
das Passwort|密码|password
die E-Mail|电子邮件|email
herunterladen|下载|to download
hochladen|上传|to upload
speichern|保存|to save`)},
{no:34,file:'Handy.html',de:'Handy & Apps',zh:'手机 · 社交 · 聊天',en:'Phone & apps',icons:['📱','💬','📸','🔋'],words:W(`
das Handy|手机|mobile phone
das Smartphone|智能手机|smartphone
die App|应用程序|app
der Bildschirm|屏幕|screen
der Akku|电池|battery
das Ladegerät|充电器|charger
die Nachricht|消息|message
der Anruf|电话|call
der Kontakt|联系人|contact
das Foto|照片|photo
das Video|视频|video
anrufen|打电话|to call
chatten|聊天|to chat
fotografieren|拍照|to photograph
teilen|分享|to share
aufladen|充电|to charge`)},
{no:35,file:'Medien.html',de:'Bücher & Medien',zh:'书籍 · 报刊 · 影视',en:'Books & media',icons:['📚','📰','🎬','🎧'],words:W(`
das Buch|书|book
der Roman|小说|novel
das Wörterbuch|词典|dictionary
die Zeitung|报纸|newspaper
die Zeitschrift|杂志|magazine
der Artikel|文章|article
die Nachricht|新闻|news item
das Fernsehen|电视|television
der Film|电影|film
die Serie|电视剧|series
die Sendung|节目|programme
das Radio|收音机 / 广播|radio
der Podcast|播客|podcast
die Musik|音乐|music
lesen|阅读|to read
ansehen|观看|to watch`)},
{no:36,file:'Begruessung.html',de:'Begrüßung & Small Talk',zh:'问候 · 寒暄 · 自我介绍',en:'Greetings & small talk',icons:['👋','🙂','💬','🤝'],words:W(`
Hallo!|你好！|Hello!
Guten Morgen!|早上好！|Good morning!
Guten Tag!|您好！|Good afternoon!
Guten Abend!|晚上好！|Good evening!
Auf Wiedersehen!|再见！|Goodbye!
Tschüss!|拜拜！|Bye!
Wie geht es Ihnen?|您好吗？|How are you?
Mir geht es gut.|我很好。|I am fine.
Danke, ebenfalls.|谢谢，你也一样。|Thanks, likewise.
Wie heißen Sie?|您叫什么名字？|What is your name?
Ich heiße …|我叫……|My name is …
Woher kommen Sie?|您来自哪里？|Where are you from?
Ich komme aus …|我来自……|I come from …
Freut mich.|很高兴认识您。|Nice to meet you.
Entschuldigung.|对不起 / 劳驾。|Excuse me.
Bis später!|回头见！|See you later!`)},
{no:37,file:'Familie.html',de:'Familie',zh:'家庭与亲属称谓',en:'Family',icons:['👨‍👩‍👧‍👦','👵','👶','🏡'],words:W(`
die Familie|家庭|family
die Eltern|父母|parents
der Vater|父亲|father
die Mutter|母亲|mother
der Sohn|儿子|son
die Tochter|女儿|daughter
der Bruder|兄弟|brother
die Schwester|姐妹|sister
die Geschwister|兄弟姐妹|siblings
der Großvater|祖父 / 外祖父|grandfather
die Großmutter|祖母 / 外祖母|grandmother
der Enkel|孙子 / 外孙|grandson
die Enkelin|孙女 / 外孙女|granddaughter
der Onkel|叔伯 / 舅舅|uncle
die Tante|姑姨 / 婶婶|aunt
verheiratet|已婚的|married`)},
{no:38,file:'Gefuehle.html',de:'Gefühle & Charakter',zh:'情绪与性格形容词',en:'Feelings & character',icons:['😊','😢','😠','😌'],words:W(`
glücklich|幸福的|happy
traurig|悲伤的|sad
fröhlich|开心的|cheerful
wütend|生气的|angry
müde|疲倦的|tired
nervös|紧张的|nervous
ruhig|平静的|calm
überrascht|惊讶的|surprised
ängstlich|害怕的|anxious
freundlich|友好的|friendly
hilfsbereit|乐于助人的|helpful
ehrlich|诚实的|honest
geduldig|耐心的|patient
fleißig|勤奋的|hard-working
lustig|有趣的|funny
zuverlässig|可靠的|reliable`)},
{no:39,file:'Termin.html',de:'Termin & Uhrzeit',zh:'时间 · 日期 · 约会',en:'Time & appointments',icons:['🕒','📅','⏰','🤝'],words:W(`
die Uhr|钟表|clock
die Uhrzeit|时间|time
die Stunde|小时|hour
die Minute|分钟|minute
der Tag|天|day
die Woche|星期|week
der Monat|月|month
das Jahr|年|year
der Termin|预约|appointment
die Verabredung|约会|arrangement
heute|今天|today
morgen|明天|tomorrow
gestern|昨天|yesterday
vormittags|上午|in the morning
nachmittags|下午|in the afternoon
pünktlich|准时的|punctual`)},
{no:40,file:'Feste.html',de:'Feste & Feiertage',zh:'节日与祝福语',en:'Festivals & holidays',icons:['🎉','🎁','🎄','🎂'],words:W(`
das Fest|节日 / 庆典|celebration
der Feiertag|法定节假日|public holiday
der Geburtstag|生日|birthday
die Hochzeit|婚礼|wedding
Weihnachten|圣诞节|Christmas
Ostern|复活节|Easter
Silvester|除夕|New Year's Eve
Neujahr|元旦|New Year
Karneval|狂欢节|carnival
das Geschenk|礼物|present
die Einladung|邀请|invitation
die Feier|庆祝活动|party
gratulieren|祝贺|to congratulate
feiern|庆祝|to celebrate
Frohe Weihnachten!|圣诞快乐！|Merry Christmas!
Herzlichen Glückwunsch!|衷心祝贺！|Congratulations!`)},
{no:41,file:'Wetter.html',de:'Wetter & Jahreszeiten',zh:'天气与四季',en:'Weather & seasons',icons:['☀️','🌧️','❄️','🍂'],words:W(`
das Wetter|天气|weather
die Sonne|太阳|sun
der Regen|雨|rain
der Schnee|雪|snow
der Wind|风|wind
die Wolke|云|cloud
der Nebel|雾|fog
das Gewitter|雷雨|thunderstorm
die Temperatur|温度|temperature
sonnig|晴朗的|sunny
bewölkt|多云的|cloudy
regnerisch|多雨的|rainy
der Frühling|春天|spring
der Sommer|夏天|summer
der Herbst|秋天|autumn
der Winter|冬天|winter`)},
{no:42,file:'Tiere.html',de:'Tiere',zh:'动物 · 宠物 · 农场',en:'Animals',icons:['🐕','🐈','🐄','🦁'],words:W(`
das Tier|动物|animal
der Hund|狗|dog
die Katze|猫|cat
der Vogel|鸟|bird
der Fisch|鱼|fish
das Kaninchen|兔子|rabbit
das Pferd|马|horse
die Kuh|奶牛|cow
das Schwein|猪|pig
das Schaf|绵羊|sheep
die Ziege|山羊|goat
das Huhn|鸡|chicken
die Ente|鸭子|duck
der Löwe|狮子|lion
der Elefant|大象|elephant
der Zoo|动物园|zoo`)},
{no:43,file:'Zahlen.html',de:'Zahlen & Mengen',zh:'数字 · 量词 · 单位',en:'Numbers & quantities',icons:['🔢','⚖️','📏','💯'],words:W(`
null|零|zero
eins|一|one
zwei|二|two
drei|三|three
zehn|十|ten
hundert|一百|hundred
tausend|一千|thousand
die Zahl|数字|number
die Menge|数量|quantity
viel|许多|much / many
wenig|少量|little / few
mehr|更多|more
weniger|更少|less
das Stück|件 / 块|piece
das Kilo|公斤|kilogram
der Liter|升|litre`)},
{no:44,file:'Farben.html',de:'Farben & Formen',zh:'颜色与形状',en:'Colours & shapes',icons:['🎨','🔴','🟦','🔺'],words:W(`
rot|红色的|red
blau|蓝色的|blue
gelb|黄色的|yellow
grün|绿色的|green
schwarz|黑色的|black
weiß|白色的|white
grau|灰色的|grey
braun|棕色的|brown
orange|橙色的|orange
rosa|粉色的|pink
lila|紫色的|purple
der Kreis|圆形|circle
das Quadrat|正方形|square
das Rechteck|长方形|rectangle
das Dreieck|三角形|triangle
die Form|形状|shape`)},
];

const esc=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
const html=p=>`<!DOCTYPE html>
<html lang="de"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(p.de)}</title><link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@300;400;500;600&family=Noto+Serif+SC:wght@400;600&display=swap" rel="stylesheet"><link rel="stylesheet" href="theme-page.css"><link rel="stylesheet" href="word-scene.css"><link rel="stylesheet" href="ai-teacher.css"></head>
<body><header><div class="topline"><div class="eyebrow"></div><a class="home" href="index.html">← Alle Themen · 返回目录</a></div><div class="title-row"><div><h1></h1><div class="sub"></div></div><div class="legend"><span><i style="background:var(--der)"></i>der（阳性）</span><span><i style="background:var(--die)"></i>die（阴性）</span><span><i style="background:var(--das)"></i>das（中性）</span></div></div><div class="rule"></div></header>
<div class="bar"><div class="bar-in"><div class="search"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg><input id="q" placeholder="搜索 德语 / 中文 / English …"></div><div class="group" id="arts"><button class="chip on" data-art="all">Alle</button><button class="chip" data-art="der">der</button><button class="chip" data-art="die">die</button><button class="chip" data-art="das">das</button><button class="chip" data-art="other">其他</button></div><div class="group" id="togs"><button class="chip tog" data-t="de">德语</button><button class="chip tog" data-t="zh">中文</button><button class="chip tog" data-t="en">English</button><button class="chip tog" data-t="ex">例句</button></div><div class="group"><button class="chip" id="play">▶ 朗读全部</button><button class="chip" id="shuffle">🔀 打乱</button><button class="chip" id="print">🖨 打印</button></div><div class="count" id="count"></div></div></div>
<main><div class="grid" id="grid"></div></main><footer><div class="tips"><div class="tip"><span class="k">Im Unterricht 01</span><h4>Was ist das?</h4><p>关闭「德语」，看中文或场景图标抢答；点击卡片即可揭晓答案。</p></div><div class="tip"><span class="k">Im Unterricht 02</span><h4>der / die / das</h4><p>按冠词筛选后做接龙练习，名词连同冠词一起记忆。</p></div><div class="tip"><span class="k">Im Unterricht 03</span><h4>Hören & Sprechen</h4><p>使用单词发音或「朗读全部」，跟读并模仿德语语音。</p></div><div class="tip"><span class="k">Hausaufgabe</span><h4>Diktat</h4><p>打乱卡片后关闭德语做听写，也可一键打印课堂词表。</p></div></div></footer>
<script>window.PAGE=${JSON.stringify(p).replaceAll('</script>','<\\/script>')}</script><script src="term-icons.js"></script><script src="theme-page.js"></script><script src="word-scenes-custom.js"></script><script src="ai-teacher.js"></script><script src="word-scene.js"></script></body></html>`;
for(const p of pages)fs.writeFileSync(new URL(p.file,import.meta.url),html(p),'utf8');
let index=fs.readFileSync(new URL('index.html',import.meta.url),'utf8');
for(const p of pages){const file=p.file.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');const re=new RegExp(`(w:)\\d+(,f:'${file}',ok:)false`);index=index.replace(re,`$1${p.words.length}$2true`)}
fs.writeFileSync(new URL('index.html',import.meta.url),index,'utf8');
console.log(`Generated ${pages.length} pages with ${pages.reduce((n,p)=>n+p.words.length,0)} vocabulary cards.`);
