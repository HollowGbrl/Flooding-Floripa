arquivo_entrada = '../finaltcc/batimetria/bati_flripa_32722_casanepagri_corrigido_imbituba_delfttbm_com_orio.xyz'
arquivo_saida= '../finaltcc/batimetria/bati_flripa_32722_corrigido_imbituba_delft_rio_campeche.xyz'
import time

print('Comecei')
#abrindo os arquivos de entrada e saida
with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saida:
    #para cada linha do arquivo, se o valor de batimetria for 0 (ou outro valor de interesse), ele vai excluir esse valor no novo arquivo
    for linha in entrada:
        #separando a linha 
        linha2=linha.split(' ')
        x, y, z =linha2[0], linha2[1], float(linha2[2])
        if z != -0.4:
            linhasaida= f'{x} {y} {round(z-0.4, 4)}\n'
            saida.write(linhasaida)
        #escrevendo as variaveis arredondadas no novo arquivo usando um f-string
    print('terminei primeira parte')
    with open('newbatimetry_epsg32722.xyz', 'r') as entrada2:
        for linha in entrada2:
            linha2=linha.split(' ')
            x, y, z =linha2[0], linha2[1], float(linha2[2])
            linhasaida= f'{x} {y} {round(z-0.4, 4)}'
            saida.write(linha)

print('terminei')
