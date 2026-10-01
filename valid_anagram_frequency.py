def is_anagram(text, text1):
    count = {}
    count1 = {}
    text = text.lower()
    text1 = text1.lower()
    for char in text:
        if char.isalpha() or char == " ":
            count[char] = count.get(char, 0) + 1
    for char1 in text1:
        if char1.isalpha() or char1 == " ":
            count1[char1] = count1.get(char1, 0) + 1

    return count == count1

print(is_anagram("apple", "paper"))

