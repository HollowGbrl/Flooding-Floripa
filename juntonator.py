# Abra os arquivos de entrada e saída
with open('Batimetria_baia_florianopolis2_32722.xyz', 'r') as arquivo1, open('testes_de_troca_virgula.xyz', 'r') as arquivo2, open('floripa_bati_32722_dasfranken', 'w') as arquivo_saida:
    # Lê o conteúdo do primeiro arquivo e escreve no arquivo de saída
    for linha in arquivo1:
        arquivo_saida.write(linha)
    
    # Lê o conteúdo do segundo arquivo e escreve no arquivo de saída
    for linha in arquivo2:
        arquivo_saida.write(linha)

# Feche os arquivos
arquivo1.close()
arquivo2.close()
print('oi')
arquivo_saida.close()