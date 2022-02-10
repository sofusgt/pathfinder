import matplotlib.pyplot as plt
from pyrosm import get_data, OSM
import geopandas
import sys
import os
import utils

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No argument given.")
    else:
        region = sys.argv[1]

        drive_net = utils.get_road_network(region)
        print("Done")