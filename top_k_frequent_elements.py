def top_k_frequent(numbers, k):
    if not numbers and not k:
        return []

    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    sorted_freq = sorted(counts.keys(), key = lambda num: counts[num], reverse = True)

    return sorted_freq[:k]

print(top_k_frequent([1,1,1,2,2,3], 2))