#!/usr/bin/python -p

import discord
import random
import time
import os
from discord.ext.commands import Bot


my_bot = Bot(command_prefix="!")
score = {}
#All pokemons with number
pokemonNumber = {"Bulbasaur": "001", "Ivysaur": "002", "Venusaur": "003", "Charmander": "004", "Charmeleon": "005", "Charizard": "006", "Squirtle": "007", "Wartortle": "008", "Blastoise": "009", "Caterpie": "010", "Metapod": "011", "Butterfree": "012", "Weedle": "013", "Kakuna": "014", "Beedrill": "015", "Pidgey": "016", "Pidgeotto": "017", "Pidgeot": "018", "Rattata": "019", "Raticate": "020", "Spearow": "021", "Fearow": "022", "Ekans": "023", "Arbok": "024", "Pikachu": "025", "Raichu": "026", "Sandshrew": "027", "Sandslash": "028", "Nidoran": "029", "Nidorina": "030", "Nidoqueen": "031", "Nidoran": "032", "Nidorino": "033", "Nidoking": "034", "Clefairy": "035", "Clefable": "036", "Vulpix": "037", "Ninetales": "038", "Jigglypuff": "039", "Wigglytuff": "040", "Zubat": "041", "Golbat": "042", "Oddish": "043", "Gloom": "044", "Vileplume": "045", "Paras": "046", "Parasect": "047", "Venonat": "048", "Venomoth": "049", "Diglett": "050", "Dugtrio": "051", "Meowth": "052", "Persian": "053", "Psyduck": "054", "Golduck": "055", "Mankey": "056", "Primeape": "057", "Growlithe": "058", "Arcanine": "059", "Poliwag": "060", "Poliwhirl": "061", "Poliwrath": "062", "Abra": "063", "Kadabra": "064", "Alakazam": "065", "Machop": "066", "Machoke": "067", "Machamp": "068", "Bellsprout": "069", "Weepinbell": "070", "Victreebel": "071", "Tentacool": "072", "Tentacruel": "073", "Geodude": "074", "Graveler": "075", "Golem": "076", "Ponyta": "077", "Rapidash": "078", "Slowpoke": "079", "Slowbro": "080", "Magnemite": "081", "Magneton": "082", "Farfetch'd": "083", "Doduo": "084", "Dodrio": "085", "Seel": "086", "Dewgong": "087", "Grimer": "088", "Muk": "089", "Shellder": "090", "Cloyster": "091", "Gastly": "092", "Haunter": "093", "Gengar": "094", "Onix": "095", "Drowzee": "096", "Hypno": "097", "Krabby": "098", "Kingler": "099", "Voltorb": "100", "Electrode": "101", "Exeggcute": "102", "Exeggutor": "103", "Cubone": "104", "Marowak": "105", "Hitmonlee": "106", "Hitmonchan": "107", "Lickitung": "108", "Koffing": "109", "Weezing": "110", "Rhyhorn": "111", "Rhydon": "112", "Chansey": "113", "Tangela": "114", "Kangaskhan": "115", "Horsea": "116", "Seadra": "117", "Goldeen": "118", "Seaking": "119", "Staryu": "120", "Starmie": "121", "Mr.Mime": "122", "Scyther": "123", "Jynx": "124", "Electabuzz": "125", "Magmar": "126", "Pinsir": "127", "Tauros": "128", "Magikarp": "129", "Gyarados": "130", "Lapras": "131", "Ditto": "132", "Eevee": "133", "Vaporeon": "134", "Jolteon": "135", "Flareon": "136", "Porygon": "137", "Omanyte": "138", "Omastar": "139", "Kabuto": "140", "Kabutops": "141", "Aerodactyl": "142", "Snorlax": "143", "Articuno": "144", "Zapdos": "145", "Moltres": "146", "Dratini": "147", "Dragonair": "148", "Dragonite": "149", "Mewtwo": "150", "Mew": "151", "Chikorita": "152", "Bayleef": "153", "Meganium": "154", "Cyndaquil": "155", "Quilava": "156", "Typhlosion": "157", "Totodile": "158", "Croconaw": "159", "Feraligatr": "160", "Sentret": "161", "Furret": "162", "Hoothoot": "163", "Noctowl": "164", "Ledyba": "165", "Ledian": "166", "Spinarak": "167", "Ariados": "168", "Crobat": "169", "Chinchou": "170", "Lanturn": "171", "Pichu": "172", "Cleffa": "173", "Igglybuff": "174", "Togepi": "175", "Togetic": "176", "Natu": "177", "Xatu": "178", "Mareep": "179", "Flaaffy": "180", "Ampharos": "181", "Bellossom": "182", "Marill": "183", "Azumarill": "184", "Sudowoodo": "185", "Politoed": "186", "Hoppip": "187", "Skiploom": "188", "Jumpluff": "189", "Aipom": "190", "Sunkern": "191", "Sunflora": "192", "Yanma": "193", "Wooper": "194", "Quagsire": "195", "Espeon": "196", "Umbreon": "197", "Murkrow": "198", "Slowking": "199", "Misdreavus": "200", "Unown": "201", "Wobbuffet": "202", "Girafarig": "203", "Pineco": "204", "Forretress": "205", "Dunsparce": "206", "Gligar": "207", "Steelix": "208", "Snubbull": "209", "Granbull": "210", "Qwilfish": "211", "Scizor": "212", "Shuckle": "213", "Heracross": "214", "Sneasel": "215", "Teddiursa": "216", "Ursaring": "217", "Slugma": "218", "Magcargo": "219", "Swinub": "220", "Piloswine": "221", "Corsola": "222", "Remoraid": "223", "Octillery": "224", "Delibird": "225", "Mantine": "226", "Skarmory": "227", "Houndour": "228", "Houndoom": "229", "Kingdra": "230", "Phanpy": "231", "Donphan": "232", "Porygon2": "233", "Stantler": "234", "Smeargle": "235", "Tyrogue": "236", "Hitmontop": "237", "Smoochum": "238", "Elekid": "239", "Magby": "240", "Miltank": "241", "Blissey": "242", "Raikou": "243", "Entei": "244", "Suicune": "245", "Larvitar": "246", "Pupitar": "247", "Tyranitar": "248", "Lugia": "249", "Ho-Oh": "250", "Celebi": "251", "Treecko": "252", "Grovyle": "253", "Sceptile": "254", "Torchic": "255", "Combusken": "256", "Blaziken": "257", "Mudkip": "258", "Marshtomp": "259", "Swampert": "260", "Poochyena": "261", "Mightyena": "262", "Zigzagoon": "263", "Linoone": "264", "Wurmple": "265", "Silcoon": "266", "Beautifly": "267", "Cascoon": "268", "Dustox": "269", "Lotad": "270", "Lombre": "271", "Ludicolo": "272", "Seedot": "273", "Nuzleaf": "274", "Shiftry": "275", "Taillow": "276", "Swellow": "277", "Wingull": "278", "Pelipper": "279", "Ralts": "280", "Kirlia": "281", "Gardevoir": "282", "Surskit": "283", "Masquerain": "284", "Shroomish": "285", "Breloom": "286", "Slakoth": "287", "Vigoroth": "288", "Slaking": "289", "Nincada": "290", "Ninjask": "291", "Shedinja": "292", "Whismur": "293", "Loudred": "294", "Exploud": "295", "Makuhita": "296", "Hariyama": "297", "Azurill": "298", "Nosepass": "299", "Skitty": "300", "Delcatty": "301", "Sableye": "302", "Mawile": "303", "Aron": "304", "Lairon": "305", "Aggron": "306", "Meditite": "307", "Medicham": "308", "Electrike": "309", "Manectric": "310", "Plusle": "311", "Minun": "312", "Volbeat": "313", "Illumise": "314", "Roselia": "315", "Gulpin": "316", "Swalot": "317", "Carvanha": "318", "Sharpedo": "319", "Wailmer": "320", "Wailord": "321", "Numel": "322", "Camerupt": "323", "Torkoal": "324", "Spoink": "325", "Grumpig": "326", "Spinda": "327", "Trapinch": "328", "Vibrava": "329", "Flygon": "330", "Cacnea": "331", "Cacturne": "332", "Swablu": "333", "Altaria": "334", "Zangoose": "335", "Seviper": "336", "Lunatone": "337", "Solrock": "338", "Barboach": "339", "Whiscash": "340", "Corphish": "341", "Crawdaunt": "342", "Baltoy": "343", "Claydol": "344", "Lileep": "345", "Cradily": "346", "Anorith": "347", "Armaldo": "348", "Feebas": "349", "Milotic": "350", "Castform": "351", "Kecleon": "352", "Shuppet": "353", "Banette": "354", "Duskull": "355", "Dusclops": "356", "Tropius": "357", "Chimecho": "358", "Absol": "359", "Wynaut": "360", "Snorunt": "361", "Glalie": "362", "Spheal": "363", "Sealeo": "364", "Walrein": "365", "Clamperl": "366", "Huntail": "367", "Gorebyss": "368", "Relicanth": "369", "Luvdisc": "370", "Bagon": "371", "Shelgon": "372", "Salamence": "373", "Beldum": "374", "Metang": "375", "Metagross": "376", "Regirock": "377", "Regice": "378", "Registeel": "379", "Latias": "380", "Latios": "381", "Kyogre": "382", "Groudon": "383", "Rayquaza": "384", "Jirachi": "385", "Deoxys": "386", "Turtwig": "387", "Grotle": "388", "Torterra": "389", "Chimchar": "390", "Monferno": "391", "Infernape": "392", "Piplup": "393", "Prinplup": "394", "Empoleon": "395", "Starly": "396", "Staravia": "397", "Staraptor": "398", "Bidoof": "399", "Bibarel": "400", "Kricketot": "401", "Kricketune": "402", "Shinx": "403", "Luxio": "404", "Luxray": "405", "Budew": "406", "Roserade": "407", "Cranidos": "408", "Rampardos": "409", "Shieldon": "410", "Bastiodon": "411", "Burmy": "412", "Wormadam": "413", "Mothim": "414", "Combee": "415", "Vespiquen": "416", "Pachirisu": "417", "Buizel": "418", "Floatzel": "419", "Cherubi": "420", "Cherrim": "421", "Shellos": "422", "Gastrodon": "423", "Ambipom": "424", "Drifloon": "425", "Drifblim": "426", "Buneary": "427", "Lopunny": "428", "Mismagius": "429", "Honchkrow": "430", "Glameow": "431", "Purugly": "432", "Chingling": "433", "Stunky": "434", "Skuntank": "435", "Bronzor": "436", "Bronzong": "437", "Bonsly": "438", "Mime Jr.": "439", "Happiny": "440", "Chatot": "441", "Spiritomb": "442", "Gible": "443", "Gabite": "444", "Garchomp": "445", "Munchlax": "446", "Riolu": "447", "Lucario": "448", "Hippopotas": "449", "Hippowdon": "450", "Skorupi": "451", "Drapion": "452", "Croagunk": "453", "Toxicroak": "454", "Carnivine": "455", "Finneon": "456", "Lumineon": "457", "Mantyke": "458", "Snover": "459", "Abomasnow": "460", "Weavile": "461", "Magnezone": "462", "Lickilicky": "463", "Rhyperior": "464", "Tangrowth": "465", "Electivire": "466", "Magmortar": "467", "Togekiss": "468", "Yanmega": "469", "Leafeon": "470", "Glaceon": "471", "Gliscor": "472", "Mamoswine": "473", "Porygon-Z": "474", "Gallade": "475", "Probopass": "476", "Dusknoir": "477", "Froslass": "478", "Rotom": "479", "Uxie": "480", "Mesprit": "481", "Azelf": "482", "Dialga": "483", "Palkia": "484", "Heatran": "485", "Regigigas": "486", "Giratina": "487", "Cresselia": "488", "Phione": "489", "Manaphy": "490", "Darkrai": "491", "Shaymin": "492", "Arceus": "493", "Victini": "494", "Snivy": "495", "Servine": "496", "Serperior": "497", "Tepig": "498", "Pignite": "499", "Emboar": "500", "Oshawott": "501", "Dewott": "502", "Samurott": "503", "Patrat": "504", "Watchog": "505", "Lillipup": "506", "Herdier": "507", "Stoutland": "508", "Purrloin": "509", "Liepard": "510", "Pansage": "511", "Simisage": "512", "Pansear": "513", "Simisear": "514", "Panpour": "515", "Simipour": "516", "Munna": "517", "Musharna": "518", "Pidove": "519", "Tranquill": "520", "Unfezant": "521", "Blitzle": "522", "Zebstrika": "523", "Roggenrola": "524", "Boldore": "525", "Gigalith": "526", "Woobat": "527", "Swoobat": "528", "Drilbur": "529", "Excadrill": "530", "Audino": "531", "Timburr": "532", "Gurdurr": "533", "Conkeldurr": "534", "Tympole": "535", "Palpitoad": "536", "Seismitoad": "537", "Throh": "538", "Sawk": "539", "Sewaddle": "540", "Swadloon": "541", "Leavanny": "542", "Venipede": "543", "Whirlipede": "544", "Scolipede": "545", "Cottonee": "546", "Whimsicott": "547", "Petilil": "548", "Lilligant": "549", "Basculin": "550", "Sandile": "551", "Krokorok": "552", "Krookodile": "553", "Darumaka": "554", "Darmanitan": "555", "Maractus": "556", "Dwebble": "557", "Crustle": "558", "Scraggy": "559", "Scrafty": "560", "Sigilyph": "561", "Yamask": "562", "Cofagrigus": "563", "Tirtouga": "564", "Carracosta": "565", "Archen": "566", "Archeops": "567", "Trubbish": "568", "Garbodor": "569", "Zorua": "570", "Zoroark": "571", "Minccino": "572", "Cinccino": "573", "Gothita": "574", "Gothorita": "575", "Gothitelle": "576", "Solosis": "577", "Duosion": "578", "Reuniclus": "579", "Ducklett": "580", "Swanna": "581", "Vanillite": "582", "Vanillish": "583", "Vanilluxe": "584", "Deerling": "585", "Sawsbuck": "586", "Emolga": "587", "Karrablast": "588", "Escavalier": "589", "Foongus": "590", "Amoonguss": "591", "Frillish": "592", "Jellicent": "593", "Alomomola": "594", "Joltik": "595", "Galvantula": "596", "Ferroseed": "597", "Ferrothorn": "598", "Klink": "599", "Klang": "600", "Klinklang": "601", "Tynamo": "602", "Eelektrik": "603", "Eelektross": "604", "Elgyem": "605", "Beheeyem": "606", "Litwick": "607", "Lampent": "608", "Chandelure": "609", "Axew": "610", "Fraxure": "611", "Haxorus": "612", "Cubchoo": "613", "Beartic": "614", "Cryogonal": "615", "Shelmet": "616", "Accelgor": "617", "Stunfisk": "618", "Mienfoo": "619", "Mienshao": "620", "Druddigon": "621", "Golett": "622", "Golurk": "623", "Pawniard": "624", "Bisharp": "625", "Bouffalant": "626", "Rufflet": "627", "Braviary": "628", "Vullaby": "629", "Mandibuzz": "630", "Heatmor": "631", "Durant": "632", "Deino": "633", "Zweilous": "634", "Hydreigon": "635", "Larvesta": "636", "Volcarona": "637", "Cobalion": "638", "Terrakion": "639", "Virizion": "640", "Tornadus": "641", "Thundurus": "642", "Reshiram": "643", "Zekrom": "644", "Landorus": "645", "Kyurem": "646", "Keldeo": "647", "Meloetta": "648", "Genesect": "649", "Chespin": "650", "Quilladin": "651", "Chesnaught": "652", "Fennekin": "653", "Braixen": "654", "Delphox": "655", "Froakie": "656", "Frogadier": "657", "Greninja": "658", "Bunnelby": "659", "Diggersby": "660", "Fletchling": "661", "Fletchinder": "662", "Talonflame": "663", "Scatterbug": "664", "Spewpa": "665", "Vivillon": "666", "Litleo": "667", "Pyroar": "668", "Flabébé": "669", "Floette": "670", "Florges": "671", "Skiddo": "672", "Gogoat": "673", "Pancham": "674", "Pangoro": "675", "Furfrou": "676", "Espurr": "677", "Meowstic": "678", "Honedge": "679", "Doublade": "680", "Aegislash": "681", "Spritzee": "682", "Aromatisse": "683", "Swirlix": "684", "Slurpuff": "685", "Inkay": "686", "Malamar": "687", "Binacle": "688", "Barbaracle": "689", "Skrelp": "690", "Dragalge": "691", "Clauncher": "692", "Clawitzer": "693", "Helioptile": "694", "Heliolisk": "695", "Tyrunt": "696", "Tyrantrum": "697", "Amaura": "698", "Aurorus": "699", "Sylveon": "700", "Hawlucha": "701", "Dedenne": "702", "Carbink": "703", "Goomy": "704", "Sliggoo": "705", "Goodra": "706", "Klefki": "707", "Phantump": "708", "Trevenant": "709", "Pumpkaboo": "710", "Gourgeist": "711", "Bergmite": "712", "Avalugg": "713", "Noibat": "714", "Noivern": "715", "Xerneas": "716", "Yveltal": "717", "Zygarde": "718", "Diancie": "719", "Hoopa": "720", "Volcanion": "721", "Rowlet": "722", "Dartrix": "723", "Decidueye": "724", "Litten": "725", "Torracat": "726", "Incineroar": "727", "Popplio": "728", "Brionne": "729", "Primarina": "730", "Pikipek": "731", "Trumbeak": "732", "Toucannon": "733", "Yungoos": "734", "Gumshoos": "735", "Grubbin": "736", "Charjabug": "737", "Vikavolt": "738", "Crabrawler": "739", "Crabominable": "740", "Oricorio": "741", "Cutiefly": "742", "Ribombee": "743", "Rockruff": "744", "Lycanroc": "745", "Wishiwashi": "746", "Mareanie": "747", "Toxapex": "748", "Mudbray": "749", "Mudsdale": "750", "Dewpider": "751", "Araquanid": "752", "Fomantis": "753", "Lurantis": "754", "Morelull": "755", "Shiinotic": "756", "Salandit": "757", "Salazzle": "758", "Stufful": "759", "Bewear": "760", "Bounsweet": "761", "Steenee": "762", "Tsareena": "763", "Comfey": "764", "Oranguru": "765", "Passimian": "766", "Wimpod": "767", "Golisopod": "768", "Sandygast": "769", "Palossand": "770", "Pyukumuku": "771", "Type: Null": "772", "Silvally": "773", "Minior": "774", "Komala": "775", "Turtonator": "776", "Togedemaru": "777", "Mimikyu": "778", "Bruxish": "779", "Drampa": "780", "Dhelmise": "781", "Jangmo-o": "782", "Hakamo-o": "783", "Kommo-o": "784", "Tapu Koko": "785", "Tapu Lele": "786", "Tapu Bulu": "787", "Tapu Fini": "788", "Cosmog": "789", "Cosmoem": "790", "Solgaleo": "791", "Lunala": "792", "Nihilego": "793", "Buzzwole": "794", "Pheromosa": "795", "Xurkitree": "796", "Celesteela": "797", "Kartana": "798", "Guzzlord": "799", "Necrozma": "800", "Magearna": "801", "Marshadow": "802"}
#, "Poipole": "803", "Naganadel": "804", "Stakataka": "805", "Blacephalon": "806", "Zeraora": "807"}
#151 Pokemon
pokemonsGen1 = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran","Nidorina","Nidoqueen","Nidoran","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr.Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]
#100 Pokemon
pokemonsGen2 = ["Chikorita","Bayleef","Meganium","Cyndaquil","Quilava","Typhlosion","Totodile","Croconaw","Feraligatr","Sentret","Furret","Hoothoot","Noctowl","Ledyba","Ledian","Spinarak","Ariados","Crobat","Chinchou","Lanturn","Pichu","Cleffa","Igglybuff","Togepi","Togetic","Natu","Xatu","Mareep","Flaaffy","Ampharos","Bellossom","Marill","Azumarill","Sudowoodo","Politoed","Hoppip","Skiploom","Jumpluff","Aipom","Sunkern","Sunflora","Yanma","Wooper","Quagsire","Espeon","Umbreon","Murkrow","Slowking","Misdreavus","Unown","Wobbuffet","Girafarig","Pineco","Forretress","Dunsparce","Gligar","Steelix","Snubbull","Granbull","Qwilfish","Scizor","Shuckle","Heracross","Sneasel","Teddiursa","Ursaring","Slugma","Magcargo","Swinub","Piloswine","Corsola","Remoraid","Octillery","Delibird","Mantine","Skarmory","Houndour","Houndoom","Kingdra","Phanpy","Donphan","Porygon2","Stantler","Smeargle","Tyrogue","Hitmontop","Smoochum","Elekid","Magby","Miltank","Blissey","Raikou","Entei","Suicune","Larvitar","Pupitar","Tyranitar","Lugia","Ho-Oh","Celebi"]
pokemonsGen3 = ["Treecko","Grovyle","Sceptile","Torchic","Combusken","Blaziken","Mudkip","Marshtomp","Swampert","Poochyena","Mightyena","Zigzagoon","Linoone","Wurmple","Silcoon","Beautifly","Cascoon","Dustox","Lotad","Lombre","Ludicolo","Seedot","Nuzleaf","Shiftry","Taillow","Swellow","Wingull","Pelipper","Ralts","Kirlia","Gardevoir","Surskit","Masquerain","Shroomish","Breloom","Slakoth","Vigoroth","Slaking","Nincada","Ninjask","Shedinja","Whismur","Loudred","Exploud","Makuhita","Hariyama","Azurill","Nosepass","Skitty","Delcatty","Sableye","Mawile","Aron","Lairon","Aggron","Meditite","Medicham","Electrike","Manectric","Plusle","Minun","Volbeat","Illumise","Roselia","Gulpin","Swalot","Carvanha","Sharpedo","Wailmer","Wailord","Numel","Camerupt","Torkoal","Spoink","Grumpig","Spinda","Trapinch","Vibrava","Flygon","Cacnea","Cacturne","Swablu","Altaria","Zangoose","Seviper","Lunatone","Solrock","Barboach","Whiscash","Corphish","Crawdaunt","Baltoy","Claydol","Lileep","Cradily","Anorith","Armaldo","Feebas","Milotic","Castform","Kecleon","Shuppet","Banette","Duskull","Dusclops","Tropius","Chimecho","Absol","Wynaut","Snorunt","Glalie","Spheal","Sealeo","Walrein","Clamperl","Huntail","Gorebyss","Relicanth","Luvdisc","Bagon","Shelgon","Salamence","Beldum","Metang","Metagross","Regirock","Regice","Registeel","Latias","Latios","Kyogre","Groudon","Rayquaza","Jirachi","Deoxys"]
pokemonsGen4 = ["Turtwig","Grotle","Torterra","Chimchar","Monferno","Infernape","Piplup","Prinplup","Empoleon","Starly","Staravia","Staraptor","Bidoof","Bibarel","Kricketot","Kricketune","Shinx","Luxio","Luxray","Budew","Roserade","Cranidos","Rampardos","Shieldon","Bastiodon","Burmy","Wormadam","Mothim","Combee","Vespiquen","Pachirisu","Buizel","Floatzel","Cherubi","Cherrim","Shellos","Gastrodon","Ambipom","Drifloon","Drifblim","Buneary","Lopunny","Mismagius","Honchkrow","Glameow","Purugly","Chingling","Stunky","Skuntank","Bronzor","Bronzong","Bonsly","Mime Jr.","Happiny","Chatot","Spiritomb","Gible","Gabite","Garchomp","Munchlax","Riolu","Lucario","Hippopotas","Hippowdon","Skorupi","Drapion","Croagunk","Toxicroak","Carnivine","Finneon","Lumineon","Mantyke","Snover","Abomasnow","Weavile","Magnezone","Lickilicky","Rhyperior","Tangrowth","Electivire","Magmortar","Togekiss","Yanmega","Leafeon","Glaceon","Gliscor","Mamoswine","Porygon-Z","Gallade","Probopass","Dusknoir","Froslass","Rotom","Uxie","Mesprit","Azelf","Dialga","Palkia","Heatran","Regigigas","Giratina","Cresselia","Phione","Manaphy","Darkrai","Shaymin","Arceus"]
pokemonsGen5 = ["Victini","Snivy","Servine","Serperior","Tepig","Pignite","Emboar","Oshawott","Dewott","Samurott","Patrat","Watchog","Lillipup","Herdier","Stoutland","Purrloin","Liepard","Pansage","Simisage","Pansear","Simisear","Panpour","Simipour","Munna","Musharna","Pidove","Tranquill","Unfezant","Blitzle","Zebstrika","Roggenrola","Boldore","Gigalith","Woobat","Swoobat","Drilbur","Excadrill","Audino","Timburr","Gurdurr","Conkeldurr","Tympole","Palpitoad","Seismitoad","Throh","Sawk","Sewaddle","Swadloon","Leavanny","Venipede","Whirlipede","Scolipede","Cottonee","Whimsicott","Petilil","Lilligant","Basculin","Sandile","Krokorok","Krookodile","Darumaka","Darmanitan","Maractus","Dwebble","Crustle","Scraggy","Scrafty","Sigilyph","Yamask","Cofagrigus","Tirtouga","Carracosta","Archen","Archeops","Trubbish","Garbodor","Zorua","Zoroark","Minccino","Cinccino","Gothita","Gothorita","Gothitelle","Solosis","Duosion","Reuniclus","Ducklett","Swanna","Vanillite","Vanillish","Vanilluxe","Deerling","Sawsbuck","Emolga","Karrablast","Escavalier","Foongus","Amoonguss","Frillish","Jellicent","Alomomola","Joltik","Galvantula","Ferroseed","Ferrothorn","Klink","Klang","Klinklang","Tynamo","Eelektrik","Eelektross","Elgyem","Beheeyem","Litwick","Lampent","Chandelure","Axew","Fraxure","Haxorus","Cubchoo","Beartic","Cryogonal","Shelmet","Accelgor","Stunfisk","Mienfoo","Mienshao","Druddigon","Golett","Golurk","Pawniard","Bisharp","Bouffalant","Rufflet","Braviary","Vullaby","Mandibuzz","Heatmor","Durant","Deino","Zweilous","Hydreigon","Larvesta","Volcarona","Cobalion","Terrakion","Virizion","Tornadus","Thundurus","Reshiram","Zekrom","Landorus","Kyurem","Keldeo","Meloetta","Genesect"]
pokemonsGen6 = ["Chespin","Quilladin","Chesnaught","Fennekin","Braixen","Delphox","Froakie","Frogadier","Greninja","Bunnelby","Diggersby","Fletchling","Fletchinder","Talonflame","Scatterbug","Spewpa","Vivillon","Litleo","Pyroar","Flabébé","Floette","Florges","Skiddo","Gogoat","Pancham","Pangoro","Furfrou","Espurr","Meowstic","Honedge","Doublade","Aegislash","Spritzee","Aromatisse","Swirlix","Slurpuff","Inkay","Malamar","Binacle","Barbaracle","Skrelp","Dragalge","Clauncher","Clawitzer","Helioptile","Heliolisk","Tyrunt","Tyrantrum","Amaura","Aurorus","Sylveon","Hawlucha","Dedenne","Carbink","Goomy","Sliggoo","Goodra","Klefki","Phantump","Trevenant","Pumpkaboo","Gourgeist","Bergmite","Avalugg","Noibat","Noivern","Xerneas","Yveltal","Zygarde","Diancie","Hoopa","Volcanion"]
pokemonsGen7 = ["Rowlet","Dartrix","Decidueye","Litten","Torracat","Incineroar","Popplio","Brionne","Primarina","Pikipek","Trumbeak","Toucannon","Yungoos","Gumshoos","Grubbin","Charjabug","Vikavolt","Crabrawler","Crabominable","Oricorio","Cutiefly","Ribombee","Rockruff","Lycanroc","Wishiwashi","Mareanie","Toxapex","Mudbray","Mudsdale","Dewpider","Araquanid","Fomantis","Lurantis","Morelull","Shiinotic","Salandit","Salazzle","Stufful","Bewear","Bounsweet","Steenee","Tsareena","Comfey","Oranguru","Passimian","Wimpod","Golisopod","Sandygast","Palossand","Pyukumuku","Type: Null","Silvally","Minior","Komala","Turtonator","Togedemaru","Mimikyu","Bruxish","Drampa","Dhelmise","Jangmo-o","Hakamo-o","Kommo-o","Tapu Koko","Tapu Lele","Tapu Bulu","Tapu Fini","Cosmog","Cosmoem","Solgaleo","Lunala","Nihilego","Buzzwole","Pheromosa","Xurkitree","Celesteela","Kartana","Guzzlord","Necrozma","Magearna","Marshadow"]
#,"Poipole","Naganadel","Stakataka","Blacephalon","Zeraora"]
# http://discordpy.readthedocs.io/en/latest/api.html?highlight=wait_for_message
# fix general chat join game
# fix score method()
# @ forran name i time attack
# 
# 
# 
# 
def write():
	output = open("stats.txt", "w")
	output.write(str(score))
	output.close()

