import os
import shutil
import traceback

from PIL import Image  # pip install pillow

# Скрипт ищет значки в ./book_icons и рамки уровней в ./book_levels.
# Создаёт все варианты книг всех зачарований всех уровней, накладывая
# картинки друг на друга а также создаёт для каждой из получившихся
# картинок файл .properties.

dirpath = os.path.abspath(os.path.dirname(__file__))

icons_path = os.path.join(dirpath, "book_icons")
levels_path = os.path.join(dirpath, "book_levels")
original_path = os.path.join(dirpath, "enchanted_book.png")

optifine_path = os.path.join(
    os.path.dirname(os.path.dirname(dirpath)),
    "assets",
    "minecraft",
    "optifine"
)

# max levels
enchantments = {
    "protection": 4,
    "aqua_affinity": 1,
    "bane_of_arthropods": 5,
    "blast_protection": 4,
    "channeling": 1,
    "binding_curse": 1,
    "vanishing_curse": 1,
    "depth_strider": 3,
    "efficiency": 5,
    "feather_falling": 4,
    "fire_aspect": 2,
    "fire_protection": 4,
    "flame": 1,
    "fortune": 3,
    "frost_walker": 2,
    "impaling": 5,
    "infinity": 1,
    "knockback": 2,
    "looting": 3,
    "loyalty": 3,
    "looting": 3,
    "luck_of_the_sea": 3,
    "lure": 3,
    "mending": 1,
    "multishot": 1,
    "piercing": 4,
    "power": 5,
    "projectile_protection": 4,
    "punch": 2,
    "quick_charge": 3,
    "respiration": 3,
    "riptide": 3,
    "sharpness": 5,
    "silk_touch": 1,
    "smite": 5,
    "sweeping": 3,
    "thorns": 3,
    "unbreaking": 3,
}

level_frames = (
    Image.open(os.path.join(levels_path, "1.png")),
    Image.open(os.path.join(levels_path, "2.png")),
    Image.open(os.path.join(levels_path, "3.png")),
    Image.open(os.path.join(levels_path, "4.png")),
    Image.open(os.path.join(levels_path, "5.png"))
)


def make_books():
    folders = []
    for f in os.listdir(dirpath):
        if os.path.isdir(f):
            folders.append(f)

    def jsonToProperties(j):
        return "\n".join([k+"="+str(j[k]) for k in j])

    for tex_name in os.listdir(icons_path):
        print(tex_name)

        ench_name = tex_name.split(".")[0]
        # assets/minecraft/optifine/cit/books/<enchantment_name>
        cit_book_path = os.path.join(optifine_path, "cit", "books", ench_name)

        if not os.path.exists(cit_book_path):
            os.makedirs(cit_book_path)

        for l in range(enchantments[ench_name]):
            book = Image.open(original_path)
            icon = Image.open(os.path.join(icons_path, tex_name))
            level = level_frames[l]

            book.paste(level, (0, 0), level)
            book.paste(icon, (0, 0), icon)

            filename = ench_name+"_"+str(l)
            print(os.path.join(cit_book_path, filename+".png"))
            book.save(os.path.join(cit_book_path, filename+".png"))

            with open(os.path.join(cit_book_path, filename+".properties"), "w") as f:
                j = {
                    "type": "item",
                    "items": "minecraft:enchanted_book",
                    "enchantmentIDs": "minecraft:"+ench_name,
                    "enchantmentLevels": str(l+1)
                }
                f.write(jsonToProperties(j))


try:
    make_books()
except:
    traceback.print_exc()

input("\ndone")
