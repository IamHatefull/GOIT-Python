def normalize(string):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

    TRANS = {1072: 'a', 1040: 'A', 1073: 'b', 1041: 'B', 1074: 'v', 1042: 'V', 1075: 'g', 1043: 'G', 1076: 'd', 1044: 'D', 1077: 'e', 1045: 'E', 1105: 'e',
             1025: 'E', 1078: 'j', 1046: 'J', 1079: 'z', 1047: 'Z', 1080: 'i', 1048: 'I', 1081: 'j', 1049: 'J', 1082: 'k', 1050: 'K', 1083: 'l', 1051: 'L',
             1084: 'm', 1052: 'M', 1085: 'n', 1053: 'N', 1086: 'o', 1054: 'O', 1087: 'p', 1055: 'P', 1088: 'r', 1056: 'R', 1089: 's', 1057: 'S', 1090: 't',
             1058: 'T', 1091: 'u', 1059: 'U', 1092: 'f', 1060: 'F', 1093: 'h', 1061: 'H', 1094: 'ts', 1062: 'TS', 1095: 'ch', 1063: 'CH', 1096: 'sh', 1064: 'SH',
             1097: 'sch', 1065: 'SCH', 1098: '', 1066: '', 1099: 'y', 1067: 'Y', 1100: '', 1068: '', 1101: 'e', 1069: 'E', 1102: 'yu', 1070: 'YU', 1103: 'u',
             1071: 'U', 1108: 'ja', 1028: 'JA', 1110: 'je', 1030: 'JE', 1111: 'ji', 1031: 'JI', 1169: 'g', 1168: 'G'}
    for c,l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()   
    
    trans_word = string.translate(TRANS)
    normalize_word = ''
    #65-90,97-122,48-57
    for i in trans_word:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <=122 or  48 <= ord(i) <=57:
            normalize_word += i
        else:
            normalize_word += '_'

        
    return normalize_word

