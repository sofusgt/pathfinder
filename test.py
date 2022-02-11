import matplotlib.pyplot as plt
from pyrosm import get_data, OSM
import geopandas
import sys
import os
import utils
import pandas

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No argument given.")
    else:
        region = sys.argv[1]

        nodes, edges = utils.get_graph(region)
        print(type(nodes))
        print(type(edges))