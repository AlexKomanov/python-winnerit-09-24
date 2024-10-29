# Syntax:
# new_list = [expression for item in iterable if condition]

# Using a regular function
# numbers = [1, 2, 3, 4, 5]
# numbers_squares = []
# for number in numbers:
#     numbers_squares.append(number ** 2)
# print(f"{numbers_squares = }")
#
# # Using map function
# numbers = [1, 2, 3, 4, 5]
# numbers_squares = list(map(lambda x: x ** 2, numbers))
# print(f"Lambda + Map: {numbers_squares}")  # Output: [1, 4, 9, 16, 25]
#
# # Using List Comprehension
# numbers = [1, 2, 3, 4, 5]
# #       [expression for item in iterable if condition]
# squares = [x ** 2 for x in numbers]
# print(f"List Comprehension: {squares}")  # Output: [1, 4, 9, 16, 25]

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # Output [2, 4, 6]
#
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)  # Output [2, 4, 6]


# words = ["hello", "world", "python"]
# uppercased = [word.upper() for word in words]
# print(uppercased)  # Output ['HELLO', 'WORLD', 'PYTHON']

# If condition - filtering
numbers = [-10, -5, 0, 5, 10, 15]
positive_numbers = [x for x in numbers if x > 0]
print(positive_numbers)  # פלט: [5, 10, 15]

# If Else condition - manipulation
numbers = [1, 2, 3, 4, 5, 6]
modified_numbers = [x * 2 if x % 2 == 0 else None for x in numbers]

# If without Else -> triggers error: # SyntaxError: expected 'else' after 'if' expression
# modified_numbers = [x * 2 if x % 2 == 0 for x in numbers]

print(modified_numbers)  # Output [None, 4, None, 8, None, 12]