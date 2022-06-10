#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os
from openpyxl import load_workbook
from openpyxl.drawing.image import Image 

def contruction_graph(locale, locale_file, df, file_name):

    df.index = np.arange(1, len(df) +1)
    #display(df)
    mean_desejavel = df['Nota desejada'].mean()
    mean_real = df['Ponto Real'].mean()
    x = df.index
    
    fig, ax = plt.subplots(figsize=(12, 6));

    width = 0.2
    ax.bar(x-0.2, df["Nota desejada"], width, edgecolor = 'black', label='Nota desejável', color='black')
    ax.bar(x, df["Ponto Real"], width, label='Real', color='blue')
    ax.bar(x+0.2, df["Ponto Autoavaliação"], width, label='Auto', color='grey')
    #ax.annotate(f'Média desejavel: {round(mean_desejavel, 2)}', xy=(1, 10))
    #ax.annotate(f'Média Real: {round(mean_real, 2)}', xy=(1, 11))

    plt.xticks(x, x, rotation=20)


    plt.title(f'{file_name}', color='white', fontsize=16)
    plt.xlabel('Competência', color='white', fontsize=16)
    plt.ylabel('Valores',  color='white', fontsize=16)
    plt.legend()
    plt.savefig(f'{locale}\\{file_name}.png')
    plt.show()
    
    

# locale = input("Digite o local dos arquivos: ")
# files = glob.glob(f'{locale}//*.xlsx')

# for i in range(len(files)):
#     df = pd.read_excel(files[i], engine='openpyxl')
#     basename = os.path.basename(files[i])
#     file_name = os.path.splitext(basename)[0]
#     contruction_graph(locale, files[i], df, file_name)
