from __future__ import annotations
import numpy as np
import geopandas

class Vertex:
    def __init__(self, id : np.int64):
        self.id = id
        self.neighbours = []
    
    def add_neighbour(self, id : Vertex):
        self.neighbours.append(id)

class Edge:
    def __init__(self, u : Vertex, v : Vertex, length : float):
        self.u = u
        self.v = v
        self.length = length

class Graph:
    def __init__(self, vertices : geopandas.GeoDataFrame, edges : geopandas.GeoDataFrame):
        self.vertices = [Vertex(np.int64(v)) for v in vertices["id"]]
    
    def get_vertex(self, id : np.int64) -> Vertex:
        for v in self.vertices:
            if v.id == id:
                return v
    