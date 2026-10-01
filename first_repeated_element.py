def first_repeated(numbers):
    if not numbers:
        return None

    seen = set()

    for num in numbers:
        if num in seen:
            return num

        seen.add(num)

    return None

print(first_repeated([5, 1, 3, 4, 3, 5]))