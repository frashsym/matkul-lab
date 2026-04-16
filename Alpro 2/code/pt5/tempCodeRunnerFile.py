# No. 1
matrix_3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# No. 2
matrix_4x4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# No. 3
matrix_2x2 = [
    [1, 2],
    [3, 4]
]

# No. 4
matrix_3x2 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# No. 5
matrix_2x3 = [
    [1, 2, 3],
    [4, 5, 6]
]

# No. 6
matrix_1x3 = [
    [1, 2, 3]
]

# No. 7
element_row2_col2 = matrix_3x3[1][1]

# No. 8
matrix_3x3_modified = [row.copy() for row in matrix_3x3]
matrix_3x3_modified[1][1] = 10

# No. 9
matrix_3x3_appended = [row.copy() for row in matrix_3x3]
matrix_3x3_appended.append([10, 11, 12])

# No. 10
matrix_3x3_deleted_row2 = [row.copy() for row in matrix_3x3]
del matrix_3x3_deleted_row2[1]


def print_matrix(name, matrix):
    print(f"{name}:")
    for row in matrix:
        print(row)
    print()


if __name__ == "__main__":
    print_matrix("No. 1", matrix_3x3)
    print_matrix("No. 2", matrix_4x4)
    print_matrix("No. 3", matrix_2x2)
    print_matrix("No. 4", matrix_3x2)
    print_matrix("No. 5", matrix_2x3)
    print_matrix("No. 6", matrix_1x3)

    print(f" No. 7: {element_row2_col2}\n")
    print_matrix("No. 8", matrix_3x3_modified)
    print_matrix("No. 9", matrix_3x3_appended)
    print_matrix("No. 10", matrix_3x3_deleted_row2)
