import json
import os
import re
import shutil
import sys
import traceback
import zipfile
import argparse

from typing import List


PACK_FORMAT = 5

# Корень ресурспака
DIRPATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
BUILD_PATH = os.path.join(DIRPATH, "sources", "build")

ASSETS_PATH = os.path.join(DIRPATH, "assets")

EDITIONS_PATH = os.path.join(BUILD_PATH, "editions")


class Edition:
    """ Класс для описания особых версий ресурспака (например, 
        версии для игроков без шейдеров).  
        Для стандартной версии используется `Edition.default()`.

        Файлы особых версий хранятся в build/editions

        Объект содержит имя версии, суффикс для названия выходного
        файла, а также списки файлов для замены и исключения."""

    def __init__(self, name: str, suffix: str, exclude_files: List[str],
                 files: List[str]):
        self.name: str = name
        self.suffix: str = suffix
        self.exclude_files: List[str] = exclude_files
        self.files: List[str] = files
        self.root_path: str = os.path.join(EDITIONS_PATH, name)

    @classmethod
    def default(cls) -> "Edition":
        """ Стандартная версия """
        return cls(DIRPATH, "", [], [])

    def is_default(self) -> bool:
        return self.name == DIRPATH

    def exclude_check(self, path: str) -> bool:
        """ Проверяет путь на наличие его либо же его шаблона
            в списке исключаемых файлов """
        for expression in self.exclude_files:
            res = re.findall(expression, path)
            if len(res) != 0:
                for r in res:
                    if r == path:
                        return True
        return False

    @classmethod
    def load(cls, name: str) -> "Edition":
        path = os.path.join(EDITIONS_PATH, name)
        exclude_path = os.path.join(path, "exclude.txt")
        suffix_path = os.path.join(path, "suffix.txt")
        assets_path = os.path.join(path, "assets")

        with open(exclude_path, "r", encoding="utf-8") as f:
            exclude = [l.strip() for l in f.read().strip().split("\n")]

        with open(suffix_path, "r", encoding="utf-8") as f:
            suffix = f.read().strip()

        files = []
        for dirpath, _, filenames in os.walk(assets_path):
            for filename in filenames:
                rel = os.path.join(dirpath, filename).split(name)[-1]
                if rel.startswith(os.path.sep):
                    rel = rel[len(os.path.sep):]
                files.append(rel)
        return cls(name, suffix, exclude, files)


CONFIG_PATH = os.path.join(BUILD_PATH, "config.json")

ALLOWED_EXTENSIONS = ("png", "ogg", "mcmeta", "properties", "json")

parser = argparse.ArgumentParser(
    description=""" """,
    formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument("--zip", "--z", action="store_true",
                    help="Pack output to zip")
parser.add_argument("--edition", "--e", help="Select version to build")
parser.add_argument("--path", "--p", default=os.path.join(BUILD_PATH, "out"),
                    help="Output folder path")
parser.add_argument("--release", action="store_true",
                    help="Use only when making release version")


def make(out_path: str, edition: str, zip: bool) -> str:
    """ Собирает готовый ресурспак без лишних файлов
        в директории `out_path`.  

        Возвращает путь к результату.

        `edition` - какую версию собирать

        `zip` - создавать сразу в виде архива"""
    # Список путей к файлам ресурспака. Нам предстоит сначала собрать
    # все пути, а потом убрать из списка лишние файлы
    paths = []

    if not isinstance(edition, str):
        edition = Edition.default()
    else:
        edition = Edition.load(edition)

    out_path = os.path.abspath(out_path)

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)

    version = config["version"]
    description = config["description"]
    archive_description = config["archive_description"]
    name = config["name"]

    if args.release:
        version = "§e§o" + version + "§r"
    else:
        version = "§d§o" + version + "§r"

    # Формируем массив путей к файлам ресурспака
    # пути начинаются с assets/
    split_by = os.path.basename(DIRPATH)
    for dirpath, _, filenames in os.walk(ASSETS_PATH):
        for filename in filenames:
            rel = os.path.join(dirpath, filename).split(split_by)[-1]
            if rel.startswith(os.path.sep):
                rel = rel[len(os.path.sep):]
            paths.append(rel)

    # Отсеиваем лишние файлы:
    # - заменяемые edition.files
    # - исключаемые exclude_check
    # - содержащие точку в начале названия папки/файла
    # - с расширением, не входящим в ALLOWED_EXTENSIONS
    def verify_path(path: str) -> bool:
        """ Проверяет правильность пути """
        return (not os.path.sep+"." in path
                and not "."+os.path.sep in path
                and not path in edition.files
                and not edition.exclude_check(path)
                and path.split(".")[-1] in ALLOWED_EXTENSIONS)

    paths = [p for p in paths if verify_path(p)]

    # Составляем имя и описание
    pack_mcmeta = {
        "pack": {
            "pack_format": PACK_FORMAT,
            "description": description.format(version=version).strip()
        }
    }

    # Настало время записывать файлы

    # Формируем конечное название
    out_name = name + "-" + version
    if not edition.is_default():
        out_name += "_" + edition.suffix

    # Создаём папку для результатов
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    # Либо корневая папка ресурспака в результате, либо название архива
    out_folder = os.path.join(out_path, out_name)

    # Если zip == True, пакуем всё в архив и завершаем выполнение
    if zip:
        zipfile_name = out_folder + ".zip"
        with zipfile.ZipFile(zipfile_name, "w") as zip_obj:
            for path in paths:
                zip_obj.write(os.path.join(DIRPATH, path), path)
            for path in edition.files:
                zip_obj.write(os.path.join(edition.root_path, path), path)

            zip_obj.write(os.path.join(DIRPATH, "pack.png"), "./pack.png")
            zip_obj.writestr(
                "pack.mcmeta",
                json.dumps(pack_mcmeta, indent=4, ensure_ascii=False),
            )

            zip_obj.comment = archive_description.encode()
        return zipfile_name

    # Копируем файлы обычной версии и дополнительные файлы
    def copy_files(root_path, paths):
        for path in paths:
            src = os.path.join(root_path, path)
            dst = os.path.join(out_folder, path)
            dst_f = os.path.dirname(dst)
            if not os.path.exists(dst_f):
                os.makedirs(dst_f)
            shutil.copy(src, dst)

    copy_files(DIRPATH, paths)
    copy_files(edition.root_path, edition.files)

    # Копируем pack.png и создаём pack.mcmeta
    pack_png_path = os.path.join(DIRPATH, "pack.png")
    out_mcmeta_path = os.path.join(out_folder, "pack.mcmeta")
    if os.path.exists(pack_png_path):
        shutil.copy(pack_png_path, os.path.join(out_folder, "pack.png"))

    with open(out_mcmeta_path, "w", encoding="utf-8") as f:
        json.dump(pack_mcmeta, f, indent=4, ensure_ascii=False)

    return out_folder


try:
    args = parser.parse_args()
    make(args.path, args.edition, args.zip)
except SystemExit:
    exit()
except Exception:
    traceback.print_exc()
    input()
