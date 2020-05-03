from PIL import Image
import os
import shutil
from copy import copy


def generate_potions(mob_effect_path, potion, lingering_potion,
                     splash_potion, potion_overlay, out_mc_path):
    effects = {
        f.split(".")[0]: Image.open(os.path.join(mob_effect_path, f))
        for f in os.listdir(mob_effect_path)
    }

    types = [(potion, "normal"), (lingering_potion, "linger"),
             (splash_potion, "splash")]

    for potion_type in types:
        potion: Image = Image.open(potion_type[0])

        for effect, icon in effects.items():
            p = copy(potion)
            p.paste(icon, (0, 0), icon)

            path = os.path.join(out_mc_path, "optifine", "cit",
                                "potion", potion_type[1], effect+".png")

            print(path)

            dn = os.path.dirname(path)
            if not os.path.exists(dn):
                os.makedirs(dn)

            p.save(path)

    shutil.copy(
        potion_overlay,
        os.path.join(out_mc_path, "textures", "item", "potion_overlay.png")
    )


dirpath = os.path.abspath(os.path.dirname(__file__))

generate_potions(
    os.path.join(dirpath, "potions", "mob_effect"),
    os.path.join(dirpath, "potions", "potion.png"),
    os.path.join(dirpath, "potions", "lingering_potion.png"),
    os.path.join(dirpath, "potions", "splash_potion.png"),
    os.path.join(dirpath, "potions", "potion_overlay.png"),
    os.path.join(os.path.dirname(dirpath), "assets", "minecraft"),
)
