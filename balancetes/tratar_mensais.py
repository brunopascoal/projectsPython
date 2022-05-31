import pandas as pd
import glob

locale = input("Digite o local onde estão os arquivos: ")
files = glob.glob(f'{locale}//*.xlsx')
list_months = ['ABR', 'AGO', 'DEZ', 'FEV', 'JAN', 'JUL', 'JUN', 'MAI', 'MAR', 'NOV', 'OUT', 'SET']



for i in range(len(files)):
    df = pd.read_excel(f"{files[i]}", engine='openpyxl')
    df = df[pd.notnull(df['CONTA'])]
    df = df[pd.notnull(df['DESCRIÇÃO_DA_CONTA'])]
    df.drop(df.loc[df['CONTA']=='Conta'].index, inplace=True)
    df = df.reindex(columns=['TIPO', 'CONTA', 'DESCRIÇÃO_DA_CONTA', f'SALDO_I_{list_months[i]}', f'DEB_{list_months[i]}', f'CRE_{list_months[i]}', f'SALDO_F_{list_months[i]}', f'MOV_{list_months[i]}'])
    df.to_excel(files[i], sheet_name='Database', index=False)