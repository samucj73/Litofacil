
def exportar_txt(cartoes, nome_arquivo="cartoes.txt"):
    caminho = f"/mnt/data/{nome_arquivo}"
    with open(caminho, "w") as f:
        for i, cartao in enumerate(cartoes, 1):
            f.write(f"Cartão {i}: {' - '.join(f'{n:02}' for n in cartao)}\n")
    return caminho

from fpdf import FPDF

def exportar_pdf(cartoes, nome_arquivo="cartoes.pdf"):
    caminho = f"/mnt/data/{nome_arquivo}"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for i, cartao in enumerate(cartoes, 1):
        linha = f"Cartão {i}: {' - '.join(f'{n:02}' for n in cartao)}"
        pdf.cell(200, 10, txt=linha, ln=True)
    pdf.output(caminho)
    return caminho
