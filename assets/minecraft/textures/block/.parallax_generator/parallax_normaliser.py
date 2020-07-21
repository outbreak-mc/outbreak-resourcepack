import os
import sys
import traceback

from PIL import Image

""" Данный скрипт подгоняет альфа-канал у карт нормалей так, чтобы
    самая высокая точка была на максимально высокой позиции, т.е.
    чтобы текстура не была утоплена излишне глубоко.
    
    Для срабатывания необходимо просто перетащить картинки на скрипт,
    либо запустить и вставить путь.
    
    Картинки перезаписываются, бэкап делается в папку .pn_backup """


def normalise_parallax(img_path: str):
    img = Image.open(img_path)

    dirname = os.path.dirname(img_path)
    backup_folder = os.path.join(dirname, ".pn_backup")
    basename = os.path.basename(img_path)

    # Создаём папку для бэкапа
    if not os.path.exists(backup_folder):
        os.mkdir(backup_folder)
    # Делаем бэкап
    img.save(os.path.join(backup_folder, basename))

    data = list(img.getdata())

    max_height = 0
    min_height = 0

    for px in data:
        alpha = px[3]

        if alpha > max_height:
            max_height = alpha

        if alpha < min_height:
            min_height = alpha

    new_data = []

    offset = 255 - max_height

    for px in data:
        new_data.append((px[0], px[1], px[2], offset+px[3]))

    img.putdata(new_data)
    img.save(img_path)

    print("Срезано", offset, "прозрачности у", os.path.basename(img_path))


try:
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            normalise_parallax(arg)
    else:
        while True:
            normalise_parallax(input("> "))
except KeyboardInterrupt:
    quit()
except:
    print(traceback.format_exc())


input("done")
