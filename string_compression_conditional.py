def compress_string(text):
    if not text:
        return ''

    count = 1
    result = ''

    for i in range(len(text) - 1):
        if text[i] == text[i+1]:
            count += 1

        else:
            result += text[i] + str(count)
            count = 1

    result += text[-1] + str(count)

    if len(result) < len(text):
        return result

    return text
print(compress_string("aaabbcccc"))

