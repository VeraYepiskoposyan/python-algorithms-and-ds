def missing_number(numbers):
    if not numbers:
        return None

    n = len(numbers)

    expected_sum = (n *(n + 1)) // 2
    actual_sum = sum(numbers)

    missing_value = expected_sum - actual_sum

    return missing_value

print(missing_number([9,6,4,2,3,5,7,0,1]))