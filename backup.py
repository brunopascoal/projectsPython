import os
from zipfile import ZipFile

def zipar_pasta(pasta, nome_zip):
    # Cria um arquivo zip para a pasta
    with ZipFile(nome_zip, 'w') as zipf:
        # Raiz da pasta a ser zipada
        comprimento_raiz = len(os.path.dirname(pasta))
        # Caminha por todos os diretórios e arquivos dentro da pasta
        for raiz, diretorios, arquivos in os.walk(pasta):
            # Adiciona cada arquivo ao arquivo zip
            for arquivo in arquivos:
                # Caminho absoluto do arquivo
                caminho_absoluto = os.path.join(raiz, arquivo)
                # Nome do arquivo dentro do zip, incluindo o caminho relativo
                nome_arquivo_zip = caminho_absoluto[comprimento_raiz:]  # Remove parte desnecessária do caminho
                zipf.write(caminho_absoluto, nome_arquivo_zip)

        print(f"Pasta {pasta} zipada com sucesso como {nome_zip}")

# Defina o caminho da pasta que contém as pastas a serem zipadas
diretorio_raiz = r'C:\Users\bpascoal\Documents\Meus documentos do IDEA\Projetos IDEA'

# Lista todas as subpastas no diretório raiz
for pasta in os.listdir(diretorio_raiz):
    caminho_pasta = os.path.join(diretorio_raiz, pasta)
    
    # Verifica se é uma pasta
    if os.path.isdir(caminho_pasta):
        nome_zip = f"{caminho_pasta}.zip"
        zipar_pasta(caminho_pasta, nome_zip)
