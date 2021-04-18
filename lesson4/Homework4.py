from pathlib import Path

def sort_junk_in_folder(path):
    print(f'_________________________\nSorting files in folder by path: {path}')
    sort_junk(path)
    print('_________________________\n')

    
#function to sort all files by path and output them
def sort_junk(path):

    source = Path(path)
    
    images = []
    video = []
    documents = []
    music = []
    arkhives = []
    known = []
    unknown = []

    for obj in source.iterdir():

        if obj.is_dir():
            new_path = f'{path}\\{obj.name}'
            sort_junk_in_folder(new_path)

        extention = obj.suffix

        if extention == '.jpeg' or extention == '.png' or extention == '.jpg' or extention == '.svg':
            images.append(obj.name)
            known.append(extention)

        elif extention == '.avi' or extention == '.mp4' or extention == '.mov' or extention == '.mkv':
            video.append(obj.name)
            known.append(extention)

        elif extention == '.doc' or extention == '.docx' or extention == '.txt' or extention == '.pdf' or extention == '.xlsx' or extention == '.pptx':
            documents.append(obj.name)
            known.append(extention)

        elif extention == '.mp3' or extention == '.ogg' or extention == '.wav' or extention == '.amr':
            music.append(obj.name)
            known.append(extention)

        elif extention == '.zip' or extention == '.gz' or extention == '.tar':
            arkhives.append(obj.name)
            known.append(extention)

        else:
            unknown.append(extention)

    images.sort()
    video.sort()
    documents.sort()
    music.sort()
    arkhives.sort()
    unic_known = set(known)
    unic_unknown = set(unknown)

    print(f'All images in {path}:\n {images}\n')
    print(f'All video files in {path}:\n {video}\n')
    print(f'All documents in {path}:\n {documents}\n')
    print(f'All music in {path}:\n {music}\n')
    print(f'All arkhives in {path}:\n {arkhives}\n')
    print(f'All known extentions in {path}:\n {unic_known}\n')
    print(f'All unknown extentions in {path}:\n{unic_unknown}\n')
    

