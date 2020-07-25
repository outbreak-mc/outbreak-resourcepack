import sys
import os
import traceback
from PIL import Image


def apply_heightmap(nm_path: str, hm_path: str, strength: float,
                    out_path: str):
    new_data = []

    nm_img = Image.open(nm_path)
    hm_img = Image.open(hm_path)

    nm_img = nm_img.convert("RGBA")
    # hm_img = hm_img.convert("RGBA")

    nm_data = nm_img.getdata()
    hm_data = list(hm_img.getdata())

    # print(hm_data)

    for num, px in enumerate(list(nm_data)):
        px = list(px)
        hm_px = hm_data[num]

        avg = int((hm_px[0]+hm_px[1]+hm_px[2])/3)

        diff = 255-avg

        px = [px[0], px[1], px[2], int(255-(diff*strength))]
        new_data.append(tuple(px))

    nm_img.putdata(new_data)

    filename = os.path.basename(nm_path)

    if out_path == "":
        out_path = os.path.join(".", filename)
    elif os.path.isdir(out_path):
        out_path = os.path.join(out_path, filename)

    nm_img.save(out_path)



try:
    apply_heightmap(
        input("normal map path > "),
        input("grayscale height map path > "),
        float(input("strength (0.0 - 1.0) > ")),
        input("out path > ")
    )
except:
    traceback.print_exc()
    input()