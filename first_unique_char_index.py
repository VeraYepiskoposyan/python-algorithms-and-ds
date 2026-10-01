def first_unique_char(text):
    if not text:
        return -1

    count = {}

    for letter in text:
        if letter.isalpha():
            lower = letter.lower()
            count[lower] = count.get(lower, 0)  + 1

    for i, letter in enumerate(text):
        if letter.isalpha() and count[letter.lower()] == 1:
            return i

    return -1
print(first_unique_char("leetcode"))
print(first_unique_char("aabb"))



