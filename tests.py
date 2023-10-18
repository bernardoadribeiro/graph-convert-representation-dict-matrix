from unittest import TestCase, main
import numpy as np

from main import Graph


class TestConvertion(TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        self._graph = Graph()
        super().__init__(methodName)

    def test_convertion_dict_to_matrix(self):
        print("\nTesting convertion of Dict to Matrix")

        adj_matrix_dict = {
            'A': ['C', 'B'],
            'B': ['A'],
            'C': []
        }

        expected_result = [
            [0, 1, 1],
            [1, 0, 0],
            [0, 0, 0],
        ]
        result = self._graph.dict_to_matrix(_graph=adj_matrix_dict)

        print(f"Expected:\n {expected_result}\n\nResult:\n {result}")
        self.assertTrue(
            np.array_equal(result, expected_result),
            "The result isn't equal to the expected result."
        )

    def test_convertion_matrix_to_dict(self):
        print("\nTesting convertion of Matrix to Dict")

        _adj_matrix = [
            [0, 1, 1],
            [1, 0, 0],
            [0, 0, 0],
        ]

        expected_result = {
            'A': ['C', 'B'],
            'B': ['A'],
            'C': []
        }
        result = self._graph.matrix_to_dict(adj_matrix=_adj_matrix)

        print(f"Expected:\n {expected_result}\n\nResult:\n {result}")
        self.assertEqual(
            result, expected_result,
            "The result isn't equal to the expected result."
        )


if __name__ == '__main__':
    print("Starting Unit Tests")
    main()
