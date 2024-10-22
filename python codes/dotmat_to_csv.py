import scipy.io
import matplotlib.pyplot as plt
import os
import datetime
import pandas as pd
import numpy as np

file = f'dados_casan/ADCP-20240115T132808Z-001/ADCP/02.BAIA_SUL/Campanha06/codes/adcp_BS06.mat'

# Load .mat file
mat_data = scipy.io.loadmat(file)
# Access the variables in the .mat file
variables = mat_data.keys()
#print(variables)
#nivel_zero = mat_data['nivel_zero']
t = mat_data['t']
t2= mat_data['t_consist']
#press= mat_data['press_temp_aux']
nivel = mat_data['nivel_zero']

# Convert Julian day to datetime
datetime_list = [datetime.datetime.fromordinal(int(jd[0])) + datetime.timedelta(days =(jd[0]%1)) - datetime.timedelta(days=366) for jd in t2]

tot = len(datetime_list) - len(nivel)

nivel = nivel[0:tot]
nivel2=[]
for n in nivel:
    nivel2.append(n[0])

print(len(datetime_list), len(nivel2))  
#convert to csv

save = f'adcpengeplus/marcoabril.csv'

with open(save, 'w') as saida:
    saida.write('data,nivel\n')
    for i in range(len(datetime_list)):
        saida.write(f'{datetime_list[i]},{nivel2[i]}\n')

# Plot the data
#plt.plot(nivel)
#plt.show()


