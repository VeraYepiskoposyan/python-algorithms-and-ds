def is_anagrama(text1,text2):
    if len(text1) != len(text2):
        return False

    count1 = {}
    count2 = {}

    for letter in text1:
        count1[letter] = count1.get(letter,0) + 1
    for letter in text2:
        count2[letter] = count2.get(letter,0) + 1

    return count1 == count2
print(is_anagrama("listen","silent"))
