#!/usr/bin/env python3
"""Write translated short UI labels (titles, tab names, filter buttons) into each locale.

Long guide text (descriptions, info-panel lines) stays English until someone
translates it. Run after tools/build_guides.py, since that tool writes the
English placeholders.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEYS = ['bc_furnace_guide.title', 'bc_furnace_guide.tab.foods', 'bc_furnace_guide.tab.ores',
        'bc_furnace_guide.tab.blocks', 'bc_furnace_guide.tab.nature', 'bc_furnace_guide.tab.fuel',
        'bc_enchanting_guide.title', 'bc_anvil_guide.title', 'bc_anvil_guide.tab.repair',
        'bc_anvil_guide.tab.format', 'bc_anvil_guide.tab.color', 'bc_anvil_guide.tab.nametag',
        'bc_smithing_guide.title', 'bc_smithing_guide.tab.armors', 'bc_smithing_guide.tab.templates',
        'bc_smithing_guide.tab.resources', 'bc_chest_guide.title', 'bc_beacon_info.title',
        'bc_cartography_info.title', 'bc_grindstone_info.title', 'bc_horse_info.title',
        'bc_inventory_info.title', 'bc_loom_info.title', 'bc_trade_info.title',
        'bc_brewing_filter.all', 'bc_brewing_filter.positive', 'bc_brewing_filter.negative',
        'bc_brewing_filter.mixed', 'bc_stonecutter_info.title']

T = {
 'bg_BG': "Ръководство за пещ|Храна|Руди|Блокове|Природа|Гориво|Омагьосвания|Ръководство за наковалня|Поправими|Форматиране|Цветове|Табелка с име|Ръководство за ковач|Брони|Шаблони|Ресурси|Сандък|Маяк|Картографска маса|Точило|Кон, магаре и муле|Инвентар|Стан|Търговия с жители|Всички|Добри|Лоши|Смесени|Каменорез",
 'cs_CZ': "Průvodce pecí|Jídlo|Rudy|Bloky|Příroda|Palivo|Kouzla|Průvodce kovadlinou|Opravitelné|Formátování|Barvy|Jmenovka|Průvodce kovářským stolem|Brnění|Šablony|Suroviny|Truhla|Maják|Kartografický stůl|Brusný kámen|Kůň, osel a mula|Inventář|Tkalcovský stav|Obchodování|Vše|Dobré|Špatné|Smíšené|Kamenická pila",
 'da_DK': "Ovnguide|Mad|Malme|Blokke|Natur|Brændsel|Fortryllelser|Ambolt-guide|Reparerbare|Formatering|Farver|Navneskilt|Smedeguide|Rustninger|Skabeloner|Ressourcer|Kiste|Fyrtårn|Kartografbord|Slibesten|Hest, æsel og muldyr|Inventar|Væv|Landsbyboerhandel|Alle|Gode|Dårlige|Blandede|Stenskærer",
 'de_DE': "Ofen-Leitfaden|Essen|Erze|Blöcke|Natur|Brennstoff|Verzauberungen|Amboss-Leitfaden|Reparierbar|Formatierung|Farben|Namensschild|Schmiede-Leitfaden|Rüstungen|Vorlagen|Ressourcen|Truhe|Leuchtfeuer|Kartentisch|Schleifstein|Pferd, Esel und Maultier|Inventar|Webstuhl|Dorfbewohnerhandel|Alle|Gut|Schlecht|Gemischt|Steinsäge",
 'el_GR': "Οδηγός κλίβανου|Φαγητά|Μεταλλεύματα|Μπλοκ|Φύση|Καύσιμα|Μαγέματα|Οδηγός άκμονα|Επισκευάσιμα|Μορφοποίηση|Χρώματα|Ετικέτα ονόματος|Οδηγός σιδηρουργείου|Πανοπλίες|Πρότυπα|Πόροι|Σεντούκι|Φάρος|Τραπέζι χαρτογράφου|Λιθάρι|Άλογο, γάιδαρος και μουλάρι|Απόθεμα|Αργαλειός|Εμπόριο χωρικών|Όλα|Καλά|Κακά|Μικτά|Λιθοκόπτης",
 'es_ES': "Guía del horno|Comida|Menas|Bloques|Naturaleza|Combustible|Encantamientos|Guía del yunque|Reparables|Formato|Colores|Etiqueta|Guía de herrería|Armaduras|Plantillas|Recursos|Cofre|Faro|Mesa de cartografía|Piedra de afilar|Caballo, burro y mula|Inventario|Telar|Comercio con aldeanos|Todo|Buenas|Malas|Mixtas|Cortapiedras",
 'es_MX': "Guía del horno|Comida|Minerales|Bloques|Naturaleza|Combustible|Encantamientos|Guía del yunque|Reparables|Formato|Colores|Etiqueta|Guía de herrería|Armaduras|Plantillas|Recursos|Cofre|Faro|Mesa de cartografía|Piedra de afilar|Caballo, burro y mula|Inventario|Telar|Comercio con aldeanos|Todo|Buenas|Malas|Mixtas|Cortapiedras",
 'fi_FI': "Uuniopas|Ruoka|Malmit|Palikat|Luonto|Polttoaine|Lumoukset|Alasinopas|Korjattavat|Muotoilu|Värit|Nimilappu|Sepänpöytäopas|Haarniskat|Mallit|Resurssit|Arkku|Majakka|Kartografipöytä|Hiomakivi|Hevonen, aasi ja muuli|Reppu|Kutomapuu|Kyläläiskauppa|Kaikki|Hyvät|Huonot|Sekalaiset|Kivisaha",
 'fr_CA': "Guide du fourneau|Nourriture|Minerais|Blocs|Nature|Combustible|Enchantements|Guide de l'enclume|Réparables|Mise en forme|Couleurs|Étiquette|Guide de la forge|Armures|Modèles|Ressources|Coffre|Balise|Table de cartographie|Meule|Cheval, âne et mule|Inventaire|Métier à tisser|Commerce avec les villageois|Tous|Bons|Mauvais|Mixtes|Tailleur de pierre",
 'fr_FR': "Guide du four|Nourriture|Minerais|Blocs|Nature|Combustible|Enchantements|Guide de l'enclume|Réparables|Mise en forme|Couleurs|Étiquette|Guide de la forge|Armures|Modèles|Ressources|Coffre|Balise|Table de cartographie|Meule|Cheval, âne et mule|Inventaire|Métier à tisser|Commerce avec les villageois|Tous|Bons|Mauvais|Mixtes|Tailleur de pierre",
 'hu_HU': "Kemence útmutató|Étel|Ércek|Blokkok|Természet|Üzemanyag|Varázslatok|Üllő útmutató|Javíthatók|Formázás|Színek|Névcédula|Kovácsasztal útmutató|Páncélok|Sablonok|Nyersanyagok|Láda|Jelzőfény|Térképasztal|Köszörűkő|Ló, szamár és öszvér|Eszköztár|Szövőszék|Falusi kereskedés|Mind|Jó|Rossz|Vegyes|Kővágó",
 'id_ID': "Panduan Tungku|Makanan|Bijih|Blok|Alam|Bahan Bakar|Sihir|Panduan Landasan|Dapat Diperbaiki|Pemformatan|Warna|Label Nama|Panduan Smithing|Armor|Templat|Sumber Daya|Peti|Suar|Meja Kartografi|Batu Asah|Kuda, Keledai, dan Bagal|Inventaris|Alat Tenun|Perdagangan Penduduk Desa|Semua|Baik|Buruk|Campuran|Pemotong Batu",
 'it_IT': "Guida alla fornace|Cibo|Minerali|Blocchi|Natura|Combustibile|Incantesimi|Guida all'incudine|Riparabili|Formattazione|Colori|Targhetta|Guida al tavolo del fabbro|Armature|Modelli|Risorse|Baule|Faro|Tavolo da cartografo|Mola|Cavallo, asino e mulo|Inventario|Telaio|Commercio con gli abitanti|Tutti|Buoni|Cattivi|Misti|Tagliapietre",
 'ja_JP': "かまどガイド|食べ物|鉱石|ブロック|自然|燃料|エンチャント|金床ガイド|修理可能|書式設定|色|名札|鍛冶ガイド|防具|テンプレート|素材|チェスト|ビーコン|製図台|砥石|馬・ロバ・ラバ|インベントリ|機織り機|村人との取引|すべて|良い|悪い|混合|石切り台",
 'ko_KR': "화로 가이드|음식|광석|블록|자연|연료|마법 부여|모루 가이드|수리 가능|서식|색상|이름표|대장간 가이드|갑옷|템플릿|자원|상자|신호기|지도 제작대|숫돌|말, 당나귀, 노새|인벤토리|베틀|주민 거래|전체|좋음|나쁨|혼합|석재 절단기",
 'nb_NO': "Ovnsguide|Mat|Malmer|Blokker|Natur|Brensel|Fortryllelser|Ambolt-guide|Reparerbare|Formatering|Farger|Navnelapp|Smie-guide|Rustninger|Maler|Ressurser|Kiste|Fyrtårn|Kartografbord|Slipestein|Hest, esel og muldyr|Inventar|Vev|Landsbyboerhandel|Alle|Gode|Dårlige|Blandede|Steinkutter",
 'nl_NL': "Ovengids|Eten|Ertsen|Blokken|Natuur|Brandstof|Betoveringen|Aambeeldgids|Repareerbaar|Opmaak|Kleuren|Naamplaatje|Smidsgids|Harnassen|Sjablonen|Grondstoffen|Kist|Baken|Cartografietafel|Slijpsteen|Paard, ezel en muildier|Inventaris|Weefgetouw|Dorpelingenhandel|Alles|Goed|Slecht|Gemengd|Steenzaag",
 'pl_PL': "Przewodnik po piecu|Jedzenie|Rudy|Bloki|Natura|Paliwo|Zaklęcia|Przewodnik po kowadle|Naprawialne|Formatowanie|Kolory|Przywieszka|Przewodnik po kowalstwie|Zbroje|Szablony|Surowce|Skrzynia|Latarnia morska|Stół kartograficzny|Kamień szlifierski|Koń, osioł i muł|Ekwipunek|Krosno|Handel z wieśniakami|Wszystkie|Dobre|Złe|Mieszane|Przecinarka do kamienia",
 'pt_BR': "Guia da fornalha|Comidas|Minérios|Blocos|Natureza|Combustível|Encantamentos|Guia da bigorna|Reparáveis|Formatação|Cores|Etiqueta|Guia de ferraria|Armaduras|Moldes|Recursos|Baú|Sinalizador|Mesa de cartografia|Rebolo|Cavalo, burro e mula|Inventário|Tear|Comércio com aldeões|Todos|Bons|Ruins|Mistos|Cortador de pedras",
 'pt_PT': "Guia da fornalha|Comida|Minérios|Blocos|Natureza|Combustível|Encantamentos|Guia da bigorna|Reparáveis|Formatação|Cores|Etiqueta|Guia de ferraria|Armaduras|Moldes|Recursos|Baú|Sinalizador|Mesa de cartografia|Mó|Cavalo, burro e mula|Inventário|Tear|Comércio com aldeões|Todos|Bons|Maus|Mistos|Cortador de pedra",
 'ru_RU': "Справочник по печи|Еда|Руды|Блоки|Природа|Топливо|Зачарования|Справочник по наковальне|Ремонтируемое|Форматирование|Цвета|Бирка|Справочник по кузнице|Броня|Шаблоны|Ресурсы|Сундук|Маяк|Картографический стол|Точило|Лошадь, осёл и мул|Инвентарь|Ткацкий станок|Торговля с жителями|Все|Хорошие|Плохие|Смешанные|Камнерез",
 'sk_SK': "Sprievodca pecou|Jedlo|Rudy|Bloky|Príroda|Palivo|Kúzla|Sprievodca nákovou|Opraviteľné|Formátovanie|Farby|Menovka|Sprievodca kováčskym stolom|Brnenie|Šablóny|Suroviny|Truhlica|Maják|Kartografický stôl|Brúsny kameň|Kôň, somár a mula|Inventár|Tkáčsky stav|Obchodovanie|Všetko|Dobré|Zlé|Zmiešané|Kamenárska píla",
 'sv_SE': "Ugnsguide|Mat|Malmer|Block|Natur|Bränsle|Förtrollningar|Städguide|Reparerbara|Formatering|Färger|Namnbricka|Smedsguide|Rustningar|Mallar|Resurser|Kista|Fyr|Kartritarbord|Slipsten|Häst, åsna och mula|Inventarie|Vävstol|Bybohandel|Alla|Bra|Dåliga|Blandade|Stenskärare",
 'tr_TR': "Fırın Rehberi|Yiyecekler|Cevherler|Bloklar|Doğa|Yakıt|Büyüler|Örs Rehberi|Onarılabilir|Biçimlendirme|Renkler|İsim Etiketi|Demircilik Rehberi|Zırhlar|Şablonlar|Kaynaklar|Sandık|Fener|Haritacı Masası|Bileme Taşı|At, Eşek ve Katır|Envanter|Dokuma Tezgâhı|Köylü Ticareti|Tümü|İyi|Kötü|Karışık|Taş Kesici",
 'uk_UA': "Посібник з печі|Їжа|Руди|Блоки|Природа|Паливо|Зачарування|Посібник з ковадла|Ремонтоване|Форматування|Кольори|Бирка|Посібник з кузні|Броня|Шаблони|Ресурси|Скриня|Маяк|Картографічний стіл|Точило|Кінь, віслюк і мул|Інвентар|Ткацький верстат|Торгівля з жителями|Усі|Добрі|Погані|Змішані|Каменерізка",
 'zh_CN': "熔炉指南|食物|矿石|方块|自然|燃料|附魔|铁砧指南|可修复|格式|颜色|命名牌|锻造指南|盔甲|模板|资源|箱子|信标|制图台|砂轮|马、驴和骡|物品栏|织布机|村民交易|全部|有益|有害|混合|切石机",
 'zh_TW': "熔爐指南|食物|礦石|方塊|自然|燃料|附魔|鐵砧指南|可修復|格式|顏色|命名牌|鍛造指南|盔甲|模板|資源|箱子|烽火台|製圖桌|砂輪|馬、驢與騾|物品欄|織布機|村民交易|全部|有益|有害|混合|切石機",
}


def main():
    for loc, row in T.items():
        vals = row.split('|')
        assert len(vals) == len(KEYS), (loc, len(vals))
        path = os.path.join(ROOT, 'pack', 'texts', loc + '.lang')
        text = open(path, encoding='utf-8').read()
        for k, v in zip(KEYS, vals):
            text, n = re.subn(rf'^{re.escape(k)}=.*$', lambda m: f'{k}={v}', text, flags=re.M)
            if not n:
                text = text.rstrip('\n') + f'\n{k}={v}\n'
        open(path, 'w', encoding='utf-8').write(text)
    print('translated', len(T), 'locales x', len(KEYS), 'labels')


if __name__ == '__main__':
    main()
