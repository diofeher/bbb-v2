import os
from PIL import Image
import string
import base64
import json
import unicodedata
from colorama import Fore


SIZE = 5


def save_candidate_name(path, image, icon_name, count):
    image.save(path + handle_name(icon_name) + '_' + str(count) + '.png')


def save_tmp_name(image, icon_name, count):
    image.save('./src/images_tmp/' + handle_name(icon_name) + '_' + str(count) + '.png')


def list_individual_images(path):
    for f in os.listdir(path):
        if f in [".DS_Store", ".gitkeep"]:
            continue
        filename = path + f
        image = Image.open(filename)
        yield f, image


def break_captcha(path, icon_name, image):
    total_width = image.size[0]
    total_height = image.size[1]
    width_icon = total_width / SIZE

    for i, col in enumerate(range(0, total_width, int(width_icon))):
        coords = (col, 0, col+width_icon, total_height)
        image_icon = image.crop(coords)
        save_candidate_name(path, image_icon, icon_name, i)
        yield icon_name, image_icon


chars = string.ascii_letters + ' ' + '_' + string.digits

def handle_name(data):
    return ''.join(x for x in unicodedata.normalize('NFKD', data) if x in chars).lower()


def save_image(folder, icon, data_b64):
    filename = f"{folder}{handle_name(icon)}.png"
    with open(filename, "wb") as fh:
        fh.write(base64.urlsafe_b64decode(data_b64))


from http.cookies import SimpleCookie

def cookie_string_to_mapping(text):
    cookie = SimpleCookie()
    cookie.load(text)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    return cookies


def read_configuration_file():
    with open('./config.json') as file:
        arguments = json.load(file)

    credentials = arguments['credentials']
    try:
        username = credentials[0]['username']
        password = credentials[0]['password']
    except IndexError as e:
        raise Exception(Fore.RED + "Você precisa preencher pelo menos um nome de usuário e senha.")
    return arguments
