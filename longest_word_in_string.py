def longest_word(text):
    clean_text = ""
    longest = ""
    max_len = 0
    for char in text:
        if char.isalpha() or char == " ":
            clean_text += char
    for word in clean_text.split():
        if len(word) > max_len:
            max_len = len(word)
            longest = word
    return longest
print(longest_word("I love machine learning"))


