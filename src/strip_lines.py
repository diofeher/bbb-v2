import os
from PIL import Image
from line_filters import lineFilter

i = 0
for img_path in os.listdir('images_individual'):
    if img_path[-4:] == ".png":
        img = Image.open('images_individual/' + img_path)
        newImg = lineFilter(img)
        newImg.save('images_individual/' + img_path)
        i += 1
    print('total', i)
