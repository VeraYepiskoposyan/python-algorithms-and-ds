def rotate_right(numbers, k):
    if not numbers:
        return None
    new_list = [0] * len(numbers)
    n = len(numbers)
    for i in range(n):
        new_index = (i + k) % n
        new_list[new_index] = numbers[i]
    return new_list
print(rotate_right([1,2,3,4,5], 2))

