numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "hello", 3.14, True]

# print(mixed_list[0] + 1)
# print(type(mixed_list[0]))
# print(type(mixed_list[1]))
# print(mixed_list[1] + 1)

first_item = fruits[0]  # "apple"

last_item = fruits[-1]  # "cherry"

# print(fruits)
fruits[1] = "orange"
# print(fruits)  # ["apple", "orange", "cherry"]


fruits = ["apple", "banana", "cherry", "orange"]
sliced_fruits = fruits[1:3]
print(sliced_fruits)

# Slicing from the beginning up to index 2
first_two = fruits[:2]
print(first_two)

# Slicing from index 2 to the end
last_two = fruits[2:]
print(last_two)

print(fruits[::-1])

# print(type("abc")) # checking what a type like str or list etc
# print(type([])) # checking what a type like str or list etc
# print(isinstance("abc", str)) # checking if belongs to class like str or list etc
# print(isinstance([], list)) # checking if belongs to class like str or list etc