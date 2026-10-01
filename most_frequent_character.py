def return_most(text):
    if not text:
        return None, None
    text = text.lower()
    clean_text = ""
    for char in text:
        if char.isalpha():
            clean_text += char
    result = {}
    for letter in clean_text:
        if letter not in result:
            result[letter] = 1
        else:
            result[letter] += 1
    max_count = 0
    most_frequent_char = None
    for key, value in result.items():
        if value >  max_count:
            max_count = value
            most_frequent_char = key
    return result,most_frequent_char
dict_output, winner = return_most("banana")
print("Dictionary:", dict_output)
print("Winner:", winner)