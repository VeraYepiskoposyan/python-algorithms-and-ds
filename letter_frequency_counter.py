def count_letters(text):
    count = {}
    text = text.lower()
    clean_text = ""
    for char in text:
        if char.isalpha():
            clean_text += char

    for letter in clean_text:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count

print(count_letters("Aa! Bb c."))

