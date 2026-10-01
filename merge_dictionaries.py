def merge_dictionaries(dict1, dict2):
    merged = {}
    for key in dict1:
        merged[key] = dict1[key]
    for key in dict2:
        merged[key] = merged.get(key, 0) + dict2[key]
    return merged

dict1 = {"apple": 2, "banana": 3}
dict2 = {"banana": 4, "orange": 5}

print(merge_dictionaries(dict1, dict2))