def read():
	global score
	output = open("stats.txt", "r")
	score = eval(output.read())

def get_rank(name):
	r = score[name]
	if 1 <= r < 100:
		return str(name)
	if 100 <= r < 300:
		return "Pallet Town Citizen "+str(name)
	if 300 <= r < 500:
		return "Gym Leader "+str(name)
	if 500 <= r < 700:
		return "Elite Four "+str(name)
	if 700 <= r < 1000:
		return "Pokemon Professor "+str(name)
	if 1000 <= r < 2000:
		return "Pokemon Master "+str(name)
	else:
		return "Trainer Red "+str(name)


@my_bot.event
async def on_ready():
	print("Client logged in")
	await my_bot.send_message(my_bot.get_channel("<channel-id>"), "Enter a command to start a game\n**!startAllGens** - Play Who's That Pokemon for Gens 1 - 7\n**!startGen#** - Play Who's That Pokemon for gen # (replace # with 1 - 7)\n**!timeAttack** - Time attack mode\n!stats - See player stats")

@my_bot.command()
async def startGen1(*args):
	channel = my_bot.get_channel("<channel-id>")
	read()
	for i in random.sample(range(151), 151):
		pokemon = pokemonsGen1[i]
		await my_bot.say("\nWho's that Pokemon?")
		await my_bot.send_file(channel, "images/hidden/"+pokemonNumber[pokemon]+".png")

		def check(msg):
			return msg.content.upper().replace(" ", "") == pokemon.upper().replace(" ", "")

		msg = await my_bot.wait_for_message(check=check)

		if score.get(msg.author.name) is None:
			score[msg.author.name] = 1
		else:
			score[msg.author.name] = score.get(msg.author.name)+1
			print (msg.author.name+": "+str(score[msg.author.name]))

		await my_bot.say("Good job "+get_rank(msg.author.name)+", "+pokemon+" is correct! You've got "+str(score[msg.author.name])+" pokemon right!")
		await my_bot.send_file(channel, "images/shown/"+pokemonNumber[pokemon]+".png")

		write()
		#time.sleep(4)
	await my_bot.say("\nGen 1 Complete type \"!startGen1\" to start again.")
	return

