def appear_once(numbers):
    seen = set()
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    result = []
    for num in numbers:
        if num in seen and num not in duplicates:
            if num not in result:
                result.append(num)
    return result
print(appear_once([5,3,5,2,1,2]))
