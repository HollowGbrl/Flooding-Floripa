from geopandas import GeoDataFrame
from shapely.geometry import Point
import geopandas as gpd

# Read the shapefile
gdf = gpd.read_file('c:/Users/labdi/Desktop/linhadecostasc.shp')

print(gdf['geometry'])

gdf['longitude'] = gdf.geometry.x
gdf['latitude'] = gdf.geometry.y

print(gdf)

# Create a GeoSeries with your coordinates
#s = GeoSeries([Point(x, y) for x, y in zip(df['longitude'], df['latitude'])])

# Set the coordinate reference system (CRS)
#s.crs = {'init': 'epsg:4326', 'no_defs': True}

# Reproject to UTM Zone 22S (EPSG:32722)
#s_reprojected = s.to_crs(epsg=32722)