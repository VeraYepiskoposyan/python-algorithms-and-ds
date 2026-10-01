def most_common(numbers):
    if not numbers:
        return None

    count = {}

    for num in numbers:
        count[num] = count.get(num, 0) + 1

    return max(count, key = count.get)

print(most_common([1, 2, 2, 3, 3, 3, 4]))