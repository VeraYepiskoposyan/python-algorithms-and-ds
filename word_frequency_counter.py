def count_word(text):
    count = {}
    text = text.lower()
    clean_text = ""
    for char in text:
        if char.isalpha() or char == " ":
            clean_text += char
    for word in clean_text.split():
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

print(count_word("Hello, word, arab, hello"))
