import pandas as pd
import geopandas as gpd

countries = gpd.read_file("env/lib/python3.9/site-packages/geopandas/datasets/naturalearth_lowres/naturalearth_lowres.shp")
countries.plot()