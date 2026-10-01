def what_is_missing_number(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] > 1:
            return numbers[i] + 1
    return None

print(what_is_missing_number([1,2,3,4,6,7,8]))

# def find_missing_number_math(numbers):
#     # The list goes up to 8, but it's missing one, so n should be len + 1
#     n = len(numbers) + 1
#
#     expected_sum = (n * (n + 1)) // 2
#     actual_sum = sum(numbers)
#
#     return expected_sum - actual_sum

# def find_missing_binary_search(numbers):
#     left = 0
#     right = len(numbers) - 1
#
#     # Keep cutting the search area in half
#     while left <= right:
#         mid = (left + right) // 2
#
#         # Is the left half okay?
#         if numbers[mid] == mid + 1:
#             # Everything on the left is fine, look in the right half
#             left = mid + 1
#         else:
#             # Something is wrong on the left side, narrow down here
#             right = mid - 1
#
#     # The left pointer will land exactly on what the missing number SHOULD be
#     return left + 1
#
#
# # Test Case
# numbers = [1, 2, 3, 4, 6, 7, 8]
# print(find_missing_binary_search(numbers))
# # Output: 5