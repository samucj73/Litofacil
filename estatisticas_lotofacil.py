
from collections import Counter
from itertools import combinations

def dezenas_mais_menos_sorteadas(resultados, top=5):
    contagem = Counter([d for r in resultados for d in r])
    mais = contagem.most_common(top)
    menos = contagem.most_common()[:-top-1:-1]
    return mais, menos

def trincas_mais_comuns(resultados, top=5):
    trincas = []
    for r in resultados:
        trincas.extend(combinations(sorted(r), 3))
    contagem = Counter(trincas)
    return contagem.most_common(top)

def linhas_e_colunas(resultados):
    linhas = {i: 0 for i in range(1, 6)}
    colunas = {i: 0 for i in range(1, 6)}
    for jogo in resultados:
        for d in jogo:
            linha = (d - 1) // 5 + 1
            coluna = (d - 1) % 5 + 1
            linhas[linha] += 1
            colunas[coluna] += 1
    return linhas, colunas

def faixas_dezenas(resultados):
    faixas = {'01-10': 0, '11-20': 0, '21-25': 0}
    for jogo in resultados:
        for d in jogo:
            if d <= 10:
                faixas['01-10'] += 1
            elif d <= 20:
                faixas['11-20'] += 1
            else:
                faixas['21-25'] += 1
    return faixas

def dezenas_ausentes(resultados, total=25):
    todas = set(range(1, total + 1))
    presentes = set([d for r in resultados for d in r])
    return sorted(todas - presentes)
