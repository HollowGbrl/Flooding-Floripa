import rasterio
import matplotlib.pyplot as plt

file_path = '../Garbosa_files/mosaico_mdt_Florianopolis.img'
#print(file_path)
try:
    with rasterio.open(file_path) as src:
        # Access metadata
        print(src.profile)

        # Read raster data
        img_array = src.read()
        plt.figure(figsize=(8, 8))
        plt.imshow(img_array.transpose((1, 2, 0)))  # Transpose the dimensions for RGB images
        plt.axis('off')  # Turn off axis labels
        plt.title('ERDAS IMAGINE Raster Image')
        plt.show()
        # Do something with the image data
        # For example, printing shape of the array
        print(img_array.shape)
except Exception as e:
    print(f"Error: {e}")