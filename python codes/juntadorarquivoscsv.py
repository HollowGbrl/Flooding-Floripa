import os
import time
import pandas as pd

#caminho do diretorio que vai trabar
caminho_pasta= "dados_casan/junto"
maregrafo= 0
#codigo que vai fazer ele criar uma lista dos arquivos do diretorio

lista_arquivos = [f for f in os.listdir(caminho_pasta) if os.path.isfile(os.path.join(caminho_pasta, f))]
print('comecei')
df= pd.DataFrame()
for nome_arquivo in lista_arquivos:
    print('abrindo arquivo: ', nome_arquivo)
    #vai chamar o arquivo como "arquivo"
    arquivo = os.path.join(caminho_pasta, nome_arquivo)
    # Open the Excel file using pandas
    df2 = pd.read_excel(arquivo, sheet_name=maregrafo)
    segunda = df2.columns[1]
    df2 = df2[round(df2[segunda], 2) != 0]
    df2[segunda]= df2[segunda] - df2[segunda].mean()
    df= pd.concat([df, df2], ignore_index=True)
    
    print(f'fiz arquivo: {nome_arquivo}')

df.to_csv('dados_casan/processado/juntos_ponte.csv')
    
    
