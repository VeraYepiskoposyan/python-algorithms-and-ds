def move_zeros(numbers):
    if not numbers:
        return []

    new_list = []

    for num in numbers:
        if num != 0:
            new_list.append(num)

    zero_length = len(numbers) - len(new_list)
    new_list.extend([0] * zero_length)
    return new_list
print(move_zeros([0,1,0,3,12]))


