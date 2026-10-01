def consecutive_pairs(numbers):
    if not numbers:
        return None
    i = 0
    pairs = []
    while i < len(numbers) - 1:
        pairs.append([numbers[i], numbers[i + 1]])
        i += 1
    return pairs
print(consecutive_pairs([1,2,3,4,5]))

