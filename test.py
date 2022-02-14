import matplotlib.pyplot as plt
from pyrosm import get_data, OSM
import geopandas
import sys
import os
import utils
import pandas
import numpy as np
import graph

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No argument given.")
        exit(1)
    else:
        region = sys.argv[1]

        vertices, edges = utils.load_graph(region)
        #utils.plot_graph(vertices, edges)

        print(vertices)
        print(edges)

        G = graph.Graph(vertices, edges)
        print(G.vertices[0])
        