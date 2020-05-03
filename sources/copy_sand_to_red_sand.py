import os
from PIL import Image
dirpath = os.path.dirname(os.path.abspath(__file__))

red_sand_path = ""

red_sand = Image.open(red_sand_path)
red_sand_datas = red_sand.getdata()

for fn in os.listdir(dirpath):
    if not fn.endswith(".png"):
        continue
    
    
    fp = os.path.join(dirpath, fn)

    img = Image.open(fp)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for num,item in enumerate(datas):
        if (item[3] != 0):
            newData.append(red_sand_datas[num])
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(fp)
