def max_subarray_sum(numbers):
    if not numbers:
        return None

    current_sum = 0
    max_sum = numbers[0]

    for num in numbers:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        elif current_sum < 0:
             current_sum = 0
    return max_sum
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))