def flatten(matrix):
    new_list = []
    for row in matrix:
        for num in row:
            new_list.append(num)
    return new_list
print(flatten([
    [1,2],
    [3,4],
    [5]
]))