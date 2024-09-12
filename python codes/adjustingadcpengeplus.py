import os


teste=0
with open('adcpengeplus/marcoabril.csv', 'r') as entrada, open('adcpengeplus/1603_2004.csv', 'w') as saida:
    for linha in entrada:
        t= linha.split(',')[0]
        nivel= linha.split(',')[1]
        hms= t.split(' ')[1]
        d= t.split(' ')[0]
        h,m,s = float(hms.split(':')[0]), float(hms.split(':')[1]), float(hms.split(':')[2])
       
        if teste<10:
            print(m)
        if s>59 and m<59:
            m+=1
        if int(m==59):
            m= '00'
            h+=1
        m= int(m)
        if m ==0:
            m= '00'
        s = '00'
        
       
        nlinha= f'{d} {int(h)}:{m}:{s},{nivel}'
        saida.write(nlinha)
        if teste<10:
            print(nlinha)

        teste+=1
    print('terminou')