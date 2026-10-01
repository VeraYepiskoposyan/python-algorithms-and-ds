def is_valid_parentheses(text):
    if not text:
        return False

    my_stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for item in text:
        if item in "([{":
            my_stack.append(item)

        elif item in ")]}":
            if not my_stack:
                return False

            popped_element = my_stack.pop()

            if popped_element != pairs[item]:
                return False

    return len(my_stack) == 0

print(is_valid_parentheses("()[]{}"))
print(is_valid_parentheses("(]"))
print(is_valid_parentheses("([{}])"))




