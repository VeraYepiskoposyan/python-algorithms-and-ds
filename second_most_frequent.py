def second_most_frequent(numbers):
    if not numbers:
        return None
    dict = {}

    for num in numbers:
        dict[num] = dict.get(num, 0) + 1

    largest_key, largest_val = None, -1
    second_key, second_val = None, -1

    for key, value in dict.items():
        if value > largest_val:
            second_key, second_val = largest_key, largest_val
            largest_key, largest_val = key, value

        elif value > second_val and value < largest_val :
            second_key, second_val = key, value

    return second_key
print(second_most_frequent([1, 1, 2, 2, 2, 3, 3, 4]))

# def second_most_frequent(numbers):
#     if not numbers:
#         return None
#     dict = {}
#
#     for num in numbers:
#         dict[num] = dict.get(num, 0) + 1
#
#     unique_frequencies = sorted(set(dict.values()), reverse=True)
#
#     if len(unique_frequencies) < 2:
#         return None
#
#     target_freq = unique_frequencies[1]
#
#     for num, freq in dict.items():
#         if freq == target_freq:
#             return num
# print(second_most_frequent([1, 1, 2, 2, 2, 3, 3, 4]))
