import os
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog

def junta_arquivos(pasta_origem, arquivo_destino):
    arquivo_destino_abs = os.path.abspath(arquivo_destino).lower()  # Converte para caminho absoluto e minúsculas
    with open(arquivo_destino, 'w') as destino:
        for arquivo in tqdm(os.listdir(pasta_origem)):
            caminho_arquivo = os.path.join(pasta_origem, arquivo)
            if arquivo.lower().endswith('.txt'):
                caminho_arquivo_abs = os.path.abspath(caminho_arquivo).lower()  # Converte para caminho absoluto e minúsculas
                if caminho_arquivo_abs != arquivo_destino_abs:  # Compara os caminhos absolutos em minúsculas
                    with open(caminho_arquivo, 'r') as origem:
                        conteudo = origem.read()
                        if conteudo.strip():  # Verifica se o conteúdo não é apenas espaços em branco
                            destino.write(conteudo)
                            destino.write('\n')

# Configura a interface gráfica para não aparecer, apenas a caixa de diálogo
root = tk.Tk()
root.withdraw()

pasta_origem = filedialog.askdirectory(title="Selecione o diretório que contém seus arquivos TXT")
arquivo_destino = os.path.join(pasta_origem, "gerado.TXT")
junta_arquivos(pasta_origem, arquivo_destino)
