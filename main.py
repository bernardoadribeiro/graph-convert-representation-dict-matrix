import numpy as np
from numpy._typing import NDArray
from numpy import float64


class Graph():
    # def __init__(self, graph_dict: dict = None, adj_matrix=None) -> None:
    #     if graph_dict:
    #         self.graph_as_dict = graph_dict
    #         self.vertices = list(graph_dict.keys())

    #     self.n_vertices = len(self.vertices)
    #     self.graph_as_matrix_adj = np.zeros((self.n_vertices, self.n_vertices))

    def dict_to_matrix(self, _graph: dict) -> NDArray[float64]:
        """
            _graph: dict that represet the graph that will be converted into adjacency matrix
        """
        vertices = list(_graph.keys())
        n_vertices = len(vertices)

        graph_as_matrix_adj = np.zeros((n_vertices, n_vertices))

        for _key in range(n_vertices):
            for _value in range(n_vertices):
                if (vertices[_key] in _graph and
                        vertices[_value] in _graph[vertices[_key]]):
                    graph_as_matrix_adj[_key][_value] = 1

        return graph_as_matrix_adj

    def matrix_to_dict(self, matrix_adj):
        pass


if __name__ == '__main__':
    print("Hello World!")
