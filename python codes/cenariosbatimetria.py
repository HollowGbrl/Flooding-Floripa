
print('comecei')

#arquivo da batimetria
arquivo= "../finaltcc/bati_altimetria/bataltsc_32722_corrigidoimbituba.xyz"

#elevação do cenario do ipcc para imbituba
cenarios= {26:0.39, 45:0.59, 85:0.81, 85_2:1.46}

for cenario in cenarios:
#abrindo o arquivo de entrada e saida
    with open(f'{arquivo}_{cenario}.xyz', 'w') as saida , open(arquivo, 'r') as entrada:
        elev= cenarios.get(cenario)
        for linha in entrada:         
            #somando a elevação em cada ponto de batimetria
            linha2=linha.split(' ')
            novabat = float(linha2[2]) - elev
            linhanova= f'{linha2[0]} {linha2[1]} {novabat}\n'
            saida.write(linhanova) 

print('terminei')