@my_bot.command()
async def startGen2(*args):
	channel = my_bot.get_channel("<channel-id>")
	read()
	for i in random.sample(range(100), 100):
		pokemon = pokemonsGen2[i]
		await my_bot.say("\nWho's that Pokemon?")
		await my_bot.send_file(channel, "images/hidden/"+pokemonNumber[pokemon]+".png")

		def check(msg):
			return msg.content.upper().replace(" ", "") == pokemon.upper().replace(" ", "")

		msg = await my_bot.wait_for_message(check=check)

		if score.get(msg.author.name) is None:
			score[msg.author.name] = 1
		else:
			score[msg.author.name] = score.get(msg.author.name)+1
			print (msg.author.name+": "+str(score[msg.author.name]))

		await my_bot.say("Good job "+get_rank(msg.author.name)+", "+pokemon+" is correct! You've got "+str(score[msg.author.name])+" pokemon right!")
		await my_bot.send_file(channel, "images/shown/"+pokemonNumber[pokemon]+".png")

		write()
		#time.sleep(4)
	await my_bot.say("\nGen 2 Complete type \"!startGen2\" to start again.")
	return

@my_bot.command()
async def startGen3(*args):
	channel = my_bot.get_channel("<channel-id>")
	read()
	for i in random.sample(range(135), 135):
		pokemon = pokemonsGen3[i]
		await my_bot.say("\nWho's that Pokemon?")
		await my_bot.send_file(channel, "images/hidden/"+pokemonNumber[pokemon]+".png")

		def check(msg):
			return msg.content.upper().replace(" ", "") == pokemon.upper().replace(" ", "")

		msg = await my_bot.wait_for_message(check=check)

		if score.get(msg.author.name) is None:
			score[msg.author.name] = 1
		else:
			score[msg.author.name] = score.get(msg.author.name)+1
			print (msg.author.name+": "+str(score[msg.author.name]))

		await my_bot.say("Good job "+get_rank(msg.author.name)+", "+pokemon+" is correct! You've got "+str(score[msg.author.name])+" pokemon right!")
		await my_bot.send_file(channel, "images/shown/"+pokemonNumber[pokemon]+".png")

		write()
		#time.sleep(4)
	await my_bot.say("\nGen 3 Complete type \"!startGen3\" to start again.")
	return

