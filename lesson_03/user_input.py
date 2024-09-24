# number_1 = int(input("Enter first number: "))
# number_2 = float(input("Enter second number: "))
#
# print(number_1)
# print(type(number_1))
# print(number_2)
# print(type(number_2))
# print(number_2 + number_1)

# name = input("Your name: ")
# age = int(input("Your age: "))
#
# final_output = f"Name: {name} \nAge: {age + 1}"
# print(final_output)
# print(type(final_output))

# num_1, num_2 = input("Enter numbers: ").split(",")
# num_1_int = int(num_1)
# num_2_int = int(num_2)
# print(num_1_int, type(num_1_int))
# print(num_2_int, type(num_2_int))

# num_2 = input("Enter numbers: ").split(",")
# print(num_2, type(num_2))

# list_of_strings = input("enter: ").split()
# print(list_of_strings, type(list_of_strings))
# list_of_unclear = map(int, list_of_strings)
# print(list_of_unclear, type(list_of_unclear))
# final_list = list(list_of_unclear)
# print(final_list, type(final_list))

list_of_strings = input("enter: ").split()
num1, num2, num3 = map(int, list_of_strings)
print(num1)
print(num2, type(num2))
print(num3)
