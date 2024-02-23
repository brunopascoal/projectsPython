import os

# Defina o caminho da pasta onde estão os arquivos .htm
diretorio = r'C:\Users\bpascoal\Documents\Meus documentos do IDEA\Projetos IDEA\Capul\Arquivos fonte.ILB\Estoque'

# Defina o nome do arquivo de saída
arquivo_saida = r'C:\Users\bpascoal\Documents\Meus documentos do IDEA\Projetos IDEA\Capul\Arquivos fonte.ILB\Estoque\saida_concatenada.htm'

# Inicializa uma variável para armazenar o conteúdo concatenado
conteudo_concatenado = ''

# Percorre todos os arquivos no diretório especificado
for arquivo in os.listdir(diretorio):
    # Verifica se o arquivo é um arquivo .htm
    if arquivo.endswith('.htm'):
        # Constrói o caminho completo do arquivo
        caminho_arquivo = os.path.join(diretorio, arquivo)
        
        # Abre o arquivo para leitura
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            # Lê o conteúdo do arquivo e o adiciona à variável de concatenação
            conteudo_concatenado += f.read() + '\n'  # Adiciona uma nova linha entre os arquivos para separação

# Salva o conteúdo concatenado em um novo arquivo
with open(os.path.join(diretorio, arquivo_saida), 'w', encoding='utf-8') as f_saida:
    f_saida.write(conteudo_concatenado)

print('Arquivos .htm concatenados com sucesso em', arquivo_saida)
