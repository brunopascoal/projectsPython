import pandas as pd
import glob
import os

locale = input("Digite o local onde estão os balancetes: ")
locale_first_export = input('Digite o local para primeira exportação: ')
name_first_export = input('Digite o nome do arquivo: ')
files = glob.glob(f'{locale}//*.xlsx')
list_months = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ' ]
#list_months = ['JAN22', 'FEV22', 'MAR22', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ' ]

xlwriter = pd.ExcelWriter(f'{locale_first_export}' + '\\' + f'{name_first_export}' + '.xlsx')
for i in range(len(files)):
    basename = os.path.basename(files[i])
    file_name = os.path.splitext(basename)[0]
    df = pd.read_excel(f"{files[i]}", engine='openpyxl')
    if len(file_name) > 31:
        df.to_excel(xlwriter, sheet_name=f'{file_name[:31]}', index=False)
    else: 
        df.to_excel(xlwriter, sheet_name=f'{file_name}', index=False)
        
xlwriter.close()

name_second_export = input('Digite o nome do arquivo final: ')

xlwriter = pd.ExcelWriter(f'{locale_first_export}' + '\\' +  f'{name_second_export}' + '.xlsx')
for i in range(len(list_months)):
    df = pd.read_excel(f'{locale_first_export}' + '\\' +  f'{name_first_export}' + '.xlsx', engine='openpyxl', sheet_name=f'BALANCETE_{list_months[i]}')
    df.to_excel(xlwriter, sheet_name=f'{list_months[i]}', index=False)
xlwriter.close()

os.remove(f'{locale_first_export}' + '\\' + f'{name_first_export}' + '.xlsx')
print('Operação realizada com sucesso!')