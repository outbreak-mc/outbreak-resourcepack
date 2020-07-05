import os
import sys
import traceback

from PIL import Image


def merge_normalmaps():
    """  """
    main_path = input("Гладкая карта с альфа-каналом > ")
    main_img = Image.open(main_path)
    second_img = Image.open(input("Шершавая карта для наложения > "))

    main_img = main_img.convert("RGBA")

    main_data = list(main_img.getdata())
    second_data = list(second_img.getdata())

    new_data = []
    for num, px in enumerate(second_data):
        px = list(px)
        alpha = main_data[num][3]

        new_data.append((*px[:3], alpha))

    main_img.putdata(new_data)
    main_img.save(main_path)


try:
    merge_normalmaps()
except:
    traceback.print_exc()

input("done")
