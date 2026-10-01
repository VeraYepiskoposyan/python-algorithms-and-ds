def most_frequent(numbers):
    if not numbers:
        return None

    max_count = 0
    most_freq_num = None

    for i in range(len(numbers)):
        count = 1
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                count += 1

        if count > max_count:
            max_count = count
            most_freq_num = numbers[i]

    return most_freq_num

print(most_frequent([1,2,3,2,5,2,1]))
