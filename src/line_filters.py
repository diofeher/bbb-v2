from PIL import Image, ImageFilter
import numpy as np


def findLineStart(img: Image.Image):
    img_array = np.array(img)
    coordinates = []

    for collum_index, collum in enumerate(np.transpose(img_array)):
        # verifica se há apenas as 5 linhas
        if np.count_nonzero(collum < 255) != 5:
            continue

        line_indexs = np.where(collum < 255)[0]

        # verifica se essas são as linhas iniciais
        if np.all(img_array.transpose()[collum_index - 1][line_indexs] < 255):
            continue

        coordinates.append((collum_index, line_indexs))
    return coordinates

def removePoint(img: Image.Image, x:int , y: int):
    px = img.load()
    interpolation = (px[x, y-1] + px[x, y+1])//2
    img.putpixel((x, y), interpolation)


def removeLines(img: Image.Image, coordinates) -> Image.Image:
    for collum_index, line_indexs in coordinates:
        for line_index in line_indexs:
            # a linha sempre dura 45px
            for i in range(45 + 1):
                removePoint(img, collum_index + i, int(line_index))
    return img


def lineFilter(img: Image.Image) -> Image.Image:
    img = img.convert("L")
    coordinates = findLineStart(img)
    return removeLines(img, coordinates)
