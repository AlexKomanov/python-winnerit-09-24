# for i in range(5):
#     print(i)

# for i in range(2, 6):
#     print(i)

# for i in range(1, 12, 2):
#     print(i)

# for i in range(10, -1, -1):
#     print(i)

fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    if fruits[i] == "cherry":
        print(fruits[i])

for fruit in fruits:
    if fruit == "banana":
        print("Done")


print(list(range(5)))
print(range(5))