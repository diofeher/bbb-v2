from utils import list_individual_images, break_captcha, save_candidate_name, save_image
import sys
import random
import os
import readline

READ_PATH = './classifier/pieces/'
SAVE_PATH = './classifier/classified/'

SOLVED = [
    'ampulheta', 'ancora', 'anel', 'apito', 'arco e flecha', 'aviao', 'balao',
    'baleia', 'bandeira', 'barco', 'bicicleta', 'bigode', 'bolo', 'bolsa', 'bota',
    'cabelo', 'cachorro', 'cadeado', 'cadeira', 'caixa', 'calca', 'calendario',
    'camera', 'caminhao', 'caneca', 'carrinho de bebe', 'carro', 'cartao', 'casa',
    'cavalo', 'celular', 'chapeu', 'chave', 'churrasqueira', 'colher', 'comida japonesa', 'computador', 'copo', 'coracao', 'coroa', 'dado', 'despertador',
    'diamante', 'dinossauro', 'disquete', 'elefante', 'engrenagem', 'envelope',
    'escadas', 'esquadro', 'faca', 'ferramenta', 'flor', 'fogo', 'folha', 'fone de ouvido', 'formiga', 'futebol', 'garrafa', 'gato', 'girafa', 'gota', 'guarda-chuva', 'halter', 'helicoptero', 'impressora', 'instrumento musical', 'janela', 'lampada', 'lanterna', 'lapis', 'letra', 'livro', 'lixeira', 'lua',
    'luminaria', 'mala', 'mao', 'martelo', 'mascara', 'meia', 'mesa', 'microfone',
    'mochila', 'moeda', 'moto', 'navio', 'neve', 'nota musical', 'numero', 'nuvem',
    'oculos', 'olho', 'onda', 'onibus', 'pao', 'passaro', 'peixe', 'pessoa',
    'peteca', 'pia', 'pincel', 'piramide', 'placa', 'planeta', 'pocao', 'porta',
    'predio', 'raquete', 'relogio', 'robo', 'secador de cabelo', 'semaforo',
    'seta', 'sino', 'sofa', 'sol', 'sorvete', 'tanque militar', 'telefone',
    'trofeu', 'tv', 'ventilador',
]

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
