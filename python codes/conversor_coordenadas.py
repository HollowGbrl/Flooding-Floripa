import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV data (replace 'your_data.csv' with your actual file name)
data = pd.read_csv('Gabriel/finaltcc/altimetria/visualizarcsv.txt', sep=' ')

print(data['z'])


#Extract columns
lat = data['x']
long = data['y']
alt = -data['z']
print(alt)


#Create a scatter plot
ax = plt.figure(figsize=(10, 6))
ax.scatter(lat, long, c=alt, cmap='rainbow', marker='o', s=20)

ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

#ax.set_zlabel("Depth")

# Set the z-axis limits
#ax.set_zlim3d(-2, 5)  # Set the view range for the z-axis to [-4, 4]
#ax.set_ylim3d(-2, 2)  # Set the view range for the y-axis to [-2, 2]
#ax.set_xlim3d(-2, 2)  # Set the view range for the x-axis to [-2, 2]


# Add title
plt.title("Depth Visualization")
plt.colorbar(label="Depth")

plt.show()

