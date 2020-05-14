
import matplotlib.pyplot as plt
import geopandas
from shapely.geometry import Polygon

#Importation des données
capitals = geopandas.read_file(geopandas.datasets.get_path("naturalearth_cities"))
world = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))

# Variable Amérique du sud
south_america = world[world["continent"] == "South America"]

# Forme de l'Amérique du sud sous forme de polygon
polygon = Polygon([(0, 0), (0, 90), (180, 90), (180, 0), (0, 0)])
poly_gdf = geopandas.GeoDataFrame([1], geometry=[polygon], crs=world.crs)

capitals_clipped = geopandas.clip(capitals, south_america)

#Prendre la position d'index (ligne et colonne)
fig, ax = plt.subplots(figsize=(12, 8))
capitals_clipped.plot(ax=ax, color="purple")
south_america.boundary.plot(ax=ax, color="green")
ax.set_title("Capitals Clipped", fontsize=20)
ax.set_axis_off()
plt.show()
