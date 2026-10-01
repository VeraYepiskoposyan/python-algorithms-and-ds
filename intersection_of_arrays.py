def intersection(list1, list2):
    new_list = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                new_list.append(list1[i])
    return new_list
print(intersection(list1 = [1,2,3,4,5], list2 = [3,4,5,6,7]))