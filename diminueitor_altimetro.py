arquivo_entrada = 'altimetria4_filt_round.xyz'
arquivo_saida= 'altimetria4_filt_round_diminuido.xyz'
import time
import random



print('Comecei')
#abrindo os arquivos de entrada e saida
with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saida:
    #para cada linha do arquivo, ele vai excluir 9 e adicionar a não excluida no final
    for linha in entrada:
        numero = random.randint(1, 10)
        if numero <1:
            saida.write(linha)
print('Terminei')
    