import pytest
from sudoku_solver.grid_checker import allowed_values


@pytest.mark.parametrize("test_input,expected", [
    ([1, 2, 3, 5, 6], [4, 7, 8, 9]),
    ([], [1, 2, 3, 4, 5, 6, 7, 8, 9])
])
def test_solver(test_input, expected):
    assert allowed_values(test_input) == expected
