def longest_increasing_streak(numbers):
    if not numbers:
        return None

    max_streak = 1
    current_streak = 1

    for i in range(1,len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 1

    return max_streak

print(longest_increasing_streak([1, 2, 3, 2, 3, 4, 5, 1]))