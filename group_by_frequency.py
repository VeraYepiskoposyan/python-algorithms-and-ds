def group_by_freq(numbers):
    if not numbers:
        return {}

    count = {}
    for num in numbers:
        count[num] = count.get(num,0) + 1
        sorted_keys = sorted(count.keys(), key=lambda x: count[x], reverse=True)

    result = {}
    for num in sorted_keys:
        result[num] = [num] * count[num]

    return result

print(group_by_freq([4,4,1,2,2,2,5]))