import os
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog

def junta_arquivos(pasta_origem, arquivo_destino):
    with open(arquivo_destino, 'w') as destino:
        for arquivo in tqdm(os.listdir(pasta_origem)):
            caminho_arquivo = os.path.join(pasta_origem, arquivo)
            # Ignora o arquivo de destino para evitar duplicação
            if caminho_arquivo == arquivo_destino:
                continue
            if arquivo.lower().endswith('.wri'):  # Aceita tanto '.wri' quanto '.WRI'
                with open(caminho_arquivo, 'r') as origem:
                    conteudo = origem.read()
                    if conteudo.strip():  # Verifica se o conteúdo não é apenas espaços em branco
                        # Escreve o nome do arquivo no início
                        destino.write("Nome do arquivo: \"" + arquivo + "\"\n")
                        destino.write(conteudo)
                        destino.write('\n\n')  # Dois saltos de linha para melhor separação entre os arquivos

root = tk.Tk()
root.withdraw()  # Para não abrir a janela do Tkinter

pasta_origem = filedialog.askdirectory(title="Selecione o diretório que contém seus arquivos wri")
arquivo_destino = os.path.join(pasta_origem, "gerado.wri")
junta_arquivos(pasta_origem, arquivo_destino)
