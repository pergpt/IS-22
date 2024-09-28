"""
Из исходного текстового файла (pazzl.html) выбрать все
html-коды изображений. Посчитать их количество
"""

import re

with open("pazzl.html", "r") as file:
    html_file = file.read()

img_tags = re.findall(r"<img.*?>", html_file)

img_count = len(img_tags)

print("Все теги img:", *img_tags, sep="\n")
print(f'Количество тегов "img": {img_count}')
