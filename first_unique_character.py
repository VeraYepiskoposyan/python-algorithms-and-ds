# def first_non_repeating(text):
#     if not text:
#         return None
#     seen = ""
#     duplicate = ""
#     clean_text = ""
#     for char in text:
#         if char.isalpha():
#             clean_text += char
#     for letter in clean_text:
#         if letter in seen:
#             duplicate += letter
#         else:
#             seen += letter
#     for letter in clean_text:
#         if letter not in duplicate:
#             return letter
#     return None

# print(first_non_repeating("aabbccddef"))

def first_non_repeating(text):
    if not text:
        return None
    counts = {}
    for char in text:
        if char.isalpha():
            lowered = char.lower()
            counts[lowered] = counts.get(lowered, 0) + 1
    for char in text:
        if char.isalpha() and counts[char.lower()] == 1:
            return char
    return None
print(first_non_repeating("aabbccddef"))


