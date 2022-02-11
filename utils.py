import matplotlib.pyplot as plt
from pyrosm import get_data, OSM
import geopandas
import sys
import os


def get_road_network(region):
    data_dir = os.path.abspath("data/")
    path_to_file = data_dir + "/" + region + "_roads.shp"

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

def get_graph(region):
    fp = get_data(region, directory="data")
    osm = OSM(fp)
    nodes, edges = osm.get_network(network_type="driving", nodes=True)
    return nodes, edges