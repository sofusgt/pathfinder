from pyrosm import get_data, OSM
import pyrosm
import numpy as np
import pandas as pd
import geopandas as gpd
from queue import PriorityQueue
import matplotlib.pyplot as plt

file = open("cities.txt", "a")

for city in pyrosm.data.available["cities"]:
    file.write(city + "\n")

file.close()