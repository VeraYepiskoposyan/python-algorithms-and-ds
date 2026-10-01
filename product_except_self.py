def product_array(array):
    if not array:
        return []

    n = len(array)
    res = [1] * n

    left = 1
    for i in range(n):
        res[i] = left
        left = left * array[i]

    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right = right * array[i]

    return res
print(product_array([1,2,3,4]))