@my_bot.command()
async def startGen4(*args):
	channel = my_bot.get_channel("<channel-id>")
	read()
	for i in random.sample(range(107), 107):
		pokemon = pokemonsGen4[i]
		await my_bot.say("\nWho's that Pokemon?")
		await my_bot.send_file(channel, "images/hidden/"+pokemonNumber[pokemon]+".png")

		def check(msg):
			return msg.content.upper().replace(" ", "") == pokemon.upper().replace(" ", "")

		msg = await my_bot.wait_for_message(check=check)

		if score.get(msg.author.name) is None:
			score[msg.author.name] = 1
		else:
			score[msg.author.name] = score.get(msg.author.name)+1
			print (msg.author.name+": "+str(score[msg.author.name]))

		await my_bot.say("Good job "+get_rank(msg.author.name)+", "+pokemon+" is correct! You've got "+str(score[msg.author.name])+" pokemon right!")
		await my_bot.send_file(channel, "images/shown/"+pokemonNumber[pokemon]+".png")

		write()
		#time.sleep(4)
	await my_bot.say("\nGen 4 Complete type \"!startGen4\" to start again.")
	return

@my_bot.command()
async def startGen5(*args):
	channel = my_bot.get_channel("<channel-id>")
	read()
	for i in random.sample(range(156), 156):
		pokemon = pokemonsGen5[i]
		await my_bot.say("\nWho's that Pokemon?")
		await my_bot.send_file(channel, "images/hidden/"+pokemonNumber[pokemon]+".png")

		def check(msg):
			return msg.content.upper().replace(" ", "") == pokemon.upper().replace(" ", "")

		msg = await my_bot.wait_for_message(check=check)

		if score.get(msg.author.name) is None:
			score[msg.author.name] = 1
		else:
			score[msg.author.name] = score.get(msg.author.name)+1
			print (msg.author.name+": "+str(score[msg.author.name]))

		await my_bot.say("Good job "+get_rank(msg.author.name)+", "+pokemon+" is correct! You've got "+str(score[msg.author.name])+" pokemon right!")
		await my_bot.send_file(channel, "images/shown/"+pokemonNumber[pokemon]+".png")

		write()
		#time.sleep(4)
	await my_bot.say("\nGen 5 Complete type \"!startGen5\" to start again.")
	return

