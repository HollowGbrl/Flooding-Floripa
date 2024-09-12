arquivo_entrada = 'floripa_batrimetra_epagritroca5.xyz'
arquivo_saida = 'batipratroca_32722.csv'

import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(arquivo_entrada, header=None, delimiter=' ')  # Assuming tab-delimited
# Iterate through the rows and convert coordinates
output_rows = []
for index, row in df.iterrows():
    x, y, z = row
    if z > -15:
        output_rows.append([x, y, z])

# Create a new DataFrame with the converted coordinates
output_df = pd.DataFrame(output_rows, columns=['UTM Easting (X)', 'UTM Northing (Y)', 'Elevation (Z)'])

# Save the new DataFrame to a CSV file
output_df.to_csv(arquivo_saida, index=False)   