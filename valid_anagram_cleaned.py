def is_anagram(text1, text2):

    count1 = {}
    count2 = {}

    clean_text1 = ''
    for letter in text1.lower():
        if letter.isalpha():
            clean_text1 += letter

    clean_text2 = ''
    for letter in text2.lower():
        if letter.isalpha():
            clean_text2 += letter

    if len(clean_text1) != len(clean_text2):
        return False

    for letter in clean_text1:
        count1[letter] = count1.get(letter, 0) + 1

    for letter in clean_text2:
        count2[letter] = count2.get(letter, 0) + 1


    return count1 == count2

print(is_anagram("hello", "world"))




