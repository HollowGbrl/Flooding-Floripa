import pandas as pd
import pyproj

# Define the input and output coordinate systems
input_proj = pyproj.Proj(init='epsg:4326')  # WGS84
output_proj = pyproj.Proj(init='epsg:32722')  # UTM Zone 22S

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('sul_copia_ajustado_floripa_toda.csv', header=None, delimiter='\t')  # Assuming tab-delimited

# Iterate through the rows and convert coordinates
output_rows = []
for index, row in df.iterrows():
    lon, lat, z = row
    x, y, z = pyproj.transform(input_proj, output_proj, lon, lat, z)
    output_rows.append([x, y, z])

# Create a new DataFrame with the converted coordinates
output_df = pd.DataFrame(output_rows, columns=['UTM Easting (X)', 'UTM Northing (Y)', 'Elevation (Z)'])

# Save the new DataFrame to a CSV file
output_df.to_csv('floripa_bati_convertedido_real.csv', index=False)