def is_palindrome(text):
    text = text.lower()
    clean_text = ""
    for char in text:
        if char.isalpha():
            clean_text += char
    left = 0
    right = len(clean_text) - 1
    while(left < right):
        if clean_text[left] != clean_text[right]:
            return False
        else:
            left += 1
            right -= 1
    return True
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("hello"))