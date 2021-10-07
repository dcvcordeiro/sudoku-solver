import pytest
from sudoku_solver.grid import Grid


def test_grid_print(capture_stdout, matrix):
    grid = Grid(matrix)
    print(grid)
    assert capture_stdout["stdout"] == "1 0\n0 2\n"


@pytest.mark.parametrize("test_input,expected", [
    (0, 1),
    (1, 0),
    (2, 0),
    (3, 2),
])
def test_cell_value(test_input, expected, matrix):
    grid = Grid(matrix)
    assert grid.cells[test_input].value == expected


@pytest.mark.parametrize("test_input,expected", [
    (0, []),
    (1, [1, 9]),
])
def test_cell_allowed_values(test_input, expected, full_matrix):
    grid = Grid(full_matrix)
    assert grid.cells[test_input].allowed_values == expected


@pytest.mark.parametrize("test_input,expected", [
    (0, 1),
    (1, 1),
    (4, 2),
    (10, 1),
    (44, 6),
    (45, 4),
    (80, 9),
])
def test_cell_box(test_input, expected, full_matrix):
    grid = Grid(full_matrix)
    assert grid.cells[test_input].box == expected
