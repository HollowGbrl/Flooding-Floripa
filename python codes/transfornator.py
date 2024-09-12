import pandas as pd
import numpy as np

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('sul_copia_ajustado_floripa_geral.csv', header=None, delimiter='\t')  # Assuming tab-delimited

# Assuming the first column is latitude (φ) and the second column is longitude (θ)
latitude_values = np.radians(df[0])  # Convert degrees to radians
longitude_values = np.radians(df[1])  # Convert degrees to radians
r_values = df[2]  # Assuming the third column is the radial distance (r)

# Convert latitude, longitude, and radial distance to Cartesian coordinates
x_values = r_values * np.cos(latitude_values) * np.cos(longitude_values)
y_values = r_values * np.cos(latitude_values) * np.sin(longitude_values)
z_values = r_values * np.sin(latitude_values)

# Update the first two columns of the DataFrame with Cartesian coordinates
df[0] = x_values
df[1] = y_values
df[2] = z_values

# Save the updated DataFrame to a new CSV file
df.to_csv('floripa_bati_transformado_cartesian_coordinates.csv', header=False, index=False, sep='\t')