@my_bot.command()
async def startGen6(*args):
	channel = my_bot.get_channel("<channel-id>")
	read()
	for i in random.sample(range(72), 72):
		pokemon = pokemonsGen6[i]
		await my_bot.say("\nWho's that Pokemon?")
		await my_bot.send_file(channel, "images/hidden/"+pokemonNumber[pokemon]+".png")

		def check(msg):
			return msg.content.upper().replace(" ", "") == pokemon.upper().replace(" ", "")

		msg = await my_bot.wait_for_message(check=check)

		if score.get(msg.author.name) is None:
			score[msg.author.name] = 1
		else:
			score[msg.author.name] = score.get(msg.author.name)+1
			print (msg.author.name+": "+str(score[msg.author.name]))

		await my_bot.say("Good job "+get_rank(msg.author.name)+", "+pokemon+" is correct! You've got "+str(score[msg.author.name])+" pokemon right!")
		await my_bot.send_file(channel, "images/shown/"+pokemonNumber[pokemon]+".png")

		write()
		#time.sleep(4)
	await my_bot.say("\nGen 6 Complete type \"!startGen6\" to start again.")
	return

@my_bot.command()
async def startGen7(*args):
	channel = my_bot.get_channel("<channel-id>")
	read()
	for i in random.sample(range(76), 76):
		pokemon = pokemonsGen7[i]
		await my_bot.say("\nWho's that Pokemon?")
		await my_bot.send_file(channel, "images/hidden/"+pokemonNumber[pokemon]+".png")

		def check(msg):
			return msg.content.upper().replace(" ", "") == pokemon.upper().replace(" ", "")

		msg = await my_bot.wait_for_message(check=check)

		if score.get(msg.author.name) is None:
			score[msg.author.name] = 1
		else:
			score[msg.author.name] = score.get(msg.author.name)+1
			print (msg.author.name+": "+str(score[msg.author.name]))

		await my_bot.say("Good job "+get_rank(msg.author.name)+", "+pokemon+" is correct! You've got "+str(score[msg.author.name])+" pokemon right!")
		await my_bot.send_file(channel, "images/shown/"+pokemonNumber[pokemon]+".png")

		write()
		#time.sleep(4)
	await my_bot.say("\nGen 7 Complete type \"!startGen7\" to start again.")
	return

