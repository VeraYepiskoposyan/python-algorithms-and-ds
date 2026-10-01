def reverse_words(text):
    reversed_word = []
    word = text.split()
    for i in range(len(word) -1, -1, -1):
        reversed_word.append(word[i])

    return " ".join(reversed_word)
print(reverse_words("I love Python"))
