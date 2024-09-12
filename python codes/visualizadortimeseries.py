import pandas
import matplotlib.pyplot as plt
import time

arquivo= 'dados_daniel/imbi_718_2001_2022_atualizado.txt'

def leitor_de_linhas():
    with open(arquivo, 'r') as f:
        for line in f:
            print(line)
            time.sleep(1)

mare = pandas.read_csv(arquivo, sep='\t')

mare['data'] = mare['data'] + ' ' + mare['hora']
mare['data'] = pandas.to_datetime(mare['data'], format='%d/%m/%Y %H:%M')
mare['nivelobs'] = mare['nivelobs'] - mare['nivelobs'].mean()
mare['nivelprs'] = mare['nivelprs'] - mare['nivelprs'].mean()


mare2= pandas.read_csv('dados_daniel/imbi_718_2001_2021.txt', sep='\t')
mare2['data'] = mare2['data'] + ' ' + mare2['hora']
mare2['data'] = pandas.to_datetime(mare2['data'], format='%d/%m/%Y %H:%M')
mare2['nivel'] = mare2['nivel'] + 1
mare.drop(columns=['hora'], inplace=True)


mare = mare[(mare['data'].dt.year >= 2019) & (mare['data'].dt.year <= 2021)]
mare2 = mare2[(mare['data'].dt.year >= 2019) & (mare2['data'].dt.year <= 2021)]
fig = plt.figure()
plt.plot(mare['data'], mare['nivelprs'], label='Previsto')
plt.plot(mare['data'], mare['nivelobs'], label='Observado')
plt.plot(mare2['data'], mare2['nivel'], label='Observado2')

plt.show()

