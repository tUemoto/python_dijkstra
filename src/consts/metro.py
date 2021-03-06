from typing import List

from src.types.type_dijkstra import EkikanT, EkimeiT

GLOBAL_EKIMEI_LIST: List[EkimeiT] = [
    EkimeiT(
        "代々木上原",
        "よよぎうえはら",
        "yoyogiuehara",
        "千代田線",
    ),
    EkimeiT(
        "代々木公園",
        "よよぎこうえん",
        "yoyogikouen",
        "千代田線",
    ),
    EkimeiT(
        "明治神宮前",
        "めいじじんぐうまえ",
        "meijijinguumae",
        "千代田線",
    ),
    EkimeiT(
        "表参道",
        "おもてさんどう",
        "omotesandou",
        "千代田線",
    ),
    EkimeiT(
        "乃木坂",
        "のぎざか",
        "nogizaka",
        "千代田線",
    ),
    EkimeiT("赤坂", "あかさか", "akasaka", "千代田線"),
    EkimeiT(
        "国会議事堂前",
        "こっかいぎじどうまえ",
        "kokkaigijidoumae",
        "千代田線",
    ),
    EkimeiT(
        "霞ヶ関",
        "かすみがせき",
        "kasumigaseki",
        "千代田線",
    ),
    EkimeiT("日比谷", "ひびや", "hibiya", "千代田線"),
    EkimeiT(
        "二重橋前",
        "にじゅうばしまえ",
        "nijuubasimae",
        "千代田線",
    ),
    EkimeiT(
        "大手町",
        "おおてまち",
        "otemachi",
        "千代田線",
    ),
    EkimeiT(
        "新御茶ノ水",
        "しんおちゃのみず",
        "shin-ochanomizu",
        "千代田線",
    ),
    EkimeiT("湯島", "ゆしま", "yushima", "千代田線"),
    EkimeiT("根津", "ねづ", "nedu", "千代田線"),
    EkimeiT("千駄木", "せんだぎ", "sendagi", "千代田線"),
    EkimeiT(
        "西日暮里",
        "にしにっぽり",
        "nishinippori",
        "千代田線",
    ),
    EkimeiT("町屋", "まちや", "machiya", "千代田線"),
    EkimeiT(
        "北千住",
        "きたせんじゅ",
        "kitasenjyu",
        "千代田線",
    ),
    EkimeiT("綾瀬", "あやせ", "ayase", "千代田線"),
    EkimeiT(
        "北綾瀬",
        "きたあやせ",
        "kitaayase",
        "千代田線",
    ),
    EkimeiT("浅草", "あさくさ", "asakusa", "銀座線"),
    EkimeiT(
        "田原町",
        "たわらまち",
        "tawaramachi",
        "銀座線",
    ),
    EkimeiT(
        "稲荷町",
        "いなりちょう",
        "inaricho",
        "銀座線",
    ),
    EkimeiT("上野", "うえの", "ueno", "銀座線"),
    EkimeiT(
        "上野広小路",
        "うえのひろこうじ",
        "uenohirokoji",
        "銀座線",
    ),
    EkimeiT(
        "末広町",
        "すえひろちょう",
        "suehirocho",
        "銀座線",
    ),
    EkimeiT("神田", "かんだ", "kanda", "銀座線"),
    EkimeiT(
        "三越前",
        "みつこしまえ",
        "mitsukoshimae",
        "銀座線",
    ),
    EkimeiT(
        "日本橋",
        "にほんばし",
        "nihonbashi",
        "銀座線",
    ),
    EkimeiT("京橋", "きょうばし", "kyobashi", "銀座線"),
    EkimeiT("銀座", "ぎんざ", "ginza", "銀座線"),
    EkimeiT("新橋", "しんばし", "shinbashi", "銀座線"),
    EkimeiT(
        "虎ノ門",
        "とらのもん",
        "toranomon",
        "銀座線",
    ),
    EkimeiT(
        "溜池山王",
        "ためいけさんのう",
        "tameikesannou",
        "銀座線",
    ),
    EkimeiT(
        "赤坂見附",
        "あかさかみつけ",
        "akasakamitsuke",
        "銀座線",
    ),
    EkimeiT(
        "青山一丁目",
        "あおやまいっちょうめ",
        "aoyamaicchome",
        "銀座線",
    ),
    EkimeiT(
        "外苑前",
        "がいえんまえ",
        "gaienmae",
        "銀座線",
    ),
    EkimeiT(
        "表参道",
        "おもてさんどう",
        "omotesando",
        "銀座線",
    ),
    EkimeiT("渋谷", "しぶや", "shibuya", "銀座線"),
    EkimeiT("渋谷", "しぶや", "shibuya", "半蔵門線"),
    EkimeiT(
        "表参道",
        "おもてさんどう",
        "omotesandou",
        "半蔵門線",
    ),
    EkimeiT(
        "青山一丁目",
        "あおやまいっちょうめ",
        "aoyama-itchome",
        "半蔵門線",
    ),
    EkimeiT(
        "永田町",
        "ながたちょう",
        "nagatacho",
        "半蔵門線",
    ),
    EkimeiT(
        "半蔵門",
        "はんぞうもん",
        "hanzomon",
        "半蔵門線",
    ),
    EkimeiT(
        "九段下",
        "くだんした",
        "kudanshita",
        "半蔵門線",
    ),
    EkimeiT(
        "神保町",
        "じんぼうちょう",
        "jinbocho",
        "半蔵門線",
    ),
    EkimeiT(
        "大手町",
        "おおてまち",
        "otemachi",
        "半蔵門線",
    ),
    EkimeiT(
        "三越前",
        "みつこしまえ",
        "mitsukoshimae",
        "半蔵門線",
    ),
    EkimeiT(
        "水天宮前",
        "すいてんぐうまえ",
        "suitengumae",
        "半蔵門線",
    ),
    EkimeiT(
        "清澄白河",
        "きよすみしらかわ",
        "kiyosumi-shirakawa",
        "半蔵門線",
    ),
    EkimeiT("住吉", "すみよし", "sumiyoshi", "半蔵門線"),
    EkimeiT(
        "錦糸町",
        "きんしちょう",
        "kinshicho",
        "半蔵門線",
    ),
    EkimeiT("押上", "おしあげ", "oshiage", "半蔵門線"),
    EkimeiT(
        "中目黒",
        "なかめぐろ",
        "nakameguro",
        "日比谷線",
    ),
    EkimeiT("恵比寿", "えびす", "ebisu", "日比谷線"),
    EkimeiT("広尾", "ひろお", "hiro", "日比谷線"),
    EkimeiT(
        "六本木",
        "ろっぽんぎ",
        "roppongi",
        "日比谷線",
    ),
    EkimeiT(
        "神谷町",
        "かみやちょう",
        "kamiyacho",
        "日比谷線",
    ),
    EkimeiT(
        "霞ヶ関",
        "かすみがせき",
        "kasumigaseki",
        "日比谷線",
    ),
    EkimeiT("日比谷", "ひびや", "hibiya", "日比谷線"),
    EkimeiT("銀座", "ぎんざ", "ginza", "日比谷線"),
    EkimeiT(
        "東銀座",
        "ひがしぎんざ",
        "higashiginza",
        "日比谷線",
    ),
    EkimeiT("築地", "つきじ", "tsukiji", "日比谷線"),
    EkimeiT(
        "八丁堀",
        "はっちょうぼり",
        "hacchobori",
        "日比谷線",
    ),
    EkimeiT(
        "茅場町",
        "かやばちょう",
        "kayabacho",
        "日比谷線",
    ),
    EkimeiT(
        "人形町",
        "にんぎょうちょう",
        "ningyomachi",
        "日比谷線",
    ),
    EkimeiT(
        "小伝馬町",
        "こでんまちょう",
        "kodemmacho",
        "日比谷線",
    ),
    EkimeiT(
        "秋葉原",
        "あきはばら",
        "akihabara",
        "日比谷線",
    ),
    EkimeiT(
        "仲御徒町",
        "なかおかちまち",
        "nakaokachimachi",
        "日比谷線",
    ),
    EkimeiT("上野", "うえの", "ueno", "日比谷線"),
    EkimeiT("入谷", "いりや", "iriya", "日比谷線"),
    EkimeiT("三ノ輪", "みのわ", "minowa", "日比谷線"),
    EkimeiT(
        "南千住",
        "みなみせんじゅ",
        "minamisenju",
        "日比谷線",
    ),
    EkimeiT(
        "北千住",
        "きたせんじゅ",
        "kitasenju",
        "日比谷線",
    ),
    EkimeiT(
        "池袋",
        "いけぶくろ",
        "ikebukuro",
        "丸ノ内線",
    ),
    EkimeiT(
        "新大塚",
        "しんおおつか",
        "shinotsuka",
        "丸ノ内線",
    ),
    EkimeiT(
        "茗荷谷",
        "みょうがだに",
        "myogadani",
        "丸ノ内線",
    ),
    EkimeiT(
        "後楽園",
        "こうらくえん",
        "korakuen",
        "丸ノ内線",
    ),
    EkimeiT(
        "本郷三丁目",
        "ほんごうさんちょうめ",
        "hongosanchome",
        "丸ノ内線",
    ),
    EkimeiT(
        "御茶ノ水",
        "おちゃのみず",
        "ochanomizu",
        "丸ノ内線",
    ),
    EkimeiT(
        "淡路町",
        "あわじちょう",
        "awajicho",
        "丸ノ内線",
    ),
    EkimeiT(
        "大手町",
        "おおてまち",
        "otemachi",
        "丸ノ内線",
    ),
    EkimeiT("東京", "とうきょう", "tokyo", "丸ノ内線"),
    EkimeiT("銀座", "ぎんざ", "ginza", "丸ノ内線"),
    EkimeiT(
        "霞ヶ関",
        "かすみがせき",
        "kasumigaseki",
        "丸ノ内線",
    ),
    EkimeiT(
        "国会議事堂前",
        "こっかいぎじどうまえ",
        "kokkaigijidomae",
        "丸ノ内線",
    ),
    EkimeiT(
        "赤坂見附",
        "あかさかみつけ",
        "akasakamitsuke",
        "丸ノ内線",
    ),
    EkimeiT("四ツ谷", "よつや", "yotsuya", "丸ノ内線"),
    EkimeiT(
        "四谷三丁目",
        "よつやさんちょうめ",
        "yotsuyasanchome",
        "丸ノ内線",
    ),
    EkimeiT(
        "新宿御苑前",
        "しんじゅくぎょえんまえ",
        "shinjuku-gyoemmae",
        "丸ノ内線",
    ),
    EkimeiT(
        "新宿三丁目",
        "しんじゅくさんちょうめ",
        "shinjuku-sanchome",
        "丸ノ内線",
    ),
    EkimeiT(
        "新宿",
        "しんじゅく",
        "shinjuku",
        "丸ノ内線",
    ),
    EkimeiT(
        "西新宿",
        "にししんじゅく",
        "nishi-shinjuku",
        "丸ノ内線",
    ),
    EkimeiT(
        "中野坂上",
        "なかのさかうえ",
        "nakano-sakaue",
        "丸ノ内線",
    ),
    EkimeiT(
        "新中野",
        "しんなかの",
        "shin-nakano",
        "丸ノ内線",
    ),
    EkimeiT(
        "東高円寺",
        "ひがしこうえんじ",
        "higashi-koenji",
        "丸ノ内線",
    ),
    EkimeiT(
        "新高円寺",
        "しんこうえんじ",
        "shin-koenji",
        "丸ノ内線",
    ),
    EkimeiT(
        "南阿佐ヶ谷",
        "みなみあさがや",
        "minami-asagaya",
        "丸ノ内線",
    ),
    EkimeiT("荻窪", "おぎくぼ", "ogikubo", "丸ノ内線"),
    EkimeiT(
        "中野新橋",
        "なかのしんばし",
        "nakano-shimbashi",
        "丸ノ内線",
    ),
    EkimeiT(
        "中野富士見町",
        "なかのふじみちょう",
        "nakano-fujimicho",
        "丸ノ内線",
    ),
    EkimeiT(
        "方南町",
        "ほうなんちょう",
        "honancho",
        "丸ノ内線",
    ),
    EkimeiT("四ツ谷", "よつや", "yotsuya", "南北線"),
    EkimeiT(
        "永田町",
        "ながたちょう",
        "nagatacho",
        "南北線",
    ),
    EkimeiT(
        "溜池山王",
        "ためいけさんのう",
        "tameikesanno",
        "南北線",
    ),
    EkimeiT(
        "六本木一丁目",
        "ろっぽんぎいっちょうめ",
        "roppongiitchome",
        "南北線",
    ),
    EkimeiT(
        "麻布十番",
        "あざぶじゅうばん",
        "azabujuban",
        "南北線",
    ),
    EkimeiT(
        "白金高輪",
        "しろかねたかなわ",
        "shirokanetakanawa",
        "南北線",
    ),
    EkimeiT(
        "白金台",
        "しろかねだい",
        "shirokanedai",
        "南北線",
    ),
    EkimeiT("目黒", "めぐろ", "meguro", "南北線"),
    EkimeiT("市ヶ谷", "いちがや", "ichigaya", "南北線"),
    EkimeiT(
        "飯田橋",
        "いいだばし",
        "idabashi",
        "南北線",
    ),
    EkimeiT(
        "後楽園",
        "こうらくえん",
        "korakuen",
        "南北線",
    ),
    EkimeiT(
        "東大前",
        "とうだいまえ",
        "todaimae",
        "南北線",
    ),
    EkimeiT(
        "本駒込",
        "ほんこまごめ",
        "honkomagome",
        "南北線",
    ),
    EkimeiT("駒込", "こまごめ", "komagome", "南北線"),
    EkimeiT(
        "西ヶ原",
        "にしがはら",
        "nishigahara",
        "南北線",
    ),
    EkimeiT("王子", "おうじ", "oji", "南北線"),
    EkimeiT(
        "王子神谷",
        "おうじかみや",
        "ojikamiya",
        "南北線",
    ),
    EkimeiT("志茂", "しも", "shimo", "南北線"),
    EkimeiT(
        "赤羽岩淵",
        "あかばねいわぶち",
        "akabaneiwabuchi",
        "南北線",
    ),
    EkimeiT(
        "西船橋",
        "にしふなばし",
        "nishi-funabashi",
        "東西線",
    ),
    EkimeiT(
        "原木中山",
        "ばらきなかやま",
        "baraki-nakayama",
        "東西線",
    ),
    EkimeiT("妙典", "みょうでん", "myoden", "東西線"),
    EkimeiT("行徳", "ぎょうとく", "gyotoku", "東西線"),
    EkimeiT(
        "南行徳",
        "みなみぎょうとく",
        "minami-gyotoku",
        "東西線",
    ),
    EkimeiT("浦安", "うらやす", "urayasu", "東西線"),
    EkimeiT("葛西", "かさい", "kasai", "東西線"),
    EkimeiT(
        "西葛西",
        "にしかさい",
        "nishi-kasai",
        "東西線",
    ),
    EkimeiT(
        "南砂町",
        "みなみすなまち",
        "minami-sunamachi",
        "東西線",
    ),
    EkimeiT(
        "東陽町",
        "とうようちょう",
        "touyoucho",
        "東西線",
    ),
    EkimeiT("木場", "きば", "kiba", "東西線"),
    EkimeiT(
        "門前仲町",
        "もんぜんなかちょう",
        "monzen-nakacho",
        "東西線",
    ),
    EkimeiT(
        "茅場町",
        "かやばちょう",
        "kayabacho",
        "東西線",
    ),
    EkimeiT(
        "日本橋",
        "にほんばし",
        "nihonbashi",
        "東西線",
    ),
    EkimeiT(
        "大手町",
        "おおてまち",
        "otemachi",
        "東西線",
    ),
    EkimeiT("竹橋", "たけばし", "takebashi", "東西線"),
    EkimeiT(
        "九段下",
        "くだんした",
        "kudanshita",
        "東西線",
    ),
    EkimeiT(
        "飯田橋",
        "いいだばし",
        "iidabashi",
        "東西線",
    ),
    EkimeiT(
        "神楽坂",
        "かぐらざか",
        "kagurazaka",
        "東西線",
    ),
    EkimeiT("早稲田", "わせだ", "waseda", "東西線"),
    EkimeiT(
        "高田馬場",
        "たかだのばば",
        "takadanobaba",
        "東西線",
    ),
    EkimeiT("落合", "おちあい", "ochiai", "東西線"),
    EkimeiT("中野", "なかの", "nakano", "東西線"),
    EkimeiT(
        "shinkiba",
        "しんきば",
        "新木場",
        "有楽町線",
    ),
    EkimeiT("tatsumi", "たつみ", "辰巳", "有楽町線"),
    EkimeiT("toyosu", "とよす", "豊洲", "有楽町線"),
    EkimeiT(
        "tsukishima",
        "つきしま",
        "月島",
        "有楽町線",
    ),
    EkimeiT(
        "shintomityou",
        "しんとみちょう",
        "新富町",
        "有楽町線",
    ),
    EkimeiT(
        "ginzaittyoume",
        "ぎんざいっちょうめ",
        "銀座一丁目",
        "有楽町線",
    ),
    EkimeiT(
        "yuurakutyou",
        "ゆうらくちょう",
        "有楽町",
        "有楽町線",
    ),
    EkimeiT(
        "sakuradamon",
        "さくらだもん",
        "桜田門",
        "有楽町線",
    ),
    EkimeiT(
        "nagatacho",
        "ながたちょう",
        "永田町",
        "有楽町線",
    ),
    EkimeiT(
        "koujimachi",
        "こうじまち",
        "麹町",
        "有楽町線",
    ),
    EkimeiT(
        "ichigaya",
        "いちがや",
        "市ヶ谷",
        "有楽町線",
    ),
    EkimeiT(
        "iidabashi",
        "いいだばし",
        "飯田橋",
        "有楽町線",
    ),
    EkimeiT(
        "江戸川橋",
        "えどがわばし",
        "edogawabasi",
        "有楽町線",
    ),
    EkimeiT(
        "護国寺",
        "ごこくじ",
        "gokokuji",
        "有楽町線",
    ),
    EkimeiT(
        "東池袋",
        "ひがしいけぶくろ",
        "higasiikebukuro",
        "有楽町線",
    ),
    EkimeiT(
        "池袋",
        "いけぶくろ",
        "ikebukuro",
        "有楽町線",
    ),
    EkimeiT(
        "要町",
        "かなめちょう",
        "kanametyou",
        "有楽町線",
    ),
    EkimeiT("千川", "せんかわ", "senkawa", "有楽町線"),
    EkimeiT(
        "小竹向原",
        "こたけむかいはら",
        "kotakemukaihara",
        "有楽町線",
    ),
    EkimeiT(
        "氷川台",
        "ひかわだい",
        "hikawadai",
        "有楽町線",
    ),
    EkimeiT(
        "平和台",
        "へいわだい",
        "heiwadai",
        "有楽町線",
    ),
    EkimeiT(
        "営団赤塚",
        "えいだんあかつか",
        "eidanakakuka",
        "有楽町線",
    ),
    EkimeiT(
        "営団成増",
        "えいだんなります",
        "eidannarimasu",
        "有楽町線",
    ),
    EkimeiT("和光市", "わこうし", "wakousi", "有楽町線"),
]

