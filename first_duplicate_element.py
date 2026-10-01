def first_duplicate(numbers):
    if not numbers:
        return None
    seen = set()
    for num in numbers:
        if num in seen:
            return num
        else:
            seen.add(num)
    return None
print(first_duplicate([2, 1, 3, 5, 3, 2]))
