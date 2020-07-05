import os
import shutil
import sys
import traceback
from typing import Optional

from PIL import Image


dirpath = os.path.dirname(os.path.abspath(__file__))
backup_dir = os.path.join(dirpath, ".normalmaps_backup")


def make_backup(img_path):
    """ Делает бэкап картинки в папку ./.normalmaps_backup """
    if not os.path.exists(backup_dir):
        print("Making dir", backup_dir)
        os.mkdir(backup_dir)
    img_name = os.path.basename(img_path)
    backup_path = os.path.join(backup_dir, img_name)
    shutil.copy(img_path, backup_path)
    return backup_path


def generate_parallax(img_path: str):
    """ Генерирует параллакс (альфа-канал) для карты нормалей
        по пути img_path на основе синего канала.

        Картинка перезаписывается, но перед этим делается бэкап
        в ./.normalmaps_backup """

    # Проверяем, картинка ли это вообще
    if not ".png" in os.path.basename(img_path):
        raise ValueError("Invalid path", img_path)

    # Делаем бэкап
    make_backup(img_path)

    # Открываем картинку и делаем нужные операции
    img = Image.open(img_path)
    new_data = []
    img = img.convert("RGBA")
    for px in list(img.getdata()):
        # Проверяем, может быть альфа уже есть
        # if px[3] != 255:
        #     print("Parallax already generated.")
        #     return None
        px = list(px)
        px = [px[0], px[1], px[2], px[2]]
        new_data.append(tuple(px))

    img.putdata(new_data)
    img.save(img_path)
    print("Generated parallax for", os.path.basename(img_path))


try:
    paths = sys.argv[1:]
    if len(paths) > 0:
        for p in paths:
            generate_parallax(p)
    else:
        while True:
            generate_parallax(input("> "))
except:
    traceback.print_exc()

input("done")
