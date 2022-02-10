import matplotlib.pyplot as plt
from pyrosm import get_data, OSM
import geopandas
import sys
import os

def get_driving_network(region):
    path_to_file = "data/" + region + "_driving.shp"

    if os.path.exists(path_to_file):
        print("Loading data from " + path_to_file)
        drive_net = geopandas.read_file(path_to_file)
        return drive_net
    else:
        print("Getting data for " + region + "...")
        fp = get_data(region, directory="data")

        print("Initializing OSM object...")
        osm = OSM(fp)

        print("Getting driving network...")
        drive_net = osm.get_network(network_type="driving")

        print("Saving data for future use to" + path_to_file)
        drive_net.to_file(path_to_file)
        return drive_net


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No argument given.")
    else:
        region = sys.argv[1]

        drive_net = get_driving_network(region)
        print("Done")