import os
import sys
import shutil
import traceback
import datetime

from typing import Tuple

from PIL import Image

DIRPATH = os.path.dirname(os.path.abspath(__file__))

BACKUPS_PATH = os.path.join(DIRPATH, ".ptools_backups")


def _save_backup(filepath: str) -> str:
    """ Сохраняет копию файла в `BACKUPS_PATH`, возвращает
        конечный путь """
    datestr = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    filename, ext = os.path.basename(filepath).rsplit(".", 1)
    if not os.path.exists(BACKUPS_PATH):
        os.makedirs(BACKUPS_PATH)
    return shutil.copy(
        filepath,
        os.path.join(BACKUPS_PATH, filename+"-"+datestr+"."+ext)
    )


def _apply_heightmap(img_n: Image.Image, img_h: Image.Image) -> Image.Image:
    """ Применяет к карте нормалей `img_n` черно-белую карту
        высот `img_h`, возвращает получившуюся картинку с альфой. """
    img_n = img_n.convert("RGBA")

    nm_data = img_n.getdata()
    hm_data = list(img_h.getdata())

    new_data = []
    for num, px in enumerate(list(nm_data)):
        px = list(px)
        hm_px = hm_data[num]
        avg = int((hm_px[0]+hm_px[1]+hm_px[2])/3)

        px = [px[0], px[1], px[2], avg]
        new_data.append(tuple(px))

    img_n.putdata(new_data)
    return img_n


def _normalise_parallax(img: Image.Image) -> Tuple[Image.Image, int]:
    """ Срезает лишнюю прозрачность и возвращает кортеж:
        `(изображение, какое_значение_срезано)` """
    data = img.getdata()

    max_height = 0
    min_height = 0

    for px in data:
        alpha = px[3]

        if alpha > max_height:
            max_height = alpha

        if alpha < min_height:
            min_height = alpha

    offset = 255 - max_height

    new_data = []
    for px in data:
        new_data.append((px[0], px[1], px[2], offset+px[3]))

    img.putdata(new_data)

    return (img, offset)


def _generate_parallax(img: Image.Image) -> Image.Image:
    new_data = []
    img = img.convert("RGBA")
    for px in img.getdata():
        px = list(px)
        px = [px[0], px[1], px[2], px[2]]
        new_data.append(tuple(px))

    img.putdata(new_data)
    return img


class Job:
    def get_description(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError


class ApplyHeightmap(Job):
    def get_description(self):
        return "Apply a grayscale heightmap to normal map"

    def run(self):
        img_n_path = input("Normal map > ")
        img_h_path = input("Grayscale heightmap > ")

        print("Normal map backup saved as", _save_backup(img_n_path))

        img = _apply_heightmap(
            Image.open(img_n_path),
            Image.open(img_h_path)
        )
        img, offset = _normalise_parallax(img)
        print("Heightmap applied. Optimizing parallax...")
        print(offset, "transparency has been clipped.")
        img.save(img_n_path)


class GenerateParallax(Job):
    def get_description(self):
        return "Generate parallax based on normal map"

    def run(self):
        img_n_path = input("Normal map > ")
        print("Normal map backup saved as", _save_backup(img_n_path))
        _generate_parallax(Image.open(img_n_path)).save(img_n_path)


try:
    jobs: Tuple[Job] = (ApplyHeightmap(), GenerateParallax())
    print("Choose what to do:")
    for index, job in enumerate(jobs):
        print(index, "-", job.get_description())
    jobs[int(input("number > "))].run()

except:
    traceback.print_exc()
    print("\n\nDone with errors")
    input()
    input()
