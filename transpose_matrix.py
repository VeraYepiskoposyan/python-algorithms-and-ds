def transpose(matrix):
    new_matrix = []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for j in range(num_cols):
        new_row = []
        for i in range(num_rows):
            new_row.append(matrix[i][j])
        new_matrix.append(new_row)
    return new_matrix
print(transpose([
 [1,2,3],
 [4,5,6]
]))










