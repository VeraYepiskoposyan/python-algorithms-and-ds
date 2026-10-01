def extract_numbers(text):
    if not text:
        return None
    result = []
    for word in text.split():
        if word.isdigit():
            result.append(int(word))
    return result
print(extract_numbers("I have 12 apples and 45 oranges."))
