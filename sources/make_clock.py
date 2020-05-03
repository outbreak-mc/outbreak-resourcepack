import json
import os
import shutil
from typing import Optional


def generate_clock(frames_folder_path: str,
                   minecraft_path: str,
                   custom_parent_model: Optional[str] = None,
                   credit: Optional[str] = None,
                   texture_name: str = "layer0",
                   json_indent=4,
                   sort_by_date=True):
    """ Генерирует файлы для создания часов любой точности

        `frames_folder_path` - папка с кадрами. Будут использованы все
        найденные в ней текстуры, от их количества зависит 
        точность часов.

        `minecraft_path` - путь к папке `assets/minecraft` ресурспака 

        `custom_parent_model` - путь к родительской модели

        `credit` - поле `"credit"` в json-файлах

        `texture_name` - имя текстуры в материалах модели

        `json_indent` - форматирование json

        `sort_by_date` - получать файлы из папки в порядке последнего
        редактирования. Если `False` - файлы будут отсортированы 
        по алфавиту """

    # minecraft_path = os.path.join(os.getenv("appdata"),
    #                               ".minecraft", "resourcepacks")
    template = {
        # "parent": "item/clock_model",
        "textures": {
            # "layer0": "item/clock_00"
        }
    }

    if credit:
        template["credit"] = credit

    # Если передано custom_parent_model, будем использовать
    # родительскую модель.
    if custom_parent_model is not None:
        template["parent"] = "item/clock/clock_parent"
    else:
        template["parent"] = "item/generated"

    filenames = os.listdir(frames_folder_path)
    filenames = [f for f in filenames if f.endswith(".png")]

    accuracy = len(filenames)

    if accuracy == 0:
        raise FileNotFoundError("No texture files found in " +
                                frames_folder_path)

    overrides = []
    # Генерируем overrides для первой модели по шаблону:
    # { "predicate": { "time": (1/x)*i }, "model": "item/clock_"+str(i) }
    # Где x - количество заготовленных текстур, а i - итерация
    for i in range(accuracy):
        overrides.append(
            {
                "predicate": {"time": (1/accuracy)*i},
                "model": "item/clock/clock_"+str(i)
            }
        )
        # Первая модель не будет лежать в папке clock
        # и будет иметь название clock
        overrides[0]["model"] = "item/clock"

    #
    # Генерируем модели
    #

    models_path = os.path.join(minecraft_path, "models", "item", "clock")

    if not os.path.exists(models_path):
        os.makedirs(models_path)

    # Если использовано custom_parent_model, записываем clock_parent
    if custom_parent_model is not None:
        shutil.copy(custom_parent_model,
                    os.path.join(models_path, "clock_parent.json"))

    # Создаём все файлы моделей
    for i in reversed(range(accuracy)):
        # Первая модель должна иметь имя clock.json
        # и НЕ должна лежать в отдельной папке
        if i == 0:
            path = os.path.join(os.path.dirname(models_path), "clock.json")
        else:
            path = os.path.join(models_path, f"clock_{i}.json")

        with open(path, "w", encoding="utf-8") as f:
            # В первом необходимо прописать overrides
            if i == 0:
                template["overrides"] = overrides
                template["textures"][texture_name] = f"item/clock/clock_{i}"
            else:
                template["textures"][texture_name] = f"item/clock/clock_{i}"
            json.dump(template, f, indent=json_indent, ensure_ascii=False)

    #
    # Копируем текстуры в нужную папку
    #

    textures_path = os.path.join(
        minecraft_path, "textures", "item", "clock")
    if not os.path.exists(textures_path):
        os.makedirs(textures_path)

    # Сортируем имена по алфавиту или по дате
    if sort_by_date:
        def k(f):
            return os.path.getmtime(os.path.join(frames_folder_path, f))
    else:
        k = None

    filenames = sorted(filenames, key=k)

    for num, fn in enumerate(filenames):
        src = os.path.join(frames_folder_path, fn)
        dst = os.path.join(textures_path, f"clock_{num}.png")
        print(src, dst)
        shutil.copy(src, dst)


dirpath = os.path.dirname(os.path.abspath(__file__))
mcpath = os.path.join(os.path.dirname(dirpath), "assets", "minecraft")
print(mcpath)
parent = os.path.join(mcpath, "models", "item", "clock_parent.json")

generate_clock(os.path.join(dirpath, "clock"), mcpath, custom_parent_model=parent)
