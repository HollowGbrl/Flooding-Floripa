import pandas as pd
from pyproj import Transformer

# Define the input and output coordinate systems
input_crs = "EPSG:4326"  # WGS84
output_crs = "EPSG:32722"  # UTM Zone 22S

# Create a transformer for the coordinate conversion
transformer = Transformer.from_crs(input_crs, output_crs)

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('teste1.xyz', header=None, delimiter=' ')  # Assuming tab-delimited
# Iterate through the rows and convert coordinates
output_rows = []
for index, row in df.iterrows():
    lat, lon, z = row
    x, y, z = transformer.transform(lon, lat, z)
    output_rows.append([x, y, z])
    print(x, lon, '------', y, lat )
    

# Create a new DataFrame with the converted coordinates
output_df = pd.DataFrame(output_rows, columns=['UTM Easting (X)', 'UTM Northing (Y)', 'Elevation (Z)'])

# Save the new DataFrame to a CSV file
output_df.to_csv('teste_batiametria5.csv', index=False)