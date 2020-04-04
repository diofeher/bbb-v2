import cv2
import numpy as np
from PIL import Image
from utils import list_individual_images, break_captcha, handle_name
import sys


READ_CAPTCHA_PATH = './images/'
PATH_EXISTENT = './images_individual/'


def calculate_diff(img1, img2):
    matcher = cv2.xfeatures2d.SIFT_create(nfeatures=100)
    # surf = cv2.xfeatures2d.SURF_create()
    # matcher = cv2.ORB_create(edgeThreshold=1)
    # find the keypoints and descriptors with SIFT
    kp1, des1 = matcher.detectAndCompute(img1,None)
    kp2, des2 = matcher.detectAndCompute(img2,None)

    # BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.match(des1, des2)

    matches = sorted(matches, key=lambda val: val.distance)
    score = sum([i.distance for i in matches])
    return score


def compare_image(image1, image2):
    img1 = cv2.imread(image1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image2, cv2.IMREAD_GRAYSCALE)
    diff = calculate_diff(img1, img2)
    return diff


def compare(target):
    target = handle_name(target)
    image_png = Image.open('./images/'+target+'.png')
    matched_diff = sys.maxsize
    match = ''
    match_pos = None

    for i, (captcha_name, captcha_image) in enumerate(break_captcha(READ_CAPTCHA_PATH, target, image_png)):
        for name, image in list_individual_images(PATH_EXISTENT):
            if target not in handle_name(name):
                continue
            captcha_part = READ_CAPTCHA_PATH + captcha_name + '_' + str(i) + '.png'
            existent_image_path = PATH_EXISTENT + name
            diff = compare_image(existent_image_path, captcha_part)
            if diff < matched_diff:
                matched_diff = diff
                match = existent_image_path
                match_pos = i

    return match_pos


if __name__ == '__main__':
    try:
        target = handle_name(sys.argv[1]).lower()
    except IndexError:
        print('You need to specify a target')
        print('python3 compare_images.py <icon-name>')
        sys.exit()

    print(compare(target))
