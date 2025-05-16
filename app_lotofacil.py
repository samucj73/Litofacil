
import streamlit as st
from gerador_lotofacil import gerar_varios_cartoes
from estatisticas_lotofacil import *
from util import exportar_txt, exportar_pdf

st.set_page_config(page_title="Lotofácil Inteligente", layout="centered")

# Título
st.title("🍀 Lotofácil Inteligente")
st.write("Gere cartões com base em estatísticas reais e critérios personalizados.")

# Simulação de resultados reais (substituir por leitura de base real depois)
ultimos_resultados = [
    [1, 2, 3, 6, 8, 10, 11, 12, 14, 16, 17, 19, 21, 24, 25],
    [2, 4, 5, 6, 7, 8, 10, 12, 13, 14, 17, 18, 21, 23, 25],
    [1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 22, 24],
    [1, 2, 4, 6, 8, 9, 11, 12, 13, 14, 15, 18, 20, 23, 24],
    [3, 5, 6, 7, 9, 10, 11, 12, 14, 15, 17, 18, 20, 22, 25]
]

# Estatísticas
st.subheader("📊 Estatísticas")
mais, menos = dezenas_mais_menos_sorteadas(ultimos_resultados)
st.write("Mais sorteadas:", mais)
st.write("Menos sorteadas:", menos)

trincas = trincas_mais_comuns(ultimos_resultados)
st.write("Trincas mais comuns:", trincas)

linhas, colunas = linhas_e_colunas(ultimos_resultados)
st.write("Frequência por linhas:", linhas)
st.write("Frequência por colunas:", colunas)

faixas = faixas_dezenas(ultimos_resultados)
st.write("Faixas mais sorteadas:", faixas)

ausentes = dezenas_ausentes(ultimos_resultados)
st.write("Dezenas ausentes:", ausentes)

# Geração de jogos
st.subheader("🎰 Gerador de Cartões")
qtd = st.slider("Quantos cartões deseja gerar?", 1, 10, 1)
fixas = st.multiselect("Dezenas fixas:", list(range(1, 26)))
excluir = st.multiselect("Dezenas a excluir:", list(range(1, 26)))
mais_s = [d for d, _ in mais]
menos_s = [d for d, _ in menos]

if st.button("Gerar Cartões"):
    jogos = gerar_varios_cartoes(qtd, fixas=fixas, excluir=excluir, mais_sorteadas=mais_s, menos_sorteadas=menos_s)
    for i, jogo in enumerate(jogos, 1):
        st.success(f"Cartão {i}: {' - '.join(f'{n:02}' for n in jogo)}")
    st.session_state.jogos = jogos

# Exportar
if 'jogos' in st.session_state:
    st.subheader("📥 Exportar")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬇️ Exportar .TXT"):
            caminho = exportar_txt(st.session_state.jogos, "cartoes_lotofacil.txt")
            st.success(f"Salvo em: {caminho}")
    with col2:
        if st.button("⬇️ Exportar .PDF"):
            caminho = exportar_pdf(st.session_state.jogos, "cartoes_lotofacil.pdf")
            st.success(f"Salvo em: {caminho}")
