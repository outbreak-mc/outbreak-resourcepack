import os
import shutil
from PIL import Image
dirpath = os.path.dirname(os.path.abspath(__file__))


default_path = os.path.join(os.getenv("appdata"), ".minecraft", "Default",
                            "textures", "block")

ctm_path = os.path.join(os.path.dirname(dirpath), "assets", "minecraft",
                        "optifine", "ctm")


def _move_properties(from_path: str, dst_folder: str):
    """ Копирует файл .properties, заменяя его название и
        `connectTiles=` в нём на название выходной папки """
    replacing = (os.path.basename(os.path.dirname(from_path)),
                 os.path.basename(dst_folder))
    out_path = os.path.join(dst_folder, replacing[1]+".properties")
    with open(from_path, "r", encoding="utf-8") as f:
        content = f.read().replace("connectTiles="+replacing[0],
                                   "connectTiles="+replacing[1])

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)


def _move_png(ctm_img_path: str, dst_filename: str):
    """  """
    # Здесь:
    # ctm_img_path - картинка, являющаяся частью ctm на основе которой
    # нужно создать копии, но с другим материалом, используя её как
    # маску для прозрачности
    #
    # dst_filename - имя нового материала

    # Загружаем маску
    mask_img = Image.open(ctm_img_path)
    # mask_img = mask_img.convert("RGBA")

    # Загружаем дефолтную текстуру
    defult_texture = Image.open(os.path.join(default_path,
                                             dst_filename+".png"))
    # defult_texture = defult_texture.convert("RGBA")
    # Получаем массив пикселей
    default_data = defult_texture.getdata()

    newData = []
    for num, item in enumerate(mask_img.getdata()):
        if (item[3] != 0):
            # Если alpha текущего пикселя маски -
            # не 0, то оставляем пиксель текстуры
            newData.append(default_data[num])
        else:
            # Eсли же 0 - вставляем прозрачный пиксель
            newData.append(item)

    # Заменяем данные в текстуре и сохраняем в новое место
    defult_texture.putdata(newData)
    defult_texture.save(os.path.join)


def copy(from_name: str, dst_name: str):
    dst_path = os.path.join(ctm_path, dst_name)
    from_path = os.path.join(ctm_path, from_name)
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)
        print("Path created:", dst_path)

    if not os.path.exists(from_path):
        raise FileNotFoundError(from_path)

    for fn in os.listdir(from_path):
        filename, ext = fn.split(".")
        if ext == "properties":
            _move_properties(os.path.join(from_path, fn), filename)
        else:
            _move_png(os.path.join(from_path, fn), filename)
