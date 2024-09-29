fruits = ["apple", "banana", "cherry"]
# print(fruits)

fruits.append("grape")
# print(fruits)

fruits.insert(1, "mango")
# print(fruits)

fruits.insert(10, "lemon") # we use index that bigger than a length of list
# print(fruits)

fruits.remove("apple")
# print("orange" in fruits) # checks if item in list
# fruits.remove("orange") # ValueError: list.remove(x): x not in list
# print(fruits)

# last_fruit = fruits.pop(20) # IndexError: pop index out of range
last_fruit = fruits.pop(0) # default is a last element
# print(fruits)
# print(last_fruit)

length = len(fruits)
# print(length)

names = ["Benny", "benny", "Rachel"]
names.sort()
print(names)
numbers = [3, 1, 4, 1, 5]
print(numbers)
# numbers.sort()
# print(numbers)  # [1, 1, 3, 4, 5]
numbers.sort(reverse=True)
print(numbers)  # [5, 4, 3, 1, 1]
# numbers.reverse()
# print(numbers)  # [5, 4, 3, 1, 1]
# print(numbers[::-1])  # [5, 4, 3, 1, 1]
without_duplications = set(numbers)
print(without_duplications)
print(list(without_duplications))