arquivo_entrada = 'mascaras/teste_mascarasemrio.csv'
arquivo_saida = 'altimetria_rtavares_semrio.xyz'


with open(arquivo_entrada, 'r', newline='') as entrada, open(arquivo_saida, 'w', newline='') as saida:
    conteudo = entrada.read()

modificado = conteudo.replace(',', ' ')

with open(arquivo_saida, 'w', newline='') as saida:
    saida.write(modificado)
