def group_by_length(words):
    if not words:
        return {}
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = [word]
        else:
            result[length].append(word)
    return result
print(group_by_length(["cat", "dog", "apple", "hi", "banana"]))














