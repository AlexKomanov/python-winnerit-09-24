user_input = input("Enter a string: ")

print("First character:", user_input[0])

print("Last character:", user_input[-1])

middle_index = len(user_input) // 2
print("Middle character:", user_input[middle_index])

print("Even index characters:", user_input[::2])

print("Odd index characters:", user_input[1::2])

print("Reversed string:", user_input[::-1])