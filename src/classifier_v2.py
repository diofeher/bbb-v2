from utils import save_image, break_captcha
import tkinter as ttk
from PIL import Image
from base64 import b64encode
import io
from os import listdir
from random import randint

UNCLASSIFIED_PATH = './src/images/'
SAVE_PATH = './src/images_individual/'


def openInterface(file_name):
    icon = file_name.split('/')[-1].split('_')[0]
    image = Image.open(file_name)

    if image.size != (265, 53):
        return

    root = ttk.Tk()
    ttk.Label(root, text=f'Click in {icon}', font=(
        'Verdana', 15)).pack(side=ttk.TOP, pady=10)
    # add PhotoImage here to not garbage colector
    # https://stackoverflow.com/questions/33987792/tkinter-cant-open-multiple-photos-at-the-same-time-python
    protoImgArray = []
    for _, sub_img in break_captcha(UNCLASSIFIED_PATH + 'sub/', icon, image):
        imgByteArr = io.BytesIO()
        sub_img.save(imgByteArr, format='GIF')
        imgByteArr = imgByteArr.getvalue()
        photoButton = ttk.PhotoImage(data=b64encode(imgByteArr))
        protoImgArray.append(photoButton)
        ttk.Button(root, command=saveNewClassified(icon, sub_img),
                   image=photoButton).pack(side=ttk.LEFT, pady=5, padx=5)
    ttk.mainloop()


def runInFolder():
    for f in listdir(UNCLASSIFIED_PATH):
        if f.split('.')[-1] != 'png':
            continue
        openInterface(UNCLASSIFIED_PATH + f)


def saveNewClassified(icon, image):
    new_filename = f"{SAVE_PATH}{icon}_{randint(10000, 99999)}.png"
    image.save(new_filename)

if __name__ == "__main__":
    runInFolder()
