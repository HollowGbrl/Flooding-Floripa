import csv
import pandas

# Nome do arquivo CSV de entrada e saída
arquivo_entrada = 'Sul_copia.csv'
arquivo_saida = 'testes_de_troca.csv'
valores_especificos =[5]
linha_auxiliar= []
latitudes = [-27, 28.5]
longitudes = [-49, -47]
#Abra o arquivo CSV de entrada em modo de leitura e o arquivo de saída em modo de escrita
with open(arquivo_entrada, 'r', newline='') as entrada, open(arquivo_saida, 'w', newline='') as saida:
    leitor_csv = csv.reader(entrada)
    escritor_csv = csv.writer(saida)


    # Leia e imprima o conteúdo atual do arquivo CSV
    for linha in leitor_csv:
        linha2= linha[0].split('\t') 
        #if float(linha2[2]) < 41 and float(linha2[2])> 0:
        #if round(float(linha2[2])) in valores_especificos:
            #if float(linha2[1])> -29 and float(linha2[1])< -27 :
                #if float(linha2[0])< -47 and float(linha2[0])> -49:  # Verifique a coluna Z (índice 2)
                    #escritor_csv.writerow(linha)
        if float(linha2[1])> -30 and float(linha2[1])< -26 :
            if float(linha2[0])< -46 and float(linha2[0])> -50:  # Verifique a coluna Z (índice 2)
                linha_auxiliar = linha2[0]
                linha2[0] = linha2[1]
                linha2[1] = linha_auxiliar
                escritor_csv.writerow(linha2)

        #lista_y.append(linha2[0])
        #linha2.remove(linha2[0])
        #print(f'linha depois do y {linha2}')
        #lista_z.append(linha2[0])
        #linha2.remove(linha2[0])
        #print(f'linha depois do z {linha2}')
  #if #round(float(linha2[2])) in valores_especificos:
  # Copie as linhas que não correspondem ao valor especificado na coluna Z para o arquivo de saída
    #for linha in leitor_csv:
        #print(linha[2])
        #if linha[2] in valores_especificos:  # Verifique a coluna Z (índice 2)
            #escritor_csv.writerow(linha)

# O arquivo de saída (saida.csv) agora contém os dados com as linhas onde Z não é igual ao valor especifico.