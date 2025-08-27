import geopandas as gpd
import math 
import os 

gdf = gpd.read_file("rawData\Lower_layer_Super_Output_Areas_(December_2021)_Boundaries_EW_BFE_(V10)_and_RUC.shp")


n_splits = 5
chunk_size = math.ceil(len(gdf) / n_splits)

os.makedirs("data_split/llosa", exist_ok=True)

for i in range(n_splits):
    start = i * chunk_size
    end = (i + 1) * chunk_size
    chunk = gdf.iloc[start:end]

    out = f"data_split/llosa/llosa_part_{i + 1}.shp"
    chunk.to_file(out)
    