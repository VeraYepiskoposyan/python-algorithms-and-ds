def majority_element(numbers):
    if not numbers:
        return None

    my_dict = {}
    majority_number = None

    for num in numbers:
        my_dict[num] = my_dict.get(num, 0) + 1

        if my_dict[num] > len(numbers) / 2:
            majority_number = num

    return majority_number

print(majority_element([2,2,1,1,2]))
