#importando os arquivos xyz e criando um arquivo novo de saida, com o proposito de diminuir o arquivo gigantesco de 62gibas
arquivo_entrada = 'altimetria2_filtrado_0e70mais_roundado.xyz'
arquivo_saida= 'p'
import time

print('Comecei')
#abrindo os arquivos de entrada e saida
with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saida:
    #para cada linha do arquivo, se o valor de batimetria for 0 (ou outro valor de interesse), ele vai excluir esse valor no novo arquivo
    for linha in entrada:
        print(linha)
        time.sleep(1)