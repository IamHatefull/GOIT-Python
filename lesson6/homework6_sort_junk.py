from pathlib import Path
import shutil

def normalize(path):
    '''
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")
    '''

    TRANS = {1072: 'a', 1040: 'A', 1073: 'b', 1041: 'B', 1074: 'v', 1042: 'V', 1075: 'g', 1043: 'G', 1076: 'd', 1044: 'D', 1077: 'e', 1045: 'E', 1105: 'e',\
             1025: 'E', 1078: 'j', 1046: 'J', 1079: 'z', 1047: 'Z', 1080: 'i', 1048: 'I', 1081: 'j', 1049: 'J', 1082: 'k', 1050: 'K', 1083: 'l', 1051: 'L',\
             1084: 'm', 1052: 'M', 1085: 'n', 1053: 'N', 1086: 'o', 1054: 'O', 1087: 'p', 1055: 'P', 1088: 'r', 1056: 'R', 1089: 's', 1057: 'S', 1090: 't',\
             1058: 'T', 1091: 'u', 1059: 'U', 1092: 'f', 1060: 'F', 1093: 'h', 1061: 'H', 1094: 'ts', 1062: 'TS', 1095: 'ch', 1063: 'CH', 1096: 'sh', 1064: 'SH',\
             1097: 'sch', 1065: 'SCH', 1098: '', 1066: '', 1099: 'y', 1067: 'Y', 1100: '', 1068: '', 1101: 'e', 1069: 'E', 1102: 'yu', 1070: 'YU', 1103: 'u',\
             1071: 'U', 1108: 'ja', 1028: 'JA', 1110: 'je', 1030: 'JE', 1111: 'ji', 1031: 'JI', 1169: 'g', 1168: 'G'}
     
    #print(path)
    path_list = str(path).split('\\')
    our_name = path_list[-1]
    trans_name = our_name.translate(TRANS)
    #print(trans_name)
    normalize_name = ''
    #65-90 or 97-122 or 48-57 or 46
    for i in trans_name:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <=122 or  48 <= ord(i) <=57 or ord(i) == 46:
            normalize_name += i
        else:
            normalize_name += '_'

    #So now we got our normalized name and should rename original file
    path_list[-1] = normalize_name
    new_path = '\\'.join(path_list)
    #print(new_path)
    p1 = Path(path)
    p2 = Path(new_path)
    #print([p1,p2])
    final_name = p1.rename(p2)
    return final_name


#function to find a path to moving destination
def moving_path(path,folder_name):
    path_list = str(path).split('\\')
    path_list.insert(-1, folder_name)
    moving_path = '\\'.join(path_list)
    return moving_path

    
#function to sort all files by path and output them
def sort_junk(path):

    source = Path(path)
    
    for obj in source.iterdir():
        normalize(obj)

    if not Path(str(path) + '\\images').is_dir():
        Path(str(path) + '\\images').mkdir()
    if not Path(str(path) + '\\documents').is_dir():
        Path(str(path) + '\\documents').mkdir()
    if not Path(str(path) + '\\audio').is_dir():
        Path(str(path) + '\\audio').mkdir()
    if not Path(str(path) + '\\video').is_dir():
        Path(str(path) + '\\video').mkdir()
    if not Path(str(path) + '\\archives').is_dir():
        Path(str(path) + '\\archives').mkdir()

    for obj in source.iterdir():
        name = obj.name

        if obj.is_dir():
            if name == 'images' or name == 'documents' or name == 'audio' or name == 'video' or name == 'archives':
                continue
            if obj.stat().st_size == 0:
                obj.rmdir()
                continue
            new_path = f'{path}\\{obj.name}'
            sort_junk(new_path)

        extention = obj.suffix

        if extention == '.jpeg' or extention == '.png' or extention == '.jpg' or extention == '.svg':
            destination_path = Path(moving_path(obj, 'images'))
            shutil.move(obj, destination_path)

        elif extention == '.avi' or extention == '.mp4' or extention == '.mov' or extention == '.mkv':
            destination_path = Path(moving_path(obj, 'video'))
            shutil.move(obj, destination_path)

        elif extention == '.doc' or extention == '.docx' or extention == '.txt' or extention == '.pdf' or extention == '.xlsx' or extention == '.pptx':
            destination_path = Path(moving_path(obj, 'documents'))
            shutil.move(obj, destination_path)

        elif extention == '.mp3' or extention == '.ogg' or extention == '.wav' or extention == '.amr':
            destination_path = Path(moving_path(obj, 'audio'))
            shutil.move(obj, destination_path)

        elif extention == '.zip' or extention == '.gz' or extention == '.tar':
            destination_path = Path(str(path) + '\\archives')
            shutil.unpack_archive(obj, destination_path)

        else:
            continue

    
    
    
'''
path = Path('E:\Libfolder')
sort_junk(path)
'''
