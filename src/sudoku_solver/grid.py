from typing import List
from dataclasses import dataclass, field


@dataclass
class Cell:
    row: int
    column: int
    value: int = 0
    allowed_values: List[int] = field(init=False)
    box: int = field(init=False)

    def __post_init__(self):
        self.box = self.get_box(self.row, self.column)
        self.allowed_values = [x for x in range(1, 10)]

    def get_box(self, row: int, column: int):
        return 3 * (row // 3) + (column // 3) + 1

    def remove_allowed_value(self, value):
        if value in self.allowed_values:
            self.allowed_values.remove(value)


class Grid:
    def __init__(self, matrix: List[List[int]]) -> None:
        self.cells: List[Cell] = []
        for j, row in enumerate(matrix):
            for i, value in enumerate(row):
                self.cells.append(Cell(j, i, value))
        self.size: int = len(matrix)
        self.initiliaze_allowed_values()

    def __repr__(self) -> str:
        cells_print = self.cells.copy()
        cells_print.sort(key=lambda x: (x.row, x.column))
        cells_value = [str(x.value) for x in cells_print]
        gridbyrow = [" ".join(cells_value[i:i+self.size]) for i in range(0, self.size * self.size, self.size)]
        return "\n".join(gridbyrow)

    def initiliaze_allowed_values(self):
        for row in range(9):
            for column in range(9):
                cell = next((x for x in self.cells if x.row == row and x.column == column), None)
                if cell and cell.value:
                    self.update_allowed_values(row, column, cell.box, cell.value)

    def update_allowed_values(self, row: int, column: int, box: int, value: int):
        """Removes the cell value from all other cells allowed values that are in the same row, column or box.
        """
        cells_to_update = [x for x in self.cells if x.row == row or x.column == column or x.box == box]
        for cell in cells_to_update:
            if cell.row == row and cell.column == column:
                cell.allowed_values = []
            else:
                cell.remove_allowed_value(value)
