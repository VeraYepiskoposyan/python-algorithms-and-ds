def first_unique(numbers):
    if not numbers:
        return None
    seen = set()
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)


    for num in numbers:
        if num not in duplicates:
            return num

    return None
print(first_unique([4,1,4,2,1,2]))