@my_bot.command()
async def startAllGens(*args):
	channel = my_bot.get_channel("<channel-id>")
	read()
	allpokemon = pokemonsGen1 + pokemonsGen2 + pokemonsGen3 + pokemonsGen4 + pokemonsGen5 + pokemonsGen6 + pokemonsGen7
	for i in random.sample(range(802), 802):
		pokemon = allpokemon[i]
		await my_bot.say("\nWho's that Pokemon?")
		await my_bot.send_file(channel, "images/hidden/"+pokemonNumber[pokemon]+".png")

		def check(msg):
			return msg.content.upper().replace(" ", "") == pokemon.upper().replace(" ", "")

		msg = await my_bot.wait_for_message(check=check)

		if score.get(msg.author.name) is None:
			score[msg.author.name] = 1
		else:
			score[msg.author.name] = score.get(msg.author.name)+1
			print (msg.author.name+": "+str(score[msg.author.name]))

		await my_bot.say("Good job "+get_rank(msg.author.name)+", "+pokemon+" is correct! You've got "+str(score[msg.author.name])+" pokemon right!")
		await my_bot.send_file(channel, "images/shown/"+pokemonNumber[pokemon]+".png")

		write()
		#time.sleep(4)
	await my_bot.say("\nAll Pokemon Complete type \"!startAllGens\" to start again.")
	return

