def move_zeros(numbers):
    if not numbers:
        return None

    write = 0

    for read in range(len(numbers)):
        if numbers[read] != 0:
            numbers[write] = numbers[read]
            write += 1

    while write < len(numbers):
        numbers[write] = 0
        write += 1

    return numbers

print(move_zeros([0, 1, 0, 3, 12]))