def second_largest(numbers):
    largest = None
    second = None
    for num in numbers:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif second is None or  num > second:
            second = num
    return second
print(second_largest([7,3,9,5,8]))