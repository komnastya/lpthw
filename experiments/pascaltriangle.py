from typing import List

PascalTriangle = List[List[int]]


# Computes Pascal's trianle of the given height returns a list of lists.
# height = 4
# result = [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
# ]


def pascal_triangle(height: int) -> PascalTriangle:
    triangle: PascalTriangle = []
    previous_row = [1]
    while len(triangle) < height:
        if len(triangle) == 0:
            triangle.append(previous_row)
        else:
            current_row = []
            current_row.append(1)
            for i in range(len(previous_row) - 1):
                current_row.append(previous_row[i] + previous_row[i + 1])
            current_row.append(1)
            triangle.append(current_row)
            previous_row = current_row
    return triangle


# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# Example: (1) -> [1]
# Example: (2) -> [1,1]
# Example: (3) -> [1,2,1]
# Example: (4) -> [1,3,3,1]


def pascal_triangle_by_index(height: int) -> List[int]:
    previous_row = [1]
    while len(previous_row) <= height:
        if height == 0:
            return previous_row
        else:
            current_row = []
            current_row.append(1)
            for i in range(len(previous_row) - 1):
                current_row.append(previous_row[i] + previous_row[i + 1])
            current_row.append(1)
            previous_row = current_row
    return previous_row
