import math
import os
import sys
import traceback

from PIL import Image

dirpath = os.path.dirname(os.path.abspath(__file__))


def split_image(img_path: str, tiles_in_row: int = 2):
    basename = os.path.basename(img_path).split(".")[0]

    prefix = ""
    if "_" in basename:
        prefix = "_"+"_".join(basename.split("_")[1:])

    print("Splitting", basename)
    img = Image.open(img_path)

    tiles = []

    tile_size = img.size[0]/tiles_in_row

    for i in range(tiles_in_row):
        for j in range(tiles_in_row):
            tiles.append(img.crop((tile_size*j,
                                   tile_size*i,
                                   tile_size*(j+1),
                                   tile_size*(i+1))))

    folder = os.path.join(dirpath, basename)
    if not os.path.exists(folder):
        os.mkdir(folder)

    # tiles.reverse()

    for num, tile in enumerate(tiles):
        tile.save(os.path.join(folder, str(num)+prefix+".png"))

try:
    tiles_in_row = int(input("Tiles in row > "))
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            split_image(arg, tiles_in_row)
    else:
        split_image(input("> "), tiles_in_row)
except:
    print(traceback.format_exc())

input("done")
