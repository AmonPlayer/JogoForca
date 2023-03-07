import random
from config import TENTATIVAS_ADICIONAIS, ARQUIVO_PALAVRAS_SECRETAS


def gerar_palavra_secreta():
    with open(ARQUIVO_PALAVRAS_SECRETASm, 'r') as f_obj:
        palavra = f_obj().splitlines()

    return random.choice(palavra)
