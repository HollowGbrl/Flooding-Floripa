arquivo_entrada ='FILE17V2.csv'
arquivo_saida = 'teste_rafa_5_6.csv'

import re
import pandas as pd
import time

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(arquivo_entrada, delimiter='\t')



#corrigindo virgulas e pontos para o formato americano
for column in df.columns:
  if column != 'time' and df[column].dtype == object:
    df[column] = df[column].str.replace(',', '.')
    df[column] = df[column].map(lambda x: re.sub(r'\.(?=.*\.)', '', x))
    df[column] = df[column].astype('float')

#setando os contadores auxiliares
contador1 = 0
oxy=0
pres=0
temp=0
sal=0
output_rows = []
#abrindo o arquivo que vai ser criado com o comando open
with open(arquivo_entrada, 'r', newline='') as entrada, open(arquivo_saida, 'w', newline='') as saida:
    saida.write('oxygen, pressure, temperature, salinity \n')
    #para cada 5 linhas, ele vai fazer a média de temperatura, salinidade e a mediana da pressão
    #e então escrever no arquivo novo.
    #se necessario, descomente os prints para visualizar o arquivo sendo modificado em tempo real.
    for index, row in df.iterrows(): 
        #print(contador1,':',  temp, 'original:', row['temperature'])
        oxy+=row['oxygen']
        if contador1==2:
            pres+=row['pressure']
        temp+=row['temperature']
        sal+=row['salinity']
        contador1 +=1
        if contador1 ==5:
            linha = f'{oxy/5}, {pres}, {temp/5}, {sal/5} \n'
            saida.write(linha)
            #print(linha)
            contador1= 0
            oxy=0
            pres=0
            temp=0
            sal=0
        