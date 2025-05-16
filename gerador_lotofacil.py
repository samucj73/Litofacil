
import random

def gerar_cartao_personalizado(mais_sorteadas=[], menos_sorteadas=[], fixas=[], excluir=[], total=15):
    dezenas_possiveis = set(range(1, 26)) - set(excluir)
    dezenas_possiveis.update(fixas)
    base = list(dezenas_possiveis - set(fixas))
    random.shuffle(base)
    complemento = [d for d in base if d not in fixas][:total - len(fixas)]
    cartao = sorted(fixas + complemento)
    return cartao

def gerar_varios_cartoes(qtd, **kwargs):
    return [gerar_cartao_personalizado(**kwargs) for _ in range(qtd)]
