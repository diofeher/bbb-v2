from utils import list_individual_images, break_captcha, save_candidate_name, save_image
import sys
import random
import os
import readline

READ_PATH = './src/classifier/pieces/'
SAVE_PATH = './src/classifier/classified/'
CAPTCHAS_TXT = './src/classifier/list_captchas.txt'

with open(CAPTCHAS_TXT, 'r') as fp:
    SOLVED = [i.strip() for i in fp.readlines()]

captchas = set([i.split('_')[0] for i in os.listdir(READ_PATH)])
[captchas.add(c) for c in SOLVED]

def completer(text, state):
    options = [i for i in captchas if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

readline.parse_and_bind("tab: complete")
readline.set_completer(completer)

if __name__ == "__main__":
    pieces = sorted(list_individual_images(READ_PATH))
    total = len(pieces)
    for i, (name, image) in enumerate(pieces):
        print(name, image)
        print('Count:', i, total)
        os.system(f'imgcat "{READ_PATH}{name}"')
        new_name = input('>')
        if new_name:
            new_filename = f"{SAVE_PATH}{new_name}_{random.randint(10000, 99999)}.png"
            image.save(new_filename)
