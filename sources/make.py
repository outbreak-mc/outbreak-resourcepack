import os
import json

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PACK_MCMETA_PATH = os.path.join(dirpath, "pack.mcmeta")

ver = input("Resourcepack version > ")

SHADERS = "§e§o"
NO_SHADERS = "§a§o"

MC_1_14 = "§e§l1.14 - §e1.15"
MC_1_15 = "§e1.14 - §e§l1.15§e"

NO_SHADERS_EXCLUDE = ["_n.png", "_s.png"]
NO_SHADERS_ANALOGS_PATH = os.path.join(dirpath, "sources",
                                       "no_shaders_analogs")

configurations = {
    "1.14-no-shaders": {
        "ver": NO_SHADERS + ver,
        "mc_ver": MC_1_14
    },
    "1.15-no-shaders": {
        "ver": NO_SHADERS + ver,
        "mc_ver": MC_1_15
    },
    "1.14": {
        "ver": SHADERS + ver,
        "mc_ver": MC_1_14
    },
    "1.15": {
        "ver": SHADERS + ver,
        "mc_ver": MC_1_15
    },
}

desc = "§6§oOutbreak §e§o{ver}§7 by §6§oFeelinVoids_\n§e{mc_ver} §7• §cOptiFine required"

pack_mcmeta = {
   "pack": {
      "pack_format": 4,
      "description": desc
   }
}


for conf in configurations:
    with open(PACK_MCMETA_PATH, "w", encoding="utf-8") as f:
