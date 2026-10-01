def frequency_count(numbers):
    if not numbers:
        return None

    count = {}

    for num in numbers:
        count[num] = count.get(num, 0) + 1

    return count

print(frequency_count([1, 2, 2, 3, 3, 3, 4]))
