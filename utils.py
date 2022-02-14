import matplotlib.pyplot as plt
from pyrosm import get_data, OSM
import geopandas
import sys
import os


def get_road_network(region : str):
    data_dir = os.path.abspath("data/")
    path_to_file = os.path.join(data_dir, region + "_roads.shp")

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

def get_graph_data(region : str):
    fp = get_data(region, directory="data")
    osm = OSM(fp)
    return osm.get_network(network_type="driving", nodes=True)

def load_graph(region : str):
    vertices_file = os.path.join("data", region + "_vertices.shp")
    edges_file = os.path.join("data", region + "_edges.shp")

    if os.path.exists(vertices_file) and os.path.exists(edges_file):
        print("Loading vertices...")
        vertices = geopandas.read_file(vertices_file)
        print("Loading edges...")
        edges = geopandas.read_file(edges_file)
        return vertices, edges
    else:
        vertices, edges = get_graph_data(region)
        print("Saving vertices...")
        vertices.to_file(vertices_file)
        print("Saving edges...")
        edges.to_file(edges_file)
        return vertices, edges

def plot_graph(vertices : geopandas.GeoDataFrame, 
               edges : geopandas.GeoDataFrame):
    print("Plotting graph...")
    ax = edges.plot(figsize=(6,6), color="gray")
    ax = vertices.plot(ax=ax, color="red", markersize=2.5)
    plt.show()