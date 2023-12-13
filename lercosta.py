import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV usando o pandas
nome_arquivo = "Sul_Novo.csv"  # Substitua pelo nome do seu arquivo CSV
dados = pd.read_csv(nome_arquivo)

# Exibir as primeiras linhas do arquivo CSV
print(dados.head())

# Plotar os dados de batimetria
plt.figure(figsize=(10, 6))
plt.plot(dados['Longitude'], dados['Latitude'], marker='o', linestyle='', markersize=3)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Visualização da Batimetria')
plt.grid()
plt.show()