@my_bot.command()
async def stats(*args):
	read()
	scoreString = "\nRanks:\nTrainer Red  -  2000\nPokemon Master  -  1000\nPokemon Professor  -  700\nElite Four  -  500\nGym Leader  -  300\nPallet Town Citizen  -  100\n\nStats:"
	sortScore = sorted(score.items(), key=lambda x:x[1])
	sortScore.reverse()
	for player in sortScore:
		scoreString += "\n"+get_rank(player[0])+"  -  "+str(player[1])
	await my_bot.say(scoreString)
	return

@my_bot.command()
async def timeAttack(*args):
	read()
	channel = my_bot.get_channel("<channel-id>")
	players = []
	timeScore = {}

	await my_bot.say("Type something in chat to join in on TimeAttack\nMax 5 Players, you got 20 seconds.")
	t_end = time.time() + 20
	while time.time() < t_end:
		msg = await my_bot.wait_for_message(channel=channel)
		if (msg.author in players) or (msg.author.name == "WTP"):
			continue
		players.append(msg.author)
		await my_bot.say(msg.author.name+" has joined the game.")
		if len(players) >= 5:
			break

	await my_bot.say(str(len(players))+" players has joined the game.")
	await my_bot.say("You got 30 seconds to guess as many as possible.\nYou only get one try on each Pokemon, make it count.\nFirst round will begin soon. Good luck and have fun!")
	time.sleep(5)
	for i, player in enumerate(players):
		await my_bot.say("Get ready "+player.name+" your round will begin in 10 seconds.")
		time.sleep(7)
		await my_bot.say("3...")
		time.sleep(1)
		await my_bot.say("2...")
		time.sleep(1)
		await my_bot.say("1...")
		time.sleep(1)
		await my_bot.say("GO!")
		t_end = time.time() + 30
		while time.time() < t_end:
			pokemon = random.choice(pokemonsGen1)
			await my_bot.send_file(channel, "images/hidden/"+pokemonNumber[pokemon]+".png", content="Who's that Pokemon?")
			msg = await my_bot.wait_for_message(author=player)
			if msg.content.upper().replace(" ", "") == pokemon.upper().replace(" ", ""):
				if timeScore.get(msg.author.name) is None:
					timeScore[msg.author.name] = 1
				else:
					timeScore[msg.author.name] = timeScore.get(msg.author.name)+1
				await my_bot.say("Correct!")
			else:
				await my_bot.send_file(channel, "images/shown/"+pokemonNumber[pokemon]+".png", content="WRONG! "+pokemon+" is the correct answer.")
	sortScore = sorted(timeScore.items(), key=lambda x:x[1])
	sortScore.reverse()
	scoreString = "\n\nDone!\nFinal score is: "
	for name in sortScore:
		scoreString += "\n"+name[0]+": "+str(name[1])
		if score.get(name[0]) is None:
			score[name[0]] = name[1]
		else:
			score[name[0]] = score.get(name[0])+name[1]
	scoreString += "\n\nTo start a new game type \"!timeAttack\"."
	write()
	await my_bot.say(scoreString)
	return

my_bot.run("<bot-id>")