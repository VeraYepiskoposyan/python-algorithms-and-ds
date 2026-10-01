def two_sum_sorted(numbers, target):
    if not numbers:
        return None

    left = 0
    right = len(numbers) - 1

    while(left < right):
        current_sum = numbers[left] + numbers[right]
        if current_sum > target:
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            return (left, right)

    return None

print(two_sum_sorted([1, 2, 4, 6, 8, 9, 14], 10))