def longest_common_prefix(words):
    if not words:
        return ""
    words.sort()
    first_word = words[0]
    last_word = words[-1]

    i = 0
    while i < len(first_word) and i < len(last_word) and first_word[i] == last_word[i]:
        i += 1

    return first_word[:i]
print(longest_common_prefix(["flower","flow","flight"]))

