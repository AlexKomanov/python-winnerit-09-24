numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)


#By using a regular function
# def take_square(num):
#     return num ** 2
#
# squared_numbers = map(take_square, numbers)