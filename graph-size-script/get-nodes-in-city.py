from pyrosm import get_data, OSM
import pyrosm
import numpy as np
import pandas as pd
import geopandas as gpd
from queue import PriorityQueue
import matplotlib.pyplot as plt
import sys

if len(sys.argv) < 2:
    print("No argument given.")
else:
    file = open("nodes-in-city.txt", "a")
    region = sys.argv[1]
    osm = OSM(get_data(region))
    vertices, edges = osm.get_network("driving", nodes=True)
    nodes = len(vertices)
    file.write(str(nodes) + ", " + region + "\n")
    file.close()
