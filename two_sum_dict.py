def two_sum(numbers, target):
    if not  numbers:
        return None

    num_dict = {}


    for i, num in enumerate(numbers):
        need = target - num
        if need in num_dict:
            return [num_dict[need], i]

        else:
            num_dict[num] = i

    return None

print(two_sum([2, 7, 11, 15], 9))




