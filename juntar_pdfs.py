import os
from PyPDF2 import PdfMerger
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog

# Cria uma janela tkinter e a esconde
root = tk.Tk()
root.withdraw()

# Mostra a caixa de diálogo para selecionar o diretório
diretorio_pdfs = filedialog.askdirectory(title="Selecione o diretório que contém seus arquivos PDF")

# Lista para armazenar os nomes dos arquivos PDF
pdfs = []

# Percorre todos os arquivos no diretório especificado
for arquivo in tqdm(os.listdir(diretorio_pdfs)):
    if arquivo.endswith('.pdf'):
        pdfs.append(os.path.join(diretorio_pdfs, arquivo))

# Cria um objeto PdfFileMerger
merger = PdfMerger()

# Adiciona cada PDF ao objeto PdfMerger
for pdf in pdfs:
    merger.append(pdf)

# Especifica o caminho de saída para o PDF concatenado
caminho_saida = os.path.join(diretorio_pdfs, "pdf_concatenado.pdf")

# Escreve o PDF concatenado no arquivo de saída
merger.write(caminho_saida)
merger.close()
