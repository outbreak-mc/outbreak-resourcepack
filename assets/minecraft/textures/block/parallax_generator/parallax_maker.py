import os
import shutil
from typing import Optional

from PIL import Image

# Скрипт ищет в папке карты нормалей (файлы с окончанием _n) и 
# генерирует для них параллакс путём изменения альфы в зависимости
# от синего канала. Старые файлы бэкапит в ./.normalmaps_backup


def generate_parallax(img):
    new_data = []
    for px in list(img.getdata()):
        # Проверяем, может быть альфа уже есть
        if px[3] != 255:
            print("Parallax already generated.")
            return None
        px = list(px)
        px[3] = px[2]
        new_data.append(tuple(px))

    img.putdata(new_data)
    return img


dirpath = os.path.dirname(os.path.abspath(__file__))
backup_dir = os.path.join(dirpath, ".normalmaps_backup")

if not os.path.exists(backup_dir):
    print("Making dir", backup_dir)
    os.mkdir(backup_dir)

for fn in os.listdir(dirpath):
    if fn.endswith("_n.png"):
        imgpath = os.path.join(dirpath, fn)
        print("Generating parallax for", imgpath)
        img = Image.open(imgpath)
        img.convert("RGBA")
        img = generate_parallax(img)
        if img is not None:
            shutil.copy(imgpath, os.path.join(backup_dir, fn))
            print("Creating a backup of", fn)
            img.save(os.path.join(dirpath, fn))
            print("Generated parallax for", fn)
