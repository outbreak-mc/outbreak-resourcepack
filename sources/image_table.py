import os

# Генерирует таблицу скриншотов для README.md

path = r"C:\Users\FeelinVoids_\AppData\Roaming\.minecraft\resourcepacks\outbreak-resourcepack\sources\screenshots\guns"

path = os.path.abspath(path)

files = os.listdir(path)

table = ("Первое лицо | Третье лицо\n"
         "----------- | -----------")
for i in range(len(files)):
    if (i % 2 == 1):
        continue
    current = files[i]
    next = files[i+1]
    table += f"\n![{current}](./sources/screenshots/guns/{current}) | ![{next}](./sources/screenshots/guns/{next})"

print(table)

input()
