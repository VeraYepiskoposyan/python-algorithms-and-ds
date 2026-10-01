def remove_duplicates_sorted(numbers):
    if not numbers:
        return []

    write = 0
    read = 1

    while read < len(numbers) - 1:
        if numbers[read] != numbers[write]:
            write += 1
            numbers[write] = numbers[read]
        read += 1

    return numbers[:write + 1]
print(remove_duplicates_sorted([1,1,2,2,3,4,4]))

