def longest_increasing_streak(numbers):
    if not numbers:
        return []

    current_len = 1
    current_start = 0

    max_len = 1
    best_start = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i -1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
                best_start = current_start

            current_start = i
            current_len = 1

    if current_len > max_len:
        max_len = current_len
        best_start = current_start

    return numbers[best_start : best_start + max_len]

print(longest_increasing_streak([1, 2, 3, 2, 4, 5, 6, 1]))
