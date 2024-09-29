import png
import csv
import os
from PIL import Image
from pathlib import Path
def get_date_taken(path):
    exif = Image.open(path)._getexif()
# raise Exception('Image {0} does not have EXIF data.'.format(path))
    if not exif:
        return None
    if 36867 not in exif:
        return None
    return exif[36867]
def main(dirname):
    dir = os.fsencode(dirname)
    
    F = open('image_data.csv', 'w')
    writer = csv.writer(F, delimiter=',')

    for file in os.listdir(dir):
        filename = os.fsdecode(file)
        if filename.endswith('.jpg') or filename.endswith('.png'):
            modtime = get_date_taken(dirname + '/' + filename)
            if modtime is not None:
                modtime_1 = modtime[:10].replace(':', '/')
                modtime_2 = modtime[10:]
                writer.writerow([modtime_1 + modtime_2])

main('your directory here:')