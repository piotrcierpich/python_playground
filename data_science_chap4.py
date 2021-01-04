from typing import List, Callable
Matrix = List[List[float]]


def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:

    return [[entry_fn(x, y) for y in range(num_cols)]
            for x in range(num_rows)]


result = make_matrix(2, 3, lambda a, b: a + b)
expected = [[0, 1, 2],
            [1, 2, 3]]
assert result == expected, f"{result} is not {expected}"


def identity_matrix(num_rows: int, num_cols: int) -> Matrix:
    return make_matrix(num_rows, num_cols, lambda i, j: 1 if i == j else 0)


identity_matrix_3x3 = identity_matrix(3, 3)
expected_identity_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
assert identity_matrix_3x3 == expected_identity_matrix
