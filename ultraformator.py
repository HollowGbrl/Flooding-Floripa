arquivo_entrada = 'batipratroca_32722.csv'
arquivo_saida = 'Batimetria_baia_florianopolis2_32722.xyz'


with open(arquivo_entrada, 'r', newline='') as entrada, open(arquivo_saida, 'w', newline='') as saida:
    conteudo = entrada.read()

modificado = conteudo.replace(',', ' ')

with open(arquivo_saida, 'w', newline='') as saida:
    saida.write(modificado)
