def is_palindrome(text):
    if not text:
        return False
    left = 0
    right = len(text) - 1

    while left <= right:
        if text[left] != text[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

print(is_palindrome("racecar"))