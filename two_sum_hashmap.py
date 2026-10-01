def two_sum(numbers, target):
    seen = {}
    for i, num in enumerate(numbers):
        needed = target - num
        if needed in seen:
            return (seen[needed], i)
        else:
            seen[num] = i
    return None
print(two_sum(numbers = [2, 11, 7, 15], target = 9))