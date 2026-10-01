def first_unique_char(text):
    if text == '':
        return -1

    my_dict = {}

    for letter in text:
        if letter.isalpha():
            lower = letter.lower()
            my_dict[lower] = my_dict.get(lower, 0) + 1

    for i, letter in enumerate(text):
        if letter.isalpha() and my_dict[letter.lower()] == 1:
            return i

    return - 1

print(first_unique_char("leetcode"))