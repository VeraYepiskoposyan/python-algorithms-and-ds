def num_mun(numbers):
    if not numbers:
        return None, None, None

    max = numbers[0]
    min = numbers[0]

    count = 0
    sum = 0

    for num in numbers:
        if num > max:
            max = num
        if num < min:
            min = num

        sum += num
        count += 1

    avg = sum / count

    return max, min, avg

print(num_mun([3, 8, 1, 9, 4, 6]))

