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
            Converts the graph representation from Dictionary (key:value) to Adjacency Matrix

            `_graph`: dict that represet the graph that will be converted into adjacency matrix
        """
        vertices = list(_graph.keys())
        n_vertices = len(vertices)

        graph_as_adj_matrix = np.zeros((n_vertices, n_vertices))

        for _key in range(n_vertices):
            for _value in range(n_vertices):
                if (vertices[_key] in _graph and
                        vertices[_value] in _graph[vertices[_key]]):
                    graph_as_adj_matrix[_key][_value] = 1

        return graph_as_adj_matrix

    def matrix_to_dict(self, adj_matrix: list[list], vertices: list = []) -> dict:
        """
            Converts the graph representation from Adjacency Matrix to Dictionary (key:value)

            `_adj_matrix`: Adjacency Matrix that represet the graph that will be converted into Dict
            representation {key:value}
            `_vertices`: vertices list of the graph
        """
        if vertices == []:
            for i in range(len(adj_matrix)):
                vertices.append(i)

            print('Vertices gerado: ', vertices)

        graph_as_dict = {}
        n_vertices = len(vertices)

        for _key in range(n_vertices):
            # `_key` is the index (or vertex)
            graph_as_dict[vertices[_key]] = []  # Create the vertex

            for _value in range(n_vertices):
                # `_value` is a neighbor (or relationship) of the vertex
                if adj_matrix[_key][_value] == 1:
                    # We append the neighbor in position [_key][_value]
                    # to the vertex, if in the coordinate has the value `1`.
                    graph_as_dict[vertices[_key]].append(vertices[_value])

        return graph_as_dict


if __name__ == '__main__':
    from tests import load_and_run_tests

    load_and_run_tests()

    # If you want to implement see the example:
