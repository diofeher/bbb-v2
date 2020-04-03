# coding: utf-8
from PIL import Image
import math
import os
from utils import list_individual_images, break_captcha, save_candidate_name

READ_PATH = './classifier/images/'
SAVE_PATH = './classifier/pieces/'

if __name__ == '__main__':
    for name, image in list_individual_images(READ_PATH):
        lst = enumerate(break_captcha(READ_PATH, name, image))
        for i, (icon_name, captcha_image) in lst:
            save_candidate_name(SAVE_PATH, captcha_image, icon_name, i)
