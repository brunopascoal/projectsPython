import glob
from pathlib import Path

locale = input("Digite o local onde estão os arquivos: ")
#list_months = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT']

files = glob.glob(f'{locale}//*')

with open("code.txt", "w") as arquivo:
    for i in range(len(files)):
        file_path = files[i]
        file_name = Path(file_path).stem

        texto = r""" dbName = "{file1}.IMD"
	Client.ImportPrintReportEx "C:\Users\bpascoal\Documents\Meus documentos do IDEA\Projetos IDEA\Unimed Avaré - Operadoras\Importar definições.ILB\Balancete 09.2023.jpm", "{file2}", dbname, FALSE, FALSE
	Client.OpenDatabase (dbName)
        """.format(file1 = file_name, file2 = file_path)

        arquivo.write(texto)
        arquivo.write("\n")
        print(texto)
