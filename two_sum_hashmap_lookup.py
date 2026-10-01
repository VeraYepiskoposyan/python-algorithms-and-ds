def two_sum(numbers, target):
    if not numbers:
        return None

    dict = {}

    for i, num in enumerate(numbers):
        needed = target - num

        if needed in dict:
            return [dict[needed], i]

        dict[num] = i

    return  None
print(two_sum([2, 7, 11, 15], 9))