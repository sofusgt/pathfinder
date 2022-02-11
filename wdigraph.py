import geopandas


class Wdigraph:
    def __init__(self, raw_nodes : geopandas.GeoDataFrame, raw_edges : geopandas.GeoDataFrame):
        _raw_nodes = raw_nodes
        _raw_edges = raw_edges
        