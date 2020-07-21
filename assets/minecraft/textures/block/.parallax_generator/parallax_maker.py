import os
import shutil
import sys
import traceback

from PIL import Image

# Скрипт ищет в папке карты нормалей (файлы с окончанием _n) и
# генерирует для них параллакс путём изменения альфы в зависимости
# от синего канала. Старые файлы бэкапит в ./.normalmaps_backup

DIRPATH = os.path.dirname(os.path.abspath(__file__))
BACKUP_DIR = os.path.join(DIRPATH, ".normalmaps_backup")


def backup(path: str) -> str:
    """ Бэкапит картинку в ./.normalmaps_backup

        Если папки нет, она будет создана

        `path` - путь к картинке.

        Возвращает путь к бэкапу."""

    if not os.path.exists(BACKUP_DIR):
        print("Making dir", BACKUP_DIR)
        os.mkdir(BACKUP_DIR)

    dst = os.path.join(BACKUP_DIR, os.path.basename(path))
    shutil.copy(path, dst)
    return dst


def _generate_parallax(img, strength: float):
    """ Создаёт параллакс для карты нормалей на
        основе синего канала 
        
        `img` - картинка PIL.Image  
        `strength` - множитель глубины"""
    new_data = []
    img = img.convert("RGBA")
    for px in list(img.getdata()):
        # Проверяем, может быть альфа уже есть
        # if px[3] != 255:
        #     print("Parallax already generated.")
        #     return None
        px = list(px)
        # multiplyed = px[2] * strength

        # shifted = (px[2]-multiplyed)+multiplyed

        diff = 255-px[2]

        px = [px[0], px[1], px[2], int(255-(diff*strength))]
        new_data.append(tuple(px))

    img.putdata(new_data)
    return img


def generate_parallax(path: str, strength: float = 1.0):
    """ Создаёт параллакс для карты нормалей на
        основе синего канала

        `path` - путь к картинке  
        `strength` - множитель глубины"""
    backup(path)
    img = Image.open(path)
    img = _generate_parallax(img, strength)
    img.save(path)


try: 
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            s = input(os.path.basename(arg) + " parallax strength > ")
            generate_parallax(arg, float(s))
    else:
        while True:
            generate_parallax(input("path > "),
                              float(input("parallax strength > ")))
except KeyboardInterrupt:
    quit()
except:
    print(traceback.format_exc())


input("done")
