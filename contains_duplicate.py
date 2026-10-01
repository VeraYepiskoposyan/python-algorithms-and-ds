def remove_duplicates(numbers):
    new_list = []
    for num in numbers:
        if num not in new_list:
            new_list.append(num)
            
    return new_list
print(remove_duplicates([1,2,2,3,4,4,5]))