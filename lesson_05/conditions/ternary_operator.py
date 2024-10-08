num = 6

result_of = ""

if num % 2 == 0:
    result_of = "Even"
else:
    result_of = "Odd"

print(result_of)

result = "Even" if num % 2 == 0 else "Odd"
print(result)

x, y = 10, 20
max_value = x if x > y else y
print(max_value)

# print("Even") if num % 2 == 0 else print("Odd")


# like if-elif-else statement
number = 0
if number > 0:
    print("Positive number")
elif number == 0: # like else if() in Java
    print("Zero number")
else:
    print("Negative number")

res = "Positive number" if number > 0 else "Zero number" if number == 0 else "Negative number"

print(res)