GLOBAL_EKIKAN_LIST: List[EkikanT] = [
    EkikanT(
        "代々木上原",
        "代々木公園",
        "千代田線",
        1.0,
        2,
    ),
    EkikanT(
        "代々木公園",
        "明治神宮前",
        "千代田線",
        1.2,
        2,
    ),
    EkikanT(
        "明治神宮前",
        "表参道",
        "千代田線",
        0.9,
        2,
    ),
    EkikanT(
        "表参道",
        "乃木坂",
        "千代田線",
        1.4,
        3,
    ),
    EkikanT("乃木坂", "赤坂", "千代田線", 1.1, 2),
    EkikanT(
        "赤坂",
        "国会議事堂前",
        "千代田線",
        0.8,
        1,
    ),
    EkikanT(
        "国会議事堂前",
        "霞ヶ関",
        "千代田線",
        0.7,
        1,
    ),
    EkikanT(
        "霞ヶ関",
        "日比谷",
        "千代田線",
        1.2,
        2,
    ),
    EkikanT(
        "日比谷",
        "二重橋前",
        "千代田線",
        0.7,
        1,
    ),
    EkikanT(
        "二重橋前",
        "大手町",
        "千代田線",
        0.7,
        1,
    ),
    EkikanT(
        "大手町",
        "新御茶ノ水",
        "千代田線",
        1.3,
        2,
    ),
    EkikanT(
        "新御茶ノ水",
        "湯島",
        "千代田線",
        1.2,
        2,
    ),
    EkikanT("湯島", "根津", "千代田線", 1.2, 2),
    EkikanT("根津", "千駄木", "千代田線", 1.0, 2),
    EkikanT(
        "千駄木",
        "西日暮里",
        "千代田線",
        0.9,
        1,
    ),
    EkikanT(
        "西日暮里",
        "町屋",
        "千代田線",
        1.7,
        2,
    ),
    EkikanT("町屋", "北千住", "千代田線", 2.6, 3),
    EkikanT("北千住", "綾瀬", "千代田線", 2.5, 3),
    EkikanT("綾瀬", "北綾瀬", "千代田線", 2.1, 4),
    EkikanT("浅草", "田原町", "銀座線", 0.8, 2),
    EkikanT("田原町", "稲荷町", "銀座線", 0.7, 1),
    EkikanT("稲荷町", "上野", "銀座線", 0.7, 2),
    EkikanT(
        "上野",
        "上野広小路",
        "銀座線",
        0.5,
        2,
    ),
    EkikanT(
        "上野広小路",
        "末広町",
        "銀座線",
        0.6,
        1,
    ),
    EkikanT("末広町", "神田", "銀座線", 1.1, 2),
    EkikanT("神田", "三越前", "銀座線", 0.7, 1),
    EkikanT("三越前", "日本橋", "銀座線", 0.6, 2),
    EkikanT("日本橋", "京橋", "銀座線", 0.7, 2),
    EkikanT("京橋", "銀座", "銀座線", 0.7, 1),
    EkikanT("銀座", "新橋", "銀座線", 0.9, 2),
    EkikanT("新橋", "虎ノ門", "銀座線", 0.8, 2),
    EkikanT(
        "虎ノ門",
        "溜池山王",
        "銀座線",
        0.6,
        2,
    ),
    EkikanT(
        "溜池山王",
        "赤坂見附",
        "銀座線",
        0.9,
        2,
    ),
    EkikanT(
        "赤坂見附",
        "青山一丁目",
        "銀座線",
        1.3,
        2,
    ),
    EkikanT(
        "青山一丁目",
        "外苑前",
        "銀座線",
        0.7,
        2,
    ),
    EkikanT("外苑前", "表参道", "銀座線", 0.7, 1),
    EkikanT("表参道", "渋谷", "銀座線", 1.3, 1),
    EkikanT("渋谷", "表参道", "半蔵門線", 1.3, 2),
    EkikanT(
        "表参道",
        "青山一丁目",
        "半蔵門線",
        1.4,
        2,
    ),
    EkikanT(
        "青山一丁目",
        "永田町",
        "半蔵門線",
        1.3,
        2,
    ),
    EkikanT(
        "永田町",
        "半蔵門",
        "半蔵門線",
        1.0,
        2,
    ),
    EkikanT(
        "半蔵門",
        "九段下",
        "半蔵門線",
        1.6,
        2,
    ),
    EkikanT(
        "九段下",
        "神保町",
        "半蔵門線",
        0.4,
        1,
    ),
    EkikanT(
        "神保町",
        "大手町",
        "半蔵門線",
        1.7,
        3,
    ),
    EkikanT(
        "大手町",
        "三越前",
        "半蔵門線",
        0.7,
        1,
    ),
    EkikanT(
        "三越前",
        "水天宮前",
        "半蔵門線",
        1.3,
        2,
    ),
    EkikanT(
        "水天宮前",
        "清澄白河",
        "半蔵門線",
        1.7,
        3,
    ),
    EkikanT(
        "清澄白河",
        "住吉",
        "半蔵門線",
        1.9,
        3,
    ),
    EkikanT("住吉", "錦糸町", "半蔵門線", 1, 2),
    EkikanT("錦糸町", "押上", "半蔵門線", 1.4, 2),
    EkikanT("中目黒", "恵比寿", "日比谷線", 1, 2),
    EkikanT("恵比寿", "広尾", "日比谷線", 1.5, 3),
    EkikanT("広尾", "六本木", "日比谷線", 1.7, 3),
    EkikanT(
        "六本木",
        "神谷町",
        "日比谷線",
        1.5,
        3,
    ),
    EkikanT(
        "神谷町",
        "霞ヶ関",
        "日比谷線",
        1.3,
        2,
    ),
    EkikanT(
        "霞ヶ関",
        "日比谷",
        "日比谷線",
        1.2,
        2,
    ),
    EkikanT("日比谷", "銀座", "日比谷線", 0.4, 1),
    EkikanT("銀座", "東銀座", "日比谷線", 0.4, 1),
    EkikanT("東銀座", "築地", "日比谷線", 0.6, 2),
    EkikanT("築地", "八丁堀", "日比谷線", 1, 2),
    EkikanT(
        "八丁堀",
        "茅場町",
        "日比谷線",
        0.5,
        1,
    ),
    EkikanT(
        "茅場町",
        "人形町",
        "日比谷線",
        0.9,
        2,
    ),
    EkikanT(
        "人形町",
        "小伝馬町",
        "日比谷線",
        0.6,
        1,
    ),
    EkikanT(
        "小伝馬町",
        "秋葉原",
        "日比谷線",
        0.9,
        2,
    ),
    EkikanT(
        "秋葉原",
        "仲御徒町",
        "日比谷線",
        1,
        1,
    ),
    EkikanT(
        "仲御徒町",
        "上野",
        "日比谷線",
        0.5,
        1,
    ),
    EkikanT("上野", "入谷", "日比谷線", 1.2, 2),
    EkikanT("入谷", "三ノ輪", "日比谷線", 1.2, 2),
    EkikanT(
        "三ノ輪",
        "南千住",
        "日比谷線",
        0.8,
        2,
    ),
    EkikanT(
        "南千住",
        "北千住",
        "日比谷線",
        1.8,
        3,
    ),
    EkikanT("池袋", "新大塚", "丸ノ内線", 1.8, 3),
    EkikanT(
        "新大塚",
        "茗荷谷",
        "丸ノ内線",
        1.2,
        2,
    ),
    EkikanT(
        "茗荷谷",
        "後楽園",
        "丸ノ内線",
        1.8,
        2,
    ),
    EkikanT(
        "後楽園",
        "本郷三丁目",
        "丸ノ内線",
        0.8,
        1,
    ),
    EkikanT(
        "本郷三丁目",
        "御茶ノ水",
        "丸ノ内線",
        0.8,
        1,
    ),
    EkikanT(
        "御茶ノ水",
        "淡路町",
        "丸ノ内線",
        0.8,
        1,
    ),
    EkikanT(
        "淡路町",
        "大手町",
        "丸ノ内線",
        0.9,
        2,
    ),
    EkikanT("大手町", "東京", "丸ノ内線", 0.6, 1),
    EkikanT("東京", "銀座", "丸ノ内線", 1.1, 2),
    EkikanT("銀座", "霞ヶ関", "丸ノ内線", 1.0, 2),
    EkikanT(
        "霞ヶ関",
        "国会議事堂前",
        "丸ノ内線",
        0.7,
        1,
    ),
    EkikanT(
        "国会議事堂前",
        "赤坂見附",
        "丸ノ内線",
        0.9,
        2,
    ),
    EkikanT(
        "赤坂見附",
        "四ツ谷",
        "丸ノ内線",
        1.3,
        2,
    ),
    EkikanT(
        "四ツ谷",
        "四谷三丁目",
        "丸ノ内線",
        1.0,
        2,
    ),
    EkikanT(
        "四谷三丁目",
        "新宿御苑前",
        "丸ノ内線",
        0.9,
        1,
    ),
    EkikanT(
        "新宿御苑前",
        "新宿三丁目",
        "丸ノ内線",
        0.7,
        1,
    ),
    EkikanT(
        "新宿三丁目",
        "新宿",
        "丸ノ内線",
        0.3,
        1,
    ),
    EkikanT("新宿", "西新宿", "丸ノ内線", 0.8, 1),
    EkikanT(
        "西新宿",
        "中野坂上",
        "丸ノ内線",
        1.1,
        2,
    ),
    EkikanT(
        "中野坂上",
        "新中野",
        "丸ノ内線",
        1.1,
        2,
    ),
    EkikanT(
        "新中野",
        "東高円寺",
        "丸ノ内線",
        1.0,
        1,
    ),
    EkikanT(
        "東高円寺",
        "新高円寺",
        "丸ノ内線",
        0.9,
        1,
    ),
    EkikanT(
        "新高円寺",
        "南阿佐ヶ谷",
        "丸ノ内線",
        1.2,
        2,
    ),
    EkikanT(
        "南阿佐ヶ谷",
        "荻窪",
        "丸ノ内線",
        1.5,
        2,
    ),
    EkikanT(
        "中野坂上",
        "中野新橋",
        "丸ノ内線",
        1.3,
        2,
    ),
    EkikanT(
        "中野新橋",
        "中野富士見町",
        "丸ノ内線",
        0.6,
        1,
    ),
    EkikanT(
        "中野富士見町",
        "方南町",
        "丸ノ内線",
        1.3,
        2,
    ),
    EkikanT("市ヶ谷", "四ツ谷", "南北線", 1.0, 2),
    EkikanT("四ツ谷", "永田町", "南北線", 1.3, 3),
    EkikanT(
        "永田町",
        "溜池山王",
        "南北線",
        0.9,
        1,
    ),
    EkikanT(
        "溜池山王",
        "六本木一丁目",
        "南北線",
        0.9,
        2,
    ),
    EkikanT(
        "六本木一丁目",
        "麻布十番",
        "南北線",
        1.2,
        2,
    ),
    EkikanT(
        "麻布十番",
        "白金高輪",
        "南北線",
        1.3,
        2,
    ),
    EkikanT(
        "白金高輪",
        "白金台",
        "南北線",
        1.0,
        2,
    ),
    EkikanT("白金台", "目黒", "南北線", 1.3, 2),
    EkikanT("市ヶ谷", "飯田橋", "南北線", 1.1, 2),
    EkikanT("飯田橋", "後楽園", "南北線", 1.4, 2),
    EkikanT("後楽園", "東大前", "南北線", 1.3, 3),
    EkikanT("東大前", "本駒込", "南北線", 0.9, 2),
    EkikanT("本駒込", "駒込", "南北線", 1.4, 2),
    EkikanT("駒込", "西ヶ原", "南北線", 1.4, 2),
    EkikanT("西ヶ原", "王子", "南北線", 1.0, 2),
    EkikanT("王子", "王子神谷", "南北線", 1.2, 2),
    EkikanT("王子神谷", "志茂", "南北線", 1.6, 3),
    EkikanT("志茂", "赤羽岩淵", "南北線", 1.1, 2),
    EkikanT(
        "西船橋",
        "原木中山",
        "東西線",
        1.9,
        3,
    ),
    EkikanT("原木中山", "妙典", "東西線", 2.1, 2),
    EkikanT("妙典", "行徳", "東西線", 1.3, 2),
    EkikanT("行徳", "南行徳", "東西線", 1.5, 2),
    EkikanT("南行徳", "浦安", "東西線", 1.2, 2),
    EkikanT("浦安", "葛西", "東西線", 1.9, 2),
    EkikanT("葛西", "西葛西", "東西線", 1.2, 2),
    EkikanT("西葛西", "南砂町", "東西線", 2.7, 2),
    EkikanT("南砂町", "東陽町", "東西線", 1.2, 2),
    EkikanT("東陽町", "木場", "東西線", 0.9, 1),
    EkikanT("木場", "門前仲町", "東西線", 1.1, 1),
    EkikanT(
        "門前仲町",
        "茅場町",
        "東西線",
        1.8,
        2,
    ),
    EkikanT("茅場町", "日本橋", "東西線", 0.5, 1),
    EkikanT("日本橋", "大手町", "東西線", 0.8, 1),
    EkikanT("大手町", "竹橋", "東西線", 1.0, 2),
    EkikanT("竹橋", "九段下", "東西線", 1.0, 1),
    EkikanT("九段下", "飯田橋", "東西線", 0.7, 1),
    EkikanT("飯田橋", "神楽坂", "東西線", 1.2, 2),
    EkikanT("神楽坂", "早稲田", "東西線", 1.2, 2),
    EkikanT(
        "早稲田",
        "高田馬場",
        "東西線",
        1.7,
        3,
    ),
    EkikanT("高田馬場", "落合", "東西線", 1.9, 3),
    EkikanT("落合", "中野", "東西線", 2.0, 3),
    EkikanT("新木場", "辰巳", "有楽町線", 1.5, 2),
    EkikanT("辰巳", "豊洲", "有楽町線", 1.7, 2),
    EkikanT("豊洲", "月島", "有楽町線", 1.4, 2),
    EkikanT("月島", "新富町", "有楽町線", 1.3, 2),
    EkikanT(
        "新富町",
        "銀座一丁目",
        "有楽町線",
        0.7,
        1,
    ),
    EkikanT(
        "銀座一丁目",
        "有楽町",
        "有楽町線",
        0.5,
        1,
    ),
    EkikanT(
        "有楽町",
        "桜田門",
        "有楽町線",
        1.0,
        1,
    ),
    EkikanT(
        "桜田門",
        "永田町",
        "有楽町線",
        0.9,
        2,
    ),
    EkikanT("永田町", "麹町", "有楽町線", 0.9, 1),
    EkikanT("麹町", "市ヶ谷", "有楽町線", 0.9, 1),
    EkikanT(
        "市ヶ谷",
        "飯田橋",
        "有楽町線",
        1.1,
        2,
    ),
    EkikanT(
        "飯田橋",
        "江戸川橋",
        "有楽町線",
        1.6,
        3,
    ),
    EkikanT(
        "江戸川橋",
        "護国寺",
        "有楽町線",
        1.3,
        2,
    ),
    EkikanT(
        "護国寺",
        "東池袋",
        "有楽町線",
        1.1,
        2,
    ),
    EkikanT("東池袋", "池袋", "有楽町線", 2.0, 2),
    EkikanT("池袋", "要町", "有楽町線", 1.2, 2),
    EkikanT("要町", "千川", "有楽町線", 1.0, 1),
    EkikanT(
        "千川",
        "小竹向原",
        "有楽町線",
        1.0,
        2,
    ),
    EkikanT(
        "小竹向原",
        "氷川台",
        "有楽町線",
        1.5,
        2,
    ),
    EkikanT(
        "氷川台",
        "平和台",
        "有楽町線",
        1.4,
        2,
    ),
    EkikanT(
        "平和台",
        "営団赤塚",
        "有楽町線",
        1.8,
        2,
    ),
    EkikanT(
        "営団赤塚",
        "営団成増",
        "有楽町線",
        1.5,
        2,
    ),
    EkikanT(
        "営団成増",
        "和光市",
        "有楽町線",
        2.1,
        3,
    ),
]
