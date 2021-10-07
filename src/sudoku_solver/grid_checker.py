def allowed_values(grid):
    allowed_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return [x for x in allowed_values if x not in grid]
