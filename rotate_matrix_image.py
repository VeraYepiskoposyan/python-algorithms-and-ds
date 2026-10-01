def rotate_matrix(matrix):
    if not matrix:
        return []

    transposed_matrix = []
    rotated_matrix = []

    num_row = len(matrix)
    num_col = len(matrix[0])

    for j in range(num_col):
        new_row = []
        for i in range(num_row):
            new_row.append(matrix[i][j])

        transposed_matrix.append(new_row)

    for row in transposed_matrix:
        rotated_matrix.append(list(reversed(row)))

    return rotated_matrix
print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
