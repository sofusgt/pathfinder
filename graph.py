from __future__ import annotations
import numpy as np
import geopandas

class Vertex:
    def __init__(self, id : np.int64, x : float, y : float):
        self.id = id
        self.pos = (x, y)

class Graph:
    def __init__(self, vertices : geopandas.GeoDataFrame, edges : geopandas.GeoDataFrame):
        self.vertices = [Vertex(np.int64(v)) for v in vertices["id"]]
        self.vertices = {}
        for row in vertices:
            key = np.int64(row["id"])
            lon = np.float32(row["lon"])
            lat = np.float32(row["lat"])
            self.vertices[key] = Vertex(key, lon, lat)
    